""" Unit tests for the wfengine_remote module """
import uuid
import unittest
from testfixtures import compare
from fireworks.core.launchpad import LaunchPad
from fireworks.fw_config import LAUNCHPAD_LOC
from fireworks.user_objects.queue_adapters.common_adapter import CommonAdapter
from wfgenes.engine.wfengine_remote import WFEngineRemote


QADAPTER_DCT = {
    '_fw_name': 'CommonAdapter',
    '_fw_q_type': 'SLURM',
    'nodes': 1,
    'ntasks': 1,
    'pre_rocket': '. python-3.6.8/bin/activate',
    'queue': 'dev_single',
    'rocket_launch': 'rlaunch singleshot',
    'walltime': '00:01:00'
}


#@unittest.skip(reason="currently skipping remote tests")
class WFEngineRemoteTest(unittest.TestCase):
    """ test the WFEngine class """
    def setUp(self):
        if LAUNCHPAD_LOC:
            self.launchpad = LaunchPad.from_file(LAUNCHPAD_LOC)
        else:
            self.launchpad = LaunchPad()

        self.qadapter = CommonAdapter.from_dict(QADAPTER_DCT)
        self.launchdir = '/home/hk-project-test-sdlmat/th7356/test12'
        self.sleep_time = 60
        self.name = str(uuid.uuid4())
        self.user = 'th7356'
        self.host = 'horeka.scc.kit.edu'
        self.conf = 'module load python/3'
        self.wf_query = {}
        self.wfe = WFEngineRemote(launchpad=self.launchpad, launchdir=self.launchdir,
                                  qadapter=self.qadapter, wf_query=self.wf_query,
                                  host=self.host, user=self.user, conf=self.conf)

    def tearDown(self):
        if self.wfe.thread is not None and self.wfe.thread.is_alive():
            self.wfe.stop()
            self.wfe.thread.join()

    def test_to_dict(self):
        """ test saving to dictionary """
        dict_to_compare = {
            'launchpad': self.launchpad,
            'qadapter': self.qadapter,
            'wf_query': {},
            'name': self.name,
            'launchdir': self.launchdir,
            'sleep_time': self.sleep_time,
            'host': self.host,
            'user': self.user,
            'conf': self.conf
        }
        dict_dumped = self.wfe.to_dict()
        self.assertCountEqual(dict_to_compare, dict_dumped)

    def test_from_dict(self):
        """ test loading from dictionary """
        dump_dict = self.wfe.to_dict()
        obj = WFEngineRemote.from_dict(dump_dict)
        self.assertEqual(type(self.wfe.launchpad), type(obj.launchpad))
        self.assertEqual(type(self.wfe.qadapter), type(obj.qadapter))
        self.assertEqual(self.wfe.launchdir, obj.launchdir)
        self.assertEqual(self.wfe.sleep_time, obj.sleep_time)
        self.assertEqual(type(self.wfe), type(obj))
        compare(self.wfe, obj)

if __name__ == '__main__':         
    unittest.main()
