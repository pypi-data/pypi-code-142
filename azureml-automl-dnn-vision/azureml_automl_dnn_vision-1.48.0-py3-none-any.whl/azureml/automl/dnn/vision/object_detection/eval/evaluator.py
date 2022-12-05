# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""Object detection and segmentation evaluation helper """

import copy
import itertools
import torch

from typing import List, Dict, Union
from azureml.automl.core.shared.constants import Tasks
from azureml.automl.dnn.vision.common import distributed_utils
from azureml.automl.dnn.vision.common.average_meter import AverageMeter
from azureml.automl.dnn.vision.common.constants import SettingsLiterals as CommonSettingsLiterals, \
    TrainingLiterals as CommonTrainingLiterals
from azureml.automl.dnn.vision.object_detection.common import masktools
from azureml.automl.dnn.vision.object_detection.common.coco_eval_box_converter import COCOEvalBoxConverter
from azureml.automl.dnn.vision.object_detection.common.constants import ValidationMetricType, \
    TrainingLiterals, TilingLiterals
from azureml.automl.dnn.vision.object_detection.common.tiling_helper import SameImageTilesVisitor
from azureml.automl.dnn.vision.object_detection.data.dataset_wrappers import DatasetProcessingType
from azureml.automl.dnn.vision.object_detection.eval import cocotools
from azureml.automl.dnn.vision.object_detection.eval.incremental_voc_evaluator import IncrementalVocEvaluator


class OdEvaluator():
    """Object detection and segmentation evaluation helper"""
    def __init__(self, settings, val_index_map, dataset_processing_type, dataset_wrapper=None) -> None:
        """
        :param settings: Dictionary with all training and model settings
        :type settings: dict
        :param val_index_map: Map from numerical indices to class names
        :type val_index_map: List of strings
        :param dataset_processing_type: Map from numerical indices to class names
        :type dataset_processing_type: object_detection.data.dataset_wrappers.DatasetProcessingType
        :param dataset_wrapper: Dataset for evaluations
        :type dataset_wrapper: CommonObjectDetectionDatasetWrapper object (see object_detection.data.dataset_wrappers)
        """
        self.enabled = False
        self.log_validation_loss = settings.get(CommonSettingsLiterals.LOG_VALIDATION_LOSS, False)
        self.task_type = settings[CommonSettingsLiterals.TASK_TYPE]
        self.val_metric_type = settings[TrainingLiterals.VALIDATION_METRIC_TYPE]
        self.val_iou_threshold = settings[TrainingLiterals.VALIDATION_IOU_THRESHOLD]
        self.tile_predictions_nms_thresh = settings[TilingLiterals.TILE_PREDICTIONS_NMS_THRESH]
        self.primary_metric = settings[CommonTrainingLiterals.PRIMARY_METRIC]
        self.val_index_map = val_index_map
        self.dataset_processing_type = dataset_processing_type
        self.distributed = distributed_utils.dist_available_and_initialized()

        self.coco_metric_time = AverageMeter()
        self.voc_metric_time = AverageMeter()
        self.tiling_merge_predictions_time = AverageMeter()
        self.tiling_nms_time = AverageMeter()

        self.eval_coco = self.val_metric_type in ValidationMetricType.ALL_COCO
        self.eval_voc = self.val_metric_type in ValidationMetricType.ALL_VOC

        # Setup evaluation tools
        self.val_coco_index = None
        if self.eval_coco:
            self.val_coco_index = cocotools.create_coco_index(dataset_wrapper)

        # Initialize mechanism to group together the tiled targets and predictions for an image.
        self.tiling_visitor = SameImageTilesVisitor(
            self._do_evaluation_step, self.tile_predictions_nms_thresh,
            self.tiling_merge_predictions_time, self.tiling_nms_time
        )

    def initialize(self, enable_evaluation: bool):
        """ Initialize incremental voc/coco evaluator """
        self.enabled = enable_evaluation
        if self.enabled:
            # need to do this before each epoch
            if self.eval_voc:
                self.incremental_voc_evaluator = IncrementalVocEvaluator(
                    self.task_type == Tasks.IMAGE_OBJECT_DETECTION, len(self.val_index_map), self.val_iou_threshold
                )
            if self.eval_coco:
                self.coco_eval_box_converter = COCOEvalBoxConverter(self.val_index_map)

    def start_evaluation(self):
        "set local voc evaluator"
        # If distributed computation, use copy of original evaluator; otherwise, use original evaluator.
        if self.enabled and self.eval_voc:
            self.incremental_voc_evaluator_local = copy.deepcopy(self.incremental_voc_evaluator) if self.distributed \
                else self.incremental_voc_evaluator

    def _convert_targets_to_objects_per_image(self, targets_per_image, image_infos):
        # Note: image_infos is needed in inherited class YoloEvaluator
        gt_objects_per_image = [
            {
                "boxes": targets["boxes"].detach().cpu().numpy(),
                "masks": [
                    masktools.encode_mask_as_rle(mask.detach().cpu()) for mask in targets["masks"]
                ] if "masks" in targets else None,
                "classes": targets["labels"].detach().cpu().numpy(),
                "scores": None
            }
            for targets in targets_per_image
        ]

        return gt_objects_per_image

    def _convert_predictions_to_objects_per_image(self, predictions_with_info_per_image):
        # Go through the images and convert the boxes, labels and scores to format consumed by incremental evaluator.
        predicted_objects_per_image = [
            {
                "boxes": predictions["boxes"].numpy(), "masks": predictions.get("masks", None),
                "classes": predictions["labels"].numpy(),
                "scores": predictions["scores"].numpy()
            }
            for predictions in predictions_with_info_per_image
        ]
        return predicted_objects_per_image

    def _create_predictions_with_info_for_tile_grouping(self, predictions, image_info):
        predictions_with_info = {}
        predictions_with_info.update(image_info)
        predictions_with_info.update(predictions)

        # move predicted labels to cpu to save gpu memory
        predictions_with_info["boxes"] = predictions_with_info["boxes"].detach().cpu()
        predictions_with_info["labels"] = predictions_with_info["labels"].detach().cpu()
        predictions_with_info["scores"] = predictions_with_info["scores"].detach().cpu()

        # encode masks as rle to save memory
        masks = predictions_with_info.get("masks", None)
        if masks is not None:
            masks = masks.detach().cpu()
            masks = (masks > 0.5)
            rle_masks = []
            for mask in masks:
                rle = masktools.encode_mask_as_rle(mask)
                rle_masks.append(rle)
            predictions_with_info["masks"] = rle_masks

        return predictions_with_info

    def _do_evaluation_step(self, targets_per_image, predictions_with_info_per_image, image_infos):
        # Convert labels and predictions to input format of incremental evaluator.
        gt_objects_per_image = self._convert_targets_to_objects_per_image(targets_per_image, image_infos)
        predicted_objects_per_image = self._convert_predictions_to_objects_per_image(
            predictions_with_info_per_image)

        # If required, save the current batch of predictions.
        if self.eval_coco:
            self.coco_eval_box_converter.add_predictions(predictions_with_info_per_image)

        # If required, run incremental evaluator on the current batch of labels and predictions.
        if self.eval_voc:
            self.incremental_voc_evaluator_local.evaluate_batch(
                gt_objects_per_image, predicted_objects_per_image, image_infos
            )

    def evaluate_predictions(self, predictions_per_image: Union[List[Dict], List[torch.tensor]],
                             image_infos : List[Dict],
                             targets_per_image : List[Dict]) -> None:
        """ Evaluate predictions
        predictions_per_image:
        example for od:
            [{
                "boxes": torch.tensor([[1, 0, 2, 100]], dtype=torch.float32),
                "labels": torch.tensor([0]),
                "scores": torch.tensor([0.5]),
                "masks": torch.Size([1, height, width])
                "filename": "image_1.jpg",
            },]
        example for yolo:
            [torch.tenosr with shape: nx6 (x, y, w, h, conf, cls)]]
            x,y,w,h should be normalized coefficients.

        image_infos:
        example:
            [{
                "width": 640, "height": 640,
                "original_width": 640, "original_height": 640,
                "filename": "image_1.jpg", "areas": [60000],
                "iscrowd": np.array([False, False, False])
            },]
        targets_per_image:
        example:
                [ {
                    "boxes": torch.tensor([[1, 0, 2, 100]], dtype=torch.float32),
                    "labels": torch.tensor([0]),
                    "scores": None,
                    "masks": torch.Size([1, height, width])
                },]

        :param predictions_per_image: Predicted info for each image
        :type:  Union[list of dict, list of torch.tensors]
        :param image_infos: Meta information for each image.
        :type: list of dict
        :param targets_per_image: Ground truth objects for each image.
        :type: list of dict
        """
        # Convert predictions to format suitable for tile grouping.
        predictions_with_info_per_image = [
            self._create_predictions_with_info_for_tile_grouping(predictions, image_info)
            for predictions, image_info in zip(predictions_per_image, image_infos)
        ]

        if self.dataset_processing_type == DatasetProcessingType.IMAGES_AND_TILES:
            # Feed targets and predictions to the tiling visitor, which will group by image and run evaluation.
            self.tiling_visitor.visit_batch(targets_per_image, predictions_with_info_per_image, image_infos)
        else:
            # Evaluate current batch.
            self._do_evaluation_step(targets_per_image, predictions_with_info_per_image, image_infos)

    def finalize_evaluation(self):
        """ finalize evaluation"""
        if not self.enabled:
            return None

        if self.dataset_processing_type == DatasetProcessingType.IMAGES_AND_TILES:
            # Do evaluation for the tiles of the last image.
            self.tiling_visitor.finalize()

        # Evaluate bounding boxes
        eval_bounding_boxes = []
        # If required, convert predicted boxes to format used in COCO-style evaluation.
        if self.eval_coco:
            eval_bounding_boxes = self.coco_eval_box_converter.get_boxes()

        # If distributed computation, aggregate evaluation data.
        if self.distributed:
            if self.eval_coco:
                # Gather eval bounding boxes from all processes.
                eval_bounding_boxes_list = distributed_utils.all_gather(eval_bounding_boxes)
                eval_bounding_boxes = COCOEvalBoxConverter.aggregate_boxes(eval_bounding_boxes_list)

            # Agregate the partial results in all evaluators, saving them in the original.
            if self.eval_voc:
                incremental_voc_evaluators = distributed_utils.all_gather(self.incremental_voc_evaluator_local)
                self.incremental_voc_evaluator.set_from_others(incremental_voc_evaluators)
        self.eval_bounding_boxes = eval_bounding_boxes
