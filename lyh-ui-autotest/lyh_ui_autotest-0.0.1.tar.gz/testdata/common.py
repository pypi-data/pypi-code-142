# coding=utf-8
"""
作者：vissy@zhu
"""
# DMP后台
common_data = {
    "chromedriver": "/Applications/Google Chrome.app/chromedriver",  # chromedriver存放chrome的安装路径
    "url": "https://demodm.liangyihui.net/start/index.html#/app/projectAdmin",  # 目标url
    "model": "pc",  # pc模式/h5模式
    "path": "./testcase/source.xls",
    "picname": "",  # 截图文件名
}
# 罕见病
# common_data = {
#     "chromedriver": "/Applications/Google Chrome.app/chromedriver",  # chromedriver存放chrome的安装路径
#     "url": "https://m.hjbxjz.com/#/home",  # 目标url
#     "model": "h5",  # pc模式/h5模式
#     "path": "./testcase/source.xls",  # 用例总入口
#     "case_name": "case",
#     "picname": "",  # 截图文件名
# }
# ES
# common_data = {
#     "chromedriver": "/Applications/Google Chrome.app/chromedriver",  # chromedriver存放chrome的安装路径
#     "url": "https://edu.liangyihui.net/",  # 目标url
#     "model": "pc",  # pc模式/h5模式
#     "path": "./testcase/source.xls",  # 用例总入口
#     "case_name": "case",
#     "picname": "",  # 截图文件名
# }
email_data = {
    "smtpserver": "smtp.exmail.qq.com",
    "user": "xun.zhu@liangyihui.net",
    "password": "QAtest2022@",
    "title": "罕见病",
    "sender": "xun.zhu@liangyihui.net",
    "receiver": ["xun.zhu@liangyihui.net"],
    "cc": []
}
result_data = {
    "starttime": "2022/10/21 11:11:11",  # 用例开始时间
    "endtime": "2022/10/22 12:12:12",  # 用例结束时间
    "total_num": "3",  # 用例总数
    "fail_num": "1",  # 失败用例数
    "pass_num": "2",  # 通过用例数
}
