
import WZCMCCAPPLOGGER.GetNetWorkInfo
import WZCMCCAPPLOGGER.LogUploader

name = "WZCMCCAPPLOGGER"

#API  DB  Redis
log_type="DB"
dbhost ='10.77.18.248,8433';


def InsertLog(APPID):

    dbuser = 'cmcclogger'
    dbpwd = 'log$zj123'
    dbname = 'WZCMCCAPPLOGGER'

    mac = WZCMCCAPPLOGGER.GetNetWorkInfo.get_mac_address();
    pcname = WZCMCCAPPLOGGER.GetNetWorkInfo.get_hostName();
    ip = WZCMCCAPPLOGGER.GetNetWorkInfo.get_hostip();

    sql ="""insert into CMCCAPPLOG(APPID,PCNAME,MAC,IP)  values ('{APPID}','{pcname}','{mac}','{ip}')""".format(APPID=APPID,pcname=pcname,mac=mac,ip=ip)
    _Obdcsql = LogUploader.Obdcsql(dbhost,dbuser,dbpwd,dbname)
    _Obdcsql.insert_record(sql)

__version__ = "0.78.0"

