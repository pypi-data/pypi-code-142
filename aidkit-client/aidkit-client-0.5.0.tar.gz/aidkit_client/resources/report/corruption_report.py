"""
Resources for the Corruption Report.
"""
from collections import defaultdict
from typing import Dict, List, Optional, Tuple, Union

import altair as alt
from ipywidgets import widgets
from pandas import DataFrame

from aidkit_client._endpoints.models import (
    ModelNormStats,
    OutputType,
    ReportCorruptionResponse,
    ReportRequest,
)
from aidkit_client._endpoints.report import ReportAPI
from aidkit_client.aidkit_api import HTTPService
from aidkit_client.configuration import get_api_client
from aidkit_client.resources.dataset import Dataset, Subset
from aidkit_client.resources.ml_model import MLModelVersion
from aidkit_client.resources.report._base_report import _BaseReport


class CorruptionReport(_BaseReport):
    """
    A report which compares model versions.
    """

    _data: ReportCorruptionResponse

    def __init__(self, api_service: HTTPService, report_response: ReportCorruptionResponse) -> None:
        """
        Create a new instance from the server response.

        :param api_service: Service instance to use for communicating with the
            server.
        :param report_response: Server response describing the report
            to be created.
        """
        self._data = report_response
        self._api_service = api_service

    @classmethod
    async def get(
        cls,
        model_name: str,
        model_versions: List[Union[str, MLModelVersion]],
        dataset: Union[str, Dataset],
        subset: Union[str, Subset],
        metrics: Optional[List[str]] = None,
        success_metric_threshold: float = 0.7,
    ) -> "CorruptionReport":
        """
        Get the corruption report to compare the given model versions.

        :param model_name: Name of the uploaded model of which versions are compared in the report.
        :param model_versions: List of model versions to compare in the report.
        :param dataset: Dataset to use for the comparison.
        :param subset: Subset whose observations are used for the comparison.
        :param metrics: List of distance metrics to consider in the comparison.
        :param success_metric_threshold: Threshold used to convert
                                        a success metric score to a binary success criterion.
        :return: Instance of the corruption report.
        """
        if metrics is None:
            metrics = []
        model_version_names = [
            model_version.name if isinstance(model_version, MLModelVersion) else model_version
            for model_version in model_versions
        ]
        dataset_name = dataset.name if isinstance(dataset, Dataset) else dataset
        subset_name = subset.name if isinstance(subset, Subset) else subset
        api_service = get_api_client()
        report = CorruptionReport(
            api_service=api_service,
            report_response=await ReportAPI(api_service).get_corruption_report(
                request=ReportRequest(
                    model=model_name,
                    model_versions=model_version_names,
                    dataset=dataset_name,
                    subset=subset_name,
                    metrics=metrics,
                    success_metric_threshold=success_metric_threshold,
                )
            ),
        )
        report.model = model_name
        return report

    def _fill_plot_with_data(self, plot: alt.LayerChart) -> alt.LayerChart:
        plot_copy = plot.copy(deep=True)
        odd_parameters = DataFrame.from_records(
            list(self.odd_parameters.items()), columns=["observation_id", "odd_parameters"]
        )
        plot_copy.datasets = {
            "data": alt.to_values(self.data)["values"],
            "odd_parameters": alt.to_values(odd_parameters)["values"],
        }
        return plot_copy

    @property
    def model_comparison_plot(self) -> alt.LayerChart:
        """
        Get the model-comparison altair plot.

        :return: Altair plot comparing the corruption robustness of the model
            versions.
        """
        return self._fill_plot_with_data(
            alt.LayerChart.from_dict(self._data.plot_recipes.model_comparison_mfr)
        )

    @property
    def odd_comparison_plot(self) -> alt.LayerChart:
        """
        Get the ODD-comparison altair plot.

        :return: Altair plot comparing the corruption robustness within
            different ODD sections.
        """
        return self._fill_plot_with_data(
            alt.LayerChart.from_dict(self._data.plot_recipes.odd_comparison_mfr)
        )

    @property
    def summary_statistics(self) -> DataFrame:
        """
        A pandas DataFrame containing summary statistics about the model
        robustness within different ODD sections.

        :return: DataFrame containing the summary statistics.
        """
        return self._get_model_comparison_stats(self._data.stats.model_comparison_stats)

    async def get_detail_view(self, perturbed_observation_id: int) -> widgets.VBox:
        """
        Return the detail for a given corruption.

        This method automatically selects the view corresponding to the model task.

        :param perturbed_observation_id: ID specifying the corruption.
        :raises ValueError: If invalid output type is passed.
        :return: View as ipython widget.
        """
        if self._data.output_type == OutputType.CLASSIFICATION:
            return await self._get_classification_detail_view(
                perturbed_observation_id=perturbed_observation_id
            )
        raise ValueError(
            f"Unsupported output type {self._data.output_type}. Should be 'CLASSIFICATION'."
        )

    @classmethod
    def _get_model_comparison_stats(
        cls,
        stats_dict: Dict[
            str, Dict[str, Dict[str, Dict[str, Dict[str, Dict[str, ModelNormStats]]]]]
        ],
    ) -> DataFrame:
        metrics_to_stat_mapper: Dict[
            Tuple[str, str, str, str, str], Dict[Tuple[str, str], float]
        ] = defaultdict(dict)
        for odd_param, odd_stats in stats_dict.items():
            for model_version, model_stats in odd_stats.items():
                for (
                    distance_metric,
                    success_metric,
                    target_class,
                    method_name,
                ), stats in cls._nested_dict_to_tuple_dict(model_stats).items():
                    for stat_name, stat_value in stats:
                        metrics_to_stat_mapper[
                            (distance_metric, success_metric, target_class, method_name, stat_name)
                        ][odd_param, model_version] = stat_value
        df = DataFrame(metrics_to_stat_mapper)
        df.index.names = ("ODD Tag", "Model Version")
        return df

    @staticmethod
    def _nested_dict_to_tuple_dict(
        nested_dict: Dict[str, Dict[str, Dict[str, Dict[str, ModelNormStats]]]]
    ) -> Dict[Tuple[str, str, str, str], ModelNormStats]:
        return_dict: Dict[Tuple[str, str, str, str], ModelNormStats] = {}
        for index_1, dict_1 in nested_dict.items():
            for index_2, dict_2 in dict_1.items():
                for index_3, dict_3 in dict_2.items():
                    for index_4, stats in dict_3.items():
                        return_dict[(index_1, index_2, index_3, index_4)] = stats
        return return_dict

    @property
    def odd_parameters(self) -> Dict[int, List[str]]:
        """
        Get the ODD parameters of the observations in the report.

        :return: A dictionary mapping each observation ID referenced in the
            report to a list of ODD parameters.
        """
        return {int(key): value for key, value in self._data.odd_parameters.items()}
