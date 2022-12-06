import os
import sys
from unittest import TestResult, TestLoader

import click

sys.path.append(os.getcwd())


@click.command()
@click.option('--file', help='test file to run')
@click.option('--folder', help='test folder to run')
def run_test(**kwargs):
    path = os.getcwd() + '/scripts'
    sys.path.append(path)
    test_result = TestResult()

    if kwargs['folder']:
        path = path + '/' + kwargs['folder']

    if kwargs['file']:
        TestLoader().discover(path, kwargs['file']).run(result=test_result)
    else:
        TestLoader().discover(path).run(result=test_result)

    if test_result.wasSuccessful():
        print("Tests run: ", test_result.testsRun)
        exit(0)
    else:
        print(test_result.errors)
        print(test_result.failures)
        exit((-1))


if __name__ == '__main__':
    run_test()
