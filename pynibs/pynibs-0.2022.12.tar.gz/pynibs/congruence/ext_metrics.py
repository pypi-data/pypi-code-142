import time
import warnings
import numpy as np
from sklearn.neighbors import KernelDensity

import pynibs


def rsd_inverse_workhorse(elm_idx_list, mep, e):
    """
    Worker function for RSD inverse computation after Bungert et al. (2017) [1]_, call from
    :py:class:`multiprocessing.Pool`.
    Calculates the RSD inverse for ``e = (E_mag, E_norm and/or E_tan)`` for given zaps and elements.
    The computations are parallelized in terms of element indices (``elm_idx_list``).

    Parameters
    ----------
    elm_idx_list : np.ndarray
         (chunksize) List of element indices, the congruence factor is computed for
    mep: list of :py:class:`~pynibs.expio.Mep`
        (n_cond) List of fitted Mep object instances for all conditions.
    e: list of list of np.ndarray of float
        [n_cond][n_datasets][n_elm] Tuple of ``n_datasets`` of the electric field to compute the congruence factor for,
        e.g. ``(e_mag, e_norm, e_tan)``.
        Each dataset is a list over all conditions containing the electric field component of interest

        * ``len(e) = n_cond``
        * ``len(e[0]) = n_comp`` (e.g: ``e_mag = e[0])``)

    Returns
    -------
    rsd_inv : np.ndarray of float
        (n_roi, n_datasets) RSD inverse in each element specified in ``elm_idx_list`` and for each input dataset.

    Notes
    -----
    .. [1] Bungert, A., Antunes, A., Espenhahn, S., & Thielscher, A. (2016).
       Where does TMS stimulate the motor cortex? Combining electrophysiological measurements and realistic field
       estimates to reveal the affected cortex position. Cerebral Cortex, 27(11), 5083-5094.
    """

    n_datasets = len(e[0])
    n_elm = len(elm_idx_list)
    n_conditions = len(mep)

    rsd_inv = np.empty((n_elm, n_datasets))
    mt_vec = np.empty((1, n_conditions))

    for i_cond in range(n_conditions):
        mt_vec[0, i_cond] = mep[i_cond].mt

    e_arr = np.array(e)

    for i_dataset in range(n_datasets):
        e_mat = np.array(e_arr[:, i_dataset, np.array(elm_idx_list).astype(int)]).transpose()
        std_vec = np.std(e_mat * mt_vec, axis=1)
        mean_vec = np.mean(e_mat * mt_vec, axis=1)
        rsd_inv[:, i_dataset] = 1 - (std_vec / mean_vec)

    return rsd_inv


def dvs_likelihood(params, x, y, verbose=True, normalize=False, bounds=[(1, 2), (1, 2)]):
    start = time.time()

    # extract parameters
    p = np.zeros(len(params) - 2)

    for i, p_ in enumerate(params):
        if i == 0:
            sigma_x = p_
        elif i == 1:
            sigma_y = p_
        else:
            p[i - 2] = p_

    # denormalize parameters from [0, 1] to bounds
    if normalize:
        sigma_x = sigma_x * (bounds[0][1] - bounds[0][0]) + bounds[0][0]
        sigma_y = sigma_y * (bounds[1][1] - bounds[1][0]) + bounds[1][0]

        for i, p_ in enumerate(p):
            p[i] = p[i] * (bounds[i + 2][1] - bounds[i + 2][0]) + bounds[i + 2][0]

    if sigma_x < 0:
        sigma_x = 0

    if sigma_y < 0:
        sigma_y = 0

    # determine posterior of DVS model with test data
    x_pre = np.linspace(np.min(x), np.max(x), 200000)
    x_post = x_pre + np.random.normal(loc=0., scale=sigma_x, size=len(x_pre))
    y_post = pynibs.sigmoid(x_post, p=p) + np.random.normal(loc=0., scale=sigma_y, size=len(x_pre))

    # bin data
    n_bins = 50
    dx_bins = (np.max(x_pre) - np.min(x_pre)) / n_bins
    x_bins_loc = np.linspace(np.min(x_pre) + dx_bins / 2, np.max(x_pre) - dx_bins / 2, n_bins)

    # determine probabilities of observations
    kde = KernelDensity(bandwidth=0.01, kernel='gaussian')

    l = []

    for i in range(n_bins):
        mask = np.logical_and(x_pre >= (x_bins_loc[i] - dx_bins / 2), x_pre < (x_bins_loc[i] + dx_bins / 2))
        mask_data = np.logical_and(x >= (x_bins_loc[i] - dx_bins / 2), x < (x_bins_loc[i] + dx_bins / 2))

        if np.sum(mask_data) == 0:
            continue

        # determine kernel density estimate
        try:
            kde_bins = kde.fit(y_post[mask][:, np.newaxis])
        except ValueError:
            warnings.warn("kde.fit(y_post[mask][:, np.newaxis]) yield NaN ... skipping bin")
            continue

        # get probability densities at data
        kde_y_post_bins = np.exp(kde_bins.score_samples(y[mask_data][:, np.newaxis]))

        l.append(kde_y_post_bins)

    l = np.concatenate(l)

    # mask out zero probabilities
    l[l == 0] = 1e-100

    # determine log likelihood
    l = np.sum(np.log10(l))

    stop = time.time()

    if verbose:
        parameter_str = [f"p[{i_p}]={p_:.5f}" for i_p, p_ in enumerate(p)]
        print(f"Likelihood: {l:.1f} / sigma_x={sigma_x:.2f}, sigma_y={sigma_y:.2f}  " +
              ", ".join(parameter_str) + f"({stop - start:.2f} sec)")

    return -l


def e_focal_workhorse(elm_idx_list, e):
    """
    Worker function to determine the site of stimulation after Aonuma et al. (2018) [1]_,
    call from :py:class:`multiprocessing.Pool`.
    Calculates the site of stimulation for ``e = (E_mag, E_norm and/or E_tan)`` for given zaps and elements by
    multiplying the electric fields with each other.
    The computations are parallelized in terms of element indices (``elm_idx_list``).

    Parameters
    ----------
    elm_idx_list : np.ndarray
        (chunksize) List of element indices, the congruence factor is computed for
    e: list of list of np.ndarray of float
        [n_cond][n_datasets][n_elm] Tuple of ``n_datasets`` of the electric field to compute the congruence factor for,
        e.g. ``(e_mag, e_norm, e_tan)``.
        Each dataset is a list over all conditions containing the electric field component of interest

        * ``len(e) = n_cond``
        * ``len(e[0]) = n_comp`` (e.g: ``e_mag = e[0])``)

    Returns
    -------
    e_focal : np.ndarray of float
        (n_roi, n_datasets) Focal electric field in each element specified in ``elm_idx_list`` and for each input.

    Notes
    -----
    .. [1] Aonuma, S., Gomez-Tames, J., Laakso, I., Hirata, A., Takakura, T., Tamura, M., & Muragaki, Y. (2018).
       A high-resolution computational localization method for transcranial magnetic stimulation mapping.
       NeuroImage, 172, 85-93.
    """

    n_datasets = len(e[0])
    n_elm = len(elm_idx_list)
    n_conditions = len(e)

    e_focal = np.ones((n_elm, n_datasets))

    for i_dataset in range(n_datasets):
        for i_cond in range(n_conditions):
            e_focal[:, i_dataset] *= e[i_cond][i_dataset][elm_idx_list]

    return e_focal


def e_cog_workhorse(elm_idx_list, mep, mep_params, e):
    """
    Worker function for electric field center of gravity (e_cog) computation after Opitz et al. (2013) [1]_
    - call from :py:class:`multiprocessing.Pool`. Calculates the e_cog for ``e = (E_mag, E_norm and/or E_tan)`` for given zaps
    and elements. The electric field is weighted by the mean MEP amplitude (turning point of the sigmoid) and summed up.
    The computations are parallelized in terms of element indices (``elm_idx_list``).

    Parameters
    ----------
    elm_idx_list : np.ndarray
        (chunksize) List of element indices, the congruence factor is computed for.
    mep : list of :py:class:`~pynibs.expio.Mep`
        (n_cond) List of fitted Mep object instances for all conditions.
    mep_params : np.ndarray of float
        (n_mep_params_total) List of all mep parameters of curve fits used to calculate the MEP, accumulated into
        one array.

        * e.g. [``mep_#1_para_#1``, ``mep_#1_para_#2``, ``mep_#1_para_#3``, ``mep_#2_para_#1``,
        ``mep_#2_para_#1``, ...]

    e : list of list of np.ndarray of float
        [n_cond][n_datasets][n_elm] Tuple of n_datasets of the electric field to compute the congruence factor for,
        e.g. ``(e_mag, e_norm, e_tan)``.
        Each dataset is a list over all conditions containing the electric field component of interest

        * e.g.: ``len(e) = n_cond``
        * ``len(e[0]) = n_comp`` (e.g: ``e_mag = e[0])``)

    Returns
    -------
    e_cog : np.ndarray of float
     (n_roi, n_datasets) RSD inverse in each element specified in ``elm_idx_list`` and for each input dataset.

    Notes
    -----
    .. [1] Opitz, A., Legon, W., Rowlands, A., Bickel, W. K., Paulus, W., & Tyler, W. J. (2013).
       Physiological observations validate finite element models for estimating subject-specific electric field
       distributions induced by transcranial magnetic stimulation of the human motor cortex. Neuroimage, 81, 253-264.
    """

    n_datasets = len(e[0])
    n_elm = len(elm_idx_list)
    n_conditions = len(mep)

    mep_params = np.array(mep_params).flatten()
    mep_params_cond = []
    start_idx = 0
    e_cog = np.empty((n_elm, n_datasets))
    mep_mean_vec = np.empty((1, n_conditions))
    intensity_mep_mean_vec = np.empty((1, n_conditions))

    # extract parameters
    for i_cond in range(n_conditions):
        mep_params_cond.append(mep_params[start_idx:(start_idx + mep[i_cond].popt.size)])
        start_idx = start_idx + mep[i_cond].popt.size

        # stimulator intensity in [A/us] for mean MEP amplitude, i.e. turning point of pynibs.sigmoid (1st para of
        # sigmoid)
        intensity_mep_mean_vec[0, i_cond] = mep[i_cond].popt[0]

        # mean MEP amplitude (function value at 1st parameter of pynibs.sigmoid)
        mep_mean_vec[0, i_cond] = mep[i_cond].eval(mep_params_cond[-1][0], mep_params_cond[-1])

    e_arr = np.array(e)

    for i_dataset in range(n_datasets):
        e_mat = np.array(e_arr[:, i_dataset, np.array(elm_idx_list).astype(int)]).transpose()
        e_cog[:, i_dataset] = np.sum(e_mat * (intensity_mep_mean_vec * mep_mean_vec), axis=1)

    return e_cog
