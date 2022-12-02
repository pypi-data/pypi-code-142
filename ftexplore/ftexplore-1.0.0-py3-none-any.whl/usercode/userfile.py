#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import os
import sys
import traceback

from .ftinterface import InterruptRequestedException
from .. import module


logger = logging.getLogger(__name__);


class UserFile(module.Module):
    '''Prepares and controls execution of a Python file provided by the user'''

    _filename = None # the filename of the file with the user code
    _flatvars = False # whether variable can be accessed without prefixing "ft." in user code
    _ft = None # the interface to the devices

    def __init__(self, ft, flatvars=True):
        '''Constructor'''
        self._flatvars = flatvars
        self._ft = ft

    @property
    def filename(self):
        return self._filename
        
    @filename.setter
    def filename(self, value):
        self._filename = value

    def get_bytecode(self):
        '''Accesses the code file and compiles it to bytecode'''
        if not os.access(self._filename, os.R_OK):
            logger.warning('Python file [{name}] does not exist or cannot be read'.format(name=self._filename))
            return None
        try:
            data = open(self._filename, encoding='UTF-8').read()
            data = data.lstrip('\ufeff') # remove BOM
            return compile(data, self._filename, 'exec')
        except Exception as e:
            #logger.exception('Exception when compiling [{name}]: {e}'.format(name=self._filename, e=e))
            text = 'Exception when compiling user code: {e}'.format(e=e)
            logger.info(text)
            trace = traceback.format_exc(limit=0)
            text = '\n' + text + '\n' + trace + '\n'
            self.enqueue_event('on_usercode_output_requested', text=text) # provide information on this exception
            return None

    def run(self):
        '''Run the user code'''
        code = self.get_bytecode()
        if code is None:
            return;
        global ft
        ft = self._ft
        if self._flatvars:
            global analog, input, motor
            analog = ft.analog
            input = ft.input
            motor = ft.motor
            global analog1, analog2
            analog1 = ft.analog1
            analog2 = ft.analog2
            global input1, input2, input3, input4, input5, input6, input7, input8
            input1 = ft.input1
            input2 = ft.input2
            input3 = ft.input3
            input4 = ft.input4
            input5 = ft.input5
            input6 = ft.input6
            input7 = ft.input7
            input8 = ft.input8
            global motor1, motor2, motor3, motor4
            motor1 = ft.motor1
            motor2 = ft.motor2
            motor3 = ft.motor3
            motor4 = ft.motor4
            global sleep, write
            sleep = ft.sleep
            write = ft.write
        try:
            exec(code)
        except SystemExit:
            # Ignore exit() call in user code
            logger.debug('User code requested exit')
        except InterruptRequestedException as e:
            logger.debug('User code terminated as requested')
            text = '\n' + str(e) + '\n'
            self.enqueue_event('on_usercode_output_requested', text=text) # provide information on this exception
            self.enqueue_event('on_alloff_requested') # make sure that all motors are stopped in this exception scenario
        except Exception as e:
            # Catch all the exceptions in the user code
            tb = sys.exc_info()[2]
            trace = traceback.format_tb(tb)
            tb = traceback.extract_tb(tb)[-1]
            text = 'Exception in user code [{name}] in line {line} in method "{method}": {e}'.format(name=tb[0], line=tb[1], method=tb[2], e=e)
            logger.info(text)
            text = '\n' + text + '\nTraceback (most recent call last):\n' + ''.join(trace) + '\n'
            self.enqueue_event('on_usercode_output_requested', text=text) # provide information on this exception
            self.enqueue_event('on_alloff_requested') # make sure that all motors are stopped in this exception scenario


if __name__ == '__main__':
    userfile = UserFile(None, False)
    userfile.filename = 'example.py'
    userfile.run()
