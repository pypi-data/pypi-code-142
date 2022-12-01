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
数据库相关异常

"""
from .baseic import AwakenBaseError


# --------------------------------------------------------------------------
class AwakenDatabaseTableNotFoundError(AwakenBaseError):
    """ [ 数据库数据表不存在 ] """

    def __init__(
        self, 
        table_name: str,
    ):
        self.table_name = table_name
        super().__init__()

    def __str__(self) -> str:
        self.bas_message = [
            f'数据库中不存在数据表:: {self.table_name} !'
        ]
        return super().__str__()


# --------------------------------------------------------------------------
class AwakenDatabaseTableNotFoundFieldError(AwakenBaseError):
    """ [ 数据库数据表不存在字段 ] """

    def __init__(
        self, 
        table_name: str,
        field_name: str,
    ):
        self.table_name = table_name
        self.field_name = field_name
        super().__init__()

    def __str__(self) -> str:
        self.bas_message = [
            f'数据库表:: {self.table_name} 不存在字段 :: {self.field_name} !'
        ]
        return super().__str__()


# --------------------------------------------------------------------------
class AwakenDatabaseTableDeductionInserteError(AwakenBaseError):
    """ [ 数据库数据表推导插入失败 ] """

    def __init__(
        self,
        table_name: str,
        expect_para_count: int,
        actual_para_count: int,
    ):
        self.table_name = table_name
        self.expect_para_count = expect_para_count
        self.actual_para_count = actual_para_count
        super().__init__()

    def __str__(self) -> str:
        self.bas_message = [
            f'数据库表:: {self.table_name}',
            f'期望接受 value 数:: {self.expect_para_count}',
            f'实际接受 value 数:: {self.actual_para_count}'
        ]
        return super().__str__()
