# dash stuff
import dash
import dash_bootstrap_components as dbc

# flask for the server
from flask import Flask
from flask_caching import Cache

# other things
from MS_visualizer.utils.toml import read_toml


# create the server
server = Flask(__name__)

# create the app
app = dash.Dash(__name__,
                server=server,
                external_stylesheets=[dbc.themes.SUPERHERO],
                suppress_callback_exceptions=True)

app.config.suppress_callback_exceptions = True

cache = Cache(app.server, config={
    'CACHE_TYPE': 'filesystem',
    'CACHE_DIR': 'cache-directory'
})

Timeout = 120

# load app settings
app.settings = read_toml("../settings.toml")
