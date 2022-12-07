import re
from pydantic import ConstrainedStr
from typing import Type, TypeVar
from enum import Enum


class FileType(str, Enum):
    src_code: str = "src"
    preview: str = "preview"
    raw: str = "raw"
    derived: str = "derived"
    configuration: str = "conf"


class FileStatus(str, Enum):
    unavailable: str = "unavailable"
    pending: str = "pending"
    available: str = "available"
    secured: str = "secured"


class UploadConcat(str, Enum):
    partial: str = "partial"
    final: str = "final"


def namestr(
    *,
    strip_whitespace: bool = True,
    to_lower: bool = True,
    strict: bool = True,
    min_length: int = 1,
    max_length: int = 50,
    curtail_length: int = None,
    regex: str = None,
) -> Type[str]:
    namespace = dict(
        strip_whitespace=strip_whitespace,
        to_lower=to_lower,
        strict=strict,
        min_length=min_length,
        max_length=max_length,
        curtail_length=curtail_length,
        regex=regex and re.compile(regex),
    )
    return type("ConstrainedStrValue", (ConstrainedStr,), namespace)


def usernamestr(
    *,
    strip_whitespace: bool = True,
    to_lower: bool = True,
    strict: bool = True,
    min_length: int = 4,
    max_length: int = 20,
    curtail_length: int = None,
    regex: str = r"^[a-z0-9]+$",
) -> Type[str]:
    namespace = dict(
        strip_whitespace=strip_whitespace,
        to_lower=to_lower,
        strict=strict,
        min_length=min_length,
        max_length=max_length,
        curtail_length=curtail_length,
        regex=regex and re.compile(regex),
    )
    return type("ConstrainedStrValue", (ConstrainedStr,), namespace)


def metastr(
    *,
    strip_whitespace: bool = True,
    to_lower: bool = True,
    strict: bool = True,
    min_length: int = 2,
    max_length: int = 20,
    curtail_length: int = None,
    regex: str = None,
) -> Type[str]:
    namespace = dict(
        strip_whitespace=strip_whitespace,
        to_lower=to_lower,
        strict=strict,
        min_length=min_length,
        max_length=max_length,
        curtail_length=curtail_length,
        regex=regex and re.compile(regex),
    )
    return type("ConstrainedStrValue", (ConstrainedStr,), namespace)


def filestr(
    *,
    strip_whitespace: bool = True,
    to_lower: bool = True,
    strict: bool = True,
    min_length: int = 4,
    max_length: int = 255,
    curtail_length: int = None,
    regex: str = r"^[a-zA-Z0-9-\.]+$",
) -> Type[str]:
    namespace = dict(
        strip_whitespace=strip_whitespace,
        to_lower=to_lower,
        strict=strict,
        min_length=min_length,
        max_length=max_length,
        curtail_length=curtail_length,
        regex=regex and re.compile(regex),
    )
    return type("ConstrainedStrValue", (ConstrainedStr,), namespace)


def datasetstr(
    *,
    strip_whitespace: bool = True,
    to_lower: bool = True,
    strict: bool = True,
    min_length: int = 4,
    max_length: int = 100,
    curtail_length: int = None,
    regex: str = r"^[a-zA-Z0-9-]+$",
) -> Type[str]:
    namespace = dict(
        strip_whitespace=strip_whitespace,
        to_lower=to_lower,
        strict=strict,
        min_length=min_length,
        max_length=max_length,
        curtail_length=curtail_length,
        regex=regex and re.compile(regex),
    )
    return type("ConstrainedStrValue", (ConstrainedStr,), namespace)


def collectionstr(
    *,
    strip_whitespace: bool = True,
    to_lower: bool = True,
    strict: bool = True,
    min_length: int = 4,
    max_length: int = 100,
    curtail_length: int = None,
    regex: str = r"^[a-zA-Z0-9-]+$",
) -> Type[str]:
    namespace = dict(
        strip_whitespace=strip_whitespace,
        to_lower=to_lower,
        strict=strict,
        min_length=min_length,
        max_length=max_length,
        curtail_length=curtail_length,
        regex=regex and re.compile(regex),
    )
    return type("ConstrainedStrValue", (ConstrainedStr,), namespace)


def scopestr(
    *,
    strip_whitespace: bool = True,
    to_lower: bool = False,
    strict: bool = False,
    min_length: int = 4,
    max_length: int = 100,
    curtail_length: int = None,
    regex: str = r"^[a-zA-Z0-9-]+$",
) -> Type[str]:
    namespace = dict(
        strip_whitespace=strip_whitespace,
        to_lower=to_lower,
        strict=strict,
        min_length=min_length,
        max_length=max_length,
        curtail_length=curtail_length,
        regex=regex and re.compile(regex),
    )
    return type("ConstrainedStrValue", (ConstrainedStr,), namespace)
