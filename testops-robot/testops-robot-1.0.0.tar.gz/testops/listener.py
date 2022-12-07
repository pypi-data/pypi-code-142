import logging
import json
import urllib3
import os

from testops_commons import ReportLifecycle, TestSuite, generate_unique_value, Metadata, TestResult, Error
from testops_commons.helper import helper
from testops_commons.core import constants
from testops_commons.model import Apis, RequestMethod, STRING_EMPTY
from .testops_helper.helper import create_testsuite, get_status

from urllib3 import PoolManager
from urllib3.exceptions import InsecureRequestWarning

logger = logging.getLogger(__name__)


def log_internal_error():
    logger.info(msg="An error has occurred in testops-robot plugin.")


class Listener:
    ROBOT_LISTENER_API_VERSION = 2

    def __create_running_test_run(self):
        self.__http.request(RequestMethod.POST, self.server_url + Apis.UPDATE_RUNNING_TEST_RUN.format(project_id = self.project_id),
            body= json.dumps({
                "sessionId": self.session_id,
                "testSuiteId": STRING_EMPTY
            }),
            headers= self.__auth_headers
        )


    def __update_test_case_info(self, test_suite, test_case, status):
        self.__http.request(RequestMethod.POST, self.server_url + Apis.UPDATE_RUNNING_TEST_RUN.format(project_id = self.project_id),
            body= json.dumps({
                "sessionId": self.session_id,
                "testSuiteId": test_suite,
                "name": test_case,
                "status": status
            }),
            headers= self.__auth_headers
        )

    def __init_env(self):
        self.project_id = self.report_lifecycle.report_uploader.configuration.project_id
        self.session_id = self.metadata.sessionId
        self.api_key = self.report_lifecycle.report_uploader.configuration.api_key
        self.server_url = self.report_lifecycle.report_uploader.configuration.server_url
        self.baseline_collection_id = self.report_lifecycle.report_uploader.configuration.baseline_collection_id
        self.__auth_headers = helper.get_api_auth_headers(self.api_key)
        if self.session_id is not None:
            os.environ[constants.TESTOPS_SESSION_ID_ENV] = self.session_id
        if self.project_id is not None:
            os.environ[constants.TESTOPS_PROJECT_ID_ENV] = str(self.project_id)
        if self.api_key is not None:
            os.environ[constants.TESTOPS_API_KEY_ENV] = self.api_key
        if self.server_url is not None:
            os.environ[constants.TESTOPS_SERVER_URL_ENV] = self.server_url
        if self.baseline_collection_id is not None:
            os.environ[constants.TESTOPS_BASELINE_COLLECTION_ID_ENV] = str(self.baseline_collection_id)

    def __init__(self, auto_report = True):
        self.auto_report = auto_report
        self.__http = PoolManager(1, cert_reqs="CERT_NONE")
        urllib3.disable_warnings(InsecureRequestWarning) # Suppress SSL warning

        self.current_testsuite: TestSuite = None
        self.report_lifecycle: ReportLifecycle = ReportLifecycle()
        """ Start the test """
        self.report_lifecycle.start_execution()

        self.metadata = Metadata("robot", "python", "N/A", STRING_EMPTY, STRING_EMPTY)
        self.metadata.sessionId = helper.generate_unique_value()
        self.report_lifecycle.write_metadata(self.metadata)

        self.__init_env()
        self.__create_running_test_run()

    def start_suite(self, name, attrs):
        ts = create_testsuite(name)
        self.report_lifecycle.start_suite(ts, generate_unique_value())
        self.current_testsuite = ts

    def end_suite(self, name, attrs):
        self.report_lifecycle.stop_test_suite(self.current_testsuite.uuid)

    def start_test(self, name, attrs):
        self.report_lifecycle.start_testcase()

    def end_test(self, name, attrs):
        self.report_lifecycle.stop_testcase(self.create_testresult(name, attrs["status"], attrs["message"]))
        if self.auto_report:
            self.__update_test_case_info(self.current_testsuite.name, name, get_status(attrs["status"]))

    def close(self):
        """ End the test """
        try:
            logger.info(msg="Processing test result...")
            self.report_lifecycle.stop_execution()
            self.report_lifecycle.write_test_results_report()
            self.report_lifecycle.write_test_suites_report()
            self.report_lifecycle.write_execution_report()
            self.report_lifecycle.reset()
            logger.info(msg="Uploading report to TestOps...")
            self.report_lifecycle.upload()
        except Exception:
            log_internal_error()

    def create_testresult(self, name, status, message) -> TestResult:
        tr = TestResult()
        tr.uuid = generate_unique_value()
        tr.name = name
        tr.suiteName = self.current_testsuite.name
        tr.parentUuid = self.current_testsuite.uuid
        tr.status = get_status(status)
        tr.errors.append(Error(message, message))
        return tr

