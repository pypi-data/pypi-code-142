def mag2flux(mag, zeropoint):
    flux = 10**(0.4*(zeropoint-mag))
    return flux