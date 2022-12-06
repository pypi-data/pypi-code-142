"""
Shared functionality for the adversarial and corruption reports.
"""

import json
import random
from abc import abstractmethod
from dataclasses import dataclass
from typing import Dict, List, Union

import altair as alt
import numpy as np
from ipywidgets import widgets
from pandas import DataFrame

from aidkit_client._endpoints.models import (
    ClassificationModelOutput,
    ImageObjectDetectionModelOutput,
    ImageSegmentationModelOutput,
    ReportAdversarialResponse,
    ReportCoreMethodOutputDetailResponse,
    ReportCorruptionResponse,
)
from aidkit_client._endpoints.report import ReportAPI
from aidkit_client.aidkit_api import HTTPService
from aidkit_client.configuration import get_api_client
from aidkit_client.plotting.base_objects import (
    display_observation,
    display_static_observation_difference,
    display_table,
)
from aidkit_client.resources.data_point import DataPointType, RemoteFile
from aidkit_client.resources.dataset import Observation


@dataclass
class ModelComparisonView:
    """
    Model-comparison view of the report.
    """

    plot: alt.LayerChart
    stats: DataFrame


class PerturbedObservationDetails:
    """
    Inference results from the report detail view corresponding to the original
    observation and a perturbed observation.
    """

    def __init__(
        self,
        api_service: HTTPService,
        adversarial_example_details: ReportCoreMethodOutputDetailResponse,
    ) -> None:
        """
        Create a new instance from the server detailed response.

        :param api_service: Service instance to use for communicating with the
            server.
        :param adversarial_example_details: Server response describing the inference results
            corresponding to a given perturbed observation.
        """
        self._api_service = api_service
        self._data = adversarial_example_details

    @classmethod
    async def get_by_perturbed_observation_id(
        cls, perturbed_observation_id: int
    ) -> "PerturbedObservationDetails":
        """
        Get detailed information on a perturbed observation.

        Information consists of:

        * Underlying observation*
        * Inference result of observation*
        * Inference result of perturbed observation*
        * Functionality to load content of perturbed observation*

        :param perturbed_observation_id: ID of the perturbed observation.
        :return: Instance of PerturbedObservationDetails.
        """
        api_service = get_api_client()
        return PerturbedObservationDetails(
            api_service=api_service,
            adversarial_example_details=await ReportAPI(
                api_service
            ).get_perturbed_observation_details(perturbed_observation_id=perturbed_observation_id),
        )

    @property
    def observation_id(self) -> int:
        """
        Get the ID of the original observation from which this perturbed
        observation was generated.

        :return: ID of the underlying observation.
        """
        return self._data.observation_id

    @property
    async def observation(self) -> Observation:
        """
        Get the original observation from which this perturbed observation was
        generated.

        :return: Instance of the underlying observation.
        """
        return await Observation.get_by_id(self.observation_id)

    @property
    def observation_inference_result(
        self,
    ) -> Union[
        ClassificationModelOutput, ImageSegmentationModelOutput, ImageObjectDetectionModelOutput
    ]:
        """
        Get the underlying observation inference results.

        :return: Instance containing the observation inference results.
        """
        return self._data.observation_inference_result

    @property
    def perturbed_observation_id(self) -> int:
        """
        Get the ID of the perturbed observation.

        :return: ID of the perturbed observation.
        """
        return self._data.core_method_output_id

    def perturbed_observation_as_remote_file(self) -> RemoteFile:
        """
        Get a perturbed observation as a RemoteFile object.

        :raises ValueError: if method output type is unknown.
        :return: Remote file.
        """
        if self._data.core_method_output_type in ["COLOR_IMAGE", "GREY_SCALE_IMAGE"]:
            data_type = DataPointType.IMAGE
        elif "TEXT" == self._data.core_method_output_type:
            data_type = DataPointType.TEXT
        else:
            raise ValueError(
                f"Unknown type for method output: '{self._data.core_method_output_type}'."
            )
        return RemoteFile(url=self._data.core_method_output_storage_url, type=data_type)

    @property
    def perturbed_observation_inference_result(
        self,
    ) -> Union[
        ClassificationModelOutput, ImageSegmentationModelOutput, ImageObjectDetectionModelOutput
    ]:
        """
        Get the perturbed observation inference results, i.e.: the softmax
        output of the model.

        :return: Instance containing the perturbed observation inference results.
        """
        return self._data.core_method_output_inference_result

    @property
    def inference_class_names(self) -> List[str]:
        """
        Class names for the classes in the inference result.

        :return: List of  class names.
        """
        return self._data.core_method_output_inference_result.class_names


class _BaseReport:
    """
    Base class for the corruption- and the adversarial report.
    """

    _data: Union[ReportCorruptionResponse, ReportAdversarialResponse]
    model = ""

    @property
    def data(self) -> DataFrame:
        """
        Get the data of the report.

        :return: DataFrame containing sample data for the report. The returned DataFrame has one row
            per combination of

            * Configured Method: All those perturbation methods which were run on all compared model
                versions and evaluated with all considered norms are included.
            * Observation: Observation: All observations in the subset the report is requested for.
            * Model Version: All model versions the report is requested for.
            * Metric Name: All norms the report is requested for.

            The returned DataFrame has the following columns:

            * ``successful``: Boolean; Whether the generated perturbation changed the model's
                prediction.
            * ``distance_metric_value``: Float; Distance between the perturbation and the original
                observation.
            * ``method_name``: Categorical; Name of the method used to create the perturbation.
            * ``param_string`` Categorical; Parameters for the method used to create the
                perturbation.
            * ``observation_id``: Integer; ID of the original observation the perturbation was
                created for.
            * ``artifact_id``: Integer; ID of the generated perturbation.
            * ``distance_metric_name``: Categorical; Name of the metric used to measure
                ``distance_metric_value``.
                One of the names in ``metric_names``.
            * ```model_version``: Categorical; Name of the model version the adversarial example was
                created for.
                One of the names in ``model_version_names``.
            * ```perturbation_type``: Categorical; Type of the perturbation, i.e.: 'Corruption'.
        """
        return DataFrame(self._data.data).astype(
            {
                "model_version": "category",
                "distance_metric_name": "category",
                "method_name": "category",
                "param_string": "category",
                "success_metric_type": "category",
                "target_class": "category",
                "perturbation_type": "category",
            }
        )

    def _get_pipeline_info_for_id(self, perturbed_observation_id: int) -> Dict:
        param_dict = json.loads(
            self.data[self.data["artifact_id"] == perturbed_observation_id]["param_string"].iloc[0]
        )
        model_version = self.data[self.data["artifact_id"] == perturbed_observation_id][
            "model_version"
        ].iloc[0]
        return {
            "Model": [f"Name: {self.model}<br>Version: {model_version}"],
            "Method Name": [
                self.data[self.data["artifact_id"] == perturbed_observation_id]["method_name"].iloc[
                    0
                ]
            ],
            "Type": [
                self.data[self.data["artifact_id"] == perturbed_observation_id][
                    "perturbation_type"
                ].iloc[0]
            ],
            "Parameters": [param_dict],
        }

    def _get_metrics_for_id(self, perturbed_observation_id: int) -> Dict:
        metric_df = self.data[self.data["artifact_id"] == perturbed_observation_id][
            ["distance_metric_name", "distance_metric_value"]
        ]
        metrics = {
            row["distance_metric_name"]: [f"{row['distance_metric_value']:.2f}"]
            for _, row in metric_df.iterrows()
        }
        return metrics

    @staticmethod
    def _assemble_widgets_in_view(
        observation_widget: widgets.CoreWidget,
        widget_list: List[widgets.CoreWidget],
        widget_header: List[str],
    ) -> widgets.VBox:
        """
        Assemble the different widgets into a single view.

        :param observation_widget: Widget displaying the observations (possibly with inference).
        :param widget_list: List of widgets to display beneath the observations.
        :param widget_header: Titles for the widgets in widget_list.
        :return: The assembled view as widget.
        """
        header_widget = widgets.HTML(value="<h1>Detail View</h1>")

        acc_list = []
        for i, widget in enumerate(widget_list):
            acc = widgets.Accordion(children=[widget])
            acc.set_title(0, widget_header[i])

            acc.layout.width = "605px"
            acc_list.append(acc)
        return widgets.VBox([header_widget, observation_widget] + acc_list)

    async def fetch_random_detail_views(
        self, number_of_inference_results: int
    ) -> List[PerturbedObservationDetails]:
        """
        Fetch a number of random detail views for the perturbed observations of
        the report. If the report has fewer perturbed observations than
        specified, all detail views are returned.

        :param number_of_inference_results: Number of detail views to return.
        :return: List of details views.
        """
        perturbed_observation_ids = list(self.data["artifact_id"].unique())
        out = [
            await PerturbedObservationDetails.get_by_perturbed_observation_id(
                perturbed_observation_id=perturbed_observation_id
            )
            for perturbed_observation_id in random.SystemRandom().sample(
                perturbed_observation_ids,
                k=min(len(perturbed_observation_ids), number_of_inference_results),
            )
        ]
        return out

    async def _get_classification_detail_view(self, perturbed_observation_id: int) -> widgets.VBox:
        """
        Produce the classification detail view for a given perturbed
        observation.

        :raises ValueError: If inference output has wrong type.
        :param perturbed_observation_id: ID specifying the perturbed observation.
        :return: View as ipython widget.
        """
        perturbed_obs_details = await PerturbedObservationDetails.get_by_perturbed_observation_id(
            perturbed_observation_id
        )
        perturbed_observation = (
            await perturbed_obs_details.perturbed_observation_as_remote_file().fetch_remote_file()
        )

        observation_resource = await perturbed_obs_details.observation
        observation = await observation_resource.as_remote_file().fetch_remote_file()
        original_observation_widget = display_observation(
            observation,
            title="<center><b>Original Observation</b></center>",
            caption=[("File", observation_resource.name), ("ID", str(observation_resource.id))],
        )
        perturbed_observation_widget = display_observation(
            perturbed_observation,
            title="<center><b>Perturbed Observation</b></center>",
            caption=[("ID", str(perturbed_observation_id))],
        )

        if isinstance(observation, str):
            observation_box = widgets.VBox
        else:
            observation_box = widgets.HBox

        observation_box_widget = observation_box(
            [
                original_observation_widget,
                perturbed_observation_widget,
            ]
        )

        difference_widget = display_static_observation_difference(
            observation, perturbed_observation
        )

        class_names = perturbed_obs_details.inference_class_names

        if not isinstance(
            perturbed_obs_details.observation_inference_result, ClassificationModelOutput
        ) or not isinstance(
            perturbed_obs_details.perturbed_observation_inference_result,
            ClassificationModelOutput,
        ):
            raise ValueError("Model task is wrongly configured.")

        observation_inference_result = perturbed_obs_details.observation_inference_result.data
        adversarial_example_inference_result = (
            perturbed_obs_details.perturbed_observation_inference_result.data
        )

        top_inference_classes = (
            list(np.array(observation_inference_result).argsort())[-5:]
            + list(np.array(adversarial_example_inference_result).argsort())[-5:]
        )

        prediction_original = np.array(observation_inference_result).argmax()
        prediction_adversarial = np.array(adversarial_example_inference_result).argmax()

        inference_table: Dict[str, List[Union[str, float, int]]] = {
            str(class_names[i]): [
                f"{float(observation_inference_result[i]):.2f}",
                f"{float(adversarial_example_inference_result[i]):.2f}",
            ]
            for i in set(top_inference_classes)
        }
        inference_table_header = ["Original observation", "Perturbed observation"]
        prediction_highlight = {str(class_names[prediction_original]): {0: "#c0edc0"}}
        if prediction_original == prediction_adversarial:
            prediction_highlight[str(class_names[prediction_adversarial])][1] = "#c0edc0"
        else:
            prediction_highlight[str(class_names[prediction_adversarial])] = {1: "#c0edc0"}
        inference_table_widget = display_table(
            inference_table, header=inference_table_header, highlight_cells=prediction_highlight
        )
        metrics_table_widget = display_table(self._get_metrics_for_id(perturbed_observation_id))
        pipeline_info_table_widget = display_table(
            self._get_pipeline_info_for_id(perturbed_observation_id)
        )

        view_elements = [
            inference_table_widget,
            metrics_table_widget,
            pipeline_info_table_widget,
            difference_widget,
        ]
        view_element_headers = [
            "Model Inference",
            "Perturbation Size",
            "Perturbation Details",
            "Difference between Original and Perturbed Observation",
        ]

        return self._assemble_widgets_in_view(
            observation_box_widget, view_elements, view_element_headers
        )

    @abstractmethod
    async def get_detail_view(self, perturbed_observation_id: int) -> widgets.VBox:
        """
        Return the detail view for a given perturbed observation.

        :param perturbed_observation_id: ID specifying the corruption.
        :return: View as ipython widget.
        """
