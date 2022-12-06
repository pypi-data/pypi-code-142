# coding=utf-8
"""
作者：vissy@zhu
发送邮件，简单做了一个数据分离，配置的数据单独读取data文件获取
"""
import time
import smtplib
from email.mime.application import MIMEApplication
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from testdata.common import result_data
import ssl
import xlrd

ssl._create_default_https_context = ssl._create_unverified_context


# 发送邮件，发送测试报告html
def send_email(path, smtpserver, user, password, title, sender, receiver, cc):
    tableopen = xlrd.open_workbook(path)
    table = tableopen.sheet_by_name('Sheet1')
    # tableopen.close()
    today = time.strftime('%Y-%m-%d')
    smtpserver = smtpserver
    title = title
    user = user
    password = password
    sender = sender
    receiver = receiver
    cc = cc
    starttime = result_data["starttime"]
    endtime = result_data["endtime"]
    total_num = str(result_data["total_num"])
    pass_num = str(result_data["pass_num"])
    fail_num = str(result_data["fail_num"])

    # 发送邮件主题
    subject = title + 'UI自动化测试报告%s' % today
    msg = MIMEMultipart('mixed')
    content = "Start Time: " + starttime + "-" + endtime + "\n\n" + "Status: Total: " + total_num + " ( Pass: " + pass_num + ", Failure: " + fail_num + ")" + "\n\n"
    msg_html = MIMEText(content, "plain", "UTF-8")
    msg.attach(msg_html)
    xlsx = MIMEApplication(open('./testcase/source.xls', 'rb').read())  # 打开Excel,读取Excel文件
    xlsx["Content-Type"] = 'application/octet-stream'  # 设置内容类型
    xlsx.add_header('Content-Disposition', 'attachment', filename="result.xls")  # ？
    msg.attach(xlsx)
    msg['From'] = sender
    msg['To'] = ';'.join(receiver)
    msg['Cc'] = ';'.join(cc)
    receiver = receiver + cc
    msg['Subject'] = Header(subject, 'utf-8');
    # 连接发送邮件
    try:
        smtp = SMTP_SSL(smtpserver)
        smtp.login(user, password)
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()
        print("邮件发送成功！")
    except smtplib.SMTPException:
        print("Error:无法发送邮件！")
