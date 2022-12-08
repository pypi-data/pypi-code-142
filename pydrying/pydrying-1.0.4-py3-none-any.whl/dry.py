# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 19:58:23 2022

@author: Hedi
"""
import json
import os
from .__mesh__ import __mesh__
from numpy import sqrt,zeros,concatenate,arange,ones,dot
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt


class _schema_obj:
    def __init__(self, dict_):
            self.__dict__.update(dict_)
class obj:
    def __init__(self,s=None):
        if s:
            schema = s
        else:
            schema = self.schema
        for k,v in schema.__dict__.items():
                if hasattr(v,"default"):
                    setattr(self,k,v.default)  
                else:
                    setattr(self,k,v)
    @property
    def type(self):
        return type(self).__name__
    @property
    def schema(self):
        return getattr(_schema,self.type)
    
def load_json(fname):
    return json.loads(json.dumps(json.
                                 loads(open (os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                                 fname+".json"), "r").read()),), object_hook=_schema_obj,)
_schema = load_json("dry")

def pvsat(T):
        """ Pressure of saturated liquid, mixture or steam
        INPUT
        Temperature in °C
        Lower boundary: Tmin = 273.16  [K] minimum temperature is triple point
        Upper boundary: Tc = 647.096  [K] critical point temperature
        OUTPUT
        pressure p in [Pa]
        Based on IAPWS-IF97
        Reference: http://www.iapws.org/
        Author : Romdhana Hedi
        Affiliation : AgroParisTech
        @ : romdhana@agroparistech.fr
        """
        eps = T + 273.15 -0.238555575678490/(T -377.0253484479800)
        A = (eps + 1167.05214527670)*eps -724213.167032060
        B = (12020.8247024700 -17.0738469400920*eps)*eps -3232555.03223330
        C = (14.9151086135300*eps -4823.26573615910)*eps + 405113.405420570
        beta = 2*C/(-B + sqrt(B*B - 4*A*C))
        return  beta**4 * 1e6

def thin_layer_sysdiff(t,XT,s):
    X = XT[0:s.n]
    T = XT[s.n:2*s.n]
    DHvap=2500000
    #evaporation rate
    aw = s.material.aw.calcul(T[-1], X[-1])# sorption isotherm
    # M/R_GP = 0.002164902525685
    psat_s = pvsat(T[-1])
    mevap = s.h*.000002165022853019004*(aw*psat_s/(T[-1]+273.15)-s.air.RH*s.air.pvsat/(s.air.T+273.15))# kg/m2/s
    Dmoy = zeros(s.n-1)
    rhoCp = s.material.rhos*(s.material.Cps+X*4180)
    alpha = s.material.Lambda.calcul(T,X)/rhoCp
    D=s.material.Diff.calcul(T,X)
    Dmoy = sqrt(D[1:]*D[:-1])   
    dXdt = zeros(s.n)
    dTdt = zeros(s.n)
    dXdt[0] = s.mesh.prem[0]*Dmoy[0]*(X[1]-X[0])
    dTdt[0] = s.mesh.prem[0]*alpha[0]*(T[1]-T[0])
    i=arange(1,s.n-1)
    dXdt[i] = s.mesh.prem[i]*Dmoy[i]*(X[i+1]-X[i])-s.mesh.prwm[i]*Dmoy[i-1]*(X[i]-X[i-1])
    dTdt[i] = s.mesh.prem[i]*alpha[i]*(T[i+1]-T[i])-s.mesh.prwm[i]*alpha[i]*(T[i]-T[i-1])
    dXdt[-1] = -s.mesh.prem[-1]*mevap/s.material.rhos*s.mesh.dx-s.mesh.prwm[-1]*Dmoy[-2]*(X[-1]-X[-2])
    dTdt[-1] = s.mesh.prem[-1]*(s.h*(s.air.T-T[-1])-DHvap*mevap)/rhoCp[-1]*s.mesh.dx-s.mesh.prwm[-1]*alpha[-1]*(T[-1]-T[-2])
    return concatenate((dXdt/s.mesh.DRm,dTdt/s.mesh.DRm))
class eval_prop:
    def __init__(self,val):
        self.val = val
    def calcul(self,*args):
        if callable(self.val):
            return self.val(*args)
        else:
            return self.val*ones(len(args[0]))
        
class material(obj):
    def __init__(self,**args):
        self.auto_calcul=False
        super().__init__()
        for k,v in args.items():
            if hasattr(self,k):
                if getattr(self.schema,k).callable:
                    setattr(self,k,eval_prop(v))
                else:
                    setattr(self,k,v)
class air(obj):
    def __init__(self,**args):
        self.auto_calcul=False
        super().__init__()
        for k,v in args.items():
            if hasattr(self,k):
                setattr(self,k,v)
    def calcul(self):
        self.pvsat = pvsat(self.T)
        
class thin_layer_res(obj):
    def __init__(self,parent):
        self.auto_calcul=False
        super().__init__(parent.schema.res)
        self.parent = parent
    @property
    def Xmoy(self):
        data = zeros(len(self.t))
        for i in range(len(self.t)):
            data[i] = dot(self.X[:,i],self.parent.mesh.vf)
        return data
class thin_layer(obj):
    def __init__(self,**args):
        self.auto_calcul=False
        super().__init__()
        self.material = material()
        self.air = air()
        self.res = thin_layer_res(self)
        for k,v in args.items():
            if hasattr(self,k):
                if isinstance(v,dict):
                    attr = getattr(self,k)
                    for k1,v1 in v.items():
                        if hasattr(attr,k1):
                            setattr(attr,k1,v1)
                else:
                    setattr(self,k,v)
        self.mesh = __mesh__(self.L,self.m,self.n)
        self.air.calcul()
        self.y0 =  concatenate(([self.material.Xinit]*self.n,[self.material.Tinit]*self.n))
        if not bool(self.t_eval):
            self.t_eval = arange(self.t0,self.tmax)  # the points of evaluation of solution
    def solve(self):
        sol = solve_ivp(thin_layer_sysdiff,[self.t0,self.tmax],self.y0,method="BDF",rtol=1e-3,atol=1e-3,t_eval=self.t_eval,args=(self,))
        #plt.plot(sol.t, sol.y[-1,:])
        self.res.t = sol.t
        self.res.X = sol.y[0:self.n,:]
        self.res.T = sol.y[self.n:self.n*2,:]