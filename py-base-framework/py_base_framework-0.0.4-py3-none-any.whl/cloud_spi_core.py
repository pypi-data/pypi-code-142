from logging.config import dictConfig

from flask import Flask, request

from py_base_framework.cloud_spi_log import log_config
import py_base_framework.cloud_spi_web

dictConfig(log_config)

app = Flask(__name__)
