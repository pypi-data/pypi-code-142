import json
import yaml
import os
import re
import sys
import unicodedata
import struct
import ctypes
from cryptography import x509
from cryptography.hazmat.primitives.serialization import Encoding
from pathlib import Path
from tpds.certs.cert import Cert
from tpds.certs.certs_backup import CertsBackup
from tpds.certs.cert_utils import get_certificate_CN
from tpds.tp_utils.tp_utils import run_subprocess_cmd
from tpds.manifest import ManifestIterator, Manifest
from tpds.secure_element import ECC608B
from tpds.tp_utils.tp_settings import TPSettings
from tpds.resource_generation import TFLXResources, TNGManifest
import cryptoauthlib as cal
from tpds.secure_element.constants import Constants
from tpds.certs.cert import Cert
from tpds.certs.tflex_certs import TFLEXCerts
from tpds.certs.create_cert_defs import CertDef
from tpds.certs.certs_backup import CertsBackup
from tpds.manifest import ManifestIterator, Manifest


ATCA_SUCCESS = 0x00


def make_valid_filename(s):
    """
    Convert an arbitrary string into one that can be used in an ascii filename.
    """
    if sys.version_info[0] <= 2:
        if not isinstance(s, unicode):
            s = str(s).decode("utf-8")
    else:
        s = str(s)
    # Normalize unicode characters
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode("ascii")
    # Remove non-word and non-whitespace characters
    s = re.sub(r"[^\w\s-]", "", s).strip()
    # Replace repeated whitespace with an underscore
    s = re.sub(r"\s+", "_", s)
    # Replace repeated dashes with a single dash
    s = re.sub(r"-+", "-", s)
    return s


class AzurertosConnect:
    def __init__(self):
        self.cfg = cal.ATCAIfaceCfg()
        self.default_creds = {
            "title": "Azure IoT Credentials",
            "subscription_id": "",
            "resourcegroup": "",
            "hubname": "",
            "dpsname": "",
            "idScope": "",
        }

        self.creds_file = os.path.join(
            TPSettings().get_base_folder(), "azure_credentials.yaml"
        )

        if not os.path.exists(self.creds_file):
            Path(self.creds_file).write_text(
                yaml.dump(self.default_creds, sort_keys=False)
            )
            with open(self.creds_file) as f:
                self.azure_credentials = yaml.safe_load(f)

        else:
            with open(self.creds_file) as f:
                self.azure_credentials = yaml.safe_load(f)
                self.resourceGroup = self.azure_credentials.get("resourcegroup")
                self.hname = self.azure_credentials.get("hubname")
                self.dname = self.azure_credentials.get("dpsname")

    def azure_connect(self, credentials):
        """
        Method login azure portal via cli and
        set the credentials in azure cli

        Inputs:
              credentials    contain azure iot hub name and
                             subscription id
        """

        # login to acccount
        sys_shell = True if sys.platform == "win32" else False
        print("Login to Azure account....", end="")
        subProcessOut = run_subprocess_cmd(cmd=["az", "login"], sys_shell=True)
        if subProcessOut.returncode:
            raise ValueError("Azure login failed with {}".format(subProcessOut))
        print("OK")

        # Setting up azure subscription id
        print("Setting the Subscription ID....\n", end="")
        self.az_subscription_id = credentials
        subProcessOut = run_subprocess_cmd(
            cmd=["az", "account", "set", "--subscription", self.az_subscription_id],
            sys_newlines=True,
            sys_shell=sys_shell,
        )
        if subProcessOut.returncode:
            raise ValueError(
                "Setting subscription failed with {}".format(subProcessOut)
            )
        print("Subscription ID ------- Valid")
        self.default_creds["subscription_id"] = self.az_subscription_id

    def azure_iot_extension(self):
        
        subProcessOut = run_subprocess_cmd(
            cmd=["az", "config", "set", "extension.use_dynamic_install=yes_prompt"], sys_shell=True
        )
        if subProcessOut.returncode:
            raise ValueError(
                "Azure extension config failed with {}".format(subProcessOut)
            )

        subProcessOut = run_subprocess_cmd(
            cmd=["az", "extension", "add", "--name", "azure-iot"], sys_shell=True
        )
        if subProcessOut.returncode:
            raise ValueError(
                "Azure iot Install failed with {}".format(subProcessOut)
            )

        print("Azure iot Extension installed successfully")

    def az_group_create(self, resourceGroup):
        print("Checking if the resourcegroup exists...")
        subProcessOut = run_subprocess_cmd(
            cmd=[
                "az",
                "group",
                "exists",
                "--name",
                resourceGroup,
                "--location",
                "centralus",
            ],
            sys_newlines=True,
            sys_shell=True,
        )

        print("Creating the Resource group .....")
        subProcessOut = run_subprocess_cmd(
            cmd=[
                "az",
                "group",
                "create",
                "--name",
                resourceGroup,
                "--location",
                "centralus",
            ],
            sys_newlines=True,
            sys_shell=True,
        )
        if subProcessOut.returncode:
            raise ValueError("Resource group creation failed. {}".format(subProcessOut))

        self.resourceGroup = resourceGroup
        print("Azure Resource group created successfully")
        self.default_creds["resourcegroup"] = self.resourceGroup

    def az_hub_create(self, hostName):
        print("Creating the iot Hub.....")
        print("Please wait, this may take up to 2 minutes...")
        subProcessOut = run_subprocess_cmd(
            cmd=[
                "az",
                "iot",
                "hub",
                "create",
                "--resource-group",
                self.resourceGroup,
                "--name",
                hostName,
            ],
            sys_newlines=True,
            sys_shell=True,
        )

        if subProcessOut.returncode:
            raise ValueError(
                "Hub creation creation failed with {}".format(subProcessOut.returncode)
            )

        self.hname = json.loads(subProcessOut.stdout)["name"]
        self.hostname = json.loads(subProcessOut.stdout)["properties"]["hostName"]
        print("Hub creation was successful")
        self.default_creds["hubname"] = self.hname

    def az_dps_create(self, dpsName):
        print("Creating the dps.... ")
        subProcessOut = run_subprocess_cmd(
            cmd=[
                "az",
                "iot",
                "dps",
                "create",
                "--resource-group",
                self.resourceGroup,
                "--name",
                dpsName,
            ],
            sys_newlines=True,
            sys_shell=True,
        )
        if subProcessOut.returncode:
            raise ValueError(
                "DPS creation creation failed with {}".format(subProcessOut.returncode)
            )

        self.serviceOpHostName = json.loads(subProcessOut.stdout)["properties"][
            "serviceOperationsHostName"
        ]
        self.idScope = json.loads(subProcessOut.stdout)["properties"]["idScope"]
        self.dname = json.loads(subProcessOut.stdout)["name"]
        print("DPS creation was successful")

        self.default_creds["dpsname"] = self.dname
        self.default_creds["idScope"] = self.idScope
        Path(self.creds_file).write_text(yaml.dump(self.default_creds, sort_keys=False))

    def link_hub_dps(self):
        print("Linking the Iot Hub to the DPS ")
        subProcessOut = run_subprocess_cmd(
            cmd=["az", "iot", "hub", "show-connection-string", "--name", self.hname],
            sys_newlines=True,
            sys_shell=True,
        )

        self.hubConnectionString = json.loads(subProcessOut.stdout)["connectionString"]
        subProcessOut = run_subprocess_cmd(
            cmd=[
                "az",
                "iot",
                "dps",
                "linked-hub",
                "create",
                "--dps-name",
                self.dname,
                "--resource-group",
                self.resourceGroup,
                "--connection-string",
                self.hubConnectionString,
            ],
            sys_newlines=True,
            sys_shell=True,
        )

        if subProcessOut.returncode:
            raise ValueError(
                "Linking DPS to the Hub failed with {}".format(subProcessOut.returncode)
            )
        print("DPS linked successfully")

    def register_dps(self, path):
        sys_shell = True if sys.platform == "win32" else False
        subProcessOut = run_subprocess_cmd(
            cmd=[
                "az",
                "iot",
                "dps",
                "enrollment",
                "show",
                "--dps-name",
                self.dname,
                "--eid",
                self.device_id,
            ],
            sys_newlines=True,
            sys_shell=sys_shell,
        )
        if subProcessOut.returncode:
            subProcessOut = run_subprocess_cmd(
                cmd=[
                    "az",
                    "iot",
                    "dps",
                    "enrollment",
                    "create",
                    "-g",
                    self.resourceGroup,
                    "--dps-name",
                    self.dname,
                    "--enrollment-id",
                    self.device_id,
                    "--attestation-type",
                    "x509",
                    "--certificate-path",
                    path,
                ],
                sys_newlines=True,
                sys_shell=sys_shell,
            )
            if subProcessOut.returncode:
                raise ValueError("Enrollment failed {}".format(subProcessOut.stdout))
            print("Device enrolled successfully")
        else:
            print("Your devcie is already enrolled")

    def enroll_device(self, i2c_address, port, manifest, b):
        self.element = ECC608B(i2c_address, port)
        self.serial_number = self.element.get_device_serial_number()
        self.kit_atcab_init(i2c_address, port)

        device_manifest = manifest.get("json_file")
        device_manifest_ca = manifest.get("ca_cert")

        if os.path.exists(device_manifest) and device_manifest.endswith(".json"):
            with open(device_manifest) as json_data:
                device_manifest = json.load(json_data)

        if not isinstance(device_manifest, list):
            raise ValueError("Unsupport manifest format to process")

        manifest_ca = Cert()
        manifest_ca.set_certificate(device_manifest_ca)
        iterator = ManifestIterator(device_manifest)
        print("Number of Devices: {}".format(iterator.index))

        while iterator.index != 0:
            se = Manifest().decode_manifest(
                iterator.__next__(), manifest_ca.certificate
            )
            se_certs = Manifest().extract_public_data_pem(se)
            slot = next((sub for sub in se_certs if sub.get("id") == str(0)), None)
            no_of_certs = len(slot.get("certs"))
            if no_of_certs:
                device_cert = "device.crt"

                with open(device_cert, "w") as f:
                    f.write(slot.get("certs")[no_of_certs - 2])
                    f.close()

                self.device_id = get_certificate_CN(device_cert)

                filename = make_valid_filename(self.device_id) + ".pem"
                crt = Cert()
                crt.set_certificate(device_cert)
                with open(filename, "wb") as f:
                    f.write(crt.certificate.public_bytes(encoding=Encoding.PEM))
                cert_path = os.path.join(os.getcwd(), filename)
                self.register_dps(cert_path)

    def kit_atcab_init(self, address, port):
        self.cfg.iface_type = int(cal.ATCAIfaceType.ATCA_UART_IFACE)
        self.cfg.devtype = int(cal.ATCADeviceType.ATECC608B)
        self.cfg.wake_delay = 1500
        self.cfg.rx_retries = 10

        self.cfg.cfg.atcauart.dev_interface = int(cal.ATCAKitType.ATCA_KIT_I2C_IFACE)
        self.cfg.cfg.atcauart.dev_identity = address
        if isinstance(port, str):
            self.cfg.cfg.cfg_data = ctypes.c_char_p(port.encode("ascii"))
        else:
            self.cfg.cfg.atcauart.port = port
        self.cfg.cfg.atcauart.baud = 115200
        self.cfg.cfg.atcauart.wordsize = 8
        self.cfg.cfg.atcauart.parity = 2
        self.cfg.cfg.atcauart.stopbits = 1
        assert cal.atcab_init(self.cfg) == ATCA_SUCCESS
        # Initialize the stack

    def saveDataSlot(self, address, port):
        # Saving azure data to slot 8
        if self.azure_credentials.get("idScope") != "":
            self.idScope = self.azure_credentials.get("idScope")

        self.kit_atcab_init(address, port)
        idScope_len = len(bytes(self.idScope, "utf-8"))
        data = struct.pack(
            "BB {var1}s ".format(var1=len(self.idScope)),
            address,
            idScope_len,
            bytes(self.idScope, "utf-8"),
        )
        bytePads = len(data) % 4
        if bytePads != 0:
            bytePads = 4 - bytePads
            data = struct.pack(
                "BB {var1}s  {bd}x".format(var1=len(self.idScope), bd=bytePads),
                address,
                idScope_len,
                bytes(self.idScope, "utf-8"),
            )

        offst = 0
        block_size = 32
        end_block = block_size

        if len(data) <= block_size:
            assert (
                cal.atcab_write_bytes_zone(
                    Constants.ATCA_DATA_ZONE,
                    8,
                    offst,
                    data[offst : len(data)],
                    len(data),
                )
                == ATCA_SUCCESS
            )
            print("Saving data to slot 8 was successful")
        else:
            while end_block < len(data):
                # assert cal.atcab_write_bytes_zone(Constants.ATCA_DATA_ZONE, 8, offst, data[offst : end_block], block_size) == ATCA_SUCCESS
                assert (
                    cal.atcab_write_bytes_zone(
                        Constants.ATCA_DATA_ZONE,
                        8,
                        offst,
                        data[offst:end_block],
                        block_size,
                    )
                    == ATCA_SUCCESS
                )

                end_block += block_size
                offst += block_size
                if end_block >= len(data):
                    end_block = len(data)
                    assert (
                        cal.atcab_write_bytes_zone(
                            Constants.ATCA_DATA_ZONE,
                            8,
                            offst,
                            data[offst:end_block],
                            (end_block - offst),
                        )
                        == ATCA_SUCCESS
                    )
                    print("Saving data to slot 8 was successful")
                    break

        cal.atcab_release()

    def save_i2c_add(self, address, port):
        self.kit_atcab_init(0x6A, port)
        data = address.to_bytes(1, "big")
        assert (
            cal.atcab_write_bytes_zone(Constants.ATCA_DATA_ZONE, 8, 0, data, 4)
            == ATCA_SUCCESS
        )
        print("Secure element address saved successfully")
        cal.atcab_release()


if __name__ == "__main__":
    pass
