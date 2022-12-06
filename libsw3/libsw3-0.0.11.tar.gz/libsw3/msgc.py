#!/usr/bin/python3
# -*- coding: utf8 -*-

__all__ = ["c_xxtz"]

import time
import libsw3 as sw3


class c_xxtz(object):
    def __init__(self, sconn=""):
        self.db = sw3.c_oracle(sconn="msgc", yslj=True)
    def send(self, title="", content="", receiveGroup=None, noticeType="1", noticeTime=None, responseModel="2",saveDay=30):
        '''
        消息通知
        :param title: 标题，对于包含邮件通知方式的请求，标题为必录项
        :param content: 内容，必录项
        :param receiveGroup: 接收人组，多个组通过英文分隔符;分隔。例子：888;999
        :param noticeType: 通知方式，0-短信 1-微信 2-邮箱。同时多种通知方式通过英文分隔符;分隔。例子：0;1;2
        :param noticeTime: 通知发布时间。默认即时发布，可指定发布时间。格式：yyyymmddHHMMSS
        :param responseModel: 通知响应模式：0-所有人必须响应 1-任意一人响应即可 2-不需要响应
        :param saveDay: 通知保留天数，默认30天
        :return:
        '''
        if noticeType is None:
            return False
        if noticeType.index("2") >= 0 and (title is None or title == ""):
            return False
        if content is None or content == "":
            return False
        if receiveGroup is None or receiveGroup == "":
            return False
        if noticeTime is None:
            noticeTime = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
        if responseModel is None:
            responseModel = "2"
        requestId = self.db.jg1("select notice_seq.nextval from dual")
        insertSQL = "insert into t_notice_request (id,title,content,notice_type,notice_time,model,create_time,create_by,save_days) values (:1,:2,:3,:4,:5,:6,sysdate,0,:7)"
        self.db.execute(insertSQL, {'1': requestId, '2': title, '3': content, '4': noticeType, '5': noticeTime, '6': responseModel, '7': saveDay})
        for groupId in receiveGroup.split(";"):
            if groupId.isdigit():
                self.db.execute("insert into t_notice_group (notice_id, group_id) values (:1, :2)",{'1': requestId, '2': groupId})
        self.db.commit()
        return True
