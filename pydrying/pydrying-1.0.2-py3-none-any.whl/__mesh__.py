# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 14:38:19 2022

@author: Hedi
"""

from numpy import zeros,arange
class __mesh__:
    def __init__(self,L,m,n):
        """
        Parameters
        ----------
        L : TYPE float
            caracteristic length in m
        m : TYPE int
            shape 
        n : TYPE, int
            mesh size
        Returns
        -------
        None.
        """
        self.dx = L/(n-1) # pas
        self.x = arange(n)*self.dx# VER position
        self.re = zeros(n)# e: est
        self.prem = zeros(n)# e: est
        self.rw = zeros(n)# w: west
        self.prwm = zeros(n)# w: west
        self.vf = zeros(n)# volume fraction
        self.re[0]=self.dx/2
        self.re[1:-1] = self.x[1:-1] + self.dx/2
        self.re[-1] = L
        self.rw[1:-1] = self.x[1:-1] - self.dx/2
        self.rw[-1] = L - self.dx/2
        self.prem[1:]=self.re[1:]**m
        self.prwm[1:]=self.rw[1:]**m
        m_=m+1
        self.V = L**m_ # domain volume
        self.vf=(self.re**m_-self.rw**m_)/self.V # volume fraction
        self.DRm=(self.re**m_-self.rw**m_)/m_*self.dx