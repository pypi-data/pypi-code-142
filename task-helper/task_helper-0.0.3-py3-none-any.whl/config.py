import os


class Config:
    """Config class"""

    PIVOTAL_TRACKER_PROJECT_ID: str
    PIVOTAL_TRACKER_TOKEN: str
    REPO_DIR: str

    def __init__(self) -> None:
        self.PIVOTAL_TRACKER_PROJECT_ID = os.environ.get("PVT_PROJECT_ID")
        self.PIVOTAL_TRACKER_TOKEN = os.environ.get("PVT_TOKEN")
        self.CSV_PROJECT_REPO_DIR = os.environ.get("CSV_PROJECT_REPO_DIR")
        self.REPO_DIR = os.getcwd()
