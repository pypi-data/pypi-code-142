
import WZCMCCAPPLOG.GetNetWorkInfo
import WZCMCCAPPLOG.LogUploader

name = "WZCMCCAPPLOG"

#API  DB  Redis
log_type="DB"
dbhost ='10.77.18.248,8433';
dbuser ='sa'
dbpwd= 'zhyw$zj123'
dbname = 'WZGJGLAPI'

def InsertLog():


    mac = WZCMCCAPPLOG.GetNetWorkInfo.get_mac_address();
    pcname = WZCMCCAPPLOG.GetNetWorkInfo.get_hostName();
    ip = WZCMCCAPPLOG.GetNetWorkInfo.get_hostip();

    sql ="""insert into CMCCAPPLOG(APPID,MAC,IP)  values ('{pcname}','{mac}','{ip}')""".format(pcname=pcname,mac=mac,ip=ip)
    _Obdcsql = LogUploader.Obdcsql('10.77.18.248,8433','sa','zhyw$zj123','WZGJGLAPI')
    _Obdcsql.insert_record(sql)

#InsertLog()
__version__ = "0.78.0"