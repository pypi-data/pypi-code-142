import requests

from sdc_dp_helpers.api_utilities.file_managers import load_file


class XMLReader:
    """
    Custom XML Reader
    """

    def __init__(self, config_filepath, **kwargs):
        self.config_path = config_filepath

        self.config = load_file(config_filepath, "yaml")

        self.url = str(self.config.get("url"))
        self.client = str(self.config.get("client"))

    def run_query(self):
        """
        Fetch XML from url
        """

        xml_content = requests.get(self.url).content

        return xml_content
