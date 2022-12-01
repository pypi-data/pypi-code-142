from cradlebio import alphafold, auth

creds = auth.authorize(safe_creds_file='/tmp/creds.json')
client = alphafold.Alphafold(creds)

structure = client.predict(
    alphafold.Sequence("MDPIRSRTPSPARELLPGPQPDRVQPTADRGGAPPAGGPLDGLPARRTMSRTRLPSPPAP"))

structure.alignment_result().to_file('/tmp/golden.a3m')
structure.fold_result().to_file('/tmp/golden.pdb')
