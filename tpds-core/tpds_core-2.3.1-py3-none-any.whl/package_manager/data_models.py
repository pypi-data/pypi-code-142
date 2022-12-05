from __future__ import annotations

from typing import Mapping, Optional, Sequence, Union

from packaging.version import VERSION_PATTERN, LegacyVersion, Version
from pydantic import BaseModel


class LegacySemVer(LegacyVersion):
    """
    Wrap python packaging version with a pydantic validator class
    """

    @classmethod
    def __get_validators__(cls):
        # one or more validators may be yielded which will be called in the
        # order to validate the input, each validator will receive as an input
        # the value returned from the previous validator
        yield cls.validate

    @classmethod
    def __modify_schema__(cls, field_schema):
        # __modify_schema__ should mutate the dict it receives in place,
        # the returned value will be ignored
        field_schema.update(
            # simplified regex here for brevity, see the wikipedia link above
            pattern=VERSION_PATTERN,
            # some example postcodes
            examples=["2.0.0", "2.0.0-rc.2", "2.0.0-rc.1", "1.0.0", "1.0.0-beta"],
        )

    @classmethod
    def validate(cls, v):
        return cls(v)


class SemVer(Version):
    """
    Wrap python packaging version with a pydantic validator class
    """

    @classmethod
    def __get_validators__(cls):
        # one or more validators may be yielded which will be called in the
        # order to validate the input, each validator will receive as an input
        # the value returned from the previous validator
        yield cls.validate

    @classmethod
    def __modify_schema__(cls, field_schema):
        # __modify_schema__ should mutate the dict it receives in place,
        # the returned value will be ignored
        field_schema.update(
            # simplified regex here for brevity, see the wikipedia link above
            pattern=VERSION_PATTERN,
            # some example postcodes
            examples=["2.0.0", "2.0.0-rc.2", "2.0.0-rc.1", "1.0.0", "1.0.0-beta"],
        )

    @classmethod
    def validate(cls, v):
        return v if isinstance(v, Version) else cls(v)


class PackageDependencies(BaseModel):
    # Conda packages
    conda: Optional[Sequence[str]] = []
    # Pip packages
    pypi: Optional[Sequence[str]] = []


class PackageDetails(BaseModel):
    # Package Name
    name: str
    # Source Channel
    channel: str
    # Description of the package
    description: Optional[str]
    # Installed Version
    installed: Union[SemVer, LegacySemVer, None] = None
    # Latest Version
    latest: Union[SemVer, LegacySemVer, None]
    # License Description String
    license: Optional[str]
    # Full license text
    license_text: Optional[str]
    # Dependencies
    dependencies: Sequence[PackageDependencies] = []
    # Optional Dependencies
    extras: Mapping[str, PackageDependencies] = {}


class CondaInfoModel(BaseModel):
    # Configured channels of the conda system
    channels: Sequence[str]
    # Configured environments
    envs: Sequence[str]


class TpdsPackagingModel(BaseModel):
    # Required Packages
    required: PackageDependencies = PackageDependencies()
    # Conditional Packages depending on the feature
    optional: Optional[Mapping[str, Sequence[str]]] = {}


class CondaAboutExtraModel(BaseModel):
    # Trust Platform specific metadata
    tpds: Optional[TpdsPackagingModel] = TpdsPackagingModel()


class CondaAboutModel(BaseModel):
    channels: Sequence[str]
    conda_build_version: Optional[str] = None
    conda_private: bool
    conda_version: Optional[str] = None
    env_vars: Mapping[str, str] = {}
    extra: Optional[CondaAboutExtraModel]
    home: Optional[str] = None
    identifiers: Optional[Sequence[str]] = []
    keywords: Optional[Sequence[str]] = []
    license: Optional[str] = None
    license_file: Union[str, Sequence[str], None] = None
    summary: Optional[str] = None
    tags: Optional[Sequence[str]] = None


class CondaPackageDetails(BaseModel):
    # Package Name
    name: str
    # Source Channel
    channel: str
    # Version
    version: Union[SemVer, LegacySemVer]
    # Conda build
    build_number: int
    # Conda build identifier
    build_string: Optional[str]
    # Is the package a conda updatable package
    updateable: Optional[bool] = False
    # Conda Package Dependencies - conda installer will manage these
    depends: Optional[Sequence[str]]
    # License Type Summary
    license: Optional[str]
    # Additional Package Information
    about: Optional[CondaAboutModel] = None

    class Config:
        allow_population_by_field_name = True
        fields = {"build_string": "build"}


class CondaSearchModel(BaseModel):
    # List of Packages
    packages: Mapping[str, Sequence[CondaPackageDetails]]
