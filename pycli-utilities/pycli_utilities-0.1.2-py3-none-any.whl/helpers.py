"""
    Copyright (c) 2022 Vishv Patel (https://github.com/itsthevp)

    Permission is hereby granted, free of charge, to any person obtaining a copy of
    this software and associated documentation files (the "Software"), to deal in
    the Software without restriction, including without limitation the rights to
    use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
    the Software, and to permit persons to whom the Software is furnished to do so,
    subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
    FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
    COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
    IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
    CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

from os import path


def null_striper(string: str) -> str:
    """Removes the NULL characters from the given string

    Args:
        string (str): string containing NULLs

    Returns:
        str: string with NULLs removed
    """
    return string.replace(chr(0), "")


def path_validate(file_path: str) -> str:
    """Handles the validation of the path (cross-platform-compatible)

    Args:
        file_path (str): path of the file

    Returns:
        str: Absolute of path of the file if exists else raises FileNotFound Error
    """
    if r"/" in file_path:
        # Unix / Linux Systems
        _path = file_path.split("/")
        _path = path.sep.join(_path)

    elif r"\\" in file_path:
        # Windows Systems
        _path = file_path.split("\\")
        _path = path.sep.join(_path)

    else:
        # Current Directory
        _path = file_path

    if path.exists(_path):
        return path.abspath(_path)
    else:
        raise FileNotFoundError(f"Unable to find file on the path {file_path}")
