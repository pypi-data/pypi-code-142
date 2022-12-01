from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

import cradlebio.alphafold
from cradlebio import alphafold
from cradlebio.auth import IdentityPlatformTokenCredentials

firebase_creds = IdentityPlatformTokenCredentials.from_file(
    '/Users/ena/cradle/client/tests/cradlebio/data/test_creds.json'
)
cradlebio.alphafold.FIRESTORE_PREFIX = 'dev-'
cradlebio.alphafold.JOBS = 'jobs'

if __name__ == '__main__':
    af = alphafold.Alphafold(creds=firebase_creds)
    with af.create_job(
            job_id='012345678',
            use_cache=False,
            show_progress=True,
            multimer=True
    ) as job:
        # job.predict(SeqRecord(Seq('SPIDERMAN'), 'spiderman'))
        job.predict(
            SeqRecord(Seq('SPIDERMAN'), 'spiderman'),
            SeqRecord(Seq('CLARINET'), 'clarinet'),
    SeqRecord(Seq('SPIDERMAN'), 'spiderman'),
            SeqRecord(Seq('CLARINET'), 'clarinet'),
    SeqRecord(Seq('SPIDERMAN'), 'spiderman'),
            SeqRecord(Seq('CLARINET'), 'clarinet'),
    SeqRecord(Seq('SPIDERMAN'), 'spiderman'),
            SeqRecord(Seq('CLARINET'), 'clarinet'),
    SeqRecord(Seq('SPIDERMAN'), 'spiderman'),
            SeqRecord(Seq('CLARINET'), 'clarinet'),
    SeqRecord(Seq('SPIDERMAN'), 'spiderman'),
            SeqRecord(Seq('CLARINET'), 'clarinet'),
        )
        # job.predict(SeqRecord(Seq('CLARINET'), 'clarinet'))
        # job.predict(SeqRecord(Seq('CCLARINET'), 'cclarinet'))

    # with af.create_job(
    #         job_id='0multimer',
    #         use_cache=False,
    #         show_progress=True,
    # ) as job:
    #     job.predict(SeqRecord(Seq('SPIDERMAN'), 'spiderman'), SeqRecord(Seq('CLARINET'), 'clarinet'))
