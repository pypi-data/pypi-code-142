#!/usr/bin/env python

import argparse
import logging
import sys
from datetime import date
from pathlib import Path
import atexit

import utilities.config as cfg
from data import (TrainingDataSlicer, get_settings_data)
from model import VolSeg2dTrainer
from utilities import CheckExt
import vsui_client.vsui_client as vsui_client

def init_argparse() -> argparse.ArgumentParser:
    """Custom argument parser for this program.

    Returns:
        argparse.ArgumentParser: An argument parser with the appropriate
        command line args contained within.
    """
    parser = argparse.ArgumentParser(
        usage="%(prog)s --data <path(s)/to/data/file(s)> --labels <path(s)/to/segmentation/file(s)> --data_dir path/to/data_directory",
        description="Train a 2d U-net model on the 3d data and corresponding"
        " segmentation provided in the files."
    )
    parser.add_argument(
        "-v", "--version", action="version",
        version=f"{parser.prog} version 1.0.0"
    )
    parser.add_argument("--" + cfg.TRAIN_DATA_ARG, metavar='Path(s) to training image data volume(s)', type=str,
                        action=CheckExt(cfg.TRAIN_DATA_EXT),
                        nargs="+", required=True,
                        help='the path(s) to file(s) containing the imaging data volume for training')
    parser.add_argument("--" + cfg.LABEL_DATA_ARG, metavar='Path(s) to label volume(s)', type=str,
                        action=CheckExt(cfg.LABEL_DATA_EXT),
                        nargs="+", required=True,
                        help='the path(s) to file(s) containing a segmented volume for training')
    parser.add_argument("--" + cfg.DATA_DIR_ARG, metavar='Path to settings and output directory (optional)', type=str,
                        nargs="?", default=Path.cwd(),
                        help='path to a directory containing the "unet-settings", data will be also be output to this location')
    parser.add_argument(
        "--" + cfg.VSUI_PROCESS_ID_ARG,
        metavar="ID for VSUI (required for VSUI Integration)",
        type=str,
        nargs="?",
        default="vsui_disabled",
        help="unique task id for this process in gui"
    )
    return parser

def main():
    def exit_handler():
        vsui_client.disconnect()

    atexit.register(exit_handler)
    
    logger = logging.getLogger()
    handler = vsui_client.RequestHandler()
    logging.basicConfig(
        level=logging.INFO, format=cfg.LOGGING_FMT, datefmt=cfg.LOGGING_DATE_FMT
    )
    logger.addHandler(handler)
    # Parse args and check correct number of volumes given
    parser = init_argparse()
    args = parser.parse_args()
    data_vols = getattr(args, cfg.TRAIN_DATA_ARG)
    label_vols = getattr(args, cfg.LABEL_DATA_ARG)
    vsui_id = getattr(args, cfg.VSUI_PROCESS_ID_ARG)
    if vsui_id != "vsui_disabled":
        vsui_client.set_task_id(vsui_id)
        vsui_client.set_logging_target('Logs')
        vsui_client.connect()

    if isinstance(data_vols, str):
        data_vols = [Path(data_vols)]
    if isinstance(label_vols, str):
        label_vols = [Path(label_vols)]

    root_path = Path(getattr(args, cfg.DATA_DIR_ARG)).resolve()
    logging.info(f'root_path: {root_path}')

    # Create the settings object
    settings_path = Path(root_path, cfg.SETTINGS_DIR, cfg.TRAIN_SETTINGS_FN)
    settings = get_settings_data(settings_path)

    if len(data_vols) != len(label_vols):
        logging.error(
            "Number of data volumes and number of label volumes must be equal!"
        )
        sys.exit(1)

    data_im_out_dir = root_path / settings.data_im_dirname  # dir for data imgs
    seg_im_out_dir = root_path / settings.seg_im_out_dirname  # dir for seg imgs
    # Keep track of the number of labels
    max_label_no = 0
    label_codes = None
    # Set up the DataSlicer and slice the data volumes into image files
    for count, (data_vol_path, label_vol_path) in enumerate(zip(data_vols, label_vols)):
        slicer = TrainingDataSlicer(data_vol_path, label_vol_path, settings)
        data_prefix, label_prefix = f"data{count}", f"seg{count}"
        slicer.output_data_slices(data_im_out_dir, data_prefix)
        slicer.output_label_slices(seg_im_out_dir, label_prefix)
        if slicer.num_seg_classes > max_label_no:
            max_label_no = slicer.num_seg_classes
            label_codes = slicer.codes
    assert label_codes is not None
    # Set up the 2dTrainer
    trainer = VolSeg2dTrainer(data_im_out_dir, seg_im_out_dir, max_label_no, settings)
    # Train the model, first frozen, then unfrozen
    num_cyc_frozen = settings.num_cyc_frozen
    num_cyc_unfrozen = settings.num_cyc_unfrozen
    model_type = settings.model["type"].name
    model_fn = f"{date.today()}_{model_type}_{settings.model_output_fn}.pytorch"
    model_out = Path(root_path, model_fn)
    trainer.output_comparison_figures()
    vsui_client.notify('training started', 'info')
    if num_cyc_frozen > 0:
        trainer.train_model(
            model_out, num_cyc_frozen, settings.patience, create=True, frozen=True
        )
    if num_cyc_unfrozen > 0 and num_cyc_frozen > 0:
        trainer.train_model(
            model_out, num_cyc_unfrozen, settings.patience, create=False, frozen=False
        )
    elif num_cyc_unfrozen > 0 and num_cyc_frozen == 0:
        trainer.train_model(
            model_out, num_cyc_unfrozen, settings.patience, create=True, frozen=False
        )
    trainer.output_loss_fig(model_out)
    trainer.output_prediction_figure(model_out)
    # Clean up all the saved slices
    slicer.clean_up_slices()
    vsui_client.notify('training completed', 'success')
    vsui_client.deactivate_task()
    vsui_client.disconnect()


if __name__ == "__main__":
    main()
