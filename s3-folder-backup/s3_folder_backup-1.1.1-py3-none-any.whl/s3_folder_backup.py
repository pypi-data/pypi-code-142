import boto3
import logging
import boto3
from botocore.exceptions import ClientError
import os
import zipfile
import os
from datetime import datetime
import logging

"""
Backup your files and folders from specific folder
Can Backup you server time to time using cron job 
"""


class s3_folder_backup:
    def __init__(self, config):
        try:
            self.logger = logging.getLogger()
            self.logger.setLevel(logging.DEBUG)
            self.config = config
            self.s3 = boto3.client(
                "s3",
                aws_access_key_id=config['AWS_ACCESS_KEY_ID'],
                aws_secret_access_key=config['AWS_SECRET_ACCESS_KEY']
            )
        except Exception as e:
            self.logger.error("Something Happened: " + str(e))

    def __zipdir(self, path, ziph):
        # ziph is zipfile handle
        for root, dirs, files in os.walk(path):
            for file in files:
                ziph.write(os.path.join(root, file))

    def __upload_file_to_s3(self, file, bucket_name):
        try:
            self.s3.upload_file(file, bucket_name, file)
        except Exception as e:
            # This is a catch all exception, edit this part to fit your needs.
            self.logger.error("Something Happened: " + str(e))
            return e
        return "ok"

    def upload(self):
        try:
            current_time = datetime.today().strftime('%Y-%m-%d-%H-%M-%S')
            filename = f'Backup_tmp-{current_time}.zip'
            zipf = zipfile.ZipFile(filename, 'w', zipfile.ZIP_DEFLATED)
            self.__zipdir(self.config["DIR"], zipf)
            self.logger.info(f"Zip Created : {filename}")
            zipf.close()
            res = self.__upload_file_to_s3(filename, self.config["BUCKET_NAME"])
            if res == "ok":
                self.logger.info(f"File Uploaded Successfully : {filename}")

            if "DELETE_LOCAL" in self.config.keys():
                if self.config['DELETE_LOCAL']:
                    os.remove(filename)
            return "ok"
        except Exception as e:
            self.logger.error("Something Happened: " + str(e))
            return e
