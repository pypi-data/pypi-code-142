import ast
import os
import pathlib
import tempfile
import zipfile

import click
import rioxarray as rxr
import utm
import xarray as xr

from lfmaptools.netcdf_utils import lfnc
from lfmaptools.utilities import _path_of_file_in_zip, latlon_to_utm_epsg


class PythonLiteralOption(click.Option):
    def type_cast_value(self, ctx, value):
        try:
            return ast.literal_eval(value)
        except:
            raise click.BadParameter(value)


class PathPath(click.Path):
    """A Click path argument that returns a pathlib Path, not a string"""

    def convert(self, value, param, ctx):
        return pathlib.Path(super().convert(value, param, ctx))


@click.command()
@click.argument(
    "input_dir",
    type=PathPath(
        exists=True,
        file_okay=True,
        dir_okay=True,
        writable=False,
        readable=True,
    ),
)
@click.argument(
    "input_file",
    type=PathPath(
        exists=False,
        file_okay=True,
        dir_okay=False,
        writable=False,
        readable=True,
    ),
)
@click.option(
    "-odir",
    "--output_dir",
    "outdir",
    type=PathPath(
        exists=False,
        file_okay=False,
        dir_okay=True,
        writable=True,
        readable=True,
    ),
    prompt="Set output directory",
    default=os.getcwd(),
)
@click.option(
    "-o",
    "--out_filename",
    "file_out",
    type=click.File(mode="w"),
    is_flag=False,
    flag_value=None,
)
@click.option(
    "-v",
    "-var",
    "var",
    type=click.STRING,
    multiple=True,
)
def lf_to_gtif(input_dir, input_file, outdir, file_out, var):

    print(f"input_dir: {input_dir}")
    print(f"input_file: {input_file}")

    print(f"file_out: {file_out}")
    print(f"var: {var}")

    if input_dir.is_dir():
        zipped = False
    else:
        if input_dir.suffix == ".zip":
            zipped = True
        else:
            raise ValueError(
                f"Input directory {input_dir} neither a LaharFlow zip file nor a directory"
            )

    with tempfile.TemporaryDirectory() as tmpdirname:

        if zipped:
            zipref = zipfile.ZipFile(input_dir, "r")
            infoFilePath = _path_of_file_in_zip("RunInfo.txt", zipref)[0]
            print(f"infoFilePath: {infoFilePath}")
            zipref.extract(infoFilePath, tmpdirname)

            resultFilePath = _path_of_file_in_zip(input_file.name, zipref)[0]
            print(f"resultFilePath: {resultFilePath}")
            zipref.extract(resultFilePath, tmpdirname)

            zipref.close()

            info_file = os.path.join(tmpdirname, "RunInfo.txt")
            result_file = os.path.join(tmpdirname, resultFilePath)

            print(f"result_file = {result_file}")
            print(f"{os.listdir(tmpdirname)}")

            ncdata = lfnc(result_file)

            centre_latitude = ncdata.get_attr("centre_latitude")
            centre_longitude = ncdata.get_attr("centre_longitude")

            utm_full = utm.from_latlon(centre_latitude, centre_longitude)
            utmCode = latlon_to_utm_epsg(centre_latitude, centre_longitude)

            raster = ncdata.to_xarray(vars=list(var))

            coords = list(raster.coords.keys())
            if "x_distance" in coords:
                raster = raster.rename({"x_distance": "x"})
            if "y_distance" in coords:
                raster = raster.rename({"y_distance": "y"})
            raster["x"] = raster["x"] + utm_full[0]
            raster["y"] = raster["y"] + utm_full[1]
            raster.rio.write_crs(utmCode, inplace=True)

        else:
            print("Currently only works for netcdf files")
            return
            # info_file = os.path.join(input_dir, "RunInfo.txt")
            # if not os.path.isfile(info_file):
            #     print(f"Run info file {info_file} does not exist")
            # result_file = os.path.join(input_dir, input_file.name)

    fileOut = os.path.join(outdir, file_out.name)

    print("Writing file to {}".format(fileOut))
    raster.rio.to_raster(fileOut)
