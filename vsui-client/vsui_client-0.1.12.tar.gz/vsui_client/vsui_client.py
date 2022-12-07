import socketio
from typing import Any
import logging
from matplotlib import pyplot as plt
import io
import sys
import base64
import atexit

sio = socketio.Client()
task_id = None
# target log for where intercepted logs should be forwarded to
logging_target = None
timeout_target = 5

timeout_count = 0

def encode_image(arr,
title: str = '',
format : str = 'jpg',
figsize: tuple = (8, 8),
cmap: str = "gray"):
    fig = plt.figure(figsize=figsize)
    plt.imshow(arr, cmap=cmap)
    plt.suptitle(title, fontsize=16)
    my_stringIObytes = io.BytesIO()
    plt.savefig(my_stringIObytes, format=format)
    my_stringIObytes.seek(0)
    my_base64_jpgData = base64.b64encode(my_stringIObytes.read()).decode()
    plt.close()
    return my_base64_jpgData

def exit_handler():
    logging.info('VSUI exit handler triggered')
    disconnect()
                    
# https://stackoverflow.com/a/51981833
def vsui_process():
    def decorator(func):
        def wrapper(*args, **kwargs):
            r = None
            atexit.register(exit_handler)
            r = func(*args, **kwargs)
            return r
        return wrapper
    return decorator

def safe_emit(event, data):
    ''' emit a socketio event with exception handling '''
    try:
        sio.emit(event, data)
    except Exception as e:
        logging.warning(e)
        pass

def connect(HOST : str = 'localhost', PORT : str = '8000') -> None:
    ''' initiate a socketio session with a server '''
    sio.connect('http://' + HOST + ':' + PORT, headers={'type':'app', 'id': task_id})
    print(f'sid is {sio.sid}')

def disconnect() -> None:
    ''' disconnect the socketio session '''
    sio.disconnect()
    print('socket disconnected')

# struct: { 'name' : 'type' }
# send a new task to be added to the server's task manager
def set_task_id(id : str) -> None:
    ''' set the id of this task '''
    global task_id
    task_id = id

def set_logging_target(key: str) -> None:
    global logging_target
    logging_target = {'element_key' : key}

# edit one of the elements in the task, this allows data updating
def edit_element(element_uid : str, value : Any) -> None:
    ''' Edit the target display element, images must be base 64 encoded '''
    safe_emit('edit_element', {'task_id' : task_id, 'element_key' : element_uid, 'value' : value})

# mark the task as completed
def deactivate_task() -> None:
    ''' deactivate the current task '''
    safe_emit('deactivate_task', task_id)

def notify(txt : str, type : str) -> None:
    ''' send a popup to the client '''
    safe_emit('notify', {'txt':txt, 'type':type})

def logging_intercept(msg) -> None:
    ''' forward logs to the target display element '''
    if logging_target is not None:
        edit_element(logging_target['element_key'],msg)
    else:
        logging.error('No logging target set.')

# http://naoko.github.io/intercept-python-logging/
class RequestHandler(logging.Handler):
    def emit(self, record):
        ''' Intercept logs '''
        logging_intercept(record.getMessage())
