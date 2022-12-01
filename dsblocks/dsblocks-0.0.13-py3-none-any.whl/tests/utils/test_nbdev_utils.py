# AUTOGENERATED! DO NOT EDIT! File to edit: ../../../nbs/00_tests/utils/tst.nbdev_utils.ipynb.

# %% auto 0
__all__ = ['sh_imported', 'example_people_data', 'myf', 'my_first_test', 'second_fails', 'third_fails', 'create_fake_tests',
           'test_test_runner', 'test_test_runner_two_tests', 'test_test_runner_two_targets', 'test_cd_root',
           'test_nbdev_build_test']

# %% ../../../nbs/00_tests/utils/tst.nbdev_utils.ipynb 2
from dsblocks.utils.nbdev_utils import *

# %% ../../../nbs/00_tests/utils/tst.nbdev_utils.ipynb 3
import pytest
import os
#try:
#    import sh
#    sh_imported = True
#except ImportError:
#    sh_imported = False
import joblib
from IPython.display import display

from dsblocks.utils.utils import remove_previous_results
sh_imported = False

# %% ../../../nbs/00_tests/utils/tst.nbdev_utils.ipynb 4
def example_people_data():
    return 5

def myf (x):
    return x*2

def my_first_test (example_people_data):
    print ('first passes')
    assert myf (example_people_data) == 10

def second_fails ():
    print ('second fails')
    assert False
    
def third_fails ():
    print ('third fails')
    assert False

# %% ../../../nbs/00_tests/utils/tst.nbdev_utils.ipynb 5
def create_fake_tests ():
    os.makedirs ('mylibrary/mytests/first', exist_ok=True)
    os.makedirs ('mylibrary/mytests/second', exist_ok=True)
    f = open ('mylibrary/mytests/first/mod_a.py','wt')
    f.write ('from ')
    f.write ('...mytests.second.mod_b import b\na=3\nprint(a)')
    f.close()
    f = open ('mylibrary/mytests/second/mod_b.py','wt')
    f.write ('b=4\nprint(b)')
    f.close()
    f = open ('mylibrary/mytests/first/mod_c.py','wt')
    f.write ('from ')
    f.write ('...mytests.first.mod_a import a\nc=5\nprint(c)')
    f.close()
    f = open ('mylibrary/mytests/mod_d.py','wt')
    f.write ('d=6\nprint(d)')
    f.close()

# %% ../../../nbs/00_tests/utils/tst.nbdev_utils.ipynb 6
def test_test_runner ():
    # one test
    tst_ = TestRunner (do_test=None, all_tests=None, load=False)
    tst_.run (my_first_test, example_people_data, True)
    assert tst_.all_tests == ['my_first_test']
    assert os.listdir('config_test')==['test_names.pk']
    
    do_test_, all_tests_, tags_, targets_, remote_targets_, localhostname_ = joblib.load ('config_test/test_names.pk')
    assert all_tests_==['my_first_test']
    assert remote_targets_==['dummy']
    assert tags_=={}


# %% ../../../nbs/00_tests/utils/tst.nbdev_utils.ipynb 7
def test_test_runner_two_tests ():
    tst_ = TestRunner (do_test=None, all_tests=None, targets='dummy', load=False)
    assert tst_.do_test==[]
    assert tst_.all_tests==[]
    tst_.run (my_first_test, example_people_data, tag='dummy')
    tst_.run (second_fails, tag='slow')
    with pytest.raises (AssertionError):
        tst_.run (third_fails, tag='dummy')
    
    assert tst_.all_tests == ['my_first_test', 'second_fails', 'third_fails']
    assert tst_.tags == {'dummy': ['my_first_test', 'third_fails'], 'slow': ['second_fails']}
    assert tst_.targets==['dummy']
    assert tst_.do_test==[]
    
    do_test_, all_tests_, tags_, targets_, remote_targets_, localhostname_ = joblib.load ('config_test/test_names.pk')
    
    assert all_tests_ == ['my_first_test', 'second_fails', 'third_fails']
    assert tags_ == {'dummy': ['my_first_test', 'third_fails'], 'slow': ['second_fails']}
    assert targets_==['dummy']
    assert do_test_==[]
    
    tst_ = TestRunner (do_test=None, all_tests=None, load=True)
    assert tst_.all_tests == ['my_first_test', 'second_fails', 'third_fails']
    
    tst_ = TestRunner (do_test=None, all_tests=None, load=False)
    assert tst_.all_tests == []


# %% ../../../nbs/00_tests/utils/tst.nbdev_utils.ipynb 8
def test_test_runner_two_targets ():
    tst_ = TestRunner (targets=['dummy','slow'], load=False)
    tst_.run (my_first_test, example_people_data, tag='slow')
    tst_.run (second_fails, tag='other')
    with pytest.raises (AssertionError):
        tst_.run (third_fails, tag='dummy')


# %% ../../../nbs/00_tests/utils/tst.nbdev_utils.ipynb 9
def test_cd_root ():
    os.chdir('nbs/utils')
    d = os.listdir ('.')
    assert 'settings.ini' not in d
    cd_root ()
    d = os.listdir ('.')
    assert 'settings.ini' in d


# %% ../../../nbs/00_tests/utils/tst.nbdev_utils.ipynb 10
def test_nbdev_build_test ():
    create_fake_tests ()
    nbdev_build_test (library_name='mylibrary', test_folder='mytests')
    
    # tests
    assert len(os.listdir ('mylibrary'))==0
    assert sorted(os.listdir ('mytests'))==['first', 'mod_d.py', 'second']
    assert sorted(os.listdir ('mytests/first'))==['mod_a.py', 'mod_c.py']
    assert sorted(os.listdir ('mytests/second'))==['mod_b.py']
    
    f = open ('mytests/first/mod_c.py','rt')
    lines = f.readlines ()
    f.close()
    assert lines[0]=='from mylibrary.mytests.first.mod_a import a\n'
    
    f = open ('mytests/first/mod_a.py','rt')
    lines = f.readlines ()
    f.close()
    assert lines[0]=='from mylibrary.mytests.second.mod_b import b\n'
    
    remove_previous_results ('mylibrary')
    remove_previous_results ('mytests')

