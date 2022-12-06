from lazycode.setting import RESOURCE_PATH
import json
import os
import random
import datetime
from dateutil import relativedelta
from datetime import date, timedelta
import time

all_data_dict = None
with open(os.path.join(RESOURCE_PATH, 'random_data.json'), 'r', encoding='utf-8') as f:
    all_data_dict = json.loads(f.read())


class LzRandomDataUser(object):
    ID: str = None
    name_first: str = None
    name_last: str = None
    name: str = None
    sex: str = None
    city_level1: str = None
    city_level1_code: str = None
    city_level2: str = None
    city_level2_code: str = None
    city_level3: str = None
    city_level3_code: str = None
    datetime_pre: str = None
    datetime: str = None
    datetime_last: str = None
    department: str = None
    phone: str = None
    email: str = None
    chinese_word: str = None
    symbol: str = None
    url: str = None
    age: str = None

    def __init__(self):
        self.init()

    def __str__(self):
        var_members = [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("__")]

        member_dict = {var: getattr(self, var) for var in var_members}

        sout = '\n'.join([f'{k} = {v}' for k, v in member_dict.items()])

        return sout

    def init(self):
        self.ID = LzRandomData.random_ID()
        self.name_first, self.name_last, self.name, self.sex = LzRandomData.random_name_sex()
        self.city_level1, self.city_level1_code, self.city_level2, self.city_level2_code, self.city_level3, self.city_level3_code = LzRandomData.random_city()

        fmt = '%Y-%m-%d %H:%M:%S.%f'
        r_dt = LzRandomData.random_datetime()
        p_dt = r_dt - relativedelta.relativedelta(years=random.randint(0, 100),
                                                  months=random.randint(0, 12 + 1),
                                                  days=random.randint(0, 30),
                                                  hours=random.randint(0, 24 + 1),
                                                  minute=random.randint(0, 60),
                                                  seconds=random.randint(0, 60))
        l_dt = r_dt + relativedelta.relativedelta(years=random.randint(0, 100),
                                                  months=random.randint(0, 12 + 1),
                                                  days=random.randint(0, 30),
                                                  hours=random.randint(0, 24 + 1),
                                                  minute=random.randint(0, 60),
                                                  seconds=random.randint(0, 60))
        self.datetime = r_dt.strftime(fmt)
        self.datetime_pre = p_dt.strftime(fmt)
        self.datetime_last = l_dt.strftime(fmt)

        self.department = LzRandomData.random_department()
        self.phone = LzRandomData.random_phone()
        self.email = LzRandomData.random_email()
        self.chinese_word = LzRandomData.random_chinese_word()
        self.symbol = LzRandomData.random_symbol()
        self.url = LzRandomData.random_url()
        self.age = random.randint(0, 100 + 1)

        return self


class LzRandomData(object):

    @staticmethod
    def random_name_sex():
        # 单姓
        firstName = all_data_dict["nameData"]["firstName"]
        # 双姓
        firstNameDouble = all_data_dict["nameData"]["firstNameDouble"]

        name_first = random.choice(firstName) if random.randint(1, 101) <= 80 else random.choice(firstNameDouble)

        # 女名
        last_name_girl = all_data_dict["nameData"]["lastNameGirl"]
        last_name_girl_double = ''.join(random.choices(last_name_girl, k=2))

        last_name_boy = all_data_dict["nameData"]["lastNameBoy"]
        last_name_boy_double = ''.join(random.choices(last_name_boy, k=2))

        if random.randint(0, 2) > 0:
            name_last = last_name_boy_double if random.randint(1, 101) <= 80 else random.choice(
                last_name_boy)
            sex = '男'
        else:
            name_last = last_name_girl_double if random.randint(1, 101) <= 80 else random.choice(
                last_name_girl)
            sex = '女'

        name = name_first + name_last
        return name_first, name_last, name, sex

    @staticmethod
    def random_city():
        cityList = all_data_dict["cityList"]
        city_level1, city_level2, city_level3 = random.choice(cityList).split("-")
        city_level1, city_level1_code = city_level1.split("_", 1)
        city_level1_code = "{:0<6}".format(city_level1_code)
        city_level2, city_level2_code = city_level2.split("_", 1)
        city_level2_code = "{:0<6}".format(city_level2_code)
        city_level3, city_level3_code = city_level3.split("_", 1)
        city_level3_code = "{:0<6}".format(city_level3_code)

        return city_level1, city_level1_code, city_level2, city_level2_code, city_level3, city_level3_code

    @staticmethod
    def random_datetime(start_datetime: datetime.datetime = None, end_datetime: datetime.datetime = None,
                        fmt='%Y-%m-%d %H:%M:%S.%f') -> datetime.datetime:

        start_datetime_timestamp = 0 if start_datetime is None else start_datetime.timestamp()
        end_datetime_timestamp = datetime.datetime.now().timestamp() if end_datetime is None else end_datetime.timestamp()

        random_dt = datetime.datetime.fromtimestamp(random.uniform(start_datetime_timestamp, end_datetime_timestamp))

        # str_datetime = random_dt.strftime(fmt=fmt)
        return random_dt

    @staticmethod
    def random_department():
        return random.choice(all_data_dict["departments"])

    @staticmethod
    def random_phone():
        phone_pre_list = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151",
                          "152", "153", "155", "156", "157", "158", "159", "186", "187", "188"]
        return random.choice(phone_pre_list) + "".join(random.choice("0123456789") for i in range(8))

    @staticmethod
    def random_email():
        emailEnd = random.choice(["@qq.com", "@163.com", "@126.com", "@139.com", "@sohu.com", "@aliyun.com", "@189.cn"])

        # 创建一个长度为[3,10)由 字母或数字组成的字符串
        headStr = LzRandomData.random_symbol(random.randint(5, 10), zztsFlag=False, wordFlag=True, numbersFlag=True,
                                             repeat=False)
        email = headStr + emailEnd
        return email

    @staticmethod
    def random_symbol(count=10, zztsFlag=True, wordFlag=True, numbersFlag=True,
                      repeat=True):

        # 特殊字符ASCII码 `~@#...
        zzts = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
                ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

        # 字母ASCII码 abcd...
        words = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        # 数字ASCII码 012...
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        allSymbol = [zzts, words, numbers]
        allSymbolFlag = [zztsFlag, wordFlag, numbersFlag]
        symbols = []
        for i, e in enumerate(allSymbolFlag):
            if e:
                symbols.extend(allSymbol[i])

        if repeat:
            return "".join(random.choices(symbols, k=count))
        else:
            if count > len(symbols):
                print("非重复的数据过长!")
                return None
            else:
                return "".join(random.sample(symbols, k=count))

    @staticmethod
    def random_chinese_word(count=1, common=True):
        if common:
            return "".join(random.choices(all_data_dict["commonWords"], k=count))
        else:
            return "".join([chr(random.randint(0x4e00, 0x9fbf)) for i in range(count)])

    @staticmethod
    def random_ID():
        id = random.choice(list(all_data_dict['CityIdNum'].keys()))
        id = id + str(random.randint(1930, time.localtime(time.time()).tm_year))  # 年份项
        da = date.today() + timedelta(days=random.randint(1, 366))  # 月份和日期项
        id = id + da.strftime('%m%d')
        id = id + str(random.randint(100, 300))  # ，顺序号简单处理

        count = 0
        weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]  # 权重项
        checkcode = {'0': '1', '1': '0', '2': 'X', '3': '9', '4': '8', '5': '7', '6': '6', '7': '5', '8': '5', '9': '3',
                     '10': '2'}  # 校验码映射
        for i in range(0, len(id)):
            count = count + int(id[i]) * weight[i]
            id = id + checkcode[str(count % 11)]  # 算出校验码
            return id

    @staticmethod
    def random_url():
        r_str1 = LzRandomData.random_symbol(zztsFlag=False)
        arg_str = '/'.join(
            [LzRandomData.random_symbol(zztsFlag=False, count=random.randint(2, 10)) for i in
             range(0, random.randint(1, 10))])

        URL = f"http://www.{r_str1}.com/{arg_str}"

        return URL


# lz = LzRandomDataUser()
#
# for i in range(10):
#     print(lz.init())
