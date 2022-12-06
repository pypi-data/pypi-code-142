#!/usr/bin/env python3

import sys
import os

if __name__ == "__main__":

    # automatically add plugins from the plugins folder to the installed python package
    # uncomment the following lines to enable this option
    # ROOT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
    # plugins_path = os.path.join(ROOT_DIRECTORY, 'plugins')
    # for entry in os.listdir(plugins_path):
    #     dir_path = os.path.join(plugins_path, entry)
    #     if os.path.isdir(dir_path):
    #         sys.path.insert(0, dir_path)

    # run the pipeline
    try:
        from poppy.pop.scripts import main
    except ImportError as exc:
        raise ImportError(
            "Couldn't import poppy-pop. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc


    main()
