# -*- coding: utf-8 -*-
import os
import sqlite3
import pandas as pd
from halmoney import youtil, pcell

vars = {}

class anydb:
	def __init__(self, db_name="", path=""):
		"""
		databse가 있는 화일의 위치를 알려주면 시작이 된다
		pandas의 장점
		1. 대용량 데이터(GB 단위 이상)를 다룰 수 있습니다. 엑셀은 데이터 용량이 100MB을 넘어가거나, 데이터가 100만 행이 넘어가면 정상적으로 작동하지 않는 현상을 겪기도 합니다.
		2. 복잡한 처리 작업들을 비교적 손쉽게 할 수 있습니다. 소위 말하는 엑셀 노가다를 할 필요가 없습니다.
		3. 손쉽게 데이터를 결합하고 분리할 수 있습니다. SQL처럼 데이터를 합치고 관계 연산을 수행할 수 있습니다.

		df.index, df.columns, df.values
		df["col1"], df[1:3]

		index는 숫자만 가능하지 않고, String(문자열) 일 수도 있다.
		index가 숫자여도 순서대로 정렬될 필요가 없다. 그리고 index는 중복될 수 있다.
		print(df.loc[:3, ['Surv', 'N']])

		df[val]	Select single column or sequence of columns from the DataFrame
		df.loc[val]	Selects single row or subset of rows from the DataFrame by label
		df.loc[:, val]	Selects single column or subset of columns by label
		df.loc[val1, val2]	Select both rows and columns by label
		df.iloc[where]	Selects single row or subset of rows from the DataFrame by integer position
		df.iloc[:, where]	Selects single column or subset of columns by integer position
		df.iloc[where_i, whe	re_j] Select both rows and columns by integer position
		df.at[label_i, label	_j] Select a single scalar value by row and column label
		df.iat[i, j]	Select a single scalar value by row and column position (integers)
		get_value(), set_val	ue() Select single value by row and column label
		"""
		self.yt = youtil.youtil()
		self.db_name = db_name
		self.table_name = ""

		self.con = ""
		self.curs = ""
		self.path = path
		self.connect_db(db_name, path)

	def add_df1_to_df2(self, input_df_1, input_df_2):
		"""
		input_df_1의 자료에 input_df_2를 맨끝에 추가하는것
		"""
		input_df_1 = pd.concat([input_df_1, input_df_2])
		return input_df_1

	def change_df_to_dic(self, input_df, style="split"):
		"""
		입력형태 : data = {"calory": [123, 456, 789], "기간": [10, 40, 20]}
		출력형태 : dataframe
		"""
		checked_style = style
		if not style in ["split", "list", 'series', 'records', 'index']:
			checked_style = "split"
		result = input_df.to_dict(checked_style)
		return result

	def change_list_to_df(self, list2d="", col_list=""):
		"""
		리스트 자료를 dataframe로 만드는것
		입력형태 : 제목리스트, 2차원 값리스트형
		출력형태 : dataframe로 바꾼것
		"""
		checked_list2d = self.yt.change_list1d_to_list2d(list2d)
		checked_col_list = []
		#컬럼의 이름이 없거나하면 기본적인 이름을 만드는 것이다
		if col_list == "" or col_list == []:
			for num in range(len(checked_list2d)):
				checked_col_list.append("col"+str(num))
		else:
			checked_col_list = col_list
		input_df = pd.DataFrame(data=checked_list2d, columns=col_list)
		return input_df

	def change_table_name(self, table_name_old, table_name_new):
		"""
		입력형태 :
		출력형태 :
		"""
		new_sql = "alter table %s rename to %s" % (table_name_old, table_name_new)
		self.run_sql(new_sql)

	def change_tabledata_to_df(self, db_name, table_name):
		"""
		sqlite를 df로 만드는것
		입력형태 :
		출력형태 :
		"""
		if self.con == "":
			self.con = sqlite3.connect(db_name, isolation_level=None)
		self.curs = self.con.cursor()
		sql = ("SELECT * From {}").format(table_name)
		query = self.curs.execute(sql)
		cols = [column[0] for column in query.description]
		input_df = pd.DataFrame.from_records(data=query.fetchall(), columns=cols)
		return input_df

	def change_tabledata_to_list(self, db_name, table_name):
		"""
		sqlite를 df로 만드는것
		입력형태 :
		출력형태 :[2차원리스트(제목), 2차원리스트(값들)]
		"""
		if self.con == "":
			self.con = sqlite3.connect(db_name, isolation_level=None)
		self.con.row_factory = sqlite3.Row
		self.curs = self.con.cursor()
		sql = "SELECT * From {}".format(table_name)
		query = self.curs.execute(sql)
		cols = [column[0] for column in query.description]

		aaa = []
		for one in query.fetchall():
			aaa.append(list(one))
		result =[cols, aaa]
		return result

	def check_col_name(self, col_name):
		for data1, data2 in [["'", ""], ["/", ""], ["\\", ""], [".", ""]]:
				col_name = col_name.replace(data1, data2)
		return col_name

	def check_db_name(self, db_name, path="."):
		"""
		database는 파일의 형태이므로 폴더에서 화일이름들을 확인한다
		입력형태 :
		출력형태 :
		"""
		result = False
		db_name_all = self.yt.read_filename_folder_all(path)
		if db_name in db_name_all:
			result = True
		else:
			print("db_name을 다시 확인하세요")
			result = None
		return result

	def check_df_range(self, input_list):
		"""
		내가만든 입력형태를 사용할수있도록 만든것
		입력형태 : ["3~4"], ["all"],[1,2,3,4], [3:4]
		출력형태 : [3:4], [:], [1:4], [3:4]
		"""
		result = self.yt.check_df_range(input_list)
		return result

	def connect_db(self, db_name=""):
		"""
		입력형태 :
		출력형태 :
		"""
		#기본적으로 test_db.db를 만든다
		#memory로 쓰면, sqlite3를 메모리에 넣도록 한다
		if db_name == "memory":
			self.connect_db_in_memory(db_name)
		#데이터베이스를 넣으면 화일로 만든다
		elif self.db_name == "" or self.db_name == "test":
			self.db_name = "test_db.db"
			self.con = sqlite3.connect(self.db_name, isolation_level=None)
		else:
			self.con = sqlite3.connect(self.db_name, isolation_level=None)
		self.curs = self.con.cursor()

	def connect_db_in_memory(self, table_name=""):
		"""
		#self.curs.execute("CREATE TABLE " + self.table_name + " (auto_no integer primary key AUTOINCREMENT)")
		입력형태 :
		출력형태 :
		"""
		self.db_name = "memory_db"
		self.con = sqlite3.connect(":memory:")
		self.con = sqlite3.connect(self.db_name, isolation_level=None)
		print("DB이름은 ==> ", self.db_name)

	def connect_db_with_table_name(self, db_name="", table_name=""):
		"""
		입력형태 :
		출력형태 :
		"""
		self.connect_db(db_name)
		self.make_table(table_name)

	def delete_columns(self, table_name, col_name_list):
		"""
		컬럼을 삭제한다
		입력형태 : ["col_1","col_2","col_3"]
		"""
		if col_name_list:
			for col_name in col_name_list:
				sql = ("ALTER TABLE %s DROP COLUMN %s " % (table_name, col_name))
				self.curs.execute(sql)

	def delete_df_emptycolumn(self, input_df):
		"""
		dataframe의 빈열을 삭제
		제목이 있는 경우에만 해야 문제가 없을것이다
		"""
		nan_value = float("NaN")
		input_df.replace(0, nan_value, inplace=True)
		input_df.replace("", nan_value, inplace=True)
		input_df.dropna(how="all", axis=1, inplace=True)
		return input_df

	def delete_empty_column(self, table_name):
		"""
		테이블의 컬럼중에서 아무런 값도 없는 컬럼을 삭제한다
		입력형태 :
		출력형태 :
		"""
		col_list = []
		for column_data in self.read_col_name_all(table_name):
			sql = ("select COUNT(*) from %s where %s is not null" % (table_name, column_data))
			self.curs.execute(sql)
			if self.curs.fetchall()[0][0] == 0:
				col_list.append(column_data)
		self.delete_columns()

	def delete_table(self, table_name):
		"""
		입력형태 : 테이블이름
		"""
		self.curs.execute("DROP TABLE " + table_name)

	def insert_cols(self, table_name, col_data_list):
		"""
		새로운 컬럼을 만든다
		입력형태 : 테이블이름, [["이름1","int"],["이름2","text"]]
		출력형태 :
		"""
		for col_name, col_type in col_data_list:
			col_name = self.check_col_name(col_name)
			self.curs.execute("alter table %s add column '%s' '%s'" % (table_name, col_name, col_type))

	def make_database(self, db_name):
		"""
		새로운 데이터베이스를 만든다
		입력형태 : 이름
		"""
		self.db_name = db_name
		new_sql = "CREATE DATABASE %s;" % (self.db_name)
		print(new_sql)

	def make_table(self, table_name):
		"""
		새로운 테이블을 만든다
		입력형태 : 테이블이름
		"""
		tables = []
		self.curs.execute("select name from sqlite_master where type = 'table'; ")
		for one_table_name in self.curs.fetchall():
			tables.append(one_table_name[0])
		if not table_name in tables:
			self.curs.execute("CREATE TABLE " + table_name + " (Item text)")

	def make_table_with_column(self, table_name, column_data_list):
		"""
		어떤 형태의 자료가 입력이 되어도 테이블을 만드는 sql을 만드는 것이다
		입력형태 1 : 테이블이름, [['번호1',"text"], ['번호2',"text"],['번호3',"text"],['번호4',"text"]]
		입력형태 2 : 테이블이름, ['번호1','번호2','번호3','번호4']
		입력형태 3 : 테이블이름, [['번호1',"text"], '번호2','번호3','번호4']
		입력형태 :
		출력형태 :
		"""

		sql_1 = "CREATE TABLE IF NOT EXISTS {}".format(table_name)
		sql_2 = sql_1 + " ("
		for one_list in column_data_list:
			if type(one_list) == type([]):
				if len(one_list)== 2:
					col_name = one_list[0]
					col_type = one_list[1]
				elif len(one_list) == 1:
					col_name = one_list[0]
					col_type = "text"
			elif type(one_list) == type("string"):
				col_name = one_list
				col_type = "text"
			sql_2 = sql_2 + "{} {}, ".format(col_name, col_type)
		sql_2 = sql_2[:-2] + ")"
		self.curs.execute(sql_2)
		return sql_2

	def pick_unique__table_col_names__new_col_names(self, table_name, col_names):
		"""
		기존 테이블의 컬럼중에서 새로운 컬럼이름이 고유한것만 추출
		입력형태 :
		출력형태 :
		"""
		result = []
		columns = self.read_col_name_all(table_name)
		update_col_names = self.yt.change_waste_data(col_names)
		for one_col_name in update_col_names:
			if not one_col_name.lower() in columns:
				result.append(one_col_name)
		return result

	def read_col_name_all(self, table_name=""):
		"""
		해당하는 테이의 컬럼구조를 갖고온다
		입력형태 : 테이블이름
		출력형태 : 컬럼이름들
		"""
		if table_name =="":
			table_name = self.table_name
		self.curs.execute("PRAGMA table_info('%s')" % table_name)
		result = []
		for temp_2 in self.curs.fetchall():
			result.append(temp_2[1].lower())
		return result

	def read_colproperty_all_for_table(self, table_name):
		"""
		해당하는 테이블의 컬럼의 모든 구조를 갖고온다
		입력형태 :
		출력형태 :
		"""

		self.curs.execute("PRAGMA table_info('%s')" % table_name)
		result = []
		for temp_2 in self.curs.fetchall():
			result.append(temp_2)
		return result

	def read_db_name_all(self, path=".\\"):
		"""
		모든 database의 이름을 갖고온다
		모든이 붙은것은 맨뒤에 all을 붙인다
		입력형태 :
		출력형태 :
		"""
		result = []
		for fname in os.listdir(path):
			if fname[-3:] ==".db":
				result.append(fname)
		return result

	def read_table_data(self, table_name=""):
		"""
		테이블의 모든 자료를 읽어온다
		입력형태 : 테이블 이름
		출력형태 :
		"""
		self.curs.execute(("select * from {}").format(table_name))
		result = self.curs.fetchall()
		return result

	def read_table_data_by_col_names(self, col_name_s="", condition="all"):
		"""
		문자는 컬럼이름으로, 숫자는 몇번째인것으로...
		입력형태 :
		출력형태 :
		"""
		if col_name_s == "":
			sql_columns = "*"
		else:
			sql_columns = self.yt.chain_list1d_text_word(col_name_s, ", ")

		if condition=="all":
			lim_no = 100
		else:
			lim_no = condition
		limit_text = "limit {}".format(lim_no)
		sql = "SELECT {} FROM {} ORDER BY auto_no {}".format(sql_columns, self.table_name, limit_text)
		self.curs.execute(sql)
		result = self.curs.fetchall()
		return result

	def read_table_data_from_no1_to_no2(self, table_name, offset=0, row_count=100):
		"""
		테이블의 자료중 원하는 갯수만 읽어오는 것
		입력형태 :
		출력형태 :
		"""
		self.curs.execute(("select * from %s LIMIT %s, %s;") % (table_name, str(offset), str(row_count)))
		result = self.curs.fetchall()
		return result

	def read_table_names(self):
		"""
		해당하는 테이의 컬럼구조를 갖고온다
		입력형태 : 데이터베이스 이름
		출력형태 : 테이블이름들
		"""
		self.curs.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
		result = []
		for temp_2 in self.curs.fetchall():
			result.append(temp_2[0])
		return result

	def run_sql(self, sql):
		"""
		입력형태 :
		출력형태 :
		"""
		self.curs.execute(sql)
		result = self.curs.fetchall()
		self.con.commit()
		return result

	def save_memorydb_to_diskdb(self, db_name):
		"""
		memory에 저장된것을 화일로 저장하는것
		python 3.7부터는 backup이 가능
		입력형태 :
		출력형태 :
		"""
		db_disk = sqlite3.connect(db_name)
		self.con.backup(db_disk)

	def split_path_n_name(self, input_value=""):
		"""
		입력값을 경로와 이름으로 분리
		"""
		file_name = ""
		path = ""
		input_value = input_value.replace("/", "\\")
		temp_1 = input_value.split("\\")
		if "." in temp_1[-1]:
			file_name = temp_1[-1]
		if len(temp_1) >1 and "\\" in temp_1[:len(temp_1[-1])]:
			path = input_value[:len(temp_1[-1])]
		result = [file_name, path]
		return result

	def write_data_to_sqlite_table(self, table_name, col_name_s, col_value_s):
		"""
		입력형태 :
		출력형태 :
		"""
		sql_columns = ""
		sql_values = ""
		for column_data in col_name_s:
			sql_columns = sql_columns + column_data + ", "
			sql_values = "?," * len(col_name_s)
		sql = "insert into %s(%s) values (%s)" % (table_name, sql_columns[:-2], sql_values[:-1])
		if type(col_value_s[0]) == type([]):
			self.curs.executemany(sql, col_value_s)
		else:
			self.curs.execute(sql, col_value_s)
		self.con.commit()

	def write_df_to_excel(self, input_df, xy = [1,1]):
		"""
		df자료를 커럼과 값을 기준으로 나누어서 결과를 돌려주는 것이다
		입력형태 :
		출력형태 :
		"""
		col_list = input_df.columns.values.tolist()
		value_list = input_df.values.tolist()
		excel=pcell.pcell()
		excel.write_value("", xy, [col_list])
		excel.dump_value("", [xy[0]+1, xy[1]], value_list)

	def write_df_to_sqlite(self, table_name, df_data):
		"""
		df자료를 sqlite에 새로운 테이블로 만들어서 넣는 것
		입력형태 :
		출력형태 :
		"""
		df_data.to_sql(table_name, self.con)

	def write_dic_to_table(self, dic_data):
		"""
		사전의 키를 y이름으로 해서 값을 입력한다
		입력형태 :
		출력형태 :
		"""
		for one_col in list(dic_data[0].keys()):
			if not one_col in self.read_col_name_all():
				self.new_y(one_col)
		sql_columns = self.yt.chain_list1d_text_word(list(dic_data[0].keys()), ", ")
		sql_values = "?," * len(list(dic_data[0].keys()))
		sql = "insert into %s (%s) values (%s)" % (self.table_name, sql_columns, sql_values[:-1])
		value_list = []
		for one_dic in dic_data:
			value_list.append(list(one_dic.values()))
		self.curs.executemany(sql, value_list)

	def write_list_to_table(self, table_name,col_name_s, list_values):
		"""
		리스트의 형태로 넘어오는것중에 y이름과 값을 분리해서 얻는 것이다
		입력형태 :
		출력형태 :
		"""
		sql_columns = self.yt.chain_list1d_text_word(col_name_s, ", ")
		sql_values = "?," * len(list_values[0])
		sql = "insert into %s (%s) values (%s)" % (table_name, sql_columns, sql_values[:-1])
		self.curs.executemany(sql, list_values)

	def write_table_data_to_df(self, table_name):
		"""
		sqlite를 df로 만드는것
		입력형태 :
		출력형태 :
		"""

		sql = "SELECT * From %s" % (table_name)
		query = self.cur.execute(sql)
		cols = [column[0] for column in query.description]
		input_df = pd.DataFrame.from_records(data=query.fetchall(), columns=cols)
		return input_df

	def append_df1_df2(self, df_obj_1, df_obj_2):
		"""
		dataframe의 끝에 dataframe로 만든 것을 맨끝에 추가하는것
		"""
		df_obj_1 = pd.concat([df_obj_1, df_obj_2])
		return df_obj_1

	def insert_df1_df2(self, df_obj_1, df_obj_2):
		"""
		df_obj_1의 자료에 df_obj_2를 맨끝에 추가하는것
		"""
		df_obj_1 = pd.concat([df_obj_1, df_obj_2])
		return df_obj_1

	def read_df_by_no(self, df_obj, x, y):
		"""
		숫자번호로 pandas의 dataframe의 일부를 불러오는 것
		단, 모든것을 문자로 넣어주어야 한다
		x=["1:2", "1~2"] ===> 1, 2열
		x=["1,2,3,4"] ===> 1,2,3,4열
		x=[1,2,3,4]  ===> 1,2,3,4열
		x=""또는 "all" ===> 전부
		"""

		x_list = self.check_df_range(x)
		y_list = self.check_df_range(y)
		exec("self.result = df_obj.iloc[{}, {}]".format(x_list, y_list))
		return self.result

	def read_df_by_xy(self, df_obj, xy=[0, 0]):
		"""
		위치를 기준으로 값을 읽어오는 것이다
		숫자를 넣으면 된다
		"""
		result = df_obj.iat[int(xy[0]), int(xy[1])]
		return result

	def read_df_by_name(self, df_obj, x, y):
		"""
		열이나 행의 이름으로 pandas의 dataframe의 일부를 불러오는 것이다
		이것은 리스트를 기본으로 사용한다
		list_x=["가"~"다"] ===> "가"~"다"열
		list_x=["가","나","다","4"] ===> 가,나,다, 4 열
		x=""또는 "all" ===> 전부
		"""

		temp = []
		for one in [x, y]:
			if ":" in one[0]:
				changed_one = one[0]
			elif "~" in one[0]:
				ed_one = one[0].split("~")
				changed_one = "'" + str(ed_one[0]) + "'" + ":" + "'" + str(ed_one[1]) + "'"

			elif "all" in one[0]:
				changed_one = one[0].replace("all", ":")
			else:
				changed_one = one
			temp.append(changed_one)
		# 이것중에 self를 사용하지 않으면 오류가 발생한다
		print(temp)
		exec("self.result = df_obj.loc[{}, {}]".format(temp[0], temp[1]))
		return self.result


	class sqlite:

		class db:
			def __init__(self, db_name=""):
				vars["db_name"] = db_name

			def change_col_name(self, table_name):
				"""
				공백을 _로 변경하는것, Column의 이름을 변경한다
				입력형태 :
				출력형태 :
				"""
				for column_data in self.read_col_name_all(table_name):
					column_data_new = column_data.replace(" ", "_")
					if not column_data_new == column_data:
						tem_2 = self.curs.execute(
							"alter table {} RENAME COLUMN {} to {}".format(table_name, column_data, column_data_new))

			def connect(self, db_name=""):
				vars["con"] = sqlite3.connect(db_name, isolation_level=None)
				vars["curs"] = vars["con"].cursor()

			def create(self, db_name=""):
				# 기본적으로 test_db.db를 만든다
				# memory로 쓰면, sqlite3를 메모리에 넣도록 한다

				vars["db_name"] = db_name

				if vars["db_name"] == "memory":
					self.connect_db_in_memory(db_name)
				# 데이터베이스를 넣으면 화일로 만든다
				elif vars["db_name"] == "" or vars["db_name"] == "test":
					vars["db_name"] = "test_db.db"
					vars["con"] = sqlite3.connect(vars["db_name"], isolation_level=None)
				else:
					vars["con"] = sqlite3.connect(vars["db_name"], isolation_level=None)
				vars["curs"] = vars["con"].cursor()

			def connect_db_in_memory(self, table_name=""):
				vars["db_name"] = "memory_db"
				vars["con"] = sqlite3.connect(":memory:")
				vars["con"] = sqlite3.connect(vars["db_name"], isolation_level=None)

			class table:
				def __init__(self, table_name=""):
					vars["table_name"] = table_name

				def create_table(self, table_name):
					tables = []
					self.curs.execute("select name from sqlite_master where type = 'table'; ")
					for one_table_name in self.curs.fetchall():
						tables.append(one_table_name[0])
					if not table_name in tables:
						self.curs.execute("CREATE TABLE " + table_name + " (Item text)")

				def insert_cols(self, table_name, col_data_list):
					"""
					새로운 컬럼을 만든다
					입력형태 : 테이블이름, [["이름1","int"],["이름2","text"]]
					출력형태 :
					"""
					for one_list in col_data_list:
						if type(one_list) ==type([]):
							col_name = self.check_col_name(one_list[0])
							col_type = one_list[1]
						else:
							col_name = self.check_col_name(one_list)
							col_type = "text"
						vars["curs"].execute("alter table %s add column '%s' '%s'" % (table_name, col_name, col_type))

				def check_col_name(self, col_name):
					for data1, data2 in [["'", ""], ["/", ""], ["\\", ""], [".", ""]]:
							col_name = col_name.replace(data1, data2)
					return col_name

				def write_data(self, table_name, col_name_s, col_value_s):
					sql_columns = ""
					sql_values = ""
					for column_data in col_name_s:
						sql_columns = sql_columns + column_data + ", "
						sql_values = "?," * len(col_name_s)
					sql = "insert into %s(%s) values (%s)" % (table_name, sql_columns[:-2], sql_values[:-1])
					if type(col_value_s[0]) == type([]):
						vars["curs"].executemany(sql, col_value_s)
					else:
						vars["curs"].execute(sql, col_value_s)
					vars["con"].commit()