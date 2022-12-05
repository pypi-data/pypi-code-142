import os
# 判断系统类型，如果是windows则引入wexpect，如果是linux则引入pexpect
if os.name == 'nt':
    import wexpect as pexpect
else:
    import pexpect
password_key = '.*assword.*'

def ssh_is_file_exist(remote_path, ip, user_name, password, port=22):
    ssh = pexpect.spawn('ssh -p %s %s@%s ls %s' % (port, user_name, ip, remote_path))
    try:
        i = ssh.expect([password_key, pexpect.EOF, pexpect.TIMEOUT], timeout=60)
        if i == 0:
            ssh.sendline(password)
            ssh.expect(pexpect.EOF)
        file_list_str = ssh.before
        if 'No such file or directory' in file_list_str:
            return False
        return True
    except pexpect.EOF:
        print('EOF')
        ssh.close()
        return False

# 获取列表下所有文件以及文件夹，并且获取这些文件的大小以及更新时间, 自动输入密码
def ssh_get_file_list(remote_path, ip, user_name, password, port=22):
    # ssh = pexpect.spawn('ssh %s@%s ls -l %s' % (user_name, ip, remote_path))
    ssh = pexpect.spawn('ssh -p %s %s@%s ls -l %s' % (port, user_name, ip, remote_path))
    try:
        i = ssh.expect([password_key, pexpect.EOF, pexpect.TIMEOUT], timeout=60)
        if i == 0:
            ssh.sendline(password)
            ssh.expect(pexpect.EOF)
        # 判断系统如果是windows，则不需要进行decode, 如果是linux则需要进行decode
        if os.name == 'nt':
            file_list_str = ssh.before
        else:
            file_list_str = ssh.before.decode('utf-8')
        if 'No such file or directory' in file_list_str:
            return None
        file_list = file_list_str.split('\r\n')
        file_list = file_list[1:-1]
        # 对列表进行处理成一个字典的列表，键分别为权限，文件个数，所有者，所属组，大小，更新时间，文件名
        file_list_dict = []
        for f in file_list:
            file_dict = {}
            f = f.split()
            if len(f) != 9:
                continue
            file_dict['permissions'] = f[0]
            file_dict['number'] = f[1]
            file_dict['owner'] = f[2]
            file_dict['group'] = f[3]
            file_dict['size'] = f[4]
            file_dict['time'] = f[5] + ' ' + f[6] + ' ' + f[7]
            file_dict['name'] = f[8]
            file_list_dict.append(file_dict)
        return file_list_dict
    except pexpect.EOF:
        print('EOF')
        ssh.close()
        return None
    except pexpect.TIMEOUT:
        print('TIMEOUT')
        ssh.close()
        return None
   
def ssh_download_file(remote_path, local_path, ip, user_name, password, port=22):
    # cmd = 'scp %s@%s:%s %s' % (user_name, ip, remote_path, local_path)
    cmd = 'scp -P %s %s@%s:%s %s' % (port, user_name, ip, remote_path, local_path)
    ssh = pexpect.spawn(cmd)
    # 不设置超时时间，因为下载文件的时间不确定
    try:
        i = ssh.expect([password_key, pexpect.EOF, pexpect.TIMEOUT])
        if i == 0:
            ssh.sendline(password)
            ssh.expect(pexpect.EOF)
        return True
    except pexpect.EOF:
        print('EOF')
        ssh.close()
        return False
    
def ssh_upload_file(local_path, remote_path, ip, user_name, password, port=22):
    # cmd = 'scp %s %s@%s:%s' % (local_path, user_name, ip, remote_path)
    # 先判断文件是否存在，如果存在，则把原来文件名重命名成_bak
    if ssh_is_file_exist(remote_path + '/' + local_path, ip, user_name, password, port):
        ssh_rename_file(remote_path + '/' + local_path, remote_path + '/' + local_path + '_bak', ip, user_name, password, port)
    cmd = 'scp -P %s %s %s@%s:%s' % (port, local_path, user_name, ip, remote_path)
    ssh = pexpect.spawn(cmd)
    # 不设置超时时间，因为下载文件的时间不确定
    try:
        i = ssh.expect([password_key, pexpect.EOF, pexpect.TIMEOUT])
        if i == 0:
            ssh.sendline(password)
            ssh.expect(pexpect.EOF)
        return True
    except pexpect.EOF:
        print('EOF')
        ssh.close()
        return False
    
def ssh_rename_file(old_path, new_path, ip, user_name, password, port=22):
    # 先判断文件是否存在
    if not ssh_get_file_list(old_path, ip, user_name, password, port):
        return False
    # cmd = 'ssh %s@%s mv %s %s' % (user_name, ip, old_path, new_path)
    cmd = 'ssh -p %s %s@%s mv %s %s' % (port, user_name, ip, old_path, new_path)
    ssh = pexpect.spawn(cmd)
    try:
        i = ssh.expect([password_key, pexpect.EOF, pexpect.TIMEOUT], timeout=60)
        if i == 0:
            ssh.sendline(password)
            ssh.expect(pexpect.EOF)
        return True
    except pexpect.EOF:
        print('EOF')
        ssh.close()
        return False
    except pexpect.TIMEOUT:
        print('TIMEOUT')
        ssh.close()
        return False
    
def ssh_delete_file(path, ip, user_name, password, port=22):
    # 先判断文件是否存在
    if not ssh_get_file_list(path, ip, user_name, password, port):
        return False
    # cmd = 'ssh %s@%s rm -rf %s' % (user_name, ip, path)
    cmd = 'ssh -p %s %s@%s rm -rf %s' % (port, user_name, ip, path)
    ssh = pexpect.spawn(cmd)
    try:
        i = ssh.expect([password_key, pexpect.EOF, pexpect.TIMEOUT], timeout=60)
        if i == 0:
            ssh.sendline(password)
            ssh.expect(pexpect.EOF)
        return True
    except pexpect.EOF:
        print('EOF')
        ssh.close()
        return False
    except pexpect.TIMEOUT:
        print('TIMEOUT')
        ssh.close()
        return False
    
def ssh_create_file(path, ip, user_name, password, port=22):
    # 先判断path是否存在
    if ssh_get_file_list(path, ip, user_name, password, port):
        return False
    # cmd = 'ssh %s@%s touch %s' % (user_name, ip, path)
    cmd = 'ssh -p %s %s@%s touch %s' % (port, user_name, ip, path)
    ssh = pexpect.spawn(cmd)
    try:
        i = ssh.expect([password_key, pexpect.EOF, pexpect.TIMEOUT], timeout=60)
        if i == 0:
            ssh.sendline(password)
            ssh.expect(pexpect.EOF)
        return True
    except pexpect.EOF:
        print('EOF')
        ssh.close()
        return False
    except pexpect.TIMEOUT:
        print('TIMEOUT')
        ssh.close()
        return False
    
def ssh_create_dir(path, ip, user_name, password, port=22):
    # 先判断path是否存在
    if ssh_get_file_list(path, ip, user_name, password, port):
        return False
    # cmd = 'ssh %s@%s mkdir %s' % (user_name, ip, path)
    cmd = 'ssh -p %s %s@%s mkdir %s' % (port, user_name, ip, path)
    ssh = pexpect.spawn(cmd)
    try:
        i = ssh.expect([password_key, pexpect.EOF, pexpect.TIMEOUT], timeout=60)
        if i == 0:
            ssh.sendline(password)
            ssh.expect(pexpect.EOF)
        return True
    except pexpect.EOF:
        print('EOF')
        ssh.close()
        return False
    except pexpect.TIMEOUT:
        print('TIMEOUT')
        ssh.close()
        return False
    
def ssh_get_file_size(path, ip, user_name, password, port=22):
    # cmd = 'ssh %s@%s du -sh %s' % (user_name, ip, path)
    cmd = 'ssh -p %s %s@%s du -sh %s' % (port, user_name, ip, path)
    ssh = pexpect.spawn(cmd)
    try:
        i = ssh.expect([password_key, pexpect.EOF, pexpect.TIMEOUT], timeout=60)
        if i == 0:
            ssh.sendline(password)
            ssh.expect(pexpect.EOF)
            file_size = ssh.before.decode('utf-8').split('\r\n')[1].split()[0]
            return file_size
        else:
            return None
    except pexpect.EOF:
        print('EOF')
        ssh.close()
        return None
    except pexpect.TIMEOUT:
        print('TIMEOUT')
        ssh.close()
        return None
    
def ssh_tail_log(path, ip, user_name, password, port=22):
    # 持续获取tail -f日志内容
    ssh = pexpect.spawn('ssh -p %s %s@%s tail -f %s' % (port, user_name, ip, path))
    # 打印出指令
    print('ssh -p %s %s@%s tail -f %s' % (port, user_name, ip, path))
    try:
        i = ssh.expect([password_key, pexpect.EOF, pexpect.TIMEOUT], timeout=60)
        if i == 0:
            ssh.sendline(password)
            print(ssh.before.decode('utf-8'))
            while True:
                i = ssh.expect([pexpect.EOF, pexpect.TIMEOUT], timeout=60)
                if i == 0:
                    print('EOF')
                    break
                elif i == 1:
                    print('TIMEOUT')
                    break
                elif i == 2:
                    print(ssh.before.decode('utf-8'))
        else:
            return None
    except pexpect.EOF:
        print('EOF')
        ssh.close()
        return None
    
if __name__ == '__main__':
    ip = '10.10.8.156'
    user_name = 'dxr'
    password = '0'
    print(ssh_get_file_list('/home/dxr', ip, user_name, password))
    res = ssh_tail_log('/home/dxr/send_robot_info/nohup.out', ip, user_name, password)
    print(res)
    