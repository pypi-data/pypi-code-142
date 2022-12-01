# -*- coding: utf-8 -*-
import re

class scolor:

	def __init__(self):
		self.check_color_name = {
			"빨": "red", "적": "red", "빨강": "red","red": "red", "r": "red",
			"주": "ora", "주황": "ora", "오렌지": "ora","yr": "ora", "yellowred": "ora","yellow_red": "ora", "yellow red": "ora", "o": "ora", "orange": "ora", "ora": "ora",
			"노": "yel", "노랑": "yel","y": "yel", "yellow": "yel", "yel": "yel",
			"연": "gy", "연두": "gy", "gy": "gy", "greenyellow": "gy", "green_yellow": "gy", "green yellow": "gy", "green-yellow": "gy", "yg": "gy",
			"초": "gre", "초록": "gre","g": "gre", "green": "gre", "gre": "gre", "녹색": "gre",
			"연초록": "gc", "greencyan": "gc", "green_cyan": "gc", "green cyan": "gc", "cg": "gc", "gc": "gc",
			"옥": "cya", "옥색": "cya", "c": "cya", "cya": "cya", "cyan": "cya",
			"청록": "bc", "청": "bc", "bluecyan": "bc", "blue_cyan": "bc", "blue cyan": "bc", "cb": "bc", "bg": "bc", "bluegreen": "bc", "bc": "bc",
			"파": "blu", "파랑": "blu", "b": "blu", "blue": "blu", "blu": "blu",
			"남": "bm", "남색": "bm","bluemagenta": "bm", "blue_magenta": "bm", "blue magenta": "bm", "bm": "bm", "pb": "bm", "purpleblue": "bm", "purple_blue": "bm", "purple blue": "bm", "violet": "bm", "vio": "bm",
			"보": "mag", "magenta": "mag", "m": "mag", "보라": "mag", "mag": "mag",
			"자홍": "rm", "자주": "rm","redmagenta": "rm", "red_magenta": "rm", "red magenta": "rm", "rm": "rm", "mr": "rm",
			"회": "gra", "회색": "gra", "gra": "gra", "gray": "gra",
			"흰": "whi", "하양": "whi", "흰색": "whi","white": "whi", "whi": "whi",
			"검": "bla", "검정": "bla", "흑": "bla", "black": "bla", "bla": "bla",
			"핑크":"pin","분홍":"pin","pink":"pin",
		}
		self.dic_colorname_hnum = {"red": 0, "ora": 30, "yel": 60, "gy": 90, "gre": 120, "gc": 150 , "cya": 180, "bc": 210, "blu": 240, "bm": 270, "mag": 300, "rm": 330, "gra": 0, "whi": 0, "bla": 0, }

		self.color_name_k_set = ["빨강", "주황", "노랑", "연두", "초록", "연초록", "옥색", "청록", "파랑", "남색", "보라", "자홍", "회색", "흰색", "검정", "분홍"]
		self.color_name_e_set = ["red", "ora", "yel", "gy", "gre", "gc" , "cya", "bc", "blu", "bm", "mag", "rm", "gra", "whi", "bla",]
		self.get_h_no_by_color_name_e = {"red": 0, "ora": 30, "yel": 60, "gy": 90, "gre": 120, "gc": 150 , "cya": 180, "bc": 210, "blu": 240, "bm": 270, "mag": 300, "rm": 330, "gra": 0, "whi": 0, "bla": 0, }
		self.rgb_12_set = [[255, 0, 0],[255, 128, 0],[255, 255, 0],[128, 255, 0],
										[0, 255, 0],[0, 255, 128],[0, 255, 255],[0, 128, 255],
										[0, 0, 255],[128, 0, 255],[255, 0, 255],[255, 0, 128],]

		self.check_pccs_name = {"v": "v", "b": "b", "s": "s", "dp": "dp", "lt": "lt", "sf": "sf",
		                                       "d": "d", "dk": "dk", "p": "p", "ltg": "ltg", "g": "g", "dkg": "dkg",
		                                       "vivid": "v", "bright": "b", "strong": "s", "deep": "dp", "light": "lt",
		                                       "soft": "sf", "dull": "d", "dark": "dk", "pale": "p",
		                                       "lightgrayish": "ltg", "grayish": "g", "darkgrayish": "dkg",
		                                       "viv": "v", "bri": "b", "str": "s", "dee": "dp", "lig": "lt",
		                                       "sof": "sf", "dul": "d", "dar": "dk", "pal": "p", "gra+": "ltg",
		                                       "gra": "g", "gra-": "dkg",
		                                       "선명한": "v", "밝은": "b", "강한": "s", "짙은": "dp", "옅은": "lt", "부드러운": "sf",
		                                       "둔한": "d", "어두운": "dk", "연한": "p", "밝은회색조": "ltg", "회색조": "g",
		                                       "어두운회색조": "dkg"}
		self.get_hsl_by_color_name_e = {
			"gra":[0,0,50],	"whi":[0,0,100],"bla":[0,0,0],	"red":[0,100,50],
			"ora": [30, 100,50],"yel": [60, 100,50],"gy": [90, 100,50],	"gre": [120, 100,50],
			"gc": [150, 100,50],"cya": [180, 100,50],"bc": [210, 100,50],"blu": [240, 100,50],
			"bm": [270, 100,50],"mag": [300, 100,50],"rm": [330, 100,50],"pin": [326, 100, 46],
		}
		self.list_colorstyle_eng = ["white", "pale", "light", "soft", "vivid", "dull", "deep", "dark", "black", "gray"]
		self.pccs_sl_set = [[90, 50], [80, 30], [80, 50], [80, 70], [50, 20], [50, 40], [50, 60], [50, 80], [20, 20], [20, 40], [20, 60], [20, 80]]

		self.excel_56rgb_set = [[0,0,0], [255,255,255], [255,0,0], [0,255,0], [0,0,255], [255,255,0],
										[255,0,255], [0,255,255], [128,0,0], [0,128,0], [0,0,128], [128,128,0],
										[128,0,128], [0,128,128], [192,192,192], [128,128,128], [153,153,255],
										[153,51,102], [255,255,204], [204,255,255], [102,0,102], [255,128,128],
										[0,102,204], [204,204,255], [0,0,128], [255,0,255], [255,255,0],
										[0,255,255], [128,0,128], [128,0,0], [0,128,128], [0,0,255],
										[0,204,255], [204,255,255], [204,255,204], [255,255,153], [153,204,255],
										[255,153,204], [204,153,255], [255,204,153], [51,102,255], [51,204,204],
										[153,204,0], [255,204,0], [255,153,0], [255,102,0], [102,102,153],
										[150,150,150], [0,51,102], [51,153,102], [0,51,0], [51,51,0],
										[153,51,0], [153,51,102], [51,51,153], [51,51,51]]

		self.basic_12hsl_set = [[0, 100, 50], [30, 100, 50], [60, 100, 50], [90, 100, 50], [120, 100, 50],
						                 [150, 100, 50], [180, 100, 50], [210, 100, 50], [240, 100, 50], [270, 100, 50],
						                 [300, 100, 50], [330, 100, 50]]

		self.johannes_hsl_set = [
			[[0, 100, 0], [0, 100, 10], [0, 100, 20], [0, 100, 30], [0, 100, 40], [0, 100, 50], [0, 100, 60], [0, 100, 70],
			 [0, 100, 80], [0, 100, 90], [0, 100, 100]],
			[[30, 100, 0], [30, 100, 10], [30, 100, 20], [30, 100, 30], [30, 100, 40], [30, 100, 50], [30, 100, 60],
			 [30, 100, 70], [30, 100, 80], [30, 100, 90], [30, 100, 100]],
			[[60, 100, 0], [60, 100, 10], [60, 100, 20], [60, 100, 30], [60, 100, 40], [60, 100, 50], [60, 100, 60],
			 [60, 100, 70], [60, 100, 80], [60, 100, 90], [60, 100, 100]],
			[[90, 100, 0], [90, 100, 10], [90, 100, 20], [90, 100, 30], [90, 100, 40], [90, 100, 50], [90, 100, 60],
			 [90, 100, 70], [90, 100, 80], [90, 100, 90], [90, 100, 100]],
			[[120, 100, 0], [120, 100, 10], [120, 100, 20], [120, 100, 30], [120, 100, 40], [120, 100, 50], [120, 100, 60],
			 [120, 100, 70], [120, 100, 80], [120, 100, 90], [120, 100, 100]],
			[[150, 100, 0], [150, 100, 10], [150, 100, 20], [150, 100, 30], [150, 100, 40], [150, 100, 50], [150, 100, 60],
			 [150, 100, 70], [150, 100, 80], [150, 100, 90], [150, 100, 100]],
			[[180, 100, 0], [180, 100, 10], [180, 100, 20], [180, 100, 30], [180, 100, 40], [180, 100, 50], [180, 100, 60],
			 [180, 100, 70], [180, 100, 80], [180, 100, 90], [180, 100, 100]],
			[[210, 100, 0], [210, 100, 10], [210, 100, 20], [210, 100, 30], [210, 100, 40], [210, 100, 50], [210, 100, 60],
			 [210, 100, 70], [210, 100, 80], [210, 100, 90], [210, 100, 100]],
			[[240, 100, 0], [240, 100, 10], [240, 100, 20], [240, 100, 30], [240, 100, 40], [240, 100, 50], [240, 100, 60],
			 [240, 100, 70], [240, 100, 80], [240, 100, 90], [240, 100, 100]],
			[[270, 100, 0], [270, 100, 10], [270, 100, 20], [270, 100, 30], [270, 100, 40], [270, 100, 50], [270, 100, 60],
			 [270, 100, 70], [270, 100, 80], [270, 100, 90], [270, 100, 100]],
			[[300, 100, 0], [300, 100, 10], [300, 100, 20], [300, 100, 30], [300, 100, 40], [300, 100, 50], [300, 100, 60],
			 [300, 100, 70], [300, 100, 80], [300, 100, 90], [300, 100, 100]],
			[[330, 100, 0], [330, 100, 10], [330, 100, 20], [330, 100, 30], [330, 100, 40], [330, 100, 50], [330, 100, 60],
			 [330, 100, 70], [330, 100, 80], [330, 100, 90], [330, 100, 100]]]

		self.faber_sl_set = [[[100, 0], [100, 50], [0, 0]],
					[[0, 0], [0, 75], [0, 100]],
					[[100, 0], [25, 75], [0, 100]],
					[[25, 0], [10, 50], [0, 75]],
					[[100, 0], [0, 0], [0, 100]],
					[[25, 0], [10, 50], [0, 75], [25, 75]], ]
		self.sl_step_small = {"1": [0, 12], "2": [0, 9], "3": [0, 6], "4": [0, 3], "5": [0, 0], "6": [0, -3], "7": [0, -6], "8": [0, -9], "9": [0, -12], "0": [0, -14],}

		self.sl_step = {"1": [100, 80], "2": [100, 77], "3": [100, 68], "4": [100, 59], "5": [100, 50], "6": [90, 41], "7": [80, 32], "8": [70, 23], "9": [60, 14] }
		self.dic_color_index = {"red":0, "ora":1, "yel":2, "yg":3, "gre":4, "gc":5, "cya":6, "cb":7, "blu":8, "bm":9, "mag":10, "mr":11, "gra":12, "whi":13, "bla":14}

		self.check_change_step = {
			55: "55", "55": "55", "ls": "55", "strong": "55", "s": "55", "강한": "55","기준": "55",
			0: "0", "0": "0", "l5": "0", "+++++": "0", "pale": "0", "p": "0", "pastel": "0", "파스텔": "0", "d5": "0",
			1: "1", "1": "1", "l4": "1", "++++": "1", "light grayish": "1", "ltg": "1", "d4": "1",
			2: "2", "2": "2", "l3": "2", "+++": "2", "light": "2", "lt": "2", "흐린": "2", "가벼운": "2", "d3": "2",
			3: "3", "3": "3", "l2": "3", "++": "3", "soft": "3", "sf": "3", "연한": "3", "d2": "3",
			4: "4", "4": "4", "l1": "4", "+": "4", "bright": "4", "b": "4", "밝은": "4", "d1": "4",
			5: "5", "5": "5", "l0": "5", "": "5", "vivid": "5", "v": "5", "선명한": "5", "basic": "5", "기본": "5", "d0": "5",
			6: "6", "6": "6", "l-1": "6", "-": "6", "deep": "6", "dp": "6", "진한": "6", "d-1": "6",
			7: "7", "7": "7", "l-2": "7", "--": "7", "dull": "7", "d": "7", "탁한": "7", "d-2": "7",
			8: "8", "8": "8", "l-3": "8", "---": "8", "dark": "8", "dk": "8", "어두운": "8", "d-3": "8",
			9: "9", "9": "9", "l-4": "9", "----": "9", "grayish": "9", "g": "9", "회색빛": "9",  "잿빛": "9", "d-4": "9",
			10: "10", "10": "10", "l-5": "10", "-----": "10", "dark grayish": "10", "dkg": "10", "어두운 회색": "10",  "d-5": "10",
			}

		self.list_basic_12h = [0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330]

		self.list_basic_10sl = [[100, 0], [90, 10], [80, 20], [70, 30],  [60, 40], [50, 50], [40, 60], [30, 70], [10, 80], [10, 90], [0, 100]]

		self.list_basic_11sl = [[100, 0], [100, 10], [100, 20], [100, 30], [100, 40], [100, 50], [100, 60], [100, 70], [100, 80],  [100, 90], [100, 100]]

		self.list_basic_12colorstyle = [[90, 50], [80, 30], [80, 50], [80, 70], [50, 20], [50, 40], [50, 60], [50, 80], [20, 20], [20, 40], [20, 60], [20, 80]]

		self.style = {"파스텔":0, "연한":1, "밝은":2, "흐린":3, "선명한":4, "기본":5, "탁한":6, "진한":7, "어두운":8, "회색":9, "검은":10, "검정":11}
		self.style_12 = [[90, 50, "파스텔"], [80, 30, "연한"], [80, 50,"밝은"], [80, 70, "흐린"], [50, 20, "선명한"], [50, 40, "기본"],
		            [50, 60, "탁한"], [50, 80, "진한"], [20, 20, "어두운"], [20, 40, "회색"], [20, 60, "검은"], [20, 80, "검정"]]
		self.color_mode = {"파스텔":9, "연한":8, "밝은":7, "흐린":6, "선명한":5, "탁한":4, "진한":3, "어두운":2, "회색":1,
									"white":9, "pale":8, "light":7, "soft":6, "vivid":5, "dull":4, "deep":3, "gray":2, "dark":1}
		self.color_mode_slno = [[90, 50], [80, 30], [80, 50], [80, 70], [50, 20], [50, 40], [50, 60], [50, 80], [20, 20], [20, 40], [20, 60], [20, 80]]

	def basic_12_rgb_pccs_style(self, hsl):
		"""
		12가지 스타일의 hsl을 돌려주는 것이다
		"""
		result = []
		for one_value in self.style_12:
			temp = self.change_hsl_to_rgb([hsl[0], one_value[0], one_value[1]])
			print("11111 ==> ", [hsl[0], one_value[0], one_value[1]], temp)
			result.append(temp)
		return result

	def basic_cool_color_name_set(self):
		"""
		차가운 색깔의 이름들
		"""
		result = ["파랑", "초록", "보라"]
		return result

	def basic_worm_color_name_set(self):
		"""
		따뜻한 색깔의 이름들
		"""
		result = ["빨강", "주황", "노랑"]
		return result

	def basic_56_excel_rgb_set(self):
		"""
		엑셀 기본 rgb 색 : 56색
		"""
		result = self.excel_56rgb_set
		return result

	def basic_8_pastel_rgb_set (self):
		"""
		기본적인
		자료가 있는 색들의 배경색으로 사용하면 좋은 색들
		"""
		color_set = self.basic_12hsl_set[:-4]
		result = []
		for hsl_value in color_set:
			rgb = self.control_hsl_with_style(hsl_value, "pastel", 4)
			result.append(rgb)
		return result

	def basic_13_color_name_eng_set(self):
		"""
		기본 13가지 색의 리스트 : 영어
		"""
		result = self.color_name_e_set
		return result

	def basic_13_color_name_kor_set(self):
		"""
		기본 13가지 색의 리스트 : 한글
		"""
		result = self.color_name_k_set
		return result

	def basic_12_hsl_set (self):
		"""
		360도의 색을 30도씩 12개로 구분한 hsl분류표
		"""
		result = self.basic_12hsl_set
		return result

	def basic_12_rgb_set (self):
		"""
		기본적으로 자장된 자료에서 갖고오는 것이다
		많이 사용하는 다른 색들을 사용하기 위해
		테두리, 폰트색이나 단색으로 나타낼때 사용하면 좋다
		"""
		result = self.rgb_12_set
		return result

	def basic_36_hsl_set (self):
		"""
		기본적인 hsl로된 36색을 갖고온다
		빨간색을 0으로하여 시작한다
		결과값 : hsl
		"""
		result = []
		for one in range(0, 360, 10):
			temp=[one, 100, 50]
			result.append(temp)
		return result

	def basic_faber_rgb_set(self, start_color=11, code = 5):
		"""
		파버 비덴의의 색체 조화론을 코드로 만든것이다
		한가지 색에대하 ㄴ조화를 다룬것
		# White(100-0) - Tone(10-50) - Color(0-0) : 색이 밝고 화사
		# Color(0-0) - Shade(0-75) - Black(0-100) : 색이 섬세하고 풍부
		# White(100-0) - GrayGray(25-75) - Black(0-100) : 무채색의 조화
		# Tint(25-0) - Tone(10-50) - Shade(0-75) 의 조화가 가장 감동적이며 세련됨
		# White(100-0) - Color(0-0) - Black(0-100) 는 기본적인 구조로 전체적으로 조화로움
		# Tint(25-0) - Tone(10-50) - Shade(0-75) - Gray(25-75) 의 조화는 빨강, 주황, 노랑, 초록, 파랑, 보라와 모두 조화를 이룬다
		"""
		h_list = self.list_basic_12h
		sl_faber = self.faber_sl_set

		h_no = h_list[start_color][0]
		result = []
		temp_hsl = sl_faber[code]
		for one_sl in temp_hsl:
			rgb = self.change_hsl_to_rgb([h_no, one_sl[0], one_sl[1]])
			result.append(rgb)
		return result

	def basic_johannes_rgb_set(self, start_color=11, num_color = 4, stongness = 5):
		"""
		요하네스 이텐의 색체 조화론을 코드로 만든것이다
		"""
		# start_color : 처음 시작하는 색 번호, 총 색은 12색으로 한다
		# num_color : 표현할 색의 갯수(2, 3, 4, 6만 사용가능)
		# stongness : 색의 농도를 나타내는 것, 검정에서 하양까지의 11단계를 나타낸것, 중간이 5이다
		h_list = self.list_basic_12h
		sl_list = self.list_basic_11sl
		hsl_johannes = self.johannes_hsl_set
		color_set = [[], [], [0, 6], [0, 5, 9], [0, 4, 7, 10], [0, 3, 5, 8, 10], [0, 3, 5, 7, 9, 11]]

		h_no = h_list[start_color][0]
		new_color_set = []
		for temp in color_set[num_color]:
			new_color_set.append((temp + int(h_no / 30)) % 12)

		result = []
		for no in new_color_set:
			temp_hsl = hsl_johannes[no][stongness]
			rgb = self.change_hsl_to_rgb(temp_hsl)
			result.append(rgb)
		return result

	def basic_12_pccs_style_eng_name_set(self):
		"""
		data로 시작하는 함수는 입력값이 없이 어떤 자료의 형태를 갖고오는 것이다
		pccs : 일본색체연구서가 빌표한 12가지 색으로 구분한것
		어떤 입력된 색의 기본적인 PCSS 12색을 돌려준다
		pccs톤, rgb로 넘어온 색을 pcss톤 12개로 만들어서 돌려준다
		"""
		result = self.list_colorstyle_eng
		return result

	def basic_12_style_name_set(self):
		"""
		스타일에 대한 이름을 갖고오는 것이다
		"""
		style = {"파스텔": 0, "연한": 1, "밝은": 2, "흐린": 3, "선명한": 4, "기본": 5, "탁한": 6, "진한": 7, "어두운": 8, "회색": 9, "검은": 10,
		         "검정": 11}
		result = list(style.keys())
		return result

	def basic_4356_hsl_set(self):
		"""
		h : 36가지
		s : 11단계
		l : 11단계
		총 4356개의 색집합
		"""
		result = {}
		for h in range(0, 360, 10):
			for s in range(0, 110, 10):
				for l in range(0, 110, 10):
					temp = self.change_hsl_to_rgb([h, s, l])
					result[str(h)+str("_")+str(s)+str("_")+str(l)] = temp
		return result

	def check_input_color(self, input_value):
		"""
		제일 처음으로 입력값을 확인하는 것이다
		#리스트형식이면 rgb나 hsl인데, 만약 분간이 안되면 hsl로 파악한다
		입력값 : rgb형식, hsl형식, scolor형식,
		"""
		hsl = self.check_input_type(input_value)
		return hsl

	def check_input_type(self, input_value):
		if type(input_value) == type("string"):
			hsl = self.change_scolor_to_hsl(input_value)
		elif type(input_value) == type(123):
			rgb = self.change_rgbint_to_rgb(input_value)
			hsl = self.change_rgb_to_hsl(rgb)
		elif type(input_value) == type([]) and len(input_value) == 3:
			if input_value[0] > 255:
				hsl = input_value
			else:
				if input_value[1]>100 or input_value[2] >100:
					hsl = self.change_rgb_to_hsl(input_value)
				else: hsl = input_value
		else:
			hsl = "error"
		return hsl

	def check_input_rgb(self, input_value):
		if type(input_value) == type(123):
			rgb = self.change_rgbint_to_rgb(input_value)
		else:
			rgb = input_value
		return rgb

	def check_input_scolor(self, input_scolor):
		"""
		scolor형식의 입력값을 확인하는 것이다
		입력값 : "red++"
		출력값 : ["숫자만","색이름","변화정도"] ==> ["","red","60"]
		"""
		number_only = ""
		color_name =""
		color_no = 0

		#색을 나타내는 글자를 추출해서,
		# 기본색이름으로 변경하는 것이다
		re_com1 = re.compile("[a-zA-Z가-힣]+")
		color_str = re_com1.findall(input_scolor)
		if color_str != []:
			color_name = self.check_color_name[color_str[0]]

		# 새롭게 정의해 보자
		#숫자로 정도를 표기한것인지를 알기위하여 숫자를 추출한다
		re_com2 = re.compile("[0-9]+")
		no_str = re_com2.findall(input_scolor)
		if no_str != []:
			color_no = int(no_str[0])
			if str(no_str[0]) == str(input_scolor):
					number_only = color_no
		#+나-를 추출하기위한 코드이다
		re_com3 = re.compile("[+]+")
		color_plus = re_com3.findall(input_scolor)
		if color_plus != []:
			color_no = 50 + 5 * len(color_plus[0])

		re_com4 = re.compile("[-]+")
		color_minus = re_com4.findall(input_scolor)
		if color_minus != []:
			color_no = 50 - 5 * len(color_minus[0])

		result = [number_only, color_name, color_no]
		return result

	def check_change_mode(self, change_mode):
		"""
		self.color_mode = {"파스텔":9, "연한":8, "밝은":7, "흐린":6, "선명한":5, "탁한":4, "진한":3, "어두운":2, "회색":1,
									"white":9, "pale":8, "light":7, "soft":6, "vivid":5, "dull":4, "deep":3, "gray":2, "dark":1}
		self.color_mode_slno = [[90, 50], [80, 30], [80, 50], [80, 70], [50, 20], [50, 40], [50, 60], [50, 80], [20, 20], [20, 40], [20, 60], [20, 80]]
		"""

		if type(change_mode) == type([]):
			result = change_mode
		elif "+" == str(change_mode)[0]:
			#현재의 값에서 10만큼 밝아지도록 한다
			l_value = 10 * len(change_mode)
			result = [0, 0, l_value]
		elif "-" == str(change_mode)[0]:
			#현재의 값에서 10만큼 어두워지도록 한다
			l_value = -10 * len(change_mode)
			result = [0, 0, l_value]
		elif change_mode in self.color_mode.keys():
			no = self.color_mode[change_mode]
			result = self.color_mode_slno[no]
		return result

	def change_scolor_to_hsl (self, input_scolor):
		"""
		입력형식 : scolor형식, 12, red45, red
		결과 : [h, s, l]
		입력된 자료를 기준으로 shl값을 돌려주는것
		"""
		if type(input_scolor) == type([]):
			if input_scolor[0] > 255:
				result = input_scolor
			else:
				if input_scolor[1]>100 or input_scolor[2] >100:
					result = self.change_rgb_to_hsl(input_scolor)
				else: result = input_scolor
		else:
			[number_only, color_name, color_step] = self.check_input_scolor(input_scolor)
			print("number_only ==> ", [number_only, color_name, color_step])

			if number_only != "":
				#만약 숫자만 입력을 햇다면, 엑셀 번호로 생각하는것
				r_no, g_no, b_no = self.excel_56rgb_set[int(number_only)]
			else:
				#색을 번호로 변경하는것
				color_index = self.check_color_name[color_name]

				if color_name =="whi" or color_name =="bla" or color_name =="gra":
					#만약 색이 흰색, 검정, 회색일경우는 h,s는 0으로 한다
					l_code_dic = {"bla": 0, "gra": 50, "whi": 100}
					h_code = 0
					s_code = 0
					l_code = int(l_code_dic[color_name]) + int(color_step)
				elif color_name and color_step == 0:
					# 기본색 인경우
					h_code, s_code, l_code = self.basic_12hsl_set[color_index]
				else:
					# 기타 다른 경우
					#print(color_name)
					#print(self.basic_12hsl_set)
					h_code = self.basic_12hsl_set[color_index]
					s_code = 100
					l_code = int(color_step)

				if int(l_code) > 100 : l_code = 100
				if int(l_code) < 0 : l_code = 0

			result = [h_code, s_code, l_code]
		return result

	def change_scolor_to_rgb (self, input_scolor):
		"""
		입력형식 : scolor형식, 12, red45, red
		결과 : [R, G, B]
		입력된 자료를 기준으로 rgb값을 돌려주는것 (숫자만이냐, 색이름, color_step)
		"""
		if type(input_scolor) == type([]):
			if input_scolor[0] > 255:
				final_rgb = input_scolor
			else:
				if input_scolor[1]>100 or input_scolor[2] >100:
					final_rgb = self.change_rgb_to_hsl(input_scolor)
				else: final_rgb = input_scolor
		else:
			[number_only, color_name, color_step] = self.check_input_scolor(input_scolor)

			if number_only != "":
				#만약 숫자만 입력을 햇다면, 엑셀 번호로 생각하는것
				r_no, g_no, b_no = self.excel_56rgb_set[int(number_only)]
			else:
				#색을 번호로 변경하는것
				#print(color_name)
				color_index = self.dic_color_index[color_name]

				if color_name =="whi" or color_name =="bla" or color_name =="gra":
					#만약 색이 흰색, 검정, 회색일경우는 h,s는 0으로 한다
					l_code_dic = {"bla": 0, "gra": 50, "whi": 100}
					h_code = 0
					s_code = 0
					l_code = int(l_code_dic[color_name]) + int(color_step)
				elif color_name and color_step == 0:
					# 기본색 인경우
					h_code, s_code, l_code = self.basic_12hsl_set[color_index]
				else:
					# 기타 다른 경우
					h_code = self.get_h_no_by_color_name_e[color_name]
					s_code = 100
					l_code = int(color_step)

				if int(l_code) > 100 : l_code = 100
				if int(l_code) < 0 : l_code = 0

			result = self.change_hsl_to_rgb([h_code, s_code, l_code])
			final_rgb = [result[0], result[1], result[2]]
		return final_rgb

	def change_hsl_to_rgb(self, hsl):
		"""
		hsl을 rgb로 바꾸는 것이다
		"""
		h, s, l = hsl
		print("hsl값은 ===>", h,s,l)
		h = float(h / 360)
		s = float(s / 100)
		l = float(l / 100)

		if s == 0:
			R = l * 255
			G = l * 255
			B = l * 255

		if l < 0.5:
			temp1 = l * (1 + s)
		else:
			temp1 = l + s - l * s

		temp2 = 2 * l - temp1

		#h = h / 360

		tempR = h + 0.333
		tempG = h
		tempB = h - 0.333

		if tempR < 0: tempR = tempR + 1
		if tempR > 1: tempR = tempR - 1
		if tempG < 0: tempG = tempG + 1
		if tempG > 1: tempG = tempG - 1
		if tempB < 0: tempB = tempB + 1
		if tempB > 1: tempB = tempB - 1

		if 6 * tempR < 1:
			R = temp2 + (temp1 - temp2) * 6 * tempR
		else:
			if 2 * tempR < 1:
				R = temp1
			else:
				if 3 * tempR < 2:
					R = temp2 + (temp1 - temp2) * (0.666 - tempR) * 6
				else:
					R = temp2

		if 6 * tempG < 1:
			G = temp2 + (temp1 - temp2) * 6 * tempG
		else:
			if 2 * tempG < 1:
				G = temp1
			else:
				if 3 * tempG < 2:
					G = temp2 + (temp1 - temp2) * (0.666 - tempG) * 6
				else:
					G = temp2
		if 6 * tempB < 1:
			B = temp2 + (temp1 - temp2) * 6 * tempB
		else:
			if 2 * tempB < 1:
				B = temp1
			else:
				if 3 * tempB < 2:
					B = temp2 + (temp1 - temp2) * (0.666 - tempB) * 6
				else:
					B = temp2
		R = int(abs(round(R * 255,0)))
		G = int(abs(round(G * 255,0)))
		B = int(abs(round(B * 255,0)))

		rgb_to_int = (int(B)) * (256 ** 2) + (int(G)) * 256 + int(R)
		return [R, G, B]

	def change_rgb_to_hex(self, rgb):
		"""
		엑셀의 Cells(1, i).Interior.Color는 hex값을 사용한다
		"""
		r, g, b = rgb[2], rgb[1], rgb[0]
		result = f"#{int(round(r)):02x}{int(round(g)):02x}{int(round(b)):02x}"
		return result

	def change_rgb_to_hsl (self, rgb_list):
		"""
		rgb를 hsl로 바꾸는 것이다
		입력은 0~255사이의 값
		"""
		r,g,b = rgb_list
		r = float(r / 255)
		g = float(g / 255)
		b = float(b / 255)
		max1 = max(r, g, b)
		min1 = min(r, g, b)
		l = (max1 + min1) / 2

		if max1 == min1:
			s = 0
		elif l < 0.5:
			s = (max1 - min1) / (max1 + min1)
		else:
			s = (max1 - min1) / (2 - max1 - min1)

		if s ==0:
			h = 0
		elif r >= max(g, b):
			h = (g - b) / (max1 - min1)
		elif g >= max(r, b):
				h = 2+ (b - r) / (max1 - min1)
		else:
				h = 4+ (r - g) / (max1 - min1)
		h = h *60
		if h > 360 : h = h -360
		if h < 0 : h = 360 -h

		return [int(h), int(s*100), int(l*100)]

	def change_rgb_to_rgbint(self, rgb_list):
		"""
		rgb인 값을 color에서 인식이 가능한 값으로 변경하는 것이다
		엑셀에서는 rgb랑 이 정수를 사용하여 색을 지정한다
		"""
		result =  int(rgb_list[0]) + (int(rgb_list[1])) * 256 + (int(rgb_list[2])) * (256 ** 2)
		return result

	def change_rgbint_to_rgb(self, input_int):
		"""
		int값을 rgb로 바꾸는 것이다
		"""
		mok0, namuji0 = divmod(input_int, 256*256)
		mok1, namuji1 = divmod(namuji0, 256)
		result = [namuji1, mok1, mok0]
		return result

	def change_rgbint_to_hsl(self, input_int):
		"""
		int값을 rgb로 바꾸는 것이다
		"""
		rgb = self.change_rgbint_to_rgb(input_int)
		hsl = self.change_rgb_to_hsl(rgb)
		return hsl

	def change_hsl_to_10_similar_color_set(self, hsl, step = 10):
		"""
		위쪽으로 5개, 아래로 5개의 채도가 비슷한 색을 돌려준다
		채도의 특성상 비슷한 부분이 많아서 10단위로 만든다
		"""
		h, s, l = hsl
		result = []
		for no in range(0,100+step,step):
			print("변경된 hsl은 s=> ", [h, no, l])
			temp = self.change_hsl_to_rgb([h, no, l])
			result.append(temp)
		return result

	def change_hsl_to_triangle_style(self, hsl):
		"""
		등간격 3색조합 : triad
		활동적인 인상과 이미지를 보인다
		"""
		h, s, l = hsl

		new_h_1 = divmod(h + 120, 360)[1]
		new_h_3 = divmod(h + 240, 360)[1]

		rgb_1 = self.change_hsl_to_rgb([new_h_1, s, l])
		rgb_2 = self.change_hsl_to_rgb(hsl)
		rgb_3 = self.change_hsl_to_rgb([new_h_3, s, l])
		result = [rgb_1, rgb_2, rgb_3]
		return result

	def change_hsl_to_bo_style(self, hsl):
		"""
		입력된 hsl의 보색을 알려주는것
		보색 : Complementary
		2차원 list의 형태로 돌려줌
		"""
		h, s, l = hsl
		new_h = divmod(h+180, 360)[1]
		result = self.change_hsl_to_rgb([new_h, s, l])
		return [result]

	def change_hsl_to_2near_style (self, hsl, h_step=36):
		"""
		근접색조합 : 양쪽 근처색
		"""
		h, s, l = hsl

		new_h_1 = divmod(h - h_step, 360)[1]
		new_h_3 = divmod(h + h_step, 360)[1]

		rgb_1 = self.change_hsl_to_rgb([new_h_1, s, l])
		rgb_2 = self.change_hsl_to_rgb(hsl)
		rgb_3 = self.change_hsl_to_rgb([new_h_3, s, l])
		result = [rgb_1, rgb_2, rgb_3]
		return result

	def change_hsl_to_4_tetra_style(self, hsl):
		"""
		4가지 꼭지의
		"""
		h, s, l = hsl

		new_h_1 = divmod(h + 0, 360)[1]
		new_h_2 = divmod(h + 90, 360)[1]
		new_h_3 = divmod(h + 180, 360)[1]
		new_h_4 = divmod(h + 270, 360)[1]
		rgb_1 = self.change_hsl_to_rgb([new_h_1, s, l])
		rgb_2 = self.change_hsl_to_rgb([new_h_2, s, l])
		rgb_3 = self.change_hsl_to_rgb([new_h_3, s, l])
		rgb_4 = self.change_hsl_to_rgb([new_h_4, s, l])
		result = [rgb_1, rgb_2, rgb_3, rgb_4]

		return result

	def change_hsl_to_2near_bo_style(self, hsl, h_step=36):
		"""
		근접보색조합 : 보색의 양쪽 근처색
		분열보색조합 : Split Complementary
		근접보색조합이라고도 한다. 보색의 강한 인상이 부담스러울때 보색의 근처에 있는 색을 사용
		2차원 list의 형태로 돌려줌
		"""
		h, s, l = hsl

		new_h_1 = divmod(h - h_step + 180, 360)[1]
		new_h_3 = divmod(h + h_step + 180, 360)[1]
		rgb_1 = self.change_hsl_to_rgb([new_h_1, s, l])
		rgb_2 = self.change_hsl_to_rgb(hsl)
		rgb_3 = self.change_hsl_to_rgb([new_h_3, s, l])
		result = [rgb_1, rgb_2, rgb_3]

		return result

	def change_hsl_by_high_l(self, hsl, high_l = 80):
		"""
		고명도의 hsl로 변경
		"""
		result = self.change_hsl_to_rgb([hsl[0], hsl[1], high_l])
		return [result]

	def change_hsl_by_middle_l(self, hsl, high_l = 50):
		"""
		중명도의 hsl로 변경
		"""
		result = self.change_hsl_to_rgb([hsl[0], hsl[1], high_l])
		return [result]

	def change_hsl_by_low_l(self, hsl, high_l = 20):
		"""
		저명도, 20%정도의 명도를 저명도로 말하자자
		"""
		result = self.change_hsl_to_rgb([hsl[0], hsl[1], high_l])
		return [result]

	def change_hsl_by_high_s(self, hsl, high_s = 80):
		#고채도
		result = self.change_hsl_to_rgb([hsl[0], high_s, hsl[2]])
		return [result]

	def change_hsl_by_middle_s(self, hsl, high_s = 50):
		#중채도
		result = self.change_hsl_to_rgb([hsl[0], high_s, hsl[2]])
		return [result]

	def change_hsl_by_low_s(self, hsl, high_s = 20):
		#저채도
		result = self.change_hsl_to_rgb([hsl[0], high_s, hsl[2]])
		return [result]

	def change_color_hsl(self, input_scolor):
		"""
		입력형식 : scolor형식, 12, red45, red
		결과 : [R, G, B]
		입력된 자료를 기준으로 rgb값을 돌려주는것 (숫자만이냐, 색이름, color_step)
		"""
		[number_only, color_name, color_step] = self.check_input_scolor(input_scolor)

		if number_only != "":
			# 만약 숫자만 입력을 햇다면, 엑셀 번호로 생각하는것
			r_no, g_no, b_no = self.excel_56rgb_set[int(number_only)]
		else:
			# 색을 번호로 변경하는것
			color_index = self.dic_color_index[color_name]

			if color_name == "whi" or color_name == "bla" or color_name == "gra":
				# 만약 색이 흰색, 검정, 회색일경우는 h,s는 0으로 한다
				l_code_dic = {"bla": 0, "gra": 50, "whi": 100}
				h_code = 0
				s_code = 0
				l_code = int(l_code_dic[color_name]) + int(color_step)
			elif color_name and color_step == 0:
				# 기본색 인경우
				h_code, s_code, l_code = self.basic_12hsl_set[color_index]
			else:
				# 기타 다른 경우
				h_code = self.list_basic_12h[color_name]
				s_code = 100
				l_code = int(color_step)

			if int(l_code) > 100: l_code = 100
			if int(l_code) < 0: l_code = 0

		result = [h_code, s_code, l_code]

		return result

	def change_color_to_rgb(self, input_scolor):
		"""
		입력형식 : scolor형식, 12, red45, red
		결과 : [R, G, B]
		입력된 자료를 기준으로 rgb값을 돌려주는것 (숫자만이냐, 색이름, color_step)
		"""
		[number_only, color_name, color_step] = self.check_input_scolor(input_scolor)

		if number_only != "":
			# 만약 숫자만 입력을 햇다면, 엑셀 번호로 생각하는것
			r_no, g_no, b_no = self.excel_56rgb_set[int(number_only)]
		else:
			# 색을 번호로 변경하는것
			# print(color_name)
			color_index = self.dic_color_index[color_name]

			if color_name == "whi" or color_name == "bla" or color_name == "gra":
				# 만약 색이 흰색, 검정, 회색일경우는 h,s는 0으로 한다
				l_code_dic = {"bla": 0, "gra": 50, "whi": 100}
				h_code = 0
				s_code = 0
				l_code = int(l_code_dic[color_name]) + int(color_step)
			elif color_name and color_step == 0:
				# 기본색 인경우
				h_code, s_code, l_code = self.basic_12hsl_set[color_index]
			else:
				# 기타 다른 경우
				h_code = self.dic_colorname_hnum[color_name]
				s_code = 100
				l_code = int(color_step)

			if int(l_code) > 100: l_code = 100
			if int(l_code) < 0: l_code = 0

		result = self.change_hsl_to_rgb([h_code, s_code, l_code])
		final_rgb = [result[0], result[1], result[2]]

		return final_rgb

	def change_color_to_rgb_with_style(self, input_scolor="red45", color_style="파스텔", style_step=5):
		"""
		입력된 기본 값을 스타일에 맞도록 바꾸고, 스타일을 강하게 할것인지 아닌것인지를 보는것
		color_style : pccs의 12가지 사용가능, 숫자로 사용가능, +-의 형태로도 사용가능
		입력예 : 기본색상, 적용스타일, 변화정도,("red45, 파스텔, 3)
		변화정도는 5를 기준으로 1~9까지임
		"""
		# 넘어온 자료중 color값을 hsl로 변경한다
		basic_hsl = self.change_color_hsl(input_scolor)
		# 스타일을 적용하는것
		step_2 = self.sl_step_small[color_style]
		# 스타일을 얼마나 강하게 적용할것인가를 나타내는것
		step_1 = self.sl_step[str(style_step)]

		h = int(basic_hsl[0])
		s = int(basic_hsl[1]) + int(step_1[1]) + int(step_2[1])
		l = int(basic_hsl[2]) + int(step_1[2]) + int(step_2[2])

		changed_rgb = self.change_hsl_to_rgb([h, s, l])
		return changed_rgb

	def change_excel56_to_rgb(self, input_no):
		"""
		엑셀 기본 rgb 색 : 56색
		"""
		result = self.excel_56rgb_set[int(input_no)]
		return result

	def change_hsl_to_3rgb_by_2near_bo(self, hsl, h_step=36):
		"""
		mode : 14
		근접보색조합 : 보색의 근처색
		분열보색조합 : Split Complementary
		근접보색조합이라고도 한다. 보색의 강한 인상이 부담스러울때 보색의 근처에 있는 색을 사용
		"""
		h, s, l = hsl

		new_h_1 = divmod(h - h_step + 180, 360)[1]
		new_h_3 = divmod(h + h_step + 180, 360)[1]

		hsl_1 = [new_h_1, s, l]
		hsl_3 = [new_h_3, s, l]
		result_rgb = self.change_hsl_to_rgb([hsl_1, hsl, hsl_3])
		return result_rgb

	def change_hsl_to_3rgb_as_like_0_120_240(self, hsl):
		"""
		mode :
		등간격 3색조합 : triad
		활동적인 인상과 이미지를 보인다
		"""
		h, s, l = hsl

		new_h_1 = divmod(h + 120, 360)[1]
		new_h_3 = divmod(h + 240, 360)[1]

		hsl_1 = [new_h_1, s, l]
		hsl_3 = [new_h_3, s, l]

		result_rgb = self.change_hsl_to_rgb([hsl_1, hsl, hsl_3])
		return result_rgb

	def change_hsl_to_bo_style_rgb(self, hsl):
		"""
		mode : 1
		보색 : Complementary
		"""
		h, s, l = hsl

		new_h_1 = h + 180
		if new_h_1 >= 360:
			new_h_1 = 360 - new_h_1

		result_rgb = self.change_hsl_to_rgb([new_h_1, s, l])
		return result_rgb

	def change_rgb_to_12_pccs_rgb_set(self, rgb):
		"""
		pccs : 일본색체연구서가 빌표한 12가지 색으로 구분한것
		어떤 입력된 색의 기본적인 PCSS 12색을 돌려준다
		pccs톤, rgb로 넘어온 색을 pcss톤 12개로 만들어서 돌려준다
		"""
		result = []
		h, s, l = self.change_rgb_to_hsl(rgb)
		result4 = self.color_name_e_set
		for one in result4:
			result.append([h, one[0], one[1]])
		return result

	def control_hsl_with_style (self, basic_hsl, color_style="파스텔", style_step = 5):

		step_2 = self.sl_step_small[color_style]
		step_1 = self.sl_step[str(style_step)]

		h = int(basic_hsl[0])
		s = int(basic_hsl[1]) + int(step_1[1]) + int(step_2[1])
		l = int(basic_hsl[2]) + int(step_1[2]) + int(step_2[2])

		changed_rgb = self.change_hsl_to_rgb([h,s,l])
		return changed_rgb

	def control_scolor_by_pccs_style (self, input_scolor="red45", color_style="파스텔", style_step = 5):
		"""
		입력된 기본 값을 스타일에 맞도록 바꾸고, 스타일을 강하게 할것인지 아닌것인지를 보는것
		color_style : pccs의 12가지 사용가능, 숫자로 사용가능, +-의 형태로도 사용가능
		입력예 : 기본색상, 적용스타일, 변화정도,("red45, 파스텔, 3)
		변화정도는 5를 기준으로 1~9까지임
		"""

		#넘어온 자료중 color값을 hsl로 변경한다
		basic_hsl = self.change_scolor_to_hsl(input_scolor)
		#스타일을 적용하는것
		step_2 = self.sl_step_small[color_style]
		#스타일을 얼마나 강하게 적용할것인가를 나타내는것
		step_1 = self.sl_step[str(style_step)]

		h = int(basic_hsl[0])
		s = int(basic_hsl[1]) + int(step_1[1]) + int(step_2[1])
		l = int(basic_hsl[2]) + int(step_1[2]) + int(step_2[2])

		changed_rgb = self.change_hsl_to_rgb([h,s,l])
		return changed_rgb

	def control_hsl_by_scolor_style(self, input_hsl, s_step="++", l_step="++"):
		"""
		sl의값을 조정하여 채도와 명도를 조절하는것
		입력형식 : hsl값을 올리거나 내리는 것
		입력 : [[36, 50, 50], "++", "--"]
		약 5씩이동하도록 만든다
		"""
		step_no = 5  # 5단위씩 변경하도록 하였다
		h, s, l = input_hsl

		if s_step == "":
			pass
		elif s_step[0] == "+":
			s = s + len(s_step) * step_no
			if s > 100: s = 100
		elif s_step[0] == "-":
			s = s - len(s_step) * step_no
			if s < 0: s = 0

		if l_step == "":
			pass
		elif l_step[0] == "+":
			l = l + len(l_step) * step_no
			if l > 100: l = 100
		elif l_step[0] == "-":
			l = l - len(l_step) * step_no
			if l < 0: l = 0

		result = self.change_hsl_to_rgb([h, s, l])
		return result

	def control_rgb_by_scolor_style(self, input_rgb, s_step="++", l_step="++"):
		input_hsl = self.change_rgb_to_hsl(input_rgb)
		step_no = 5  # 5단위씩 변경하도록 하였다
		h, s, l = input_hsl

		if s_step == "":
			pass
		elif s_step[0] == "+":
			s = s + len(s_step) * step_no
			if s > 100: s = 100
		elif s_step[0] == "-":
			s = s - len(s_step) * step_no
			if s < 0: s = 0

		if l_step == "":
			pass
		elif l_step[0] == "+":
			l = l + len(l_step) * step_no
			if l > 100: l = 100
		elif l_step[0] == "-":
			l = l - len(l_step) * step_no
			if l < 0: l = 0

		result = self.change_hsl_to_rgb([h, s, l])
		return result

	def change_hsl_to_36_hsl_by_h_step(self, hsl):
		"""
		위쪽으로 5개, 아래로 5개의 명도가 비슷한 색을 돌려준다
		"""
		h, s, l = hsl
		result = []
		for no in range(0, 36):
			result.append([no*10, s, l])
		return result

	def change_hsl_to_20_hsl_by_s_step(self, hsl):
		"""
		위쪽으로 5개, 아래로 5개의 명도가 비슷한 색을 돌려준다
		"""
		h, s, l = hsl
		result = []
		for no in range(0, 21):
			result.append([h, no*5, l])
		return result

	def change_hsl_to_20_hsl_by_l_step(self, hsl):
		"""
		위쪽으로 5개, 아래로 5개의 명도가 비슷한 색을 돌려준다
		"""
		h, s, l = hsl
		result = []
		for no in range(0, 21):
			result.append([h, s, no*5])
		return result

	def change_hsl_to_3_hsl_with_big_s_gab (self, hsl, s_step = 30):
		"""
		채도차가 큰 2가지 1가지색
		"""
		rgb_1 = self.change_hsl_to_rgb([hsl[0], s_step, hsl[2]])
		rgb_2 = self.change_hsl_to_rgb(hsl)
		rgb_3 = self.change_hsl_to_rgb([hsl[0], 100-s_step, hsl[2]])
		result = [rgb_1, rgb_2, rgb_3]
		return result

	def change_hsl_to_3_hsl_with_big_l_gab (self, hsl, l_step = 30):
		"""
		명도차가 큰 2가지 1가지색
		"""
		h, s, l = hsl
		rgb_1 = self.change_hsl_to_rgb([hsl[0], hsl[1], l_step])
		rgb_2 = self.change_hsl_to_rgb(hsl)
		rgb_3 = self.change_hsl_to_rgb([hsl[0], hsl[1], 100-l_step])
		result = [rgb_1, rgb_2, rgb_3]
		return result

	def get_rgb_by_excel_color_no(self, input_no):
		"""
		엑셀의 기본 번호를 넣으면 rgb값을 돌려주는것
		엑셀 기본 rgb 색 : 56색
		"""
		result = self.excel_56rgb_set[int(input_no)]
		return result

	def move_hsl_to_pastel_style(self, input_hsl, strong_level=0.5):
		"""
		입력받은 hsl값을 파스텔톤으로 적용시키는것
		bright = [100,100], sharp = [50,100], graish = [100,0], dark = [0,0], black = [50, 0]
		"""
		h, s, l = input_hsl
		style = pastel = [0,100]

		delta_s = (style[0] - s)*strong_level
		delta_l = (style[1] - l)*strong_level

		changed_s = s + delta_s
		changed_l = l + delta_l
		return [h, changed_s, changed_l]

	def move_hsl_to_bright_style(self, input_hsl, strong_level=0.5):
		"""
		입력받은 hsl값을 명도가 높은 쪽으로 이동시키는것
		bright = [100,100], sharp = [50,100], graish = [100,0], dark = [0,0], black = [50, 0]
		"""
		h, s, l = input_hsl
		style = bright = [100,100]

		delta_s = (style[0] - s) * strong_level
		delta_l = (style[1] - l) * strong_level

		changed_s = s + delta_s
		changed_l = l + delta_l
		return [h, changed_s, changed_l]

	def move_hsl_to_dark_style(self, input_hsl, strong_level=0.5):
		"""
		입력받은 hsl값을 어두운 쪽으로 이동시키는것
		bright = [100,100], sharp = [50,100], graish = [100,0], dark = [0,0], black = [50, 0]
		"""
		h, s, l = input_hsl
		style = dark = [0,0]

		delta_s = (style[0] - s) * strong_level
		delta_l = (style[1] - l) * strong_level

		changed_s = s + delta_s
		changed_l = l + delta_l
		return [h, changed_s, changed_l]

	def move_hsl_to_gray_style(self, input_hsl, strong_level=0.5):
		"""
		입력받은 hsl값을 어두운 쪽으로 이동시키는것
		bright = [100,100], sharp = [50,100], graish = [100,0], dark = [0,0], black = [50, 0]
		"""
		h, s, l = input_hsl
		style = graish = [100,0]

		delta_s = (style[0] - s) * strong_level
		delta_l = (style[1] - l) * strong_level

		changed_s = s + delta_s
		changed_l = l + delta_l
		return [h, changed_s, changed_l]

	def move_hsl_to_vivid_style(self, input_hsl, strong_level=0.5):
		"""
		입력받은 hsl값을 어두운 쪽으로 이동시키는것
		bright = [100,100], sharp = [50,100], graish = [100,0], dark = [0,0], black = [50, 0]
		"""
		h, s, l = input_hsl
		style = sharp = [50,100]

		delta_s = (style[0] - s) * strong_level
		delta_l = (style[1] - l) * strong_level

		changed_s = s + delta_s
		changed_l = l + delta_l
		return [h, changed_s, changed_l]

	def make_one_color_to_many_colors_by_step (self, input_color = "red", step = 10):
		"""
		하나의 색을 지정하면 10가지의 단계로 색을 돌려주는 것이다
		"""
		result =[]
		for no in range(0,100,int(100/step)):
			temp = self.change_color_to_rgb(input_color+str(no))
			result.append(temp)
		return result