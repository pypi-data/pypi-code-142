from typing import Union

from pydantic import Field, constr

from servicefoundry.auto_gen import models


class DockerFileBuild(models.DockerFileBuild):
    type: constr(regex=r"dockerfile") = "dockerfile"


class PythonBuild(models.PythonBuild):
    type: constr(regex=r"tfy-python-buildpack") = "tfy-python-buildpack"


class RemoteSource(models.RemoteSource):
    type: constr(regex=r"remote") = "remote"


class LocalSource(models.LocalSource):
    type: constr(regex=r"local") = "local"


class Build(models.Build):
    type: constr(regex=r"build") = "build"
    build_source: Union[
        models.RemoteSource, models.GitSource, models.LocalSource
    ] = Field(default_factory=LocalSource)


class Manual(models.Manual):
    type: constr(regex=r"manual") = "manual"


class Schedule(models.Schedule):
    type: constr(regex=r"scheduled") = "scheduled"


class GitSource(models.GitSource):
    type: constr(regex=r"git") = "git"


class HttpProbe(models.HttpProbe):
    type: constr(regex=r"http") = "http"


class BasicAuthCreds(models.BasicAuthCreds):
    type: constr(regex=r"basic_auth") = "basic_auth"


class TruefoundryModelRegistry(models.TruefoundryModelRegistry):
    type: constr(regex=r"tfy-model-registry") = "tfy-model-registry"


class HuggingfaceModelHub(models.HuggingfaceModelHub):
    type: constr(regex=r"hf-model-hub") = "hf-model-hub"
