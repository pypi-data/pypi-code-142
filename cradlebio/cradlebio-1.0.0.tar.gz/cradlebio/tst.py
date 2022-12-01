import cradlebio.alphafold
from cradlebio import auth
from cradlebio.alphafold import Alphafold, Sequence

if __name__ == '__main__':
    cradlebio.alphafold.FIRESTORE_PREFIX = 'dev-'

    credentials = auth.authorize(safe_creds_file="/Users/ena/cradle/client/tests/cradlebio/data/test_creds.json")
    folder = Alphafold(credentials)

    monomer_sequences = Sequence.from_dict(
        {i: seq for i, seq in enumerate(
            [
                "SKAVKYYTLEEIQKHNNSKSTWLILHYKVYDLTKFLEEHPGGEEVLREQAGGDATENFEDVGHSTDARELSKTFIIGELHPDDRSKITKPSES",
                "MTYKLILNGKTLKGETTTEAVDIATAADVFAQYAADNGVKGEWTADEATKTFTVTE",
                "KDTIALVVSTLNNPFFVSLKDGAQKEADKLGYNLVVLDSQNNPAKELANVQDLTVRGTKILLINPTDSDAVGNAVKMANQANIPVITLDRQATKGEVVSHIASDNVLGGKIAGDYIAKKAGEGAKVIELQGIAGTSAARERGEGFQQAVAAHKFNVLASQPADFDRIKGLNVMQNLLTAHPDVQAVFAQNDEMALGALRALQTAGKSDVMVVGFDGTPDGEKAVNDGKLAATIAQLPDQIGAKGVETADKVLKGEKVQAKYPVDLKLVVKQ"])
         }
    )

    monomers = folder.predict(
        sequences=monomer_sequences,
        show_progress=True,
        block=True,
        use_cache=False)
