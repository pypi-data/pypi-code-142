try:
    from pynut_3ftp.pyNutFtp import nutFtp as ftp
except:
    try:
        from pyNutFtp import nutFtp as ftp
    except:
        print('Online Test...')
        from pyNut import pyNutFtp as ftp

import pytest


# python -m pytest test/test_nutFtp.py



#=============================================================================
# UNIT TEST
#=============================================================================







