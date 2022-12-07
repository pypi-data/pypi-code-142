
#python3 -m unittest

import unittest
from InCli import InCli
#from InCli.SFAPI import restClient

class Test_Main(unittest.TestCase):

    def test_q(self):
        InCli.main(["-u","uormaechea.devnoscat2@nos.pt","-q", "select fields(all) from Order limit 1"])

    def test_o(self):
        InCli.main(["-u","uormaechea.devnoscat2@nos.pt","-o"])

    def test_o_name(self):
        InCli.main(["-u","uormaechea.devnoscat2@nos.pt","-o","-name","order"])

    def test_o_like(self):
        InCli.main(["-u","uormaechea.devnoscat2@nos.pt","-o","-like","XOM"])

    def test_h(self):
        InCli.main(["-h"])

    def test_check_Catalog(self):
        InCli.main(["-u","NOSDEV","-checkCatalogs"])

    def test_logs(self):
        InCli.main(["-u","NOSDEV","-logs"])

    def test_log_ls(self):
        InCli.main(["-u","NOSDEV","-logs:ls"])

    def test_log_ID(self):
        InCli.main(["-u","NOSDEV","-logs","07L3O00000DajQIUAZ"])

    def test_log_last(self):
        InCli.main(["-u","NOSDEV","-logs","-last","10"])

    def test_default(self):
        InCli.main(["-default:set","u"])
        InCli.main(["-default:set","u","NOSDEV"])
        InCli.main(["-default:get","u"])        
        InCli.main(["-logs","-last","1"])
        InCli.main(["-default:del","u"])

    def test_d(self):
        InCli.main(["-u","NOSDEV","-d"])
        InCli.main(["-u","NOSDEV","-d","Order"])
        InCli.main(["-u","NOSDEV","-d","Order:Status"])

    def test_l(self):
        InCli.main(["-u","NOSDEV","-l"])
        InCli.main(["-u","DEVNOSCAT2","-l"])