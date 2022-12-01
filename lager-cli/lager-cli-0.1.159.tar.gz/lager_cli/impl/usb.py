import sys
import os
import json
import brainstem
from brainstem.result import Result

def is_enabled(val):
    return val & 1 > 0 and val & 2 > 0

def do_list(mappings, stem):
    for key in mappings:
        port = mappings[key]['port']
        result = stem.usb.getPortState(int(port))
        if result.error != Result.NO_ERROR:
            raise RuntimeError(f"Error reading state for device {key}")
        enabled = is_enabled(result.value)
        print(f'Device: {key} enabled: {enabled}')

def do_action(mappings, stem, device_name, action):
    device = mappings[device_name]
    port = int(device['port'])
    if action == 'on':
        stem.usb.setPortEnable(port)
    elif action == 'off':
        stem.usb.setPortDisable(port)
    elif action == 'toggle':
        result = stem.usb.getPortState(int(port))
        enabled = is_enabled(result.value)
        if enabled:
            stem.usb.setPortDisable(port)
        else:
            stem.usb.setPortEnable(port)

def main():
    mappings = json.loads(os.environ['LAGER_USB_MAPPINGS'])
    data = json.loads(sys.argv[1])
    action = data['action']
    device_name = data['device']
    try:
        stem = brainstem.stem.USBHub2x4()
        result = stem.discoverAndConnect(brainstem.link.Spec.USB)
        if result != Result.NO_ERROR:
            raise RuntimeError("No USB hub found")

        if action is None:
            do_list(mappings, stem)
        else:
            do_action(mappings, stem, device_name, action)

    finally:
        stem.disconnect()

if __name__ == '__main__':
    main()
