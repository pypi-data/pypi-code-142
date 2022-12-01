from .__about__ import __version__
from ._paths import diff_dirs, diff_files, diff_paths, have_same_content
from ._strings import diff_strings

__all__ = [
    "__version__",
    "diff_dirs",
    "diff_files",
    "diff_paths",
    "diff_strings",
    "have_same_content",
]
