# -*- coding: utf-8 -*-
import shutil
import zipfile
import os
import pickle
import time
import inspect
import pyperclip
import pyautogui
import re
import chardet
import string
import screeninfo
import sys


class youtil:
	"""
	여기저기 사용이 가능한것을 하나로 모아놓은 것이다
	"""

	def __init__(self):
		self.manual = {}

	def calc_value_text_pixel(self, input_text, target_pixel, font_name="malgun.ttf", font_size=12, fill_char=" "):
		"""
		원하는 길이만큼 텍스트를 근처의 픽셀값으로 만드는것
		원래자료에 붙이는 문자의 픽셀값
		"""
		fill_px = self.calc_pixel_size_of_text(fill_char, font_size, font_name)[0]
		total_length = 0
		for one_text in input_text:
			# 한글자씩 필셀값을 계산해서 다 더한다
			one_length = self.calc_pixel_size_of_text(fill_char, font_size, font_name)[0]
			total_length = total_length + one_length

		# 원하는 길이만큼 부족한 것을 몇번 넣을지 게산하는것
		times = round((target_pixel - total_length) / fill_px)
		result = input_text + " " * times

		# 최종적으로 넣은 텍스트의 길이를 한번더 구하는것
		length = self.calc_pixel_size_of_text(result, font_size, font_name)[0]

		# [최종변경문자, 총 길이, 몇번을 넣은건지]
		return [result, length, times]

	def chage_list1d_to_text_with_chainword(self, input_list, chain_word=" ,"):
		"""
		리스트 자료들을 중간문자를 추가하여 하나의 문자열로 만드는 것,
		“aa, bbb, ccc” 이런 식으로 만드는 방법이다
		"""
		result = ""
		for one_word in input_list:
			result = result + str(one_word) + str(chain_word)

		return result[:-len(chain_word)]

	def chain_list_withword(self, input_list, chain_word=" ,"):
		"""
		리스트 자료들을 중간에 문자를 추가하여 한줄의 문자로 만드는 것
		입력형태 : ["aa", "bb","ccc"]
		출력형태 : “aa, bbb, ccc”
		"""
		result = ""
		for one_word in input_list:
			result = result + str(one_word) + str(chain_word)
		return result[:-len(chain_word)]

	def change_df_to_list(self, df_obj):
		"""
		df자료를 커럼과 값을 기준으로 나누어서 결과를 돌려주는 것이다
		"""
		result = []
		col_list = df_obj.columns.values.tolist()
		value_list = df_obj.values.tolist()
		return [col_list, value_list]


	def change_filename(self, old_path, new_path):
		"""
		화일이름 변경
		"""
		old_path = self.check_filepath(old_path)
		new_path = self.check_filepath(new_path)
		os.rename(old_path, new_path)

	def change_folder_name(self, old_path, new_path):
		"""
		폴더이름 변경
		"""
		os.rename(old_path, new_path)

	def change_input_data_to_list2d(self, input_data):
		"""
		입렫된 자료를 2차원으로 만드는 것
		입력자료는 리스트나 듀플이어야 한다
		"""
		if type(input_data[0]) == type([]) or type(input_data[0]) == type(()):
			# 2차원의 자료이므로 입력값 그대로를 돌려준다
			result = input_data
		else:
			# 1차원의 자료라는 뜻으로, 이것을 2차원으로 만들어 주는 것이다
			result = []
			for one in input_data:
				result.append([one])
		return result

	def change_list1d_to_list2d(self, input_list):
		"""
		change_list_1d_to2d( input_list="입력필요")
		1차원의 리스트가 오면 2차원으로 만들어주는 것
		입력값중 길이가 다른 리스트를 같게 만들어 주는것
		입력형태 : 제목리스트, 2차원 값리스트형
		출력형태 : dataframe로 바꾼것
		"""
		result = []
		if len(input_list) > 0:
			if type(input_list[0]) != type([]):
				for one in input_list:
					result.append([one, ])
		return result

	def change_list2d_to_list1d(self, input_data):
		"""
		2차원의 list를 1차원으로 만들어 주는것
		항목 : ['항목1', '기본값1', '설명', {'입력형태1':'설명1', '입력형태2':'설명1',.... }]
		결과 ['항목1', '기본값1', '설명', '입력형태1:설명1', '입력형태2:설명1',.... }]
		위 형태의 자료를 한줄로 만들기위해 자료를 변경한다
		"""
		result = []
		for one_data in input_data:
			if type(one_data) == type({}):
				for key in list(one_data.Keys()):
					value = str(key) + " : " + str(one_data[key])
					result.append(value)
			elif type(one_data) == type(()) or type(one_data) == type([]) or type(one_data) == type(set()):
				for value in one_data:
					result.append(value)
			else:
				result.append(one_data)
		return result

	def change_capitalized_value(self, datas, argue=1):
		"""
		대소문자를 변경하는 것입니다
		이것은 단일 리스트만 가능하게 만들었다,  리스트안에 리스트가있는것은 불가능하다 (2004년 5월 2일 변경)
		기본은 대문자로 바꾸는 것이다
		"""
		results = []
		for data in datas:
			# print (data)
			if argue == 0: result = str(data).lower()  # 모두 소문자로
			if argue == 1: result = str(data).upper()  # 모두 대문자로
			if argue == 2: result = str(data).capitalize()  # 첫글자만 대문자
			if argue == 3: result = str(data).swapcase()  # 대소문자 변경
			results.append(result)
		return results

	def change_lower_value(self, data):
		"""
		모든 리스트의 자료를 소문자로 만드는것이다
		"""
		for a in range(len(data)):
			data[a] = str(data[a]).lower()
		return data

	def change_waste_data(self, original_data):
		"""
		숫자와 문자만 남기는것
		result = []
		입력형태 :
		출력형태 :
		"""
		result = []
		for one_data in original_data:
			temp = ""
			for one in one_data:
				if str(one) in ' 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_':
					temp = temp + str(one)
			result.append(temp)
		return result

	def get_one_line_as_serched_word(self, file_name="pcell.py", input_text="menu_dic["):
		"""
		화일안에서 원하는 단어가 들어간 줄을 리스트로 만들어서 돌려주는것
		"""
		aa = open(file_name, 'r', encoding="UTF-8")
		result = []
		for one in aa.readlines():
			if input_text in str(one).strip():
				print(str(one).strip())
				result.append(str(one).strip())
		return result

	def check_col_name(self, col_name):
		"""
		각 제목으로 들어가는 글자에 대해서 변경해야 하는것을 변경하는 것이다
		커럼의제목으로 사용 못하는것을 제외
		"""
		for temp_01 in [[" ", "_"], ["(", "_"], [")", "_"], ["/", "_per_"], ["%", ""], ["'", ""], ['"', ""], ["$", ""],
		                ["__", "_"], ["__", "_"]]:
			col_name = col_name.replace(temp_01[0], temp_01[1])
		if col_name[-1] == "_": col_name = col_name[:-2]
		return col_name

	def check_filepath(self, file):
		"""
		입력자료가 폴더를 갖고있지 않으면 현재 폴더를 포함해서 돌려준다
		"""
		if len(file.split(".")) > 1:
			result = file
		else:
			cur_dir = self.read_current_path()
			result = cur_dir + "\\" + file
		return result


	def get_maxsize_in_list2d(self, list_2d_data):
		"""
		2차원 배열의 제일 큰 갯수를 확인한다
		#an_array = [[1, 2], [3, 4, 5]]
		#print("2차배열 요소의 최대 갯수는 ==>", check_list_maxsize(an_array))
		"""
		max_length = max(len(row) for row in list_2d_data)
		return max_length

	def click_mouse(self):
		"""
		마우스 왼쪽 한번 클릭하기
		"""
		pyautogui.click()

	def doubleclick_mouse(self):
		pyautogui.doubleClick()

	def compare_list_two_value(self, raw_data, req_number, project_name, vendor_name, nal):
		"""
		위아래 비교
		회사에서 사용하는 inq용 화일은 두줄로 구성이 된다
		한줄은 client가 요청한 스팩이며
		나머지 한줄은 vendor가 deviation사항으로 만든 스팩이다
		이두가지의 스팩을 하나로 만드는 것이다
		즉, 두줄에서 아래의 글씨가 있고 그것이 0, None가 아니면 위의것과 치환되는 것이다
		그런후 이위의 자료들만 따로 모아서 돌려주는 것이다
		"""
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

	def copy_file(self, old_path, new_path, meta=""):
		"""
		화일복사
		"""
		old_path = self.check_filepath(old_path)
		new_path = self.check_filepath(new_path)
		if meta == "":
			shutil.copy(old_path, new_path)
		else:
			shutil.copy2(old_path, new_path)

	def copy_folder(self, old_path, new_path):
		"""
		폴더복사
		"""
		shutil.copy(old_path, new_path)

	def copy_to_clipboard(self, input_text):
		"""
		클립보드에 입력된 내용을 복사를 하는 것이다
		"""
		pyperclip.copy(input_text)

	def count_same_value_by_ordered_in_list(self, input_list):
		"""
		리스트안의 자료들을 반복횟수가 놓은것으로만 확인
		"""
		result_dic = {}
		# 리스트안의 자료가 몇번나오는지 갯수를 센후에
		# 1번이상의 자료만 남기고 다 삭제하는것
		for one in input_list:
			if one in result_dic.keys():
				result_dic[one] = result_dic[one] + 1
			else:
				result_dic[one] = 1

		# 1번이상의 자료만 남기고 다 삭제하는것
		for one in list(result_dic.keys()):
			if result_dic[one] == 1:
				del result_dic[one]

		# 사전자료를 2차원리스트로 만든것
		new_list = []
		for key, val in result_dic.items():
			new_list.append([key, val])

		# 사전자료를 2차원리스트로 만든것을 역순으로 정렬한것
		new_list = sorted(new_list, key=lambda x: x[1], reverse=True)
		return new_list

	def delete_value_in_list1d_by_step(self, input_list, step, start=0):
		"""
		원하는 순서째의 자료를 ""으로 만드는것
		"""
		flag_no = 0
		for num in range(start, len(input_list)):
			flag_no = flag_no + 1
			if flag_no == step:
				input_list[num] = ""
				flag_no = 0
		return input_list

	def delete_empty_column_in_df(self, df_obj):
		"""
		dataframe의 빈열을 삭제
		제목이 있는 경우에만 해야 문제가 없을것이다
		"""
		nan_value = float("NaN")
		df_obj.replace(0, nan_value, inplace=True)
		df_obj.replace("", nan_value, inplace=True)
		df_obj.dropna(how="all", axis=1, inplace=True)
		return df_obj

	def delete_empty_value_in_list(self, input_list, condition=["", None, [], ()]):
		"""
		넘어온 리스트 형태의 자료중 조건에 맞는것이 있으면 제거하는 것
		입력형태 : ["aaa", "", None, "", "bbb"], [["aaa", "", None, "", "bbb"],"werw", 31231, [], ["aaa", "", None, "", "bbb"]]
		출력형태 : ["aaa", "bbb"], [['aaa', 'bbb'], 'werw', 31231, [], ['aaa', 'bbb']]
		"""
		# print(condition)
		for x in range(len(input_list) - 1, -1, -1):
			if input_list[x] in condition:
				del (input_list[x])
			else:
				if type(input_list[x]) == type([]):
					for y in range(len(input_list[x]) - 1, -1, -1):
						if input_list[x][y] in condition:
							del (input_list[x][y])
				else:
					if input_list[x] in condition:
						del (input_list[x])
		return input_list

	def delete_file(self, old_path):
		"""
		화일삭제
		"""
		old_path = self.check_filepath(old_path)
		os.remove(old_path)

	def delete_folder(self, old_dir, empty="no"):
		"""
		폴더삭제
		폴더안에 자료가 있어도 삭제
		"""
		if empty == "no":
			shutil.rmtree(old_dir)
		else:
			os.rmdir(old_dir)

	def delete_over2_emptyline_in_file(self, filename):
		"""
		화일을 읽어 내려가다가 2줄이상의 띄어쓰기가 된것을 하나만 남기는것
		텍스트로 저장된것을 사용하다가 필요해서 만듦
		"""
		f = open(filename, 'r', encoding='UTF8')
		lines = f.readlines()
		num = 0
		result = ""
		for one_line in lines:
			if one_line == "\n":
				num = num + 1
				if num == 1:
					result = result + str(one_line)
				elif num > 1:
					# print("2줄발견")
					pass
			else:
				num = 0
				result = result + str(one_line)
		return result

	def delete_special_letter_in_text(self, input_text):
		"""
		특수문자를 제거하는것
		"""
		for one in input_text:
			if str(one) in ' 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_':
				temp = temp + str(one)
		result = temp
		return result

	def split_file_by_each_method(self, filename):
		"""
		화일에서 def를 기준으로 분리하는 것
		"""
		# 텍스트 읽어오기
		file_pointer = open(filename, 'r', encoding='utf-8')
		# 한번에 다 읽기
		result = {}
		file_list = file_pointer.readlines()
		key_value = "__aa__bb__cc__"
		temp = []
		for ori_value in file_list:
			one_value = str(ori_value).replace(" ", "")
			one_value = str(one_value).replace("\t", "")
			if one_value[0:3] == "def":
				# print(key_value)
				result[key_value] = temp
				temp = []
				key_value = "__aa__bb__cc__" + str(ori_value)
			else:
				temp.append(ori_value)
		result[key_value] = temp

		aaa = list(result.keys())
		aaa.sort()

		for one in aaa:
			update_one = one.replace("__aa__bb__cc__", "")
			update_one = update_one.replace("\n", "")
			print(update_one)
			for one_1 in result[one]:
				one_1 = one_1.replace("\n", "")
				print(one_1)

	def devide_list1d_by_step(self, input_list1d, step_no):
		total_no = len(input_list1d)
		repeat_no = step_no
		group_no = divmod(len(input_list1d), int(step_no))[0]
		namuji = total_no - repeat_no * group_no
		result = []
		print(total_no, namuji)
		for y in range(step_no):
			for x in range(group_no + 1):
				new_no = x * step_no + y
				if new_no > total_no - 1:
					break
				else:
					print(y, x, new_no)
					result.append(input_list1d[int(new_no)])
		return result


	def change_num_as_1000comma(self, input_num):
		"""
		입력된 숫자를 1000단위로 콤마를 넣는것
		"""
		temp = str(input_num).split(".")
		total_len = len(temp[0])
		result = ""
		for num in range(total_len):
			one_num = temp[0][- num - 1]
			if num % 3 == 2:
				result = "," + one_num + result
			else:
				result = one_num + result
		if len(temp) > 1:
			result = result + "." + str(temp[1])
		return result

	def insert_data_in_list_by_step(self, input_list, insert_value, step):
		"""
		기존자료에 n번째마다 자료를 추가하는 기능
		raw_data = ['qweqw','qweqweqw','rterert','gdgdfgd',23,534534,'박상진']
		added_data = "new_data"
		step=3, 각 3번째 마다 자료를 추가한다면
		"""
		var_1, var_2 = divmod(len(input_list), int(step))
		for num in range(var_1, 0, -1):
			input_list.insert(num * int(step) - var_2 + 1, insert_value)
		return input_list

	def keyboard_input_for_action(self, action, key):
		"""
		pyautogui.keyDown('ctrl')  # ctrl 키를 누른 상태를 유지합니다.
		pyautogui.press('c')  # c key를 입력합니다.
		pyautogui.keyUp('ctrl')  # ctrl 키를 뗍니다.
		"""
		if action == "keydown":
			pyautogui.keyDown(key)
		if action == "keyup":
			pyautogui.keyUp(key)
		if action == "press":
			pyautogui.press(key)

	def keyboard_input_for_hotkey(self, input_keys=['ctrl', 'c']):
		"""
		pyautogui.hotkey('ctrl', 'c')  # ctrl-c to copy
		"""
		text = ""
		for one in input_keys:
			text = text + "'" + str(one) + "',"
		pyautogui.hotkey(text[:-1])

	def keyboard_input_for_keypad(self, action='enter', times=1, input_interval=0.1):
		"""
		pyautogui.press('enter', presses=3, interval=3) # enter 키를 3초에 한번씩 세번 입력합니다.
		"""
		pyautogui.press(action, presses=times, interval=input_interval)

	def keyboard_input_for_letter(self, input_text, input_interval=""):
		"""
		암호나 글자를 입력하는 데 사용하는것이다
		이것은 대부분 마우스를 원하는 위치에 옮기고, 클릭을 한번한후에 사용하는것이 대부분이다
		그저 글자를 타이핑 치는 것이다
		"""
		time.sleep(1)
		pyperclip.copy(input_text)
		pyautogui.hotkey("ctrl", "v")

	def make_folder(self, old_dir):
		"""
		폴더 만들기
		"""
		os.mkdir(old_dir)

	def change_list2d_to_samelen_list2d(self, input_data):
		"""
		길이가 다른 2dlist의 내부 값들을 길이가 같게 만들어주는 것이다
		가변적인 2차원배열을 최대크기로 모두 같이 만들어 준다
		"""
		result = []
		max_len = max(len(row) for row in input_data)
		for list_x in input_data:
			temp = list_x
			for no in range(len(list_x), max_len):
				temp.append("")
			result.append(temp)
		return result

	def make_zip_file(self, zip_name_path, new_path_all):
		"""
		화일들을 zip으로 압축하는것
		"""
		with zipfile.ZipFile(zip_name_path, 'w', compression=zipfile.ZIP_DEFLATED) as new_zip:
			for one in new_path_all:
				new_zip.write(one)
		new_zip.close()

	def move_file(self, old_file, new_file):
		"""
		화일을 이동시키는것
		"""
		old_file = self.check_filepath(old_file)
		shutil.move(old_file, new_file)

	def move_folder(self, old_dir, new_dir):
		"""
		폴더를 이동시키는것
		"""
		shutil.move(old_dir, new_dir)

	def move_mouse_xy(self, x1, y1):
		"""
		move_mouse_xy
		현재있는 위치를 기준으로 이동
		"""
		pyautogui.move(x1, y1)
		print(x1, y1)

	def paste_clipboard(self, ):
		"""
		클립보드에 복사된 내용을 현재 활성화된 프로그램에 붙여넣기를 하는 것이다
		"""
		result = pyperclip.paste()
		return result

	def pick_unique_col_name_compare_table_col_name(self, table_name, data2):
		"""
		고유한 컬럼만 골라낸다
		"""
		result = []
		columns = self.read_folder_filename_all(table_name)
		update_data2 = self.change_waste_data(data2)
		for temp_3 in update_data2:
			if not temp_3.lower() in columns:
				result.append(temp_3)
		return result

	def read_current_path(self):
		"""
		현재의 경로를 돌려주는것
		"""
		result = os.getcwd()
		return result

	def read_all_filename_in_folder(self, directory):
		"""
		폴더이름은 제외한다
		"""
		result = [f for f in os.listdir(directory) if os.isfile(os.path.join(directory, f))]
		return result

	def get_help_text_in_object_by_method(self, object):
		"""
		객체를 주면 메소드의 help를 돌려 주는것
		"""
		result = {}
		for one in dir(object):
			temp = []
			if not one.startswith('__'):
				try:
					temp.append(one)
					# print(one)
					temp.append(getattr(object, one).__doc__)
				# print(getattr(obgect, one).__doc__)
				except:
					pass
			result[one] = temp
		return result

	def get_method_name_with_argument_in_object(self, object):
		"""
		원하는 객체를 넣으면, 객체의 함수와 각 함수의 인자를 사전형식으로 돌려준다
		"""
		result = {}
		for obj_method in dir(object):
			try:
				method_data = inspect.signature(getattr(object, obj_method))
				dic_fun_var = {}
				if not obj_method.startswith("_"):
					for one in method_data.parameters:
						value_default = method_data.parameters[one].default
						value_data = str(method_data.parameters[one])

						if value_default == inspect._empty:
							dic_fun_var[value_data] = None
						else:
							value_key, value_value = value_data.split("=")
							if "remove" in obj_method:
								print(value_key, value_value)
							if value_value == "''" or value_value == '""':
								value_value = ''
							# 변수값중 ''가 들어간것이 없어져서, 아래의 것을 주석처리를 함
							# value_value = str(value_value).replace("'", "")
							# print(value_data, "키값==>", value_key, "입력값==>", value_value)
							dic_fun_var[str(value_key)] = value_value
						result[obj_method] = dic_fun_var

			except:
				pass
		return result

	def read_mouse_xy(self, ):
		"""
		현재의 마우스의 위치 읽어오기
		"""
		xy = pyautogui.position()
		return (xy.x, xy.y)

	def read_pickle_file(self, path_n_name=""):
		"""
		pickle로 자료를 만든것을 읽어오는 것이다
		"""
		with open(path_n_name, "rb") as fr:
			result = pickle.load(fr)
		return result

	def read_pickle_filenames_in_folder(self, directory="./", filter="pickle"):
		"""
		pickle로 만든 자료를 저장하는것
		"""
		result = []
		all_files = os.listdir(directory)
		if filter == "*" or filter == "":
			filter = ""
			result = all_files
		else:
			filter = "." + filter
			for x in all_files:
				if x.endswith(filter):
					result.append(x)
		return result

	def read_encodeing_type_in_system(self, ):
		"""
		기본적인 시스템에서의 인코딩을 읽어온다
		"""
		system_in_basic_incoding = sys.stdin.encoding
		system_out_basic_incoding = sys.stdout.encoding
		print("시스템의 기본적인 입력시의 인코딩 ====> ", system_in_basic_incoding)
		print("시스템의 기본적인 출력시의 인코딩 ====> ", system_out_basic_incoding)

	def pick_unique_value_in_list(self, input_datas, status=0):
		"""
		중복된 리스트의 자료를 없애는 것이다. 같은것중에서 하나만 남기고 나머지는 []으로 고친다
		"""
		if status == 0:
			result = []
			# 계속해서 pop으로 하나씩 없애므로 하나도 없으면 그만 실행한다
			while len(input_datas) != 0:
				gijun = input_datas.pop()
				sjpark = 0
				result.append(gijun)
				for number in range(len(input_datas)):
					if input_datas[int(number)] == []:  # 빈자료일때는 그냥 통과한다
						pass
					if input_datas[int(number)] == gijun:  # 자료가 같은것이 있으면 []으로 변경한다
						sjpark = sjpark + 1
						input_datas[int(number)] = []
		else:
			# 중복된것중에서 아무것도없는 []마저 없애는 것이다. 위의 only_one을 이용하여 사용한다
			# 같은것중에서 하나만 남기고 나머지는 []으로 고친다
			# 이것은 연속된 자료만 기준으로 삭제를 하는 것입니다
			# 만약 연속이 되지않은 같은자료는 삭제가 되지를 않읍니다
			result = list(self.remain_list_unique_value(input_datas))
			for a in range(len(result) - 1, 0, -1):
				if result[a] == []:
					del result[int(a)]
		return result

	def replace_word_in_text(self, input_text, before_text, after_text):
		"""
		폰트와 글자를 주면, 필셀의 크기를 돌려준다
		"""
		result = input_text.replace(before_text, after_text)
		return result

	def resize_list(self, input_list="", xy=""):
		"""
		입력으로 들어온 자료를 2차원으로 만든후
		xy로 넘어온 자료를 기준으로 만드는 것이다
		사이즈의 크기에 따라서 들어온 자료를 만든다
		"""
		result = []
		x_len, y_len = xy
		list1_max_len = len(input_list)
		list2_max_len = 0

		# 최대의 길이를 구한다
		for one_value in input_list:
			if type(one_value) == type([]):
				if list2_max_len < len(one_value):
					list2_max_len = len(one_value)

		for one_value in input_list:
			temp_list = []
			# 모든 항목을 리스트형태로 만든다
			if type(one_value) != type(one_value):
				temp_list = temp_list.append(one_value)
			else:
				temp_list = one_value

			# 최대길이에 맞도록 적은것은 ""으로 갯수를 채운다
			if list2_max_len - len(temp_list) > 0:
				for no in range(list2_max_len - len(temp_list)):
					temp_list.append("")
			result.append(temp_list)

		if xy != "":
			# x갯수를 정리한다
			if x_len < len(result):
				changed_result_2 = result[0:x_len]
			# y갯수를 정리한다
			changed_result_3 = []
			if y_len < len(changed_result_2[0]):
				for one_list in changed_result_2:
					changed_result_3.append(one_list[0:y_len])
			else:
				changed_result_3 = changed_result_2
			result = changed_result_3

		return result

	def save_file_by_pickle(self, input_data="", path_n_name=""):
		"""
		피클로 객체를 저장하는것
		"""
		if ":" in path_n_name:
			full_filename = path_n_name
		else:
			full_filename = "./" + path_n_name
		with open(str(full_filename) + ".pickle", "wb") as fr:
			pickle.dump(input_data, fr)

	def sort_list(self, input_data):
		"""
		aa = [[111, 'abc'], [222, 222],['333', 333], ['777', 'sjpark'], ['aaa', 123],['zzz', 'sang'], ['jjj', 987], ['ppp', 'park']]
		정렬하는 방법입니다
		"""
		result = []
		for one_data in input_data:
			for one in one_data:
				result.append(one.sort())
		return result

	def sort_list2d(self, input_set, sort_index=[0]):
		"""
		집합자료를 정렬하는것
		사용법 : [자료, [1,-2,3]]
		자료를 1,2,3순으로 정렬을 하는데, 2번째는 역순으로 정렬
		"""
		temp = ""
		for one in sort_index:
			# 역순으로 정렬할게 있는지 확인하는것
			if "-" in str(one):
				temp = temp + ("-x[%s], " % (str(abs(one))))
			else:
				temp = temp + ("x[%s], " % (str(one)))
		# lamda형식으로 만들어서 sorted의 key로 사용
		str_lambda = ("lambda x :(%s)" % temp[:-2])
		# print(str_lambda)
		result = sorted(input_set, key=eval(str_lambda))
		return result

	def sort_list_by_index(self, input_list, index_no=0):
		"""
		입력 :  리스트자료
		리스트자료를 몇번째 순서를 기준으로 정렬하는것
		aa = [[111, 'abc'], [222, 222],['333', 333], ['777', 'sjpark'], ['aaa', 123],['zzz', 'sang'], ['jjj', 987], ['ppp', 'park']]
		value=sort_list(리스트자료, 정렬기준번호)
		"""
		result_before = [(i[index_no], i) for i in input_list]
		result_before.sort()
		result = [i[1] for i in result_before]
		return result

	def split_file_by_def(self, filename, base_text="def"):
		"""
		화일안의 def를 기준으로 문서를 분리하는것
		같은 함수의 코드를 찾기위해 def로 나누는것
		맨앞의 시작글자에 따라서 나눌수도 있다
		"""
		temp_list = []
		result = []
		# 화일을 읽어온다
		f = open(filename, 'r', encoding='UTF8')
		lines = f.readlines()
		original = lines
		# 빈 줄을 제거한다
		lines = list(map(lambda s: s.strip(), lines))
		start_no = 0
		for no in range(len(lines)):
			line = lines[no]

			# 각줄의 공백을 제거한다
			one_line = line.strip()
			# 혹시 잇을수있는 줄바꿈을 제거한다
			one_line = one_line.replace("\n", "")
			# 맨앞에서 def가 발견이되면 여태저장한것을 최종result리스트에 저장 하고 새로이 시작한다
			if one_line[0:(len(base_text) + 1)] == base_text and temp_list != []:
				print("처음은 ===> ", start_no)
				print("끝은 ===> ", no)
				result.append(temp_list, start_no, no)
				start_no = no
				temp_list = []
			# 빈행이나 주석으로된 열을 제외한다
			if one_line != "" and one_line[0] != "#":
				temp_list.append(one_line)
		f.close()
		return result

	def split_jamo_in_korean(self, one_text):
		"""
		한글자의 한글을 자음과 모음으로 구분해 주는것
		"""

		first_letter = ["ㄱ", "ㄲ", "ㄴ", "ㄷ", "ㄸ", "ㄹ", "ㅁ", "ㅂ", "ㅃ", "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅉ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"]
		# 19 글자
		second_letter = ["ㅏ", "ㅐ", "ㅑ", "ㅒ", "ㅓ", "ㅔ", "ㅕ", "ㅖ", "ㅗ", "ㅘ", "ㅙ", "ㅚ", "ㅛ", "ㅜ", "ㅝ", "ㅞ", "ㅟ", "ㅠ", "ㅡ",
		                 "ㅢ", "ㅣ"]  # 21 글자
		third_letter = ["", "ㄱ", "ㄲ", "ㄳ", "ㄴ", "ㄵ", "ㄶ", "ㄷ", "ㄹ", "ㄺ", "ㄻ", "ㄼ", "ㄽ", "ㄾ", "ㄿ", "ㅀ", "ㅁ", "ㅂ", "ㅄ",
		                "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"]  # 28 글자, 없는것 포함
		one_byte_data = one_text.encode("utf-8")

		new_no_1 = (int(one_byte_data[0]) - 234) * 64 * 64
		new_no_2 = (int(one_byte_data[1]) - 128) * 64
		new_no_3 = (int(one_byte_data[2]) - 128)

		value = new_no_1 + new_no_2 + new_no_3 - 3072

		temp_num_1 = divmod(value, 588)  # 초성이 몇번째 자리인지를 알아내는것
		temp_num_2 = divmod(divmod(value, 588)[1], 28)  # 중성과 종성의 자릿수를 알아내는것것

		chosung = first_letter[divmod(value, 588)[0]]  # 초성
		joongsung = second_letter[divmod(divmod(value, 588)[1], 28)[0]]  # 중성
		jongsung = third_letter[divmod(divmod(value, 588)[1], 28)[1]]  # 종성

		return [chosung, joongsung, jongsung]

	def split_list1d_by_step(self, input_list1d, step_no):
		"""
		12개의 리스트를
		입력 : [ [1,2,3,4,5,6,7,8,9,10,11,12], 4]를 받으면
			총 4개의 묶읆으로 순서를 섞어서 만들어 주는것
			[1,5,9,  2,6,10,  3,7,11,  4,8,12] 로 만들어 주는것
		"""
		total_no = len(input_list1d)
		repeat_no = step_no
		group_no = divmod(len(input_list1d), int(step_no))[0]
		namuji = total_no - repeat_no * group_no
		result = []
		# print(total_no, namuji)
		for y in range(step_no):
			for x in range(group_no + 1):
				new_no = x * step_no + y
				if new_no > total_no - 1:
					break
				else:
					# print(y, x, new_no)
					result.append(input_list1d[int(new_no)])
		return result

	def split_list1d_by_string(self, input_list, input_text):
		"""
		리스트로 들어온 자료들을 한번에 분리해서 2차원리스트로 만드는 것
		"""

		result = []
		for one_value in input_list:
			temp_result = str(one_value).split(input_text)
			result.append(temp_result)
		return result

	def split_num_n_char_in_text(self, raw_data):
		"""
		문자와숫자를 분리해서 리스트로 돌려주는 것이다
		123wer -> ['123','wer']
		"""
		temp = ""
		int_temp = ""
		result = []
		datas = str(raw_data)
		for num in range(len(datas)):
			if num == 0:
				temp = str(datas[num])
			else:
				try:
					fore_var = int(datas[num])
					fore_var_status = "integer"
				except:
					fore_var = datas[num]
					fore_var_status = "string"
				try:
					back_var = int(datas[num - 1])
					back_var_status = "integer"
				except:
					back_var = datas[num - 1]
					back_var_status = "string"

				if fore_var_status == back_var_status:
					temp = temp + datas[num]
				else:
					result.append(temp)
					temp = datas[num]
		if len(temp) > 0:
			result.append(temp)
		return result

	def split_path_by_n_name(self, input_value=""):
		"""
		입력값을 경로와 이름으로 분리
		"""
		filename = ""
		path = ""
		input_value = input_value.replace("/", "\\")
		temp_1 = input_value.split("\\")
		if "." in temp_1[-1]:
			filename = temp_1[-1]
		if len(temp_1) > 1 and "\\" in temp_1[:len(temp_1[-1])]:
			path = input_value[:len(temp_1[-1])]
		result = [filename, path]
		return result

	def split_text_by_step(self, input_text, number):
		"""
		문자열을 몇개씩 숫자만큼 분리하기
		['123456'] => ['12','34','56']
		"""
		result = []
		for i in range(0, len(input_text), number):
			result.append("".os.path.join(input_text[i:i + number]))
		return result

	def split_text_by_newline_tab(self, input_text, number):
		"""
		문자열을 \n, tab으로 구분해서 분리한다
		"""
		result = []
		temp_list = str(input_text).split("\n")
		for one_value_1 in temp_list:
			temp = []
			tab_list = str(one_value_1).split("\t")
			for one_value_2 in tab_list:
				temp.append(one_value_2)
			result.append(temp)

		return result

	def trans_list(self, input_list2d="입력필요"):
		"""
		trans_list( input_list2d="입력필요")
		2차원자료를 행과열을 바꿔서 만드는것
		단, 길이가 같아야 한다
		입력형태 :
		출력형태 :
		"""
		checked_input_list2d = self.make_list2d_samelen(input_list2d)
		result = [list(x) for x in zip(*checked_input_list2d)]
		return result

	def swap_list_data(self, input_data):
		# input_data : [a, b, c, d]
		# result : [b, a, d, c]
		# 두개의 자료들에 대해서만 자리를 바꾸는 것이다
		result = []
		for one_data in range(int(len(input_data) / 2)):
			result.append(input_data[one_data * 2 + 1])
			result.append(input_data[one_data * 2])
		return result

	def check_text_encoding_data(self, text, encoding_type):
		byte_data = text.encode(encoding_type)
		hex_data_as_str = " ".os.path.join("{0}".format(hex(c)) for c in byte_data)
		int_data_as_str = " ".os.path.join("{0}".format(int(c)) for c in byte_data)

		print("\"" + text + "\" 전체 문자 길이: {0}".format(len(text)))
		print("\"" + text + "\" 전체 문자를 표현하는 데 사용한 바이트 수: {0} 바이트".format(len(byte_data)))
		print("\"" + text + "\" 16진수 값: {0}".format(hex_data_as_str))
		print("\"" + text + "\" 10진수 값: {0}".format(int_data_as_str))
		# 사용법 : text_encoding_data("Hello", "utf-8")
		return int_data_as_str

	def write_hangul_cjj(self, letters="박상진", canvas_size=[50, 50], stary_xy=[1, 1]):
		# 입력받은 한글을 크기가 50 x 50의 엑셀 시트에 글씨를 색칠하여 나타내는 것이다

		# 기본 설정부분
		size_x = canvas_size[0]
		size_y = canvas_size[1]
		# 문자 하나의 기본크기
		# 기본문자는 10을 기준으로 만들었으며, 이것을 얼마만큼 크게 만들것인지 한글자의 배수를 정하는것
		h_mm = int(canvas_size[0] / 10)
		w_mm = int(canvas_size[1] / 10)
		# 시작위치
		h_start = stary_xy[0]
		w_start = stary_xy[1]

		check_han = re.compile("[ㄱ-ㅎ|ㅏ-ㅣ|가-힣]")
		for one_char in letters:
			# 한글을 초성, 중성, 종성으로 나누는 것이다
			if check_han.match(one_char):
				jamo123 = self.split_hangul_jamo(one_char)
				if jamo123[0][2] == "":
					# 가, 나, 다
					if jamo123[0][1] in ["ㅏ", "ㅐ", "ㅑ", "ㅒ", "ㅓ", "ㅔ", "ㅕ", "ㅖ", "ㅣ"]:
						# 기본설정은 시작점은 [1,1]이며, 캔버스의 크기는 [50, 50]인것이다

						start_xy = [1, 1]
						size = [10, 5]  # 위에서 배수를 5,5를 기본으로 해서 50x50되는 것이다
						# 자음의 시작점은 1,1이며, 크기는 50 x 25의 사이즈의 자음을 만드는 것이다
						self.draw_jaum_color(jamo123[0][0],
						                     [h_start + h_mm * (start_xy[0] - 1), w_start + w_mm * (start_xy[1] - 1)],
						                     [h_mm * size[0], w_mm * size[1]])
						# 모음의 시작점은 자음의 끝점에서 5를 이동한 1,30이며, 크기는 자음보다 가로의 크기를 좀 줄인
						# 50 x 20의 사이즈의 자음을 만드는 것이다

						start_xy = [1, 7]
						size = [10, 4]
						self.draw_moum_color(jamo123[0][1],
						                     [h_start + h_mm * (start_xy[0] - 1), w_start + w_mm * (start_xy[1] - 1)],
						                     [h_mm * size[0], w_mm * size[1]])

					# 구, 누, 루
					if jamo123[0][1] in ["ㅗ", "ㅛ", "ㅜ", "ㅡ"]:
						start_xy = [1, 1]
						size = [4, 10]
						self.draw_jaum_color(jamo123[0][0],
						                     [h_start + h_mm * (start_xy[0] - 1), w_start + w_mm * (start_xy[1] - 1)],
						                     [h_mm * size[0], w_mm * size[1]])
						start_xy = [6, 1]
						size = [5, 10]
						self.draw_moum_color(jamo123[0][1],
						                     [h_start + h_mm * (start_xy[0] - 1), w_start + w_mm * (start_xy[1] - 1)],
						                     [h_mm * size[0], w_mm * size[1]])

					# 와, 왜, 궈
					if jamo123[0][1] in ["ㅘ", "ㅙ", "ㅚ", "ㅝ", "ㅞ", "ㅟ", "ㅢ"]:
						# lists = self.div_mo2_mo1(jamo123[0][1])

						start_xy = [1, 1]
						size = [10, 5]
						self.draw_jaum_color(jamo123[0][0],
						                     [h_start + h_mm * (start_xy[0] - 1), w_start + w_mm * (start_xy[1] - 1)],
						                     [h_mm * size[0], w_mm * size[1]])
						start_xy = [8, 1]
						size = [3, 8]
						self.draw_moum_color(jamo123[0][1],
						                     [h_start + h_mm * (start_xy[0] - 1), w_start + w_mm * (start_xy[1] - 1)],
						                     [h_mm * size[0], w_mm * size[1]])
						start_xy = [1, 8]
						size = [6, 3]
						self.draw_moum_color(jamo123[0][1],
						                     [h_start + h_mm * (start_xy[0] - 1), w_start + w_mm * (start_xy[1] - 1)],
						                     [h_mm * size[0], w_mm * size[1]])

				if jamo123[0][2] != "":
					# 왕, 웍, 윔
					if jamo123[0][1] in ["ㅘ", "ㅙ", "ㅚ", "ㅝ", "ㅞ", "ㅟ", "ㅢ"]:
						hangul_type = "23자음+1332-2중모음+24자음"
						# lists = div_mo2_mo1(jamo123[0][1])

						start_xy = [1, 1]
						size = [4, 5]
						self.draw_jaum_color(jamo123[0][0],
						                     [h_start + h_mm * (start_xy[0] - 1), w_start + w_mm * (start_xy[1] - 1)],
						                     [h_mm * size[0], w_mm * size[1]])
						start_xy = [4, 1]
						size = [3, 7]
						self.draw_moum_color(jamo123[0][1],
						                     [h_start + h_mm * (start_xy[0] - 1), w_start + w_mm * (start_xy[1] - 1)],
						                     [h_mm * size[0], w_mm * size[1]])
						start_xy = [1, 7]
						size = [6, 3]
						self.draw_moum_color(jamo123[0][1],
						                     [h_start + h_mm * (start_xy[0] - 1), w_start + w_mm * (start_xy[1] - 1)],
						                     [h_mm * size[0], w_mm * size[1]])
						start_xy = [8, 1]
						size = [3, 6]
						self.draw_jaum_color(jamo123[0][0],
						                     [h_start + h_mm * (start_xy[0] - 1), w_start + w_mm * (start_xy[1] - 1)],
						                     [h_mm * size[0], w_mm * size[1]])

					# 앙, 양, 건
					if jamo123[0][1] in ["ㅏ", "ㅐ", "ㅑ", "ㅒ", "ㅓ", "ㅔ", "ㅕ", "ㅖ", "ㅣ"]:
						start_xy = [1, 1]
						size = [3, 5]
						self.draw_jaum_color(jamo123[0][0],
						                     [h_start + h_mm * (start_xy[0] - 1), w_start + w_mm * (start_xy[1] - 1)],
						                     [h_mm * size[0], w_mm * size[1]])
						start_xy = [1, 6]
						size = [5, 4]
						self.draw_moum_color(jamo123[0][1],
						                     [h_start + h_mm * (start_xy[0] - 1), w_start + w_mm * (start_xy[1] - 1)],
						                     [h_mm * size[0], w_mm * size[1]])
						start_xy = [7, 2]
						size = [3, 6]
						self.draw_jaum_color(jamo123[0][0],
						                     [h_start + h_mm * (start_xy[0] - 1), w_start + w_mm * (start_xy[1] - 1)],
						                     [h_mm * size[0], w_mm * size[1]])

					# 곡, 는
					if jamo123[0][1] in ["ㅗ", "ㅛ", "ㅜ", "ㅡ"]:
						start_xy = [1, 1]
						size = [3, 10]
						self.draw_jaum_color(jamo123[0][0],
						                     [h_start + h_mm * (start_xy[0] - 1), w_start + w_mm * (start_xy[1] - 1)],
						                     [h_mm * size[0], w_mm * size[1]])
						start_xy = [4, 1]
						size = [3, 10]
						self.draw_moum_color(jamo123[0][1],
						                     [h_start + h_mm * (start_xy[0] - 1), w_start + w_mm * (start_xy[1] - 1)],
						                     [h_mm * size[0], w_mm * size[1]])
						start_xy = [8, 1]
						size = [3, 10]
						self.draw_jaum_color(jamo123[0][0],
						                     [h_start + h_mm * (start_xy[0] - 1), w_start + w_mm * (start_xy[1] - 1)],
						                     [h_mm * size[0], w_mm * size[1]])

	def get_moum_xy_list(size=[1, 2], input_data="ㅏ"):
		# 모음을 엑셀에 나타내기 위한 좌표를 주는 것이다
		x, y = size
		# x, y는 글자의 크기
		mo_01 = [["ㅏ"], [1, 0.6 * y, x, 0.6 * y],
		         [0.4 * x, 0.6 * y, 0.4 * x, 0.8 * y]]
		mo_02 = [["ㅑ"], [1, 0.6 * y, x, 0.6 * y],
		         [0.4 * x, 0.6 * y, 0.4 * x, 0.8 * y],
		         [0.6 * x, 0.6 * y, 0.6 * x, 0.8 * y]]
		mo_03 = [["ㅓ"], [1, 0.6 * y, x, 0.6 * y],
		         [0.4 * x, 0.4 * y, 0.4 * x, 0.6 * y]]
		mo_04 = [["ㅕ"], [1, 0.6 * y, x, 0.6 * y],
		         [0.4 * x, 0.4 * y, 0.4 * x, 0.6 * y],
		         [0.6 * x, 0.4 * y, 0.6 * x, 0.6 * y]]
		mo_10 = [["ㅣ"], [1, 0.6 * y, x, 0.6 * y]]
		mo_05 = [["ㅗ"], [x, 1, x, y],
		         [x, 0.5 * y, 0.8 * x, 0.5 * y]]
		mo_06 = [["ㅛ"], [x, 1, x, y],
		         [x, 0.3 * y, 0.8 * x, 0.3 * y],
		         [x, 0.7 * y, 0.8 * x, 0.7 * y]]
		mo_07 = [["ㅜ"], [1, 1, 1, y],
		         [1, 0.5 * y, 0.5 * x, 0.5 * y]]
		mo_08 = [["ㅠ"], [1, 1, 1, y],
		         [1, 0.3 * y, 0.8 * x, 0.3 * y],
		         [1, 0.7 * y, 0.8 * x, 0.7 * y]]
		mo_09 = [["ㅡ"], [0.5 * x, 1, 0.5 * x, y]]

		mo_21 = [["ㅐ"], [1, 0.6 * y, x, 0.6 * y],
		         [1, 0.8 * y, x, 0.8 * y],
		         [0.4 * x, 0.6 * y, 0.4 * x, 0.8 * y]]
		mo_22 = [["ㅒ"], [1, 0.6 * y, x, 0.6 * y],
		         [1, 0.8 * y, x, 0.8 * y],
		         [0.4 * x, 0.6 * y, 0.4 * x, 0.6 * y],
		         [0.6 * x, 0.8 * y, 0.6 * x, 0.8 * y]]
		mo_23 = [["ㅔ"], [1, 0.6 * y, x, 0.6 * y],
		         [1, 0.8 * y, x, 0.8 * y],
		         [0.4 * x, 0.4 * y, 0.4 * x, 0.6 * y]]
		mo_24 = [["ㅖ"], [1, 0.6 * y, x, 0.6 * y],
		         [1, 0.8 * y, x, 0.8 * y],
		         [0.4 * x, 0.4 * y, 0.4 * x, 0.6 * y],
		         [0.6 * x, 0.4 * y, 0.6 * x, 0.6 * y]]

		jamo2_dic = {
			"ㅏ": mo_01, "ㅑ": mo_02, "ㅓ": mo_03, "ㅕ": mo_04, "ㅗ": mo_05,
			"ㅛ": mo_06, "ㅜ": mo_07, "ㅠ": mo_08, "ㅡ": mo_09, "ㅣ": mo_10,
			"ㅐ": mo_21, "ㅒ": mo_22, "ㅔ": mo_23, "ㅖ": mo_24,
		}
		result = jamo2_dic[input_data]
		return result

	def get_jaum_xy_list(size=[1, 2], input_data="ㄱ"):
		x, y = size
		# x, y는 글자의 크기
		ja_01 = [["ㄱ"], [1, 1, 1, y], [1, y, x, y]]
		ja_02 = [["ㄴ"], [1, 1, x, 1], [x, 1, x, y]]
		ja_03 = [["ㄷ"], [1, y, 1, 1], [1, 1, x, 1], [x, 1, x, y]]
		ja_04 = [["ㄹ"], [1, 1, 1, y], [1, y, 0.5 * x, y], [0.5 * x, y, 0.5 * x, 1], [0.5 * x, 1, x, 1], [x, 1, x, y]]
		ja_05 = [["ㅁ"], [1, 1, 1, y], [1, y, x, y], [x, y, x, 1], [x, 1, 1, 1]]
		ja_06 = [["ㅂ"], [1, 1, x, 1], [x, 1, x, y], [x, y, 1, y], [0.5 * x, 1, 0.5 * x, y]]
		ja_07 = [["ㅅ"], [1, 0.5 * y, 0.3 * x, 0.5 * y], [0.3 * x, 0.5 * y, x, 1], [0.3 * x, 0.5 * y, x, y]]
		ja_08 = [["ㅇ"], [0.8 * x, 0.2 * y, 0.8 * x, 0.8 * y], [0.8 * x, 0.8 * y, 0.6 * x, y, ""],
		         [0.6 * x, y, 0.2 * x, y], [0.2 * x, y, 1, 0.8 * y, "/"], [1, 0.8 * y, 1, 0.2 * y],
		         [1, 0.2 * y, 0.2 * x, 1, ""], [0.2 * x, 1, 0.6 * x, 1], [0.6 * x, 1, 0.8 * x, 0.2 * y, "/"]]
		ja_09 = [["ㅈ"], [1, 1, 1, y], [1, 0.5 * y, 0.5 * x, 0.5 * y], [0.5 * x, 0.5 * y, x, 1, "/"],
		         [0.5 * x, 0.5 * y, x, y, ""]]
		ja_10 = [["ㅊ"], [0.2 * x, 0.5 * y, 1, 0.5 * y], [0.2 * x, 1, 0.2 * x, y], [0.2 * x, 0.5 * y, 0.4 * x, 0.5 * y],
		         [1, 0.5 * y, 0.5 * x, 0.5 * y], [0.5 * x, 0.5 * y, x, 1], [0.5 * x, 0.5 * y, x, y, ""]]
		ja_11 = [["ㅋ"], [1, 1, 1, y], [1, y, x, y], [0.5 * x, 1, 0.5 * x, y]]
		ja_12 = [["ㅌ"], [1, y, 1, 1], [1, 1, x, 1], [x, 1, x, y], [0.5 * x, 1, 0.5 * x, y]]
		ja_13 = [["ㅍ"], [1, 1, 1, y], [x, 1, x, y], [1, 0.2 * y, x, 0.2 * y], [1, 0.8 * y, x, 0.8 * y]]
		ja_14 = [["ㅎ"], [1, 0.5 * y, 0.2 * x, 0.5 * y], [0.2 * x, 1, 0.2 * x, y], [0.4 * x, 0.3 * y, 0.4 * x, 0.8 * y],
		         [0.4 * x, 0.8 * y, 0.6 * x, y], [0.6 * x, y, 0.8 * x, y], [0.8 * x, y, x, 0.8 * y],
		         [x, 0.8 * y, x, 0.3 * y], [x, 0.3 * y, 0.8 * x, 1], [0.8 * x, 1, 0.6 * x, 1],
		         [0.6 * x, 1, 0.4 * x, 0.3 * y]]
		ja_31 = [["ㄲ"], [1, 1, 1, 0.4 * y], [1, 0.4 * y, x, 0.4 * y], [1, 0.7 * y, 1, y], [1, y, x, y], ]
		ja_32 = [["ㄸ"], [1, 1, 1, 0.4 * y], [1, 1, x, 1], [x, 1, x, 0.4 * y], [1, 0.7 * y, 1, y],
		         [1, 0.7 * y, x, 0.7 * y], [x, 0.7 * y, x, y], ]
		ja_33 = [["ㅃ"], [1, 1, x, 1], [x, 1, x, 0.4 * y], [x, 0.4 * y, 1, 0.4 * y], [0.5 * x, 1, 0.5 * x, 0.4 * y],
		         [1, 0.7 * y, x, 0.7 * y], [x, 0.7 * y, x, y], [x, y, 1, y], [0.5 * x, 0.7 * y, 0.5 * x, y], ]
		ja_34 = [["ㅆ"], [1, 0.3 * y, 0.4 * x, 0.3 * y], [0.4 * x, 0.3 * y, x, 1], [0.4 * x, 0.3 * y, x, 0.5 * y],
		         [1, 0.8 * y, 0.4 * x, 0.8 * y], [0.4 * x, 0.8 * y, x, 0.6 * y], [0.4 * x, 0.8 * y, x, y], ]
		ja_35 = [["ㅉ"], [1, 1, 1, 0.5 * y], [1, 0.3 * y, 0.4 * x, 0.3 * y], [0.4 * x, 0.3 * y, x, 1],
		         [0.4 * x, 0.3 * y, x, 0.5 * y], [1, 0.6 * y, 1, y], [1, 0.8 * y, 0.4 * x, 0.8 * y],
		         [0.4 * x, 0.8 * y, x, 0.6 * y], [0.4 * x, 0.8 * y, x, y], ]
		ja_36 = [["ㄳ"], [1, 1, 1, 0.4 * y], [1, 0.4 * y, x, 0.4 * y], [1, 0.8 * y, 0.4 * x, 0.8 * y],
		         [0.4 * x, 0.8 * y, x, 0.6 * y], [0.4 * x, 0.8 * y, x, y], ]
		ja_37 = [["ㄵ"], [1, 1, x, 1], [x, 1, x, 0.4 * y], [1, 0.6 * y, 1, y], [1, 0.8 * y, 0.4 * x, 0.8 * y],
		         [0.4 * x, 0.8 * y, x, 0.6 * y], [0.4 * x, 0.8 * y, x, y], ]
		ja_38 = [["ㄶ"], [1, 1, x, 1], [x, 1, x, 0.4 * y], [0.1 * x, 0.8 * y, 1, 0.8 * y],
		         [0.2 * x, 0.6 * y, 0.2 * x, y], [0.4 * x, 0.7 * y, 0.4 * x, 0.9 * y], [0.4 * x, 0.9 * y, 0.6 * x, y],
		         [0.6 * x, y, x, 0.9 * y], [x, 0.9 * y, x, 0.7 * y], [x, 0.7 * y, 0.8 * x, 0.6 * y],
		         [0.8 * x, 0.6 * y, 0.6 * x, 0.6 * y], [0.6 * x, 0.6 * y, 0.4 * x, 0.7 * y]]
		ja_39 = [["ㄺ"], [1, 1, 1, 0.4 * y], [1, 0.4 * y, 0.5 * x, 0.4 * y], [0.5 * x, 0.4 * y, 0.5 * x, 1],
		         [0.5 * x, 1, x, 1], [x, 1, x, 0.4 * y], [1, 0.7 * y, 1, y], [1, y, x, y], ]
		ja_40 = [["ㄻ"], [1, 1, 1, 0.4 * y], [1, 0.4 * y, 0.5 * x, 0.4 * y], [0.5 * x, 0.4 * y, 0.5 * x, 1],
		         [0.5 * x, 1, x, 1], [x, 1, x, 0.4 * y], [1, 0.7 * y, 1, y], [1, y, x, y], [x, y, x, 0.7 * y],
		         [x, 0.7 * y, 1, 0.7 * y], ]
		ja_41 = [["ㄼ"], [1, 1, 1, 0.4 * y], [1, 0.4 * y, 0.5 * x, 0.4 * y], [0.5 * x, 0.4 * y, 0.5 * x, 1],
		         [0.5 * x, 1, x, 1], [x, 1, x, 0.4 * y], [1, 0.7 * y, x, 0.7 * y], [x, 0.7 * y, x, y], [x, y, 1, y],
		         [0.5 * x, 0.7 * y, 0.5 * x, y], ]
		ja_42 = [["ㄽ"], [1, 1, 1, 0.4 * y], [1, 0.4 * y, 0.5 * x, 0.4 * y], [0.5 * x, 0.4 * y, 0.5 * x, 1],
		         [0.5 * x, 1, x, 1], [x, 1, x, 0.4 * y], [1, 0.8 * y, 0.4 * x, 0.8 * y], [0.4 * x, 0.8 * y, x, 0.6 * y],
		         [0.4 * x, 0.8 * y, x, y], ]
		ja_43 = [["ㄾ"], [1, 1, 1, 0.4 * y], [1, 0.4 * y, 0.5 * x, 0.4 * y], [0.5 * x, 0.4 * y, 0.5 * x, 1],
		         [0.5 * x, 1, x, 1], [x, 1, x, 0.4 * y], [1, 0.7 * y, 1, y], [1, 0.7 * y, x, 0.7 * y],
		         [x, 0.7 * y, x, y], [0.5 * x, 0.7 * y, 0.5 * x, y], ]
		ja_44 = [["ㄿ"], [1, 1, 1, 0.4 * y], [1, 0.4 * y, 0.5 * x, 0.4 * y], [0.5 * x, 0.4 * y, 0.5 * x, 1],
		         [0.5 * x, 1, x, 1], [x, 1, x, 0.4 * y], [1, 0.6 * y, 1, y], [x, 0.6 * y, x, y],
		         [1, 0.7 * y, x, 0.7 * y], [1, 0.9 * y, x, 0.9 * y], ]
		ja_45 = [["ㅀ"], [1, 1, 1, 0.4 * y], [1, 0.4 * y, 0.5 * x, 0.4 * y], [0.5 * x, 0.4 * y, 0.5 * x, 1],
		         [0.5 * x, 1, x, 1], [x, 1, x, 0.4 * y], [0.1 * x, 0.8 * y, 1, 0.8 * y], [0.2 * x, 0.6 * y, 0.2 * x, y],
		         [0.4 * x, 0.7 * y, 0.4 * x, 0.9 * y], [0.4 * x, 0.9 * y, 0.6 * x, y], [0.6 * x, y, x, 0.9 * y],
		         [x, 0.9 * y, x, 0.7 * y], [x, 0.7 * y, 0.8 * x, 0.6 * y], [0.8 * x, 0.6 * y, 0.6 * x, 0.6 * y],
		         [0.6 * x, 0.6 * y, 0.4 * x, 0.7 * y]]
		ja_46 = [["ㅄ"], [1, 1, x, 1], [x, 1, x, 0.4 * y], [x, 0.4 * y, 1, 0.4 * y], [0.5 * x, 1, 0.5 * x, 0.4 * y],
		         [1, 0.8 * y, 0.4 * x, 0.8 * y], [0.4 * x, 0.8 * y, x, 0.6 * y], [0.4 * x, 0.8 * y, x, y], ]

		jamo1_dic = {"ㄱ": ja_01, "ㄴ": ja_02, "ㄷ": ja_03, "ㄹ": ja_04, "ㅁ": ja_05,
		             "ㅂ": ja_06, "ㅅ": ja_07, "ㅇ": ja_08, "ㅈ": ja_09, "ㅊ": ja_10,
		             "ㅋ": ja_11, "ㅌ": ja_12, "ㅍ": ja_13, "ㅎ": ja_14,
		             "ㄲ": ja_31, "ㄸ": ja_32, "ㅃ": ja_33, "ㅆ": ja_34, "ㅉ": ja_35,
		             "ㄳ": ja_36, "ㄵ": ja_37, "ㄶ": ja_38, "ㄺ": ja_39, "ㄻ": ja_40,
		             "ㄼ": ja_41, "ㄽ": ja_42, "ㄾ": ja_43, "ㄿ": ja_44, "ㅀ": ja_45, "ㅄ": ja_46,
		             }

		result = jamo1_dic[input_data]
		return result

	def split_double_moum(self, double_moum):
		# 이중모음을 단모음으로 바꿔주는것
		mo2_dic = {"ㅘ": ["ㅗ", "ㅏ"], "ㅙ": ["ㅗ", "ㅐ"], "ㅚ": ["ㅗ", "ㅣ"], "ㅝ": ["ㅜ", "ㅓ"], "ㅞ": ["ㅜ", "ㅔ"], "ㅟ": ["ㅜ", "ㅣ"],
		           "ㅢ": ["ㅡ", "ㅣ"], }
		result = mo2_dic[double_moum]
		return result

	def split_engnum(self, data):
		# 단어중에 나와있는 숫자, 영어를 분리하는기능
		re_compile = re.compile(r"([a-zA-Z]+)([0-9]+)")
		result = re_compile.findall(data)
		new_result = []
		for dim1_data in result:
			for dim2_data in dim1_data:
				new_result.append(dim2_data)
		return new_result

	def split_hangul_jamo(self, text):
		# 한글자의 한글을 자음과 모음으로 구분해 주는것
		first_letter = ["ㄱ", "ㄲ", "ㄴ", "ㄷ", "ㄸ", "ㄹ", "ㅁ", "ㅂ", "ㅃ", "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅉ", "ㅊ", "ㅋ", "ㅌ", "ㅍ",
		                "ㅎ"]  # 19 글자
		second_letter = ["ㅏ", "ㅐ", "ㅑ", "ㅒ", "ㅓ", "ㅔ", "ㅕ", "ㅖ", "ㅗ", "ㅘ", "ㅙ", "ㅚ", "ㅛ", "ㅜ", "ㅝ", "ㅞ", "ㅟ", "ㅠ", "ㅡ",
		                 "ㅢ",
		                 "ㅣ"]  # 21 글자
		third_letter = ["", "ㄱ", "ㄲ", "ㄳ", "ㄴ", "ㄵ", "ㄶ", "ㄷ", "ㄹ", "ㄺ", "ㄻ", "ㄼ", "ㄽ", "ㄾ", "ㄿ", "ㅀ", "ㅁ", "ㅂ", "ㅄ",
		                "ㅅ",
		                "ㅆ", "ㅇ", "ㅈ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"]  # 28 글자, 없는것 포함
		one_byte_data = text.encode("utf-8")
		no_1 = int(one_byte_data[0])
		no_2 = int(one_byte_data[1])
		no_3 = int(one_byte_data[2])

		new_no_1 = (no_1 - 234) * 64 * 64
		new_no_2 = (no_2 - 128) * 64
		new_no_3 = (no_3 - 128)

		bite_no = [no_1, no_2, no_3]  # 바이트번호인 16진수를 10진수로 나타낸것
		bite_no_1 = [new_no_1, new_no_2, new_no_3]  # 바이트번호를 각 자릿수에 맞도록 1자리 숫자로 만들기 위해 변경한것

		value_sum = new_no_1 + new_no_2 + new_no_3

		value = value_sum - 3072  # 1의자리에서부터 시작하도록 만든것
		temp_num_1 = divmod(value, 588)  # 초성이 몇번째 자리인지를 알아내는것
		temp_num_2 = divmod(temp_num_1[1], 28)  # 중성과 종성의 자릿수를 알아내는것것

		chosung = first_letter[divmod(value, 588)[0]]  # 초성
		joongsung = second_letter[divmod(temp_num_1[1], 28)[0]]  # 중성
		jongsung = third_letter[temp_num_2[1]]  # 종성

		step_letter = [temp_num_1[1], temp_num_2[0], temp_num_2[1]]  # 초성, 중성, 종성의 자릿수
		chojoongjong = [chosung, joongsung, jongsung]  # 초성, 중성, 종성의 글자

		# print("encode한 것 ==> ", one_byte_data)
		# print("바이트번호를 각 자릿수에 맞도록 1자리 숫자로 만들기 위해 변경한것 ==> ", bite_no_1)
		# print("입력한 한글 한글자는 ==> ", text)
		# print("초성, 중성, 종성의 자릿수 ==> ", step_letter)
		# print("초성, 중성, 종성의 글자 ==> ", chojoongjong)

		return [chojoongjong, step_letter, bite_no, value, one_byte_data]

	def split_hangul_to_jamo(self, text):
		# 한글자의 한글을 자음과 모음으로 구분해 주는것
		one_byte_data = text.encode("utf-8")
		value_sum = 0
		char_type = ""

		if str(text) in "0123456789":
			char_type = "숫자"

		# compile_1 = re.compile("\d")
		# if str(text) in re.:
		#    char_type = "숫자"

		compile_1 = re.compile("\d+")
		no = compile_1.findall(text)

		try:
			no_1 = int(one_byte_data[0])
			no_2 = int(one_byte_data[1])
			no_3 = int(one_byte_data[2])
			new_no_1 = (no_1 - 234) * 64 * 64
			new_no_2 = (no_2 - 128) * 64
			new_no_3 = (no_3 - 128)
			value_sum = new_no_1 + new_no_2 + new_no_3

			if value_sum >= -28367 and value_sum <= -28338:
				char_type = "ja_only"
			if value_sum >= -28337 and value_sum <= -28317:
				char_type = "mo_only"

		except:
			char_type = "no_han"
			# 이것은 영어나 숫자, 특수문자라는 뜻이다
			no_1 = one_byte_data
			no_2 = ""
			no_3 = ""

		return [char_type, text]

	def change_list2d_to_dic_by_title(self, list_2d, list_title):
		# 2차원리스트를 제목과 연결해서 사전을 만들어서 다음에 편하게 쓰고 넣을수있도록 만들려고 한다
		result = []
		for one in list_2d:
			my_dic = {}
			for no in range(len(list_title)):
				my_dic[list_title[no]] = one[no]
			result.append(my_dic)
		return result

	def read_file_by_filename(self, filename):
		try:
			f = open(filename, 'r',encoding='UTF-8')
			result = f.readlines()
			f.close()
		except:
			f = open(filename, 'r')
			result = f.readlines()
			f.close()

		return result

	def change_upper_value (self, data):
		for a in range(len(data)):
			data[a] = string.upper(data[a])
		return data

	def delete_contineous_value (self, input_datas):
		if len(input_datas) == 0:
			#print ("아무자료도 없읍니다. 확인 바랍니다")
			pass
		else:
			a = 0
			while a!= len(input_datas)-1:
				if input_datas[a] == input_datas[a+1]: input_datas[a] = []
				a = a+1
		return input_datas

	def delete_holsu_value (self, data):
			for a in range(len(data)):
				if (a%2) == 0:
					data[a] = []
			return data

	def delete_odd_value (self, data):
		for a in range(len(data)):
			if (a%2) == 0:
				data[a] = []
		return data

	def sort (self, a,b = 0):
		result_before = [(i[b], i) for i in a]
		result_before.sort()
		result = [i[1] for i in result_before]
		return result

	def sort_datas_on(self, input_datas):
			result = []
			for one_data in input_datas:
				for one in one_data:
					result.append(one.sort())
			return result

	def read_sum_value (self, data):
		total = 0
		for a in data:
			total = total+a
		eval = total / len(data)
		return [total, eval, len(data), max(data), min(data)]

	def delete_step_value (self, data, num):
		data.insert(0,[])
		for a in range(len(data)):
			if (a%num) == 0 :
				data[a] = []
		result = data[1:]
		return result

	def insert_value_by_step(self, input_datas, number = 1, input_data = []):
		total_number = len(input_datas)
		dd = 0
		for a in range(len(input_datas)):
			if a % number == 0 and a != 0:
				if total_number != a:
					input_datas.insert(dd, input_data)
					dd = dd + 1
			dd = dd + 1
		return input_datas

	def delete_same_value_in_list (self, input_datas, status = 0):
		if status == 0:
			result = []
			#계속해서 pop으로 하나씩 없애므로 하나도 없으면 그만 실행한다
			while len(input_datas)!= 0:
				gijun = input_datas.pop()
				sjpark = 0
				result.append(gijun)
				for number in range(len(input_datas)):
					if input_datas[int(number)] == [] : #빈자료일때는 그냥 통과한다
						pass
					if input_datas[int(number)] == gijun :#자료가 같은것이 있으면 []으로 변경한다
						sjpark = sjpark+1
						input_datas[int(number)] = []
			else:
				#중복된것중에서 아무것도없는 []마저 없애는 것이다. 위의 only_one을 이용하여 사용한다
				#같은것중에서 하나만 남기고 나머지는 []으로 고친다
				#이것은 연속된 자료만 기준으로 삭제를 하는 것입니다
				#만약 연속이 되지않은 같은자료는 삭제가 되지를 않읍니다
				result = list(self.delete_only_one(input_datas))
				for a in range(len(result)-1,0,-1):
					if result[a] == []:
						del result[int(a)]
		return result



	def get_biff_record(self):
		height = self.height
		options = 0x00
		if self.bold:
			options |= 0x01
			self._weight = 0x02BC
		if self.italic:
			options |= 0x02
		if self.underline != self.UNDERLINE_NONE:
			options |= 0x04
		if self.struck_out:
			options |= 0x08
		if self.outline:
			options |= 0x010
		if self.shadow:
			options |= 0x020
		colour_index = self.colour_index
		weight = self._weight
		escapement = self.escapement
		underline = self.underline
		family = self.family
		charset = self.charset
		name = self.name
		#return BIFFRecords.FontRecord(height, options, colour_index, weight, escapement,
		#			underline, family, charset,
		#			name)
	def read_file_as_2_types(self, file_full_name):
		file_object = open(file_full_name, "r", encoding="UTF-8")
		file_as_list = file_object.readlines()
		file_object.close()
		one_file = ""
		for one in file_as_list:
			one_file = one_file + one
		return [file_as_list, one_file]

	def write_file(self, file_full_name, source_data):
		"""
		텍스트자료를 화일로 저장하는것
		"""
		new_file = open(file_full_name, "r", encoding="UTF-8")
		for one in source_data:
			new_file.write(one)

	def delete_all_explanation(self, input_text):
		"""
		넘어온 text에서 주석으로 사용되는 것들을 지우는것
		"""
		input_text = re.sub(re.compile(r"[\s]*#.*[\n]"), "\n", input_text)
		input_text = re.sub(re.compile(r"[\s]*'''.*?'''", re.DOTALL|re.MULTILINE), "", input_text)
		input_text = re.sub(re.compile(r'[\s]*""".*?"""', re.DOTALL|re.MULTILINE), "", input_text)
		input_text = re.sub(re.compile(r"[\n][\s]*?[\n]"), "\n", input_text)
		return input_text

	def split_method_and_delete_empty_line(self, filename):
		"""
		화일의 메소드를 기준으로 나누면서 동시에 빈라인은 삭제하는것
		"""
		def_list = []
		result = []
		total_code = ""
		total = ""
		# 화일을 읽어온다
		f = open(filename, 'r', encoding='UTF8')
		original_lines = f.readlines()
		f.close()
		print(len(original_lines))
		num = 1
		temp = ""
		exp_start = ""
		exp_end = ""
		exp_mid = ""
		for one_line in original_lines:
			total = total + one_line
			changed_one_line = one_line.strip()
			if changed_one_line == "":
				one_line = ""
			elif changed_one_line[0] == "#":
				one_line = ""
			elif changed_one_line[0:3] == "def":
				def_list.append(temp)
				temp = one_line
			elif '"""' in changed_one_line:
				if changed_one_line[0:3] == '"""':
					exp_end = "no"
					exp_start = "yes"
					one_line = ""
				elif changed_one_line[:-3] == '"""':
					if exp_mid == "yes":
						exp_mid = "no"
					else:
						exp_end = "yes"
						exp_start = "no"
						one_line = ""
				else:
					if exp_mid == "yes":
						exp_mid = "no"
					else:
						exp_mid = "yes"

				num = num +1

			if exp_start == "yes" and exp_end == "no":
				one_line = ""

			temp = temp + one_line
			total_code = total_code + one_line
		print(num)

		return [def_list, total_code, total]

	def save_pickle_data(self, source_data = "", file_name = "", path = "D:\\"):
		"""
		자료를 pickle 로 저장하는것
		"""
		if "." in file_name:
			file_name = file_name +".sjp"
		with open(path+file_name, "wb") as fr:
			pickle.dump(source_data, fr)

	def make_list_unique(self, input_data):
		"""
		리스트의 값중 고유한것만 골라내기
		"""
		temp = set()
		for one in input_data:
			temp.add(one)
		result = list(temp)
		return result

	def get_file_list_from_directorty(self, directory):
		#file_list = os.listdir(directory)
		#print("file_list: {}".format(directory))
		#file_list = glob.glob(directory)
		#file_list_py = [file for file in file_list if file.endswith("")]
		filenames = os.listdir(directory)
		#for filename in filenames:
		#	full_filename = os.path.join(directory, filename)
			#print("화일 명 ==== >", full_filename)
		return filenames

	def change_encoding_type_of_file(self, path, filename, original_type="EUC-KR", new_type="UTF-8", new_filename=""):
		"""
		#텍스트가 안 읽혀져서 확인해보니 인코딩이 달라서 안되어져서
		#이것으로 전체를 변경하기위해 만듦
		"""
		full_path = path + "\\" + filename
		full_path_changed = path + "\\" + new_filename + filename
		try:
			aaa = open(full_path, 'rb')
			result = chardet.detect(aaa.read())
			# print(result['encoding'], filename)
			aaa.close()

			if result['encoding'] == original_type:
				# print("화일의 인코딩은 ======> {}, 화일이름은 {} 입니다".format(original_type, filename))
				aaa = open(full_path, "r", encoding=original_type)
				file_read = aaa.readlines()
				aaa.close()

				new_file = open(full_path_changed, mode='w', encoding=new_type)
				for one in file_read:
					new_file.write(one)
				new_file.close()
		except:
			print("화일이 읽히지 않아요=====>", filename)

		path = "C:\Python39-32\Lib\site-packages\myez_xl\myez_xl_test_codes"
		file_lists = os.listdir(path)
		for one_file in file_lists:
			self.change_encoding_type_of_file(path, one_file, "EUC-KR", "UTF-8", "_changed")


	def read_monitors_properties(self):
		# 연결된 모니터들의 속성을 알려준다
		result = {}
		sub_result = {}
		num = 0
		for m in screeninfo.get_monitors():
			num = num + 1
			# print(m)
			sub_result["x"] = m.x
			sub_result["y"] = m.y
			sub_result["height_mm"] = m.height_mm
			sub_result["width_mm"] = m.width_mm
			sub_result["height"] = m.height
			sub_result["width"] = m.width
			sub_result["primary"] = m.is_primary
			sub_result["name"] = m.name
			name = "monitor" + str(num)
			result[name] = sub_result
		return result


	def check_hangul_jamo(self, text):
		# 한글자의 한글을 자음과 모음으로 구분해 주는것
		one_byte_data = text.encode("utf-8")
		value_sum = 0
		char_type = ""

		if str(text) in "0123456789":
			char_type = "숫자"

		# compile_1 = re.compile("\d")
		# if str(text) in re.:
		#    char_type = "숫자"

		compile_1 = re.compile("\d+")
		no = compile_1.findall(text)

		try:
			no_1 = int(one_byte_data[0])
			no_2 = int(one_byte_data[1])
			no_3 = int(one_byte_data[2])
			new_no_1 = (no_1 - 234) * 64 * 64
			new_no_2 = (no_2 - 128) * 64
			new_no_3 = (no_3 - 128)
			value_sum = new_no_1 + new_no_2 + new_no_3

			if value_sum >= -28367 and value_sum <= -28338:
				char_type = "ja_only"
			if value_sum >= -28337 and value_sum <= -28317:
				char_type = "mo_only"

		except:
			char_type = "no_han"
			# 이것은 영어나 숫자, 특수문자라는 뜻이다
			no_1 = one_byte_data
			no_2 = ""
			no_3 = ""

		return [char_type, text]

	def change_value_sort (self, a,b = 0):
		result_before = [(i[b], i) for i in a]
		result_before.sort()
		result = [i[1] for i in result_before]
		return result


	def moum_xy_list(self, size=[1, 2], input_text="ㅏ"):
		# 모음을 엑셀에 나타내기 위한 좌표를 주는 것이다
		x, y = size
		# x, y는 글자의 크기
		mo_01 = [["ㅏ"], [1, 0.6 * y, x, 0.6 * y],
		         [0.4 * x, 0.6 * y, 0.4 * x, 0.8 * y]]
		mo_02 = [["ㅑ"], [1, 0.6 * y, x, 0.6 * y],
		         [0.4 * x, 0.6 * y, 0.4 * x, 0.8 * y],
		         [0.6 * x, 0.6 * y, 0.6 * x, 0.8 * y]]
		mo_03 = [["ㅓ"], [1, 0.6 * y, x, 0.6 * y],
		         [0.4 * x, 0.4 * y, 0.4 * x, 0.6 * y]]
		mo_04 = [["ㅕ"], [1, 0.6 * y, x, 0.6 * y],
		         [0.4 * x, 0.4 * y, 0.4 * x, 0.6 * y],
		         [0.6 * x, 0.4 * y, 0.6 * x, 0.6 * y]]
		mo_10 = [["ㅣ"], [1, 0.6 * y, x, 0.6 * y]]
		mo_05 = [["ㅗ"], [x, 1, x, y],
		         [x, 0.5 * y, 0.8 * x, 0.5 * y]]
		mo_06 = [["ㅛ"], [x, 1, x, y],
		         [x, 0.3 * y, 0.8 * x, 0.3 * y],
		         [x, 0.7 * y, 0.8 * x, 0.7 * y]]
		mo_07 = [["ㅜ"], [1, 1, 1, y],
		         [1, 0.5 * y, 0.5 * x, 0.5 * y]]
		mo_08 = [["ㅠ"], [1, 1, 1, y],
		         [1, 0.3 * y, 0.8 * x, 0.3 * y],
		         [1, 0.7 * y, 0.8 * x, 0.7 * y]]
		mo_09 = [["ㅡ"], [0.5 * x, 1, 0.5 * x, y]]

		mo_21 = [["ㅐ"], [1, 0.6 * y, x, 0.6 * y],
		         [1, 0.8 * y, x, 0.8 * y],
		         [0.4 * x, 0.6 * y, 0.4 * x, 0.8 * y]]
		mo_22 = [["ㅒ"], [1, 0.6 * y, x, 0.6 * y],
		         [1, 0.8 * y, x, 0.8 * y],
		         [0.4 * x, 0.6 * y, 0.4 * x, 0.6 * y],
		         [0.6 * x, 0.8 * y, 0.6 * x, 0.8 * y]]
		mo_23 = [["ㅔ"], [1, 0.6 * y, x, 0.6 * y],
		         [1, 0.8 * y, x, 0.8 * y],
		         [0.4 * x, 0.4 * y, 0.4 * x, 0.6 * y]]
		mo_24 = [["ㅖ"], [1, 0.6 * y, x, 0.6 * y],
		         [1, 0.8 * y, x, 0.8 * y],
		         [0.4 * x, 0.4 * y, 0.4 * x, 0.6 * y],
		         [0.6 * x, 0.4 * y, 0.6 * x, 0.6 * y]]

		jamo2_dic = {
			"ㅏ": mo_01, "ㅑ": mo_02, "ㅓ": mo_03, "ㅕ": mo_04, "ㅗ": mo_05,
			"ㅛ": mo_06, "ㅜ": mo_07, "ㅠ": mo_08, "ㅡ": mo_09, "ㅣ": mo_10,
			"ㅐ": mo_21, "ㅒ": mo_22, "ㅔ": mo_23, "ㅖ": mo_24,
		}
		result = jamo2_dic[input_text]
		return result


	def jaum_xy_list(self, size=[1, 2], input_text="ㄱ"):
		x, y = size
		# x, y는 글자의 크기
		ja_01 = [["ㄱ"], [1, 1, 1, y], [1, y, x, y]]
		ja_02 = [["ㄴ"], [1, 1, x, 1], [x, 1, x, y]]
		ja_03 = [["ㄷ"], [1, y, 1, 1], [1, 1, x, 1], [x, 1, x, y]]
		ja_04 = [["ㄹ"], [1, 1, 1, y], [1, y, 0.5 * x, y], [0.5 * x, y, 0.5 * x, 1], [0.5 * x, 1, x, 1], [x, 1, x, y]]
		ja_05 = [["ㅁ"], [1, 1, 1, y], [1, y, x, y], [x, y, x, 1], [x, 1, 1, 1]]
		ja_06 = [["ㅂ"], [1, 1, x, 1], [x, 1, x, y], [x, y, 1, y], [0.5 * x, 1, 0.5 * x, y]]
		ja_07 = [["ㅅ"], [1, 0.5 * y, 0.3 * x, 0.5 * y], [0.3 * x, 0.5 * y, x, 1], [0.3 * x, 0.5 * y, x, y]]
		ja_08 = [["ㅇ"], [0.8 * x, 0.2 * y, 0.8 * x, 0.8 * y], [0.8 * x, 0.8 * y, 0.6 * x, y, ""],
		         [0.6 * x, y, 0.2 * x, y], [0.2 * x, y, 1, 0.8 * y, "/"], [1, 0.8 * y, 1, 0.2 * y],
		         [1, 0.2 * y, 0.2 * x, 1, ""], [0.2 * x, 1, 0.6 * x, 1], [0.6 * x, 1, 0.8 * x, 0.2 * y, "/"]]
		ja_09 = [["ㅈ"], [1, 1, 1, y], [1, 0.5 * y, 0.5 * x, 0.5 * y], [0.5 * x, 0.5 * y, x, 1, "/"],
		         [0.5 * x, 0.5 * y, x, y, ""]]
		ja_10 = [["ㅊ"], [0.2 * x, 0.5 * y, 1, 0.5 * y], [0.2 * x, 1, 0.2 * x, y], [0.2 * x, 0.5 * y, 0.4 * x, 0.5 * y],
		         [1, 0.5 * y, 0.5 * x, 0.5 * y], [0.5 * x, 0.5 * y, x, 1], [0.5 * x, 0.5 * y, x, y, ""]]
		ja_11 = [["ㅋ"], [1, 1, 1, y], [1, y, x, y], [0.5 * x, 1, 0.5 * x, y]]
		ja_12 = [["ㅌ"], [1, y, 1, 1], [1, 1, x, 1], [x, 1, x, y], [0.5 * x, 1, 0.5 * x, y]]
		ja_13 = [["ㅍ"], [1, 1, 1, y], [x, 1, x, y], [1, 0.2 * y, x, 0.2 * y], [1, 0.8 * y, x, 0.8 * y]]
		ja_14 = [["ㅎ"], [1, 0.5 * y, 0.2 * x, 0.5 * y], [0.2 * x, 1, 0.2 * x, y], [0.4 * x, 0.3 * y, 0.4 * x, 0.8 * y],
		         [0.4 * x, 0.8 * y, 0.6 * x, y], [0.6 * x, y, 0.8 * x, y], [0.8 * x, y, x, 0.8 * y],
		         [x, 0.8 * y, x, 0.3 * y], [x, 0.3 * y, 0.8 * x, 1], [0.8 * x, 1, 0.6 * x, 1],
		         [0.6 * x, 1, 0.4 * x, 0.3 * y]]
		ja_31 = [["ㄲ"], [1, 1, 1, 0.4 * y], [1, 0.4 * y, x, 0.4 * y], [1, 0.7 * y, 1, y], [1, y, x, y], ]
		ja_32 = [["ㄸ"], [1, 1, 1, 0.4 * y], [1, 1, x, 1], [x, 1, x, 0.4 * y], [1, 0.7 * y, 1, y],
		         [1, 0.7 * y, x, 0.7 * y], [x, 0.7 * y, x, y], ]
		ja_33 = [["ㅃ"], [1, 1, x, 1], [x, 1, x, 0.4 * y], [x, 0.4 * y, 1, 0.4 * y], [0.5 * x, 1, 0.5 * x, 0.4 * y],
		         [1, 0.7 * y, x, 0.7 * y], [x, 0.7 * y, x, y], [x, y, 1, y], [0.5 * x, 0.7 * y, 0.5 * x, y], ]
		ja_34 = [["ㅆ"], [1, 0.3 * y, 0.4 * x, 0.3 * y], [0.4 * x, 0.3 * y, x, 1], [0.4 * x, 0.3 * y, x, 0.5 * y],
		         [1, 0.8 * y, 0.4 * x, 0.8 * y], [0.4 * x, 0.8 * y, x, 0.6 * y], [0.4 * x, 0.8 * y, x, y], ]
		ja_35 = [["ㅉ"], [1, 1, 1, 0.5 * y], [1, 0.3 * y, 0.4 * x, 0.3 * y], [0.4 * x, 0.3 * y, x, 1],
		         [0.4 * x, 0.3 * y, x, 0.5 * y], [1, 0.6 * y, 1, y], [1, 0.8 * y, 0.4 * x, 0.8 * y],
		         [0.4 * x, 0.8 * y, x, 0.6 * y], [0.4 * x, 0.8 * y, x, y], ]
		ja_36 = [["ㄳ"], [1, 1, 1, 0.4 * y], [1, 0.4 * y, x, 0.4 * y], [1, 0.8 * y, 0.4 * x, 0.8 * y],
		         [0.4 * x, 0.8 * y, x, 0.6 * y], [0.4 * x, 0.8 * y, x, y], ]
		ja_37 = [["ㄵ"], [1, 1, x, 1], [x, 1, x, 0.4 * y], [1, 0.6 * y, 1, y], [1, 0.8 * y, 0.4 * x, 0.8 * y],
		         [0.4 * x, 0.8 * y, x, 0.6 * y], [0.4 * x, 0.8 * y, x, y], ]
		ja_38 = [["ㄶ"], [1, 1, x, 1], [x, 1, x, 0.4 * y], [0.1 * x, 0.8 * y, 1, 0.8 * y],
		         [0.2 * x, 0.6 * y, 0.2 * x, y], [0.4 * x, 0.7 * y, 0.4 * x, 0.9 * y], [0.4 * x, 0.9 * y, 0.6 * x, y],
		         [0.6 * x, y, x, 0.9 * y], [x, 0.9 * y, x, 0.7 * y], [x, 0.7 * y, 0.8 * x, 0.6 * y],
		         [0.8 * x, 0.6 * y, 0.6 * x, 0.6 * y], [0.6 * x, 0.6 * y, 0.4 * x, 0.7 * y]]
		ja_39 = [["ㄺ"], [1, 1, 1, 0.4 * y], [1, 0.4 * y, 0.5 * x, 0.4 * y], [0.5 * x, 0.4 * y, 0.5 * x, 1],
		         [0.5 * x, 1, x, 1], [x, 1, x, 0.4 * y], [1, 0.7 * y, 1, y], [1, y, x, y], ]
		ja_40 = [["ㄻ"], [1, 1, 1, 0.4 * y], [1, 0.4 * y, 0.5 * x, 0.4 * y], [0.5 * x, 0.4 * y, 0.5 * x, 1],
		         [0.5 * x, 1, x, 1], [x, 1, x, 0.4 * y], [1, 0.7 * y, 1, y], [1, y, x, y], [x, y, x, 0.7 * y],
		         [x, 0.7 * y, 1, 0.7 * y], ]
		ja_41 = [["ㄼ"], [1, 1, 1, 0.4 * y], [1, 0.4 * y, 0.5 * x, 0.4 * y], [0.5 * x, 0.4 * y, 0.5 * x, 1],
		         [0.5 * x, 1, x, 1], [x, 1, x, 0.4 * y], [1, 0.7 * y, x, 0.7 * y], [x, 0.7 * y, x, y], [x, y, 1, y],
		         [0.5 * x, 0.7 * y, 0.5 * x, y], ]
		ja_42 = [["ㄽ"], [1, 1, 1, 0.4 * y], [1, 0.4 * y, 0.5 * x, 0.4 * y], [0.5 * x, 0.4 * y, 0.5 * x, 1],
		         [0.5 * x, 1, x, 1], [x, 1, x, 0.4 * y], [1, 0.8 * y, 0.4 * x, 0.8 * y], [0.4 * x, 0.8 * y, x, 0.6 * y],
		         [0.4 * x, 0.8 * y, x, y], ]
		ja_43 = [["ㄾ"], [1, 1, 1, 0.4 * y], [1, 0.4 * y, 0.5 * x, 0.4 * y], [0.5 * x, 0.4 * y, 0.5 * x, 1],
		         [0.5 * x, 1, x, 1], [x, 1, x, 0.4 * y], [1, 0.7 * y, 1, y], [1, 0.7 * y, x, 0.7 * y],
		         [x, 0.7 * y, x, y], [0.5 * x, 0.7 * y, 0.5 * x, y], ]
		ja_44 = [["ㄿ"], [1, 1, 1, 0.4 * y], [1, 0.4 * y, 0.5 * x, 0.4 * y], [0.5 * x, 0.4 * y, 0.5 * x, 1],
		         [0.5 * x, 1, x, 1], [x, 1, x, 0.4 * y], [1, 0.6 * y, 1, y], [x, 0.6 * y, x, y],
		         [1, 0.7 * y, x, 0.7 * y], [1, 0.9 * y, x, 0.9 * y], ]
		ja_45 = [["ㅀ"], [1, 1, 1, 0.4 * y], [1, 0.4 * y, 0.5 * x, 0.4 * y], [0.5 * x, 0.4 * y, 0.5 * x, 1],
		         [0.5 * x, 1, x, 1], [x, 1, x, 0.4 * y], [0.1 * x, 0.8 * y, 1, 0.8 * y], [0.2 * x, 0.6 * y, 0.2 * x, y],
		         [0.4 * x, 0.7 * y, 0.4 * x, 0.9 * y], [0.4 * x, 0.9 * y, 0.6 * x, y], [0.6 * x, y, x, 0.9 * y],
		         [x, 0.9 * y, x, 0.7 * y], [x, 0.7 * y, 0.8 * x, 0.6 * y], [0.8 * x, 0.6 * y, 0.6 * x, 0.6 * y],
		         [0.6 * x, 0.6 * y, 0.4 * x, 0.7 * y]]
		ja_46 = [["ㅄ"], [1, 1, x, 1], [x, 1, x, 0.4 * y], [x, 0.4 * y, 1, 0.4 * y], [0.5 * x, 1, 0.5 * x, 0.4 * y],
		         [1, 0.8 * y, 0.4 * x, 0.8 * y], [0.4 * x, 0.8 * y, x, 0.6 * y], [0.4 * x, 0.8 * y, x, y], ]

		jamo1_dic = {"ㄱ": ja_01, "ㄴ": ja_02, "ㄷ": ja_03, "ㄹ": ja_04, "ㅁ": ja_05,
		             "ㅂ": ja_06, "ㅅ": ja_07, "ㅇ": ja_08, "ㅈ": ja_09, "ㅊ": ja_10,
		             "ㅋ": ja_11, "ㅌ": ja_12, "ㅍ": ja_13, "ㅎ": ja_14,
		             "ㄲ": ja_31, "ㄸ": ja_32, "ㅃ": ja_33, "ㅆ": ja_34, "ㅉ": ja_35,
		             "ㄳ": ja_36, "ㄵ": ja_37, "ㄶ": ja_38, "ㄺ": ja_39, "ㄻ": ja_40,
		             "ㄼ": ja_41, "ㄽ": ja_42, "ㄾ": ja_43, "ㄿ": ja_44, "ㅀ": ja_45, "ㅄ": ja_46,
		             }

		result = jamo1_dic[input_text]
		return result


	def swap(self, a, b):
		# a,b를 바꾸는 함수이다
		t = a
		a = b
		b = t
		return [a, b]



	def change_column_value(self, temp_title):
		"""
		화일의 제목으로 사용이 불가능한것을 제거한다
		"""
		for temp_01 in [[" ", "_"], ["(", "_"], [")", "_"], ["/", "_per_"], ["%", ""], ["'", ""], ['"', ""], ["$", ""], ["__", "_"], ["__", "_"]]:
			temp_title = temp_title.replace(temp_01[0], temp_01[1])
		if temp_title[-1] == "_": temp_title = temp_title[:-2]
		return


	def text_encoding_data(self, text, encoding_type):
		byte_data = text.encode(encoding_type)
		hex_data_as_str = " ".join("{0}".format(hex(c)) for c in byte_data)
		int_data_as_str = " ".join("{0}".format(int(c)) for c in byte_data)

		print("\"" + text + "\" 전체 문자 길이: {0}".format(len(text)))
		print("\"" + text + "\" 전체 문자를 표현하는 데 사용한 바이트 수: {0} 바이트".format(len(byte_data)))
		print("\"" + text + "\" 16진수 값: {0}".format(hex_data_as_str))
		print("\"" + text + "\" 10진수 값: {0}".format(int_data_as_str))
		# 사용법 : text_encoding_data("Hello", "utf-8")
		return int_data_as_str


	def read_method_code(self, str_method_name):
		# 메소드의 코드를 읽어오는것
		# 문자료 넣을수있도록 만든 것이다

		method_name = eval(str_method_name)
		code_text = inspect.getsource(method_name)
		return code_text