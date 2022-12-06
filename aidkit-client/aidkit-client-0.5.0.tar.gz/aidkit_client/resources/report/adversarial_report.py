"""
Resources for the Adversarial Report.
"""
from collections import defaultdict
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple, Union

import altair as alt
import numpy as np
import PIL.Image
from ipywidgets import widgets
from pandas import DataFrame

from aidkit_client._endpoints.models import (
    ImageObjectDetectionModelOutput,
    ModelNormStats,
    OutputType,
    ReportAdversarialResponse,
    ReportRequest,
)
from aidkit_client._endpoints.report import ReportAPI
from aidkit_client.aidkit_api import HTTPService
from aidkit_client.configuration import get_api_client
from aidkit_client.plotting.base_objects import (
    display_class_color,
    display_inference_per_class_widget,
    display_object_detection_box_count_widget,
    display_observation,
    display_selection_class_detection_widget,
    display_semantic_segmentation_inference_argmax_widget,
    display_static_observation_difference,
    display_table,
    get_inference_argmax_prediction,
    get_inference_per_class_confidence,
)
from aidkit_client.resources.dataset import Dataset, Subset
from aidkit_client.resources.ml_model import MLModelVersion
from aidkit_client.resources.report._base_report import (
    ModelComparisonView,
    PerturbedObservationDetails,
    _BaseReport,
)


@dataclass
class AttackDetailView:
    """
    Attack-detail view of the report.
    """

    plot: alt.LayerChart


@dataclass
class AttackComparisonView:
    """
    Attack-comparison view of the report.
    """

    plot: alt.LayerChart
    stats: Dict[str, DataFrame]


class AdversarialReport(_BaseReport):
    """
    A report which compares model versions.
    """

    _data: ReportAdversarialResponse

    def __init__(
        self, api_service: HTTPService, report_response: ReportAdversarialResponse
    ) -> None:
        """
        Create a new instance from the server response.

        :param api_service: Service instance to use for communicating with the
            server.
        :param report_response: Server response describing the report
            to be created.
        """
        self._data = report_response
        self._api_service = api_service
        self.model = ""

    @classmethod
    async def get(
        cls,
        model_name: str,
        model_versions: List[Union[str, MLModelVersion]],
        dataset: Union[str, Dataset],
        subset: Union[str, Subset],
        metrics: Optional[List[str]] = None,
        success_metric_threshold: float = 0.7,
    ) -> "AdversarialReport":
        """
        Get the adversarial report to compare the given model versions.

        :param model_name: Name of the uploaded model of which versions are compared in the report.
        :param model_versions: List of model versions to compare in the report.
        :param dataset: Dataset to use for the comparison.
        :param subset: Subset whose observations are used for the comparison.
        :param metrics: List of distance metrics to consider in the comparison.
        :param success_metric_threshold: Threshold used to convert
                                        a success metric score to a binary success criterion.
        :return: Instance of the adversarial report.
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
        report = AdversarialReport(
            api_service=api_service,
            report_response=await ReportAPI(api_service).get_adversarial_report(
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

    @staticmethod
    def _nested_dict_to_tuple_dict(
        nested_dict: Dict[str, Dict[str, Dict[str, ModelNormStats]]]
    ) -> Dict[Tuple[str, str, str], ModelNormStats]:
        return_dict: Dict[Tuple[str, str, str], ModelNormStats] = {}
        for index_1, dict_1 in nested_dict.items():
            for index_2, dict_2 in dict_1.items():
                for index_3, stats in dict_2.items():
                    return_dict[(index_1, index_2, index_3)] = stats
        return return_dict

    @classmethod
    def _get_model_comparison_stats(
        cls, stats_dict: Dict[str, Dict[str, Dict[str, Dict[str, ModelNormStats]]]]
    ) -> DataFrame:
        metrics_to_stat_mapper: Dict[Tuple[str, str, str, str], Dict[str, float]] = defaultdict(
            dict
        )
        for model_version, model_stats in stats_dict.items():
            for (
                distance_metric,
                success_metric,
                target_class,
            ), stats in cls._nested_dict_to_tuple_dict(model_stats).items():
                for stat_name, stat_value in stats:
                    metrics_to_stat_mapper[
                        (distance_metric, success_metric, target_class, stat_name)
                    ][model_version] = stat_value
        return DataFrame(metrics_to_stat_mapper)

    @classmethod
    def _get_attack_comparison_stats(
        cls,
        stats_dict: Dict[
            str, Dict[str, Dict[str, Dict[str, Dict[str, Dict[str, ModelNormStats]]]]]
        ],
    ) -> Dict[str, DataFrame]:
        model_version_df_dict: Dict[str, DataFrame] = {}
        for model_version, attack_dict in stats_dict.items():
            stats_dict_in_pandas_form: Dict[
                Tuple[str, str, str, str], Dict[Tuple[str, str], float]
            ] = defaultdict(dict)
            for attack_class, attack_class_stats in attack_dict.items():
                for param_string, attack_instance_stats in attack_class_stats.items():
                    for (
                        distance_metric,
                        success_metric,
                        target_class,
                    ), stats in cls._nested_dict_to_tuple_dict(attack_instance_stats).items():
                        for stat_name, stat_value in stats.dict().items():
                            stats_dict_in_pandas_form[
                                (distance_metric, success_metric, target_class, stat_name)
                            ][(attack_class, param_string)] = stat_value
                        model_version_df_dict[model_version] = DataFrame(
                            data=stats_dict_in_pandas_form
                        )
        return model_version_df_dict

    def _fill_plot_with_data(self, plot: alt.LayerChart) -> alt.LayerChart:
        plot_copy = plot.copy(deep=True)
        plot_copy.data = self.data
        return plot_copy

    @property
    def model_comparison_view(self) -> ModelComparisonView:
        """
        Get the model-comparison view of the report.

        :return: Model-comparison view containing a plot and summary statistics.
        """
        return ModelComparisonView(
            plot=self._fill_plot_with_data(
                alt.LayerChart.from_dict(self._data.plot_recipes.model_comparison_asr)
            ),
            stats=self._get_model_comparison_stats(self._data.stats.model_comparison_stats),
        )

    @property
    def attack_comparison_view(self) -> AttackComparisonView:
        """
        Get the attack-comparison view of the report.

        :return: Attack-comparison view containing a plot and summary statistics.
        """
        return AttackComparisonView(
            plot=self._fill_plot_with_data(
                alt.LayerChart.from_dict(self._data.plot_recipes.attack_comparison_asr)
            ),
            stats=self._get_attack_comparison_stats(
                stats_dict=self._data.stats.attack_comparison_stats
            ),
        )

    @property
    def attack_detail_view(self) -> AttackDetailView:
        """
        Get the attack-detail view of the report.

        :return: Attack-detail view containing a plot.
        """
        return AttackDetailView(
            plot=self._fill_plot_with_data(
                alt.LayerChart.from_dict(self._data.plot_recipes.attack_detail_asr)
            )
        )

    async def get_detail_view(self, perturbed_observation_id: int) -> widgets.VBox:
        """
        Return the detail for a given adversarial example.

        This method automatically selects the view corresponding to the model task.

        :param perturbed_observation_id: ID specifying the adversarial example.
        :raises ValueError: If invalid output type is passed.
        :return: View as ipython widget.
        """
        if self._data.output_type == OutputType.CLASSIFICATION:
            return await self._get_classification_detail_view(
                perturbed_observation_id=perturbed_observation_id
            )
        if self._data.output_type == OutputType.SEGMENTATION:
            return await self._get_semantic_segmentation_detail_view(
                adversarial_example_id=perturbed_observation_id
            )
        if self._data.output_type == OutputType.DETECTION:
            return await self._get_object_detection_detail_view(
                adversarial_example_id=perturbed_observation_id
            )

        raise ValueError(
            "Unsupported output type. Should be one of 'CLASSIFICATION', 'SEGMENTATION'\
                or 'DETECTION'."
        )

    async def _get_semantic_segmentation_detail_view(
        self, adversarial_example_id: int
    ) -> widgets.VBox:
        """
        Produce the semantic segmentation detail view for a given adversarial
        example.

        :param adversarial_example_id: ID specifying the adversarial example.
        :return: View as ipython widget.
        """
        aversarial_example_details = await (
            PerturbedObservationDetails.get_by_perturbed_observation_id(adversarial_example_id)
        )
        adversarial_example = await (
            aversarial_example_details.perturbed_observation_as_remote_file().fetch_remote_file()
        )
        observation = (
            await (await aversarial_example_details.observation)
            .as_remote_file()
            .fetch_remote_file()
        )
        observation_resource = await aversarial_example_details.observation

        # Display the observation and the adversarial example side by side
        original_observation_widget = display_observation(
            observation,
            title="<center><b>Original Observation</b></center>",
            caption=[("File", observation_resource.name), ("ID", str(observation_resource.id))],
        )
        perturbed_observation_widget = display_observation(
            adversarial_example,
            title="<center><b>Perturbed Observation</b></center>",
            caption=[("ID", str(adversarial_example_id))],
        )

        observation_box_widget = widgets.HBox(
            [
                original_observation_widget,
                perturbed_observation_widget,
            ]
        )

        # Perform a fex computation to display in the detail view
        target_classes = aversarial_example_details.inference_class_names
        n_classes = len(target_classes)

        # Transform the inference data into numpy arrays
        inference_array = np.array(aversarial_example_details.observation_inference_result.data)
        perturbed_inference_array = np.array(
            aversarial_example_details.perturbed_observation_inference_result.data
        )

        # Compute the images to show in the inference section of the detail view
        inference_per_class_confidence_images = get_inference_per_class_confidence(inference_array)
        perturbed_inference_per_class_confidence_images = get_inference_per_class_confidence(
            perturbed_inference_array
        )

        inference_argmax_image = get_inference_argmax_prediction(inference_array)
        perturbed_inference_argmax_image = get_inference_argmax_prediction(
            perturbed_inference_array
        )

        # Compute the coverage metrics
        inference_array_argmax = np.argmax(inference_array, axis=2)
        inference_array_perturbed_argmax = np.argmax(perturbed_inference_array, axis=2)

        coverage_original = (
            np.bincount(inference_array_argmax.flatten(), minlength=n_classes)
            / inference_array_argmax.size
        )
        coverage_perturbed = (
            np.bincount(inference_array_perturbed_argmax.flatten(), minlength=n_classes)
            / inference_array_perturbed_argmax.size
        )

        target_classes_properties = []
        target_classes_dropdown_options = []

        coverage_per_class: Dict[str, List[Union[str, float, int]]] = {}
        coverage_class_highlight: Dict[str, str] = {}

        # Iterate over the classes. Assign a color to them, create the dropdown
        # selector and prepare the coverage table.
        for i, target_class_name in enumerate(target_classes):

            color = display_class_color(i, n_classes, "turbo")
            target_classes_properties.append({"name": target_class_name, "color": color})

            target_classes_dropdown_options.append((target_class_name, i))

            coverage_per_class[target_class_name] = [
                f"{coverage_original[i]:.2%}",
                f"{coverage_perturbed[i]:.2%}",
            ]

            coverage_class_highlight[target_class_name] = color

        # All classes inference
        semantic_inference_widget = display_semantic_segmentation_inference_argmax_widget(
            observation,
            adversarial_example,
            inference_argmax_image,
            perturbed_inference_argmax_image,
            target_classes_properties,
        )

        # Specific class inference
        class_inference_per_class_widget = display_inference_per_class_widget(
            inference_per_class_confidence_images,
            perturbed_inference_per_class_confidence_images,
            target_classes_dropdown_options,
        )

        # Put the two inference widgets together
        inference_widget_tabs = widgets.Tab(
            children=[semantic_inference_widget, class_inference_per_class_widget]
        )
        for i, val in enumerate(["All classes", "Specific class"]):
            inference_widget_tabs.set_title(i, val)

        # Coverage widget
        coverage_table = display_table(
            data=coverage_per_class,
            header=["Original", "Perturbed"],
            table_width=500,
            highlight_row_header=coverage_class_highlight,
        )
        percentage_of_pixels_that_changed_class = (
            np.count_nonzero(inference_array_argmax - inference_array_perturbed_argmax)
            / inference_array_argmax.size
        )
        coverage_widget = widgets.VBox(
            [
                coverage_table,
                widgets.HTML(
                    value="<b>Percentage of pixels with changed prediction</b>: "
                    f"{percentage_of_pixels_that_changed_class:.2%}"
                ),
            ]
        )

        # Metrics widget
        metrics_table_widget = display_table(self._get_metrics_for_id(adversarial_example_id))
        pipeline_info_table_widget = display_table(
            self._get_pipeline_info_for_id(adversarial_example_id)
        )

        # Difference Widget
        difference_widget = display_static_observation_difference(observation, adversarial_example)

        view_elements = [
            inference_widget_tabs,
            coverage_widget,
            metrics_table_widget,
            pipeline_info_table_widget,
            difference_widget,
        ]
        view_element_headers = [
            "Model Inference",
            "Class Coverage",
            "Perturbation Size",
            "Perturbation Details",
            "Difference between Original and Perturbed Observation",
        ]

        return self._assemble_widgets_in_view(
            observation_box_widget, view_elements, view_element_headers
        )

    async def _get_object_detection_detail_view(self, adversarial_example_id: int) -> widgets.VBox:
        """
        Produce the object detection detail view for a given adversarial
        example.

        :raises ValueError: If inference output has wrong type.
        :param adversarial_example_id: ID specifying the adversarial example.
        :return: View as ipython widget.
        """
        artifact_details = await PerturbedObservationDetails.get_by_perturbed_observation_id(
            adversarial_example_id
        )
        adversarial_example: PIL.Image.Image = (
            await artifact_details.perturbed_observation_as_remote_file().fetch_remote_file()
        )
        observation_resource = await artifact_details.observation
        observation: PIL.Image.Image = (
            await observation_resource.as_remote_file().fetch_remote_file()
        )

        if not isinstance(
            artifact_details.observation_inference_result, ImageObjectDetectionModelOutput
        ) or not isinstance(
            artifact_details.perturbed_observation_inference_result, ImageObjectDetectionModelOutput
        ):
            raise ValueError("Model task is wrongly configured.")

        observation_inference = artifact_details.observation_inference_result.data
        adversarial_example_inference = artifact_details.perturbed_observation_inference_result.data

        observation_box_with_selector = display_selection_class_detection_widget(
            observation,
            adversarial_example,
            observation_inference,
            adversarial_example_inference,
            class_names=artifact_details.inference_class_names,
            observation_title="<center><b>Original Observation</b></center>",
            observation_caption=f"<center><b>File</b>: {observation_resource.name}, "
            f"<b>ID</b>: {observation_resource.id}</center>",
            perturbation_title="<center><b>Perturbed Observation</b></center>",
            perturbation_caption=f"<center><b>ID</b>: {adversarial_example_id}</center>",
        )

        difference_widget = display_static_observation_difference(observation, adversarial_example)

        box_count_widget = display_object_detection_box_count_widget(
            observation_inference,
            adversarial_example_inference,
            artifact_details.inference_class_names,
        )
        metrics_table_widget = display_table(self._get_metrics_for_id(adversarial_example_id))
        pipeline_info_table_widget = display_table(
            self._get_pipeline_info_for_id(adversarial_example_id)
        )

        view_elements = [
            box_count_widget,
            metrics_table_widget,
            pipeline_info_table_widget,
            difference_widget,
        ]
        view_element_headers = [
            "Bounding Boxes per Class",
            "Perturbation Size",
            "Perturbation Details",
            "Difference between Original and Perturbed Observation",
        ]

        return self._assemble_widgets_in_view(
            observation_box_with_selector, view_elements, view_element_headers
        )
