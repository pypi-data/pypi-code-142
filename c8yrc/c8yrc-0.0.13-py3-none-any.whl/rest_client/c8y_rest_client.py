import datetime
import json
import logging
import random
import string
import time
import requests
from c8yrc.rest_client.c8y_enterprise import Cube, SoftwareImage, CubeOperation
from c8yrc.rest_client.c8y_exception import C8yException
from c8yrc.rest_client.rest_constants import UPDATE_FIRMWARE_OPERATION_HEADER, C8YQueries, C8YOperationStatus


class C8yRestClient(object):
    """
    A class to interface with Schindler Cumulocity Device Management Platform
    """
    def __init__(self, c8y_serial_number, user, password, url=None, tenant=None, session_verify=False, tfacode=None):

        self._operation_marker = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        if url is None:
            self.url = 'https://main.dm-zz-q.ioee10-cloud.com/'
        else:
            self.url = url
        self.session = requests.Session()
        self.session.verify = session_verify
        self.device_id = None
        if tenant is None:
            self.tenant = 't2700'
        else:
            self.tenant = tenant
        self.headers = None
        self.cy8_device = None
        self.ext_type = 'c8y_Serial'
        self.c8y_serial_number = c8y_serial_number
        self.start(user=user, password=password, tfacode=tfacode)

    def start(self, user: str, password: str, tfacode: int):
        """
        Initialize authentication and session

        :param user: The cy8 user name
        :param password: The cy8 user password
        :param tfacode: The code generated by google authenticator for the specific user
        :return : None
        """
        self.validate_tenant_id()
        self.retrieve_token(user, password, tfacode)
        # os.environ['C8Y_TOKEN'] = self.session.cookies.get_dict()['authorization']
        self.headers = {'Content-Type': 'application/json', 
                        'X-XSRF-TOKEN': self.session.cookies.get_dict()['XSRF-TOKEN']}
        self.get_device_info()

    def validate_tenant_id(self):
        """
        Validate the tenant

        """
        current_user_url = self.url + C8YQueries.GET_TENANT_OPTIONS
        headers = {}
        response = self.session.get(current_user_url, headers=headers)
        logging.debug(f'Response received: {response}')
        if response.status_code == 200:
            login_options_body = json.loads(response.text)
            login_options = login_options_body['loginOptions']
            for option in login_options:
                if 'initRequest' in option:
                    tenant_id = option['initRequest'].split('=')[1]
                    if self.tenant != tenant_id:
                        logging.debug(f'Wrong Tenant ID {self.tenant}, Correct Tenant ID: {tenant_id}')
                        self.tenant = tenant_id
                    break
        else:
            logging.error('Error validating Tenant ID!')

    def retrieve_token(self, user: str, password: str, tfacode: int):
        """
        Get the authentication token from cumulocity to be used in the session

        :param user: The cy8 user name
        :param password: The cy8 user password
        :param tfacode: The code generated by google authenticator for the specific user
        :return : None
        :exception C8yException: raise when the user is not able to be authenticated
        """
        oauth_url = self.url + C8YQueries.POST_OAUTH.format(self.tenant)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        body = {
            'grant_type': 'PASSWORD',
            'username': user,
            'password': password,
            'tfa_code': tfacode
        }
        logging.debug(f'Sending requests to {oauth_url}')
        response = self.session.post(oauth_url, headers=headers, data=body)
        if response.status_code == 200:
            logging.debug(f'Authentication successful. Tokens have been updated {self.session.cookies.get_dict()}!')
            return

        msg = f'Server Error received for User {user} and Tenant {self.tenant}. Status Code: {response.status_code}'
        logging.error(msg)
        raise C8yException(msg, None)

    def get_data(self, query: str) -> dict:
        """
        Method to get data by specified query

        :param query:   Query
        :return:        Response data in dict representation
        """
        response = self.session.get(url=f'{self.url}{query}', headers=self.headers)
        return json.loads(response.text)

    def send_data(self, query: str, data):
        """
        Method to send data to the Cumulocity host URL

        :param query:   Query
        :param data:    Data to send
        :return:        Response data
        """
        response = self.session.post(url=f'{self.url}{query}', data=json.dumps(data), headers=self.headers)
        return response.request

    def get_device_id_by_serial_number(self, serial_number: str, ext_type: str) -> int:
        """
        Method to get Cumulocity device ID by device serial number

        :param ext_type: Cy8 external type
        :param serial_number:   Cumulocity device ESN (serial number container device prefix)
        :return:                Cumulocity device ID
        """
        response = self.get_data(query=C8YQueries.GET_DEVICE_ID_BY_ESN.format(ext_type, serial_number))
        return int(response['managedObject']['id'])

    def get_cube_availability_status(self) -> str:
        """
        Method to get Cumulocity device availability status

        :return:            Cumulocity device availability status
        """
        response = self.get_data(query=C8YQueries.SELECT_DEVICE_BY_ID.format(self.device_id))
        return response['c8y_Availability']['status']

    def get_cube_connection_status(self) -> str:
        """
        Method to get Cumulocity device connection status

        :return:            Cumulocity device connection status
        """
        # c8y devices get --id {device_id} --select "id,c8y_Connection.status"
        response = self.get_data(query=C8YQueries.SELECT_DEVICE_BY_ID.format(self.device_id))
        return response['c8y_Connection']['status']

    def get_current_firmware(self, device_type: str) -> tuple:
        """
        Method to get firmware currently installed on the Cube

        :param device_type:     Cumulocity device type
        :return:                Currently installed firmware
        """
        response = self.get_data(query=C8YQueries.SELECT_DEVICE_BY_ID.format(self.device_id))
        firmware_name = response['c8y_Firmware']['name']
        firmware_version = response['c8y_Firmware']['version']
        available_firmwares = self.get_available_firmwares(device_type)
        return tuple(firmware for firmware in available_firmwares[firmware_name] if firmware_version in firmware)

    def get_available_firmwares(self, device_type: str):
        """
        Method to get a list of available firmwares for selected device software type

        :param device_type: Cumulocity device software type, including architecture
        :return:
        """
        all_firmwares = {}
        firmwares = self.get_data(C8YQueries.GET_FIRMWARE_BY_DEVICE_TYPE.format(device_type))
        supported_firmwares = tuple((firmware['name'], firmware['id']) for firmware in firmwares['managedObjects'])
        for firmware in supported_firmwares:
            firmware_images = self.get_data(C8YQueries.GET_FIRMWARE_BINARY.format(firmware[1]))

            firmware_version_url = [
                (firmware[0], image['c8y_Firmware']['version'], image['c8y_Firmware']['url']) for image in firmware_images['managedObjects']
            ]

            all_firmwares.update({firmware[0]: sorted(firmware_version_url)})
        return all_firmwares

    def wait_for_operation_state(self, operation_id: int, expected_state: str, time_to_wait: int = 10 * 60,
                                 period: int = 60):
        """
        Function to wait until operation state will be equal to expected state.

        :param operation_id:    Cumulocity operation ID.
        :param expected_state:  Expected state.
        :param time_to_wait:    Time to wait.
        :param period:          Time between state verification

        :return: Whether state is expected (bool).
        """
        time_start = time.time()
        while time.time() < time_start + time_to_wait:
            elapsed_time = time.time() - time_start
            current_state = self.get_operation_state(operation_id)
            if current_state == expected_state:
                logging.info(f"Operation ('{operation_id}') change to {expected_state}' after '{elapsed_time}' seconds")
                return True
            if current_state == C8YOperationStatus.FAILED:
                logging.error(f"Operation ('{operation_id}') FAILED' after '{elapsed_time}' seconds")
                return False
            logging.debug(f'{current_state} for operation {operation_id} waiting more {period} seconds')
            time.sleep(period)

        logging.warning(f"Operation ('{operation_id}') is not changed to '{expected_state}' in '{time_to_wait}' seconds")
        return False

    def get_operation_state(self, operation_id: int) -> str:
        """
        Method to get Cumulocity operation status by operation ID

        :param operation_id:    Cumulocity operation ID
        :return:                Cumulocity operation status
        """
        response = self.get_data(query=C8YQueries.GET_OPERATION.format(operation_id))
        return response['status']

    def get_remote_configuration_from_cumulocity(self) -> dict:
        """
        Method to get a remote configuration
        :return: Cube remote configuration from Cumulocity
        """
        # c8y devices get --id 20228252 --select "schindler_RemoteConfiguration"
        response = self.get_data(query=C8YQueries.SELECT_DEVICE_BY_ID.format(self.device_id))
        return response['schindler_RemoteConfiguration']

    def get_lxc_container(self) -> str:
        """
        Method to get a currently installed LXC container

        :return: LXC container version
        """
        response = self.get_data(query=C8YQueries.SELECT_DEVICE_BY_ID.format(self.device_id))

        return response['ac_lxcContainer']['contVersion']

    def update_cube_firmware(self, firmware: SoftwareImage):
        """
        Method to start update operation for cube under test

        :type firmware: SoftwareImage : Object the contains the software image details
        :return: None
        """

        operation_description = f"{self._operation_marker}:{UPDATE_FIRMWARE_OPERATION_HEADER} to: {firmware.name} ({firmware.version})"
        firmware_info = {
            "c8y_Firmware": {
                "name": firmware.name,
                "url": firmware.url,
                "version": firmware.version
            },
            "deviceId": str(self.device_id),
            "description": operation_description,
        }
        self.send_data(C8YQueries.POST_OPERATION, data=firmware_info)

    def get_device_info(self):
        """
        Get the all device information from cumulocity, includes internal device Id and software list
        The response is stored in the Cube object
        """
        # 1st query the device id
        identity_url = self.url + C8YQueries.GET_DEVICE_ID_BY_ESN.format(self.ext_type, self.c8y_serial_number)
        response = self.session.get(identity_url, headers=self.headers)
        if response.status_code != 200:
            raise C8yException(f'Error on  {identity_url}. '
                               f'Status Code {response.status_code}', None)
        ext_id = json.loads(response.text)
        self.device_id = ext_id['managedObject']['id']

        # 2nd query the device info
        identity_url = self.url + C8YQueries.GET_DEVICE_INFO_BY_DEV_ID.format(self.device_id)
        response = self.session.get(identity_url, headers=self.headers)
        if response.status_code != 200:
            raise C8yException(f'Error on {identity_url}. Status Code {response.status_code}', None)
        self.cy8_device = Cube(response.text)

    def get_device_operation(self) -> CubeOperation:
        """
        Get the operation defined by a fixed description.
        Stores that information ins the CubeOperation class
        :return: CubeOperation

        """
        current_time = datetime.datetime.today()
        to_date_str = (current_time + datetime.timedelta(+1)).strftime('%Y-%m-%d')
        from_date_str = (current_time + datetime.timedelta(-5)).strftime('%Y-%m-%d')
        identity_url = self.url + C8YQueries.GET_UPDATE_OPERATION_BY_DEVICE_ID.format(from_date_str, to_date_str, self.device_id)
        response = self.session.get(identity_url, headers=self.headers)
        if response.status_code != 200:
            raise C8yException(f'Error on  {identity_url}. '
                               f'Status Code {response.status_code}', None)
        operations = json.loads(response.text)
        update_operations = [
            the_operation for the_operation in operations['operations']
            if f'{self._operation_marker}' in the_operation.get('description', '')
        ]

        if len(update_operations) == 0:
            logging.error('operation not found')
            return None
        my_operation = CubeOperation(update_operations)
        return my_operation




