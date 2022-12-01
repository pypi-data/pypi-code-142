'''
Pre-defined physical constants.
'''

PI = 3.1415926535
PI_SQRT = PI ** 0.5
VACUUM_PERMITTIVITY = 8.854_187_812_8E-12  # farad/meter
ELEMENTARY_CHARGE = 1.602_176_62E-19  # coulomb
AVOGADRO = 6.022_140_76E23
MILLI = 1E-3
MICRO = 1E-6
NANO = 1E-9
PICO = 1E-12
# q^2/nm -> 138.93545522028575 kJ/mol
ONE_4PI_EPS0 = 1 / (4 * PI * VACUUM_PERMITTIVITY) \
               * ELEMENTARY_CHARGE ** 2 / NANO / 1000 * AVOGADRO
