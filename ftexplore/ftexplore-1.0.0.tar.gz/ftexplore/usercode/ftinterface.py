# -*- coding: utf-8 -*-

import logging
import time

from .. import module_caching


logger = logging.getLogger(__name__);


class InterruptRequestedException(Exception):
    '''User-defined exception used to interrupt user code'''
    pass


class Motor(object):
    '''Class providing operations for controlling a numbered motor'''

    callback_func = None # callback function for controlling the motor
    num = None # number of this motor

    def __init__(self, num, callback_func):
        '''Constructor to set member variables based on the provided arguments'''
        self.num = num
        self.callback_func = callback_func
    
    def set(self, speed: int):
        '''Set motor to a new speed'''
        if (speed < -100) or (speed > 100):
            raise ValueError('Speed for motor{num} out of allowed range (-100..100)'.format(num=num))
        self.callback_func(self.num, speed)

    def forward(self):
        '''Set motor to full forward speed'''
        self.set(100)

    def reverse(self):
        '''Set motor to full reverse speed'''
        self.set(-100)

    def on(self):
        '''Set motor to full (forward) speed'''
        self.set(100)

    def off(self):
        '''Switch-off motor'''
        self.set(0)

    def stop(self):
        '''Stop motor immediately'''
        self.set(None)


class FTInterface(module_caching.ModuleCaching):
    '''Interface to motors and sensors made available in user code'''

    _interrupt_requested = None # flag indicating whether user code shall be interrupted or not
    motors = [] # list of objects representing the motors

    def __init__(self, interrupt_requested):
        '''Constructor'''
        super().__init__()
        self.motors = [ Motor(i, self.set_motor) for i in range(4) ]
        self._interrupt_requested = interrupt_requested

    def check_for_interruption_request(self):
        '''Stop execution of user code if requested'''
        if self._interrupt_requested.is_set():
            raise InterruptRequestedException('Code execution interrupted')

    def set_motor(self, num, speed):
        '''Set speed of specified motor (not to be used by user)'''
        self.enqueue_event('on_motor_set_requested', num=num, speed=speed)
        self.check_for_interruption_request()

    def analog(self, num: int):
        '''Provide current value of a analog input'''
        pass # ***
        self.check_for_interruption_request()
        
    def analog1(self):
        return self.analog(1)
    def analog2(self):
        return self.analog(2)

    def input(self, num: int):
        '''Provide current value of a digital input'''
        pass # ***
        self.check_for_interruption_request()
        
    def input1(self):
        return self.input(1)
    def input2(self):
        return self.input(2)
    def input3(self):
        return self.input(3)
    def input4(self):
        return self.input(4)
    def input5(self):
        return self.input(5)
    def input6(self):
        return self.input(6)
    def input7(self):
        return self.input(7)
    def input8(self):
        return self.input(8)

    def motor(self, num: int, speed: int = 9999):
        '''Return a motor object or set the motor's speed (in case a speed is provided)'''
        if (num < 1) or (num > 4):
            raise ValueError('Invalid motor accessed, allowed numbers are 1..4')
        if speed == 9999:
            return self.motors[num-1]
        else:
            self.motors[num-1].set(speed)

    @property
    def motor1(self):
        return self.motors[0]
    @property
    def motor2(self):
        return self.motors[1]
    @property
    def motor3(self):
        return self.motors[2]
    @property
    def motor4(self):
        return self.motors[3]
        
    def sleep(self, sec):
        '''Wait as long as requested in an interruptible manner'''
        millisec = sec * 1000
        # Multiples of 0.1s
        for i in range(millisec // 100):
            time.sleep(0.1)
            self.check_for_interruption_request()
        # Remaining time < 0.1s
        time.sleep(millisec % 100)

    def write(self, text):
        '''Output text'''
        self.enqueue_event('on_usercode_output_requested', text=text)
        self.check_for_interruption_request()
