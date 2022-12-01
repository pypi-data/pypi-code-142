import numpy as np
from copy import deepcopy as dc
from spatialmath import base as smb

def get_tr(transform):
    tr = np.eye(4)
    tr[:3, :3] = get_r(transform.rotation)
    tr[:3, 3] = np.array([transform.location.x, transform.location.y, transform.location.z])
    return tr

def get_r(rotation):
    return smb.rpy2r(rotation.roll, rotation.pitch, rotation.yaw, unit="deg", order="zyx")

def r2rpy(R):
    return smb.tr2rpy(R, unit="deg", order="zyx")

def iso2unity(transform):
    u_transform = dc(transform)
    u_transform.location.x = -transform.location.y
    u_transform.location.y = transform.location.z
    u_transform.location.z = transform.location.x
    u_transform.rotation.roll = -transform.rotation.roll
    u_transform.rotation.pitch = transform.rotation.pitch
    u_transform.rotation.yaw = -transform.rotation.yaw

    return u_transform

def unity2iso(transform):
    i_transform = dc(transform)
    i_transform.location.x = transform.location.z
    i_transform.location.y = -transform.location.x
    i_transform.location.z = transform.location.y
    i_transform.rotation.roll = -transform.rotation.roll
    i_transform.rotation.pitch = transform.rotation.pitch
    i_transform.rotation.yaw = -transform.rotation.yaw

    return i_transform

def enu2world(transform):
    u_transform = dc(transform)
    u_transform.location.x = -transform.location.x
    u_transform.location.y = transform.location.z
    u_transform.location.z = -transform.location.y
    u_transform.rotation.roll = -transform.rotation.roll
    u_transform.rotation.pitch = transform.rotation.pitch
    u_transform.rotation.yaw = -transform.rotation.yaw + 270

    return u_transform

def world2enu(transform):
    i_transform = dc(transform)
    i_transform.location.x = -transform.location.x
    i_transform.location.y = -transform.location.z
    i_transform.location.z = transform.location.y
    i_transform.rotation.roll = -transform.rotation.roll
    i_transform.rotation.pitch = transform.rotation.pitch
    i_transform.rotation.yaw = -(transform.rotation.yaw-180)+90

    return i_transform
