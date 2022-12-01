# -*- coding: utf-8 -*-
import re
import time
import datetime
import arrow
from datetime import date, timedelta
import calendar

class ymd_cls:
	def __init__(self, input_date=""):
		months = {"JAN":1, "FEB":2, "MAR":3, "APR":4, "MAY":5, "JUN":6, "JUL":7, "AUG":8, "SEP":9, "OCT":10, "NOV":11, "DEC":12, "JANUARY":1, "FEBRUARY":2, "MARCH":3, "APRIL":4, "JUNE":6,
		"JULY":7, "AUGUST":8,"SEPTEMBER":9, "OCTOBER":10, "NOVEMBER":11, "DECEMBER":12}
		if input_date =="":
			#아무것도 입력하지 않으 면 local time 으로 인식한다
			self.lt = time.localtime()
			self.year = int(time.strftime("%Y", self.lt))
			self.month = int(time.strftime("%m", self.lt))
			self.day = int(time.strftime("%d", self.lt))
			self.lt_utc = datetime.datetime(self.year, self.month, self.day).timestamp()

		elif type(input_date) == type(float(123.00)):
			#실수일 경우는 localutc로 인식한다
			self.lt_utc = time.localtime(float(input_date))
			self.year = int(time.strftime("%Y", self.lt_utc))
			self.month = int(time.strftime("%m", self.lt_utc))
			self.day = int(time.strftime("%d", self.lt_utc))
		elif type(input_date) == type([]):
			#리스트 형태의 경우 : [2022t 1f 3]
			if len(input_date) >= 3:
				self.year, self.month, self.day = int(input_date[0]), int(input_date[1]), int(input_date[2])
				self.jt_utc = datetime.datetime(self.year, self.month, self.day).timestamp()

		elif type("string") == type(input_date) or type(int(123)) == type(input_date):
			#  만약 입력형태가 문자열이면
			#  "202201Or", "22/mar/01","22mar01"
			input_date = str(input_date)
			re_compiled = re.compile("Wd+")
			temp = re.findall(re_compiled, input_date)
			re_str = re.compile("[a-zA-Z]+")

			temp_str = re.findall(re_str, input_date)
			if len(temp) == 3:
				self.year, self.month, self.day = [int(temp[0]), int(temp[1]), int(temp[2])]
			elif len(temp) == 1:
				if len(temp[0]) == 6:
					self.year, self.month, self.day = [int(temp[0][:2]), int(temp[0][2:4]), int(temp[0][-2:])]
			elif len(temp[0]) == 8:
				self.year, self.month, self.day = [int(temp[0][:4]), int(temp[0][4:6]), int(temp[0][-2:])]
			elif len(temp) == 2 and len(temp_str) == 1:
				if temp_str[0] in list(months.keys()):
					self.year, self.month, self.day =[int(temp[0]), int(months[str(temp_str[0]).upper()]), int(temp[1])]
					self.lt_utc = datetime.datetime(self.year, self.month, self.day).timestamp()


class pynal():
	def __init__(self):
		self.seoul_time = ""
		self.present = arrow.now()
		self.future = ""
		self.var = {}
		self.holiday = {}
		self.overtime = {}
		self.working_time = {}

	def terms(self, input_sec):
		"""
		용어정리
		아래와같은 형태로 용어를 사용한다
		"""

		result = """
		date     : 2000-01-01
		datelist : [2000, 01, 01]
		ymdlist : [2000, 01, 01]
		time     : 시간의 여러형태로 입력을 하면, 이에 맞도록 알아서 조정한다
		dhms     : 2일3시간10분30초, day-hour-minute-sec
		hmslist  : [시, 분, 초]
		utftime  : 1640995200.0 또는 "", 1648037614.4801838 (의미 : 2022-03-23T21:13:34.480183+09:00)
		move     : 입력값에 더하거나 빼서 다른 값으로 바꾸는것, 입력값과 출력값이 다를때 (출력값을 입력의 형태로 바꾸면 값이 다른것)
		change   : 형태를 바꾼것
		read     : 입력값을 원하는 형태로 변경해서 갖고오는것
		get      : 입력값에서 원하는 형태의 값을 갖고오는것
		shift    : 현재의 값을 같은 형태에서 값을 이동시키는것
		"""
		return result

	def change_sec_dhms(self, input_data):
		"""
		초를 날자로 계산해 주는것
		입력값 : 1000초
		출력값 : 2일3시간10분30초
		dhms : day-hour-minute-sec
		"""
		nalsu = int(input_data)/(60*60*24)
		return nalsu

	def change_time_utftime(self, input_data=""):
		"""
		현재의시간을 돌려준다
		입력값이 ""이면 지금의 시간을 뜻한다
		시간형태 : 1648037614.4801838 (의미 : 2022-03-23T21:13:34.480183+09:00)
		"""
		localtime = self.check_inputtime(input_data)
		atime = arrow.get(localtime)
		result = atime.timestamp()
		return result

	def change_sec_time(self, input_data=""):
		"""
		초로 넘어온 자료를 기간으로 돌려주는 것
		입력값 : 123456
		"""
		step_1 = divmod(int(input_data), 60)
		step_2 = divmod(step_1[0], 60)
		final_result = [step_2[0], step_2[1], step_1[1]]
		return final_result

	def change_hmslist_sec(self, input_data=""):
		"""
		hmslist : [시, 분, 초]
		input_data = "14:06:23"
		출력값 : 초
		입력값으로 온 시분초를 초로 계산한것
		"""
		re_compile = re.compile("\d+")
		result = re_compile.findall(input_data)
		total_sec = int(result[0]) * 3600 + int(result[1]) * 60 + int(result[2])
		return total_sec

	def change_time_yearlist(self, input_data=""):
		"""
		년 -----> ['22', '2022']
		닞은숫자 -> 많은글자 순으로 정리
		"""
		lt = self.check_inputtime(input_data)
		year_s = time.strftime('%y', lt)
		year = time.strftime('%Y', lt)
		result = [year_s, year]
		return result

	def change_time_monthlist (self, input_data=""):
		"""
		입력값 : utf시간숫자, 1640995200.0 또는 ""
		월 -----> ['04', Apr, April]
		닞은숫자 -> 많은글자 순으로 정리
		"""
		lt = self.check_inputtime(input_data)
		mon = time.strftime('%m', lt)
		mon_e = time.strftime('%b', lt)
		mon_e_l = time.strftime('%B', lt)
		result = [mon, mon_e, mon_e_l]
		return result

	def change_time_weeklist(self, input_data=""):
		"""
		입력값 : utf시간숫자, 1640995200.0 또는 ""
		주 -----> ['5', '13', 'Fri', 'Friday']
		닞은숫자 -> 많은글자 순으로 정리
		"""
		lt = self.check_inputtime(input_data)
		week_no = time.strftime('%w', lt)
		yearweek_no = time.strftime('%W', lt)
		week_e = time.strftime('%a', lt)
		week_e_l = time.strftime('%A', lt)
		result = [week_no, yearweek_no, week_e, week_e_l]
		return result

	def change_time_daylist (self, input_data=""):
		"""
		입력값 : utf시간숫자, 1640995200.0 또는 ""
		일 -----> ['05']
		닞은숫자 -> 많은글자 순으로 정리
		"""
		lt = self.check_inputtime(input_data)
		#print(lt)
		day = time.strftime('%d', lt)
		day_l = time.strftime('%j', lt)
		result = [day, day_l]
		#print("daylist", result)
		return result

	def change_time_hourlist (self, input_data=""):
		"""
		입력값 : utf시간숫자, 1640995200.0 또는 ""
		시 -----> ['10', '22']
		닞은숫자 -> 많은글자 순으로 정리
		"""
		lt = self.check_inputtime(input_data)
		hour = time.strftime('%I', lt)
		hour_l = time.strftime('%H', lt)
		result = [hour, hour_l]
		return result

	def change_time_minlist (self, input_data=""):
		"""
		입력값 : utf시간숫자, 1640995200.0 또는 ""
		분 -----> ['07']
		닞은숫자 -> 많은글자 순으로 정리
		"""
		lt = self.check_inputtime(input_data)
		min = time.strftime('%M', lt)
		result = [min]
		return result

	def change_time_seclist(self, input_data=""):
		"""
		입력값 : utf시간숫자, 1640995200.0 또는 ""
		초 -----> ['48']
		닞은숫자 -> 많은글자 순으로 정리
		"""
		lt = self.check_inputtime(input_data)
		sec = time.strftime('%S', lt)
		result = [sec]
		return result

	def change_hmdlist_sec(self, base_day, input_list=[0,0,1]):
		"""
		몇년 몇월 몇일을 초로 바꾸는 것
		입력형태 : [몇년, 몇월, 몇일]
		현재일자를 기준으로
		월은 30일 기준으로 계산한다
		기준날짜에서 계산을 하는 것이다
		"""
		total_sec = int(input_list[0]) *60*60*24*365  + int(input_list[1]) *60*60*24*30 + int(input_list[2])*60*60*24
		return total_sec

	def change_time_timedic(self, input_data=""):
		"""
		입력된 시간에 대한 왠만한 모든 형식의 날짜 표현을 사전형식으로 돌려준다
		"""
		lt = self.check_inputtime(input_data)

		#s는 short, e는 english, l은 long
		year_s = time.strftime('%y', lt)
		year = time.strftime('%Y', lt)

		mon = time.strftime('%m', lt)
		mon_e = time.strftime('%b', lt)
		mon_e_l = time.strftime('%B', lt)

		day = time.strftime('%d', lt)
		day_l = time.strftime('%j', lt)

		week_no = time.strftime('%w', lt)
		yearweek_no = time.strftime('%W', lt)
		week_e = time.strftime('%a', lt)
		week_e_l = time.strftime('%A', lt)

		hour = time.strftime('%I', lt)
		hour_l = time.strftime('%H', lt)
		ampm = time.strftime('%p', lt)
		min = time.strftime('%M', lt)
		sec = time.strftime('%S', lt)
		result = {"year_s":year_s, "year":year,
		          "month":mon, "mon":mon, "mon_e":mon_e, "mon_e_l":mon_e_l,
		          "day":day,"day_l":day_l,
		          "hour":hour,"hour_l":hour_l,
		          "ampm":ampm,
		          "min":min,"minute":min,
		          "sec":sec,"second":sec,
		          "week_no":week_no,"week_e":week_e,"week_e_l":week_e_l,"yearweek_no":yearweek_no}
		return result

	def change_time_date(self, input_data=""):
		lt = self.check_inputtime(input_data)
		atime = arrow.get(lt)
		result = atime.format("YYYY-MM-DD")
		return result

	def change_ymd_utftime(self, input_list):
		"""
		입력 : [년도, 월, 날]
		출력 : utc값
		"""
		atime = arrow.get(date(int(input_list[0]), int(input_list[1]), int(input_list[2])))
		result = atime.timestamp()
		return result

	def change_time_weekno(self, input_data=""):
		"""
		시간이 들어온면
		입력값 : 년도, 위크번호
		한 주의 시작은 '월'요일 부터이다
		"""
		lt = self.check_inputtime(input_data)
		result = time.strftime('%W', lt)
		return result

	def change_time_endofmonth(self, input_data=""):
		"""
		입력한 날짜나 시간의 마지막날을 게산하는것
		입력값 : 시간 또는 날짜
		출력값 : 그달의 마지막날
		"""
		lt = self.check_inputtime(input_data)
		result = time.strftime('%W', lt)
		return result

	def check_inputtime(self, input_data=""):
		"""
		입력 : 입력값이 시간일때
		출력 : localtime값, 1575142526.500323
		만약 입력값이 없으면 지금 시간의 localtime값을 돌려준다
		"""
		if input_data == "":
			result = time.localtime()
		elif type(input_data) == type([]) and len(input_data) == 3:
			result = self.change_ymd_utftime(input_data)
		else:
			result = time.localtime(input_data)
		return result

	def check_inputdate(self, input_data):
		result = ""
		if type([]) == type(input_data):
			#만약 입력형태가 리스트이면
			if len(input_data) == 3:
				result = input_data
		elif type("string") == type(input_data):
			#만약 입력형태가 문자열이면
			re_compiled = re.compile("\d+")
			temp = re.findall(re_compiled, input_data)
			print(temp)
			if len(temp) == 3:
					result = temp
			elif len(temp) == 1:
				if len(temp[0]) == 6:
					result = [temp[0][:2], temp[0][2:4],temp[0][-2:]]
				elif len(temp[0]) == 8:
					result = [temp[0][:4], temp[0][4:6],temp[0][-2:]]
		return result

	def get_date_monday_of_weekno(self, year, week_no):
		"""
		입력값 : 년도, 위크번호
		한 주의 시작은 '월'요일 부터이다
		"""
		first = date(year, 1, 1)
		base = 1 if first.isocalendar()[1] == 1 else 8
		temp = first + timedelta(days=base - first.isocalendar()[2] + 7 * (int(week_no) - 1))
		days = str(temp).split("-")
		#input_utf_time_no = nal.change_ymd_utftime([2022, 1, 1])
		#return [str(temp), temp, input_utf_time_no]

	def get_today(self):
		result = self.today()
		return result

	def get_ymlist_lastday(self, input_list = [2002, 3]):
		"""
		입력값 : datetime.date(2012, month, 1)
		결과값 : 원하는 년과 월의 마지막날을 알아내는것
		"""
		any_day = datetime.date(input_list[0], input_list[1], 1)
		next_month = any_day.replace(day=28) + datetime.timedelta(days=4)  # this will never fail
		result = next_month - datetime.timedelta(days=next_month.day)
		return result

	def minus_date0_date1(self, input_date1, input_date2):
		utc1 = self.change_ymd_utftime(input_date1)
		utc2 = self.change_ymd_utftime(input_date2)
		result = abs((float(utc1) - float(utc2))/(60*60*24))
		return result

	def shift_day(self, input_list, input_no):
		"""
		기준날짜에서 일을 이동시키는것
		"""
		input_list  =self.check_inputdate(input_list)
		old_input_utf_time_no = self.change_ymd_utftime(input_list)
		new_second = int(input_no)*60*60*24
		new_input_utf_time_no = old_input_utf_time_no + new_second
		result = self.change_time_ymd(new_input_utf_time_no)
		return result

	def shift_month(self, input_list, input_no):
		#기준날짜에서 월을 이동시키는것
		input_list  =self.check_inputdate(input_list)
		year = int(input_list[0])
		month = int(input_list[1])
		day = int(input_list[2])

		add_year,  remain_month = divmod((month + int(input_no)), 12)
		if remain_month == 0:
			add_year = add_year -1
			remain_month = 12
		result = [year+int(add_year), remain_month, day]
		return result

	def shift_time_byday(self, base_time = "", input_no = 3):
		"""
		입력한 날짜를 기준으로 날을 이동시키는것
		아무것도 입력하지 않으면 현재 시간
		입력값 : 시간
		출력값 : 2022-01-01
		"""
		if base_time =="":
			base_time = arrow.now()
		shift_now = base_time.shift(days=int(input_no))
		result = shift_now.format("YYYY-MM-DD")
		return result

	def shift_time_bymonth(self, base_time = "", input_no = 3):
		"""
		입력한 날짜를 기준으로 날을 이동시키는것
		아무것도 입력하지 않으면 현재 시간
		입력값 : 시간
		출력값 : 2022-01-01
		"""
		if base_time =="":
			base_time = arrow.now()
		shift_now = base_time.shift(months=int(input_no))
		result = shift_now.format("YYYY-MM-DD")
		return result

	def shift_datelist_byday(self, input_list, input_no):
		"""
		입력한 날짜리스트를 기준으로 날을 이동시키는것
		아무것도 입력하지 않으면 현재 시간
		입력값 : [2022, 03, 02]
		출력값 : 2022-01-01
		"""
		just_now = arrow.get(str(input_list[0]) & "-" & str(input_list[1]) & str(input_list[2]))
		shift_now = just_now.shift(days=int(input_no))
		changed_time = shift_now.format("YYYY-MM-DD")
		return changed_time

	def shift_datelist_bymonth(self, input_list, input_no):
		just_now = arrow.get(str(input_list[0]) & "-" & str(input_list[1]) & str(input_list[2]))
		shift_now = just_now.shift(months=int(input_no))
		changed_time = shift_now.format("YYYY-MM-DD")
		return changed_time

	def shift_year(self, input_list, input_no):
		"""
		기준날짜에서 월을 이동시키는것
		입력형태 : [2022, 3, 1]
		"""
		input_list  =self.check_inputdate(input_list)
		year = int(input_list[0])
		remain_month = int(input_list[1])
		day = int(input_list[2])
		result = [year+int(input_no), remain_month, day]
		return result

	def today(self):
		"""
		오늘 날짜를 yyyy-mm-dd형식으로 돌려준다
		지금의 날짜를 돌려준다
		입력값 : 없음
		출력값 : 2022-03-01,
		"""
		just_now = arrow.now()
		tuday = just_now.format("YYYY-MM-DD")
		return tuday

	def holiday_nation (self):
		#휴일기준
		self.holiday["common"] = ["0101","0301","0505","0606", "0815","1001","1225",1.3]
		self.holiday["company"] = ["0708"]

	def working_hour(self):
		#근무시간기준
		self.wt["wt96"] = [[900,1800]]
		self.wt["wt85"] = [[800,1700]]

	def overtime(self):
		#[시작시간, 끝시간, 일당몇배]
		self.ot["common"] = [["0000", "0500", 1],["0505", "0606", 1.2]]
		self.ot["company"] = ["0708"]

	def salary(self):
		#휴일기준
		self.holiday["common"] = ["0101","0301","0505","0606", "0815","1001","1225",1.3]
		self.holiday["company"] = ["0708"]

	def period(self):
		#계산기간
		self.during["common"] = ["0101","0301","0505","0606", "0815","1001","1225",1.3]

	def service_period(self):
		#재직기간
		self.during["common"] = [["20110203","20130301"],["20150101","20160708"]]

	def getMonthRage(self, year, month):
		date = datetime.datetime(year=year, month=month, day=1).date()
		monthrange = calendar.monthrange(date.year, date.month)
		first_day = calendar.monthrange(date.year, date.month)[0]
		last_day = calendar.monthrange(date.year, date.month)[1]
		return [date, monthrange, first_day, last_day]


	def minus_date1_date2(self, date_1, date_2):
		time_big = ymd_cls(date_1)
		time_small = ymd_cls(date_2)
		if time_big.lt_utc > time_small.lt_utc:
			pass
		else:
			time_big, time_small = time_small, time_big
		time_big.last_day = self.getMonthRage(time_big.year, time_big.month)[3]
		time_small.last_day = self.getMonthRage(time_small.year, time_small.month)[3]

		delta_year = abs(time_big.year - time_small.year)
		delta_day = int(abs(time_big.lt_utc - time_small.lt_utc) / (24 * 60 * 60))
		# 실제 1 년의 차이는 365 일 5 시간 48 분 46초 + 0.5초이다 (2 년에 1 번씩 윤초를 실시》
		actual_delta_year = int(abs(time_big.lt_utc - time_small.lt_utc) / (31556926 + 0.5))
		delta_month = abs((time_big.year * 12 + time_big.month) - (time_small.year * 12 + time_small.month))
		if time_big.day > time_small.day:
			actual_delta_month = delta_month - 1
		else:
			actual_delta_month = delta_month
		actual_delta_day = delta_day
		return [delta_year, delta_month, delta_day, actual_delta_year, actual_delta_month, actual_delta_day]