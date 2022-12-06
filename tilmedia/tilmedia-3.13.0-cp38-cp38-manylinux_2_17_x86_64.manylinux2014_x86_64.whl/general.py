from typing import List, Union
from . import core


def clear_medium_name_cache():
    """
    Clear the name cache. This might be required if the data path has been changed.
    """
    core.clear_medium_name_cache()


def get_all_liquid_names() -> List[str]:
    """
    Get the list of Liquid names

    Returns:
        list: list of Liquid names
    """
    return core.get_all_liquid_names()


def get_all_gas_names() -> List[str]:
    """
    Get the list of Gas names

    Returns:
        list: list of Gas names
    """
    return core.get_all_gas_names()


def get_all_condensing_gas_names() -> List[str]:
    """
    Get the list of Condensing Gas names

    Returns:
        list: list of Condensing Gas names
    """
    return core.get_all_condensing_gas_names()


def get_all_vleFluid_names() -> List[str]:
    """
    Get the list of VLEFluid names

    Returns:
        list: list of VLEFluid names
    """
    return core.get_all_vleFluid_names()


def get_all_adsorption_and_absorption_names() -> List[str]:
    """
    Get the list of medium names

    Returns:
        list: list of medium names
    """
    return core.get_all_adsorption_and_absorption_names()


def get_data_path() -> Union[None, str]:
    """
    Get the TILMediaDataPath

    Returns:
        str : Data path of TILMedia
    """
    return core.get_data_path()


def set_data_path(path: str):
    """
    Set the TILMediaDataPath

    Args:
        path (str): Data path of TILMedia
    """
    core.set_data_path(path)


def license_is_valid() -> bool:
    """
    Check if the TILMedia License is valid.
    """
    return core.license_is_valid()


def get_closest_vleFluid_dpT(d: float, p: float, T: float) -> Union[None, str]:
    """
    detect medium name for a given critical point of a VLEFluid

    Args:
        d (float): critical density
        p (float): critical pressure
        T (float): critical temperature

    Returns:
        str: medium name
    """
    return core.get_closest_vleFluid_dpT(d, p, T)
