
import CMCCAPPLOG.GetNetWorkInfo
import CMCCAPPLOG.LogUploader

name = "CMCCAPPLOG"

#API  DB  Redis
log_type="DB"

def InsertLog():

    mac = CMCCAPPLOG.GetNetWorkInfo.get_mac_address();
    pcname = CMCCAPPLOG.GetNetWorkInfo.get_hostName();
    ip = CMCCAPPLOG.GetNetWorkInfo.get_hostip();

    sql ="""insert into CMCCAPPLOG(APPID,MAC,IP)  values ('{pcname}','{mac}','{ip}')""".format(pcname=pcname,mac=mac,ip=ip)
    _Obdcsql = LogUploader.Obdcsql('10.77.18.248,8433','sa','zhyw$zj123','WZGJGLAPI')
    _Obdcsql.insert_record(sql)

#InsertLog()
__version__ = "0.78.0"