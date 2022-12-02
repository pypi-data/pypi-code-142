import re
import logging
from util.mongo_util import *
from util.mysql_util import *



def getParameterValue(b):
    """
    通过数据库查询，获取变量的实际值
    """
    b_list = b.split("|")
    replace_values = []
    for b in b_list:
        try:
            #分片处理
            key = (str(b).split("&&"))[0].split("{")[1]
            sql = str((str(b).split("&&"))[1:]).split("[")[1].split("}']")[0] + "' "
            print("sql:",sql)
            #调用数据库查询变量值
            #判断是否是mongo数据库，是则继续执行
            if 'db.' in sql:
                result = tongyongSql(sql)
                if key == 'id':
                    key = '_id'
                value = result.get(key)

            # 判断是否是mysql数据库，是则继续执行
            elif 'SELECT' or 'select' or 'Select' in sql:
                sql = sql.split('\'')[1]
                result = tongyongMYSql(sql)
                value = str(result).split('(')[1].split(',')[0]
                #判断是否为字符创，是则继续分片删除''
                if '\'' in value:
                    value = value.split('\'')[1].split('\'')[0]
            else:
                print('变量查询语句错误')
            # print(value)

            # print(value)
            #将变量值存放到列表中
            replace_values.append(value)
            print(replace_values)
            #返回实际参数列表
        except:
            logging.error("参数预处理失败【%s】\n" % b)
            logging.info("\n")
    return replace_values

def replaceParameterValue(b,blist):
    """
    替换匹配的变量参数
    """
    global_num = re.findall(r"\$\{(get_unique_\w*)\}", b)
    i = 0
    while i < len(global_num):
        b = re.sub(r"\$\{(get_unique_\w*)\}", str(blist[i]), b, count=1)
        i += 1
    print(b)
    return b


if __name__ == "__main__":
# testIrole001
    a = 'username=${get_unique_num}&password=1a64a010767f0725fb52111b0a9e9f84&userType=3&companyId=62822cf91a79c900018bd3f0&departmentId=628d82d19fed7920041d4318&roleIds=%5B%22628d8384a34deb3b137bbdfc%22%5D&defaultModule=home&realName=testrp001&permissionTimestamp=0&wrongLoginLock=true&id=${get_unique_num1}'
    b = '{username&&db.User.find({"username":"testIrole001"})}|{id&&db.User.find({"username":"testIrole001"})}'
    c = '/i2vApi/i2v/terminalapp/sysGroup/saveSysUserGroup?groupId=${get_unique_num}&idList=105137&groupName=${get_unique_num1}'
    d = '{idList&&SELECT id FROM sys_group WHERE group_name = "autoGroup";}|{group_name&&SELECT group_name FROM sys_group WHERE group_name = "autoGroup";}'
    # blist = getParameterValue(b)
    # a = replaceParameterValue(a,blist)
    blist = getParameterValue(d)
    c = replaceParameterValue(c, blist)

    # print(blist)



    # i=0
    # for alist in a_list:
    #     variable = re.search(r"\$\{(get_unique_\w*)\}", alist)
    #     if variable is not None:
    #         newVariable = re.sub('\$\{(get_unique_\w*)\}', blist[i], alist)
    #     i += 1
    # print(a)
    # global_num_name = re.findall(r"\$\{(get_unique_\w*)\}", a)
    # print(global_num_name)
    # getParameterValue(b)



# dict = {"memberId":"${memberID}","password":"123456","loanId":"${loanId}","amount":"-100"}
# data = {"memberId":10001, "loanId":1}
# for param in dict:
#     value = dict[param]
#     if param in data.keys():
#         s = str(data[param])
#     newValue = re.sub('\$\{.*\}', s, value)
#     dict[param] = newValue
# print(dict)
# sql = 'db.User.find({"username":"testIrole001"})'
# sqldata = tongyongSql(sql)
# id = sqldata.get('_id')
# id1 = str(id)
# print(type(id1))
# a = re.sub(r"\$\{(get_unique_\w*)\}", id1, a)
# print(a)
