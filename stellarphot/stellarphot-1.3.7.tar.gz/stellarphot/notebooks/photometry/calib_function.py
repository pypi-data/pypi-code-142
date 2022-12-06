import numpy as np
from scipy.optimize import curve_fit

from astropy.table import Table
from astropy.coordinates import SkyCoord

from fit_functions import get_cat, f, opts_to_str, calc_residual


def transform_to_catalog(observed_mags_grouped, obs_mag_col, obs_filter,
                         obs_error_column=None,
                         cat_filter='r_mag', cat_color=('r_mag', 'i_mag'),
                         a_delta=0.5, a_cen=0, b_delta=1e-6, c_delta=0.5, d_delta=1e-6,
                         zero_point_range=(18, 22),
                         in_place=True, fit_diff=True,
                         verbose=True):
    """
    Transform a set of intrumental magnitudes to a standard system using either
    instrumental colors or catalog colors.

    Parameters
    ----------

    observed_magnitudes_grouped : astropy.table.Table group
        An astropy table, grouped by whatever you want that sepearates the data into
        data from just one image. BJD of the center of the observatory is one reasonable choice

    obs_mag_col : str
        Name of the column in `observed_magnitudes_grouped` that contains instrumental
        magnitudes.

    obs_filter : str
        Name of the filter in which observations were done. Should be one of the names at
        https://www.aavso.org/filters

    obs_error_column : str, optional
        Name of the column in `observed_magnitudes_grouped` that contains the error in the magnitude.

    cat_filter : str
        Name of the filter/passband in catalog that should be matched to the instrumental magnitudes.

    cat_color : tuple of two strings
        Names of the two columns in the caatalog that should be used to calculate color. The magnitude
        difference will be calculated in the ortder the fitlers are given. For example, if the value is
        ``('r_mag', 'i_mag')`` then the calculated color will be the ``r_mag`` column minus
        the ``i_mag`` column.

    a_delta, b_delta, c_delta, d_delta : flt, optional
        Range allowed in fitting for each of the parameters ``a``, ``b``, ``c``, and ``d``. Use ``1E-6`` to fix a parameter.

    a_cen : flt, optional
        Center of range for the fitting parameter ``a``.

    zero_point_range : tuple of flt, optional
        Range to which the value of the zero point is restricted in fitting to observed magnitudes.

    in_place : bool, optional
        If ``True``, add the calibrated magnitude to the input table, othewise return a copy.

    fit_diff : bool, optional
        If ``True``, fit the difference between the instrumental and catalog magnitude instead of the
        treating the catalog mag as the dependent variable.

    verbose: bool optional
        If ``True``, print additional output.
    """

    if obs_error_column is None:
        print("are you sure you want to do that? Error weighting is important!")

    fit_bounds_lower = [
        a_cen - a_delta,     # a
        -b_delta,   # b
        -c_delta,   # c
        -d_delta,   # d
        zero_point_range[0],    # z
    ]

    fit_bounds_upper = [
        a_cen + a_delta,     # a
        b_delta,  # b
        c_delta,  # c
        d_delta,  # d
        zero_point_range[1],    # z
    ]

    fit_bounds = (fit_bounds_lower, fit_bounds_upper)
    zero_point_mid = sum(zero_point_range) / 2

    a = []
    b = []
    c = []
    d = []
    z = []

    all_params = [a, b, c, d, z]

    cal_mags = []
    resids = []
    cat_mags = []
    cat = None
    cat_coords = None

    for file, one_image in zip(observed_mags_grouped.groups.keys, observed_mags_grouped.groups):
        our_coords = SkyCoord(one_image['RA'], one_image['Dec'], unit='degree')
        if cat is None or cat_coords is None:
            cat, cat_coords = get_cat(one_image)
            cat['color'] = cat[cat_color[0]] - cat[cat_color[1]]

        cat_idx, d2d, _ = our_coords.match_to_catalog_sky(cat_coords)

        mag_inst = one_image[obs_mag_col]
        cat_mag = cat[cat_filter][cat_idx]
        color = cat['color'][cat_idx]

        # Impose some constraints on what is included in the fit
        good_cat = ~(color.mask | cat_mag.mask) & (d2d.arcsecond < 1)
        good_data = ((one_image[obs_mag_col] < -3) &
                     (one_image[obs_mag_col] > -20) &
                     ~np.isnan(one_image[obs_mag_col])
                     )

        mag_diff = cat_mag - mag_inst

        good_data = good_data & (np.abs(mag_diff - np.nanmean(mag_diff)) < 1)

        try:
            good_data = good_data & ~one_image[obs_mag_col].mask
        except AttributeError:
            pass

        good = good_cat & good_data

        # Prep for fitting
        init_guess = (a_cen, 0, 0, 0, zero_point_mid)
        X = (mag_inst[good], color[good])
        catm = cat_mag[good]
        if catm.mask.any() or X[1].mask.any() or np.isnan(X[0]).any():
            print("heck")
        if obs_error_column is not None:
            errors = one_image[obs_error_column][good]
        else:
            errors = None

        if fit_diff:
            offset = X[0]
        else:
            offset = 0

        # Do the fit
        popt, pcov = curve_fit(f, X, catm - offset,
                               p0=init_guess, bounds=fit_bounds,
                               sigma=errors)

        # Accumulate the parameters
        for param, value in zip(all_params, popt):
            param.extend([value] * len(one_image))

        # Calculate and accumulate residual
        residual = calc_residual(f(X, *popt) + offset, catm)
        resids.extend([residual] * len(one_image))

        # Calculate calibrated magnitudes and accumulate, settings ones with no catalog match to NaN
        X = (mag_inst, color)
        cal_mag = f(X, *popt)
        if fit_diff:
            cal_mag = cal_mag + X[0]
        bad_match = d2d.arcsecond > 1
        cal_mag[bad_match] = np.nan
        cal_mags.extend(cal_mag)
        cat_mags.extend(cat_mag)

        # Keep the user entertained....
        print(f'{file[0]} has fit {opts_to_str(popt)} with {residual=:.4f}')

    mag_col_name = obs_mag_col + '_cal'
    if not in_place:
        result = observed_mags_grouped.copy()
    else:
        result = observed_mags_grouped

    result[mag_col_name] = cal_mags
    if obs_error_column is not None:
        result[mag_col_name + '_error'] = (
            (1 + np.asarray(all_params[0])) * result[obs_error_column]
        )
    opt_names = ['a', 'b', 'c', 'd', 'z']

    for name, values in zip(opt_names, all_params):
        result[name] = values

    result['mag_cat'] = cat_mags
    return result
