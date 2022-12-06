from astropy.coordinates import SkyCoord
from astropy import units as u
from astroquery.vizier import Vizier


def f(X, a, b, c, d, z):
    mag_inst, color = X
    
    return a * mag_inst + b * mag_inst ** 2 + c * color + d * color**2 + z


def get_cat(image):
    our_coords = SkyCoord(image['RA'], image['Dec'], unit='degree')
    # Get catalog via cone search
    Vizier.ROW_LIMIT = -1  # Set row_limit to have no limit
    desired_catalog = 'II/336/apass9'
    a_star = our_coords[0]
    rad = 1 * u.degree
    cat = Vizier.query_region(a_star, radius=rad, catalog=desired_catalog)
    cat = cat[0]
    cat_coords =  SkyCoord(cat['RAJ2000'], cat['DEJ2000'])
    return cat, cat_coords


def opts_to_str(opts):
    opt_names = ['a', 'b', 'c', 'd', 'z']
    names = []
    for name, value in zip(opt_names, opts):
        names.append(f'{name}={value:.4f}')
    return ', '.join(names)

def calc_residual(new_cal, catalog):
    resid = new_cal - catalog
    return resid.std()
