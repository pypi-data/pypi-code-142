import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.getcwd() + "/.env")

AOC_TOKEN = os.environ.get("AOC_TOKEN", "")
INPUT_FOLDER = os.environ.get("INPUT_FOLDER", "./inputs")
