import requests
import time
from yyweaknet.stf import STFServer


class WeakNetworkConfig(object):
    """
        弱网配置工具类提供以下功能
        1、自动连接/断开弱网wifi
        2、为设备配置弱网配置
    """
    # ios切换网络app bundle_id
    IOS_APP_BUNDLE_ID = "com.yy.net"
    # atc 接口
    ATC_AUTH_URI = "/api/v1/auth/{}/"
    ATC_SHAPE_URI = "/api/v1/shape/{}/"

    def __init__(self, atc_host="http://172.29.182.90:8000", stf_url=None, sft_token=None, wifi_name="yy_net",
                 wifi_password=""):
        """
            :param atc_host: atc服务地址
            :param stf_url: sft服务器地址
            :param sft_token: sft服务token
            :param wifi_name: wifi名称
            :param wifi_password: wifi密码
        """

        self._atc_host = atc_host
        self._wifi_name = wifi_name
        self._wifi_password = wifi_password
        self.device_ip = None
        self.device = None
        self._stf = STFServer(url=stf_url, token=sft_token)
        self.serail = None

    def _get_device_info(self, device_serial, platform='ios'):
        """
            获取当前设备信息
            :param device_serial: 设备serial
            :param platform: ios/android
        """
        self.platform = platform
        if self.device is None:
            self.device = self._stf.get_device_info(device_serial, platform)
        if self.device is None:
            raise Exception('No devices:{} found'.format(device_serial))

    def connect_wifi(self, device_serial, platform='ios'):
        """
            连接弱网WIFI热点
        """
        self.platform = platform
        self.serail = device_serial
        if self.platform == 'ios':
            self._get_device_info(device_serial, platform=platform)
            return self._connect_ios()
        else:
            return self._connect_android()

    def disconnect_wifi(self):
        """
            断开弱网WIFI热点
        """
        if self.platform == 'ios':
            return self._disconnect_ios()
        else:
            return self._disconnect_android()

    def _connect_android(self):
        ret = self._stf.toggleAndroidWifi(self.serail, "1", wifiname=self._wifi_name, wifipass=self._wifi_password)
        ip = ret.get("ip", None)
        if str(ip).startswith("192.168.0"):
            return True
        else:
            return False

    def _connect_ios(self):
        # 发送自动点击弹窗配置
        self._stf.watch_alert(self.device['wda_url'])
        self._stf.stop_ios_app(self.device['wda_url'], WeakNetworkConfig.IOS_APP_BUNDLE_ID)
        self._stf.launch_ios_app(self.device['wda_url'], WeakNetworkConfig.IOS_APP_BUNDLE_ID)
        timeout = 5 * 60
        t1 = time.time()
        while True:
            if time.time() - t1 > timeout:
                raise Exception('get_device_ip:{} timeout:{}'.format(self.device['wda_url'], timeout))
            self._device_ip = self._stf.get_device_ip(self.device['wda_url'], self.platform)
            if self._device_ip:
                # 弱网断网现在是192.168.0 如果网段变化则需要修改下面的逻辑
                if self._device_ip.startswith('192.168.0'):
                    self._set_auth()
                    return True
                else:
                    return False

    def _disconnect_android(self):
        if self.serail:
            ret = self._stf.toggleAndroidWifi(self.serail, "3", self._wifi_name, self._wifi_password)
            ip = ret.get("ip", None)
            if not str(ip).startswith("192.168.0"):
                return True
            else:
                return False
        else:
            raise Exception(f"device_serial is None")

    def _disconnect_ios(self):
        self.bundle_id = self._stf.find_ios_bundle_id(self.serail, WeakNetworkConfig.IOS_APP_BUNDLE_ID)
        if self.bundle_id is None:
            raise Exception('No iOS app bundle:{} found'.format(WeakNetworkConfig.IOS_APP_BUNDLE_ID))
        self._stf.stop_ios_app(self.device['wda_url'], WeakNetworkConfig.IOS_APP_BUNDLE_ID)
        self._stf.launch_ios_app(self.device['wda_url'], WeakNetworkConfig.IOS_APP_BUNDLE_ID, args=['disconnect'])
        return True

    def _set_auth(self):
        url = "{host}{uri}".format(host=self._atc_host,
                                   uri=WeakNetworkConfig.ATC_AUTH_URI.format(self._device_ip))
        r = requests.post(url)
        try:
            if r.status_code == 200:
                return True
            else:
                return False
        except Exception as e:
            return False

    def set_net_config(self, config_json):
        """
        :param config_json: 弱网配置参数
        :return: True if successful
        """
        url = "{host}{uri}".format(host=self._atc_host,
                                   uri=WeakNetworkConfig.ATC_SHAPE_URI.format(self._device_ip))
        r = requests.post(url, json=config_json)
        try:
            if r.status_code == 200:
                return True
            else:
                return False
        except Exception as e:
            return False


if __name__ == '__main__':
    token = "24dc77b46c7542a28cc74888aed16d15fc0d0d3077ed48e5b68956e2668eef27"
    sft_url = "http://10.12.35.2:8086"
    config = WeakNetworkConfig("2834d69c9ee8c9c02280d7d8828697cde1920cd6", stf_url=sft_url, sft_token=token)
