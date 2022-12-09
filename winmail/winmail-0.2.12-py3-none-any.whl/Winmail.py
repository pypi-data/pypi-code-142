# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import os
from .utils import SqliteDb, MySqlDb, PostgreDb

DB_TYPES = ['mysqlin', 'mysql', 'pgsql']


def xml_replace(xml_path: str):
    """
    xml文件中特殊字符的替换，XML有标准字符，如&不可以出现。使用前要做处理。
    注意XML标准不允许使用&符号，Winmail配置中有可能出现，必须事先处理。
    将&符号替换为(|and|)，在返回结果时再把"(|and|)"替换成&。
    """
    xml = ""
    with open(xml_path, 'r', encoding="utf-8") as fd:
        for line in fd:
            if "&" in line:
                line = line.replace("&", "(|and|)")
            xml += line

    return xml


def xml_unreplace(s):
    """
    把xmlReplace()替换的字符替换回去。
    """
    result = s
    if "(|and|)" in s:
        result = s.replace("(|and|)", "&")
    return result


def get_xml_element_value(xml_path, element_path):
    """
    使用ET的查找返回element节点。返回结果
    注意XML标准不允许使用&符号，Winmail的system.cfg配置中有可能出现，在读取之前必须事先处理。
    将&符号替换为(|and|)，在返回结果时再把"(|and|)"替换成&。
    使用函数xmlReplace()xmlUnReplace()处理。

    :xml_path: 配置文件完整路径
    :element_path: XML路径
    :return:
    """

    xml = xml_replace(xml_path)

    root = ET.fromstring(xml)
    it = root.find(element_path)
    # print(f'{xml_path}: {element_path}-> {it.text}')
    if it is None:
        return ''
    else:
        if it.text is None:
            return ''
        return xml_unreplace(it.text)


def get_all_xml_element_value(xml_path, element_path):
    """
    查询配置文件中的有重复的项比如 ".//smtpoption//domaindelivery//domainhost//"
    """
    result = []
    xml = xml_replace(xml_path)

    root = ET.fromstring(xml)

    for it in root.findall(element_path):
        # print(it.tag, it.attrib, it.text)
        result.append(xml_unreplace(it.text))
    return result


def modify_xml_element(xml_path, element_path, value_text):
    """
    使用ET的findall查找返回element节点。直接给节点赋值返回bool。

    :xml_path: xml文件完整路径
    :element_path: 节点完整路径
    :value_text:节点值
    :return:
        bool
    """

    tree = ET.parse(xml_path)

    root = tree.getroot()

    for it in root.findall(element_path):
        # print(iter.text)
        it.text = value_text
    tree.write(xml_path, encoding="utf-8")
    for it in root.findall(element_path):
        if it.text != value_text:
            return False

    return True


def insert_xml_element(xml_path, element_path, element_target, element_text):
    """

    :xmlPath: XML文件路径
    :elementPath: 要插入到的节点
    :elementTarget: 要插入的节点名
    :elementText: 要插入的节点值
    :return:
        bool.
    """
    tree = ET.parse(xml_path)
    root = tree.getroot()

    # 使用ET.Element("elementTarget") 把节点先建好。
    node = ET.Element(element_target)
    node.text = "\n"
    node.text = element_text
    # 使用root.iter，打开节点，循环打开elementPath，直到最后一层，再使用append插入。
    pathList = []
    for i in element_path.split("/"):
        if i != "":
            pathList.append(i)

    n = len(pathList) - 1
    m = 0
    for i in pathList:

        if m == 0 and (root.tag == pathList[0] or pathList[0] == "."):
            m += 1
            continue

        iterTag = ""
        for it in root.iter(i):
            if ET.iselement(it):
                iterTag = it.tag
                it.text = "\\n" + it.text

        if iterTag == i:
            if m == n:
                # insert node插入切点位置
                for it in root.iter(i):
                    it.append(node)
                    tree.write(xml_path, encoding="utf-8")
                return True
            m += 1
            continue
        else:
            return False


def get_winmail_path():
    """
    获取Winmail的安装路径
    """

    winmail_path = None
    error_info = 'os.name check error!'

    if os.name == "nt":
        # 优先使用注册表取路径，如果失败从DLL取，DLL有32位64位区分，如果要打包，需要在不同环境分别打包。
        import winreg

        try:
            regkey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                                    "SYSTEM\\ControlSet001\\services\\MagicWinmailServer")
            winmail_path = os.path.dirname(
                winreg.QueryValueEx(regkey, "ImagePath")[0].split('\"')[1])  # ~Magic Winmail\\server\\
        except OSError as e:
            error_info = [f"Get winreg "
                          f"HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\services\\MagicWinmailServer"
                          f" error! see: {str(e)}"]

        if not winmail_path:
            try:
                regkey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                                        "SYSTEM\\CurrentControlSet\\services\\MagicWinmailServer")
                winmail_path = os.path.dirname(
                    winreg.QueryValueEx(regkey, "ImagePath")[0].split('\"')[1])  # ~Magic Winmail\\server\\
            except Exception as e:
                error_info.append(f"Get winreg "
                                  f"HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\services\\MagicWinmailServer"
                                  f" error! see: {str(e)}")
        if not winmail_path:
            try:
                from win32com.client import Dispatch

                dll = Dispatch("MailServerCtrl.MailDBInterface")
                dll.InitControl("")
                winmail_path = dll.GetDBPath()
            except Exception as e:
                error_info.append(f"Dispatch(\"MailServerCtrl.MailDBInterface\") error:{str(e)}")

    if os.name == "posix":
        from configparser import ConfigParser

        service_file = "/usr/lib/systemd/system/winmail.service"
        if os.path.isfile(service_file):
            winmail_service = ConfigParser()
            winmail_service.read(service_file)
            winmail_path = winmail_service['Service']['WorkingDirectory']
            error_info = 'Get Winmail Path from /usr/lib/systemd/system/winmail.service error!'
        if not winmail_path:
            winmail_path = "/opt/winmail"
            error_info = 'Get Winmail Path error!'

    if os.path.isdir(winmail_path):
        return winmail_path
    else:
        raise Exception(error_info)


class Winmail:
    """
    获取各Winmail相关的路径
    """

    def __init__(self, db_pwd=None):

        self.winmail_path = get_winmail_path()

        self.winmail_sys_conf_path = os.path.join(self.winmail_path, "data//system.cfg")
        self.winmail_domain_conf_path = os.path.join(self.winmail_path, "data//domain.db")
        self.winmail_mailgroup_conf_path = os.path.join(self.winmail_path, "data//mailgroup.db")
        self.winmail_mailuser_stat_conf_path = os.path.join(self.winmail_path, "data//mailuserstat.db")
        self.winmail_mailuser_conf_path = os.path.join(self.winmail_path, "data//mailuser.db")

        if not self.check_winmail_path():
            raise Exception("Get WinmailPath Error : self.winmailPath -> %s;" % self.winmail_path)

        self.db_type = self.get_db_type()
        self.db_pwd = db_pwd
        self.tblprefix = ''
        self.domain_table = 'domain'
        self.domainalias_table = 'domainalias'
        self.mailuser_table = 'mailuser'
        self.useralias_table = 'useralias'
        self.mailgroup_table = 'mailgroup'
        self.mailuser_stat_table = 'stat'

        # 如非sqlite数据库，从配置中取前缀并定义数据库表名，并取出数据库连接相关信息。系统自带的mysqlin使用root用户。密码在管理工具中显示。
        if self.db_type in DB_TYPES:
            self.tblprefix = get_xml_element_value(self.winmail_sys_conf_path, f'./dboption/{self.db_type}/tblprefix')

            self.domain_table = self.tblprefix + 'domain'
            self.domainalias_table = self.tblprefix + 'domainalias'
            self.mailuser_table = self.tblprefix + 'mailuser'
            self.useralias_table = self.tblprefix + 'useralias'
            self.mailgroup_table = self.tblprefix + 'mailgroup'
            self.mailuser_stat_table = self.tblprefix + 'mailuserstat'

            self.db_host = get_xml_element_value(self.winmail_sys_conf_path, f'./dboption/{self.db_type}/host')
            self.db_port = int(get_xml_element_value(self.winmail_sys_conf_path, f'./dboption/{self.db_type}/port'))
            if self.db_type == 'mysqlin':
                self.db_user = 'root'
            else:
                self.db_user = get_xml_element_value(self.winmail_sys_conf_path, f'./dboption/{self.db_type}/username')
            self.db_database = get_xml_element_value(self.winmail_sys_conf_path, f'./dboption/{self.db_type}/database')

    def connect_db(self, sqlite_db_path: str = None):
        """
        按数据库类型打开数据库

        :return: Object
        """

        if self.db_type == 'mysql':

            return MySqlDb(host=self.db_host, port=self.db_port,
                           user=self.db_user, pwd=self.db_pwd,
                           db=self.db_database)

        if self.db_type == 'mysqlin':

            return MySqlDb(host=self.db_host, port=self.db_port,
                           user=self.db_user, pwd=self.db_pwd,
                           db=self.db_database)

        if self.db_type == 'pgsql':

            return PostgreDb(host=self.db_host, port=self.db_port,
                             user=self.db_user, pwd=self.db_pwd,
                             db=self.db_database)

        if sqlite_db_path:
            return SqliteDb(sqlite_db_path)
        else:
            return SqliteDb()

    def get_sys_config(self, element_path):

        if os.path.isfile(self.winmail_sys_conf_path):
            value_string = get_xml_element_value(self.winmail_sys_conf_path, element_path)
            return value_string
        return None

    def get_db_type(self):

        db_type_element_path = "./dboption/dbtype"

        return self.get_sys_config(db_type_element_path)

    def check_winmail_path(self):
        """
        winmailPath:Winmail安装目录路径，要求指向到~magic Winmail\\server\\
        :return: bool
        """

        if os.path.isdir(self.winmail_path):
            if os.path.isfile(self.winmail_mailgroup_conf_path) \
                    and os.path.isfile(self.winmail_mailuser_stat_conf_path) \
                    and os.path.isfile(self.winmail_sys_conf_path) \
                    and os.path.isfile(self.winmail_domain_conf_path) \
                    and os.path.isfile(self.winmail_mailuser_conf_path):
                return True
        return False

    def get_user_mailstore_path(self, email):
        """
        获取用户的邮件存储路径
        :param email: 用户邮件地址
        :return: string。 路径
        """

        user, domain = email.split("@")
        mailstore_path = ""
        store_element_path = "./advanced/directory/mailstore"

        if self.check_pri_domain(domain):
            user_db_domain = ""
        else:
            user_db_domain = domain

        # 查询用户属性中的mailstorepath。

        user_sql = \
            f'select mailstorepath from {self.mailuser_table} where domain=\'{user_db_domain}\' and name=\'{user}\';'

        db_handel = self.connect_db()

        if self.db_type not in DB_TYPES:
            db_handel = self.connect_db(sqlite_db_path=self.winmail_mailuser_conf_path)

        db_handel.execute(user_sql)
        sql_result = db_handel.fetchone()
        db_handel.close()

        if isinstance(sql_result, tuple) and sql_result[0]:
            mailstore_path = sql_result[0]

        # check mailstorepath from domain.db.
        domain_sql = f"select mailstorepath from {self.domain_table} where domain=\'{domain}\';"
        # 未在用户表中查到路径时，在域名属性中检查是否有配置域的存储路径
        if not mailstore_path:

            db_handel = self.connect_db()
            if self.db_type not in DB_TYPES:
                db_handel = self.connect_db(sqlite_db_path=self.winmail_mailuser_conf_path)

            db_handel.execute(domain_sql)
            sql_result = db_handel.fetchone()
            db_handel.close()

            if isinstance(sql_result, tuple) and sql_result[0]:

                if user_db_domain:
                    mailstore_path = os.path.join(sql_result[0], f"{user}@{domain}")
                else:
                    mailstore_path = os.path.join(sql_result[0], f"{user}")

        # 未在用户和域属性中的配置路径下取system.cfg配置文件数据
        if not mailstore_path:

            mailstore_path = get_xml_element_value(self.winmail_sys_conf_path, store_element_path)

            # 如果配置文件中查到结果
            if mailstore_path:
                if user_db_domain:
                    mailstore_path += f"//{user}@{domain}"
                else:
                    mailstore_path += f"//{user}"
            # 结果为None或者为空字符时取系统安装目录
            else:
                if user_db_domain:
                    mailstore_path = self.winmail_path + f"//store//{user}@{domain}"
                else:
                    mailstore_path = self.winmail_path + f"//store//{user}"

        return mailstore_path

    def get_user_netstore_path(self, email):
        """
        获取用户的网盘路径
        :param email: 用户邮件地址
        :return: 字符串路径
        """

        user, domain = email.split("@")
        mailstore_path = ""
        store_element_path = "./advanced/directory/netstore"

        # 确定主域名是什么，mailuser.db中的主域查询是使用空字符串，普通域使用正常域名。
        if self.check_pri_domain(domain):
            user_db_domain = ""
        else:
            user_db_domain = domain

        # 查询用户属性中的mailstorepath。
        user_sql = \
            f'select ftpstorepath from {self.mailuser_table} where domain=\'{user_db_domain}\' and name=\'{user}\';'

        db_handel = self.connect_db()
        if self.db_type not in DB_TYPES:
            db_handel.open(self.winmail_mailuser_conf_path)

        db_handel.execute(user_sql)
        sql_result = db_handel.fetchone()
        db_handel.close()

        if isinstance(sql_result, tuple) and sql_result[0]:
            mailstore_path = sql_result[0]
        # 查询域名中的指定路径
        domain_sql = f"select ftpstorepath from {self.domain_table} where domain=\'{domain}\';"

        if not mailstore_path:

            db_handel = self.connect_db()
            if self.db_type not in DB_TYPES:
                db_handel.open(self.winmail_domain_conf_path)

            db_handel.execute(domain_sql)
            sql_result = db_handel.fetchone()
            db_handel.close()

            if isinstance(sql_result, tuple) and sql_result[0]:

                if user_db_domain:
                    mailstore_path = os.path.join(sql_result[0], f"{user}@{domain}")
                else:
                    mailstore_path = os.path.join(sql_result[0], f"{user}")

        # 查询system配置文件中路径
        if not mailstore_path:

            mailstore_path = get_xml_element_value(self.winmail_sys_conf_path, store_element_path)
            if mailstore_path:

                if user_db_domain:
                    mailstore_path += f"//{user}@{domain}"
                else:
                    mailstore_path += f"//{user}"
            else:

                if user_db_domain:
                    mailstore_path = self.winmail_path + f"//netstore//{user}@{domain}"
                else:
                    mailstore_path = self.winmail_path + f"//netstore//{user}"

        return mailstore_path

    def get_domain_mailstore_path(self, domain):
        """
        获取域名的邮件存储目录
        :param domain: 域名
        :return: 字符串路径
        """
        mailstore_path = ""
        store_element_path = "./advanced/directory/mailstore"

        domain_sql = f'select mailstorepath from {self.domain_table} where domain=\'{domain}\';'

        db_handel = self.connect_db()
        if self.db_type not in DB_TYPES:
            db_handel.open(self.winmail_domain_conf_path)

        db_handel.execute(domain_sql)
        sql_result = db_handel.fetchone()
        db_handel.close()

        if isinstance(sql_result, tuple) and sql_result[0]:
            mailstore_path = sql_result[0]

        # 域名属性中没有配置时取system.cfg配置。
        if not mailstore_path:

            mailstore_path = get_xml_element_value(self.winmail_sys_conf_path, store_element_path)
            if not mailstore_path:
                mailstore_path = os.path.join(self.winmail_path, "store")

        return mailstore_path

    def get_domain_netstore_path(self, domain):
        """
        获取域名的网盘路径
        """
        mailstore_path = ""
        store_element_path = "./advanced/directory/netstore"

        domain_sql = f'select ftpstorepath from {self.domain_table} where domain=\'{domain}\';'

        db_handel = self.connect_db()
        if self.db_type not in DB_TYPES:
            db_handel.open(self.winmail_domain_conf_path)

        db_handel.execute(domain_sql)
        sql_result = db_handel.fetchone()
        db_handel.close()

        if isinstance(sql_result, tuple) and sql_result[0]:
            mailstore_path = sql_result[0]

        if not mailstore_path:

            mailstore_path = get_xml_element_value(self.winmail_sys_conf_path, store_element_path)

            if not mailstore_path:
                mailstore_path = os.path.join(self.winmail_path, "netstore")

        return mailstore_path

    def get_mailbackup_path(self):
        """
        获取Winmail邮件备份路径
        """
        backup_element_path = ".//advanced//directory//mailbackup"

        if os.path.isfile(self.winmail_sys_conf_path):
            mail_backup_path = get_xml_element_value(self.winmail_sys_conf_path, backup_element_path)
            if mail_backup_path is None or mail_backup_path == '':
                mail_backup_path = os.path.join(self.winmail_path, "backup")
            return mail_backup_path
        return None

    def get_mailarchive_path(self):
        """
        获取winmail归档存储路径
        """
        archive_element_path = ".//advanced//directory//mailarchive"

        if os.path.isfile(self.winmail_sys_conf_path):
            mail_archive_path = get_xml_element_value(self.winmail_sys_conf_path, archive_element_path)
            # print(mail_archive_path)
            if mail_archive_path is None or mail_archive_path == '':
                mail_archive_path = os.path.join(self.winmail_path, "archive")
            return mail_archive_path
        return None

    def get_pri_domain(self):
        """
        返回结果包含域名和域别名中的已存在的域名
        :return: str domain域名
        """

        db_handel = self.connect_db()
        if self.db_type not in DB_TYPES:
            db_handel.open(self.winmail_domain_conf_path)

        db_handel.execute(f'select domain from {self.domain_table} where type=\'1\';')
        domain = db_handel.fetchone()[0]
        db_handel.close()
        return domain

    def get_domain_list(self):
        """
        返回结果包含域名域名
        :return:  list [domainName]域名
        """
        domain_list = []

        db_handel = self.connect_db()
        if self.db_type not in DB_TYPES:
            db_handel.open(self.winmail_domain_conf_path)

        db_handel.execute(f'select domain from {self.domain_table};')
        sql_result = db_handel.fetchall()
        if sql_result:
            for domain in sql_result:
                domain_list.append(domain[0])
        db_handel.close()
        return domain_list

    def get_all_domain_list(self):
        """
        返回结果包含域名和域别名中的已存在的域名
        :return:  list [domainName]域名
        """
        domain_list = []

        db_handel = self.connect_db()
        if self.db_type not in DB_TYPES:
            db_handel.open(self.winmail_domain_conf_path)

        db_handel.execute(f'select domain from {self.domain_table} union select domain from {self.domainalias_table};')
        sql_result = db_handel.fetchall()
        if sql_result:
            for domain in sql_result:
                domain_list.append(domain[0])
        db_handel.close()

        return domain_list

    def get_domain_tuple_list(self):
        """
        获取域名tuple组成的list
        :return:    tuple组成的list [(domainName,domainType)]域名,域类型（是否主域）
        """

        db_handel = self.connect_db()
        if self.db_type not in DB_TYPES:
            db_handel.open(self.winmail_domain_conf_path)
        db_handel.execute(f'select domain,type from {self.domain_table};')
        domain_list = db_handel.fetchall()
        db_handel.close()

        return domain_list

    def get_user_list(self):
        """
        获取用户列表
        :return:   list，[[email,fullname][email,fullname]]
        """

        pri_domain = ""

        domain_list = self.get_domain_tuple_list()
        if domain_list:
            for dl in domain_list:
                if dl[1] == 1:
                    pri_domain = dl[0]

        new_user_list = []

        db_handel = self.connect_db()
        if self.db_type not in DB_TYPES:
            db_handel.open(self.winmail_mailuser_conf_path)

        db_handel.execute(f'select name,domain,fullname from {self.mailuser_table};')
        user_list = db_handel.fetchall()
        db_handel.close()
        if user_list:
            for li in user_list:
                if li[1] == "":
                    new_user_list.append([li[0] + "@" + pri_domain, li[2]])
                else:
                    new_user_list.append([li[0] + "@" + li[1], li[2]])

        return new_user_list

    def get_user_alias_list(self):
        """
        获取用户别名列表。
        :return:   list，[[email,realuser],[email,realuser]]
        """
        pri_domain = ""

        domain_list = self.get_domain_tuple_list()
        if domain_list:
            for dl in domain_list:
                if dl[1] == 1:
                    pri_domain = dl[0]

        new_user_list = []

        db_handel = self.connect_db()
        if self.db_type not in DB_TYPES:
            db_handel.open(self.winmail_mailuser_conf_path)

        db_handel.execute(f'select name,domain,realuser from {self.useralias_table};')
        user_list = db_handel.fetchall()
        db_handel.close()
        if user_list:
            for li in user_list:
                if li[1] == "":
                    new_user_list.append([li[0] + "@" + pri_domain, li[2]])
                else:
                    new_user_list.append([li[0] + "@" + li[1], li[2]])
        return new_user_list

    def get_group_list(self):
        """
        获取组列表
        :return:  list[email,email]
        """
        pri_domain = ""

        domain_list = self.get_domain_tuple_list()
        if domain_list:
            for dl in domain_list:
                if dl[1] == 1:
                    pri_domain = dl[0]

        new_user_list = []

        db_handel = self.connect_db()
        if self.db_type not in DB_TYPES:
            db_handel.open(self.winmail_mailgroup_conf_path)
        db_handel.execute(f'select name,domain from {self.mailgroup_table};')
        user_list = db_handel.fetchall()
        db_handel.close()
        if user_list:
            for li in user_list:
                if li[1] == "":
                    new_user_list.append(li[0] + "@" + pri_domain)
                else:
                    new_user_list.append(li[0] + "@" + li[1])
        return new_user_list

    def check_pri_domain(self, domain):
        """
        通过Domain和tuple组成的list [(domainName:domainType)]域名:域类型（是否主域)对比。
        :param domain: 域名
        :return: bool
        """
        for i in self.get_domain_tuple_list():
            if i[1] == 1:
                if i[0] == domain:
                    return True
        return False


if __name__ == "__main__":
    wm = Winmail('123456')
    print(wm.db_type)
    print(wm.domain_table, wm.domainalias_table, wm.useralias_table, wm.mailuser_table, wm.mailgroup_table,
          wm.mailuser_stat_table)
    print(wm.get_user_mailstore_path('a@test.com'))
    print(wm.get_user_list())
    print(wm.get_pri_domain())
    print(wm.get_domain_list())
    print(wm.get_all_domain_list())
    print(wm.get_user_alias_list())

    print(wm.get_group_list())

    print(wm.get_mailbackup_path())
    print(wm.get_mailarchive_path())

    print("domain mailstore", wm.get_domain_mailstore_path("winmail.cn"))
    print("domain netstore", wm.get_domain_netstore_path("winmail.cn"))

    print("user mailstore", wm.get_user_mailstore_path("a@winmail.cn"))
    print("user netstore", wm.get_user_netstore_path("a@winmail.cn"))

    print(os.path.join(wm.get_domain_mailstore_path('winmail.cn'), 'AAAAA'))
