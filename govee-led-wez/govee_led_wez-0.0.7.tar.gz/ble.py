import asyncio
from uuid import UUID
from typing import Union, List
from bleak import BleakScanner, BleakClient, AdvertisementData, BLEDevice
from govee_led_wez import GoveeController, GoveeColor

GOVEE_MFR = [34817, 34818]

DESK_STRIP = "4D:C6:A4:C1:38:E1:DA:AC"
GLIDE = "03:F7:D7:37:32:34:0C:6F"
LAMP2 = "23:B7:CF:34:38:39:35:29"
LAMP1 = "89:94:C2:34:38:39:34:11"

GOVEE_SVC = UUID("00010203-0405-0607-0809-0a0b0c0d1910")
GOVEE_CHR = UUID("00010203-0405-0607-0809-0a0b0c0d2b11")

async def main():
    # await discover_govee_ble()

    controller = GoveeController()
    try:
        def device_changed(device):
            print(device.device_id, device.model, device.ble_device)

        controller.set_device_change_callback(device_changed)
        controller.set_http_api_key("817fe6f2-f244-4dd8-8d6a-23f490a25b36")
        #await controller.query_http_devices()
        controller.start_lan_poller()
        await controller.query_ble_devices()

        lamp = None
        while not lamp:
            lamp = controller.get_device_by_id(LAMP1)
            if lamp and lamp.ble_device:
                break;
            print("waiting for lamp to show up")
            await asyncio.sleep(1)

        print("Doing control now")
        #await controller.set_power_state(lamp, False)
        #await asyncio.sleep(3)
        #await controller.set_brightness(lamp, 50)
        #await asyncio.sleep(3)
        #await controller.set_brightness(lamp, 100)
        await controller.set_color(lamp, GoveeColor(255, 0, 0))
        await asyncio.sleep(2)
        await controller.set_color_temperature(lamp, 9000)
        await asyncio.sleep(2)
        await controller.set_color_temperature(lamp, 2000)
        # await power(DESK_STRIP, False)

    finally:
        await controller.async_stop()

asyncio.run(main())
