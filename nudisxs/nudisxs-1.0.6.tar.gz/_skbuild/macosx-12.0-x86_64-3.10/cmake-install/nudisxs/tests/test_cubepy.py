import numpy as np
import cubepy
from nudisxs.disxs import *
from nudisxs import _nudisxs as xs
dis = disxs()

def total_cross_section(enu,mode='cc'):
#    xs.e_nu.e_nu = enu
    def integrand(v,enu,mode):
        return np.ones_like(v)*xs.d2sdiscc_dxdy(enu,v[0],v[1])

    low  = np.array([[0.0],[0.0]])
    high = np.array([[1.0],[1.0]])
#    value, error = cubepy.integrate(lambda x: xs.d2sdiscc_dxdy(x[0],x[1])*np.ones_like(x),low, high)
#    value, error = cubepy.integrate(integrand,low, high,args=(enu))
    value, error = cubepy.integrate(
        integrand, [0.0, 0.0], [1.0, 1.0 ], args=(enu,1)
    )
    print(value)

def calculate_total(enu,mode='cc'):
    if mode == 'cc':
        xs_function = xs.d2sdiscc_dxdy
    elif mode == 'nc':
        xs_function = xs.d2sdisnc_dxdy
    else:
        log.error(f'this mode={mode} is not supported')
    print(xs_function,enu,mode)
    low  = np.array([[0.0],[0.0]])
    high = np.array([[1.0],[1.0]])
    def integrand(v,enu,dummy):
        return xs_function(enu,v[0],v[1])*np.ones_like(v)

    return cubepy.integrate(integrand,low, high,args=(enu,1))

xsec = calculate_total(10.)
print(xsec)
#total_cross_section(100.)
