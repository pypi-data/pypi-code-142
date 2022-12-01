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
[ 转换格式相关函数 ]

"""
import re
import json

from ..error.type_error import AwakenTypeDetectionFailedError


# --------------------------------------------------------------------------
def try_converting_string_format(string: str):
    """ 
    [ 尝试将字符串转换为对应格式 ]

    ---
    参数
    - string : { str } - 参与计算的字符串。

    """
    # 如果值是字典, 则使用解析成json串返回
    if isinstance(string, dict):
        string = json.dumps(string, ensure_ascii=False).replace("'", r'\"')
        return string

    # 如果参与计算的值不是字符串则尝试转换成字符串
    if not isinstance(string, str):
        try:
            string = str(string)
        except BaseException:
            AwakenTypeDetectionFailedError(expect='str', result=type(string))

    # 字符串规则
    # 如果字符串被 <'> 或 <"> 符号包裹, 则视其为字符串类型
    if string[0] == "'" and string[-1] == "'":
        string_extract = re.findall(r'\'(.*)\'', string)
        return string_extract[0] if len(string_extract) > 0 else ''

    if string[0] == '"' and string[-1] == '"':
        string_extract = re.findall(r'\"(.*)\"', string)
        return string_extract[0] if len(string_extract) > 0 else ''

    # 布尔值规则
    if string in ['true', 'True', 'TRUE']:
        return True
    if string in ['false', 'False', 'FALSE']:
        return False

    # 整数与浮点数规则
    try:
        int_extract = float(string)
        if int_extract.is_integer():
            int_extract = int(int_extract)
        return int_extract

    except ValueError:
        return string
