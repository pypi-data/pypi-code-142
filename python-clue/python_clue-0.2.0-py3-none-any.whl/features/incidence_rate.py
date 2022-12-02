from typing import List, Dict

from clue_pb2 import (
    RequestIncidenceRate,
    RequestIncidenceRateStream
)

from pyclue.converter import convert
from pyclue.stream import Stream


class IncidenceRateFeatures:
  @convert()
  def get_incidence_rate_result(
      self,
      incidence_rate_id: int
  ) -> List[Dict]:
    """
    Get the incidence rate result table.

    :param int incidence_rate_id:
      ID of the incidence rate.

    :return: List of table rows.
    :rtype: List of dictionaries.
    """
    incidence_rate = self.stub.GetIncidenceRateResult(RequestIncidenceRate(
        incidence_rate_id=incidence_rate_id
    ))

    return incidence_rate.row_list

  def get_incidence_rate_raw(
      self,
      incidence_rate_id: int
  ) -> Stream:
    """
    Get the incidence rate raw table.

    :param int incidence_rate_id:
      ID of the incidence rate.

    :return: StreamObject
    :rtype: List of dictionaries.
    """
    return Stream(
        self.stub.GetIncidenceRateRaw,
        RequestIncidenceRateStream,
        incidence_rate_id=incidence_rate_id
    )
