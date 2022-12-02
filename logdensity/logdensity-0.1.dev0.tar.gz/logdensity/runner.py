""" Run the command line interface """
import logging
import mrcfile
import shutil

import importlib.metadata

import logdensity

import numpy as np

import rich.console
import rich.logging

import logdensity.arguments


def create_rich_logger():
    FORMAT = "%(message)s"
    logging.basicConfig(level="INFO",
                        format=FORMAT,
                        datefmt="[%X]",
                        handlers=[rich.logging.RichHandler()])
    return logging.getLogger("rich")


def apply_floor(data, floor):
    
    data[data < floor] = floor
    return data

def run():
    """ run the command line interface """

    # set up the console for printing and logging
    console = rich.console.Console()
    log = create_rich_logger()

    # derive the program version via git
    try:
        version = importlib.metadata.version("mrcsmooth")
    except importlib.metadata.PackageNotFoundError:
        version = "Unknown"

    command_line_arguments = (
        logdensity.arguments.get_command_line_arguments(version))

    log.info("Reading density ...")

    # because copying mrcfile objects is hard, start out by copying the file
    shutil.copy2(command_line_arguments.density,
                 command_line_arguments.output_density)

    output_density = mrcfile.open(command_line_arguments.output_density,
                                  'r+',
                                  permissive=True)

    output_density.header.ispg = mrcfile.constants.VOLUME_SPACEGROUP

    log_data = np.log(apply_floor(output_density.data, command_line_arguments.floor))
    
    output_density.set_data(log_data)

    output_density.close()

    log.info("done")
