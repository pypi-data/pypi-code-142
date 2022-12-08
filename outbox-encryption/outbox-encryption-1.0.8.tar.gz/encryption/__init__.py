# Ref : 
#   https://www.geeksforgeeks.org/fernet-symmetric-encryption-using-cryptography-module-in-python/
#   https://able.bio/rhett/how-to-set-and-get-environment-variables-in-python--274rgt5

import binascii
import os
from io import StringIO
from pathlib import Path

from cryptography.fernet import Fernet  # pip install cryptography
from decouple import Config, Csv, RepositoryEnv  # pip install python-decouple

class OutboxEncryption:
    '''
        Rules:
            Di semua linux yg aktif environmnetnya selalu ada variabel environment PS1
            Di windows variabel VENV


            UPDATE :
                8 Desember 2022
                # Ubah env_list dari string menjadi array []
                # Ubah env_local dari string menjadi array []
                # Ubah env_server dari string menjadi array []

                DI local 
                    iwan : django-outbox-dev
                    dony : outbox
                    
                Di server pythonanywhere 
                    env_outbox
                    
                Di server niaga hoster
                    ((outbox:3.10))

                Cari identifier sama persis data di atas
    '''


    keyword_local = []              # keyword must be only exist in local, if not assumtion script run in server
    # keyword_server = []             # agar bisa setting server 1 dan server 2 berbeda

    # PS1 for environmnet linux
    # VENV for environment windows
    env_list = ['PS1', 'VENV']                # os.environ.get("PS1") --> list of environment
    # env_local = '.env.local'        # environment name local    (DELETE pending)
    # env_server = '.env.server'      # environment name server   (DELETE pending)
    env_name = '.env'               # + keyword_local (after string replace all symbol to _)
    BASE_DIR = ''

    # constructor
    def __init__(self, base_dir=None):
        # self.keyword_local = ['env_opd'] # lets empty (for remainder user to insert keywordlocal)
        # self.keyword_server = ['env_opd', 'outbox', 'env_outbox']

        if not base_dir:
            self.BASE_DIR = Path(__file__).resolve().parent.parent
        else:
            self.BASE_DIR = base_dir
        # pass        
    
    def bytes2hex(self, bytes_text):
        res_hex = binascii.hexlify(bytes_text)
        return res_hex.decode()

    def hex2bytes(self, hex_text):
        res_bytes = binascii.unhexlify(hex_text)
        return res_bytes    # return in bytes format

    def generate_key(self):
        # save key to file
        return Fernet.generate_key()
    
    def encrypt(self, plain_text, key):
        # key created using generate_key()
        f = Fernet(key)

        # the plain_text is converted to ciphertext
        return f.encrypt(plain_text)

    def decrypt(self, cipher_text, key):
        # Load existing key
        f = Fernet(key)
        
        # the ciphertext converted to plain_text
        return f.decrypt(cipher_text)

    def clear_keyword_local(self):    # Untuk create env file lainnya
        self.keyword_local.clear()

    def set_keyword_local(self, keyword):
        '''
            Update keyword sesuai project, misal :
            env_opd
            env_outbox
        '''
        # keyword = keyword.replace('-','_') # pindah ke pada saat create file
        # keyword = keyword.replace(':','_')
        # keyword = keyword.replace('.','_')
        self.keyword_local.append(keyword)

    def create_env_file(self, file_path):
        if not Path(file_path).is_file():
            with open(file_path, "w") as f:
                f.write('\n') 
                f.close()

            if Path(file_path).is_file():
                print('File is created')
            else:
                print('Fail create!')
        # else:
        #     print('Fail updated!')

    def string_replace(self, keyword):
        res = keyword.replace('-','_')
        res = res.replace(':','_')
        res = res.replace('.','_')
        return res

    def string_replace_env(self, keyword):
        res = keyword.replace('(','')
        res = res.replace(')','')        
        return res.strip()

    def encrypt_environ(self, plain_text):
        '''
            Write directly to environment file
            plain_text in dictionary format :
                # {db_password: 123},
                {secret_key: &#^@#&^$^}
                # {etc: etc..}
        '''
        if not self.keyword_local:
            print("Please set keyword_local fisrt!")
        else:
            
            file_path  = []
            
            # 1. Read ALL data
            for i in range(len(self.keyword_local)):                
                tmp = self.env_name + '.' + self.string_replace(self.keyword_local[i])
                file_path.append(os.path.join(self.BASE_DIR, tmp))
                # print('file_path =', file_path, Path(file_path).is_file())
                
                # create file if not exists
                self.create_env_file(file_path[i])
                

                # # create file if not exists
                # if not Path(file_path).is_file():
                #     with open(file_path, "w") as f:
                #         f.write('\n') 
                #         f.close()

                #     if Path(file_path).is_file():
                #         print('File is created')
                #     else:
                #         print('Fail create!')
                # else:
                #     print('Fail updated!')

            # print(file_path)
            for j in range(len(file_path)):
                dict1 = {}                

                with open(file_path[j], "r") as f:
                    for line in f.readlines():                
                        values = line.split('=')
                        if len(values) > 1:                    
                            dict1[values[0]] = values[1]
                    f.close()
                        
                
                # 2. Encrypt data        
                key = self.generate_key()
                # print(key)
                key_in_hex = self.bytes2hex(key)
                # print(key_in_hex)

                # get key, value from parameter (plain_text)
                values = list(plain_text.values())        
                keys = list(plain_text.keys())

                # Khusus data yg di enkripsi aja (simpan di parameter plain_text)
                # data yg tidak di enkripsi seperti debug=True dll, di tulis manual
                enc = []
                enc_in_hex = []
                for i in range(len(keys)):
                    tmp = self.encrypt(values[i].encode(), key)
                    enc.append(tmp)
                    enc_in_hex.append(self.bytes2hex(tmp))

                # 3. Update Data        
                # dict1['DB_USER'] = '123\n'
                for i in range(len(keys)):
                    dict1[keys[i]] = enc_in_hex[i]

                dict1['DB_KEY'] = key_in_hex

                # 4. Write Back Data        
                values = list(dict1.values())        
                keys = list(dict1.keys())

                with open(file_path[j], "w") as f:
                    # tulis ulang DB_KEY (Penambahan ada di dict1)           
                    # f.write('DB_KEY' + '=' + key_in_hex + '\n')
                    
                    # tulis ulang DB_PASSWORD, SECRET_KEY
                    for i in range(len(keys)):
                        if '\n' in values[i]:
                            f.write(keys[i] + '=' + values[i])
                        else:
                            f.write(keys[i] + '=' + values[i] + '\n') 

                    f.close()

                print('File is create on :', file_path[j])
                    
    def decrypt_environ(self, mplaint_key, mplaint_list=[], mplaint_tuple=[]): #, env_name, cipher_text, key_hex):
        '''        
            Read directly from environment file
            cipher_text and key_hex, in hexadecimal format            
        '''
        # text = self.hex2bytes(cipher_text)
        # key = self.hex2bytes(key_hex)
        # BASE_DIR = Path(__file__).resolve().parent.parent

        # env_list = os.environ.get(self.env_list)
        if not self.keyword_local:
            print("Please set keyword_local fisrt!")
        else:
            
            file_path  = []
            find_env_name = [] 

            # 1. Read ALL data
            for i in range(len(self.keyword_local)):                
                find_env_name.append(self.string_replace(self.keyword_local[i]))
                tmp = self.env_name + '.' + find_env_name[i]
                file_path.append(os.path.join(self.BASE_DIR, tmp))
                # print('file_path =', file_path, Path(file_path).is_file())
                
                # create file if not exists
                self.create_env_file(file_path[i])

            # print('file_path = ',file_path)

            # Baca data dari variable ENV, jika ketemu data dari list (keyword_local) maka load data dari file itu
            for j in range(len(self.env_list)):   
                env_list_split = []
                env_list_split2 = [] # karena ada tag pembuka dan penutup, maka split 2 kali

                # print('preses ', self.env_list[j])
                env_list = os.getenv(self.env_list[j]) # PS1 atau VENV
                # env_list = os.environ.get(self.env_list[j]) # PS1 atau VENV
                is_found = False
                file_path_idx = 0

                # test
                # env_list = 'outbox'
                # env_list = "(\[\033[0;34m\]django-outbox-dev\[\033[0;0m\]) \[\033[0;31m\]✘-127\[\033[0;0m\] \[\033[0;33m\]\w\[\033[0;0m\] [\[\033[0;35m\]${GIT_BRANCH}\[\033[0;0m\]|\[\033[0;34m\]✚ 44\[\033[0;0m\]\[\033[0;36m\]…7\[\033[0;0m\]\[\033[0;0m\]] \n\[\033[0;37m\]$(date +%H:%M)\[\033[0;0m\] $"
                # env_list = '((outbox:3.10)) '
                # env_list = "(env_outbox) \[\033[0;37m\]$(date +%H:%M) \w\[\033[0;33m\] $(parse_git_branch)\[\033[1;32m\]$ \[\033[0;37m\]"
                if env_list:
                    env_list_split = env_list.split('\[')
                    for i in env_list_split:
                        for k in i.split('\]'):
                            env_list_split2.append(self.string_replace_env(k))  # clear tanda (()) di dalam env


                # print('env_list_split2',env_list_split2)

                # create file if not exists        
                # create sebelum dibaca oleh RepositoryEnv di path tersebut jika tidak ada file maka akan muncul error
                # file_path = self.BASE_DIR / self.env_local
                # if not Path(file_path).is_file():
                #     with open(file_path, "w") as f:
                #         f.write('\n') 
                #         f.close()               

                #     if Path(file_path).is_file(): 
                #         print('File is created')
                #     else:
                #         print('Fail create!')
                # # else:
                # #     print('Fail updated!')

                # file_path = self.BASE_DIR / self.env_server
                # if not Path(file_path).is_file():
                #     with open(file_path, "w") as f:
                #         f.write('\n') 
                #         f.close()

                #     if Path(file_path).is_file(): 
                #         print('File is created')
                #     else:
                #         print('Fail create!')

                    # print('File is created')

                # print('self.keyword_local = ' , self.keyword_local)
                # print('env_list = ', env_list)
                if env_list:
                    file_path_idx = -1
                    for i in self.keyword_local:
                        # print('i=',i)
                        file_path_idx += 1
                        if i in env_list_split2:
                            # env_config = Config(RepositoryEnv(self.BASE_DIR / self.env_local))
                            # print('file_path[i] = ', file_path_idx, file_path[file_path_idx])

                            env_config = Config(RepositoryEnv(file_path[file_path_idx]))
                            # file_path = os.path.join(self.BASE_DIR, self.env_local)
                            print('Load setting from ' + self.keyword_local[file_path_idx])
                            
                            is_found = True
                            # print('FOUND!!!!')
                            break

                # if is_run_from_server:
                #     env_config = Config(RepositoryEnv(file_path[i]))
                #     # file_path = os.path.join(self.BASE_DIR, self.env_server)
                #     print('Load setting from ' + self.keyword_local[i])
                

                # print('File is load from :', file_path)
                # Get ALL env_config data

                if is_found:
                    dict1 = {}        
                    with open(file_path[file_path_idx], "r") as f:
                        for line in f.readlines():                
                            values = line.split('=')
                            if len(values) > 1:                    
                                dict1[values[0]] = values[1].replace('\n','')
                        f.close()

                    # print(dict1)
                    keys = list(dict1.keys())
                    values = list(dict1.values())
                    # print(keys)

                    # decrypt DB_KEY
                    # dapatkan key dulu untuk proses decrypt yg lain
                    tmp_keys = ''
                    for i in range (len(keys)):        
                        if keys[i]=='DB_KEY':                
                            tmp_keys = self.hex2bytes(values[i])                
                            # dict1[keys[i]] = tmp_keys # key tetap rahasia, jangan disimpan di dict
                            break

                    for i in range (len(keys)):        
                        if keys[i] in mplaint_key:  # khusus tipe data enkripsi
                            tmp = self.hex2bytes(values[i])
                            tmp = self.decrypt(tmp, tmp_keys).decode()
                            # print(keys[i], tmp)                
                            dict1[keys[i]] = tmp

                        elif keys[i] in mplaint_list:   # khusus tipe data list
                            # dict1[keys[i]] = env_config(keys[i], cast=lambda v: [s.strip() for s in v.split(',')])
                            dict1[keys[i]] = env_config(keys[i], cast=Csv())

                        elif keys[i] in mplaint_tuple:   # khusus tipe data tuple
                            # contoh di environment : os.environ['SECURE_PROXY_SSL_HEADER'] = 'HTTP_X_FORWARDED_PROTO, https'
                            # proses casting : config('SECURE_PROXY_SSL_HEADER', cast=Csv(post_process=tuple))  <--
                            # ('HTTP_X_FORWARDED_PROTO', 'https')
                            
                            dict1[keys[i]] = env_config(keys[i], cast=Csv(post_process=tuple))

                        else:                           # konversi sesuai tipe data python standart
                            # print(keys[i], values[i])
                            #dict1[keys[i]] = values[i]
                            # Ambil sesuai tipe data
                            if values[i] in ['True', 'False']:
                                dict1[keys[i]] = env_config(keys[i], default=True, cast=bool)
                            elif values[i].isnumeric():
                                dict1[keys[i]] = env_config(keys[i], default=0, cast=int)

                        # selain kondisi di atas, biarkan apa adanya (default = string)

                    # print('hasilnya = ', dict1)
                    return dict1
                else:
                    print('Activate environment first!')
                

# test module level
if __name__=='__main__':
    # print('Begin Test ENCRYPTION')
    # print('---------------------')
    # secret_text = input("Input Secret Text: ")    

    lib = OutboxEncryption()
    # key = lib.generate_key()    

    # # Out key in hexadecimal format
    # key = lib.bytes2hex(key)
    # print('Key:', key)
    
    # res_enc = lib.encrypt(secret_text.encode(), lib.hex2bytes(key))

    # # Out in hexadecimal
    # res_enc = lib.bytes2hex(res_enc)
    # print('Encrypt result:', res_enc)

    # print('')
    # print('Begin Test DECRYPTION')
    # print('---------------------')
    
    # res_dec = lib.decrypt(lib.hex2bytes(res_enc), lib.hex2bytes(key))
    # print('Decrypt result:', res_dec.decode())
    # print('')
    
    print('')
    print('Encrypt to Environment')
    print('----------------------')
    # BASE_DIR = Path(__file__).resolve().parent.parent
    # print(BASE_DIR)

    # mplaint_text = {
    #     'DB_PASSWORD': 'password untuk koneksi ke database',
    #     'SECRET_KEY': 'secret key yg ada di setting.py'
    # }

    mplaint_text = {
        'DB_PASSWORD': '',
        'SECRET_KEY': 'xxg_7me8rl2m#a_h2oresgt2#ni=3_4*!ai*=rtsq)yi!g7_5-51xx'
    }
    lib.set_keyword_local('django-outbox-dev')      # iwan
    lib.set_keyword_local('outbox')                 # dony
    lib.set_keyword_local('env_outbox')             # python anywhere
    lib.set_keyword_local('outbox:3.10')            # niaga hoster


    lib.encrypt_environ(mplaint_text)
    print('Show Hidden File to Show .env.local')


    # print('')
    # print('Decrypt From Environment')
    # print('----------------------')
    # # agar bisa mendeteksi environment local
    # lib.set_keyword_local('django-outbox-dev')

    # kunci yg di buka khusus, karena ada proses enkripsi
    # selain kunci ini, langsung ambil datanya, tipe data string

    # mplaint_key = list(mplaint_text.keys())
    mplaint_list = ['localhost:8000', '127.0.0.1:8000']    # daftar tipe data list (cara konversinya khsusus)
    # mplaint_tuple = ['SECURE_PROXY_SSL_HEADER']

    # mplaint_key = [
    #     'DB_PASSWORD', 'SECRET_KEY'
    # ]

    lib.decrypt_environ(mplaint_text, mplaint_list)
    print('Decrypt Finish')
