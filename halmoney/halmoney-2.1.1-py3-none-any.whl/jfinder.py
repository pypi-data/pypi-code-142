# -*- coding: utf-8 -*-
import re

class jfinder:
    def jfinder (self, input_text=""):
        print(input_text)
        result = input_text.replace(" ", "")

        setup_list = [
            ["(대소문자무시)", "(?!)"], #re.IGNORECASE 대소문자 무시
            ["(여러줄)", "(?m)"], # re.MULITILINE 여러줄도 실행
            ["(개행문자포함)", "(?s)"], # re.DOTALL 개행문자도 포함
            ]

        for one in setup_list:
            result = result.replace(one[0], one[1])

        basic_list = [
            [":(\d+)[~](\d*)[\]]",             "]{\\1,\\2}"], # :3~4] ==> ]{3,4}
            ["[\[](\d+)[~](\d*)[\]]",          "{\\1,\\2}"], # [3~4] ==> {3,4}

            ["\(뒤에있음:(.*)\)",                "(?=\\1)" ], #(뒤에있음:(abc)) => (?=abc)
            ["\(뒤에없음:(.*)\)",                "(?!\\1)" ], #(뒤에없음:(abc)) => (?!abc)
            ["\((.*):뒤에있음\)",                "(?=\\1)" ], #(뒤에있음:(abc)) => (?=abc)
            ["\((.*):뒤에없음\)",                "(?!\\1)" ], #(뒤에없음:(abc)) => (?!abc)
            ["\(앞에있음:(.*)\)",                "(?<=\\1)"], #(앞에있음:(abc)) => (?<=abc)
            ["\(앞에없음:(.*)\)",                "(?<!\\1)"], #(앞에없음:(abc)) => (?<!abc)

            ["([\[]?)한글모음[&]?([\]]?)",       "\\1ㅏ-ㅣ\\2"], #[ㅏ-ㅣ]
            ["([\[]?)한글[&]?([\]]?)",          "\\1ㄱ-ㅎ|ㅏ-ㅣ|가-힣\\2"],
            ["([\[]?)숫자[&]?([\]]?)",          "\\1 0-9 \\2"],
            ["([\[]?)영어대문자[&]?([\]]?)",     "\\1A-Z\\2"],
            ["([\[]?)영어소문자[&]?([\]]?)",     "\\1a-z\\2"],
            ["([\[]?)영어[&]?([\]]?)",          "\\1a-zA-Z\\2"],
            ["([\[]?)일본어[&]?([\]]?)",        "\\1ぁ-ゔ|ァ-ヴー|々〆〤\\2"],
            ["([\[]?)한자[&]?([\]]?)",          "\\1一-龥\\2"],
            ["([\[]?)특수문자[&]?([\]]?)",       "\\1 @#$&-_ \\2"],
            ["([\[]?)모든문자[&]?([\]]?)",      "\\1.\n\\2"],
            ["([\[]?)문자[&]?([\]]?)",          "\\1.\\2"],
            ["([\[]?)공백[&]?([\]]?)",          "\\1\\\s\\2"],

            ["[\[]단어([(].*?[)])([\]]?)",      "\\1"],
            ["[\[]또는([(].*?[)])([\]]?)",      "\\1|"],
            ["[\(]이름<(.+?)>(.+?)[\)]",        "?P<\\1>\\2"], #[이름<abc>표현식]
            ]

        for one in basic_list:
            result = re.sub(one[0], one[1], result)
            result = result.replace(" ", "")

        simple_list = [
            ['[처음]', '^'], ['[맨앞]', '^'], ['[시작]', '^'],
            ['[맨뒤]', '$'], ['[맨끝]', '$'], ['[끝]', '$'],
            ['[또는]', '|'], ['또는', '|'],['or', '|'],
            ['not', '^'],
            ]

        for one in simple_list:
            result = result.replace(one[0], one[1])

        #최대탐색을 할것인지 최소탐색을 할것인지 설정하는 것이다
        if "(최소찾기)" in result:
            result = result.replace("[1,]","+")
            result = result.replace("[1,]","*")

            result = result.replace("+","+?")
            result = result.replace("*","*?")
            result = result.replace("(최소찾기)","")


        #이단계를 지워도 실행되는데는 문제 없으며, 실행 시키지 않았을때가 약간 더 읽기는 편하다
        high_list = [
            ['[^a-zA-Z0-9]', '\W'],
            ['[^0-9a-zA-Z]', '\W'],
            ['[a-zA-Z0-9]', '\w'],
            ['[0-9a-zA-Z]', '\w'],
            ['[^0-9]', '\D'],
            ['[0-9]', '\d'],
            ['{0,}', '*'],
            ['{1,}', '+'],
            ]

        for one in high_list:
            result = result.replace(one[0], one[1])
        return result

    def change_jfsql_to_resql (self, jf_sql):
        result = self.jfinder(jf_sql)
        return result

    def search (self, jf_sql, input_text):
        re_sql = self.jfinder(jf_sql)
        re_compiled = re.compile(re_sql)
        result = re_compiled.findall(input_text)
        return result

    def search_by_resql (self, re_sql, input_text):
        re_compiled = re.compile(re_sql)
        result = re_compiled.findall(input_text)
        return result

    def replace (self, jf_sql, input_text, replace_word):
        re_sql = self.jfinder(jf_sql)
        result = re.sub(re_sql, replace_word, input_text)
        return result

    def delete (self, jf_sql, input_text, replace_word=""):
        re_sql = self.jfinder(jf_sql)
        result = re.sub(re_sql, "", input_text)
        return result

    def delete_by_resql (self, re_sql, input_text, replace_word=""):
        result = re.sub(re_sql, "", input_text)
        return result

    def replace_by_resql (self, re_sql, input_text, replace_word):
        result = re.sub(re_sql, replace_word, input_text)
        return result

    def run (self, jf_sql, input_text):
        #결과값을 얻는것이 여러조건들이 있어서 이것을 하나로 만듦
        # [[결과값, 시작순서, 끝순서, [그룹1, 그룹2...], match결과].....]
        re_sql = self.jfinder(jf_sql)
        re_com = re.compile(re_sql)
        result_match = re_com.match(input_text)
        result_finditer = re_com.finditer(input_text)

        final_result = []
        num=0
        for one_iter in result_finditer:
            temp=[]
            #찾은 결과값과 시작과 끝의 번호를 넣는다
            temp.append(one_iter.group())
            temp.append(one_iter.start())
            temp.append(one_iter.end())

            #그룹으로 된것을 넣는것이다
            temp_sub = []
            if len(one_iter.group()):
                for one in one_iter.groups():
                    temp_sub.append(one)
                temp.append(temp_sub)
            else:
                temp.append(temp_sub)

            #제일 첫번째 결과값에 match랑 같은 결과인지 넣는것
            if num == 0: temp.append(result_match)
            final_result.append(temp)
            num+=1
        return final_result

    def run_by_resql(self, input_sql, input_text):
        re_com = re.compile(input_sql)
        re_results = re_com.finditer(input_text)
        result = []
        if re_results:
            for one in re_results:
                result.append([one.group(), one.start(), one.end()])
        return result


    def make_list_on_re_compile(self, re_txt, file_name):
        # 텍스트화일을 읽어서 re에 맞도록 한것을 리스트로 만드는 것이다
        # 함수인 def를 기준으로 저장을 하며, [[공백을없앤자료, 원래자료, 시작줄번호].....]
        re_com = re.compile(re_txt)
        f = open(file_name, 'r', encoding='UTF8')
        lines = f.readlines()
        num = 0
        temp = ""
        temp_original = ""
        result = []
        for one_line in lines:
            aaa = re.findall(re_com, str(one_line))
            original_line = one_line
            changed_line = one_line.replace(" ", "")
            changed_line = changed_line.replace("\n", "")

            if aaa:
                result.append([temp, temp_original, num])
                temp = changed_line
                temp_original = original_line
            # print("발견", num)
            else:
                temp = temp + changed_line
                temp_original = temp_original + one_line
        return result

    def get_between_number_length(self, input_text, m, n):
        # m,n개사이인것만 추출
        re_basic = "^\d{" + str(m) + "," + str(n) + "}$"
        result = re.findall(re_basic, input_text)
        return result

    def get_between_text_length(self, input_text, m, n):
        # 문자수제한 : m다 크고 n보다 작은 문자
        re_basic = "^.{" + str(m) + "," + str(n) + "}$"
        result = re.findall(re_basic, input_text)
        return result

    def get_text_between_ab(self, input_text, text_a, text_b):
        # 입력된 자료에서 두개문자사이의 글자를 갖고오는것
        replace_lists = [
            ["(", "\("],
            [")", "\)"],
        ]
        origin_a = text_a
        origin_b = text_b

        for one_list in replace_lists:
            text_a = text_a.replace(one_list[0], one_list[1])
            text_b = text_b.replace(one_list[0], one_list[1])
        re_basic = text_a + "[^" + str(origin_b) + "]*" + text_b
        result = re.findall(re_basic, input_text)
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


    def check_all_cap(self, input_text):
        # 모두 알파벳대문자
        re_basic = "^[A-Z]+$"
        result = re.findall(re_basic, input_text)
        return result

    def check_dash_date(self, input_text):
        # 모두 알파벳대문자
        re_basic = "^\d{4}-\d{1,2}-\d{1,2}$"
        result = re.findall(re_basic, input_text)
        return result

    def check_email_address(self, input_text):
        # 이메일주소 입력
        re_basic = "^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$"
        result = re.findall(re_basic, input_text)
        return result

    def check_eng_only(self, input_text):
        # 모두 영문인지
        re_basic = "^[a-zA-Z]+$"
        result = re.findall(re_basic, input_text)
        return result

    def check_handphone_only(self, input_text):
        # 특수문자가들어가있는지
        re_basic = "^(010|019|011)-\d{4}-\d{4}"
        result = re.findall(re_basic, input_text)
        return result

    def check_ip_address(self, input_text):
        # 이메일주소 입력
        re_basic = "((?:(?:25[0-5]|2[0-4]\\d|[01]?\\d?\\d)\\.){3}(?:25[0-5]|2[0-4]\\d|[01]?\\d?\\d))"
        result = re.findall(re_basic, input_text)
        return result

    def check_korean_only(self, input_text):
        # 모두 한글인지
        re_basic = "[ㄱ-ㅣ가-힣]"
        result = re.findall(re_basic, input_text)
        return result

    def check_special_char(self, input_text):
        # 특수문자가들어가있는지
        re_basic = "^[a-zA-Z0-9]"
        result = re.findall(re_basic, input_text)
        return result

    def delete_except_engnum(self, input_text):
        # 알파벳과 숫자만 있는것을 확인하는것
        re_com = re.compile("[^A-Za-z0-9]")
        if (re_com.search(input_text) == None):
            new_text = input_text
        else:
            print(re_com.search(input_text))
            new_text = re_com.sub("", input_text)
            print(new_text)
        return new_text

    def delete_except_korengnum(self, input_text):
        # 한글, 영어, 숫자만 남기고 나머지는 모두 지우는 것이다
        re_com = re.compile("[^A-Za-z0-9ㄱ-ㅎㅏ-ㅣ가-힣]")
        if (re_com.search(input_text) == None):
            new_text = input_text
        else:
            print(re_com.search(input_text))
            new_text = re_com.sub("", input_text)
            print(new_text)
        return new_text

    def delete_except_numcomma(self, input_text):
        # 숫자중에서 ,로 분비리된것중에서 ,만 없애는것
        # 1,234,567 => 1234567
        re_com = re.compile("[0-9,]")
        re_com_1 = re.compile("[,]")
        if (re_com.search(input_text) == None):
            new_text = input_text
        else:
            new_text = re_com_1.sub("", input_text)
            print(new_text)
        return new_text

    def delete_except_specialchar(self, input_text):
        # 공백과 특수문자등을 제외하고 같으면 새로운 y열에 1을 넣는 함수
        # 리스트의 사이즈를 조정한다
        re_com = re.compile("[\s!@#$%^*()\-_=+\\\|\[\]{};:'\",.<>\/?]")
        if (re_com.search(input_text) == None):
            new_text = input_text
        else:
            new_text = re_com.sub("", input_text)
            print(new_text)
        return new_text

    def delete_text_specialletter(self, input_list):
        # 입력받은 텍스트로된 리스트의 자료를 전부 특수문자를 없앤후 돌려주는 것이다
        # 입력된 자료가 1차원 리스트인지 판단한다
        if type(input_list) == type([]) and type(input_list[0]) != type([]):
            result = []
            for one in input_list:
                if one != "" or one != None:
                    temp = self.re_delete_specialletter(one)
                    result.append(temp)
        return result

    def delete_all_explanation(self, input_text):
        input_text = re.sub(re.compile(r"'''.*'''", re.DOTALL), "", input_text)
        input_text = re.sub(re.compile(r'""".*"""', re.DOTALL), "", input_text)
        result = re.sub(re.compile(r"#.*[\n]"), "\n", input_text)
        return result


    def pick_eng_in_text(self, input_text):
        """
		단어중에 나와있는 영어만 분리하는기능
		"""
        re_compile = re.compile(r"([a-zA-Z]+)")
        result = re_compile.findall(input_text)
        new_result = []
        for dim1_data in result:
            for dim2_data in dim1_data:
                new_result.append(dim2_data)
        return new_result

    def pick_num_in_text(self, input_text):
        """
		단어중에 나와있는 숫자만 분리하는기능
		"""
        re_compile = re.compile(r"([0-9]+)")
        result = re_compile.findall(input_text)
        new_result = []
        for dim1_data in result:
            for dim2_data in dim1_data:
                new_result.append(dim2_data)
        return new_result

    def convert_data_except_num_n_eng(self, original_data):
        """
        영문과 숫자와 공백을 제외하고 다 제거를 하는것
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