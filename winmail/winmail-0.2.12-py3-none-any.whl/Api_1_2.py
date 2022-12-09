# -*- coding:utf-8 -*-
from typing import Dict, Optional, Any
from .OpenApi import OpenApi


class Api(OpenApi):

    def __init__(self, server: str, port: int, apikey: str, apisecret: str, use_ssl: bool = False) -> None:
        """
        初始化
        :param server: 服务器地址
        :param port:  端口
        :param apikey: APIkey
        :param apisecret: API密钥
        :param use_ssl:  是否使用SSL端口
        """
        super().__init__(server, port, apikey, apisecret, use_ssl)
        self.login_status = False
        self.login_result = None

    def login(self, user: str, pwd: str, manage_path: Optional[str] = '', tid: int = 2) -> Dict[str, Any]:
        """ 登陆认证
        登陆并修改登陆状态login_status,保存sessid。
        :param user: 认证邮箱用户名
        :param pwd:  密码
        :param manage_path: 如果是管理端接口请写入管理地址，在winmail管理工具中的系统设置-高级设置-系统参数-HTTP配置中查看
        :param tid: 手机使用2，否则默认或者对应的风格数字。参考web代码
        :return: Dict
        管理端返回：
        {
            "result": "ok",
            "info":
            {
                “ sessid ”:  "efd24f9f63d69d6f6f169b235822ca5875eb2bae",
                “ user ”:  "admin"
            }
        }
        用户端返回：
        {
        "result": "ok",
        "info":
            {
            “ sessid ”:  "1a2db1b0edda735295508723d8c6a962",
            “uid”: "test",
            “email”: " test@cnu.com ",
            “fullname”: "测试用户",
            “mobile”: "13900000000",
            “company”: "华兆科技",
            “department”: "系统研发部",
            “jobtitle”: "工程帅",
            “office”: "",
            “officephone”: "",
            “homeaddress”: "",
            “homephone”: "",
            }
        }
        """

        self.login_result = super().login(user, pwd, manage_path=manage_path, tid=tid)

        if self.login_result['result'] == 'ok':
            self.login_status = True

        return self.login_result

    def updatesession(self):
        """更新会话
        更新Sessid，sessid默认为3分钟超时。
        :return: bool
        """
        return super().update_session()

    def domain(self, pageno: int = 0) -> Dict[str, Any]:
        """ 获取域名
        取所有域名列表
        :param pageno: 分页序号，以 0 开始
        :return: Dict
        {
        "result": "ok",
        "info":
            {
            “ domains ”: 域名列表 ,
            “ totalcount ”: 域名总数
            “ pagecount ”:  分页总数
            }
        }
        """

        method_params = {"sessid": self.sessid, "method": "domain"}
        method_params.update({"pageno": pageno})

        return self.get_api(**method_params)

    def domain_added(self, domain: str,
                     description: Optional[str] = None,
                     mailquota: Optional[int] = None,
                     mailcount: Optional[int] = None,
                     ftpquota: Optional[int] = None,
                     ftpcount: Optional[int] = None,
                     **kwargs: Optional[Dict]
                     ) -> Dict[str, Any]:
        """ 新增域名
        新增域名
        :param domain: 域名
        :param description: 描述
        :param mailquota: 新邮箱默认空间大小,单位 MB
        :param mailcount: 新邮箱默认最多邮件数
        :param ftpquota: 新邮箱默认网络磁盘空间大小
        :param ftpcount: 新邮箱默认网络磁盘最多文件数
        :param kwargs: 其他可能参数
        :return:成功返回值
        { "result": "ok"}
        失败返回值
        { "result": "err", errno: 1}
        错误代码：
        errno  值  含义
        -1  域名数已经达到允许注册数
        1  域名新增失败
        2  相同的域名已经存在
        3  相同的域别名已经存在
        4  相同的 NT 认证域名已经存在
        99  您没有权限进行此项操作
        """

        method_params = {"sessid": self.sessid, "method": "domain.added"}
        for args_name, args_value in locals().items():
            if args_name == "self":
                continue
            if args_name == "kwargs":
                method_params.update(kwargs)
                continue
            if args_value is not None:
                method_params.update({args_name: args_value})

        return self.get_api(**method_params)

    def domain_edited(self, domain: str,
                      description: Optional[str] = None,
                      mailquota: Optional[int] = None,
                      mailcount: Optional[int] = None,
                      ftpquota: Optional[int] = None,
                      ftpcount: Optional[int] = None,
                      **kwargs: Optional[Dict]
                      ) -> Dict[str, Any]:
        """ 修改域名
        修改指定域名
        :param domain: 域名
        :param description: 描述
        :param mailquota: 新邮箱默认空间大小,单位 MB
        :param mailcount: 新邮箱默认最多邮件数
        :param ftpquota: 新邮箱默认网络磁盘空间大小
        :param ftpcount: 新邮箱默认网络磁盘最多文件数
        :param kwargs: 其他可能参数
        :return:成功返回值
        { "result": "ok"}
        失败返回值
        { "result": "err", errno: 1}
        错误代码：
        errno  值  含义
        1  域名修改失败
        99  您没有权限进行此项操作
        """

        method_params = {"sessid": self.sessid, "method": "domain.edited"}
        for args_name, args_value in locals().items():
            if args_name == "self":
                continue
            if args_name == "kwargs":
                method_params.update(kwargs)
                continue
            if args_value is not None:
                method_params.update({args_name: args_value})

        return self.get_api(**method_params)

    def domain_delete(self, domain: str) -> Dict[str, Any]:
        """ 删除域名
        删除指定域名
        :param domain: 要删除的域名
        :return: 成功返回值
        { "result": "ok"}
        失败返回值
        { "result": "err", errno: 1}
        errno  值  含义
        -1  域名数已经达到允许注册数。
        1  域名删除失败
        2  此域名下存在邮箱，请先删除域下用户，别名和组
        3  主域名不能被删除
        99  您没有权限进行此项操作
        """

        method_params = {"sessid": self.sessid, "method": "domain.delete"}
        method_params.update({"domain": domain})

        return self.get_api(**method_params)

    def user(self, domain: str, pageno: Optional[int] = 0) -> Dict[str, Any]:
        """ 获取用户列表
        获取指定域名下用户列表
        :param domain: 域名
        :param pageno: 分页序号，以 0 开始
        :return: 成功返回值
            {
            "result": "ok",
            "info":
                {
                “ users ”: 邮箱用户列表 ,
                “ totalcount ”: 用户总数
                “ pagecount ”:  分页总数
                “ domain ”:  所属域名
                }
            }
        """

        method_params = {"sessid": self.sessid, "method": "user"}
        method_params.update({"domain": domain, "pageno": pageno})

        return self.get_api(**method_params)

    def user_added(self, name: str,
                   domain: str,
                   password: str,
                   authtype: Optional[int] = 0,
                   status: Optional[int] = 0,
                   fullname: Optional[str] = '',
                   description: Optional[str] = '',
                   homeaddress: Optional[str] = '',
                   homephone: Optional[str] = '',
                   mobile: Optional[str] = '',
                   company: Optional[str] = '',
                   department: Optional[str] = '',
                   jobtitle: Optional[str] = '',
                   office: Optional[str] = '',
                   officephone: Optional[str] = '',
                   mailquota: Optional[int] = 0,
                   mailcount: Optional[int] = 0,
                   ftpquota: Optional[int] = 0,
                   ftpcount: Optional[int] = 0,
                   **kwargs: Optional[Dict]
                   ) -> Dict[str, Any]:
        """ 新增用户
        管理员新增邮箱用户接口。
        :param name: 邮箱用户名
        :param domain: 域名
        :param password: 邮箱密码
        :param authtype: 认证方式 0 - 本系统认证； 1 - NT 域认证； 2 - 第三方认证
        :param status: 状态 0 - 正常；1 - 禁止；2 - 等待审核
        :param fullname: 用户姓名
        :param description: 描述
        :param homeaddress: 家庭地址
        :param homephone: 电话电话
        :param mobile: 手机
        :param company: 工作单位
        :param department: 部门
        :param jobtitle: 职位
        :param office: 办公室
        :param officephone: 办公电话
        :param mailquota: 邮箱空间大小 单位MB
        :param mailcount: 邮箱最多邮件数
        :param ftpquota: 网络磁盘空间大小 单位MB
        :param ftpcount: 网络磁盘最多文件数
        :param kwargs: 其他参数
        :return:成功返回值
            { "result": "ok"}
            失败返回值
            { "result": "err", errno: 1}
            错误代码：
            errno  值  含义
            -1  用户数已经达到允许注册数
            1  用户新增失败
            2  相同的用户已经存在
            3  相同的用户别名已经存在
            4  相同的邮件组已经存在
            6  此域下用户邮箱数已经达到本域允许的注册数
            7  此域下用户邮箱容量已经达到本域允许的总容量
            8  此域下用户网络磁盘容量已经达到本域允许的总容量
            101  主服务器增加用户失败
            102  主服务器上相同的用户已经存在
            103  主服务器上相同的用户别名已经存在
            104  主服务器上相同的邮件组已经存在
            99  您没有权限进行此项操作
        """
        method_params = {"sessid": self.sessid, "method": "user.added"}
        for args_name, args_value in locals().items():
            if args_name == "self":
                continue
            if args_name == "kwargs":
                method_params.update(kwargs)
                continue
            if args_value is not None:
                method_params.update({args_name: args_value})

        return self.get_api(**method_params)

    def user_edited(self, name: str,
                    domain: str,
                    password: str,
                    changedpwd: Optional[int] = 0,
                    authtype: Optional[int] = 0,
                    status: Optional[int] = 0,
                    fullname: Optional[str] = '',
                    description: Optional[str] = '',
                    homeaddress: Optional[str] = '',
                    homephone: Optional[str] = '',
                    mobile: Optional[str] = '',
                    company: Optional[str] = '',
                    department: Optional[str] = '',
                    jobtitle: Optional[str] = '',
                    office: Optional[str] = '',
                    officephone: Optional[str] = '',
                    mailquota: Optional[int] = 0,
                    mailcount: Optional[int] = 0,
                    ftpquota: Optional[int] = 0,
                    ftpcount: Optional[int] = 0,
                    **kwargs: Optional[Dict]
                    ) -> Dict[str, Any]:
        """ 修改用户
        管理员修改邮箱用户接口。*如果要修改密码，增加参数 changedpwd ，值设置为 1
        :param name: 邮箱用户名
        :param domain: 域名
        :param password: 邮箱密码
        :param changedpwd: 是否修改密码
        :param authtype: 认证方式 0 - 本系统认证； 1 - NT 域认证； 2 - 第三方认证
        :param status: 状态 0 - 正常；1 - 禁止；2 - 等待审核
        :param fullname: 用户姓名
        :param description: 描述
        :param homeaddress: 家庭地址
        :param homephone: 电话电话
        :param mobile: 手机
        :param company: 工作单位
        :param department: 部门
        :param jobtitle: 职位
        :param office: 办公室
        :param officephone: 办公电话
        :param mailquota: 邮箱空间大小 单位MB
        :param mailcount: 邮箱最多邮件数
        :param ftpquota: 网络磁盘空间大小 单位MB
        :param ftpcount: 网络磁盘最多文件数
        :param kwargs: 其他参数
        :return:成功返回值
            { "result": "ok"}
            失败返回值
            { "result": "err", errno: 1}
            错误代码：
            errno  值  含义
            1  用户修改失败
            99  您没有权限进行此项操作
        """
        method_params = {"sessid": self.sessid, "method": "user.edited"}
        for args_name, args_value in locals().items():
            if args_name == "self":
                continue
            if args_name == "kwargs":
                method_params.update(kwargs)
                continue
            if args_value is not None:
                method_params.update({args_name: args_value})

        return self.get_api(**method_params)

    def user_delete(self, name: str, domain: str) -> Dict[str, Any]:
        """删除用户
        删除邮箱用户
        :param name: 邮箱用户名
        :param domain: 域名
        :return: 成功返回值
            { "result": "ok"}
            失败返回值
            { "result": "err", errno: 1}
            错误代码：
            errno  值  含义
            1  用户删除失败
            99  您没有权限进行此项操作
        """

        method_params = {"sessid": self.sessid, "method": "user.delete"}
        method_params.update({"name": name, "domain": domain})

        return self.get_api(**method_params)
