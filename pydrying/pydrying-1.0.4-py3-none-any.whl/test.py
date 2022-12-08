# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 16:58:10 2022

@author: Hedi
"""

from numpy import ones,exp
from pydrying.dry import thin_layer, material

# diffusion coeff in the material
def Diff(T,X):
    """
    Parameters
    ----------
    T : Temperature [°C]
    X : TYPE
        moisture content [dry basis]
    Returns
    -------
    Diffusion coefficient [m2/s]
    """
    return 1e-9*ones(len(T))
# sorption isotherms
def aw(T,X):
    """
    Parameters
    ----------
    T : Temperature [°C]
    X : TYPE
        moisture content [dry basis]
    Returns
    -------
    water activity of the drying material [decimal]
    """
    return (1.0-exp(-0.6876*(T+45.5555)*X*X))
# thermal conductivity of the drying material
def Lambda(T,X):
    """
    Parameters
    ----------
    T : Temperature [°C]
    X : TYPE
        moisture content [dry basis]
    Returns
    -------
    thermal conductivity [W/m/K]
    """
    return .02

material_shape = 0 # flat material, (1: cylinder, 2: sphere)
caracteristic_length = 1e-2 # m
drying_time = 3600 # s
heat_transfer_coefficient = 25 # W/m2/K

drying_material = material(Diff=Diff,aw=aw,Lambda=Lambda,
                           m=material_shape, tmax=drying_time,
                           L=caracteristic_length,h=heat_transfer_coefficient)

tl = thin_layer(material=drying_material,air={})
tl.solve()
import matplotlib.pyplot as plt
plt.plot(tl.res.t, tl.res.Xmoy())
# plt.xlabel("drying time in s")
# plt.ylabel("material surface temperature in °C")
