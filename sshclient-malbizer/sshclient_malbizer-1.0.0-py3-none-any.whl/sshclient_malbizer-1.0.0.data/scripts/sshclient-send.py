from sshclient.sshclient import SSHHost, SSHClient
import sys

class Command:
    def __init__(self, filelocation):
        self.host = None
        self.client = None
        self.file_location = filelocation
        self.file = None
        
        
    def start(self):
        try:
            with open(self.file_location,'r') as f:
                self.file = f.read()
        except Exception as e:
            print("Erro ao abrir arquivo de configuração... ", e)
            
        for line in self.file.split("\n"):
            self.commandRead(line)
    
    def commandRead(self, line):
        values = line.split("|")
        if values[0]=='init':
            config = values[1].split(",")
            self.host = SSHHost(config[0], config[1], config[3], config[2])
            self.client = SSHClient(self.host)
            self.client.connect()
            
        elif values[0]=='uploaddir':
            dirs = values[1].split(",")
            self.client.upload_dir(dirs[0],dirs[1])
            
        elif values[0]=='comm':
            self.client.command(values[1])
        
        elif values[0]=='sendcomm':
            self.client.send_commands()
        
        elif values[0]=='ignorefiles':
            self.client.ignore_files = values[1].split(",")
            
            
res = sys.argv

if len(res)<2:
    print('Envie a localização do arquivo de comandos como argumento...')
else:
    cmd = Command(res[1])
    cmd.start()

