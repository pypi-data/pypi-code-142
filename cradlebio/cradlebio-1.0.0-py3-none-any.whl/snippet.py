
from concurrent.futures import as_completed

from cradlebio import auth
from cradlebio.alphafold import Alphafold

credentials = auth.authorize()
client = Alphafold(credentials)

job = client.predict_from_file(
    fasta_file='/Users/ena/cradle/client/tests/cradlebio/data/monomer/0.fasta',
    job_id='demoo')

for folded_structure_future in as_completed(s.folded() for s in job.structures()):
    folded_structure = folded_structure_future.result()
    # print(f'\nName: {folded_structure.name}\n'
    #       f'Scores: {folded_structure.to_dict()["ptms"]}')

from tests.cradlebio.conftest import recursive_delete
import time
time.sleep(5)
recursive_delete(job._doc)
