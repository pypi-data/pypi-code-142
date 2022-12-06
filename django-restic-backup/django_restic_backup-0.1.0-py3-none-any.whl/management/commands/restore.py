import base64
import getpass
import multiprocessing
import os
import re
import subprocess  # nosec
from distutils.dir_util import copy_tree
from pathlib import Path

import yaml
from common.django.common_command import CommonCommand
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from django.conf import settings


class Command(CommonCommand):
    help = (
        "Restore files or/and database backup from an environment (backup server) "
        "with encrypted secret file after decrypting it (secret file is defined in "
        "settings.BACKUP_CONF_FILE)"
    )

    def handle(self, *args, **options):
        if options["encrypt"] is True and options["decrypt"] is True:
            return self.error(
                "You can not use both encrypt and decrypt options at the same time"
            )

        if options["db_only"] is True and options["files_only"] is True:
            return self.error(
                "You can not use both db_only and files_only options at the same time"
            )

        if options["db_only"] is False and options["files_only"] is False:
            # it should manage both database and files if these options are not defined
            should_manage_app_and_db = True
        else:
            should_manage_app_and_db = False

        conf = self.get_backup_conf()
        key = self.create_key()
        if options["encrypt"] is True:
            # Just encrypt the conf file
            if should_manage_app_and_db is True or options["db_only"] is True:
                # Encrypt restic database backup configuration
                self.encrypt(conf, options["name_env"], "DB", key)
                self.success(
                    "Encryption of the configuration file of the Database backup "
                    "is completed."
                )

            if should_manage_app_and_db is True or options["files_only"] is True:
                # Encrypt restic documents backup configuration
                self.encrypt(conf, options["name_env"], "APP", key)
                self.success(
                    "Encryption of the configuration file of the Documents backup "
                    "is completed."
                )
        elif options["decrypt"] is True:
            # Just decrypt the conf file
            if should_manage_app_and_db is True or options["db_only"] is True:
                # Decrypt restic database backup configuration
                self.decrypt_and_save(conf, options["name_env"], "DB", key)
            if should_manage_app_and_db is True or options["files_only"] is True:
                # Decrypt restic documents backup configuration
                self.decrypt_and_save(conf, options["name_env"], "APP", key)
        elif options["show_secret"] is True:
            # Just show secrets
            if should_manage_app_and_db is True or options["db_only"] is True:
                # Show secrets of database backup configuration
                self.display_secret(conf, options["name_env"], "DB", key)
            if should_manage_app_and_db is True or options["files_only"] is True:
                # Show secrets of documents backup configuration
                self.display_secret(conf, options["name_env"], "APP", key)
        else:
            # decrypt conf file and restore backup
            lisa_conf = self.get_db_conf()
            if should_manage_app_and_db is True or options["db_only"] is True:
                # Restore or unlock database
                db_access = self.decrypt(conf, options["name_env"], "DB", key)
                self.set_restic_access(db_access)
                if options["unlock"] is True:
                    self.unlock_backups("db")
                elif options["list_snapshots"] is True:
                    self.list_snapshots()
                else:
                    self.get_backup_db(lisa_conf, options["db_id"])

            if should_manage_app_and_db is True or options["files_only"] is True:
                # Restore or unlock app documents
                app_access = self.decrypt(conf, options["name_env"], "APP", key)
                self.set_restic_access(app_access)
                if options["unlock"] is True:
                    self.unlock_backups("app")
                elif options["list_snapshots"] is True:
                    self.list_snapshots()
                else:
                    self.get_backup_documents(options["app_id"], options["deal"])
                    self.success("Restoration of documents completed.")

    def add_arguments(self, parser):
        parser.add_argument(
            "name_env",
            type=str,
            help="Name of env to back up "
            '(like primary for "digital ocean" and secondary for "aws")',
        ),
        parser.add_argument(
            "--encrypt",
            default=False,
            required=False,
            action="store_true",
            help="Just encrypt the file that contains "
            "secrets (tokens, password, etc.) of backup server "
            "(incompatible with --decrypt option)",
        )
        parser.add_argument(
            "--decrypt",
            default=False,
            required=False,
            action="store_true",
            help="Just decrypt the file that contains "
            "secrets (tokens, password, etc.) of backup server "
            "(incompatible with --encrypt option)",
        )
        parser.add_argument(
            "--db-only",
            default=False,
            required=False,
            action="store_true",
            help="Restore the backup of the database only "
            "(if --encrypt or --decrypt option is defined, "
            "just encrypt or decrypt the file that contains "
            "secrets (tokens, password, etc.) "
            "of DATABASE backup server "
            "(incompatible with --files-only option)",
        )
        parser.add_argument(
            "--files-only",
            default=False,
            required=False,
            action="store_true",
            help="Restore the backup of the database only "
            "(if --encrypt or --decrypt option is defined, "
            "just encrypt or decrypt the file that contains "
            "secrets (tokens, password, etc.) "
            "of FILES backup server "
            "(incompatible with --db-only option)",
        )
        parser.add_argument("--db-id", default="latest", required=False)
        parser.add_argument("--app-id", default="latest", required=False)
        parser.add_argument(
            "--unlock",
            default=False,
            required=False,
            action="store_true",
            help="Unlock backup if there are locked",
        )
        parser.add_argument(
            "-ls",
            "--list-snapshots",
            default=False,
            required=False,
            action="store_true",
            help="List every backup available",
        )
        parser.add_argument(
            "--show-secret",
            default=False,
            required=False,
            action="store_true",
            help="show the secret decrypted configured for the environment selected",
        )
        parser.add_argument(
            "--deal",
            type=str,
            help="Deal folder that should be retrive",
        )

    def get_db_conf(self):
        f = open(settings.CONF_FILE, mode="r")
        conf_content = f.read()
        lisa_conf = {}
        data = re.search(r'USER\"\s*:\s*"(.+)"', conf_content)
        lisa_conf["USER"] = data.group(1)
        data = re.search(r'PASSWORD\"\s*:\s*"(.+)"', conf_content)
        lisa_conf["PASSWORD"] = data.group(1)
        data = re.search(r'NAME\"\s*:\s*"(.+)"', conf_content)
        lisa_conf["NAME"] = data.group(1)
        data = re.search(r'HOST\"\s*:\s*"(.+)"', conf_content)
        if data is not None:
            lisa_conf["HOST"] = data.group(1)
        data = re.search(r'PORT\"\s*:\s*"(.+)"', conf_content)
        if data is not None:
            lisa_conf["PORT"] = data.group(1)
        return lisa_conf

    def get_backup_conf(self):
        with open(settings.BACKUP_CONF_FILE) as file:
            conf = yaml.load(file, Loader=yaml.SafeLoader)
            return conf

    def encrypt(self, conf, env, type, key):
        f = Fernet(key)
        with open(conf[env][type], "rb") as file:
            file_data = file.read()
        encrypted_data = f.encrypt(file_data)
        with open(conf[env][type], "wb") as file:
            file.write(encrypted_data)

    def decrypt_and_save(self, conf, env, type, key):
        decrypted_data = self.decrypt(conf, env, type, key)
        backup = "Database" if type == "DB" else "Documents"
        with open(conf[env][type], "wb") as file:
            file.write(decrypted_data)
        self.success(
            f"Decryption of the configuration file of the {backup} backup "
            "is completed. Be careful !"
        )

    def decrypt(self, conf, env, type, key):
        f = Fernet(key)
        with open(conf[env][type], "rb") as file:
            encrypted_data = file.read()
        decrypted_data = f.decrypt(encrypted_data)
        return decrypted_data

    def display_secret(self, conf, env, type, key):
        decrypted_data = self.decrypt(conf, env, type, key)
        backup = "Database" if type == "DB" else "Documents"
        self.success(f"{backup} secrets:")
        print(decrypted_data.decode("utf-8"))

    def create_key(self):
        pw = getpass.getpass("Password:")
        password = pw.encode("utf-8")
        salt = os.urandom(0)
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(password))
        return key

    def set_restic_access(self, access):
        access_str = access.decode("utf-8")
        os.environ["AWS_ACCESS_KEY_ID"] = re.search(
            'AWS_ACCESS_KEY_ID="(.+)"', access_str
        ).group(1)
        os.environ["AWS_SECRET_ACCESS_KEY"] = re.search(
            'AWS_SECRET_ACCESS_KEY="(.+)"', access_str
        ).group(1)
        os.environ["RESTIC_REPOSITORY"] = re.search(
            'RESTIC_REPOSITORY="(.+)"', access_str
        ).group(1)
        os.environ["RESTIC_PASSWORD"] = re.search(
            'RESTIC_PASSWORD="(.+)"', access_str
        ).group(1)

    def get_backup_db(self, lisa_conf, backup_id):
        p1 = subprocess.Popen(  # nosec
            ["restic", "dump", backup_id, "icarus_test.sql.gz"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        p2 = subprocess.Popen(  # nosec
            ["pigz", "-d"],
            stdin=p1.stdout,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        p3 = subprocess.Popen(  # nosec
            [
                "mysql",
                "-u",
                lisa_conf["USER"],
                lisa_conf["NAME"],
                f"-p{lisa_conf['PASSWORD']}",
            ]
            + (["-h", lisa_conf["HOST"]] if "HOST" in lisa_conf else []),
            stdin=p2.stdout,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        (output3, err3) = p3.communicate()
        (output2, err2) = p2.communicate()
        (output1, err1) = p1.communicate()
        if (
            len(err3.decode("utf-8")) != 0
            or len(err2.decode("utf-8")) != 0
            or len(err1.decode("utf-8")) != 0
        ):
            self.error("Restoration of database not completed.")
            self.unlock_backups("DB")
        else:
            self.success("Restoration of database completed.")

    def unlock_backups(self, repo_name):
        p1 = subprocess.Popen(  # nosec
            [
                "restic",
                "unlock",
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        (output, err) = p1.communicate()
        if len(err.decode("utf-8")) == 0:
            self.success(f"Backups are successfully unlocked for {repo_name}.")
        else:
            self.error(f"Backups have not been unlocked for {repo_name}.")

    def list_snapshots(self):
        p1 = subprocess.Popen(  # nosec
            [
                "restic",
                "snapshots",
            ],
        )
        p1.communicate()

    def get_backup_documents(self, backup_id, deal):
        if deal is None:
            arguments = ["restic", "restore", backup_id, "--target", "/tmp/restic"]
        else:
            arguments = [
                "restic",
                "restore",
                backup_id,
                "--target",
                "/tmp/restic",
                "--include",
                deal,
            ]
        p = subprocess.Popen(arguments)  # nosec
        (output, err) = p.communicate()
        p.wait()
        location = Path("/tmp/restic")
        documents_path = next(iter(location.rglob("**/documents/")))
        copy_tree(
            documents_path,
            "documents/",
        )
