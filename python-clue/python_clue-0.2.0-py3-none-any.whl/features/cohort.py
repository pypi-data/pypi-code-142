from typing import List, Dict

from clue_pb2 import (
    EmptyMessage,
    RequestCohortList,
    RequestTableSchema,
    RequestCohortTable
)

from pyclue.converter import convert
from pyclue.stream import Stream


class CohortFeatures:
  @convert()
  def get_cohort_list(
      self,
      page: int = 1,
      length: int = 0,
      term: str = ""
  ) -> List[Dict]:
    """
    Get the list of cohorts.

    :param int page:
      Page number.
    :param int length:
      Number of cohorts in a page. If 0, all cohorts will be returned.
    :param str term:
      Search term.

    :return: List of cohorts.
    :rtype: List of dictionaries.
    """
    cohort_list = self.stub.GetCohortList(RequestCohortList(
        term=term,
        page=page,
        length=length,
    )).cohort_list

    return cohort_list

  @convert()
  def get_cohort_table_list(self) -> List[str]:
    """
    Get the list of the tables.

    :return List of table names
    :rtype: List of string
    """
    table_list = self.stub.GetCohortTableList(EmptyMessage()).table_list
    return table_list

  def __make_response(self, schema_info, obj):
    result_obj = {}
    for col, value in zip(schema_info.int32_cols, obj.int32_values):
      result_obj[col] = value.value

    for col, value in zip(schema_info.int64_cols, obj.int64_values):
      result_obj[col] = value.value

    for col, value in zip(schema_info.float_cols, obj.float_values):
      result_obj[col] = value.value

    for col, value in zip(schema_info.str_cols, obj.str_values):
      result_obj[col] = value.value

    for col, value in zip(schema_info.bool_cols, obj.bool_values):
      result_obj[col] = value.value

    return result_obj

  def get_cohort_table(self, cohort_id, table_name):
    """
    """
    schema_info = self.stub.GetCohortTableSchema(RequestTableSchema(
        table_name=table_name
    ))

    return Stream(
        self.stub.GetCohortTable,
        RequestCohortTable,
        lambda obj: self.__make_response(schema_info, obj),
        cohort_id=cohort_id,
        table_name=table_name,
    )
