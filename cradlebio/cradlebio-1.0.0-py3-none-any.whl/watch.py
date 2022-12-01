import logging
import threading
from concurrent.futures import Future
from dataclasses import dataclass
from typing import List, TypeVar, Callable, Tuple, Iterable

import google.cloud.exceptions
from google.cloud import firestore
from google.cloud.firestore_v1.watch import DocumentChange, ChangeType, Watch
from tqdm import tqdm
from proto.datetime_helpers import DatetimeWithNanoseconds

logging.getLogger('google.api_core.bidi').setLevel(level=logging.ERROR)
logging.getLogger('google.cloud.firestore_v1.watch').setLevel(level=logging.WARNING)


def unsubscribe_watch(event, job_watch):
    event.wait()
    job_watch.unsubscribe()


@dataclass
class DocumentProgress:
    document: firestore.DocumentSnapshot

    @property
    def data(self):
        return self.document.to_dict()

    @property
    def status(self):
        return self.document.get('status')

    @property
    def sequence_statuses(self) -> Tuple[str]:
        return tuple(str(seq.get('status')) for seq in self.document.reference.collection('sequences').stream())

    @property
    def description(self):
        if self.status == 'MSA_RUNNING' and 'msa_progress' in self.data:
            return self.data['msa_progress']['status']
        return ' '.join(self.status.split('_'))

    @property
    def current(self):
        if self.status not in {'MSA_RUNNING', 'FOLDING'}:
            return 0 if self.status in {'PENDING', 'MSA_QUEUE', 'FOLD_QUEUE'} else 100

        if self.status == 'MSA_RUNNING':
            if 'msa_progress' not in self.data:
                return 0
            return self.data.get('msa_progress')['current'] * 2  # msa progress goes up to 50

        elif self.status == 'FOLDING':
            data = self.data
            if {'completed_sequences', 'failed_sequences', 'sequence_count'}.issubset(data.keys()):
                completed = data['completed_sequences']
                failed = data['failed_sequences']
                total = data['sequence_count']
            else:
                statuses = self.sequence_statuses
                completed = statuses.count('DONE')
                failed = len(tuple(filter(lambda x: x in {'MSA_FAILED', 'FOLDING_FAILED'}, statuses)))
                total = len(statuses)
            return 100 * ((completed + failed) / total)


def _fetch_progress_bar(snapshot):
    status = snapshot.get('status')
    if status in {'PENDING', 'MSA_QUEUE', 'MSA_RUNNING', 'MSA_COMPLETE'}:
        return tqdm(
            desc='ALIGNING ',
            total=100,
            unit='%', miniters=1, mininterval=0, ncols=110, bar_format='{l_bar}{bar}|[{unit}]')
    elif status in {'FOLD_QUEUE', 'FOLDING'}:
        return tqdm(
            desc='FOLDING ',
            total=100,
            unit='%', miniters=1, mininterval=0, ncols=110, bar_format='{l_bar}{bar}|[{unit}]')


def add_progress_listener(job_doc: firestore.DocumentReference):
    """ Listens to changes on the job document and sequences in firestore and updates a progress bar. """
    snapshot = job_doc.get()
    progress_bar = _fetch_progress_bar(snapshot)

    if progress_bar is None:
        print(f'Job finished with status {snapshot.get("status")}')
        return

    progress_bar.n = DocumentProgress(snapshot).current
    progress_bar.update(0)

    done = threading.Event()
    fold_started = threading.Event()

    def job_callback(docs: List[firestore.DocumentSnapshot],
                     changes: List[DocumentChange],
                     _: DatetimeWithNanoseconds):
        nonlocal progress_bar
        for document, change in zip(docs, changes):
            if change.type != ChangeType.MODIFIED:
                continue

            data = document.to_dict()
            if 'status' not in data:
                continue

            progress = DocumentProgress(document)

            status = data['status']
            prev_unit = progress_bar.unit.strip()
            progress_bar.unit = progress.description.ljust(34)

            if status == 'MSA_COMPLETE' and not fold_started.is_set():
                progress_bar.close()
                progress_bar = tqdm(desc='FOLDING', total=100, unit='STARTING', miniters=1, mininterval=0,
                                    ncols=110, bar_format='{l_bar}{bar}|[{unit}]')
                fold_started.set()
            elif status in {'MSA_FAILED', 'FOLDING_FAILED', 'DONE'}:
                if status == 'DONE':
                    progress_bar.n = 100
                    progress_bar.update(0)
                progress_bar.close()
                done.set()
                continue
            elif status in {'MSA_RUNNING', 'FOLDING'}:
                if 'QUEUE' in prev_unit:
                    progress_bar.update()
                else:
                    progress_bar.n = progress.current
                    progress_bar.update(0)
            else:
                progress_bar.update()

    job_watch = job_doc.on_snapshot(job_callback)
    threading.Thread(target=unsubscribe_watch, args=(done, job_watch)).start()


def add_simple_progress_listener(total: int, structures):
    from concurrent.futures import as_completed
    kwargs = {'ncols': 110, 'bar_format': '{l_bar}{bar}|', 'total': total}

    if all(future.exception(timeout=1) for future in
           tqdm(as_completed(s.aligned() for s in structures), desc='ALIGNING', **kwargs)):
        return

    tuple(tqdm(as_completed(s.folded() for s in structures), desc='FOLDING', **kwargs))


def safe_unsubscribe(watcher: Watch):
    """Start a thread that unsubscribes from the given watcher"""
    # Because unsubscribes are triggered by the watcher thread themselves
    # start a new thread for unsubscribing so that the watcher thread can exit
    threading.Thread(target=watcher.unsubscribe, daemon=True).start()


T = TypeVar('T')


def _handle_snapshot(callback: Callable[[firestore.DocumentSnapshot], T],
                     snapshot: firestore.DocumentSnapshot, future: 'Future[T]'):
    """Propagate results of a callback on a snapshot to a Future"""
    try:
        result = callback(snapshot)
        if result is not None:
            future.set_result(result)
    except Exception as e:
        future.set_exception(e)


def callback_future(
        doc: firestore.DocumentReference,
        callback: Callable[[firestore.DocumentSnapshot], T],
) -> 'Future[T]':
    """
    Return a future that is set by `callback` returning a non-None value in a watcher thread.
    """

    future = Future()
    try:
        initial_snapshot = doc.get()
    except google.cloud.exceptions.NotFound:
        pass
    else:
        _handle_snapshot(callback, initial_snapshot, future)

    def callback_wrapper(docs: List[firestore.DocumentSnapshot],
                         changes: List[DocumentChange],
                         _: DatetimeWithNanoseconds):
        for document, change in zip(docs, changes):
            if change.type in {ChangeType.ADDED, ChangeType.MODIFIED}:
                _handle_snapshot(callback, document, future)

            if change.type in {ChangeType.REMOVED}:
                future.set_exception(
                    RuntimeError(f'Document {document.to_dict()} removed during watch'))

            if future.done():
                return

    if not future.done():
        watcher = doc.on_snapshot(callback_wrapper)
        future.add_done_callback(lambda _: safe_unsubscribe(watcher))

    return future
