#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os.path as osp
from poppy.core.logger import logger
import sys

from xml.dom import minidom
from xml.etree import ElementTree
from .xmltodict import xmltodict as xml

__all__ = ["loadXML", "prettify"]




def loadXML(filename, *args, **kwargs):
    """
    To load a file in xml format.
    """
    # check file existence
    if not osp.isfile(filename):
        logger.error(
            "File not found: {0}!".format(filename)
        )
        sys.exit(-1)

    # read the file and parse the xml structure to a dictionary
    logger.info("Loading {0}...".format(filename))
    with open(filename, 'r') as f:
        config = xml.parse(f.read(), *args, **kwargs)

    return config


def prettify(element, indent="\t", encoding="utf-8"):
    """
    To make a nice print of an element of an XML tree.
    """
    rough_string = ElementTree.tostring(element, encoding)
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent=indent)


# vim: set tw=79 :
