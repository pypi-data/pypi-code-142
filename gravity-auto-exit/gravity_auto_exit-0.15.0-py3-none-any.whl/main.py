import datetime
import logging
import threading
import time
import uuid
from cad.main import CAD
from whikoperator.main import Wpicoperator
import requests
import io
from PIL import Image
from gravity_auto_exit import settings as s
from gravity_auto_exit.logger import logger
import os


class AutoExit:
    def __init__(self, cam_host, cam_login, cam_password,
                 auth_method='Digest', engine_callback=None,
                 reload_time=15, debug=False,
                 detection_amount=4, failed_callback=None,
                 fail_callback_react_amount=3, fail_reload_time=1.5,
                 active=True, resize_photo=False, cam_port=80):
        self.cad = CAD(host=cam_host, port=cam_port, login=cam_login,
                       password=cam_password,
                       callback_func=self.cad_callback_func,
                       delay_time=0,
                       logger=logger)
        cam_ip = cam_host.replace('http://', '')
        cam_ip = f"{cam_ip}:{cam_port}"
        self.reload_time = reload_time
        self.active = active
        self.resize_photo = resize_photo
        self.fail_callback_react_amount = fail_callback_react_amount
        self.fail_reload_time = fail_reload_time
        self.cam = Wpicoperator(cam_ip=cam_ip,
                                cam_login=cam_login,
                                cam_pass=cam_password,
                                auth_method=auth_method)
        self.callback_request_url = None
        self.debug = debug
        self.count = 0
        self.fail_count = 0
        self.detection_amount = detection_amount
        self.last_take = datetime.datetime.now()
        self.failed_callback = failed_callback
        threading.Thread(target=self.counter_checker).start()
        self.engine_callback = engine_callback
        logger.info('AUTO_EXIT has started successfully')

    def set_active(self, activity_bool: bool):
        self.active = activity_bool

    def start(self):
        self.cad.mainloop()

    def cut_photo(self, photo, size):
        if not size:
            return photo
        img = Image.open(io.BytesIO(photo))
        # left, upper, right, lower
        im_r = img.crop(size)
        img_byte_arr = io.BytesIO()
        im_r.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()
        return img_byte_arr

    def save_pic(self, pic_name, pic_body, frmt='.jpg'):
        logger.debug(f'Saving picture {pic_name}')
        with open(pic_name + frmt, 'wb') as fobj:
            fobj.write(pic_body)
        logger.debug("Success!")

    def cad_callback_func(self, data):
        if not self.active:
            logging.debug("It is not active")
            return
        self.count += 1
        logger.debug(f'self.count: {self.count}')
        if self.count >= self.detection_amount and datetime.datetime.now() - self.last_take > datetime.timedelta(
                seconds=self.reload_time):
            logger.debug(f'Working')
            result = self.camera_and_recognise()
            if result:
                self.last_take = datetime.datetime.now()
                self.count = 0
                self.fail_count = 0
                return result
            else:
                self.fail_count += 1
                logger.debug(f'Неудачное считывание! {self.fail_count}')
                if not self.fail_count >= self.fail_callback_react_amount:
                    time.sleep(self.fail_count + self.fail_reload_time)
        if self.fail_count >= self.fail_callback_react_amount and self.failed_callback:
            logger.warning('Неудачное считывание!')
            self.failed_callback()

    def camera_and_recognise(self):
        result = self.try_recognise_plate()
        if result:
            if self.engine_callback:
                self.engine_callback(result)
            if self.callback_request_url:
                self.http_callback(number=result)
        return result

    def http_callback(self, number):
        requests.post(self.callback_request_url,
                      params={'number': number})

    def try_recognise_plate(self):
        logger.debug(f'Taking photo...')
        photo = self.cam.take_shot()
        logger.debug(f'Cutting photo...')
        cut_photo = self.cut_photo(photo, self.resize_photo)
        if self.debug:
            photo_name = str(uuid.uuid4())
            cut_pic_name = photo_name + '-2'
            photo_name = os.path.join(s.pics_dir, photo_name)
            cut_pic_name = os.path.join(s.pics_dir, cut_pic_name)
            logger.debug('Saving original')
            self.save_pic(photo_name, photo)
            logger.debug('Saving cut pic')
            self.save_pic(cut_pic_name, cut_photo)
        # Отправляю запрос
        logger.debug(f'Sending request...')
        response = self.get_state_number(
            url='https://dispatcher.ml.neuro-vision.tech/1.4/predict/'
                'car_plate_gpu',
            photo=cut_photo,
            login='admin',
            password='admin'
        )
        logger.debug(f'Get response: {response.json()}')
        number = self.parse_recognition_result(response.json())
        logger.debug(f'Parsing result: {number}')
        return number

    def get_state_number(self, url, photo, login, password):
        response = requests.post(
            url,
            files={'images': ('image.jpg', photo, 'image/jpeg')},
            auth=(login, password))
        return response

    def parse_recognition_result(self, response):
        if response['results'][0]['status'] == 'Success':
            return response['results'][0]['plate']

    def set_post_request_url(self, url):
        self.callback_request_url = url
        return url

    def counter_checker(self):
        count_time = datetime.datetime.now()
        count_now = self.count
        while True:
            if self.count != count_now:
                logger.debug('Abort checker internal counter')
                count_now = self.count
                count_time = datetime.datetime.now()
            if count_now != 0 and self.count == count_now and (
                    datetime.datetime.now() - count_time > datetime.timedelta(
                seconds=5)):
                logger.debug('Abort self.count')
                self.count = 0
                self.fail_count = 0
            time.sleep(1)


if __name__ == '__main__':
    inst = AutoExit(  # 'http://172.16.6.176',
        'http://127.0.0.1',
        'admin',
        'Assa+123',
        debug=True,
        cam_port=82,
    )
    # inst.set_post_request_url('http://127.0.0.1:8080/start_auto_exit')
    # inst.try_recognise_plate()
    inst.start()
