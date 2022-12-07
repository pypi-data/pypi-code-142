
from testops_commons import TestSuite, Status


class TestSuiteStatus:
    PASS = "PASS"
    FAIL = "FAIL"
    SKIP = "SKIP"


def create_testsuite(name) -> TestSuite:
    ts = TestSuite()
    ts.name = name
    return ts


def get_status(status):
    if status == TestSuiteStatus.PASS:
        return Status.PASSED
    if status == TestSuiteStatus.FAIL:
        return Status.FAILED
    if status == TestSuiteStatus.SKIP:
        return Status.SKIPPED
    return Status.INCOMPLETE

