class StringSort:
    """Library that helps with string: sort them,
    delete sings that are not useful,
    and so on!
    """

    def __init__(self, string):
        self.string = string

    def delete(self, delete):
        """method to delete one sign from string"""

        self.delete = delete
        list1 = []
        list1.extend(str(self.string))

        for i in range(len(list1)):
            if list1[i] == str(self.delete):
                list1[i] = ''
        return ''.join(list1)

    def delete_2_symbols(self, sign1, sign2):
        """method to delete two sign from string"""

        list1 = []
        list1.extend(str(self.string))

        for i in range(len(list1)):
            if (list1[i] == str(sign1)) | (list1[i] == str(sign2)):
                list1[i] = ''
        return ''.join(list1)

    def delete_3_symbols(self, sign1, sign2, sign3):
        """method to delete three sign from string"""

        list1 = []
        list1.extend(str(self.string))

        for i in range(len(list1)):
            if (list1[i] == str(sign1)) | (list1[i] == str(sign2)) | (list1[i] == str(sign3)):
                list1[i] = ''
        return ''.join(list1)

    def delete_4_symbols(self, sign1, sign2, sign3, sign4):
        """method to delete four sign from string"""

        list1 = []
        list1.extend(str(self.string))

        for i in range(len(list1)):
            if (list1[i] == str(sign1)) | (list1[i] == str(sign2)) | (list1[i] == str(sign3)) | (
                    list1[i] == str(sign4)):
                list1[i] = ''
        return ''.join(list1)

    def delete_5_symbols(self, sign1, sign2, sign3, sign4, sign5):
        """method to delete five sign from string"""

        list1 = []
        list1.extend(str(self.string))

        for i in range(len(list1)):
            if (list1[i] == str(sign1)) | (list1[i] == str(sign2)) | (list1[i] == str(sign3)) | (list1[i] == str(sign4)) \
                    | (list1[i] == str(sign5)):
                list1[i] = ''
        return ''.join(list1)

    def delete_6_symbols(self, sign1, sign2, sign3, sign4, sign5, sign6):
        """method to delete six sign from string"""

        list1 = []
        list1.extend(str(self.string))

        for i in range(len(list1)):
            if (list1[i] == str(sign1)) | (list1[i] == str(sign2)) | (list1[i] == str(sign3)) | (list1[i] == str(sign4)) \
                    | (list1[i] == str(sign5)) | (list1[i] == str(sign6)):
                list1[i] = ''
        return ''.join(list1)

    def delete_7_symbols(self, sign1, sign2, sign3, sign4, sign5, sign6, sign7):
        """method to delete seven sign from string"""

        list1 = []
        list1.extend(str(self.string))

        for i in range(len(list1)):
            if (list1[i] == str(sign1)) | (list1[i] == str(sign2)) | (list1[i] == str(sign3)) | (list1[i] == str(sign4)) \
                    | (list1[i] == str(sign5)) | (list1[i] == str(sign6)) | (list1[i] == str(sign7)):
                list1[i] = ''
        return ''.join(list1)

    def delete_8_symbols(self, sign1, sign2, sign3, sign4, sign5, sign6, sign7, sign8):
        """method to delete eight sign from string"""

        list1 = []
        list1.extend(str(self.string))

        for i in range(len(list1)):
            if (list1[i] == str(sign1)) | (list1[i] == str(sign2)) | (list1[i] == str(sign3)) | (list1[i] == str(sign4)) \
                    | (list1[i] == str(sign5)) | (list1[i] == str(sign6)) | (list1[i] == str(sign7)) | \
                    (list1[i] == str(sign8)):
                list1[i] = ''
        return ''.join(list1)

    def delete_9_symbols(self, sign1, sign2, sign3, sign4, sign5, sign6, sign7, sign8, sign9):
        """method to delete nine sign from string"""

        list1 = []
        list1.extend(str(self.string))

        for i in range(len(list1)):
            if (list1[i] == str(sign1)) | (list1[i] == str(sign2)) | (list1[i] == str(sign3)) | (list1[i] == str(sign4)) \
                    | (list1[i] == str(sign5)) | (list1[i] == str(sign6)) | (list1[i] == str(sign7)) | \
                    (list1[i] == str(sign8)) | (list1[i] == str(sign9)):
                list1[i] = ''
        return ''.join(list1)

    def delete_10_symbols(self, sign1, sign2, sign3, sign4, sign5, sign6, sign7, sign8, sign9, sign10):
        """method to delete ten sign from string"""

        list1 = []
        list1.extend(str(self.string))

        for i in range(len(list1)):
            if (list1[i] == str(sign1)) | (list1[i] == str(sign2)) | (list1[i] == str(sign3)) | (list1[i] == str(sign4)) \
                    | (list1[i] == str(sign5)) | (list1[i] == str(sign6)) | (list1[i] == str(sign7)) | \
                    (list1[i] == str(sign8)) | (list1[i] == str(sign9)) | (list1[i] == str(sign10)):
                list1[i] = ''
        return ''.join(list1)

    def alphabetical_order(self):
        """string in alphabetical order"""

        list1 = []
        list1.extend(self.string)
        list1.sort()
        return ''.join(list1)

    def delete_with_space(self, delete):
        """method to delete one sign from string with space"""

        self.delete = delete
        list1 = []
        list1.extend(str(self.string))

        for i in range(len(list1)):
            if list1[i] == str(self.delete):
                list1[i] = ' '
        return ''.join(list1)

    def delete_2_symbols_with_space(self, sign1, sign2):
        """method to delete two sign from string with space"""

        list1 = []
        list1.extend(str(self.string))

        for i in range(len(list1)):
            if (list1[i] == str(sign1)) | (list1[i] == str(sign2)):
                list1[i] = ' '
        return ''.join(list1)

    def delete_3_symbols_with_space(self, sign1, sign2, sign3):
        """method to delete three sign from string with space"""

        list1 = []
        list1.extend(str(self.string))

        for i in range(len(list1)):
            if (list1[i] == str(sign1)) | (list1[i] == str(sign2)) | (list1[i] == str(sign3)):
                list1[i] = ' '
        return ''.join(list1)

    def delete_4_symbols_with_space(self, sign1, sign2, sign3, sign4):
        """method to delete four sign from string with space"""

        list1 = []
        list1.extend(str(self.string))

        for i in range(len(list1)):
            if (list1[i] == str(sign1)) | (list1[i] == str(sign2)) | (list1[i] == str(sign3)) | (
                    list1[i] == str(sign4)):
                list1[i] = ' '
        return ''.join(list1)

    def delete_5_symbols_with_space(self, sign1, sign2, sign3, sign4, sign5):
        """method to delete five sign from string with space"""

        list1 = []
        list1.extend(str(self.string))

        for i in range(len(list1)):
            if (list1[i] == str(sign1)) | (list1[i] == str(sign2)) | (list1[i] == str(sign3)) | (list1[i] == str(sign4)) \
                    | (list1[i] == str(sign5)):
                list1[i] = ' '
        return ''.join(list1)

    def delete_6_symbols_with_space(self, sign1, sign2, sign3, sign4, sign5, sign6):
        """method to delete six sign from string with space"""

        list1 = []
        list1.extend(str(self.string))

        for i in range(len(list1)):
            if (list1[i] == str(sign1)) | (list1[i] == str(sign2)) | (list1[i] == str(sign3)) | (list1[i] == str(sign4)) \
                    | (list1[i] == str(sign5)) | (list1[i] == str(sign6)):
                list1[i] = ' '
        return ''.join(list1)

    def delete_7_symbols_with_space(self, sign1, sign2, sign3, sign4, sign5, sign6, sign7):
        """method to delete seven sign from string with space"""

        list1 = []
        list1.extend(str(self.string))

        for i in range(len(list1)):
            if (list1[i] == str(sign1)) | (list1[i] == str(sign2)) | (list1[i] == str(sign3)) | (list1[i] == str(sign4)) \
                    | (list1[i] == str(sign5)) | (list1[i] == str(sign6)) | (list1[i] == str(sign7)):
                list1[i] = ' '
        return ''.join(list1)

    def delete_8_symbols_with_space(self, sign1, sign2, sign3, sign4, sign5, sign6, sign7, sign8):
        """method to delete eight sign from string with space"""

        list1 = []
        list1.extend(str(self.string))

        for i in range(len(list1)):
            if (list1[i] == str(sign1)) | (list1[i] == str(sign2)) | (list1[i] == str(sign3)) | (list1[i] == str(sign4)) \
                    | (list1[i] == str(sign5)) | (list1[i] == str(sign6)) | (list1[i] == str(sign7)) | \
                    (list1[i] == str(sign8)):
                list1[i] = ' '
        return ''.join(list1)

    def delete_9_symbols_with_space(self, sign1, sign2, sign3, sign4, sign5, sign6, sign7, sign8, sign9):
        """method to delete nine sign from string with space"""

        list1 = []
        list1.extend(str(self.string))

        for i in range(len(list1)):
            if (list1[i] == str(sign1)) | (list1[i] == str(sign2)) | (list1[i] == str(sign3)) | (list1[i] == str(sign4)) \
                    | (list1[i] == str(sign5)) | (list1[i] == str(sign6)) | (list1[i] == str(sign7)) | \
                    (list1[i] == str(sign8)) | (list1[i] == str(sign9)):
                list1[i] = ' '
        return ''.join(list1)

    def delete_10_symbols_with_space(self, sign1, sign2, sign3, sign4, sign5, sign6, sign7, sign8, sign9, sign10):
        """method to delete ten sign from string with space"""

        list1 = []
        list1.extend(str(self.string))

        for i in range(len(list1)):
            if (list1[i] == str(sign1)) | (list1[i] == str(sign2)) | (list1[i] == str(sign3)) | (list1[i] == str(sign4)) \
                    | (list1[i] == str(sign5)) | (list1[i] == str(sign6)) | (list1[i] == str(sign7)) | \
                    (list1[i] == str(sign8)) | (list1[i] == str(sign9)) | (list1[i] == str(sign10)):
                list1[i] = ' '
        return ''.join(list1)

    def which_one_delete(self, sing, number):
        f"""this method delete {number}th {sing} of the string"""

        self.sign = sing
        self.number = number
        list1 = []
        list1.extend(str(self.string))

        num = 0

        for i in range(len(list1)):
            if list1[i] == str(self.sign):
                num += 1
                if list1.count(self.sign) >= self.number:
                    if num == int(self.number):
                        list1[i] = ''
                else:
                    raise SyntaxError(f"your string '{self.string}' don't have {self.number} of '{self.sign}'")

        return ''.join(list1)

    def which_one_delete_with_space(self, sing, number):
        """this method delete number sing of the string with space"""

        self.sign = sing
        self.number = number
        list1 = []
        list1.extend(str(self.string))

        num = 0

        for i in range(len(list1)):
            if list1[i] == str(self.sign):
                num += 1
                if list1.count(self.sign) >= self.number:
                    if num == int(self.number):
                        list1[i] = ' '
                else:
                    raise SyntaxError(f"your string '{self.string}' don't have {self.number} of '{self.sign}'")

        return ''.join(list1)

    def same_signs(self, search_string):
        """this method will find same sings"""

        list1 = []

        list2 = []

        list1.extend(self.string)

        list2.extend(search_string)

        list3 = []

        if len(list1) <= len(list2):
            for i in range(len(list2)):
                if list2[i] != ' ':
                    for j in list1:
                        if list2[i] == j:
                            list3.append(j)
                            list1.remove(j)
        else:
            raise SyntaxError(f"string '{list1}' is bigger than '{list2}'")

        return ', '.join(list3)

    def delete_all_types_of_parentheses(self):
        """method to delete all types of parentheses from string"""

        list1 = []
        list1.extend(str(self.string))

        if ('(' in list1) and (')' in list1) and ('{' in list1) and ('}' in list1) and ('[' in list1) and (']' in list1):
            for i in range(len(list1)):
                if (list1[i] == '(') | (list1[i] == '[') | (list1[i] == '{') | \
                        (list1[i] == '}') | (list1[i] == ']') | (list1[i] == ')'):
                    list1[i] = ''
            return ''.join(list1)
        else:
            raise SyntaxError(self.string + " don't have '{}', '[]' or '()'")

    def delete_all_types_of_parentheses_with_space(self):
        """method to delete all types of parentheses from string with space"""

        list1 = []
        list1.extend(str(self.string))

        if ('(' in list1) | (')' in list1) | ('{' in list1) | ('}' in list1) | ('[' in list1) | (']' in list1):
            for i in range(len(list1)):
                if (list1[i] == '(') | (list1[i] == '[') | (list1[i] == '{') | \
                        (list1[i] == '}') | (list1[i] == ']') | (list1[i] == ')'):
                    list1[i] = ' '
            return ''.join(list1)
        else:
            raise SyntaxError(self.string + " don't have '{}', '[]' or '()'")

    def split(self, number_of_signs):
        list1 = []
        list1.extend(self.string)

        num = 0

        for i in range(len(list1)):
            num += 1
            if num == number_of_signs:
                if list1[i] != ' ':
                    list1[i] = list1[i] + '-' + '\n'
                    num = 0
                else:
                    list1[i] = list1[i] + '\n'
                    num = 0

        return ''.join(list1)