"""Client library for folding proteins using Cradle's implementation of Alphafold.

Example:

    ::

        from concurrent.futures import as_completed

        from cradlebio import auth
        from cradlebio.alphafold import Alphafold

        credentials = auth.authorize()
        client = Alphafold(credentials)

        job = client.predict_from_file(
            fasta_file='/Users/ena/cradle/client/tests/cradlebio/data/monomer/0.fasta',
            job_id='demo')

        for folded_structure_future in as_completed(s.folded() for s in job.structures()):
            folded_structure = folded_structure_future.result()
            print(f'\\nName: {folded_structure.name}\\n'
                  f'Scores: {folded_structure.to_dict()["ptms"]}')

See Also:
    - :meth:`Alphafold.create_job <cradlebio.alphafold.Alphafold.create_job()>`
    - :meth:`Alphafold.predict_from_file <cradlebio.alphafold.Alphafold.predict_from_file()>`
"""
import concurrent
import time
import uuid
from concurrent.futures import Future
from dataclasses import dataclass
from datetime import datetime
import json
import logging
import hashlib
from pathlib import Path
from typing import Dict, List, Union, Optional, Iterator, Tuple
import sys

import fsspec
import google.cloud.exceptions
from Bio import SeqIO
from fsspec.core import OpenFile
from google.api_core.exceptions import PermissionDenied, AlreadyExists
from google.cloud import firestore
from proto.datetime_helpers import DatetimeWithNanoseconds

from cradlebio import auth
from cradlebio import watch
from cradlebio.auth import IdentityPlatformTokenCredentials
from cradlebio.watch import add_progress_listener

CRADLE_GCS_BUCKET = 'cradle-bio.appspot.com'
JOBS = 'jobs'  # the name of the sub-collection where jobs are stored in Firebase
STRUCTURES = 'sequences'  # name of the sub-collection within jobs where structures are stored TODO: backend name align
FIRESTORE_PREFIX = ''
DONE_JOB_STATUS = frozenset(('DONE', 'MSA_FAILED', 'FOLDING_FAILED'))
ENSEMBLE_LENGTH = 5


class MsaException(Exception):
    """Indicator class for a server-side error during Multiple Sequence Alignment (MSA)"""
    pass


class PdbException(Exception):
    """Indicator class for a server-side error during sequence folding"""
    pass


@dataclass
class Sequence:
    """
    An amino acid sequence

    Args:
        aas: amino acid sequence
        id: the id of this sequence, used to fetch MSA results for multimers
    """
    aas: str
    id: str = f'autoid-{uuid.uuid4()}'

    def to_fasta(self) -> str:
        return f'>{"autoid" if self.id.startswith("autoid") else self.id}\n{self.aas}'

    def __len__(self):
        return len(self.aas)

    def __repr__(self):
        return self.aas


@dataclass
class AlignmentResult:
    """
    A wrapper class encapsulating the results of a multi-sequence alignment run

    Args:
        path: The Google Cloud Storage path for the multiple sequence alignment file.

    """
    path: str
    creds: IdentityPlatformTokenCredentials

    @property
    def a3m(self) -> OpenFile:
        """

        A reference to a requested .a3m file produced by an alignment run.

        Note this is a reference, and the file will not actually be opened until used in a context manager, e.g::

            with alignment_result.a3m as f:
                alignment_file = Bio.AlignIO.parse(f, 'fasta')

        This reference is not serializable, so if you need to store the location for later use,
        use ``alignment_result.path``.

        """
        with auth.fsspec_creds(self.creds):
            return fsspec.open(self.path, mode='rt')

    def to_file(self, filename: str):
        """

           Saves the .a3m file produced by an alignment run to a file.
           Args:
               filename: the name for the resulting file

        """
        with self.a3m as f:
            Path(filename).write_text(f.read())


@dataclass
class FoldResult:
    path: str
    creds: IdentityPlatformTokenCredentials

    """
    Args:
        path: A serializable reference to a requested PDB file.
    """

    @property
    def pdb(self) -> OpenFile:
        """

        An OpenFile instance pointing to the contents of the 3D protein structure in PDB format.

        Note this is a reference, and the file will not actually be opened until used in a context manager, e.g::

            with protein.pdb() as f:
                struct = Bio.PDB.PDBParser.PDBParser().get_structure('my_structure_tag', f)

        See Also: :meth:`FoldResult.path <cradlebio.alphafold.FoldResult.path>`

        Returns:
            an ``OpenFile`` object if it is available.


        """
        with auth.fsspec_creds(self.creds):
            return fsspec.open(self.path, mode='rt')

    def to_file(self, filename: str):
        """
           Saves the resulting PDB file to a local file.
           Args:
               filename: the name for the local file to save the results to
        """
        with self.pdb as f:
            Path(filename).write_text(f.read())


class Structure:
    """A protein that is being folded by AlphaFold.

    This object is immutable and represents the state of folding at the moment of object creation.

    To get an updated copy run::

        structure: Structure = structure.update()

    Some functions will only return values after significant computation such as ``structure.alignment_result()`` or
    ``structure.fold_result()``. For these functions, the convenience methods ``aligned()`` and ``folded()`` will
    return a ``Future`` the result of which is a copy of the ``Structure`` object where those fields are guaranteed
    to be available.

    Examples:
        Print out structure IDs and scores::

            from concurrent.futures import as_completed

            from cradlebio import auth
            from cradlebio.alphafold import Alphafold

            credentials = auth.authorize()
            client = Alphafold(credentials)

            with client.create_job(
                    job_id='test job',
                    relax=False,
                    show_progress=False) as job:
                job.predict(Sequence('CAMPER'), name='camper')
                job.predict(Sequence('VAN'), name='van')

            print('Waiting for structures to fold...')
            for folded_structure_future in as_completed(s.folded() for s in job.structures()):
                folded_structure = folded_structure_future.result()
                print(f'Name: {folded_structure.name}\\n'
                      f'Scores: {folded_structure.to_dict()["ptms"]}')

        Or launch followup computation once each sequence has completed::

            def my_callback(folded_structure_future: 'Future[Sequence]'):
                folded_structure = folded_structure_future.result()
                # Do stuff
                ...

            for structure in job.structures():
                structure.folded().add_done_callback(my_callback)

        See `concurrent.futures` for full details on how to use these objects.
    """

    def __init__(self, snapshot: firestore.DocumentSnapshot):
        self._snapshot = snapshot

    def __str__(self) -> str:
        return f'Id: {self.id}\n{json.dumps(self.to_dict(), indent=4)}'

    @property
    def snapshot(self) -> firestore.DocumentSnapshot:
        return self._snapshot

    @property
    def id(self) -> str:
        return self.snapshot.id

    @property
    def name(self) -> str:
        return self.snapshot.get('name')

    @property
    def sequence(self) -> Sequence:
        """
        Returns:
            The amino acid sequence for the protein that is being folded

        Raises:
             ``ValueError`` if the protein is a multimer (since a multimer has multiple sequences)
        """
        sequences = self.sequences
        if len(sequences) > 1:
            raise ValueError('The sequence property is ambiguous for multimer ``Structures`` use sequences')

        return self.sequences[0]

    @property
    def sequences(self) -> Tuple[Sequence]:
        """
        Returns:
            This ``Structure``'s amino acid sequences.
            For simple proteins (monomers) the returned result will have a single element,
            identical to the sequence returned by the ``sequence`` property.
        """
        sequences_ = self.snapshot.get('seq')
        chain_ids = self.snapshot.get('chain_ids')

        if isinstance(sequences_, str):
            assert isinstance(chain_ids, str)
            return Sequence(sequences_, id=chain_ids),

        return tuple(Sequence(sequence, id=id_) for sequence, id_ in zip(sequences_, chain_ids))

    @property
    def is_multimer(self) -> bool:
        return len(self.sequences) > 1

    def _sequence_to_alignment_id(self, sequence_id):
        aas = tuple(sequence.aas for sequence in self.sequences)
        return aas.index(aas[tuple(s.id for s in self.sequences).index(sequence_id)])

    def update(self) -> 'Structure':
        """
        Since the ``Structure`` object is immutable, to get an updated version of the ``Structure`` as it undergoes
        folding use this method.

        Returns:
             An updated version of the ``Structure`` object

        """
        return Structure(self.snapshot.reference.get())

    def to_dict(self) -> Dict:
        """
        Fetch all information about this `Structure` in Dict format.
        """
        return self.snapshot.to_dict()

    def job(self) -> 'Job':
        """
        Returns:
             the job this ``Structure`` belongs to
        """
        return Job(self._snapshot.reference.parent.parent)

    def _aligned_callback(self, document: firestore.DocumentSnapshot) -> Optional['Structure']:
        result = document.to_dict()
        status = result.get('status')

        if status == 'FOLDING_FAILED':
            # folding failed and no msa means scheduling error
            error = result.get('a3m_error', 'Unknown error during scheduling')
            logging.error(f'Error during scheduling for {self.name}: {error}')
            raise PdbException(error)

        elif status not in {'MSA_COMPLETE', 'MSA_FAILED'}:
            # already aligned and moved forward in the pipeline
            if status != 'MSA_RUNNING' and 'a3m' in result:
                return Structure(document)

            # hasn't completed
            return

        if status == 'MSA_FAILED':
            error = result.get('a3m_error', 'Unknown error during alignment')
            logging.error(f'Error during alignment for {self.name}: {error}')
            raise MsaException(error)

        if 'a3m' not in result or (self.is_multimer and 'a3m_paired' not in result):
            error = 'Missing output'
            logging.error(f'Error during alignment for {self.name}: {error}')
            raise MsaException('Missing output')

        return Structure(document)

    def aligned(self) -> 'Future[Structure]':
        """
        Returns:
            a Future object, the successful ``result()`` of which returns a copy of the current ``Structure``.
            The ``alignment_result()`` method of the returned ``Structure`` object is guaranteed to return an
            ``AlignmentResult`` object.

            In case of alignment failure, the ``result()`` method of the returned Future object raises ``MsaException``.

        See Also:
            - :meth:`Structure.alignment_result <cradlebio.alphafold.Structure.alignment_result()>`
            - :meth:`AlignmentResult <cradlebio.alphafold.AlignmentResult>`
        """
        return watch.callback_future(
            doc=self._snapshot.reference,
            callback=self._aligned_callback)

    def alignment_result(self, paired: bool = False, sequence_id: Optional[str] = None) -> Optional[AlignmentResult]:
        """
        Returns:
            either an ``AlignmentResult`` object or None depending on whether the ``Structure`` has been successfully
            aligned.

        Notes: Alignments for complex proteins (multimers) result in multiple files, one paired and one unpaired .a3m
                file for each sequence.

        Args:
            paired: **relevant only for multimer alignment results** whether to fetch the path to a paired sequence
                alignment (as opposed to a regular sequence-wise multiple sequence alignment) file.
                Learn more about paired alignments `here <https://www.biorxiv.org/content/10.1101/2021.08.15.456425v2.full>`_.
            sequence_id: **required for multimer alignment results**, references the required ``Sequence`` within the
                multimer

        See Also:
            - :meth:`Structure.aligned <cradlebio.alphafold.Structure.aligned()>`
            - :meth:`AlignmentResult <cradlebio.alphafold.AlignmentResult>`
            - :meth:`Structure.sequences <cradlebio.alphafold.Structure.sequences>`
            - :meth:`Sequence <cradlebio.alphafold.Sequence>`

        """
        result = self.to_dict()
        if 'a3m' not in result:
            return

        if self.is_multimer and sequence_id is None:
            raise ValueError('Must provide a sequence id to fetch multimer results, see `Structure.sequences`')

        if paired and not self.is_multimer:
            raise ValueError('Pair alignment only exists for multimers')

        path = result['a3m_paired'] if paired else result['a3m']

        if sequence_id is not None:
            alignment_id = self._sequence_to_alignment_id(sequence_id)
            if alignment_id is None:
                raise ValueError('Unrecognized alignment id')
            path = path[alignment_id]
        else:
            path = path[0]

        assert isinstance(path, str), path

        return AlignmentResult(
            path=f'gs://{Path(CRADLE_GCS_BUCKET) / result["gcs_path"] / path}',
            creds=self._snapshot._client._credentials)

    def _folded_callback(self, document: firestore.DocumentSnapshot) -> Optional['Structure']:
        result = document.to_dict()
        status = result.get('status')
        if status not in {'DONE', 'MSA_FAILED', 'FOLDING_FAILED'}:
            return

        if status == 'MSA_FAILED':
            error = result.get('a3m_error', 'Unknown error during alignment')
            logging.error(f'Error during alignment for {self.name}: {error}')
            raise MsaException(error)

        if status == 'FOLDING_FAILED':
            logging.error(status)
            error = result.get('pdb_error', 'Unknown error during folding')
            logging.error(f'Error folding {self.name}: {error}')
            raise PdbException(error)

        if 'pdbs_unrelaxed' not in result:
            error = result.get('pdb_error', 'Missing output')
            logging.error(f'Error folding {self.name}: {error}')
            raise PdbException(error)

        return Structure(document)

    def folded(self) -> 'Future[Structure]':
        """
        Returns:
            a Future object, the successful ``result()`` of which returns a copy of the current ``Structure``.
            The ``fold_result()`` method of the returned ``Structure`` object is guaranteed to return an
            ``FoldResult`` object.

            In case of alignment or folding failure, the ``result()`` method of the returned Future object raises
            an ``MsaException`` or ``PdbException`` respectively.

        See Also:
            - :meth:`Structure.fold_result <cradlebio.alphafold.Structure.fold_result()>`
            - :meth:`FoldResult <cradlebio.alphafold.FoldResult>`
        """
        return watch.callback_future(self._snapshot.reference, self._folded_callback)

    def fold_result(self, relaxed: bool = True, rank: int = 0) -> Optional[FoldResult]:
        """

        Args:
            relaxed: whether to fetch the results pre- or post- Amber relaxation
            rank: the rank of the ensemble model whose results to fetch, since there are 5 models in the ensemble the \
                  ranks range from 0 to 4, 0 being the best performing model in the ensemble

        Raises:
            `ValueError`:

                - `relaxed=True` but relaxation was not requested for the structure
                - `rank` is invalid (should be an integer between 0 and 4)

            `IndexError`: an error occurred during folding and the resulting files were not produced

        Returns:
            either a ``FoldResult`` object or None depending on whether the ``Structure`` has been successfully
            folded.

        See Also:
            - :meth:`FoldResult <cradlebio.alphafold.FoldResult>`
            - :meth:`Structure.fold_result <cradlebio.alphafold.Structure.fold_result()>`
        """
        result = self.to_dict()
        if 'pdbs_unrelaxed' not in result:
            return

        relaxed_paths = result['pdbs']
        if relaxed and len(relaxed_paths) == 0:
            raise ValueError('Requested relaxed pdb paths from a structure that wasn\'t relaxed. '
                             'See `Job.predict` or `Alphafold.predict` for setting the `relax` parameter.')

        if ENSEMBLE_LENGTH - 1 < rank < 0:
            raise ValueError(f'Rank should be an integer between 0 and {ENSEMBLE_LENGTH - 1}, got {rank}.')

        path_suffix = (relaxed_paths if relaxed else result['pdbs_unrelaxed'])[rank]

        return FoldResult(
            path=f'gs://{Path(CRADLE_GCS_BUCKET) / result["gcs_path"] / path_suffix}',
            creds=self._snapshot._client._credentials)


class Job:
    """
    A conceptually grouped set of structures to fold.

    Examples:
        ::

            from cradlebio import auth
            from cradlebio.alphafold import Alphafold

            credentials = auth.authorize()
            client = Alphafold(credentials)

            with client.create_job('test_job', multimer=True) as job:
                job.predict(Sequence('GRAND'), Sequence('CANYQN'))
                job.predict(Sequence('LAVA'), Sequence('LAMP'))

                # The job starts only after exiting the context
                assert not job.started

            assert job.started

    See Also:
        to access the job's results see:
         - :meth:`Job.wait <cradlebio.alphafold.Job.wait()>`
         - :meth:`Job.structures <cradlebio.alphafold.Job.structures()>`
         - :meth:`Structure <cradlebio.alphafold.Structure>`
    """

    def __init__(self,
                 doc: firestore.DocumentReference,
                 use_cache: bool = True,
                 relax: bool = True,
                 show_progress: bool = True,
                 multimer: bool = False):
        self._doc = doc
        self.use_cache = use_cache
        self.show_progress = show_progress
        self.relax = relax
        self._batch = None
        self.unique_sequences = set()
        self.multimer = multimer

    @property
    def id(self) -> str:
        return self._doc.id

    @property
    def md5_sum(self) -> str:
        return self._doc.get(['md5_sum']).get('md5_sum')

    @property
    def creation_time(self) -> DatetimeWithNanoseconds:
        return self._doc.get().create_time

    @property
    def last_update_time(self) -> DatetimeWithNanoseconds:
        return self._doc.get().update_time

    @property
    def started(self) -> bool:
        try:
            snapshot = self._doc.get()
            return snapshot.exists
        except google.cloud.exceptions.NotFound:
            return False

    def to_dict(self) -> Dict:
        """Fetch all information about this `Job` object in Dict format"""
        return self._doc.get().to_dict()

    def structures(self) -> Iterator[Structure]:
        """
        Returns: all the structures within this job.
        """
        for struct_snap in self._doc.collection(STRUCTURES).stream():
            yield Structure(struct_snap)

    def wait(self,
             aligned_only: bool = False,
             timeout: Optional[int] = None,
             return_when: str = concurrent.futures.ALL_COMPLETED):
        """
        Wait (blocking) for the results of the ``Job`` at various stages of completion.

        Args:
            aligned_only:  wait until all the structures within this job have been aligned (as opposed to folded)
            timeout: wait for timeout seconds (or indefinitely if None)
            return_when: one of

                - ``concurrent.futures.FIRST_COMPLETED``
                - ``concurrent.futures.FIRST_EXCEPTION``
                - ``concurrent.futures.ALL_COMPLETED``

        Returns:
            a named tuple (``done``, ``not_done``) of sets of ``Futures`` (if ``timeout=None`` the ``.not_done``
            set will be empty).

        Examples:

            ::

                from cradlebio import auth
                from cradlebio.alphafold import Alphafold, Sequence

                credentials = auth.authorize()
                client = Alphafold(credentials)

                with client.create_job(
                        job_id='wait_test_job',
                        relax=False,
                        show_progress=False) as job:
                    job.predict(Sequence('REDUCE'), name='reduce')
                    job.predict(Sequence('FRACKING'), name='fracking')

                result = job.wait(aligned_only=True, timeout=60)
                for aligned_future in result.done:
                    structure = aligned_future.result()
                    print(f'Successfully aligned {structure.name} within 60 seconds')
                    print(f'The alignment results can be found at: `{structure.alignment_result().path()}`')

                if len(result.not_done) > 0:
                    print('Some structures were not aligned within the selected timeframe')

        """
        if aligned_only:
            futures = tuple(structure.aligned() for structure in self.structures())
        else:
            futures = tuple(structure.folded() for structure in self.structures())

        return concurrent.futures.wait(futures, timeout=timeout, return_when=return_when)

    def predict(self, *sequences: Union[Sequence, str], name: str = '') -> Structure:
        """
        Adds a structure to this folding ``Job``.

        Args:
            *sequences: a list of Sequence objects which contains amino acid sequences to fold into a
                        single structure. For simple proteins (monomers), the sequences parameter consists of a
                        single Sequence instance
            name: a name for the ``Structure``, empty by default

        Returns:
            A ``Structure`` object which can be used to get the resulting fold.

        See Also:
            :meth:`Sequence <cradlebio.alphafold.Sequence>`

        """
        if self._batch is None:
            raise RuntimeError('Can only call `job.predict` inside a context')

        if self._struct_count >= 50:
            raise ValueError('Too many structures, a job should contain at maximum 50 structures')

        if not (self.multimer ^ (len(sequences) < 2)):
            raise ValueError(f'A job shouldn\'t mix monomer and multimer structures, '
                             f'got multimer={self.multimer}, with {len(sequences)} sequence(s).')

        if sum(len(sequence) for sequence in sequences) > 1400:
            raise ValueError(f'Structure {name} is too long, must be shorter than 1400 AAs')

        sequences = [Sequence(s) if isinstance(s, str) else s for s in sequences]

        fasta_str = '\n'.join([sequence.to_fasta() for sequence in sequences])
        logging.debug(f'Making job with sequences:\n {fasta_str}')
        self._hash.update(fasta_str.encode('utf-8'))
        if self.relax:
            self._hash.update('relax'.encode('utf-8'))

        # TODO: denormalize this backend struct to allow for easier per chain metadata
        chain_ids, seqs = zip(*((sequence.id, str(sequence.aas)) for sequence in sequences))
        if len(sequences) == 1:
            chain_ids = chain_ids[0]
            seqs = seqs[0]

        if ':'.join(seqs) in self.unique_sequences:
            raise RuntimeError(f'Structure {name} is a duplicate, sequences: {sequences}')
        else:
            self.unique_sequences.add(':'.join(seqs))

        data = {
            'name': name,
            'status': 'PENDING',
            'creation_time': datetime.now(),
            'chain_ids': chain_ids,
            'seq': seqs
        }

        struct_doc: firestore.DocumentReference = self._doc.collection(STRUCTURES).document(
            str(self._struct_count).rjust(2, '0'))
        self._batch.create(struct_doc, data)
        self._struct_count += 1
        return Structure(firestore.DocumentSnapshot(struct_doc,
                                                    data,
                                                    exists=False,
                                                    read_time=None,
                                                    create_time=None,
                                                    update_time=None))

    def __enter__(self):
        if self.started:
            raise RuntimeError(f'Cannot start new job, job with id {self._doc.id} '
                               'already started. Give job a new unique ID.')
        self._batch = firestore.WriteBatch(self._doc._client)
        self._batch.create(self._doc, {})
        self._hash = hashlib.md5()
        self._struct_count = 0
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            if exc_type is not None:
                # Don't commit if we had an exception in the context block. Just reraise.
                # Note it should be safe to restart here.
                return False

            hash_digest = self._hash.hexdigest()

            identical_jobs = self._doc.parent.where('md5sum', '==', hash_digest).get()
            if self.use_cache and identical_jobs:
                self._doc = next(iter(identical_jobs)).reference
                logging.info(f'Found job {self._doc.id} with the same hash. Using existing ref.')
            else:
                self._batch.update(
                    self._doc,
                    {
                        'status': 'PENDING',
                        'md5sum': hash_digest,
                        'creation_time': datetime.now(),
                        'sequence_count': self._struct_count,  # Backend name align
                        'relax': 'ALL' if self.relax else 'NONE',
                    })
                self._batch.commit()

            if self.show_progress:
                add_progress_listener(self._doc)
                self.wait()
                time.sleep(5)  # wait for the progress bar to wrap-up todo: remove

        finally:
            # Always unset flag that allows us to predict
            self._batch = None


def _predict_file(fasta_file: Path, job: Job, multimer: bool = False):
    for record in SeqIO.parse(fasta_file, format='fasta'):
        if multimer:
            sequences = [Sequence(str(seq), id=f'{record.id}_{i}') for i, seq in enumerate(record.seq.split(':'))]
        else:
            sequences = [Sequence(str(record.seq), id=record.id)]
        job.predict(*sequences, name=record.name)


class Alphafold:
    """ Main entry point for folding proteins. """

    def __init__(self, creds: auth.IdentityPlatformTokenCredentials):
        self.creds = creds
        self.client = auth.get_client(creds)

        self.user_doc = self.client.document(f'{FIRESTORE_PREFIX}users/{self.creds.uid}')
        self._current_job = None
        try:
            self.user_doc.create({})
        except PermissionDenied:
            print('Access to Cradle Alphafold is only permitted for trusted testers. Please sign up at '
                  'https://cradlebio.typeform.com/to/lEzf6l1E if you would like to try Cradle Alphafold.')
            sys.exit(1)
        except AlreadyExists:
            pass

    def create_job(self,
                   job_id: str = None,
                   use_cache: bool = True,
                   relax: bool = True,
                   show_progress: bool = True,
                   multimer: bool = False) -> Job:
        """
        Create a ``Job`` instance for folding a set of conceptually similar structures

        Args:
            job_id: a unique identifier for that job (can be used to fetch the job, see ``Alphafold.get_job_by_id()``
            use_cache: if `True` and an identical previously started job exists, reuse that job
            relax: whether to perform AmberRelaxation on the resulting PDB files
            show_progress: whether to show a progress bar
            multimer: whether the job wraps multimer sequences

        Returns:
            a ``Job`` instance. To start the job enter its context and add sequences to it within the context.
            After exiting the context the job will start.

        See Also:
             :meth:`Job <cradlebio.alphafold.Job>`
        """
        return Job(self.user_doc.collection(JOBS).document(job_id),
                   use_cache=use_cache,
                   relax=relax,
                   show_progress=show_progress,
                   multimer=multimer)

    def predict(self,
                *sequences: Union[Sequence, str],
                job_id: str = None,
                structure_name: str = '',
                use_cache: bool = True,
                relax: bool = True,
                show_progress: bool = True) -> Structure:
        """
        Convenience method for creating and starting a job that folds a single structure.
        Typically, the ``sequences`` parameter contains a single sequence, unless the folded protein is a multimer.

        Args:
            *sequences: sequences of the structure to predict (only one for monomers)
            job_id: the id of the folding job to create
            structure_name: the name for the single ``Structure`` within this ``Job``
            use_cache: if `True` and an identical previously started job exists, reuse that job
            relax: whether to perform AmberRelaxation on the resulting PDB files
            show_progress: whether to show a progress bar

        Returns:
            a folding ``Structure``

        See Also:
             - :meth:`Structure <cradlebio.alphafold.Structure>`
             - :meth:`Alphafold.create_job <cradlebio.alphafold.Alphafold.create_job()>` - for multiple-structure jobs
             - :meth:`Job <cradlebio.alphafold.Job>`

        Examples:
            ::

                from cradlebio import auth
                from cradlebio.alphafold import Alphafold, Sequence

                credentials = auth.authorize()
                client = Alphafold(credentials)

                # start a folding job
                structure = client.predict(Sequence('CLARINET'),
                                           job_id='example',
                                           relax=False)

                # wait for the structure to be folded
                structure: Structure = structure.folded().result()

                # analyse the results
                with structure.fold_result().pdb(relaxed=False) as f:
                    print(f'The predicted 3D structure in PDB format is:' or something similar: \\n'
                          f'`{f.read()}`')
        """
        with self.create_job(job_id,
                             use_cache=use_cache,
                             relax=relax,
                             show_progress=show_progress,
                             multimer=len(sequences) > 1) as job:
            job.predict(*sequences, name=structure_name)
        return next(job.structures())

    def predict_from_file(self,
                          fasta_file: Union[str, Path],
                          job_id: Optional[str] = None,
                          use_cache: bool = True,
                          relax: bool = True,
                          show_progress: bool = True,
                          multimer: bool = False) -> Job:
        """
        Start a folding ``Job`` directly from a FASTA file.

        Args:
            fasta_file: a path to the fasta file
            job_id: the id of the folding job to create, if not provided defaults to filename + creation time
            use_cache: if `True`, if an identical previously started job exists, reuse that job
            relax: whether to perform AmberRelaxation on the resulting PDB files
            show_progress: whether to show a progress bar
            multimer: whether the FASTA file contains multimers, if that is the case write the entire complex in a
                single line separated by a colon `:` and make sure all the sequences within that FASTA file represent
                multimers

        Returns:
            the created ``Job``

        Examples:

            Example FASTA files:

                monomers::

                    > first structure
                    CAMPER
                    > second structure
                    VAN
                    ...

                multimers::

                    > first structure
                    CENTRAL:PARK
                    > second structure
                    MARVEL:SPIDERMAN:CAPE
                    ...

        """
        fasta_file = Path(fasta_file)
        with self.create_job(
                job_id or f'{fasta_file.name}@{datetime.now().isoformat()}',
                use_cache=use_cache,
                relax=relax,
                show_progress=show_progress,
                multimer=multimer,
        ) as job:
            _predict_file(fasta_file, job=job, multimer=multimer)

        return job

    def predict_from_directory(self,
                               path: Union[str, Path],
                               job_id: str = None,
                               use_cache: bool = True,
                               relax: bool = True,
                               show_progress: bool = True,
                               multimer: bool = False) -> Job:
        """

        Start a folding ``Job`` from all FASTA files in a given directory.

        Args:
            path: a path to the directory containing the FASTA files
            job_id: the id of the folding job to create, if not provided defaults to filename + creation time
            use_cache: if `True`, if an identical previously started job exists, reuse that job
            relax: whether to perform AmberRelaxation on the resulting PDB files
            show_progress: whether to show a progress bar
            multimer: whether the FASTA file represents a multimer, if that is the case write the entire complex in a \
            single line separated by a colon

        Returns:
            the created ``Job``

        See Also:
            :meth:`Alphafold.predict_from_file <cradlebio.alphafold.Alphafold.predict_from_file()>`
        """
        path = Path(path)
        if not path.is_dir():
            raise ValueError(f'Expected a path to a directory, got {path}')

        with self.create_job(
                job_id or f'{path.name}@{datetime.now().isoformat()}',
                use_cache=use_cache,
                relax=relax,
                show_progress=show_progress,
                multimer=multimer,
        ) as job:
            for file in path.iterdir():
                if file.suffix not in {'.fasta', '.faa', '.fa'}:
                    pass
                _predict_file(file, job=job, multimer=multimer)
        return job

    def get_jobs(self, active_only=True) -> List[Job]:
        """
        Args:
            active_only: if `True`, returns only ``Jobs`` that are currently running

        Returns:
            a list of alphafold ``Jobs`` for the current user. Jobs are returned ordered by creation time, starting with
            the most recent one
        """
        jobs_collection = self.user_doc.collection(JOBS)
        if active_only:
            jobs_collection = jobs_collection.where('status', 'not-in', DONE_JOB_STATUS)

        jobs = [Job(job.reference) for job in jobs_collection.stream()]
        jobs.sort(key=lambda job: job.creation_time, reverse=True)
        return jobs

    def get_job_by_id(self, job_id: str) -> Optional[Job]:
        """

        Args:
            job_id: the id of the ``Job`` to retrieve

        Returns:
            the required ``Job`` instance or None if it doesn't exist

        """
        job_doc = self.client.document(f'{FIRESTORE_PREFIX}users/{self.creds.uid}/{JOBS}/{job_id}').get()
        if job_doc.exists:
            return Job(job_doc.reference)
        return None

    def search_jobs(self, keyword: str, active_only=True) -> List[Job]:
        """
        Search all ``Jobs`` that match the given keyword.

        Args:
            keyword: (sub) `string` to search for in one of the following ``Job`` fields:

                - ``status``, one of: ``PENDING``, ``MSA_QUEUE``, ``MSA_RUNNING``, ``MSA_COMPLETE``, ``MSA_FAILED``, \
                    ``FOLD_QUEUE``, ``FOLDING``, ``DONE``, ``FOLDING_FAILED``.
                - ``id`` (see ``Alphafold.create_job``)
                - ``md5_sum`` (see ``Job.md5_sum``)
                - ``creation_time``,  should be given as YY-MM-DD.

            active_only: if `True`, only jobs that are currently active are returned

        Examples:

            ::

                # search by id
                jobs = client.search_jobs('my first job')

                # search by creation time
                jobs = client.search_jobs('2022-12-1')
                jobs = client.search_jobs('2022')

                # search by status
                jobs = client.search_jobs('PENDING')
        """
        jobs: List[Job] = self.get_jobs(active_only)
        if not keyword:
            return jobs

        result = []
        for job in jobs:
            data = job.to_dict()
            for s in map(str, [job.id, *[data[k] for k in {'status', 'md5sum', 'creation_time'}]]):
                if keyword in s:
                    result.append(job)
                    break
        return result
