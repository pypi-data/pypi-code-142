import paramiko
import os
import datetime

class SSHHost:
    def __init__(self, hostname, user, keylocation=None, pasw = None):
        self.__hostname = hostname
        self.__keylocation = keylocation
        self.__user = user
        self.__pasw = pasw
        
    @property
    def hostname(self):
         return self.__hostname
     
    @property
    def key(self):
         return self.__keylocation
    
    @property
    def user(self):
         return self.__user
    
    @property
    def password(self):
         return self.__pasw

class SSHClient:
    def __init__(self, host: SSHHost, ignore_files=[]):
        self.__host = host
        self.client = paramiko.SSHClient()
        self.__commands = []
        self.ignore_files = ignore_files
        self.ftp_client = None
        # try:
        #     with open('upload_ignore.txt', 'r') as f:
        #         self.ignore_files = str(f.read()).split("\n")
        # except Exception as e:
        #     print(e)
        
    def __del__(self):
        try:
            self.ftp_client.close()
            self.client.close()
        except Exception as e:
            print(e)
        
    @property
    def getDate(self):
        return str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    
    def out(self, out_text, break_line=False):
        text = self.getDate + "=> \t "
        text += '\n'+ out_text if break_line else out_text
        print(text)
    
    def connect(self):
        try:
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.client.connect(hostname=self.__host.hostname, username = self.__host.user, password=self.__host.password, key_filename=self.__host.key)
            self.ftp_client = self.client.open_sftp()
        except Exception as e:
            print(e)
            
    def command(self, command):
        try:
            self.__commands.append(command)
        except Exception as e:
            print(e)
    
    def send_commands(self):
        try:
            stdin , stdout, stderr = self.client.exec_command(";".join(self.__commands))
            text_error = stderr.read().decode()
            if not text_error:
                text_out = stdout.readlines() 
                self.out("".join(text_out),True)
            else:
                print(text_error)
        except Exception as e:
            print(e)
    
    def download_file(self, local_file, out_dir_file):
        try:
            self.ftp_client.get(local_file, out_dir_file)
        except Exception as e:
            print(e)

    def upload_file(self, local_file, remote_file):
        try:
            self.ftp_client.put(local_file, remote_file)
            self.out("Uploaded: " + remote_file)
        except Exception as e:
            print(e)
    
    def mkdir(self, dir_name, mode=511):
        try:
            self.ftp_client.mkdir(dir_name, mode)
        except Exception as e:
            pass
    
    def create_locate(self, remote_dir):
        try:
            l = []
            locates = str(remote_dir).split("/")
            for locate in locates:
                l.append(locate)
                self.mkdir("/".join(l))
        except Exception as e:
            pass
    
    
    def upload_dir(self, local_dir_master, remote_dir_master):
        try:
            self.remote_master = remote_dir_master
            self.create_locate(self.remote_master)
            self.out("Upload dir: " + remote_dir_master)
            
            def upload(local_dir, remote_dir):
                try:
                    for item in os.listdir(local_dir):
                        if os.path.isfile(os.path.join(local_dir, item)):
                            if item not in self.ignore_files:
                                self.upload_file(os.path.join(local_dir, item), '%s/%s' % (remote_dir, item))
                        else:
                            new_remote_dir = '%s/%s' % (remote_dir, item)
                            if new_remote_dir.replace(self.remote_master+"/","") not in self.ignore_files:
                                self.mkdir(new_remote_dir)
                                self.out("Created: " + new_remote_dir)
                                upload(os.path.join(local_dir, item), new_remote_dir)
                except Exception as e:
                    print(e)
                    
            upload(local_dir_master, remote_dir_master)
        except Exception as e:
            print(e)