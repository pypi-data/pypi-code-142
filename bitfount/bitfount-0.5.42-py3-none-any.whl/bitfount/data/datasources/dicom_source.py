"""Module containing DICOMSource class.

DICOMSource class handles loading of DICOM data.
"""
from __future__ import annotations

from glob import glob
import logging
import os
from pathlib import Path
from typing import Any, Dict, Iterable, List, Union

import PIL
import numpy as np
import pandas as pd
import pydicom

from bitfount.data.datasources.base_source import BaseSource
from bitfount.data.exceptions import DataSourceError
from bitfount.types import _Dtypes
from bitfount.utils import delegates

logger = logging.getLogger(__name__)


@delegates()
class DICOMSource(BaseSource):
    """Data source for loading DICOM files.

    Args:
        path: The path to the directory containing the DICOM files.
        output_path: The path where to save the images from the DICOM files.
            Defaults to 'preprocessed/'.
        include_slo: Whether to include SLO_IR images from a separate file.
            Defaults to False. Ophthalmology-specific argument; refers
            to the scanning laser ophthalmoscope (SLO) image, typically
            referred to as an 'en-face' image of the retina.
        oct_string: The string pointing to oct files in the filename.
            Defaults to 'OCT'. Ophthalmology-specific argument; refers
            to the optical coherence tomography (OCT) image, typically
            these are a series of 2D images used to show a cross-section
            of the tissue layers in the retina, combined to form a 3D image.
        slo_string: The string pointing to slo files in the filename.
            Defaults to 'SLO_IR'. Ophthalmology-specific argument; refers
            to the scanning laser ophthalmoscope (SLO) image, typically
            referred to as an 'en-face' image of the retina.
        **kwargs: Keyword arguments passed to the BaseSource constructor.
    """

    def __init__(
        self,
        path: Union[os.PathLike, str],
        output_path: Union[os.PathLike, str] = "preprocessed/",
        include_slo: bool = False,
        oct_string: str = "OCT",
        slo_string: str = "SLO_IR",
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.path = Path(path)
        self.include_slo = include_slo
        self.oct_string = oct_string
        self.slo_string = slo_string
        self.out_path = Path(output_path)
        self.out_path.mkdir(exist_ok=True)
        if include_slo:
            # recursive load of all files within a specified path
            self.dicom_files = [
                y
                for x in os.walk(self.path)
                for y in glob(os.path.join(x[0], "*.dcm"))
                if self.slo_string not in y
            ]
        else:
            self.dicom_files = [
                y for x in os.walk(self.path) for y in glob(os.path.join(x[0], "*.dcm"))
            ]
        if not self.dicom_files:
            logger.warning("Didn't detect any DICOM files in the provided directory.")

    def get_values(
        self, col_names: List[str], **kwargs: Any
    ) -> Dict[str, Iterable[Any]]:
        """Get distinct values from columns in DICOM dataset.

        Args:
            col_names: The list of the columns whose distinct values should be
                returned.

        Returns:
            The distinct values of the requested column as a mapping from col name to
            a series of distinct values.
        """
        dic: Dict[str, Iterable[Any]] = {}
        for col in col_names:
            try:
                dic[col] = self.get_data()[col].unique()
            except TypeError:
                logger.warning(f"Found unhashable value type, skipping column {col}.")
        return dic

    def get_column(self, col_name: str, **kwargs: Any) -> Union[np.ndarray, pd.Series]:
        """Loads and returns single column from DICOM dataset.

        Args:
            col_name: The name of the column which should be loaded.

        Returns:
            The column request as a series.
        """
        dicom_df: pd.DataFrame = self.get_data()
        return dicom_df[col_name]

    def get_dtypes(self, **kwargs: Any) -> _Dtypes:
        """Loads and returns the columns and column types of the DICOM dataframe.

        Returns:
            A mapping from column names to column types.
        """
        dicom_df: pd.DataFrame = self.get_data()
        return self._get_data_dtypes(dicom_df)

    def get_data(self, **kwargs: Any) -> pd.DataFrame:
        """Loads and returns data from DICOM dataset.

        Returns:
            A DataFrame which contains the data.
        """
        dicom_list = []
        images_3d = False
        images_2d = False
        for filename in self.dicom_files:
            # Read each file in the dicom files.
            ds = pydicom.dcmread(filename, force=True)
            # Get the path of the file, which will be used for saving the image data.
            # First, get the filename without the extension.
            # This will be the folder name where the images will be saved.
            # We also use the same folder structure in the output path
            # as it was for the original dicom files
            file_id = os.path.join(
                os.path.split(os.path.split(filename)[0])[1], os.path.split(filename)[1]
            )
            save_prefix = self.out_path / file_id
            save_prefix.mkdir(parents=True, exist_ok=True)
            data = {}
            for elem in ds:
                if elem.name not in self._ignore_cols:
                    if elem.VR == "SQ":
                        # A DICOM file has different Value Representation (VR).
                        # Unfortunately we cannot support sequence data (SQ)
                        # for using it in dataframes, so we ignore those columns.
                        self._ignore_cols.append(elem.name)
                        logger.info(
                            f"Cannot process sequence data, ignoring column {elem.name}"
                        )
                    elif hasattr(elem, "VM") and elem.VM > 1:
                        # The Value Multiplicity of a Data Element specifies the number
                        # of Values that can be encoded in the Value Field of that Data
                        # Element. The VM of each Data Element is specified explicitly
                        # in PS3.6. If the number of Values that may be encoded in a
                        # Data Element is variable, it shall be represented by two
                        # numbers separated by a dash; e.g., "1-10" means that there
                        # may be 1 to 10 Values in the Data Element. Similar to the
                        # SQ case, dataframes do not support sequence data so we only
                        # take the first element.
                        data[elem.name] = elem[0]
                    elif elem.name != "Pixel Data":
                        # for all non-image fields, we take the value of the column
                        data[elem.name] = elem.value
                    elif elem.name == "Pixel Data":
                        # If there is an image, we get the pixel_array instead.
                        arr = ds.pixel_array
                        if int(ds.NumberOfFrames) > 1 and images_2d is False:
                            # If there is more than one frame, we load them separately
                            images_3d = True
                            for iter in range(int(ds.NumberOfFrames)):
                                # For each image in the 3d DICOM image,
                                # save each frame separately.
                                save_path = os.path.join(
                                    save_prefix,
                                    f"{ds.PatientID}-{ds.StudyDate}-{ds.StudyTime}-{iter}.png",
                                )
                                if not os.path.exists(save_path):
                                    # But don't save images again if they have
                                    # already been saved once.
                                    self._save_PIL_image_to_path(
                                        ds, arr[iter], save_path
                                    )
                                # For each image we assign a column according to the
                                # frames order and write in the df the path where
                                # the image is saved.
                                data[f"Pixel Data {iter}"] = save_path
                        elif int(ds.NumberOfFrames) > 1 and images_2d is True:
                            # If we already processed at least one 2d image,
                            # we cannot process 3d images, so we raise an error.
                            raise (
                                DataSourceError(
                                    "The data provided has a mix of both 3d and 2d "
                                    "images. Please make sure that the files provided"
                                    " contains only 3d or only 2d images."
                                )
                            )
                        else:
                            if images_3d is True:
                                # If we already processed at least one 3d image,
                                # we cannot process 2d images, so we raise an error.
                                raise (
                                    DataSourceError(
                                        "The data provided has a mix of both 3d and 2d "
                                        "images. Please make sure that the files "
                                        "provided contains only 3d or only 2d images."
                                    )
                                )
                            images_2d = True
                            save_path = os.path.join(
                                save_prefix,
                                f"{ds.PatientID}-{ds.StudyDate}-{ds.StudyTime}.png",
                            )
                            if not os.path.exists(save_path):
                                self._save_PIL_image_to_path(ds, arr, save_path)
                            data["Pixel Data"] = save_path
            if self.include_slo:
                # Ophthalmology specific, if include_slo is true we can
                # process SLO images as well.
                slo_filename = filename.replace(self.oct_string, self.slo_string)
                # Check that the string has been replaced
                # and that the filename exists
                if os.path.exists(slo_filename) and filename != slo_filename:
                    slo_ds = pydicom.dcmread(slo_filename, force=True)
                    slo_path = os.path.join(
                        save_prefix,
                        f"{ds.PatientID}-{ds.StudyDate}-{ds.StudyTime}-SLO_IR.png",
                    )
                    if not os.path.exists(slo_path):
                        self._save_PIL_image_to_path(
                            slo_ds, slo_ds.pixel_array, slo_path
                        )
                    data["SLO Image Data"] = save_path
                else:
                    logger.warning(
                        "`include_slo` was set to True, but no corresponding "
                        "SLO file found. Make sure that your filename is the "
                        "same as the OCT file and SLO_IR replaces `OCT` for "
                        "the slo file."
                    )
            dicom_list.append(data)
        df = pd.DataFrame.from_records(dicom_list)
        return df

    def __len__(self) -> int:
        return len(self.get_data())

    @property
    def multi_table(self) -> bool:
        """Attribute to specify whether the datasource is multi table."""
        return False

    @staticmethod
    def _get_LUT_value(data: np.ndarray, window: int, level: int) -> np.ndarray:
        """Apply the RGB Look-Up Table for the given data and window/level value."""
        return np.piecewise(
            data,
            [
                data <= (level - 0.5 - (window - 1) / 2),
                data > (level - 0.5 + (window - 1) / 2),
            ],
            [
                0,
                255,
                lambda data: ((data - (level - 0.5)) / (window - 1) + 0.5) * (255 - 0),
            ],
        )

    @staticmethod
    def _save_PIL_image_to_path(
        dataset: pydicom.FileDataset,
        pixel_array: np.ndarray,
        filename: Union[Path, str],
    ) -> None:
        """Get Image object from Python Imaging Library(PIL) and save it.

        Args:
            dataset: The DICOM data.
            pixel_array: The pixel array from the dataset.
            filename: The filepath where to save the image.
        """
        # We can only apply LUT if these window info exists
        if ("WindowWidth" not in dataset) or ("WindowCenter" not in dataset):
            bits = dataset.BitsAllocated
            samples = dataset.SamplesPerPixel
            # Different bits and samples configurations have different
            # modes for loading the images.
            if bits == 8 and samples == 1:
                mode = "L"
            elif bits == 8 and samples == 3:
                mode = "RGB"
            elif bits == 16:
                mode = "I;16"
            else:
                raise TypeError(
                    f"Don't know PIL mode for {bits} BitsAllocated "
                    f"and {samples} SamplesPerPixel"
                )

            size = (dataset.Columns, dataset.Rows)
            # Recommended to specify all details
            # by http://www.pythonware.com/library/pil/handbook/image.htm
            im = PIL.Image.frombuffer(mode, size, pixel_array, "raw", mode, 0, 1)
            im.save(filename, "PNG")
        else:
            ew = dataset.WindowWidth
            ec = dataset.WindowCenter
            image = DICOMSource._get_LUT_value(pixel_array, int(ew), int(ec))
            # Convert mode to L since LUT has only 256 values:
            #   http://www.pythonware.com/library/pil/handbook/image.htm
            im = PIL.Image.fromarray(image).convert("L")
            im.save(filename, "PNG")
