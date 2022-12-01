"""A tool to easily create complicated and dynamic URLs and headers.

:copyright: (c) 2022-present Tanner B. Corcoran
:license: MIT, see LICENSE for more details.

"""


__title__ = "http-prep"
__author__ = "Tanner B. Corcoran"
__email__ = "tannerbcorcoran@gmail.com"
__license__ = "MIT License"
__copyright__ = "Copyright (c) 2022-present Tanner B. Corcoran"
__version__ = "0.0.6"
__description__ = "A tool to easily create complicated and dynamic URLs and headers"
__url__ = "https://github.com/tanrbobanr/http-prep"
__download_url__ = "https://pypi.org/project/http-prep"


from .Headers import Headers
from .URL import URL, URLComponents, URLSeparators
from .OverloadDict import OverloadDict
