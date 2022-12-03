#!/usr/bin/env python3

# Standard libraries
from argparse import Namespace
from typing import List

# Components
from ..engines.engine import Engine

# ImagesFeature class
class ImagesFeature:

    # Members
    __engine = None
    __images: List[str]
    __options: Namespace

    # Constructor
    def __init__(self, jobs, options: Namespace) -> None:

        # Prepare container images
        self.__images = []
        for job in jobs:

            # Extract container image
            image = jobs[job]['image']
            if image and not jobs[job]['options'].host and image not in self.__images:
                self.__images += [image]

            # Extract container services
            for service in jobs[job]['services']:
                if service['image'] not in self.__images:
                    self.__images += [service['image']]

        # Prepare container engine
        self.__engine = Engine(options)

        # Prepare options
        self.__options = options

    # Pull
    def pull(self) -> bool:

        # Pull container images
        if self.__images:
            self.__images.sort()
            for image in self.__images:
                self.__engine.pull(image, self.__options.force)

        # Result
        return bool(self.__images)

    # Remove images
    def rmi(self) -> bool:

        # Remove container images
        if self.__images:
            self.__images.sort()
            for image in self.__images:
                self.__engine.rmi(image)

        # Result
        return bool(self.__images)
