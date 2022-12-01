"""An easy way to get pretrained auto models."""

import os
from typing import Tuple

from .auto_model import AutoModel, AutoModelFamily
from .breast_density_classification.auto import \
    BreastDensityClassificationFamily
from .endoscopic_inbody_classification.auto import \
    EndoscopicInbodyClassificationFamily
from .exceptions import ConfigError
from .skin_lesion_diagnosis.auto import SkinLesionDiagnosisFamily

_AUTO_MODEL_FAMILIES: Tuple[AutoModelFamily] = (
    BreastDensityClassificationFamily,
    SkinLesionDiagnosisFamily,
    EndoscopicInbodyClassificationFamily
)


def from_pretrained(name: str,
                    meta_data: dict,
                    resource_dir: str,
                    version: int = 1,
                    **kwargs) -> AutoModel:
    """Initiate an AutoModel instance from pretrained models.

    Args:
        name:
            The name of the pretrained model.
        version:
            The version of the pretrained model.
        meta_data:
            The metadata of the pretrained model.
        resource_dir:
            The root dir of the resource for setup process, i.e. parameter files.
        kwargs:
            Other keyword arguments.
    """
    if not name or not isinstance(name, str):
        raise ConfigError(f'Invalid pretrained model name: {name}.')
    if not version or not isinstance(version, int) or version < 1:
        raise ConfigError(f'Invalid pretrained model version: {version}.')
    if not meta_data or not isinstance(meta_data, dict):
        raise ConfigError(f'Invalid pretrained model meta data: {meta_data}.')
    if not resource_dir or not isinstance(resource_dir, str):
        raise ConfigError(f'Invalid pretrained model resource directory: {resource_dir}.')
    if name != meta_data.get('name') or version != meta_data.get('version'):
        raise ConfigError('Pretrained model and meta data do not match.')
    _validate_meta_data(meta_data=meta_data, resource_dir=resource_dir)

    for _family in _AUTO_MODEL_FAMILIES:
        auto_class = _family.get_auto_model(name, version)
        if auto_class is not None:
            return auto_class(meta_data=meta_data,
                              resource_dir=resource_dir,
                              **kwargs)
    raise ConfigError(f'No auto model found for name: {name}.')


def _validate_meta_data(meta_data: dict, resource_dir: str):
    """Make some simple but common validations, i.e. does the specified file exist."""
    if not meta_data or not isinstance(meta_data, dict):
        raise ConfigError(f'Invalid meta data: {meta_data}.')
    model_file = meta_data.get('model_file')
    module_dir = meta_data.get('module_dir')
    param_file = meta_data.get('param_file')
    if not model_file and not module_dir:
        raise ConfigError(f'Model source files missing: {meta_data}.')
    if module_dir:
        if not isinstance(module_dir, str):
            raise ConfigError(f'Invalid module directory: {module_dir}.')
        module_dir_full_path = os.path.join(resource_dir, module_dir)
        if not os.path.isdir(module_dir_full_path):
            raise ConfigError('Module directory cannot be accessed or is not a directory: ',
                              module_dir_full_path)
    if model_file:
        if not isinstance(model_file, str):
            raise ConfigError(f'Invalid model file: {model_file}.')
        model_file_full_path = os.path.join(resource_dir, model_file)
        if not os.path.isfile(model_file_full_path):
            raise ConfigError('Model file cannot be accessed or is not a file:',
                              model_file_full_path)
    if not param_file or not isinstance(param_file, str):
        raise ConfigError(f'Invalid param file: {param_file}.')
    param_file_full_path = os.path.join(resource_dir, param_file)
    if not os.path.isfile(param_file_full_path):
        raise ConfigError('Param file cannot be accessed or is not a file:',
                          param_file_full_path)
