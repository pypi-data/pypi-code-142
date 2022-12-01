# Copyright 2022 quinn.7@foxmail.com All rights reserved.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
[ 模板渲染器 ]

"""


# --------------------------------------------------------------------------
class TemplateStyle:
    """ 
    [ 模板样式对象 ]

    """
    tab_horizontal   = '━'
    """ 制表符::水平 """
    tab_side         = '┃'
    """ 制表符::边柱 """
    tab_side_left    = '┣'
    """ 制表符::左柱 """
    tab_side_right   = '┫'
    """ 制表符::右柱 """
    tab_top_left     = '┏'
    """ 制表符::左上 """
    tab_bottom_left  = '┗'
    """ 制表符::左下 """
    tab_top_right    = '┓'
    """ 制表符::右上 """
    tab_bottom_right = '┛'
    """ 制表符::右下 """
    size = 70
    """ 表格长度 """


# --------------------------------------------------------------------------
class TemplateRendering:
    """
    [ 模板渲染器 ]

    ---
    描述
    - 采用模板的方式美化命令行信息输出。

    """
    _tab_style: TemplateStyle
    """ 模板样式 """


    # ----------------------------------------------------------------------
    def __init__(self, style: TemplateStyle = None) -> ...:
        self._tab_style = style if style != None else TemplateStyle
        self._tabulation_top     = ''.join([self._tab_style.tab_top_left, self._tab_style.tab_horizontal*self._tab_style.size, self._tab_style.tab_top_right])
        self._tabulation_bearing = ''.join([self._tab_style.tab_side_left, self._tab_style.tab_horizontal*self._tab_style.size, self._tab_style.tab_side_right])
        self._tabulation_bottom  = ''.join([self._tab_style.tab_bottom_left, self._tab_style.tab_horizontal*self._tab_style.size, self._tab_style.tab_bottom_right])


    # ----------------------------------------------------------------------
    def render_print(
        self, 
        source: list,
        title: str = None,
        is_show_number: bool = True,
        is_keep_space_top_and_bottom: bool = True,
        ) -> ...:
        """
        [ 渲染打印 ]

        ---
        描述
        - 打印模板表格。

        ---
        参数
        - source                       : { list } - 字符串列表。
        - title                        : { str }  - 模板抬头, 默认为空。
        - is_show_number               : { bool } - 是否显示编号, 默认为 True。
        - is_keep_space_top_and_bottom : { bool } - 是否保持上下间距, 默认为 True。
        
        """
        cmd_template = self.draw(source, title, is_show_number, is_keep_space_top_and_bottom)
        print('\n')
        for string in cmd_template:
            print(string)


    # ----------------------------------------------------------------------
    def draw(
        self, 
        source: list,
        title: str = None,
        is_show_number: bool = True,
        is_keep_space_top_and_bottom: bool = True,
        ) -> list:
        """
        [ 描绘 ]
        
        ---
        描述
        - 绘制模板表格。
        
        ---
        参数
        - source                       : { list } - 字符串列表。
        - title                        : { str }  - 模板抬头, 默认为空。
        - is_show_number               : { bool } - 是否显示编号, 默认为 True。
        - is_keep_space_top_and_bottom : { bool } - 是否保持上下间距, 默认为 True。
        
        ---
        返回
        - list : 模板字符串列表。
        
        """
        # 绘制模板抬头
        final_output_list = [self._tabulation_top]

        if title:
            if self._calculate_character_exceed(title):
                title, _ = self._clipping_out_of_length_strings(title)
            final_output_list.append(self._process_template_content(title))
            final_output_list.append(self._tabulation_bearing)

        if is_keep_space_top_and_bottom:
            source = [' ', *source, ' ']

        # 处理最终输出列表
        new_number = 0
        for str in source:
            if is_show_number and str != ' ':
                new_number += 1
                str = f'{ new_number } : { str }'
            while 1:
                if self._calculate_character_exceed(str):
                    str1, str = self._clipping_out_of_length_strings(str)
                    final_output_list.append(self._process_template_content(str1))
                    continue
                final_output_list.append(self._process_template_content(str))
                break
        final_output_list.append(self._tabulation_bottom)
        return final_output_list


    # ----------------------------------------------------------------------
    def _process_template_content(self, string: str) -> str:
        """
        [ 处理模板内容 ]

        ---
        描述
        - 根据Unicode编码判断字符是否中文以计算偏移量, 加以处理模板内容。

        ---
        返回
        - str : 处理完毕的模板内容。

        """
        offset = self._calculate_character_offset(string)
        return ''.join([
            self._tab_style.tab_side, ' ',
            string,
            ' '*((self._tab_style.size - len(string) - 2) - offset),
            ' ', self._tab_style.tab_side,
        ])


    # ----------------------------------------------------------------------
    def _calculate_character_offset(self, cha: str) -> int:
        """
        [ 计算字符偏移量 ]
        
        ---
        描述
        - 根据Unicode编码表判断字符是否中文以计算偏移量。

        ---
        返回
        - int : 字符偏移量。

        """
        offset = 0
        for s in cha:
            if u'\u4e00' <= s <= u'\u9fff':
                offset += 1
        return offset


    # ----------------------------------------------------------------------
    def _calculate_character_exceed(self, cha: str) -> bool:
        """
        [ 计算字符是否超出 ]

        ---
        描述
        - 根据模板表格的长度计算字符是否超出。

        ---
        返回
        - bool : 判断布尔值。

        """
        cha_number = len(cha)
        cha_offset = self._calculate_character_offset(cha)
        calculated_value = (self._tab_style.size - 2) - (cha_number + cha_offset)

        if calculated_value < 0:
            return True
        else:
            return False


    # ----------------------------------------------------------------------
    def _clipping_out_of_length_strings(self, string: str, accuracy: int = 0.01) -> tuple[str, str]:
        """
        [ 剪裁超出长度的字符串 ]

        """
        try:
            if accuracy >= 1 or accuracy < 0.01:
                raise Exception('参数 accuracy 只允许传入 0.01 - 0.99 的值.')

            first_decimal_point = int(str(accuracy)[2])
            truncation = 0.01 if first_decimal_point == 0 else 0.1
            while 1:
                subscript = int(len(string)*(1-truncation))
                if self._calculate_character_exceed(string[0: subscript]):
                    truncation += accuracy
                    continue
                str1 = string[0: subscript]
                str2 = string[subscript:]
                return str1, str2

        except BaseException as error:
            print(str(error))
            return self._clipping_out_of_length_strings(string, 1)


# --------------------------------------------------------------------------
G_TEMPLATE_RENDERING: TemplateRendering = TemplateRendering()
""" 模板渲染器全局实例 """
