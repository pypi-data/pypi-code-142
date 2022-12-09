from enum import Enum
from .locale import Language

class Region(Enum):
    North_America = ({Language.English: 'NA', Language.Korean: '북미'}, "US")
    Europe = ({Language.English: 'EU', Language.Korean: '유럽'}, "EU")
    Korea = ({Language.English: 'KR', Language.Korean: '한국'}, "KR")
    China = ({Language.English: 'CN', Language.Korean: '중국'}, "CN")

    # auth_code is the name of the region on the SC2Editor publish screen for authenticating into the region
    def __init__(self, codes, auth_code: str):
        self._codes = codes
        self._auth_code = auth_code

    def get_code(self, locale: Language):
        return self._codes[locale]

    def get_auth_code(self):
        return self._auth_code

    def get_english_code(self):
        return self.get_code(Language.English)

    def get_korean_code(self):
        return self.get_code(Language.Korean)
