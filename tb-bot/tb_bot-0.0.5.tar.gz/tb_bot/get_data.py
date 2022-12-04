import requests
import re
import sys
import pandas as pd
from datetime import datetime as dt

import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
from multiprocessing import Pool
import tqdm

import shutil
import tempfile
import sys
import libtorrent as lt
import os
from time import sleep
from datetime import datetime as dt



client = MongoClient("mongodb+srv://madhan2211:madhan221197@cluster0.vjuwnvf.mongodb.net/?retryWrites=true&w=majority")

db = client["Tamilblasters"]

homepage = "https://tamilblasters.com"

tamil_blaster_links = {
    "tamil": {
        "hdrip": f"{homepage}/index.php?/forums/forum/7-tamil-new-movies-hdrips-bdrips-dvdrips-hdtv",
        "tcrip": f"{homepage}/index.php?/forums/forum/8-tamil-new-movies-tcrip-dvdscr-hdcam-predvd",
        "dubbed": f"{homepage}/index.php?/forums/forum/9-tamil-dubbed-movies-bdrips-hdrips-dvdscr-hdcam-in-multi-audios",
        "series": f"{homepage}/index.php?/forums/forum/63-tamil-new-web-series-tv-shows",
    },
    "malayalam": {
        "tcrip": f"{homepage}/index.php?/forums/forum/75-malayalam-new-movies-tcrip-dvdscr-hdcam-predvd",
        "hdrip": f"{homepage}/index.php?/forums/forum/74-malayalam-new-movies-hdrips-bdrips-dvdrips-hdtv",
        "dubbed": f"{homepage}/index.php?/forums/forum/76-malayalam-dubbed-movies-bdrips-hdrips-dvdscr-hdcam",
        "series": f"{homepage}/index.php?/forums/forum/98-malayalam-new-web-series-tv-shows",
    },
    "telugu": {
        "tcrip": f"{homepage}/index.php?/forums/forum/79-telugu-new-movies-tcrip-dvdscr-hdcam-predvd",
        "hdrip": f"{homepage}/index.php?/forums/forum/78-telugu-new-movies-hdrips-bdrips-dvdrips-hdtv",
        "dubbed": f"{homepage}/index.php?/forums/forum/80-telugu-dubbed-movies-bdrips-hdrips-dvdscr-hdcam",
        "series": f"{homepage}/index.php?/forums/forum/96-telugu-new-web-series-tv-shows",
    },
    "hindi": {
        "tcrip": f"{homepage}/index.php?/forums/forum/87-hindi-new-movies-tcrip-dvdscr-hdcam-predvd",
        "hdrip": f"{homepage}/index.php?/forums/forum/86-hindi-new-movies-hdrips-bdrips-dvdrips-hdtv",
        "dubbed": f"{homepage}/index.php?/forums/forum/88-hindi-dubbed-movies-bdrips-hdrips-dvdscr-hdcam",
        "series": f"{homepage}/index.php?/forums/forum/89-hindi-new-web-series-tv-shows",
    },
    "kannada": {
        "tcrip": f"{homepage}/index.php?/forums/forum/83-kannada-new-movies-tcrip-dvdscr-hdcam-predvd",
        "hdrip": f"{homepage}/index.php?/forums/forum/82-kannada-new-movies-hdrips-bdrips-dvdrips-hdtv",
        "dubbed": f"{homepage}/index.php?/forums/forum/84-kannada-dubbed-movies-bdrips-hdrips-dvdscr-hdcam",
        "series": f"{homepage}/index.php?/forums/forum/103-kannada-new-web-series-tv-shows",
    },
    "english": {
        "tcrip": f"{homepage}/index.php?/forums/forum/52-english-movies-hdcam-dvdscr-predvd",
        "hdrip": f"{homepage}/index.php?/forums/forum/53-english-movies-hdrips-bdrips-dvdrips",
        "series": f"{homepage}/index.php?/forums/forum/92-english-web-series-tv-shows",
    },
}

db_data = pd.DataFrame(list(db.Alldata.find()))
dl = db_data[(db_data.HD_Status==1) & (db_data.Status==0)]
dl = dl.groupby(['Language','Type']).head()
data_dict = dl.to_dict('records')

def get_df(path="."):
    # df = pd.DataFrame(get_size_df(path))
    return data_dict