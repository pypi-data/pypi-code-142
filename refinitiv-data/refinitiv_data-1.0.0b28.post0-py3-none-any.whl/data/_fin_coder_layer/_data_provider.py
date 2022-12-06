from typing import TYPE_CHECKING

import numpy as np
import pandas as pd

from .._tools._dataframe import convert_df_columns_to_datetime, convert_dtypes

if TYPE_CHECKING:
    from .context_collection import ADCContext, HPContext
    from ._containers import HPAndCustInstDataContainer, ADCDataContainer


def convert_types(column: list, column_names: list) -> list:
    date_columns = [
        i
        for i, column_name in enumerate(column_names)
        if any([i for i in ["Date", "date", "_DT", "DATE"] if i in column_name])
        and all([i if i not in column_name else False for i in ["DateType", "Dates"]])
    ]
    result = [i if i is not None and i != "" else pd.NA for i in column]

    if date_columns:
        for i in date_columns:
            result[i] = pd.to_datetime(result[i])

    return result


class DataProvider:
    def get_df(
        self,
        adc: "ADCContext",
        mixed: "HPContext",
        adc_data: "ADCDataContainer",
        mixed_data: "HPAndCustInstDataContainer",
        use_field_names_in_headers: bool,
    ) -> pd.DataFrame():

        if not mixed_data and not adc_data:
            return pd.DataFrame()

        elif mixed.can_build_df:
            return mixed.df

        elif adc.can_build_df:
            return adc.df

        # merge_data
        columns, data = self.merge_data(
            adc_data, mixed_data, use_field_names_in_headers
        )

        if not any(columns):
            return pd.DataFrame()

        else:
            df = pd.DataFrame(np.array(data), columns=columns)
            df = convert_df_columns_to_datetime(
                df, entry="Date", utc=True, delete_tz=True
            )
            return convert_dtypes(df)

    def merge_data(
        self,
        adc_data: "ADCDataContainer",
        mixed_data: "HPAndCustInstDataContainer",
        use_field_names_in_headers: bool,
    ):
        adc_columns, data = self.get_columns_and_data_from_adc_raw(
            adc_data.raw, use_field_names_in_headers
        )
        columns = adc_columns + mixed_data.columns
        if not adc_columns and mixed_data.columns:
            columns.insert(0, "Instrument")

        result_data = []
        for universe in mixed_data.raw:
            if universe in data:
                for column in data[universe]:
                    column.extend(mixed_data.raw[universe])
                    result_data.append(column)

            else:
                data[universe] = (
                    [universe]
                    + [pd.NA] * (len(adc_columns) - 1)
                    + mixed_data.raw[universe]
                )
                result_data.append(data[universe])

        return columns, result_data

    def get_columns_and_data_from_adc_raw(
        self, raw: dict, use_field_names_in_headers: bool
    ) -> tuple:
        headers = raw.get("headers", [[{}]])

        if headers and isinstance(headers[0], list):
            columns = [
                header.get("displayName")
                if not use_field_names_in_headers
                else header.get("field", header.get("displayName"))
                for header in headers[0]
            ]
        else:
            columns = [
                header.get("name")
                if use_field_names_in_headers
                else header.get("title")
                for header in headers
            ]

            if "instrument" in columns:
                columns[columns.index("instrument")] = "Instrument"

        _data = raw.get("data", [])
        data = {}

        for column in _data:
            if column[0] not in data:
                data[column[0]] = []

            data[column[0]].append(convert_types(column, columns))

        if not data:
            columns = []

        return columns, data
