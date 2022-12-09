from gravity_auto_exit.main import AutoExit

if __name__ == '__main__':
    inst = AutoExit(  # 'http://172.16.6.176',
        'http://127.0.0.1',
        'admin',
        'Assa+123',
        debug=True,
        cam_port=83,
        resize_photo=()
    )
    # inst.set_post_request_url('http://127.0.0.1:8080/start_auto_exit')
    inst.try_recognise_plate()
    inst.start()
