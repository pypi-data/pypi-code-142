# -*- coding: utf-8 -*-

import win32gui
import win32com.client
from halmoney import basic_data, scolor
import re
import math
import string
import random
import time

class pcell:

	def __init__(self, filename=""):
		#공통으로 사용할 변수들을 설정하는 것
		self.color = scolor.scolor()
		self.basic = basic_data.basic_data()
		self.common_data = self.basic.basic_data()

		# 만약 화일의 경로가 있으면 그 화일을 열도록 한다
		self.xlapp = win32com.client.dynamic.Dispatch('Excel.Application')
		self.xlapp.Visible = 1

		if filename != None:
			self.filename = filename.lower()

		if self.filename == 'activeworkbook' or self.filename == '':
			# activeworkbook으로 된경우는 현재 활성화된 workbook을 그대로 사용한다
			self.xlbook = self.xlapp.ActiveWorkbook
			if self.xlbook == None:
				# 만약 activework북을 부르면서도 화일이 존재하지 않으면 새로운 workbook을 만드는 것
				try:
					self.xlapp.WindowState = -4137
					self.xlbook = self.xlapp.WorkBooks.Add()
				except:
					win32gui.MessageBox(0, "There is no Activeworkbook", "xxw.halmoney.com", 0)
		elif filename.lower() == 'new':
			# 빈것으로 된경우는 새로운 workbook을 하나 열도록 한다
			self.xlapp.WindowState = -4137
			self.xlbook = self.xlapp.WorkBooks.Add()
		elif not (self.filename == 'activeworkbook') and self.filename:
			# 만약 화일 이름이 따로 주어 지면 그 화일을 연다
			try:
				self.xlapp.WindowState = -4137
				self.xlbook = self.xlapp.Workbooks.Open(self.filename)
			except:
				win32gui.MessageBox(0, "Please check file path", "xxw.halmoney.com", 0)

	def add_button_with_macro(self, sheet_name="", xyxy="", macro_code="", title=""):
		"""
		매크로랑 연결된 버튼을 만드는것
		버튼을 만들어서 그 버튼에 매크로를 연결하는 것이다
		매크로와 같은것을 특정한 버튼에 연결하여 만드는것을 보여주기위한 것이다
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		new_btn = sheet_object.Buttons()
		new_btn.Add(x1, x2, y1, y2)
		new_btn.OnAction = macro_code
		new_btn.Text = title

	def add_sheet_new(self):
		"""
		시트하나 추가하기
		위치는 자동으로 제일 뒤에 추가되는것이며, 시트이름이 없어 자동으로 만들어지는 이름입니다
		"""
		self.xlbook.Worksheets.Add()

	def add_text_in_range_at_left(self, sheet_name="", xyxy="", input_text="입력필요"):
		"""
		선택한 영역의 왼쪽에 입력한 글자를 추가
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		for x in range(x1, x2 + 1):
			for y in range(y1, y2 + 1):
				cell_value = str(sheet_object.Cells(x, y).Value)
				if cell_value == None: cell_value = ""
				sheet_object.Cells(x, y).Value = str(input_text)+cell_value

	def add_text_in_range_at_right(self, sheet_name="", xyxy="", input_text="입력필요"):
		"""
		선택한 영역의 오른쪽에 입력한 글자를 추가
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		for x in range(x1, x2 + 1):
			for y in range(y1, y2 + 1):
				cell_value = str(sheet_object.Cells(x, y).Value)
				if cell_value == None: cell_value = ""
				sheet_object.Cells(x, y).Value = cell_value+str(input_text)

	def add_text_in_range_bystep(self, sheet_name="", xyxy="", input_text="", step=""):
		"""
		선택한 영역의 시작점부터 n번째 셀마다 값을 넣기
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		basic_list = []
		for one_data in input_text.split(","):
			basic_list.append(one_data.strip())

		for x in range(int(basic_list[0]), int(basic_list[1]) + 1, int(basic_list[2])):
			for y in range(y1, y2 + 1):
				cell_value = str(sheet_object.Cells(x, y).Value)
				if cell_value == None: cell_value = ""
				sheet_object.Cells(x, y).Value = cell_value+str(input_text)

	def add_text_in_range_by_xystep(self, sheet_name="", xyxy="", input_text="", xystep=[1, 1]):
		"""
		선택한 영역의 시작점부터 x,y 번째 셀마다 값을 넣기
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)

		for x in range(x1, x2 + 1):
			if divmod(x, xystep[0])[1] == 0:
				for y in range(y1, y2 + 1):
					if divmod(y, xystep[1])[1] == 0:
						cell_value = str(sheet_object.Cells(x, y).Value)
						if cell_value == None:
							cell_value = ""
						# self.write_value_in_cell(sheet_name, [x, y], cell_value + str(input_text))
						sheet_object.Cells(x, y).Value = cell_value + str(input_text)

	def check_address_with_datas(self, xyxy="", input_datas="입력필요"):
		"""
		입력주소와 자료를 받아서 최소로할것인지 최대로 할것인지를 골라서 나타낼려고 한다
		[$A$1], [$A$1:$B$2], [$1:$7], [$A:$B] ["A1"],[2,1,3,2], [1,2]이 경우가 가능
		Output Style :  [["$A$2:$B$3"],["A1","B2],[2,1,3,2]]무조건 3개의 형태로 나오도록 만든다
		"""
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		result = {}
		y_len = len(input_datas)
		x_len = len(input_datas[0])
		y_len_rng = y2 - y1
		x_len_rng = x2 - x1
		max_num = max(map(lambda y: len(y), input_datas))
		min_num = min(map(lambda y: len(y), input_datas))
		max_y = max(y_len, y_len_rng)
		max_x = max(max_num, x_len_rng)
		min_y = max(y_len, y_len_rng)
		min_x = max(x_len, x_len_rng)
		# 입력할것중 가장 적은것을 기준으로 적용
		result["xyxy_min"] = [x1, y1, x1 + min_y, y1 + min_num]
		# 입력할것중 가장 큰것을 기준으로 적용
		result["xyxy_max"] = [x1, y1, x1 + max_y, y1 + max_y]
		# 일반적인기준으로 적용하는것
		result["xyxy_basic"] = [x1, y1, x1 + x_len, y1 + max_num]
		return result

	def change_address_to_xyxy_v1(self, address):
		"""
		들어오는 값은 #$E$13, $4:$12, $B:$I, $C$4:$F$11 이런 형태만 한다
		Output Style :  [y1, x1, y2, x2] ==> [원래값, [1,2,3,4]]
		"""
		temp_list_0 = []
		temp_list_1 = []
		temp_list_0 = address.split(":")
		for one in temp_list_0:
			temp_list_1.append(one.split("$"))
		if len(temp_list_1[0]) == 2:
			if temp_list_1[0][1].isdigit():
				address_list = [0, temp_list_1[0][1], 0, temp_list_1[1][1]]
			else:
				address_list = [temp_list_1[0][1], 0, temp_list_1[1][1], 0]
		if len(temp_list_1[0]) == 3:
			address_list = [temp_list_1[0][1], temp_list_1[0][2], temp_list_1[1][1], temp_list_1[1][2]]
		if address_list[0] != 0: address_list[0] = self.change_char_to_num(address_list[0])
		if address_list[2] != 0: address_list[2] = self.change_char_to_num(address_list[2])
		address_list = [int(address_list[0]), int(address_list[1]), int(address_list[2]), int(address_list[3])]
		return [address, address_list]

	def change_address_to_xyxy(self, xyxy):
		"""
		셀의 $aa$10 --> aa10,으로 바꾸어주는 함수
		문자, 숫자, :만을 남겨놓고 나머지는 모두 삭제하는 것이다
		*** $를 없애는 코드를 별도로 만든다
		"""
		char_in_start_cell = ""
		eng_spell = string.ascii_lowercase + string.digits + ':'
		list_cell = list(xyxy)
		for one_word in list_cell:
			one_word = str(one_word).lower()
			if one_word in eng_spell:
				char_in_start_cell = char_in_start_cell + one_word
		return char_in_start_cell

	def change_char_to_num(self, input_text="입력필요"):
		"""
		문자가 오던 숫자가 오던 숫자로 변경하는 것이다
		 b를 2로 바꾸어 주는것
		"""
		aaa = re.compile("^[a-zA-Z]+$")  # 처음부터 끝가지 알파벳일때
		result_str = aaa.findall(str(input_text))

		bbb = re.compile("^[0-9]+$")  # 처음부터 끝가지 숫자일때
		result_num = bbb.findall(str(input_text))

		if result_str != []:
			no = 0
			result = 0
			for one in input_text.lower()[::-1]:
				num = string.ascii_lowercase.index(one) + 1
				result = result + 26 ** no * num
				no = no + 1
		elif result_num != []:
			result = int(input_text)
		else:
			result = "error"
		return result

	def change_inputdata_to_list2d(self, input_data):
		"""
		입력된 자료형에 따라서 2차원으로 만들어 주는것
		1차원의 리스트는 [1,2,3,4]의 형태이며
		이것은 같은 가로에 세로의 글자가 다른것이다
		"""
		if type(input_data) == type([]) or type(input_data) == type(()):
			if type(input_data[0]) == type([]) or type(input_data[0]) == type(()):
				result = input_data
			else:
				result = [input_data]
		elif type(input_data) == type("123") or type(input_data) == type(123):
			result = [[input_data]]
		return result

	def change_list1d_to_list2d(self, input_data):
		"""
		1차원의 리스트가 오면 2차원으로 만들어주는 것
		"""
		result = []
		if len(input_data) > 0:
			if type(input_data[0]) != type([]):
				for one in input_data:
					result.append([one, ])
		return result

	def change_list1d_to_list2d_with_yline_style(self, input_list1d):
		"""
		1차원의 리스트를 세로열에 출력이 되도록 2차원으로 만든다
		"""
		result = []
		for one in input_list1d:
			result.append([one])
		return result

	def change_list2d_as_samelen(self, input_list2d="입력필요"):
		"""
		2차원 리스트의 최대 길이로 같게 만드는 것
		가끔 자료의 갯수가 달라서 생기는 문제가 발생할 가능성이 있는것을 맞추는것
		추가할때는 ""를 맞는갯수를 채워넣는다
		"""
		input_text = None
		max_num = max(map(lambda x: len(x), input_list2d))
		result = []
		for one in input_list2d:
			one_len = len(one)
			if max_num == one_len:
				result.append(one)
			else:
				one.extend([input_text] * (max_num - one_len))
				result.append(one)
		return result

	def change_num_to_char(self, input_data="입력필요"):
		"""
		입력값 : 27 => 출력값 : aa
		숫자를 문자로 바꿔주는 것
		"""
		re_com = re.compile(r"([0-9]+)")
		result_num = re_com.match(str(input_data))

		if result_num:
			base_number = int(input_data)
			result_01 = ''
			result = []
			while base_number > 0:
				div = base_number // 26
				mod = base_number % 26
				if mod == 0:
					mod = 26
					div = div - 1
				base_number = div
				result.append(mod)
			for one_data in result:
				result_01 = string.ascii_lowercase[one_data - 1] + result_01
			final_result = result_01
		else:
			final_result = input_data
		return final_result

	def change_rgb_to_rgbint(self, input_data):
		"""
		rgb인 값을 color에서 인식이 가능한 정수값으로 변경
		"""
		result = (int(input_data[2])) * (256 ** 2) + (int(input_data[1])) * 256 + int(input_data[0])
		return result

	def change_sheet_name(self, old_name="입력필요", new_name="입력필요"):
		"""
		시트이름을 변경하는 것
		"""
		self.xlbook.Worksheets(old_name).Name = new_name

	def change_string_address(self, input_text="입력필요"):
		"""
		입력형태 : "", "$1:$8", "1", "a","a1", "a1b1", "2:3", "b:b"
		입력된 주소값을 [x1, y1, x2, y2]의 형태로 만들어 주는 것이다
		"""
		aaa = re.compile("[a-zA-Z]+|\d+")
		address_list = aaa.findall(str(input_text))
		temp = []
		result = []

		for one in address_list:
			temp.append(self.check_one_address(one))

		if len(temp) == 1 and temp[0][1] == "string":
			# "a"일때
			result = [0, temp[0][0], 0, temp[0][0]]
		elif len(temp) == 1 and temp[0][1] == "num":
			# 1일때
			result = [temp[0][0], 0, temp[0][0], 0]
		elif len(temp) == 2 and temp[0][1] == temp[1][1] and temp[0][1] == "string":
			# "a:b"일때
			result = [0, temp[0][0], 0, temp[1][0]]
		elif len(temp) == 2 and temp[0][1] == temp[1][1] and temp[0][1] == "num":
			# "2:3"일때
			result = [temp[0][0], 0, temp[1][0], 0]
		elif len(temp) == 2 and temp[0][1] != temp[1][1] and temp[0][1] == "num":
			# "2a"일때
			result = [temp[0][0], temp[1][0], temp[0][0], temp[1][0]]
		elif len(temp) == 2 and temp[0][1] != temp[1][1] and temp[0][1] == "string":
			# "a2"일때
			result = [temp[1][0], temp[0][0], temp[1][0], temp[0][0]]
		elif len(temp) == 4 and temp[0][1] != temp[1][1] and temp[0][1] == "num":
			# "a2b3"일때
			result = [temp[0][0], temp[1][0], temp[2][0], temp[3][0]]
		elif len(temp) == 4 and temp[0][1] != temp[1][1] and temp[0][1] == "string":
			# "2a3c"일때
			result = [temp[1][0], temp[0][0], temp[3][0], temp[2][0]]

		return result

	def change_range_value_to_capital(self, sheet_name, xyxy):
		"""
		change_text_as_capital(sheet_name, xyxy)
		선택한 영역의 값들을 첫글자만 대문자로 변경
		입력값 : 입력값없이 사용가능
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)

		for x in range(x1, x2 + 1):
			for y in range(y1, y2 + 1):
				value = str(sheet_object.Cells(x, y).Value)
				if value == None: value = ""
				value = str(sheet_object.Cells(x, y).Value)

				sheet_object.Cells(x, y).Value = value.capitalize()

	def change_range_value_to_lower(self, sheet_name="", xyxy=""):
		"""
		선택영역안의 모든글자를 소문자로 만들어 주는것
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		for x in range(x1, x2 + 1):
			for y in range(y1, y2 + 1):
				value = str(sheet_object.Cells(x, y).Value)
				if value == None: value = ""
				value = str(sheet_object.Cells(x, y).Value)

				sheet_object.Cells(x, y).Value = value.lower()

	def change_range_value_to_ltrim(self, sheet_name="", xyxy=""):
		"""
		왼쪽끝의 공백을 삭제하는 것
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)

		for x in range(x1, x2 + 1):
			for y in range(y1, y2 + 1):
				cell_value = str(sheet_object.Cells(x, y).Value)
				changed_data = str(cell_value).lstrip()
				if cell_value == changed_data or cell_value == None or type(cell_value) == type(123):
					pass
				else:
					sheet_object.Cells(x, y).Value = changed_data
					self.paint_color_in_cell(sheet_name, [x, y], 16)

	def change_range_value_to_rtrim(self, sheet_name="", xyxy=""):
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		for x in range(x1, x2 + 1):
			for y in range(y1, y2 + 1):
				cell_value = str(sheet_object.Cells(x, y).Value)
				changed_data = str(cell_value).rstrip()
				if cell_value == changed_data or cell_value == None or type(cell_value) == type(123):
					pass
				else:
					sheet_object.Cells(x, y).Value = changed_data

					self.paint_color_in_cell(sheet_name, [x, y], 16)

	def change_range_value_to_strikethrough(self, sheet_name="", xyxy=""):
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet_object.Range(sheet_object.Cells(x1, y1), sheet_object.Cells(x2, y2))
		my_range.Font.Strikethrough = True

	def change_range_value_to_swapcase(self, sheet_name="", xyxy=""):
		"""
		선택한 영역의 값들을 대소문자를 변경
		입력값 : 입력값없이 사용가능
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		for x in range(x1, x2 + 1):
			for y in range(y1, y2 + 1):
				value = str(sheet_object.Cells(x, y).Value)
				if value == None: value = ""
				value = str(sheet_object.Cells(x, y).Value)
				sheet_object.Cells(x, y).Value = value.swapcase()

	def change_range_value_to_trim(self, sheet_name="", xyxy=""):
		"""
		왼쪽끝의 공백을 삭제하는 것
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		for x in range(x1, x2 + 1):
			for y in range(y1, y2 + 1):
				cell_value = str(sheet_object.Cells(x, y).Value)
				changed_data = self.fun_trim(cell_value)
				if cell_value == changed_data or cell_value == None:
					pass
				else:
					sheet_object.Cells(x, y).Value = changed_data
					self.paint_color_in_cell(sheet_name, [x, y], 16)

	def change_range_value_to_underline(self, sheet_name="", xyxy=""):
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet_object.Range(sheet_object.Cells(x1, y1), sheet_object.Cells(x2, y2))

		my_range.Font.Underline = True

	def change_range_value_to_upper(self, sheet_name="", xyxy=""):
		"""
		선택한 영역의 값들을 대문자로 변경
		입력값 : 입력값없이 사용가능
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		for x in range(x1, x2 + 1):
			for y in range(y1, y2 + 1):
				value = str(sheet_object.Cells(x, y).Value)
				if value == None: value = ""

				value = str(sheet_object.Cells(x, y).Value)
				sheet_object.Cells(x, y).Value = value.upper()

	def change_xy_to_a1(self, xy=[3, 4]):
		x_char = self.change_num_to_char(xy[0])
		result = str(x_char[0]) + str(xy[1])
		return result

	def change_xylist_to_addresschar(self, xy_list=[[1, 1], [2, 3], [2, 4]]):
		result = ""
		for one_data in xy_list:
			y_char = self.change_num_to_char(one_data[1])
			result = result + str(y_char[0]) + str(one_data[0]) + ', '
		return result[:-2]

	def change_xyxy_to_r1r1(self, xyxy=""):
		"""
		Input Style :   [1,2,3,4]
		Output Style : "b1:d3"
		"""
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		str_1 = self.change_num_to_char(y1)
		str_2 = self.change_num_to_char(y2)
		result = str_1 + str(x1) + ":" + str_2 + str(y1)
		return result

	def check_address_value(self, input_data=""):
		"""
		입력형태 :, "", [1,2], [1,2,3,4], "$1:$8", "1", "a","a1", "a1b1", "2:3", "b:b"
		입력된 주소값을 [x1, y1, x2, y2]의 형태로 만들어 주는 것이다
		입력된 자료의 형태에 따라서 구분을 한다
		"""
		if input_data == "" or input_data == None:  # 아무것도 입력하지 않을때
			input_type = self.read_address_in_selection()
			result = self.change_string_address(input_type)

		elif type(input_data) == type("string"):  # 문자열일때
			result = self.change_string_address(input_data)

		elif type(input_data) == type([]):  # 리스트형태 일때
			if len(input_data) == 2:
				result = input_data + input_data
			elif len(input_data) == 4:
				result = input_data
		return result

	def check_cell_type(self, input_data="입력필요"):
		"""
		check_cell_type( input_data="입력필요")
		주소형태의 문자열이 어떤 형태인지 알아 내는 것
		입력값 : 주소형태의 문자열
		Output Style : "a1", "aa", "11"
		"""
		result = ""
		if input_data[0][0] in string.ascii_lowercase and input_data[1][0] in string.digits:
			result = "a1"
		if input_data[0][0] in string.ascii_lowercase and input_data[1][0] in string.ascii_lowercase:
			result = "aa"
		if input_data[0][0] in string.digits and input_data[1][0] in string.digits:
			result = "11"
		return result

	def check_data_type(self, input_data="입력필요"):
		"""
		영역으로 입력된 자료의 형태를 확인해서 돌려주는 것
		입력값으로 들어온것이 리스트형태인지, 영역의 형태인지, 값의 형태인지를 알아보는것이다
		Input Style :   1개의 입력값
		Output Style : "list", "range", "value", "error"
		"""
		if type(input_data) == type([]):
			result = "list"
		elif len(str(input_data).split(":")) > 1:
			result = "range"
		elif type(input_data) == type("aaa"):
			result = "value"
		else:
			result = "error"
		return result

	def check_inputdata(self, input_data):
		"""
		입력된 자료형을 확인하는것
		입렫된 자료를 2차원으로 만드는 것
		입력자료는 리스트나 듀플이어야 한다
		"""
		if type(input_data) == type([]):
			if type(input_data[0]) == type([]):
				# 2차원의 자료이므로 입력값 그대로를 돌려준다
				result = "list2d_list"
			elif type(input_data[0]) == type(()):
				result = "list_tuple"
			else:
				result = "list1d"
		elif type(input_data) == type(()):
			if type(input_data[0]) == type([]):
				# 2차원의 자료이므로 입력값 그대로를 돌려준다
				result = "tuple_list"
			elif type(input_data[0]) == type(()):
				result = "tuple_tuple"
			else:
				result = "tuple1d"
		elif type(input_data) == type(123):
			result = "int"
		elif type(input_data) == type("123"):
			result = "string"
		return result

	def check_list_address(self, input_list="입력필요"):
		"""
		주소값을 4자리 리스트로 만들기 위하여 사용하는것
		"""
		result = []
		if len(input_list) == 1:
			xy = str(input_list[0]).lower()
			# 값이 1개인경우 : ['1'], ['a']
			if xy[0] in string.digits:
				result = [xy, 0, xy, 0]
			elif xy[0].lower() in string.ascii_lowercase:
				result = [0, xy, 0, xy]
		elif len(input_list) == 2:
			# 값이 2개인경우 : ['a', '1'], ['2', '3'], ['a', 'd']
			y1 = str(input_list[0]).lower()
			x1 = str(input_list[1]).lower()
			if y1[0] in string.digits:
				if x1[0] in string.digits:
					result = [y1, 0, x1, 0]
				elif x1[0] in string.ascii_lowercase:
					result = [y1, y1, y1, y1]
			elif y1[0] in string.ascii_lowercase:
				if x1[0] in string.digits:
					result = [x1, y1, y1, y1]
				elif x1[0] in string.ascii_lowercase:
					result = [0, y1, 0, x1]
		elif len(input_list) == 4:
			y1 = str(input_list[0]).lower()
			x1 = str(input_list[1]).lower()
			y2 = str(input_list[2]).lower()
			x2 = str(input_list[3]).lower()
			# 값이 4개인경우 : ['aa', '1', 'c', '44'], ['1', 'aa', '44', 'c']
			if y1[0] in string.digits and x2[0] in string.digits:
				if x1[0] in string.ascii_lowercase and x2[0] in string.ascii_lowercase:
					result = [x1, y1, x2, y2]
				elif x1[0] in string.digits and x2[0] in string.digits:
					result = [x1, y1, x2, y2]
			elif y1[0] in string.ascii_lowercase and x2[0] in string.ascii_lowercase:
				if x1[0] in string.digits and x2[0] in string.digits:
					result = [x1, y1, x2, x2]
		final_result = []
		for one in result:
			one_value = str(one)[0]
			if one_value in string.ascii_lowercase:
				aaa = self.change_char_to_num(one)
			else:
				aaa = str(one)
			final_result.append(aaa)
		return final_result

	def check_one_address(self, input_text=""):
		"""
		입력된 1개의 주소를 문자인지, 숫자인지와 숫자로 변경하는 것이다
		"""
		re_com_1 = re.compile("^[a-zA-Z]+$")  # 처음부터 끝가지 알파벳일때
		result_str = re_com_1.findall(str(input_text))

		re_com_2 = re.compile("^[0-9]+$")  # 처음부터 끝가지 숫자일때
		result_num = re_com_2.findall(str(input_text))

		if result_num == [] and result_str != []:
			address_type = "string"
			no = 0
			address_int = 0
			for one in input_text.lower()[::-1]:
				num = string.ascii_lowercase.index(one) + 1
				address_int = address_int + 26 ** no * num
				no = no + 1
		elif result_str == [] and result_num != []:
			address_type = "num"
			address_int = int(input_text)
		else:
			address_int = "error"
			address_type = "error"
		return [address_int, address_type, input_text]

	def check_sheet_name(self, sheet_name=""):
		"""
		시트이름으로 객체를 만들어서 돌려주는 것이다
		"""
		sheet_name = str(sheet_name).lower()
		if sheet_name == "" or sheet_name == None or sheet_name == "activesheet":
			sheet_object = self.xlapp.ActiveSheet
		else:
			sheet_object = self.xlbook.Worksheets(sheet_name)
		return sheet_object

	def check_string_address(self, input_text="입력필요"):
		"""
		Input Style :   "$1:$8", "1", "a","a1", "a1b1", "2:3", "b:b"
		Output Style :숫자와 문자로 된부분을 구분하는 것
		string형태의 address를 문자와 숫자로 나누는것
		"""
		aaa = re.compile("[a-zA-Z]+|\d+")
		result = aaa.findall(str(input_text))
		return result

	def check_xx_address(self, xyxy="입력필요"):
		"""
		입력 주소중 xx가 맞는 형식인지를 확인하는것
		결과= [2, 2]의 형태로 만들어 주는것
		"""
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		result = [x1, x2]
		return result

	def check_xy_address(self, xyxy=""):
		"""
		x나 y의 하나를 확인할때 입력을 잘못하는 경우를 방지하기위해 사용
		Input Style :   3, [3], [2,3], D, [A,D], [D]
		Output Style : [3,3], [2,3], [4,4], [1,4]
		"""
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		result = [x1, y1]
		return result

	def check_yy_address(self, yy="입력필요"):
		"""
		결과= ["b", "b"]의 형태로 만들어 주는것
		"""
		y1, y2 = self.check_address_value(yy)
		result = [y1, y2]
		return result

	def check_inputcolor_rgb(self, input_value):
		input_type = type(input_value)
		if input_type == type(123):
			result = self.color.change_rgbint_to_rgb(input_value)
		elif input_type == type("abc"):
			result = self.color.change_scolor_to_rgb(input_value)
		elif input_type == type([]):
			if input_value[0] > 100 or input_value[1] > 100 or input_value[2] > 100:
				# 리스트는 2가지 형태로 rgb나 hsv가 가능하니 100이상이 되면 hsv이니, 전부 100이하이면 hsv로 하도록 한다
				result = input_value
			else:
				result = self.color.change_hsl_to_rgb(input_value)
		return result

	def compare_two_value(self, raw_data, req_number, project_name, vendor_name, nal):
		self.data = list(raw_data)
		self.data_set = []
		self.data_set_final = []
		for self.a in range(0, len(self.data), 2):
			for self.b in range(len(self.data[1])):
				if not (self.data[self.a + 1][self.b] == self.data[self.a][self.b]) and self.data[self.a + 1][
					self.b] != None and self.data[self.a + 1][self.b] != 0:
					self.data_set.append(self.data[self.a + 1][self.b])
				else:
					self.data_set.append(self.data[self.a][self.b])
			self.data_set.append(req_number)
			self.data_set.append(project_name)
			self.data_set.append(vendor_name)
			self.data_set.append(nal)
			self.data_set_final.append(self.data_set)
			self.data_set = []
		return self.data_set_final

	def close(self):
		self.xlbook.Close(SaveChanges=0)
		del self.xlapp

	def copy_range(self, sheet_name="", xyxy=""):
		sheet_object = self.check_sheet_name(sheet_name)
		self.check_address_value(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		sheet_object.Range(sheet_object.Cells(x1, y1), sheet_object.Cells(x2, y2)).Copy()

	def copy_xxline(self, sheet_name="", xyxy=""):
		"""
		세로의 값을 복사
		"""
		self.copy_range(sheet_name, xyxy)

	def copy_yyline(self, sheet_name="", xyxy=""):
		self.copy_range(sheet_name, xyxy)

	def count_range_samevalue(self, sheet_name="", xyxy=""):
		"""
		 입력값 : 입력값없이 사용가능
		 선택한 영역의 반복되는 갯수를 구한다
		 1. 선택한 영역에서 값을 읽어온다
		 2. 사전으로 읽어온 값을 넣는다
		 3. 열을 2개를 추가해서 하나는 값을 다른하나는 반복된 숫자를 넣는다
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		all_data = self.write_value_in_range("", [x1, y1, x2, y2])
		py_dic = {}
		# 읽어온 값을 하나씩 대입한다
		for line_data in all_data:
			for one_data in line_data:
				# 키가와 값을 확인
				if one_data in py_dic:
					py_dic[one_data] = py_dic[one_data] + 1
				else:
					py_dic[one_data] = 1
		self.insert_yyline_in_range(sheet_name, 1)
		self.insert_yyline_in_range(sheet_name, 1)
		dic_list = list(py_dic.keys())
		for no in range(len(dic_list)):
			sheet_object.Cells(no + 1, 1).Value = dic_list[no]
			sheet_object.Cells(no + 1, 2).Value = py_dic[dic_list[no]]

	def count_sheet_nos(self):
		"""
		시트의 갯수를 돌려준다
		"""
		return self.xlbook.Worksheets.Count

	def delete_all_drawing_in_sheet(self, sheet_name=""):
		"""
		시트안의 모든 객체를 삭제하는 것
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		drawings_no = sheet_object.Shapes.Count
		if drawings_no > 0:
			for aa in range(sheet_object.Shapes.Count, 0, -1):
				# Range를 앞에서부터하니 삭제하자마자 번호가 다시 매겨져서, 뒤에서부터 삭제하니 잘된다
				sheet_object.Shapes(aa).Delete()
		return drawings_no

	def delete_all_line_in_range(self, sheet_name="", xyxy=""):
		"""
		영역의 모든선을 지운다
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet_object.Range(sheet_object.Cells(x1, y1), sheet_object.Cells(x2, y2))
		for each in [5, 6, 7, 8, 9, 10, 11, 12]:
			my_range.Borders(each).LineStyle = -4142

	def delete_all_value_in_sheet(self, sheet_name=""):
		"""
		시트안의 모든 값을 삭제한다
		"""

		sheet_object = self.check_sheet_name(sheet_name)
		sheet_object.Cells.ClearContents()

	def delete_color_in_range(self, sheet_name="", xyxy=""):
		"""
		영역의 색을 지우는 것
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet_object.Range(sheet_object.Cells(x1, y1), sheet_object.Cells(x2, y2))
		my_range.Interior.Pattern = -4142
		my_range.Interior.TintAndShade = 0
		my_range.Interior.PatternTintAndShade = 0

	def delete_continious_samevalue_in_range(self, sheet_name="", xyxy=""):
		"""
		아래로 같은 값들을 지울때
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		for y in range(y2, y1, -1):
			for x in range(x1, x2 + 1):
				base_value = sheet_object.Cells(x, y).Value
				up_value = str(sheet_object.Cells(x, y - 1).Value)
				if base_value == up_value:
					# self.write_value_in_cell(sheet_name, [x, y], "")
					sheet_object.Cells(x, y).Value = ""

	def delete_linecolor_in_range(self, sheet_name="", xyxy=""):
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet_object.Range(sheet_object.Cells(x1, y1), sheet_object.Cells(x2, y2))
		my_range.Interior.Pattern = 0
		my_range.Interior.PatternTintAndShade = 0

	def delete_link_in_range(self, sheet_name="", xyxy=""):
		"""
		영역안의 링크를 삭제하는 것
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet_object.Range(sheet_object.Cells(x1, y1), sheet_object.Cells(x2, y2))

		my_range.Hyperlinks.Delete()

	def delete_memo_in_range(self, sheet_name="", xyxy=""):
		"""
		영역안의 메모를 삭제하는 것
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet_object.Range(sheet_object.Cells(x1, y1), sheet_object.Cells(x2, y2))
		my_range.ClearComments()

	def delete_panthom_rangname(self):
		"""
		엑셀의 이름영역중에서 연결이 끊긴것을 삭제하는 것이다
		"""
		cnt = self.xlapp.Names.Count
		for num in range(1, cnt + 1):
			aaa = self.xlapp.Names(num).Name
			if aaa.find("!") < 0:
				self.xlapp.Names(aaa).Delete()

	def delete_patial_value_in_range_as_0toN(self, sheet_name="", xyxy="", num="입력필요"):
		"""
		선택영역의 값중에서 일부분만 지우는것
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)

		for x in range(x1, x2 + 1):
			for y in range(y1, y2 + 1):

				cell_value = str(sheet_object.Cells(x, y).Value)
				if cell_value != "" or cell_value != None or cell_value != None:
					sheet_object.Cells(x, y).Value = cell_value[int(num):]

	def delete_rangename_by_name(self, range_name):
		"""
		rangename을  삭제하는 것
		"""
		self.xlapp.Names(range_name).Delete()

	def delete_rangename_all(self):
		"""
		rangename을  삭제하는 것
		"""
		aaa = self.xlapp.Names
		for one in aaa:
			ddd = str(one.Name)
			if ddd.find("!") < 0:
				print(one.Name)
				self.xlapp.Names(aaa).Delete()

	def delete_rangname_panthom(self):
		"""
		연결이 끊긴 이름영역을 제거한다
		"""
		cnt = self.xlapp.Names.Count
		for num in range(1, cnt + 1):
			aaa = self.xlapp.Names(num).Name
			if aaa.find("!") < 0:
				self.xlapp.Names(aaa).Delete()

	def delete_samevalue_in_range(self, sheet_name="", xyxy=""):
		"""
		영역안의 같은 값을 지우는 것이다
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		set_a = set([])
		for x in range(x1, x2 + 1):
			for y in range(y1, y2 + 1):
				value = str(sheet_object.Cells(x, y).Value)
				if value == "" or value == None:
					pass
				else:
					len_old = len(set_a)
					set_a.add(value)
					len_new = len(set_a)
					if len_old == len_new:
						sheet_object.Cells(x, y).Value = ""

	def delete_samevalue_in_range_by_many_column_are_same(self, sheet_name="", xyxy="", input_list="입력필요"):
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		base_data_1 = self.write_value_in_range(sheet_name, xyxy)
		base_data_2 = base_data_1
		same_num = len(input_list)
		del_list = []
		for x in range(x1, x2 + 1):
			line_data = base_data_1[x]
			for x_2 in range(x + 1, x2 + 1):
				count = 0
				com_one_line = base_data_1[x_2]
				for one_num in input_list:
					if line_data[one_num] == com_one_line[one_num]:
						count = count + 1
				if count == same_num:
					del_list.append(x_2)
					sheet_object.Range(sheet_object.Cells(x1 + x, y1),
					                   sheet_object.Cells(x1 + x, y2)).ClearContents()

	def delete_shape_in_sheet_by_name(self, sheet_name="", shape_name="입력필요"):
		"""
		객체의 이름으로 제거하는것
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		sheet_object.Shapes(shape_name).Delete()

	def delete_sheet(self, sheet_name=""):
		"""
		시트하나 삭제하기
		"""
		try:
			sheet_object = self.check_sheet_name(sheet_name)
			self.xlapp.DisplayAlerts = False
			sheet_object.Delete()
			self.xlapp.DisplayAlerts = True
		except:
			pass

	def delete_sheet_name(self, sheet_name):
		"""
		셀의 줄바꿈을 설정할때 사용한다
		만약 status를 false로 하면 줄바꿈이 실행되지 않는다.
		self.check_sheet_name (sheet_name)
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		ddd = sheet_object.Cells
		aaa = self.xlapp.Names
		for one in aaa:
			ddd = str(one.Name)
			if ddd.find("!") < 0:
				print(one.Name)

	def delete_value_in_cell(self, sheet_name="", xyxy=""):
		"""
		셀안의 값을 삭제하는것
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		sheet_object.Cells(x1, y1).ClearContents()

	def delete_value_in_range(self, sheet_name="", xyxy=""):
		"""
		영역안의 값을 삭제하는것
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet_object.Range(sheet_object.Cells(x1, y1), sheet_object.Cells(x2, y2))
		my_range.ClearContents()

	def delete_value_in_range_between_a_and_b(self, sheet_name="", xyxy="", input_list=["(", ")"]):
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		# re_basic = "\\"+str(input_new[0]) + "[\^" + str(input_new[0]) +"]*\\" + str(input_new[1])
		input_list[0] = str(input_list[0]).strip()
		input_list[1] = str(input_list[1]).strip()
		special_char = ".^$*+?{}[]\|()"
		# 특수문자는 역슬래시를 붙이도록
		if input_list[0] in special_char: input_list[0] = "\\" + input_list[0]
		if input_list[1] in special_char: input_list[1] = "\\" + input_list[1]
		re_basic = str(input_list[0]) + ".*" + str(input_list[1])
		# 찾은값을 넣을 y열을 추가한다
		new_x = int(x2) + 1
		self.insert_xline(sheet_name, new_x)
		for y in range(y1, y2 + 1):
			temp = ""
			for x in range(x1, x2 + 1):
				cell_value = str(sheet_object.Cells(x, y).Value)
				result_list = re.findall(re_basic, cell_value)
				if result_list == None or result_list == []:
					pass
				else:
					# print("result_list == >", result_list)
					temp = temp + str(result_list)
					# 발견된곳에 색을 칠한다
					self.paint_color_in_cell("", [x, y], "yel++")
			sheet_object.Cells(y, new_x).Value = temp

	def delete_value_in_range_between_specific_letter(self, sheet_name="", xyxy="", input_list=["(", ")"]):
		"""
		(sheet_name="", yxyx="", input_list=["(",")"])
		입력형식 : ["(",")"]
		입력자료의 두사이의 자료를 포함하여 삭제하는것
		예: abc(def)gh ==>abcgh
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)

		# re_basic = "\\"+str(input_new[0]) + "[\^" + str(input_new[0]) +"]*\\" + str(input_new[1])
		input_list[0] = str(input_list[0]).strip()
		input_list[1] = str(input_list[1]).strip()
		special_char = ".^$*+?{}[]\|()"
		# 특수문자는 역슬래시를 붙이도록
		if input_list[0] in special_char: input_list[0] = "\\" + input_list[0]
		if input_list[1] in special_char: input_list[1] = "\\" + input_list[1]
		re_basic = str(input_list[0]) + ".*" + str(input_list[1])
		# 찾은값을 넣을 y열을 추가한다
		new_y = int(y2) + 1
		self.insert_yline(sheet_name, new_y)
		for x in range(x1, x2 + 1):
			temp = ""
			for y in range(y1, y2 + 1):
				cell_value = str(sheet_object.Cells(x, y).Value)
				result_list = re.findall(re_basic, cell_value)
				if result_list == None or result_list == []:
					pass
				else:
					temp = temp + str(result_list)
					# 발견된곳에 색을 칠한다
					self.paint_color_in_range("", [x, y], "yel++")
			sheet_object.Cells(x, new_y).Value = temp

	def delete_value_in_range_by_continious_samevalue(self, sheet_name="", xyxy=""):
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)

		for y in range(y2, y1, -1):
			for x in range(x1, x2 + 1):
				base_value = sheet_object.Cells(x, y).Value
				up_value = sheet_object.Cells(x, y - 1).Value
				if base_value == up_value:
					# self.write_value_in_cell(sheet_name, [x, y], "")
					sheet_object.Cells(x, y).Value = ""

	def delete_value_in_range_by_no(self, sheet_name="", xyxy="", input_no=""):
		"""
		선택한 영역에서 각셀마다 왼쪽에서 N번째까지의글자삭제하기
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)

		for x in range(x1, x2 + 1):
			for y in range(y1, y2 + 1):
				cell_value = str(sheet_object.Cells(x, y).Value)
				if cell_value == "" or cell_value == None or cell_value == None:
					pass
				else:
					# self.write_value_in_cell(sheet_name, [x, y], cell_value[int(input_no):])
					sheet_object.Cells(x, y).Value = cell_value[int(input_no):]

	def delete_value_in_range_by_step(self, sheet_name="", xyxy="", input_list=""):
		"""
		삭제 : 선택자료중 n번째 가로열의 자료를 값만 삭제하는것
		일하다보면 3번째 줄만 삭제하고싶은경우가 있다, 이럴때 사용하는 것이다
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)

		base_data_1 = self.write_value_in_range(sheet_name, xyxy)
		base_data_2 = base_data_1
		same_num = len(input_list)
		del_list = []
		for x in range(x1, x2 + 1):
			line_data = base_data_1[x]
			for x_2 in range(x + 1, x2 + 1):
				count = 0
				com_one_line = base_data_1[x_2]
				for one_num in input_list:
					if line_data[one_num] == com_one_line[one_num]:
						count = count + 1
				if count == same_num:
					del_list.append(x_2)
					sheet_object.Range(sheet_object.Cells(x1 + x, y1),
					                   sheet_object.Cells(x1 + x, y2)).ClearContents()

	def delete_value_in_usedrange(self, sheet_name=""):
		"""
		자주사용하는 것 같아서 usedrange의 값을 지우는것을 만들어 보았다
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		aaa = self.read_usedrange_address(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(aaa)
		my_range = sheet_object.Range(sheet_object.Cells(x1, y1), sheet_object.Cells(x2, y2))
		my_range.ClearContents()

	def delete_rangename(self, sheet_name, range_name):
		"""
		입력한 이름을 삭제한다
		name은 workbook으로 되지만 동일하게 하기위하여 sheet_name을 넣은 것이다
		"""

		result = self.xlbook.Names(range_name).Delete()
		return result

	def delete_xline(self, sheet_name="", xx=""):
		"""
		선택한영역에서 x줄의 값이 없으면 x줄을 삭제한다
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		new_xx = self.check_xx_address(xx)
		sheet_object.Rows(str(new_xx[0]) + ':' + str(new_xx[1])).Delete()

	def delete_xline_in_range_as_empty(self, sheet_name="", xyxy=""):
		"""
		선택한영역에서 x줄의 값이 없으면 x줄을 삭제한다
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)

		for y in range(y2, y1, -1):
			changed_address = str(y) + ":" + str(y)
			num = self.xlapp.WorksheetFunction.CountA(sheet_object.Range(changed_address))
			if num == 0:
				self.delete_xline(sheet_name, y)

	def delete_xline_in_range_by_samevalue(self, sheet_name="", xyxy="", input_list="입력필요"):
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		base_data_1 = self.read_value_in_range(sheet_name, xyxy)
		base_data_2 = base_data_1
		same_num = len(input_list)
		del_list = []
		for y in range(y1, y2 + 1):
			line_data = base_data_1[y]
			for x_2 in range(x1 + 1, x2 + 1):
				count = 0
				com_one_line = base_data_1[x_2]
				for one_num in input_list:
					if line_data[one_num] == com_one_line[one_num]:
						count = count + 1
				if count == same_num:
					del_list.append(x_2)
					sheet_object.Range(sheet_object.Cells(y1 + y, x1),
					                   sheet_object.Cells(y1 + y, x2)).ClearContents()

	def delete_xline_in_range_by_step(self, sheet_name="", xyxy="", step_no="입력필요"):
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		mok, namuji = divmod(y2 - y1 + 1, int(step_no))
		end_no = y2 - namuji
		start_no = y1
		for y in range(end_no, start_no, -1):
			if divmod(y, int(step_no))[1] == 0:
				self.delete_xline(sheet_name, [y, y])

	def delete_xline_value_in_range_by_step(self, sheet_name="", xyxy="", step_no="입력필요"):
		"""
		삭제 : 2 ==> 기존의 2번째 마다 삭제 (1,2,3,4,5,6,7 => 1,3,5,7)
		삽입 : 2 ==> 2번째에 새로운것 추가 (1,2,3,4,5,6,7 => 1,2,2,3,4,4,5,6,6,7)
		삭제 : 선택자료중 n번째 세로줄의 자료를 값만 삭제하는것
		일하다보면 3번째 줄만 삭제하고싶은경우가 있다, 이럴때 사용하는 것
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)

		mok, namuji = divmod(y2 - y1 + 1, int(step_no))
		end_no = y2 - namuji
		start_no = y1

		for y in range(end_no, start_no, -1):
			if divmod(y, int(step_no))[1] == 0:
				self.delete_value_in_range(sheet_name, [y, x1, y, x2])

	def delete_xxline_in_sheet(self, sheet_name, xx):
		"""
		가로 한줄삭제하기
		입력형태는 2, [2,3]의 두가지가 가능하다
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		new_xx = self.check_xy_address(xx)
		sheet_object.Rows(str(new_xx[0]) + ':' + str(new_xx[1])).Delete(-4121)

	def delete_yline(self, sheet_name="", yy=""):
		"""
		선택한영역에서 x줄의 값이 없으면 x줄을 삭제한다
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		new_yy = self.check_yy_address(yy)
		sheet_object.Rows(str(new_yy[0]) + ':' + str(new_yy[1])).Delete()

	def delete_yline_in_range_bystep(self, sheet_name="", xyxy="", step_no="입력필요"):
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)

		mok, namuji = divmod(y2 - y1 + 1, int(step_no))
		end_no = y2 - namuji
		start_no = y1
		for y in range(end_no, start_no, -1):
			if divmod(y, int(step_no))[1] == 0:
				self.delete_yline(sheet_name, [y, y])

	def delete_yline_value_in_range_bystep(self, sheet_name="", xyxy="", step_no="입력필요"):
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)

		mok, namuji = divmod(y2 - y1 + 1, int(step_no))
		end_no = y2 - namuji
		start_no = y1
		for y in range(end_no, start_no, -1):
			if divmod(y, int(step_no))[1] == 0:
				self.delete_value_in_range(sheet_name, [x1, y, x2, y])

	def delete_yyline_in_sheet(self, sheet_name, yy):
		"""
		세로 한줄삭제하기
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		new_yy = self.check_xy_address(yy)
		sheet_object.Columns(str(new_yy[0]) + ':' + str(new_yy[1])).Delete()

	def draw_bottomline_in_range(self, sheet_name="", xyxy="", line_style="", thickness="입력필요", color="입력필요"):
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet_object.Range(sheet_object.Cells(x1, y1), sheet_object.Cells(x2, y2))

		rgb_list = self.color.change_scolor_to_rgb(color)
		my_range.Borders(9).Color = self.color.change_rgb_to_rgbint(rgb_list)
		my_range.Borders(9).Weight = thickness
		my_range.Borders(9).LineStyle = line_style

	def draw_innerx_line_in_range(self, sheet_name="", xyxy="", line_style="", thickness="입력필요", color="입력필요"):
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet_object.Range(sheet_object.Cells(x1, y1), sheet_object.Cells(x2, y2))

		rgb_list = self.color.change_scolor_to_rgb(color)
		my_range.Borders(12).Color = self.color.change_rgb_to_rgbint(rgb_list)
		my_range.Borders(12).Weight = thickness
		my_range.Borders(12).LineStyle = line_style

	def draw_innery_line_in_range(self, sheet_name="", xyxy="", line_style="", thickness="입력필요", color="입력필요"):
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet_object.Range(sheet_object.Cells(x1, y1), sheet_object.Cells(x2, y2))

		rgb_list = self.color.change_scolor_to_rgb(color)
		my_range.Borders(11).Color = self.color.change_rgb_to_rgbint(rgb_list)
		my_range.Borders(11).Weight = thickness
		my_range.Borders(11).LineStyle = line_style

	def draw_left_line_in_range(self, sheet_name="", xyxy="", line_style="", thickness="입력필요", color="입력필요"):
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet_object.Range(sheet_object.Cells(x1, y1), sheet_object.Cells(x2, y2))

		rgb_list = self.color.change_scolor_to_rgb(color)
		my_range.Borders(7).Color = self.color.change_rgb_to_rgbint(rgb_list)
		my_range.Borders(7).Weight = thickness
		my_range.Borders(7).LineStyle = line_style

	def draw_line_in_pxyxy_range(self, sheet_name, line_xyxy, rgb_int):
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(line_xyxy)

		sheet_object.Shapes.AddLine(x1, y1, x2, y2).Select()
		self.xlapp.Selection.ShapeRange.Line.ForeColor.RGB = rgb_int
		self.xlapp.Selection.ShapeRange.Line.Weight = 5

	def draw_line_in_range(self, sheet_name="", xyxy="", input_list=""):
		"""
		입력예 : [선의위치, 라인스타일, 굵기, 색깔] ==> [7,1,2,1], ["o","","4","bla"]
		""으로 된것이 기본으로 설정하는 것이다
		"l": left, "t": top, "b": bottom, "r": right, "h": horizental, "v": vertical, "a": all,"o": outside,"/": "/","\\": "\",
		"""

		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet_object.Range(sheet_object.Cells(x1, y1), sheet_object.Cells(x2, y2))

		line_position = {"l": [7], "t": [8], "b": [9], "r": [10], "h": [11], "v": [12], "a": [7, 8, 9, 10, 11, 12],
		                 "o": [7, 8, 9, 10],
		                 "/": [6], "\\": [5], "left": [7], "top": [8], "bottom": [9], "right": [10], "inside-h": [11],
		                 "inside-v": [12],
		                 "대각선오른쪽": [6], "대각선왼쪽": [5], "왼쪽": [7], "위쪽": [8], "아래쪽": [9], "오른쪽": [10], "안쪽세로": [11],
		                 "안쪽가로": [12],
		                 }
		line_style_dic = {"": 1, "-": -4115, "-.": 4, "-..": 5, ".": -4142, " = ": -4119, "no": -4118, "/.": 13,
		                  }
		weight_dic = {"": 2, "4": 1, "5": 2, "6": -4138, "7": 4,
		              "basic": -4138, "실선": -4138, "매우가는선": 1, "가는선": 2, "굵은선": 4, "진한선": 4,
		              }
		rgb_list = self.color.change_scolor_to_rgb(input_list[3])
		color_int = self.color.change_rgb_to_rgbint(rgb_list)
		for po_no in line_position[input_list[0]]:
			my_range.Borders(po_no).Color = color_int
			my_range.Borders(po_no).Weight = weight_dic[input_list[2]]
			my_range.Borders(po_no).LineStyle = line_style_dic[input_list[1]]

	def draw_user_style_02(self, sheet_name="", xyxy=""):
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		range_head = [x1, y1, x1, y2]
		range_body = [x1 + 1, y1, x2 - 1, y2]
		range_tail = [x2, y1, x2, y2]
		range_outside = [x1, y1, x2, y2]

		line_list_head = [["o", "", "5", "bla"], ["h", "", "5", "bla"], ]
		line_list_body = [["v", "", "4", "bla"], ["h", "", "5", "bla"], ]
		line_list_tail = [["o", "", "5", "bla"], ["h", "", "5", "bla"], ]
		line_list_outside = [["o", "", "6", "red"], ]

		for one in line_list_head:
			self.draw_line_in_range(sheet_name, range_head, one)
		for one in line_list_body:
			self.draw_line_in_range(sheet_name, range_body, one)
		for one in line_list_tail:
			self.draw_line_in_range(sheet_name, range_tail, one)
		for one in line_list_outside:
			self.draw_line_in_range(sheet_name, range_outside, one)

	def draw_triangle(self, xyxy, per=100, reverse=1, size=100):
		"""
		직각삼각형
		정삼각형에서 오른쪽이나 왼쪽으로 얼마나 더 간것인지
		100이나 -100이면 직삼각형이다
		사각형은 왼쪽위에서 오른쪽 아래로 만들어 진다
		"""
		x1, y1, x2, y2 = xyxy
		width = x2 - x1
		height = y2 - y1
		lt = [x1, y1]  # left top
		lb = [x2, y1]  # left bottom
		rt = [x1, y2]  # right top
		rb = [x2, y2]  # right bottom
		tm = [x1, int(y1 + width / 2)]  # 윗쪽의 중간
		lm = [int(x1 + height / 2), y1]  # 윗쪽의 중간
		rm = [int(x1 + height / 2), y1]  # 윗쪽의 중간
		bm = [x2, int(y1 + width / 2)]  # 윗쪽의 중간
		center = [int(x1 + width / 2), int(y1 + height / 2)]

		result = [lb, rb, rt]
		return result

	def draw_detail_line_in_range(self, **input):
		enum_line = {
			"msoArrowheadNone": 1, "msoArrowheadTriangle": 2, "msoArrowheadOpen": 3, "msoArrowheadStealth": 4,
			"msoArrowheadDiamond": 5, "msoArrowheadOval": 6,
			"": 1, "<": 2, ">o": 3, ">>": 4, ">": 2, "<>": 5, "o": 6,
			"basic": 1, "none": 1, "triangle": 2, "open": 3, "stealth": 4, "diamond": 5, "oval": 6,
			"msoArrowheadNarrow": 1, "msoArrowheadWidthMedium": 2, "msoArrowheadWide": 3,
			"msoArrowheadShort": 1, "msoArrowheadLengthMedium": 2, "msoArrowheadLong": 3,
			"short": 1, "narrow": 1, "medium": 2, "long": 3, "wide": 3,
			"-1": 1, "0": 2, "1": 3,
			"dash": 4, "dashdot": 5, "dashdotdot": 6, "rounddot": 3, "longdash": 7, "longdashdot": 8,
			"longdashdotdot": 9,
			"squaredot": 2,
			"-": 4, "-.": 5, "-..": 6, ".": 3, "--": 7, "--.": 8, "--..": 9, "ㅁ": 2,
		}
		base_data = {
			"sheet_name": "",
			"xyxy": [100, 100, 0, 0],
			"color": 10058239,
			"line_style": "-.",
			"thickness": 0.5,
			"transparency": 0,
			"head_style": ">",
			"head_length": "0",
			"head_width": "0",
			"tail_style": ">",
			"tail_length": "0",
			"tail_width": "0",
		}
		# 기본자료에 입력받은값을 update하는것이다
		sheet_object = self.check_sheet_name("")
		base_data.update(input)
		sheet = self.check_sheet_name(base_data["sheet_name"])
		set_line = sheet_object.Shapes.AddLine(base_data["xyxy"][0], base_data["xyxy"][1], base_data["xyxy"][2], base_data["xyxy"][3])
		set_line.Select()
		set_line.Line.ForeColor.RGB = base_data["color"]
		set_line.Line.DashStyle = enum_line[base_data["line_style"]]
		set_line.Line.Weight = base_data["thickness"]
		set_line.Line.Transparency = base_data["transparency"]
		# 엑셀에서는 Straight Connector 63의 형태로 이름이 자동적으로 붙여진다
		set_line.Line.BeginArrowheadStyle = enum_line[base_data["head_style"]]
		set_line.Line.BeginArrowheadLength = enum_line[base_data["head_length"]]
		set_line.Line.BeginArrowheadWidth = enum_line[base_data["head_width"]]
		set_line.Line.EndArrowheadStyle = enum_line[base_data["tail_style"]]  # 화살표의 머리의 모양
		set_line.Line.EndArrowheadLength = enum_line[base_data["tail_length"]]  # 화살표의 길이
		set_line.Line.EndArrowheadWidth = enum_line[base_data["tail_width"]]  # 화살표의 넓이
		result = set_line.Name
		return result

	def dump_value_in_range_at_newsheet(self, input_datas):
		self.add_sheet_new()
		self.write_value_in_range("", [1, 1], input_datas)

	def excel_fun_ltrim(self, input_data):
		aaa = self.xlapp.WorksheetFunction.LTrim(input_data)
		return aaa

	def excel_fun_rtrim(self, input_data):
		aaa = self.xlapp.WorksheetFunction.RTrim(input_data)
		return aaa

	def excel_fun_trim(self, input_data="입력필요"):
		aaa = self.xlapp.WorksheetFunction.Trim(input_data)
		return aaa

	def fill_emptycell_in_range_as_uppercell(self, sheet_name="", xyxy=""):
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet_object.Range(sheet_object.Cells(x1, y1), sheet_object.Cells(x2, y2))
		old_data = ""
		for x in range(x1, x2 + 1):
			for y in range(y1, y2 + 1):
				cell_value = str(sheet_object.Cells(x, y).Value)
				if y == y1:
					# 만약 자료가 제일 처음이라면
					old_data = cell_value
				else:
					if cell_value == None or cell_value == "":
						sheet_object.Cells(x, y).Value = old_data

					else:
						old_data = cell_value

	def get_activesheet_object(self):
		sheet_name = self.xlapp.ActiveSheet.Name
		sheet_object = self.check_sheet_name(sheet_name)
		return sheet_object

	def get_diagonal_xy(self, xyxy=[5, 9, 12, 21]):
		"""
		좌표와 대각선의 방향을 입력받으면, 대각선에 해당하는 셀을 돌려주는것
		좌표를 낮은것 부터 정렬하기이한것 [3, 4, 1, 2] => [1, 2, 3, 4]
		"""
		result = []
		if xyxy[0] > xyxy[2]:
			x1, y1, x2, y2 = xyxy[2], xyxy[3], xyxy[0], xyxy[1]
		else:
			x1, y1, x2, y2 = xyxy

		x_height = abs(x2 - x1) + 1
		y_width = abs(y2 - y1) + 1
		step = x_height / y_width
		temp = 0

		if x1 <= x2 and y1 <= y2:
			# \형태의 대각선
			for y in range(1, y_width + 1):
				x = y * step
				if int(x) >= 1:
					final_x = int(x) + x1 - 1
					final_y = int(y) + y1 - 1
					if temp != final_x:
						result.append([final_x, final_y])
						temp = final_x
		else:
			for y in range(y_width, 0, -1):
				x = x_height - y * step

				final_x = int(x) + x1
				final_y = int(y) + y1 - y_width
				temp_no = int(x)

				if temp != final_x:
					temp = final_x
					result.append([final_x, final_y])
		return result

	def get_sheet_object(self, sheet_name=""):
		if str(sheet_name).lower() == "activesheet" or sheet_name == "":
			sheet = self.xlapp.ActiveSheet
		elif sheet_name in self.read_activesheet_name():
			sheet_object = self.check_sheet_name(sheet_name)
		else:
			self.insert_workbook_sheet()
			old_sheet_name = self.read_activesheet_name()
			self.change_sheet_name(old_sheet_name, sheet_name)
			sheet_object = self.check_sheet_name(sheet_name)
		return sheet_object

	def get_vba_module_name(self, ):
		"""
		현재 열려진 엑셀 화일안의 매크로모듈 이름을 찾아서 돌려주는 것
		아래에 1,2,3을 쓴것은 모듈의 종류를 여러가지인데, 해당하는 모듈의 종류이며.
		이것을 하지 않으면 다른 종류의 것들도 돌려쥬기 때문이다

		 xlapp.Close(SaveChanges=False)
		 xlapp.Quit()
		 del.xlapp
		"""
		result = []
		for i in self.xlbook.VBProject.VBComponents:
			if i.type in [1, 2, 3]:
				result.append(i.Name)
		return result

	def get_xxline_object(self, sheet_name, xx):
		new_x = self.check_xx_address(xx)
		sheet_object = self.check_sheet_name(sheet_name)
		result = sheet_object.Rows(str(new_x[0]) + ':' + str(new_x[1]))
		return result

	def get_yyline_object(self, sheet_name, yy):
		"""
		yy영역을 돌려주는것
		"""
		new_y = self.check_yy_address(yy)
		sheet_object = self.check_sheet_name(sheet_name)
		result = sheet_object.Columns(str(new_y[0]) + ':' + str(new_y[1]))
		return result

	def hide_sheet(self, sheet_name, hide=0):
		"""
		시트 숨기기
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		sheet_object.Visible = hide

	def hide_workbook(self):
		"""
		실행되어있는 엑셀을 화면에 보이지 않도록 설정합니다
		"""
		self.xlapp.Visible = 0

	def input_messagebox_value(self, text_01="Pyofficer"):
		"""
		입력창을 만들어서 입력값을 받는것
		"""
		result = self.xlapp.InputBox(text_01)
		return result

	def insert_image_in_sheet(self, sheet_name, file_path, xywh, link=0, image_in_file=1):
		"""
		image화일을 넣는것
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		rng = sheet_object.Cells(xywh[0], xywh[1])
		# sh.Shapes.AddPicture("화일이름", "링크가있나", "문서에저장", "x좌표", "y좌표", "넓이","높이")
		sheet_object.Shapes.AddPicture(file_path, link, image_in_file, rng.Left, rng.Top, xywh[2], xywh[3])

	def insert_line_in_sheet(self, data, number=1, input_data=[]):
		"""
		리스트에 일정한 간격으로 자료삽입
		"""
		total_number = len(data)
		dd = 0
		for a in range(len(data)):
			if a % number == 0 and a != 0:
				if total_number != a:
					data.insert(dd, input_data)
					dd = dd + 1
			dd = dd + 1
		return data

	def insert_sheet(self, sheet_name=""):
		"""
		시트하나 추가하기
		"""
		if sheet_name == "":
			self.xlbook.Worksheets.Add()
		else:
			self.xlbook.Worksheets.Add()
			old_name = self.xlapp.ActiveSheet.Name
			self.xlbook.Worksheets(old_name).Name = sheet_name

	def insert_sheet_with_name(self, new_name="입력필요"):
		"""
		 입력값 : 입력값없이 사용가능
		 시트하나 추가하기
		"""
		if new_name == "":
			self.xlbook.Worksheets.Add()
		else:
			self.xlbook.Worksheets.Add()
			old_name = self.xlapp.ActiveSheet.Name
			self.xlbook.Worksheets(old_name).Name = new_name

	def insert_picture_in_sheet(self, sheet_name):
		sheet_object = self.check_sheet_name(sheet_name)
		sheet_object.Shapes.AddPicture("c:\icon_sujun.gif", 0, 1, 541.5, 92.25, 192.75, 180)

	def insert_xline(self, sheet_name, xx):
		"""
		가로열을 한줄삽입하기
		"""
		self.insert_xxline(sheet_name, xx)

	def insert_xxline(self, sheet_name, xx):
		"""
		가로열을 한줄삽입하기
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		value_list = self.split_value_as_engnum(xx)
		num_1 = self.change_char_to_num(value_list[0])
		if len(value_list) == 2:
			num_2 = self.change_char_to_num(value_list[1])
		else:
			num_2 = num_1
		print("insert_yyline ==> ", num_1, num_2)
		sheet_object.Range(str(num_1) + ':' + str(num_2)).Insert(-4121)

	def insert_xline_in_range_bystep(self, sheet_name="", xyxy="", step_no="입력필요"):
		"""
		n번째마다 열을 추가하는것
		새로운 가로열을 선택한 영역에 1개씩 추가하는것
		n번째마다는 n+1번째가 추가되는 것
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet_object.Range(sheet_object.Cells(x1, y1), sheet_object.Cells(x2, y2))

		for x in range(0, x2 - x1 + 1):
			mok, namuji = divmod(x, int(step_no))
			if namuji == step_no - 1:
				print("===>", x + x1)
				x_no = self.change_char_to_num(x + x1)
				print("===>", x_no)
				sheet_object.Range(str(x_no) + ':' + str(x_no)).Insert(-4121)

	def insert_xxline_in_range(self, sheet_name="", xx="입력필요"):
		"""
		가로열을 한줄삽입하기
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		xx = self.check_xx_address(xx)
		sheet_object.Rows(str(xx[0]) + ':' + str(xx[1])).Insert()

	def insert_yline(self, sheet_name, y):
		"""
		 세로행을 한줄삽입하기
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		num_r1 = self.change_num_to_char(y)
		sheet_object.Columns(str(num_r1) + ':' + str(num_r1)).Insert(-4121)

	def split_value_as_engnum(self, data):
		"""
		 단어중에 나와있는 숫자, 영어를 분리하는기능
		"""
		re_compile = re.compile(r"[a-zA-Z0-9]+")
		result = re_compile.findall(data)

		new_result = []
		for dim1_data in result:
			for dim2_data in dim1_data:
				new_result.append(dim2_data)
		return new_result

	def insert_yyline(self, sheet_name, yy):
		"""
		 세로행을 한줄삽입하기
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		value_list = self.split_value_as_engnum(yy)

		num_1 = self.change_num_to_char(value_list[0])
		if len(value_list) == 2:
			num_2 = self.change_num_to_char(value_list[1])
		else:
			num_2 = num_1
		sheet_object.Columns(str(num_1) + ':' + str(num_2)).Insert()

	def insert_yline_in_range_bystep(self, sheet_name="", xyxy="", step_no="입력필요"):
		"""
		 n번째마다 열을 추가하는것
		 새로운 가로열을 선택한 영역에 1개씩 추가하는것
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)

		# 일정부분으로 추가되는것을 앞에서부터 적용
		step_no = int(step_no)
		add_y = 0
		for no in range(0, y2 - y1 + 1):
			y = add_y + no
			if divmod(y, step_no)[1] == step_no - 1:
				self.insert_yyline_in_range(sheet_name, y + y1)
				add_y = add_y + 1

	def insert_yyline_in_range(self, sheet_name="", yy="입력필요"):
		"""
		 가로열을 한줄삽입하기
		"""
		self.insert_yyline(sheet_name, yy)

	def intersect_range1_range2(self, rng1="입력필요", rng2="입력필요"):
		"""
		두개의 영역에서 교차하는 구간을 돌려준다
		만약 교차하는게 없으면 ""을 돌려준다
		"""
		range_1 = self.check_address_value(rng1)
		range_2 = self.check_address_value(rng2)
		x11, y11, x12, y12 = range_1
		x21, y21, x22, y22 = range_2
		if x11 == 0:
			x11 = 1
			x12 = 1048576
		if x21 == 0:
			x21 = 1
			x22 = 1048576
		if y11 == 0:
			y11 = 1
			y12 = 16384
		if y21 == 0:
			y21 = 1
			y22 = 16384
		new_range_x = [x11, x21, x12, x22]
		new_range_y = [y11, y21, y12, y22]
		new_range_x.sort()
		new_range_y.sort()
		if x11 <= new_range_x[1] and x12 >= new_range_x[2] and y11 <= new_range_y[1] and y12 >= new_range_y[1]:
			result = [new_range_x[1], new_range_y[1], new_range_x[2], new_range_y[2]]
		else:
			result = "교차점없음"
		return result

	def is_empty_xline(self, sheet_name, no):
		"""
		열전체가 빈 것인지 확인해서 돌려준다
		현재의 기능은 한줄만 가능하도록 하였다
		다음엔 영역이 가능하도록 하여야 겠다
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		result = self.xlapp.WorksheetFunction.CountA(sheet_object.Rows(no).EntireRow)
		return result

	def is_empty_yline(self, sheet_name, no):
		"""
		열전체가 빈 것인지 확인해서 돌려준다
		현재의 기능은 한줄만 가능하도록 하였다
		다음엔 영역이 가능하도록 하여야 겠다
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		result = self.xlapp.WorksheetFunction.CountA(sheet_object.Rows(no).EntireColumn)
		return result

	def lock_sheet(self, sheet_name="", password="1234"):
		sheet_object = self.check_sheet_name(sheet_name)
		sheet_object.protect(password)

	def make_y_value(self, input_data):
		result = []
		if len(input_data) > 0:
			if type(input_data[0]) != type([]):
				for one in input_data:
					result.append([one, ])
		return result

	def making_tag(self, ):
		import pcell
		excel = pcell.pcell('activeworkbook')
		all_data = self.write_value_in_range("Sheet1", [1, 1, 90, 15])
		for no_1 in range(len(all_data)):
			x = int((no_1 + 1) / 5)
			y = (no_1 + 1) - x * 5
			for no_2 in range(15):
				self.write_value_in_cell("Tag", [x * 20 + no_2 + 4, y * 3 + 3], all_data[no_1][no_2])

	def move_bottom_in_range(self, sheet_name="", xyxy=""):
		"""
		선택한 위치에서 끝부분으로 이동하는것
		xlDown: - 4121,xlToLeft : - 4159, xlToRight: - 4161, xlUp : - 4162
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		sheet_object.Cells(x1, y1).End(- 4121).Select()

	def move_cell_to_another_sheet(self, sheet_list="입력필요", xy_list="입력필요"):
		sheet1 = self.check_sheet_name(sheet_list[0])
		sheet2 = self.check_sheet_name(sheet_list[1])
		range_old = sheet1.Cells(xy_list[0][0], xy_list[0][1])
		range_new = sheet2.Cells(xy_list[1][0], xy_list[1][1])
		range_old.Select()
		range_old.Cut()
		range_new.Select()
		range_new.Paste()

	def move_degree_distance(self, degree="입력필요", distance="입력필요"):
		"""
		move_degree_distance( degree="입력필요", distance="입력필요")
		현재 위치 x,y에서 30도로 20만큼 떨어진 거리의 위치를 돌려주는 것
		"""
		degree = degree * 3.141592 / 180
		y = distance * math.cos(degree)
		x = distance * math.sin(degree)
		return [x, y]

	def move_activecell_to_leftend_in_range(self, sheet_name="", xyxy=""):
		"""
		입력값 : 입력값없이 사용가능
		선택한 위치에서 끝부분으로 이동하는것
		xlDown : - 4121, xlToLeft : - 4159, xlToRight : - 4161, xlUp : - 4162
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet_object.Range(sheet_object.Cells(x1, y1), sheet_object.Cells(x2, y2))
		sheet_object.Cells(x1, y1).End(- 4159).Select()

	def move_activecell_to_rightend_in_range(self, sheet_name="", xyxy=""):
		"""
		선택한 위치에서 끝부분으로 이동하는것
		xlDown: - 4121,xlToLeft : - 4159, xlToRight: - 4161, xlUp : - 4162
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet_object.Range(sheet_object.Cells(x1, y1), sheet_object.Cells(x2, y2))
		my_range.End(- 4161).Select()

	def move_activecell_to_top_in_range(self, sheet_name="", xyxy=""):
		sheet_object = self.check_sheet_name(sheet_name)
		"""
		선택한 위치에서 끝부분으로 이동하는것
		xlDown: - 4121,xlToLeft : - 4159, xlToRight: - 4161, xlUp : - 4162
		"""
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet_object.Range(sheet_object.Cells(x1, y1), sheet_object.Cells(x2, y2))
		my_range.End(- 4162).Select()
		return "ok"

	def move_value_in_range_to_left_except_emptycell(self, sheet_name="", xyxy=""):
		"""
		선택한 영역에서 세로의 값중에서 빈셀을 만나면, 아래의 값중 있는것을 위로 올리기
		전체영역의 값을 읽어오고, 하나씩 다시 쓴다
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet_object.Range(sheet_object.Cells(x1, y1), sheet_object.Cells(x2, y2))
		value_2d = self.read_value_in_range(sheet_name, xyxy)
		self.delete_value_in_range(sheet_name, xyxy)
		for x in range(0, x2 - x1 + 1):
			new_y = 0
			for y in range(0, y2 - y1 + 1):
				value = value_2d[x][y]
				if value == "" or value == None:
					pass
				else:
					sheet_object.Cells(x + x1, new_y + y1).Value = value
					new_y = new_y + 1

	def move_xxline_to_another_sheet(self, sheet_list="입력필요", xx_list="입력필요"):
		sheet1 = self.check_sheet_name(sheet_list[0])
		sheet2 = self.check_sheet_name(sheet_list[1])
		xx0_1, xx0_2 = self.check_xy_address(xx_list[0])
		xx1_1, xx1_2 = self.check_xy_address(xx_list[1])
		xx0_1 = self.change_char_to_num(xx0_1)
		xx0_2 = self.change_char_to_num(xx0_2)
		xx1_1 = self.change_char_to_num(xx1_1)
		xx1_2 = self.change_char_to_num(xx1_2)
		sheet1.Select()
		sheet1.Columns(str(xx0_1) + ':' + str(xx0_2)).Select()
		sheet1.Columns(str(xx0_1) + ':' + str(xx0_2)).Copy()
		sheet2.Select()
		sheet2.Columns(str(xx1_1) + ':' + str(xx1_2)).Select()
		sheet2.Columns(str(xx1_1) + ':' + str(xx1_2)).Insert()
		if sheet1 == sheet2:
			if xx0_1 <= xx1_1:
				sheet1.Columns(str(xx0_1) + ':' + str(xx0_2)).Delete()
			else:
				new_xx0_1 = self.change_num_to_char(xx0_1 + xx1_2 - xx1_1)
				new_xx0_2 = self.change_num_to_char(xx0_2 + xx1_2 - xx1_1)
				sheet1.Columns(str(new_xx0_1) + ':' + str(new_xx0_2)).Delete()
		else:
			sheet1.Columns(str(xx0_1) + ':' + str(xx0_2)).Delete()

	def move_yyline(self, sheet_list="입력필요", yy_list="입력필요"):
		range_1 = self.select_range(sheet_list[0], yy_list[0])
		range_1.Select()
		range_1.Cut()

		range_2 = self.select_range(sheet_list[1], yy_list[1])
		range_2.Select()
		range_2.Insert()

	def move_yyline_to_another_sheet(self, sheet_name_list, yy_list):
		"""
		세로의 값을 이동시킵니다
		"""
		sheet1 = self.check_sheet_name(sheet_name_list[0])
		sheet2 = self.check_sheet_name(sheet_name_list[1])
		yy0_1, yy0_2 = self.check_xy_address(yy_list[0])
		yy1_1, yy1_2 = self.check_xy_address(yy_list[1])
		yy0_1 = self.change_num_to_char(yy0_1)
		yy0_2 = self.change_num_to_char(yy0_2)
		yy1_1 = self.change_num_to_char(yy1_1)
		yy1_2 = self.change_num_to_char(yy1_2)
		sheet1.Select()
		sheet1.Columns(str(yy0_1) + ':' + str(yy0_2)).Select()
		sheet1.Columns(str(yy0_1) + ':' + str(yy0_2)).Cut()
		sheet2.Select()
		sheet2.Columns(str(yy1_1) + ':' + str(yy1_2)).Select()
		sheet2.Columns(str(yy1_1) + ':' + str(yy1_2)).Insert()

	def merge_eachline_in_range(self, sheet_name="", xyxy=""):  # 셀들을 합하는 것이다
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet_object.Range(sheet_object.Cells(x1, y1), sheet_object.Cells(x2, y2))

		if y1 == y2:
			my_range.Merge(0)
		else:
			for a in range(y2 - y1 + 1):
				sheet_object.Range(sheet_object.Cells(y1 + a, x1), sheet_object.Cells(y1 + a, x2)).Merge(0)

	def move_rangevalue_linevalue(self, sheet_name="", xyxy=""):
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet_object.Range(sheet_object.Cells(x1, y1), sheet_object.Cells(x2, y2))

		output_list = self.read_value(sheet_name, xyxy)
		make_one_list = self.yt.change_list1d_to_list2d(output_list)
		self.insert_cols(sheet_name, x2 + 1)
		self.write_value_from_top_to_down(sheet_name, [y1, x2 + 1], make_one_list)

	def move_compare_2sheets(self):
		"""
		전체가 빈 가로열 삭제
		두개의 시트에서 기준시트와 똑같은 열로 다른 시트를 옮기는것이름으로
		1. 현재의 시트 이름을 알아온다
		2. 옮길 시트이름을 얻는다
		3. 기준시트의 사용된영역중 첫번째 열의 모든 내용을 읽어온다
		4. 옮길시트의 사용된영역중 첫번째 열의 모든 내용을 읽어온다
		5. 두개를 비교해서 몇번째로 이동을 할것인지 새로운 기준시트의 첫번째 열의 모든 내용을 읽어와서 하나씩 비교를 한다
		"""

		sheet_name_1 = self.read_activesheet_name()
		sheet_name_2 = self.read_inputbox_value()
		var_1 = self.read_usedrange_address(sheet_name_1)[2]
		var_2 = self.read_usedrange_address(sheet_name_2)[2]
		sheet_1_end_num = self.change_address_to_xyxy(var_1)[1][2]
		sheet_2_end_num = self.change_address_to_xyxy(var_1)[1][2]
		for x1 in range(1, sheet_1_end_num + 1):
			var_3 = self.read_value_in_cell(sheet_name_1, [1, x1])
			var_5 = 0
			for x2 in range(1, sheet_2_end_num):
				var_4 = self.read_value_in_cell(sheet_name_2, [1, x2])
				if var_3 == var_4 and var_5 == 0:
					self.insert_xline(sheet_name_2, x1)
					self.copy_range(sheet_name_2, sheet_name_2, x2 + 1, x1)
					self.delete_xline(sheet_name_2, x2 + 1)
					var_5 = 1
			if var_5 == 0:
				self.insert_xline(sheet_name_2, x1)
				sheet_2_end_num = sheet_2_end_num + 1

	def move_arrange_two_sheet_y_02(self, sheet_name="", xyxy=""):
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet_object.Range(sheet_object.Cells(x1, y1), sheet_object.Cells(x2, y2))
		input_list = []
		# 기준시트와 옮길시트의 이름을 갖고온다
		input_data = self.input_messagebox_value("Please input specific char : ex) sheet_a, sheet_b")
		sheet_names = input_data.split(",")
		# sheet_names = ["aaa", "bbb"]
		# 사용한 범위를 갖고온다
		range_1 = self.read_usedrange_address(sheet_names[0])
		range_2 = self.read_usedrange_address(sheet_names[1])
		no_title2 = range_2[2]
		# 기준 시트의 제목을 읽어와서 저장한다
		title_1 = self.write_value_in_range(sheet_names[0], [1, range_1[1], 1, range_1[3]])
		title_1_list = []
		for no in range(1, len(title_1[0]) + 1):
			title_1_list.append([no, title_1[0][no - 1]])
		# 하나씩 옮길시트의 값을 읽어와서 비교한후 맞게 정렬한다
		for y1 in range(len(title_1_list)):
			found = 0
			basic_title = title_1_list[y1][1]
			# print("기준자료 == >", basic_title)
			# 기준자료의 제목이 비어잇으면 새로이 한칸을 추가한다
			if basic_title == None or basic_title == "":
				self.insert_yyline_in_range(sheet_names[1], y1 + 1)
				no_title2 = no_title2 + 1
			else:
				# 만약 기준시트의 제목보다 더 넘어가면 그냥 넘긴다
				if y1 > no_title2:
					pass
				else:
					for y2 in range(y1, no_title2 + 1):
						move_title = self.read_value_in_cell(sheet_names[1], [1, y2 + 1])
						if found == 0 and move_title == basic_title:
							# print("발견자료 == >", move_title)
							found = 1
							if y1 == y2:
								pass
							else:
								self.move_yyline(sheet_names[1], sheet_names[1], y2 + 1, y1 + 1)
					if found == 0:
						# 빈칸을 하나 넣는다
						self.insert_yline(sheet_names[1], y1 + 1)

	def set_cell_color(self, sheet_name, xy, input_color="입력필요"):
		self.paint_color_in_cell(sheet_name, xy, input_color)

	def paint_color_in_cell(self, sheet_name, xy, input_color="입력필요"):
		"""
		paint_color(sheet_name, xyxy, input_data="입력필요")
		선택 셀에 색깔을 넣는다
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		self.check_address_value(xy)

		rgbvalue = self.color.change_scolor_to_rgb(input_color)
		rgb_to_int = (int(rgbvalue[2])) * (256 ** 2) + (int(rgbvalue[1])) * 256 + int(rgbvalue[0])
		sheet_object.Cells(xy[0], xy[1]).Interior.Color = int(rgb_to_int)

	def paint_rgbcolor_in_cell(self, sheet_name, xy, input_color="입력필요"):
		"""
		paint_color(sheet_name, xyxy, input_data="입력필요")
		선택 셀에 색깔을 넣는다
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		self.check_address_value(xy)

		rgb_to_int = (int(input_color[2])) * (256 ** 2) + (int(input_color[1])) * 256 + int(input_color[0])
		sheet_object.Cells(xy[0], xy[1]).Interior.Color = int(rgb_to_int)

	def paint_color_in_cell_as_emptycell(self, sheet_name="", xyxy=""):
		"""
		빈셀의 갯수를 계산
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet_object.Range(sheet_object.Cells(x1, y1), sheet_object.Cells(x2, y2))
		temp_result = 0
		for x in range(x1, x2 + 1):
			for y in range(y1, y2 + 1):
				cell_value = sheet_object.Cells(x, y).Value
				if cell_value == None:
					self.paint_color_in_cell(sheet_name, [x, y], 16)
					temp_result = temp_result + 1
		return temp_result

	def paint_color_in_sheet_tab(self, sheet_name, input_color="입력필요"):
		"""
		시트탭의색을 넣는것
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		rgbvalue = self.color.change_scolor_to_rgb(input_color)
		rgb_to_int = (int(rgbvalue[2])) * (256 ** 2) + (int(rgbvalue[1])) * 256 + int(rgbvalue[0])
		sheet_object.Tab.Color = rgb_to_int

	def paint_color_in_range(self, sheet_name, xyxy, input_color="입력필요"):
		"""
		paint_color(sheet_name, xyxy, input_data="입력필요")
		선택 셀에 색깔을 넣는다
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet_object.Range(sheet_object.Cells(x1, y1), sheet_object.Cells(x2, y2))

		rgbvalue = self.color.change_scolor_to_rgb(input_color)
		rgb_to_int = (int(rgbvalue[2])) * (256 ** 2) + (int(rgbvalue[1])) * 256 + int(rgbvalue[0])
		my_range.Interior.Color = rgb_to_int

	def paint_color_in_range_as_samevalue_by_excelcolorno(self, sheet_name="", xyxy="", excelcolorno=4):
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet_object.Range(sheet_object.Cells(x1, y1), sheet_object.Cells(x2, y2))
		set_a = set([])
		for x in range(x1, x2 + 1):
			for y in range(y1, y2 + 1):
				value = str(sheet_object.Cells(x, y).Value)
				if value == "" or value == None:
					pass
				else:
					len_old = len(set_a)
					set_a.add(value)
					len_new = len(set_a)
					if len_old == len_new:
						self.paint_color_in_cell(sheet_name, [x, y], excelcolorno)

	def paint_color_in_range_bywords(self, sheet_name="", xyxy=""):
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)

		bbb = self.input_messagebox_value("Please input text : in, to, his, with")
		basic_list = []
		for one_data in bbb.split(","):
			basic_list.append(one_data.strip())
		total_no = len(basic_list)
		for x in range(x1, x2 + 1):
			for y in range(y1, y2 + 1):
				cell_value = str(sheet_object.Cells(x, y).Value)
				temp_int = 0
				for one_word in basic_list:
					if re.match('(.*)' + one_word + '(.*)', cell_value):
						temp_int = temp_int + 1
				if temp_int == total_no:
					self.paint_color_in_range(sheet_name, [x, y], 4)

	def paint_color_in_range_in_maxvalue_in_each_xline(self, sheet_name="", xyxy=""):
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)

		all_data = self.write_value_in_range(sheet_name, [x1, y1, x2, y2])
		if not (x1 == x2 and y1 == y2):
			for line_no in range(len(all_data)):
				line_data = all_data[line_no]
				filteredList = list(filter(lambda x: type(x) == type(1) or type(x) == type(1.0), line_data))
				if filteredList == []:
					pass
				else:
					max_value = max(filteredList)
					x_location = x1 + line_no
					for no in range(len(line_data)):
						y_location = y1 + no
						if (line_data[no]) == max_value:
							self.paint_color_in_cell(sheet_name, [x_location, y_location], 16)
		else:
			print("Please re-check selection area")

	def paint_color_in_range_in_samevalue(self, sheet_name="", xyxy="", input_color="gray"):
		"""
		paint_range_samevalue(sheet_name="", xyxy="")
		선택한 영역에서 2번이상 반복된것만 색칠하기
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)

		set_a = set([])
		for x in range(x1, x2 + 1):
			for y in range(y1, y2 + 1):
				value = str(sheet_object.Cells(x, y).Value)
				if value == "" or value == None:
					pass
				else:
					len_old = len(set_a)
					set_a.add(value)
					len_new = len(set_a)
					if len_old == len_new:
						self.paint_color_in_cell(sheet_name, [x, y], input_color)

	def paint_color_in_range_in_spacecell(self, sheet_name="", xyxy="", input_color="입력필요"):
		"""
		빈셀처럼 보이는데 space문자가 들어가 있는것 찾기
		선택한 영역의 셀을 하나씩 읽어와서 re모듈을 이용해서 공백만 있는지 확인한다
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet_object.Range(sheet_object.Cells(x1, y1), sheet_object.Cells(x2, y2))
		for x in range(x1, x2 + 1):
			for y in range(y1, y2 + 1):
				cell_value = str(sheet_object.Cells(x, y).Value)
				com = re.compile("^\s+")
				if cell_value != None:
					if com.search(cell_value):
						self.paint_color_in_cell(sheet_name, [x, y], input_color)

	def paint_color_in_range_in_specific_text(self, sheet_name="", xyxy="", input_list="입력필요", input_color="입력필요"):
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet_object.Range(sheet_object.Cells(x1, y1), sheet_object.Cells(x2, y2))
		selection_range = x1, y1, x2, y2
		datas = list(self.write_value_in_range(sheet_name, selection_range))
		temp = []
		result = []
		min_value = []
		input_text = input_list
		for data_xx in datas:
			temp_list = []
			temp_num = 0
			for data_x in data_xx:
				if str(input_text) in str(data_x) and data_x != None:
					self.paint_color_in_range(sheet_name, [x1, y1 + temp_num, x1, y1 + temp_num],
					                          input_color)
				temp_num = temp_num + 1
			x1 = x1 + 1

	def paint_color_in_range_with_minvalue_in_each_xline(self, sheet_name="", xyxy=""):
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet_object.Range(sheet_object.Cells(x1, y1), sheet_object.Cells(x2, y2))
		all_data = self.write_value_in_range(sheet_name, [x1, y1, x2, y2])
		if not (x1 == x2 and y1 == y2):
			for line_no in range(len(all_data)):
				line_data = all_data[line_no]
				filteredList = list(filter(lambda x: type(x) == type(1) or type(x) == type(1.0), line_data))
				if filteredList == []:
					pass
				else:
					max_value = min(filteredList)
					x_location = x1 + line_no
					for no in range(len(line_data)):
						y_location = y1 + no
						if (line_data[no]) == max_value:
							self.paint_color_in_cell(sheet_name, [x_location, y_location], 3)
		else:
			print("Please re-check selection area")

	def paint_fontcolor_in_cell_byrgb(self, sheet_name="", xyxy="", rgb=""):
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet_object.Range(sheet_object.Cells(x1, y1), sheet_object.Cells(x2, y2))
		my_range.Font.Color = int(rgb[0]) + int(rgb[1]) * 256 + int(rgb[2]) * 65536

	def paint_fontcolor_in_range(self, sheet_name="", xyxy="", font_color=""):
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet_object.Range(sheet_object.Cells(x1, y1), sheet_object.Cells(x2, y2))

		input_data = self.color.change_scolor_to_rgb(font_color)
		rgb_to_int = (int(input_data[2])) * (256 ** 2) + (int(input_data[1])) * 256 + int(input_data[0])
		my_range.Font.Color = rgb_to_int

	def paint_rgbcolor_in_range(self, sheet_name="", xyxy="", input_data=""):
		"""
		영역에 색깔을 입힌다
		엑셀에서의 색깔의 번호는 아래의 공식처럼 만들어 진다
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet_object.Range(sheet_object.Cells(x1, y1), sheet_object.Cells(x2, y2))

		rgb_to_int = (int(input_data[2])) * (256 ** 2) + (int(input_data[1])) * 256 + int(input_data[0])
		my_range.Interior.Color = rgb_to_int

	def paint_textcolor_in_range(self, sheet_name="", xyxy="", input_color="입력필요"):
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet_object.Range(sheet_object.Cells(x1, y1), sheet_object.Cells(x2, y2))

		rgbvalue = self.color.change_scolor_to_rgb(input_color)
		rgb_to_int = (int(rgbvalue[2])) * (256 ** 2) + (int(rgbvalue[1])) * 256 + int(rgbvalue[0])
		my_range.Font.Color = rgb_to_int

	def paste_range(self, sheet_name="", xyxy=""):
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		sheet_object.Cells(x1, y1).Select()
		sheet_object.Paste()

	def pick_unique_value_in_range(self, xyxy):
		"""
		선택한 자료중에서 고유한 자료만을 골라내는 것이다
		1. 관련 자료를 읽어온다
		2. 자료중에서 고유한것을 찾아낸다
		3. 선택영역에 다시 쓴다
		"""
		sheet_object = self.check_sheet_name("")
		x1, y1, x2, y2 = self.check_address_value(xyxy)

		temp_datas = self.write_value_in_range("", xyxy)
		temp_result = []
		for one_list_data in temp_datas:
			for one_data in one_list_data:
				if one_data in temp_result or type(one_data) == type(None):
					pass
				else:
					temp_result.append(one_data)
		self.delete_value_in_range("", xyxy)
		for num in range(len(temp_result)):
			mox, namuji = divmod(num, x2 - x1 + 1)
			sheet_object.Cells(x1 + namuji, y1 + mox).Value = temp_result[num]

	def print_page(self, sheet_name, **var_dic):
		sheet_object = self.check_sheet_name(sheet_name)
		sheet_object.PageSetup.Zoom = False
		sheet_object.PageSetup.FitToPagesTall = 1
		sheet_object.PageSetup.FitToPagesWide = 1
		# sheet_object.PageSetup.PrintArea = print_area
		sheet_object.PageSetup.LeftMargin = 25
		sheet_object.PageSetup.RightMargin = 25
		sheet_object.PageSetup.TopMargin = 50
		sheet_object.PageSetup.BottomMargin = 50
		# sheet_object.ExportAsFixedFormat(0, path_to_pdf)
		sheet_object.PageSetup.LeftFooter = "&D"  # 날짜
		sheet_object.PageSetup.LeftHeader = "&T"  # 시간
		sheet_object.PageSetup.CenterHeader = "&F"  # 화일명
		sheet_object.PageSetup.CenterFooter = "&P/&N"  # 현 page/ 총 page
		sheet_object.PageSetup.RightHeader = "&Z"  # 화일 경로
		sheet_object.PageSetup.RightFooter = "&P+33"  # 현재 페이지 + 33

	def print_preview(self, sheet_name=""):
		sheet_object = self.check_sheet_name(sheet_name)
		sheet_object.PrintPreview()

	def read_activesheet_name(self):
		sheet_name = self.xlapp.ActiveSheet.Name
		return sheet_name

	def read_address_in_currentregion(self, sheet_name="", xy=""):
		"""
		이것은 현재의 셀에서 공백과 공백열로 둘러싸인 활성셀영역을 돌려준다
		"""
		result = self.check_address_value(self.xlapp.ActiveCell.CurrentRegion.Address)
		return result

	def read_address_in_activecell(self, sheet_name="", xy=""):
		result = self.check_address_value(self.xlapp.ActiveCell.Address)
		return result

	def read_address_in_selection(self):
		"""
		현재선택된 영역의 주소값을 돌려준다
		"""
		result = ""
		temp_address = self.xlapp.Selection.Address
		temp_list = temp_address.split(",")
		if len(temp_list) == 1:
			result = self.check_address_value(temp_address)
		if len(temp_list) > 1:
			result = []
			for one_address in temp_list:
				result.append(self.check_address_value(one_address))
		return result

	def read_all_property_in_cell(self, sheet_name="", xy=[7, 7]):
		basic_cell = basic_data.basic_cell_class()
		sheet_object = self.check_sheet_name(sheet_name)
		one_cell = sheet_object.Cells(xy[0], xy[1])
		result = basic_cell.values
		y = result["y"] = xy[0]
		x = result["x"] = xy[1]
		result["value"] = one_cell.Value
		result["value2"] = one_cell.Value2
		result["formular"] = one_cell.Formula
		result["formularr1c1"] = one_cell.FormulaR1C1
		result["text"] = one_cell.Text
		if result["value"] != "" and result["value"] != None:
			# 값이 없으면 font에 대한 것을 읽지 않는다
			result["font_dic"]["background"] = one_cell.Font.Background
			result["font_dic"]["bold"] = one_cell.Font.Bold
			result["font_dic"]["color"] = one_cell.Font.Color
			result["font_dic"]["colorindex"] = one_cell.Font.ColorIndex
			# result["font_dic"]["creator"] = one_cell.Font.Creator
			result["font_dic"]["style"] = one_cell.Font.FontStyle
			result["font_dic"]["italic"] = one_cell.Font.Italic
			result["font_dic"]["name"] = one_cell.Font.Name
			result["font_dic"]["size"] = one_cell.Font.Size
			result["font_dic"]["strikethrough"] = one_cell.Font.Strikethrough
			result["font_dic"]["subscript"] = one_cell.Font.Subscript
			result["font_dic"]["superscript"] = one_cell.Font.Superscript
			# result["font_dic"]["themecolor"] = one_cell.Font.ThemeColor
			# result["font_dic"]["themefont"] = one_cell.Font.ThemeFont
			# result["font_dic"]["tintandshade"] = one_cell.Font.TintAndShade
			result["font_dic"]["underline"] = one_cell.Font.Underline
		try:
			result["memo"] = one_cell.Comment.Text()
		except:
			result["memo"] = ""
		result["background_color"] = one_cell.Interior.Color
		result["background_colorindex"] = one_cell.Interior.ColorIndex
		result["numberformat"] = one_cell.NumberFormat
		if one_cell.Borders.LineStyle != -4142:
			if one_cell.Borders(7).LineStyle != -4142:
				# linestyle이 없으면 라인이 없는것으로 생각하고 나머지를 확인하지 않으면서 시간을 줄이는 것이다
				result["line_top_dic"]["style"] = one_cell.Borders(7).LineStyle
				result["line_top_dic"]["color"] = one_cell.Borders(7).Color
				result["line_top_dic"]["colorindex"] = one_cell.Borders(7).ColorIndex
				result["line_top_dic"]["thick"] = one_cell.Borders(7).Weight
				result["line_top_dic"]["tintandshade"] = one_cell.Borders(7).TintAndShade
			if one_cell.Borders(8).LineStyle != -4142:
				result["line_bottom_dic"]["style"] = one_cell.Borders(8).LineStyle
				result["line_bottom_dic"]["color"] = one_cell.Borders(8).Color
				result["line_bottom_dic"]["colorindex"] = one_cell.Borders(8).ColorIndex
				result["line_bottom_dic"]["thick"] = one_cell.Borders(8).Weight
				result["line_bottom_dic"]["tintandshade"] = one_cell.Borders(8).TintAndShade
			if one_cell.Borders(9).LineStyle != -4142:
				result["line_left_dic"]["style"] = one_cell.Borders(9).LineStyle
				result["line_left_dic"]["color"] = one_cell.Borders(9).Color
				result["line_left_dic"]["colorindex"] = one_cell.Borders(9).ColorIndex
				result["line_left_dic"]["thick"] = one_cell.Borders(9).Weight
				result["line_left_dic"]["tintandshade"] = one_cell.Borders(9).TintAndShade
			if one_cell.Borders(10).LineStyle != -4142:
				result["line_right_dic"]["style"] = one_cell.Borders(10).LineStyle
				result["line_right_dic"]["color"] = one_cell.Borders(10).Color
				result["line_right_dic"]["colorindex"] = one_cell.Borders(10).ColorIndex
				result["line_right_dic"]["thick"] = one_cell.Borders(10).Weight
				result["line_right_dic"]["tintandshade"] = one_cell.Borders(10).TintAndShade
			if one_cell.Borders(11).LineStyle != -4142:
				result["line_x1_dic"]["style"] = one_cell.Borders(11).LineStyle
				result["line_x1_dic"]["color"] = one_cell.Borders(11).Color
				result["line_x1_dic"]["colorindex"] = one_cell.Borders(11).ColorIndex
				result["line_x1_dic"]["thick"] = one_cell.Borders(11).Weight
				result["line_x1_dic"]["tintandshade"] = one_cell.Borders(11).TintAndShade
			if one_cell.Borders(12).LineStyle != -4142:
				result["line_x2_dic"]["style"] = one_cell.Borders(12).LineStyle
				result["line_x2_dic"]["color"] = one_cell.Borders(12).Color
				result["line_x2_dic"]["colorindex"] = one_cell.Borders(12).ColorIndex
				result["line_x2_dic"]["thick"] = one_cell.Borders(12).Weight
				result["line_x2_dic"]["tintandshade"] = one_cell.Borders(12).TintAndShade
		return result

	def read_color_in_cell(self, sheet_name="", xyxy=""):
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet_object.Range(sheet_object.Cells(x1, y1), sheet_object.Cells(x2, y2))

		result = my_range.Interior.Color
		return result

	def read_coord_in_cell(self, sheet_name, xyxy):
		"""
		셀의 픽셀 좌표를 갖고온다
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet_object.Range(sheet_object.Cells(x1, y1), sheet_object.Cells(x2, y2))

		rng_x_coord = my_range.Left
		rng_y_coord = my_range.Top
		rng_width = my_range.Width
		rng_height = my_range.Height
		return [rng_x_coord, rng_y_coord, rng_width, rng_height]

	def read_general_value(self):
		"""
		몇가지 엑셀에서 자주사용하는 것들정의
		엑셀의 사용자, 현재의 경로, 화일이름, 현재시트의 이름
		"""
		result = []
		result.append(self.xlapp.ActiveWorkbook.Name)
		result.append(self.xlapp.Username)
		result.append(self.xlapp.ActiveWorkbook.ActiveSheet.Name)
		return result

	def read_inputbox_value(self, title="Please Input Value"):
		result = self.xlapp.Application.InputBox(title)
		return result

	def read_memo_in_cell(self, sheet_name="", xyxy=""):
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet_object.Range(sheet_object.Cells(x1, y1), sheet_object.Cells(x2, y2))

		result = my_range.Comment.Text()
		return result

	def read_rangename_address(self, sheet_name="", range_name="입력필요"):
		sheet_object = self.check_sheet_name(sheet_name)
		temp = sheet_object.Range(range_name).Address
		result = self.check_address_value(temp)
		return result

	def read_rangename_all(self):
		names_count = self.xlbook.Names.Count
		result = []
		if names_count > 0:
			for aaa in range(1, names_count + 1):
				name_name = self.xlbook.Names(aaa).Name
				name_range = self.xlbook.Names(aaa)
				result.append([aaa, str(name_name), str(name_range)])
		return result

	def read_shape_in_sheet_name_by_no(self, sheet_name="", shape_no="입력필요"):
		sheet_object = self.check_sheet_name(sheet_name)
		result = sheet_object.Shapes(shape_no).Name
		return result

	def read_usedrange_address(self, sheet_name=""):
		sheet_object = self.check_sheet_name(sheet_name)
		result = self.check_address_value(sheet_object.UsedRange.address)
		return result

	def read_username(self):
		result = self.xlapp.Username
		return result

	def read_value_in_activecell(self):
		result = [self.xlapp.ActiveCell.Row, self.xlapp.ActiveCell.Column, self.xlapp.ActiveCell.Value]
		return result

	def read_cell_value(self, sheet_name="", xyxy=""):
		self.read_value_in_cell(sheet_name, xyxy)

	def read_value_in_cell(self, sheet_name="", xyxy=""):
		"""
		# 값을 일정한 영역에서 갖고온다
		만약 영역을 두개만 주면 처음과 끝의 영역을 받은것으로 간주해서 알아서 처리하도록 변경하였다
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		result = sheet_object.Cells(x1, y1).Value

		if type(result) == type(123):
			result = int(result)
		elif result == None:
			result = ""
		return result

	def read_value_in_continous_range(self, sheet_name="", xyxy=""):
		"""
		# 현재선택된 셀을 기준으로 연속된 영역을 가지고 오는 것입니다
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		row = xyxy
		col = xyxy
		sheet_object = self.check_sheet_name(sheet_name)
		bottom = row  # 아래의 행을 찾는다
		while sheet_object.Cells(bottom + 1, col).Value not in [None, '']:
			bottom = bottom + 1
		right = col  # 오른쪽 열
		while sheet_object.Cells(row, right + 1).Value not in [None, '']:
			right = right + 1
		return sheet_object.Range(sheet_object.Cells(row, col), sheet_object.Cells(bottom, right)).Value

	def read_value_in_range(self, sheet_name, xyxy):
		"""
		# 값을 일정한 영역에서 갖고온다
		만약 영역을 두개만 주면 처음과 끝의 영역을 받은것으로 간주해서 알아서 처리하도록 변경하였다
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet_object.Range(sheet_object.Cells(x1, y1), sheet_object.Cells(x2, y2))
		if x1 == -1:
			return sheet_object.Range(x1, y1).Value
		return my_range.Value

	def read_value_in_selection(self, sheet_name="", xyxy=""):
		"""
		값을 일정한 영역에서 갖고온다
		만약 영역을 두개만 주면 처음과 끝의 영역을 받은것으로 간주해서 알아서 처리하도록 변경하였다
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet_object.Range(sheet_object.Cells(x1, y1), sheet_object.Cells(x2, y2))
		self.get_activesheet_object()
		self.check_address_value(self.xlapp.Selection.Address)
		result = my_range.Value
		return result

	def read_value_in_xxline(self, sheet_name="", xx="입력필요"):
		sheet_object = self.check_sheet_name(sheet_name)
		return sheet_object.Range(sheet_object.Cells(xx[0], 1), sheet_object.Cells(xx[1], 1)).EntireRow.Value

	def read_value_in_yyline(self, sheet_name="", yy="입력필요"):
		sheet_object = self.check_sheet_name(sheet_name)
		return sheet_object.Range(sheet_object.Cells(1, yy[0]), sheet_object.Cells(1, yy[1])).EntireColumn.Value

	def read_workbook_fullname(self):
		return self.xlbook.FullName

	def read_workbook_name(self):
		return self.xlbook.Name

	def read_workbook_path(self):
		return self.xlbook.Path

	def read_workbook_username(self):
		return self.xlapp.Username

	def read_worksheet_count(self):
		return self.xlbook.Worksheets.Count

	def read_sheet_name_all(self):
		result = []
		for a in range(1, self.xlbook.Worksheets.Count + 1):
			result.append(self.xlbook.Worksheets(a).Name)
		return result

	def read_worksheet_numbers(self):
		return self.xlbook.Worksheets.Count

	def remove_vba_module(self, module_name_list):
		"""
		입력형태 : 리스트형, 메크로 모듈이름
		역활 : 열려있는 화일안에서 입력리스트의 메크로를 삭제를 하는 것
		"""
		for module_name in module_name_list:
			xlmodule = self.xlbook.VBProject.VBComponents(module_name)
			self.xlbook.VBProject.VBComponents.Remove(xlmodule)

	def read_selection_address(self):
		"""
		영문으로 되어있는 주소를 아라비아숫자로 변경하는 것이다
		예전이름 : def address_all (self, input_datas)
		"""
		input_datas = str(self.xlapp.Selection.Address)
		input_datas = str(input_datas).lower()
		arange = str(input_datas).replace("$", "").split(":")
		if len(arange) == 1:    arange.append(arange[0])
		if str(arange[0]).lower() in string.ascii_lowercase and str(arange[1]).lower() in string.ascii_lowercase:
			arange[0] = arange[0] + "0"
			arange[1] = arange[1] + "65536"
		if str(arange[0]).lower() in string.digits and str(arange[1]).lower() in string.digits:
			arange[0] = "a" + arange[0]
			arange[1] = "iv" + arange[1]
		result = []
		for a in arange:
			if str(a[0]).lower() in string.ascii_lowercase and str(a[1]).lower() in string.ascii_lowercase:
				result.append(a[0:2])
				result.append(a[2:])
			else:
				result.append(a[0])
				result.append(a[1:])
		if result[0]:
			if len(result[0]) == 1:
				result[0] = (string.ascii_lowercase.index(result[0]) + 1)
			else:
				aaa = (string.ascii_lowercase.index(result[0][0]) + 1) * 26
				result[0] = aaa + (string.ascii_lowercase.index(result[0][1]) + 1)
		if result[2]:
			if len(result[2]) == 1:
				result[2] = (string.ascii_lowercase.index(result[2]) + 1)
			else:
				aaa = (string.ascii_lowercase.index(result[2][0]) + 1) * 26
				result[2] = aaa + (string.ascii_lowercase.index(result[2][1]) + 1)
		final_data = [int(result[1]), int(result[0]), int(result[3]), int(result[2])]  # 2005-02-17 추가
		return final_data

	def remove_emptyvalue(self, sheet_name="", xyxy="", condition=[None, ""]):
		"""
		이상하게 이것을 다시 설정하지 않으면 에러가 난다
		"""
		condition = [None, ""]
		values = self.read_value_in_range(sheet_name, xyxy)
		time.sleep(2)
		self.delete_value_in_range(sheet_name, xyxy)
		values_checked = self.yt.delete_emptyvalue_in_list(values, condition)
		self.write_value_in_range(sheet_name, xyxy, values_checked)

	def replace_word_many_in_range(self, sheet_name="", xyxy="", input_list="입력필요"):
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)

		for y in range(y1, y2 + 1):
			for x in range(x1, x2 + 1):
				cell_value = str(self.read_cell_value(sheet_name, [x, y]))
				for one_list in input_list:
					cell_value = cell_value.replace(one_list[0], one_list[1])
				self.write_cell_value(sheet_name, [y, x + 1], cell_value)

	def resize_list(self, xy_list, resize=[1, 1]):
		result = []
		# 자료의 x갯수를 요청한것과 비교
		if len(xy_list) < resize[0] or resize[0] == 0:
			pass
		else:
			xy_list = xy_list[:resize[0]]
		# 자료의 y갯수를 요청한것과 비교
		for x_list in xy_list:
			if len(x_list) < resize[1] or resize[1] == 0:
				pass
			else:
				x_list = xy_list[:resize[0]]
			result.append(x_list)
		return result

	def run_vba_module(self, vba_code, macro_name):
		"""
		텍스트로 만든 매크로 코드를 실행하는 코드이다
		"""
		new_vba_code = "Sub " + macro_name + "()" + vba_code + " End Sub"
		mod = self.xlbook.VBProject.VBComponents.Add(1)
		mod.CodeModule.AddFromString(new_vba_code)
		self.xlapp.Run(macro_name)

	def save(self, newfilename):
		if newfilename == "":
			self.xlbook.Save()
		else:
			self.xlbook.SaveAs(newfilename)

	def screen_update_off(self):
		self.xlapp.ScreenUpdating = False

	def screen_update_on(self):
		self.xlapp.ScreenUpdating = True

	def select_range(self, sheet_name="", xyxy=""):
		"""
		영역을 선택한다
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet_object.Range(sheet_object.Cells(x1, y1), sheet_object.Cells(x2, y2))
		my_range.Select()

	def select_sheet(self, sheet_name=""):
		"""
		현재의 엑셀중에서 활성화된 시트의 이름을 돌려준다
		"""
		if sheet_name == None or sheet_name == "":
			self.show_messagebox_value("시트이름을 다시한번 확인 해 주십시요")
		elif sheet_name in self.read_sheet_name_all():
			self.xlbook.Worksheets(sheet_name).Select()

	def select_top_in_range(self, sheet_name="", xyxy=""):
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		sheet_object.Cells(x1, y1).End(- 4162).Select()

	def set_autofit_in_range(self, sheet_name="", xyxy="all"):
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		new_y1 = self.change_num_to_char(y1)
		new_y2 = self.change_num_to_char(y2)
		if xyxy == "" or xyxy == "all":
			sheet_object.EntireColumn.AutoFit()
		else:
			sheet_object.Columns(str(new_y1) + ':' + str(new_y2)).AutoFit()

	def set_bold_in_range(self, sheet_name="", xyxy=""):
		"""
		영역안의 글씨체를 진하게 만든다
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet_object.Range(sheet_object.Cells(x1, y1), sheet_object.Cells(x2, y2))
		my_range.Font.Bold = True

	def set_conditional_in_range(self):
		sheet_object = self.check_sheet_name("")
		my_range = sheet_object.Range(sheet_object.Cells(1, 1), sheet_object.Cells(20, 20))
		formula1 = ' = IF($A1 = "", TRUE, FALSE)'
		# win32com.client.constants.xlCellValue = > 1
		# win32com.client.constants.xlGreaterEqual = > 7
		my_range.FormatConditions.Add(1, 7, formula1)
		my_range.FormatConditions(my_range.FormatConditions.Count).SetFirstPriority()
		my_range.FormatConditions(1).Font.Bold = True
		my_range.FormatConditions(1).Font.Strikethrough = False
		my_range.FormatConditions(1).Font.TintAndShade = 0
		my_range.FormatConditions(1).Interior.PatternColorIndex = 1
		my_range.FormatConditions(1).Interior.Color = 5296274
		my_range.FormatConditions(1).Interior.TintAndShade = 0
		my_range.FormatConditions(1).StopIfTrue = False

	def set_font_in_range(self, sheet_name="", xyxy="", font="입력필요"):
		"""
		영역에 글씨체를 설정한다
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet_object.Range(sheet_object.Cells(x1, y1), sheet_object.Cells(x2, y2))
		my_range.Font.Name = font

	def set_fontcolor_in_range(self, sheet_name="", xyxy="", font_name=""):
		"""
		영역에 글씨체를 설정한다
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet_object.Range(sheet_object.Cells(x1, y1), sheet_object.Cells(x2, y2))
		my_range.Font.Color = font_name

	def set_fontsize_in_range(self, sheet_name="", xyxy="", size="입력필요"):
		"""
		영역에 글씨크기를 설정한다
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet_object.Range(sheet_object.Cells(x1, y1), sheet_object.Cells(x2, y2))
		my_range.Font.Size = int(size)

	def set_formula_in_range(self, sheet_name="", xyxy="", input_data=" = Now()"):
		"""
		set_range_formula(sheet_name="", xyxy="", input_data="=Now()")
		영역에 수식을 넣는것
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet_object.Range(sheet_object.Cells(x1, y1), sheet_object.Cells(x2, y2))
		my_range.Formula = input_data

	def set_fullscreen(self, fullscreen=1):
		"""
		전체화면으로 보기
		"""
		self.xlapp.DisplayFullScreen = fullscreen

	def set_gridline_off(self):
		self.xlapp.ActiveWindow.DisplayGridlines = 0

	def set_gridline_on(self):
		self.xlapp.ActiveWindow.DisplayGridlines = 1

	def set_gridline_onoff(self):
		if self.xlapp.ActiveWindow.DisplayGridlines == 0:
			self.xlapp.ActiveWindow.DisplayGridlines = 1
		else:
			self.xlapp.ActiveWindow.DisplayGridlines = 0

	def set_height_in_xxline(self, sheet_name, xx, height=13.5):
		"""
		가로줄의 높이를 설정
		"""
		my_range = self.check_xx_address(sheet_name, xx)
		my_range.RowHeight = height

	def set_merge_in_range(self, sheet_name="", xyxy=""):
		"""
		셀들을 병합하는 것
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet_object.Range(sheet_object.Cells(x1, y1), sheet_object.Cells(x2, y2))
		my_range.Merge(0)

	def set_numberformat_in_cell(self, type="general", number=0):
		"""
		셀의 숫자에대한 형식을 설정
		"""
		if type == 'general':
			format = "#,##0.00_ "
		elif type == 'number':
			format = "US$#,##0.00"
		elif type == 'account':
			format = "_-""US$""* #,##0.00_ ;_-""US$""* -#,##0.00 ;_-""US$""* ""-""??_ ;_-@_ "
		elif type == 'date':
			format = "mm""/""dd""/""yy"
		elif type == 'datetime':
			format = "yyyy""-""m""-""d h:mm AM/PM"
		elif type == 'percent':
			format = "0.00%"
		elif type == 'bunsu':
			format = "# ?/?"
		elif type == 'jisu':
			format = "0.00E+00"
		elif type == 'text':
			format = "@"
		elif type == 'etc':
			format = "000-000"
		elif type == 'other':
			format = "$#,##0.00_);[빨강]($#,##0.00)"
		range.NumberFormatLocal = format

	def set_numberformat_in_range(self, sheet_name="", xyxy="", numberformat="입력필요"):
		"""
		영역에 숫자형식을 지정하는 것
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet_object.Range(sheet_object.Cells(x1, y1), sheet_object.Cells(x2, y2))
		my_range.NumberFormat = numberformat

	def set_numberproperty_in_range(self, sheet_name="", xyxy="", type1="입력필요"):
		if type1 == 'general':
			result = "#,##0.00_ "
		elif type1 == 'number':
			result = "US$""#,##0.00"
		elif type1 == 'account':
			result = "_-""US$""* #,##0.00_ ;_-""US$""* -#,##0.00 ;_-""US$""* ""-""??_ ;_-@_ "
		elif type1 == 'date':
			result = "mm""/""dd""/""xx"
		elif type1 == 'datetime':
			result = "xxxx""-""m""-""d h:mm AM/PM"
		elif type1 == 'percent':
			result = "0.00%"
		elif type1 == 'bunsu':
			result = "# ?/?"
		elif type1 == 'jisu':
			result = "0.00E+00"
		elif type1 == 'text':
			result = "@"
		elif type1 == 'etc':
			result = "000-000"
		elif type1 == 'other':
			result = "$#,##0.00_);[빨강]($#,##0.00)"
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet_object.Range(sheet_object.Cells(x1, y1), sheet_object.Cells(x2, y2))
		my_range.NumberFormat = result

	def set_picture_in_cell(self, sheet_name, xy, full_path):
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xy)
		sheet_object.Cells(x1, y1).Select()
		aaa = sheet_object.Pictures
		aaa.Insert(full_path).Select()

	def set_print_page(self, sheet_name="", **var_dic):
		sheet_object = self.check_sheet_name(sheet_name)
		sheet_object.PageSetup.Zoom = False
		sheet_object.PageSetup.FitToPagesTall = 1
		sheet_object.PageSetup.FitToPagesWide = 1
		# sheet_object.PageSetup.PrintArea = print_area
		sheet_object.PageSetup.LeftMargin = 25
		sheet_object.PageSetup.RightMargin = 25
		sheet_object.PageSetup.TopMargin = 50
		sheet_object.PageSetup.BottomMargin = 50
		# sheet_object.ExportAsFixedFormat(0, path_to_pdf)
		sheet_object.PageSetup.LeftFooter = "&D"  # 날짜
		sheet_object.PageSetup.LeftHeader = "&T"  # 시간
		sheet_object.PageSetup.CenterHeader = "&F"  # 화일명
		sheet_object.PageSetup.CenterFooter = "&P/&N"  # 현 page/ 총 page
		sheet_object.PageSetup.RightHeader = "&Z"  # 화일 경로
		sheet_object.PageSetup.RightFooter = "&P+33"  # 현재 페이지 + 33

	def set_rangename(self, sheet_name="", xyxy="", name=""):
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet_object.Range(sheet_object.Cells(x1, y1), sheet_object.Cells(x2, y2))
		self.xlbook.Names.Add(name, my_range)

	def set_sheet_visible(self, input_data=0):
		self.xlapp.Visible = input_data

	def set_unmerge_in_range(self, sheet_name="", xyxy=""):
		"""
		영역안의 병합된 것을 푸는 것이다
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet_object.Range(sheet_object.Cells(x1, y1), sheet_object.Cells(x2, y2))
		my_range.UnMerge()

	def set_workbook_close(self):
		"""
		현재는 close를 시키면 엑셀워크북만이 아니라 엑셀자체도 종료 시킵니다
		"""
		self.xlbook.Close(SaveChanges=0)
		del self.xlapp

	def set_workbook_fullscreen(self, fullscreen=1):
		self.xlapp.DisplayFullScreen = fullscreen

	def set_workbook_visible(self, value=1):
		"""
		실행되어있는 엑셀을 화면에 보이지 않도록 설정합니다
		기본설정은 보이는 것으로 되너 있읍니다
		"""
		self.xlapp.Visible = value

	def set_wrap_in_range(self, sheet_name="", xyxy="", input_data=""):
		"""
		셀의 줄바꿈을 설정할때 사용한다
		만약 status를 false로 하면 줄바꿈이 실행되지 않는다.
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		sheet_object.Range(xyxy).WrapText = input_data

	def show_messagebox_value(self, input_text="입력필요", input_title="pcell"):
		"""
		메세지박스를 보여주는것
		"""
		win32gui.MessageBox(0, input_text, input_title, 0)

	def split_value_to_special_string(self, sheet_name="", input_text="입력필요"):
		"""
		split_inputvalue_as_special_string( input_text="입력필요"):
		선택한 1줄의 영역에서 원하는 문자나 글자를 기준으로 분리할때
		2개의 세로행을 추가해서 결과값을 쓴다
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		rng_select = self.read_address_in_selection()
		rng_used = self.read_usedrange_address()
		[x1, y1, x2, y2] = self.intersect_range1_range2(rng_select, rng_used)
		self.insert_xline("", x1 + 1)
		self.insert_xline("", x1 + 1)
		result = []
		length = 2
		# 자료를 분리하여 리스트에 집어 넣는다
		for x in range(x1, x2 + 1):
			for y in range(y1, y2 + 1):
				cell_value = str(sheet_object.Cells(x, y).Value)
				list_data = cell_value.split(input_text)
				result.append(list_data)
		# 집어넣은 자료를 다시 새로운 세로줄에 넣는다
		for y_no in range(len(result)):
			if len(result[x_no]) > length:
				for a in range(len(result[x_no]) - length):
					self.insert_xline("", x1 + length)
				length = len(result[x_no])
			for x_no in range(len(result[x_no])):
				sheet_object.Cells(x1 + x_no, y1 + y_no + 1).Value = result[x_no][y_no]

	def split_value_to_str_num(self, input_text):
		re_com_num = re.compile("[a-zA-Z]+|\d+")
		result = re_com_num.findall(input_text)
		return result

	def swap_cap_small(self, sheet_name="", xyxy=""):
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		for y in range(y1, y2 + 1):
			for x in range(x1, x2 + 1):
				temp_data = self.read_cell_value(sheet_name, [x, y])
				self.write_cell_value(sheet_name, [x, y], string.swapcase(temp_data))

	def unlock_sheet(self, sheet_name="", password="1234"):
		sheet_object = self.check_sheet_name(sheet_name)
		sheet_object.Unprotect(password)

	def write_df_to_excel(self, sheet_name="", df_obj="입력필요", xyxy=[1, 1]):
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)

		col_list = df_obj.columns.values.tolist()
		value_list = df_obj.values.tolist()
		self.write_value_in_range(sheet_name, xyxy, [col_list])
		self.write_value_in_range(sheet_name, [x1 + 1, y1], value_list)

	def write_list1d_in_range(self, sheet_name="", xyxy="", input_list="입력필요"):
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)

		for x in range(len(input_list)):
			sheet_object.Cells(x1 + x, y1).Value = input_list[x]

	def write_list_in_range(self, sheet_name="", xyxy="", input_list="입력필요"):
		if type(input_list[0]) == type([]):
			self.write_value_in_range(sheet_name, xyxy, input_list)
		else:
			self.write_value_in_range(sheet_name, xyxy, input_list)

	def write_memo_in_cell(self, sheet_name="", xyxy="", text="입력필요"):
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet_object.Range(sheet_object.Cells(x1, y1), sheet_object.Cells(x2, y2))

		my_range.AddComment(text)

	def write_nansu_in_range(self, sheet_name="", xyxy="", input_data="입력필요"):
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)

		no_start, no_end = input_data.split(",")
		no_start = int(no_start.strip())
		no_end = int(no_end.strip())
		basic_data = list(range(no_start, no_end + 1))
		random.shuffle(basic_data)
		temp_no = 0
		for x in range(x1, x2 + 1):
			for y in range(y1, y2 + 1):
				self.write_cell_value(sheet_name, [x, y], basic_data[temp_no])
				if temp_no >= no_end - no_start:
					random.shuffle(basic_data)
					temp_no = 0
				else:
					temp_no = temp_no + 1

	def write_value_in_activecell(self, value="입력필요"):
		self.get_activesheet_object()
		x1, y1, x2, y2 = self.read_value_in_activecell()
		self.write_value_in_cell("", [x1, y1], value)

	def write_cell_value(self, sheet_name="", xyxy="", value="입력필요"):
		self.write_value_in_cell(sheet_name, xyxy, value)

	def write_value_in_cell(self, sheet_name="", xyxy="", value="입력필요"):
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)

		# 문자형식의 숫자인지를 확인하는 것
		# 숫자와 문자가 모두 숫자형으로 인식하여서 첨가해야하는 것
		if type(value) == type("abc"):
			re_com = re.compile("^[0-9.]+$")
			check_type = re_com.search(value)
			if check_type != None:
				changed_value = "'" + value
			else:
				changed_value = value
		else:
			changed_value = value
		sheet_object.Cells(x1, y1).Value = changed_value

	def write_value_in_range(self, sheet_name="", xyxy="", input_datas="입력필요"):
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		changed_input_datas = self.change_inputdata_to_list2d(input_datas)

		for x in range(0, len(changed_input_datas)):
			for y in range(0, len(changed_input_datas[x])):
				sheet_object.Cells(x + x1, y + y1).Value = changed_input_datas[x][y]

	def write_value_in_range_by_range_priority(self, sheet_name="", xyxy="", input_datas="입력필요"):
		"""
		영역이 더 우선하는 것
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		checked_datas = self.change_inputdata_to_list2d(input_datas)
		x1, y1, x2, y2 = self.check_address_value(xyxy)

		x_len = len(checked_datas)
		if (x2 - x1) <= x_len:
			x_len = x2 - x1

		y_len = len(checked_datas[0])
		if (y2 - y1) <= y_len:
			y_len = y2 - y1

		for x in range(0, x_len):
			for y in range(0, y_len):
				sheet_object.Cells(x + x1, y + y1).Value = input_datas[x][y]

	def write_value_in_range_by_trans(self, sheet_name="", xyxy="", input_list2d=""):
		"""
		입력자료의 xy를 바꿔서 입력하는 것
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet_object.Range(sheet_object.Cells(x1, y1), sheet_object.Cells(x2, y2))
		aaa = self.write_value_in_range_by_trans(input_list2d)
		for y in range(len(aaa)):
			sheet_object.Range(sheet_object.Cells(x1, y + y1), sheet_object.Cells(x2, y + y1)).Value = input_list2d[y]

	def write_value_in_range_xystep(self, sheet_name="", xyxy="", input_text="", xystep=[1, 1]):
		"""
		선택한 영역의 시작점부터 x,y 번째 셀마다 값을 넣기
		"""
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet_object.Range(sheet_object.Cells(x1, y1), sheet_object.Cells(x2, y2))

		for x in range(x1, x2 + 1):
			if divmod(x, xystep[0])[1] == 0:
				for y in range(y1, y2 + 1):
					if divmod(y, xystep[1])[1] == 0:
						sheet_object.Cells(x, y).Value = str(input_text)

	def write_value_in_range_as_speedy(self, sheet_name="", xyxy="", input_datas="입력필요"):
		sheet_object = self.check_sheet_name(sheet_name)
		x1, y1, x2, y2 = self.check_address_value(xyxy)
		my_range = sheet_object.Range(sheet_object.Cells(x1, y1), sheet_object.Cells(x2, y2))
		checked_input_datas = self.yt.change_list1d_to_list2d(input_datas)
		if y1 == y2 and x1 == x2:
			sheet_object.Range(sheet_object.Cells(x1, y1),
			                 sheet_object.Cells(y1 + len(checked_input_datas) - 1,
			                                  x1 + len(checked_input_datas[0]) - 1)).Value = checked_input_datas
		else:
			if (y2 - y1) <= len(checked_input_datas[0]) and (y2 - y1) <= len(
					checked_input_datas[0]):
				pass