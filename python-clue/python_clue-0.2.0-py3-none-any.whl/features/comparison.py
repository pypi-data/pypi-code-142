from typing import List, Dict

from clue_pb2 import (
    RequestComparison
)

from pyclue.converter import convert


class CohortComparisonFeatures:
  @convert()
  def get_cohort_comparison(
      self,
      comparison_id: int
  ) -> List[Dict]:
    """
    Get the comparison of cohorts.
 
    :param int comparison_id:
      ID of the cohort comparison.
 
    :return: Comparison.
    :rtype: List of dictionaries.
    """
    comparison = self.stub.GetCohortComparison(RequestComparison(
        comparison_id=comparison_id
    ))

    rows = []
    for row in comparison.row_list:
      row_dict = {
          "category1": row.category1,
          "category2": row.category2,
          "p_value": row.p_value,
          "p_value_is_group": row.p_value_is_group
      }

      for idx, cohort in enumerate(comparison.cohort_list):
        row_dict[cohort.name] = row.values[idx]

      rows.append(row_dict)

    return rows
