# -*- coding: utf-8 -*-
# 2018 to present - Copyright Microchip Technology Inc. and its subsidiaries.

# Subject to your compliance with these terms, you may use Microchip software
# and any derivatives exclusively with Microchip products. It is your
# responsibility to comply with third party license terms applicable to your
# use of third party software (including open source software) that may
# accompany Microchip software.

# THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER
# EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED
# WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A PARTICULAR
# PURPOSE. IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL,
# PUNITIVE, INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY
# KIND WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP
# HAS BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE
# FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN
# ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
# THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.


import os
import shutil
from pathlib import Path
import yaml
import cryptoauthlib as cal
from helper import (connect_to_prototyping_board,connect_to_proto_board_VC, generate_custom_pki,
                    verify_cert_chain_custompki, verify_cert_chain,
                    verify_SE_with_random_challenge, generate_manifest,
                    restore_mchp_certs_on_device, generate_project_config_h)
from tpds.cloud_connect.azure_connect import AzureConnect
from tpds.cloud_connect.azureRTOS_connect import AzurertosConnect
from tpds.tp_utils.tp_print import print
import tpds.tp_utils.tp_input_dialog as tp_userinput
from tpds.certs.cert_utils import get_certificate_CN


class AzureConnectBase():
    def __init__(self, boards):
        self.boards = boards
        self.connection = AzureConnect()

    def connect_to_cloud(self, b=None):
        resp_data = self.__azure_login(b)
        assert resp_data == 'Success', f'''Azure login config failed with "{resp_data}"'''

    def connect_to_board(self, b=None):
        self.element = connect_to_prototyping_board(self.boards, b)
        assert self.element, 'Connection to Board failed'
        self.serial_number = self.element.get_device_serial_number()

    def is_cn_supports_azure(self, device_cert, b=None):
        return (' ' not in get_certificate_CN(device_cert))

    def __azure_login(self, b=None):
        with open(self.connection.creds_file) as f:
            azure_credentials = yaml.safe_load(f)
        if all(dict((k, v.strip()) for k, v in azure_credentials.items()).values()):
            self.connection.set_credentials(azure_credentials)
            print(f'Azure IoT Hub: {self.connection.az_hub_name}', canvas=b)
            print(
                f'Azure Subscription: {self.connection.az_subscription_id}',
                canvas=b)
            azure_connect = os.path.join(os.getcwd(), 'azure_connect.h')
            with open(azure_connect, 'w') as f:
                f.write('#ifndef _AZURE_CONNECT_H\n')
                f.write('#define _AZURE_CONNECT_H\n\n')
                f.write('#include "cryptoauthlib.h"\n\n')
                f.write('#ifdef __cplusplus\n')
                f.write('extern "C" {\n')
                f.write('#endif\n\n')
                cloud_endpoint = (
                    f'#define CLOUD_ENDPOINT "{self.connection.az_hub_name}'
                    '.azure-devices.net"\n\n')
                f.write(cloud_endpoint)
                f.write('#ifdef __cplusplus\n')
                f.write('}\n')
                f.write('#endif\n')
                f.write('#endif\n')
            return 'Success'
        else:
            msg_box_info = (
                '<font color=#0000ff><b>Invalid Azure account credentials'
                '</b></font><br>'
                '<br>To setup an Azure account, please refer Usecase help guide<br>')
            acc_cred_diag = tp_userinput.TPMessageBox(
                title="Azure account credentials",
                info=msg_box_info)
            acc_cred_diag.invoke_dialog()
            return 'Credentials are unavailable'


class AzureCustomPKI(AzureConnectBase):
    def __init__(self, boards):
        super().__init__(boards)

    def generate_resources(self, b=None):
        self.connect_to_board(b)

        print('Generating CustomPKI certs...', canvas=b)
        generate_custom_pki(b)
        self.root_crt = 'root_crt.crt'
        self.root_key = 'root_key.key'
        self.signer_crt = 'signer_FFFF.crt'
        self.signer_key = 'signer_FFFF.key'
        self.device_crt = f'device_{self.serial_number.hex().upper()}.crt'
        azure_support = self.is_cn_supports_azure(self.device_crt, b)
        generate_project_config_h(cert_type='CUSTOM', address=0x6C, azure_support=azure_support)
        assert azure_support, ((
                'Connected TFLX device doesn\'t support Azure.\n'
                'Cert CN contains space(s).'))

    def register_certificates(self, b=None):
        self.connect_to_cloud(b)

        # Register Signer
        signer_cert = self.signer_crt
        signer_cer = os.path.splitext(signer_cert)[0]+'.cer'
        shutil.copy(signer_cert, signer_cer)
        print(f'Registering {signer_cer} to Azure account...', canvas=b)
        self.connection.register_signer_certificate(
                                    signer_cert=signer_cer,
                                    signer_key=self.signer_key)
        print('Completed...', canvas=b)

        # Register Device
        device_crt = self.device_crt
        print(f'Register {device_crt} to Azure account...', canvas=b)
        self.connection.register_device_as_CA_signed(device_cert=device_crt)
        print('Completed...', canvas=b)

    def verify_cert_chain(self, b=None):
        device_cert, crt_template = verify_cert_chain_custompki(
                    self.root_crt, self.root_key,
                    self.signer_crt, self.signer_key,
                    self.device_crt, b)
        self.device_crt = device_cert
        self.crt_template = crt_template

    def verify_SE_with_random_challenge(self, b=None):
        verify_SE_with_random_challenge(
                    b, self.device_crt, device_crt_template=self.crt_template['device'])


class AzureIoTAuthentication(AzureConnectBase):
    def __init__(self, boards):
        super().__init__(boards)
   

    def generate_resources(self, b=None):
        self.connect_to_board(b)

        mchp_certs, r_manifest = restore_mchp_certs_on_device(
                            self.serial_number, b)
        self.device_crt = mchp_certs.get('device')
        self.signer_crt = mchp_certs.get('signer')
        self.root_crt = mchp_certs.get('root')
        if r_manifest:
            self.manifest = r_manifest
        else:
            self.manifest = generate_manifest(
                b, self.signer_crt.certificate, self.device_crt.certificate)
        azure_support = self.is_cn_supports_azure(self.device_crt.certificate, b)
        generate_project_config_h(cert_type='MCHP', address=0x6C, azure_support=azure_support)
        assert azure_support, ((
                'Connected TFLX device doesn\'t support Azure.\n'
                'Cert CN contains space(s).'))

    def register_device(self, b=None):
        self.connect_to_cloud(b)
        print('Registering device into azure account...', canvas=b)
        self.connection.register_device_from_manifest(
                        device_manifest=self.manifest.get('json_file'),
                        device_manifest_ca=self.manifest.get('ca_cert'))
        print('Completed...', canvas=b)

    def verify_cert_chain(self, b=None):
        if(self.root_crt is not None):
            self.dev_cert = verify_cert_chain(
                b, self.signer_crt.certificate, self.device_crt.certificate, self.root_crt.certificate)
        else:
            self.dev_cert = verify_cert_chain(
                b, self.signer_crt.certificate, self.device_crt.certificate)
        if self.dev_cert is None:
            raise ValueError('Certificate chain validation is failed')

    def verify_SE_with_random_challenge(self, b=None):
        verify_SE_with_random_challenge(b, self.dev_cert)




class AzureRTOS(AzureConnectBase):
    def __init__(self, boards,i2c_address):
        super().__init__(boards)
        self.i2c_address = i2c_address
     
    def connect_to_bo(self, b=None):
        self.element = connect_to_proto_board_VC(self.boards,self.i2c_address, b)
        self.port = self.element.port
        assert self.element, 'Connection to Board failed'
        self.serial_number = self.element.get_device_serial_number() 
     
     
    def generate_resources(self, b=None):
        
        self.connect_to_bo(b)

        mchp_certs, r_manifest = restore_mchp_certs_on_device(
                            self.serial_number, b)
        self.device_crt = mchp_certs.get('device')
        self.signer_crt = mchp_certs.get('signer')
        self.root_crt = mchp_certs.get('root')
        if r_manifest:
            self.manifest = r_manifest
        else:
            self.manifest = generate_manifest(
                b, self.signer_crt.certificate, self.device_crt.certificate)
        azure_support = self.is_cn_supports_azure(self.device_crt.certificate, b)
        #generate_project_config_h(cert_type='MCHP', address=0x6C, azure_support=azure_support)
        assert azure_support, ((
                'Connected TFLX device doesn\'t support Azure.\n'
                    'Cert CN contains space(s).'))
    
    
    def Azure_DPS_setup(self, b):
        self.azure_data = AzurertosConnect()
        with open(self.azure_data.creds_file) as f:
            azure_credentials = yaml.safe_load(f) 
        
        if azure_credentials.get('subscription_id') == '':
            text_box_desc = (
                '''<font color=#0000ff><b>Set your subscription ID</b></font><br>
                <br>Your Azure Subscription needs to be active .<br>''')
            subscription = tp_userinput.TPInputTextBox(
                                        desc=text_box_desc,
                                        dialog_title='Azure Subscription ID')
            subscription.invoke_dialog()
            self.azure_data.azure_connect(subscription.user_text)
        else:
            self.azure_data.azure_connect(azure_credentials.get('subscription_id'))
        self.azure_data.azure_iot_extension() 
        


        if azure_credentials.get('resourcegroup') == '' or  azure_credentials.get('hubname') == '' or  azure_credentials.get('dpsname') == '':
            
            if azure_credentials.get('resourcegroup') == '':
            
                text_box_desc = (
                    '''<font color=#0000ff><b>Enter a name for the Resource Group</b></font><br>
                    <br>A resource group is a container that holds your Azure solution related resources .<br>''')
                resourceGroup = tp_userinput.TPInputTextBox(
                                            desc=text_box_desc,
                                            dialog_title='Resource Group Name')
                resourceGroup.invoke_dialog()
                self.azure_data.az_group_create(resourceGroup.user_text)

                text_box_desc = (
                    '''<font color=#0000ff><b>Enter a name for your Azure Hub </b></font><br>
                    <br>The Hub name needs to be globally unique .<br>''')
                hostName = tp_userinput.TPInputTextBox(
                                            desc=text_box_desc,
                                            dialog_title='Azure Hub Name ')
                hostName.invoke_dialog()
                self.azure_data.az_hub_create(hostName.user_text)

                text_box_desc = (
                    '''<font color=#0000ff><b>Enter a name for your DPS instance</b></font><br>
                    <br>DPS is the device provisioning helper service for your IoT Hub that will provides all the means to provision your devices in a secure and scalable manner .<br>''')
                dpsName = tp_userinput.TPInputTextBox(
                                            desc=text_box_desc,
                                            dialog_title='DPS Name')
                dpsName.invoke_dialog()
                self.azure_data.az_dps_create(dpsName.user_text)
                self.azure_data.link_hub_dps()

            elif azure_credentials.get('hubname') == '' and azure_credentials.get('dpsname') == ''  :
                text_box_desc = (
                    '''<font color=#0000ff><b>Enter a for your Azure Hub </b></font><br>
                    <br>The Hub name needs to be globally unique .<br>''')
                hostName = tp_userinput.TPInputTextBox(
                                            desc=text_box_desc,
                                            dialog_title='Azure Hub Name ')
                hostName.invoke_dialog()
                self.azure_data.az_hub_create(hostName.user_text)

                text_box_desc = (
                    '''<font color=#0000ff><b>Enter a name for your DPS instance</b></font><br>
                    <br>DPS is the device provisioning helper service for your IoT Hub that will provides all the means to provision your devices in a secure and scalable manner .<br>''')
                dpsName = tp_userinput.TPInputTextBox(
                                            desc=text_box_desc,
                                            dialog_title='DPS Name')
                dpsName.invoke_dialog() 
                self.azure_data.az_dps_create(dpsName.user_text)
                self.azure_data.link_hub_dps()

            else :
                text_box_desc = (
                    '''<font color=#0000ff><b>Enter a name for your DPS instance</b></font><br>
                    <br>DPS is the device provisioning helper service for your IoT Hub that will provides all the means to provision your devices in a secure and scalable manner .<br>''')
                dpsName = tp_userinput.TPInputTextBox(
                                            desc=text_box_desc,
                                            dialog_title='DPS Name')
                dpsName.invoke_dialog() 
                self.azure_data.az_dps_create(dpsName.user_text)
                self.azure_data.link_hub_dps()
        else:
            print("Your Azure Iot is already set")
        
      

    
    def register_device(self, b=None):
            self.azure_data.enroll_device(self.i2c_address, self.port, self.manifest, b)
            self.azure_data.saveDataSlot(self.i2c_address, self.port)
            self.azure_data.save_i2c_add(self.i2c_address, self.port)
            cal.atcab_release()

    
    def verify_cert_chain(self, b=None):
            if(self.root_crt is not None):
                self.dev_cert = verify_cert_chain(
                    b, self.signer_crt.certificate, self.device_crt.certificate, self.root_crt.certificate)
            else:
                self.dev_cert = verify_cert_chain(
                    b, self.signer_crt.certificate, self.device_crt.certificate)
            if self.dev_cert is None:
                raise ValueError('Certificate chain validation is failed')

    
    def verify_SE_with_random_challenge(self, b=None):
        self.azure_data.kit_atcab_init(self.i2c_address, self.port)
        verify_SE_with_random_challenge(b,self.dev_cert)
        cal.atcab_release()



# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    pass
