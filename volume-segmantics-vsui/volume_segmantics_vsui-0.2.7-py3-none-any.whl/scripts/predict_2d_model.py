#!/usr/bin/env python

import logging
import warnings
from datetime import date
from pathlib import Path

import volume_segmantics.utilities.config as cfg
from volume_segmantics.data import get_settings_data
from volume_segmantics.model import VolSeg2DPredictionManager
from volume_segmantics.utilities import get_2d_prediction_parser
import vsui_client.vsui_client as vsui_client

warnings.filterwarnings("ignore", category=UserWarning)

def create_output_path(root_path, data_vol_path):
    pred_out_fn = f"{date.today()}_{data_vol_path.stem}_2d_model_vol_pred.h5"
    return Path(root_path, pred_out_fn)

@vsui_client.vsui_process()
def main():
    logger = logging.getLogger()
    handler = vsui_client.RequestHandler()
    logging.basicConfig(
        level=logging.INFO, format=cfg.LOGGING_FMT, datefmt=cfg.LOGGING_DATE_FMT
    )
    logger.addHandler(handler)
    # Parse Args
    parser = get_2d_prediction_parser()
    args = parser.parse_args()

    vsui_id = getattr(args, cfg.VSUI_PROCESS_ID_ARG)
    if vsui_id != "vsui_disabled":
        vsui_client.set_task_id(vsui_id)
        vsui_client.set_logging_target('Logs')
        vsui_client.connect()

    # Define paths
    root_path = Path(getattr(args, cfg.DATA_DIR_ARG)).resolve()
    print(f'rootpath: {root_path}')
    settings_path = Path(root_path, cfg.SETTINGS_DIR, cfg.PREDICTION_SETTINGS_FN)

    model_file_path = getattr(args, cfg.MODEL_PTH_ARG)
    data_vol_path = Path(getattr(args, cfg.PREDICT_DATA_ARG))

    if isinstance(model_file_path, str):
        model_file_path = Path(model_file_path)
        
    output_path = create_output_path(root_path, data_vol_path)
    print(f'model_file_path: {model_file_path}')
    print(f'data_vol_path: {data_vol_path}')
    print(f'output_path: {output_path}')

    # Get settings object
    settings = get_settings_data(settings_path)
    # Create prediction manager and predict
    pred_manager = VolSeg2DPredictionManager(model_file_path, data_vol_path, settings)
    pred_manager.predict_volume_to_path(output_path)
    vsui_client.notify('prediction completed', 'success')
    vsui_client.deactivate_task()
    vsui_client.disconnect()


if __name__ == "__main__":
    main()
