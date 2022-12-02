#%%

import api_jama as aj
Test=aj.JamaAPI("trinkler", "Casillas_1", "353")
list=Test.generateTC(MainCompID="12656346")
# %%
Test.delete_TC_set([t for r,t in list])