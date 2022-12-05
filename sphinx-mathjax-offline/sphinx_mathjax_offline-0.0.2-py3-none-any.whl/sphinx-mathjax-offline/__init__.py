import os
from sphinx.util.fileutil import copy_asset


def copy_mathjax_files(app, exc):
    ext_dir = os.path.dirname(os.path.abspath(__file__))
    mathjax_dir = ext_dir + "/static/mathjax"
    if exc is None: # build succeeded
        copy_asset(mathjax_dir, os.path.join(app.outdir, '_static', 'mathjax'))

def setup(app):
    app.connect('build-finished', copy_mathjax_files)
    app.config.mathjax_path = "mathjax/tex-chtml.js"
