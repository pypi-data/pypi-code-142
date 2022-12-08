import os
import h5py
import numpy as np
import yaml

import pynibs


def cf_curveshift_workhorse_stretch_correction(elm_idx_list, mep, mep_params, e, n_samples=100):
    """
    Worker function for congruence factor computation - call from multiprocessing.pool
    Calculates congruence factor for ``e = (E_mag, E_norm and/or E_tan)`` for given zaps and elements.
    The computations are parallelized in terms of element indices (``elm_idx_list``).
    ``n_samples`` are taken from fitted_mep, within the range of the :py:class:`~pynibs.expio.Mep`.

    Parameters
    ----------
    elm_idx_list : np.ndarray
        (chunksize) List of element indices, the congruence factor is computed for
    mep : list of :py:class:`~pynibs.expio.Mep`
        (n_cond) List of fitted Mep object instances for all conditions.
    mep_params : np.ndarray of float
        (n_mep_params_total) List of all mep parameters of curve fits used to calculate the MEP,
        accumulated into one array.

        * e.g. [``mep_#1_para_#1``, ``mep_#1_para_#2``, ``mep_#1_para_#3``,
          ``mep_#2_para_#1``, ``mep_#2_para_#1``, ...]

    e : list of list of np.ndarray of float
        [n_cond][n_datasets][n_elm] Tuple of n_datasets of the electric field to compute the congruence factor for,
        e.g. ``(e_mag, e_norm, e_tan)``.
        Each dataset is a list over all conditions containing the electric field component of interest

        * e.g.: ``len(e) = n_cond``
        * ``len(e[0]) = n_comp`` (e.g: ``e_mag = e[0])``)

    n_samples : int, default=100
        Number of data points to generate discrete mep and e curves.

    Returns
    -------
    congruence_factor : np.ndarray of float
        (n_roi, n_datasets) Congruence factor in each element specified in elm_idx_list and for each input dataset.
    """

    stepsize = 1e-1
    n_datasets = len(e[0])
    n_elm = len(elm_idx_list)
    n_conditions = len(mep)

    mep_params = np.array(mep_params).flatten()

    congruence_factor = np.empty((n_elm, n_datasets))

    # rearrange mep parameters to individual conditions
    mep_params_cond = []
    start_idx = 0
    for i_cond in range(n_conditions):
        mep_params_cond.append(mep_params[start_idx:(start_idx + mep[i_cond].popt.size)])
        start_idx = start_idx + mep[i_cond].popt.size

    del start_idx

    intensities = []
    intensities_min = []
    intensities_max = []
    mep_curve = []

    # calculate mep curves per condition
    for i_cond in range(n_conditions):
        intensities.append(np.linspace(mep[i_cond].x_limits[0], mep[i_cond].x_limits[1], n_samples))
        mep_curve.append(mep[i_cond].eval(intensities[-1], mep_params_cond[i_cond]))
        intensities_min.append(mep[i_cond].x_limits[0])
        intensities_max.append(mep[i_cond].x_limits[1])

    for i_datasets in range(n_datasets):

        # calculate corresponding electric field values per condition
        for elm_idx, elmIdx in enumerate(elm_idx_list):
            e_curve = []
            stepsize_local_shift = []

            # get e-curves for reference solutions with n_samples
            for i_cond in range(n_conditions):
                e_curve.append(e[i_cond][i_datasets][elmIdx] * intensities[i_cond])
                stepsize_local_shift.append(e_curve[-1][1] - e_curve[-1][0])

            # KERNEL CODE STARTED HERE
            e_min = np.min(e_curve, axis=1)  # minima of electric field for every condition
            # ceil to .stepsize
            e_min = np.ceil(e_min / stepsize) * stepsize
            e_max = np.max(e_curve, axis=1)  # maxima of electric field for every condition
            e_max = np.floor(e_max / stepsize) * stepsize

            # find median mep cond
            e_mean = np.mean((e_max + e_min) / 2)

            # return NaN if xmax-xmin is smaller than stepsize
            if np.any(e_max - e_min <= stepsize):
                congruence_factor[elm_idx, i_datasets] = np.nan

            else:

                # find start and stop indices of e_x in global e array
                start_ind = np.empty(n_conditions, dtype=int)
                stop_ind = np.empty(n_conditions, dtype=int)
                e_x_global = np.arange(0, np.max(e_max) + stepsize, stepsize)

                for idx in range(n_conditions):
                    # lower boundary idx of e_x_cond in e_x_global
                    start_ind[idx] = pynibs.mesh.utils.find_nearest(e_x_global, e_min[idx])

                    # upper boundary idx of e_x_cond in e_x_global
                    stop_ind[idx] = pynibs.mesh.utils.find_nearest(e_x_global, e_max[idx])

                # get tau distances for all conditions vs reference condition
                # distances for ref,i == i,ref. i,i == 0. So only compute upper triangle of matrix
                ref_range = np.arange(n_conditions)
                t_cond = np.zeros((n_conditions, n_conditions))
                idx_range = list(reversed(np.arange(n_conditions)))

                for reference_idx in ref_range:
                    # remove this reference index from idx_range
                    idx_range.pop()
                    # # as we always measure the distance of the shorter mep_cond, save idx to store in matrix
                    # reference_idx_backup = copy.deepcopy(reference_idx)

                    for idx in idx_range:
                        idx_save = idx
                        # # switch ref and idx, as we want to measure from short mep_y to avoid overshifting

                        # get initially shifted mep curve
                        # e axis of initially shifted mep curve (just needed for length)

                        # resampled intensity axis of initially shifted mep curve
                        intens_mep = np.linspace(intensities_min[idx],
                                                 intensities_max[idx],
                                                 ((e_min[reference_idx] - stepsize_local_shift[reference_idx]) -
                                                  ((e_min[reference_idx] - stepsize_local_shift[reference_idx]) /
                                                   intensities_max[idx] * intensities_min[idx])) /
                                                 stepsize_local_shift[reference_idx])

                        # ficticious e_mep value for initial shift (e'_mep)
                        e_mep_initial_shift = (e_min[reference_idx] - stepsize_local_shift[reference_idx]) / \
                                              intensities_max[idx]

                        # start index of initially shifted and stretched mep curve
                        start_idx_mep_initial_shift = pynibs.mesh.utils.find_nearest(e_x_global,
                                                                                     e_mep_initial_shift *
                                                                                     intensities_min[idx])

                        mep_shift = mep[idx].eval(intens_mep, mep_params_cond[idx])

                        # determine length of mep curve in dependence on its location
                        max_e_mep_end = (e_max[reference_idx] + stepsize_local_shift[reference_idx]) * \
                                        intensities_max[idx] / intensities_min[idx]
                        len_e_ref = n_samples
                        len_e_mep_start = mep_shift.size
                        len_e_mep_end = np.ceil((max_e_mep_end - e_max[reference_idx] +
                                                 stepsize_local_shift[reference_idx]) /
                                                stepsize_local_shift[reference_idx])

                        # length of shifted curve as a function of position (gets longer while shifting)
                        len_mep_idx_shift = np.round(np.linspace(
                                len_e_mep_start,
                                len_e_mep_end,
                                len_e_mep_start + len_e_ref + 2 * stepsize_local_shift[reference_idx]))

                        # construct shift array (there are less 0 at the beginning and more at the end because the mep
                        # curve is stretched during shifting)
                        stepsize_local_shift_intens = (intensities_max[reference_idx] -
                                                       intensities_min[reference_idx]) / \
                                                      n_samples
                        min_intens_ref_prime = intensities_min[reference_idx] - stepsize_local_shift_intens * \
                                               (1 + len_e_mep_start)
                        max_intens_ref_prime = intensities_max[reference_idx] + stepsize_local_shift_intens * \
                                               (1 + len_e_mep_end)

                        shift_array = mep[reference_idx].eval(np.arange(min_intens_ref_prime,
                                                                        max_intens_ref_prime,
                                                                        stepsize_local_shift_intens),
                                                              mep_params_cond[reference_idx])

                        # generate index shift list to compare curves
                        slice_indices = np.outer(len_mep_idx_shift[:, np.newaxis],
                                                 np.linspace(0, 1, len_e_mep_start)[np.newaxis, :])
                        slice_indices = np.round(
                                np.add(slice_indices, np.arange(slice_indices.shape[0])[:, np.newaxis])).astype(int)

                        # the error is y-difference between mep[idx] and mep[reference].zero_padded
                        err = np.sqrt(np.sum((shift_array[slice_indices] - mep_shift) ** 2, axis=1))

                        # which shift leads to minimum error. remember that we don't start at 0-shift, so add start idx
                        t_cond[reference_idx, idx_save] = (start_idx_mep_initial_shift - start_ind[idx]) * stepsize + \
                                                          np.argmin(err) * stepsize_local_shift[reference_idx]

                # sum all errors and divide by e_mean over all conditions
                congruence_factor[elm_idx, i_datasets] = 1 / (
                        np.sqrt(np.sum(np.square(t_cond) * 2)) / e_mean / n_conditions / (n_conditions - 1))

    return congruence_factor


def cf_curveshift_workhorse_stretch_correction_new(mep, mep_params, e, n_samples=100, ref_idx=0):
    """
    Worker function for congruence factor computation - call from :py:class:`multiprocessing.Pool`.
    Calculates congruence factor for ``e = (E_mag, E_norm and/or E_tan)`` for given zaps and elements.
    The computations are parallelized in terms of element indices (``elm_idx_list``).
    ``n_samples`` are taken from fitted_mep, within the range of the :py:class:`~pynibs.expio.Mep`.

    Parameters
    ----------
    mep : list of :py:class:`~pynibs.expio.Mep`
        (n_cond) List of fitted Mep object instances for all conditions.
    mep_params : np.ndarray of float [n_mep_params_total]
        List of all mep parameters of curve fits used to calculate the MEP (accumulated into one array)

        * e.g. [``mep_#1_para_#1``, ``mep_#1_para_#2``, ``mep_#1_para_#3``, ``mep_#2_para_#1``, ``mep_#2_para_#1``, ...]

    e : np.ndarray of float
        (n_elm, n_cond) Electric field in elements.
    n_samples : int, default=100
        Number of data points to generate discrete mep and e curves.

    Returns
    -------
    congruence_factor : np.ndarray of float
        (n_elm) Congruence factor in each element specified in elm_idx_list and for each input dataset.
    """
    n_elm = e.shape[0]
    n_conditions = e.shape[1]
    c_idx = [idx for idx in np.arange(n_conditions) if idx != ref_idx]

    # rearrange mep parameters to individual conditions
    mep_params_cond = []
    start_idx = 0
    for i_cond in range(n_conditions):
        mep_params_cond.append(mep_params[start_idx:(start_idx + mep[i_cond].popt.size)])
        start_idx = start_idx + mep[i_cond].popt.size

    mep_params_ref = mep_params_cond[ref_idx]
    mep_params_c = [mep_params_cond[idx] for idx in c_idx]

    # intensities max and min [n_curves]
    i_ref_min = mep[ref_idx].intensities[0]
    i_ref_max = mep[ref_idx].intensities[-1]

    i_c_min = np.array([mep[idx].intensities[0] for idx in c_idx])
    i_c_max = np.array([mep[idx].intensities[-1] for idx in c_idx])

    i_stepsize = (i_ref_max - i_ref_min) / (n_samples - 1)

    # number of samples before and after shift with stretch correction
    n_c_before = np.round((1 - i_c_min / i_c_max) / (i_ref_max / i_ref_min - 1) * n_samples)
    n_c_after = np.round((i_c_max / i_c_min - 1) / (1 - i_ref_min / i_ref_max) * n_samples)

    # evaluate curves
    i_ref_shift = np.arange(i_ref_min - max(n_c_before) * i_stepsize,
                            i_ref_max + max(n_c_after) * i_stepsize + i_stepsize,
                            i_stepsize)

    mep_ref_shift = mep[ref_idx].eval(i_ref_shift, mep_params_ref)
    err_min_idx = []
    for i, idx in enumerate(c_idx):
        # evaluate curves at resampled intensity axis
        i_c_shift = np.linspace(i_c_min[i], i_c_max[i], n_c_before[i])
        mep_c_shift = mep[idx].eval(i_c_shift, mep_params_c[i])
        # generate index shift list to compare curves
        slice_indices = np.outer(
                np.round(np.linspace(n_c_before[i], n_c_after[i], n_c_before[i] + n_samples))[:, np.newaxis],
                np.linspace(0, 1, n_c_before[i])[np.newaxis, :])
        slice_indices = np.round(slice_indices + np.arange(slice_indices.shape[0])[:, np.newaxis])
        slice_indices = (slice_indices + (np.max(n_c_before) - n_c_before[i])).astype(int)
        # the error is y-difference between mep[idx] and mep[reference].zero_padded
        err = np.sum((mep_ref_shift[slice_indices] - mep_c_shift) ** 2, axis=1)
        err_min_idx.append(np.argmin(err))
    # electric fields [n_elm x n_curves]
    e_ref = e[:, ref_idx][:, np.newaxis]
    e_c = e[:, c_idx]

    # determine stepsizes in intensity and electric field space
    e_max = np.hstack((i_ref_max, i_c_max)) * np.hstack((e_ref, e_c))
    e_min = np.hstack((i_ref_min, i_c_min)) * np.hstack((e_ref, e_c))
    e_mean = np.mean((e_max + e_min) / 2, axis=1)[:, np.newaxis]
    e_stepsize = e_ref * i_stepsize

    # determine initial shift in electric field space
    initial_shift = e_c * i_c_min - e_ref * i_ref_min * i_c_min / i_c_max

    # determine total shift
    total_shift = np.zeros((n_elm, n_conditions))
    total_shift[:, 1:] = initial_shift - e_stepsize * np.array(err_min_idx)[np.newaxis, :]

    # sum all errors and divide by e_mean over all conditions
    congruence_factor = (e_mean ** 2) / np.var(total_shift, axis=1)[:, np.newaxis]

    return congruence_factor


def cf_curveshift_workhorse_stretch_correction_sign_new(mep, mep_params, e, n_samples=100, ref_idx=0):
    """
    Worker function for congruence factor computation - call from :py:class:`multiprocessing.Pool`.
    Calculates congruence factor for ``e = (E_mag, E_norm and/or E_tan)`` for given zaps and elements.
    The computations are parallelized in terms of element indices (``elm_idx_list``).
    ``n_sample``s are taken from fitted_mep, within the range of the :py:class:`~pynibs.expio.Mep`.

    Parameters
    ----------
    mep : list of :py:class:`~pynibs.expio.Mep`
        (n_cond) List of fitted Mep object instances for all conditions.
    mep_params : np.ndarray of float
        (n_mep_params_total) List of all mep parameters of curve fits used to calculate the MEP, accumulated into
        one array.

        * e.g. [``mep_#1_para_#1``, ``mep_#1_para_#2``, ``mep_#1_para_#3``, ``mep_#2_para_#1``,
          ``mep_#2_para_#1``, ...]

    e : np.ndarray of float
        (n_elm, n_cond) Electric field in elements.
    n_samples : int, default=100
        Number of data points to generate discrete mep and e curves.

    Returns
    -------
    congruence_factor : np.ndarray of float
        (n_elm, 1) Congruence factor in each element specified in elm_idx_list and for each input dataset.
    """
    n_elm = e.shape[0]
    n_conditions = e.shape[1]
    err_min_idx = np.zeros((n_conditions, n_conditions))
    initial_shift = np.zeros((n_elm, n_conditions, n_conditions))
    x_mean = np.empty((1, n_conditions))
    e_stepsize = np.zeros((n_elm, n_conditions))

    mep_params_cond = []
    start_idx = 0

    mask_pos = e > 0
    mask_neg = e < 0

    mask_only_one_curve = np.logical_or(np.sum(mask_pos, axis=1) == 1, np.sum(mask_neg, axis=1) == 1)
    n_curves = np.ones(n_elm) * n_conditions
    n_curves[mask_only_one_curve] = n_conditions - 1

    # rearrange mep parameters to individual conditions
    for i_cond in range(n_conditions):
        mep_params_cond.append(mep_params[start_idx:(start_idx + mep[i_cond].popt.size)])
        start_idx = start_idx + mep[i_cond].popt.size
        x_mean[0, i_cond] = (mep[i_cond].x_limits[0] + mep[i_cond].x_limits[1]) / 2

    for ref_idx in range(n_conditions):
        c_idx = [idx for idx in np.arange(n_conditions) if idx != ref_idx]

        mep_params_ref = mep_params_cond[ref_idx]
        mep_params_c = [mep_params_cond[idx] for idx in c_idx]

        # intensities max and min [n_curves]
        i_ref_min = np.min(mep[ref_idx].intensities)  # [0]
        i_ref_max = np.max(mep[ref_idx].intensities)  # [-1]

        i_c_min = np.array([np.min(mep[idx].intensities) for idx in c_idx])
        i_c_max = np.array([np.max(mep[idx].intensities) for idx in c_idx])

        i_stepsize = (i_ref_max - i_ref_min) / (n_samples - 1)

        # number of samples before and after shift with stretch correction
        n_c_before = np.round((1 - i_c_min / i_c_max) / (i_ref_max / i_ref_min - 1) * n_samples).astype(int)
        n_c_after = np.round((i_c_max / i_c_min - 1) / (1 - i_ref_min / i_ref_max) * n_samples)

        # evaluate curves
        i_ref_shift = np.arange(i_ref_min - max(n_c_before) * i_stepsize,
                                i_ref_max + max(n_c_after) * i_stepsize + i_stepsize,
                                i_stepsize)

        mep_ref_shift = mep[ref_idx].eval(i_ref_shift, mep_params_ref)

        for i, idx in enumerate(c_idx):
            # evaluate curves at resampled intensity axis
            i_c_shift = np.linspace(i_c_min[i], i_c_max[i], n_c_before[i])
            mep_c_shift = mep[idx].eval(i_c_shift, mep_params_c[i])
            # generate index shift list to compare curves
            slice_indices = np.outer(
                    np.round(np.linspace(n_c_before[i], n_c_after[i], n_c_before[i] + n_samples))[:, np.newaxis],
                    np.linspace(0, 1, n_c_before[i])[np.newaxis, :])
            slice_indices = np.round(slice_indices + np.arange(slice_indices.shape[0])[:, np.newaxis])
            slice_indices = (slice_indices + (np.max(n_c_before) - n_c_before[i])).astype(int)
            # the error is y-difference between mep[idx] and mep[reference].zero_padded
            err = np.sum((mep_ref_shift[slice_indices] - mep_c_shift) ** 2, axis=1)
            err_min_idx[ref_idx, idx] = np.argmin(err)

        # electric fields [n_elm x n_curves]
        e_ref = e[:, ref_idx][:, np.newaxis]
        e_c = e[:, c_idx]

        # determine stepsizes in intensity and electric field space
        e_stepsize[:, ref_idx] = (e_ref * i_stepsize).flatten()

        # determine initial shift in electric field space
        initial_shift[:, c_idx, ref_idx] = e_c * i_c_min - e_ref * i_ref_min * i_c_min / i_c_max

    mean_pos = np.array([np.mean(row[mask_pos[i, :]] * x_mean[0, mask_pos[i, :]]) for i, row in enumerate(e)])
    mean_neg = np.array([np.mean(row[mask_neg[i, :]] * x_mean[0, mask_neg[i, :]]) for i, row in enumerate(e)])

    # determine total shift
    total_shift_pos = []
    total_shift_neg = []

    for i_elm in range(n_elm):
        curve_idx_neg = np.where(mask_neg[i_elm, :])[0]
        curve_idx_pos = np.where(mask_pos[i_elm, :])[0]

        if curve_idx_neg.size != 0:
            ref_idx_neg = curve_idx_neg[0]
            total_shift_neg.append(initial_shift[i_elm, curve_idx_neg[1:], ref_idx_neg] -
                                   e_stepsize[i_elm, ref_idx_neg] * err_min_idx[ref_idx_neg, curve_idx_neg[1:]])
        else:
            total_shift_neg.append(np.array([]))

        if curve_idx_pos.size != 0:
            ref_idx_pos = curve_idx_pos[0]
            total_shift_pos.append(initial_shift[i_elm, curve_idx_pos[1:], ref_idx_pos] -
                                   e_stepsize[i_elm, ref_idx_pos] * err_min_idx[ref_idx_pos, curve_idx_pos[1:]])
        else:
            total_shift_pos.append(np.array([]))

    var_pos = np.array([np.sum(mask_pos[i, :]) * np.var(np.hstack((0, row))) for i, row in enumerate(total_shift_pos)])
    var_neg = np.array([np.sum(mask_neg[i, :]) * np.var(np.hstack((0, row))) for i, row in enumerate(total_shift_neg)])

    mean_pos[np.isnan(mean_pos)] = np.inf
    mean_neg[np.isnan(mean_neg)] = np.inf

    mean_pos[np.isnan(var_pos)] = np.inf
    mean_neg[np.isnan(var_neg)] = np.inf

    var = (var_pos / mean_pos ** 2 + var_neg / mean_neg ** 2) / n_curves

    congruence_factor = (1 / var)[:, np.newaxis]

    return congruence_factor


def cf_curveshift_workhorse_stretch_correction_variance(elm_idx_list, mep, mep_params, e, n_samples=100):
    """
    Worker function for congruence factor computation - call from :py:class:`multiprocessing.Pool`.
    Calculates congruence factor for ``e = (E_mag, E_norm and/or E_tan)`` for given zaps and elements.
    The computations are parallelized in terms of element indices (``elm_idx_list``).
    ``n_samples`` are taken from fitted_mep, within the range of the :py:class:`~pynibs.expio.Mep`.

    Parameters
    ----------
    elm_idx_list : np.ndarray
        (chunksize) List of element indices, the congruence factor is computed for.
    mep : list of :py:class:`~pynibs.expio.Mep`
        (n_cond) List of fitted Mep object instances for all conditions
    mep_params : np.ndarray of float [n_mep_params_total]
        List of all mep parameters of curve fits used to calculate the MEP (accumulated into one array)

        * e.g. [``mep_#1_para_#1``, ``mep_#1_para_#2``, ``mep_#1_para_#3``, ``mep_#2_para_#1``, ``mep_#2_para_#1``, ...]

    e : list of list of np.ndarray of float
        [n_cond][n_datasets][n_elm] Tuple of n_datasets of the electric field to compute the congruence factor for,
        e.g. ``(e_mag, e_norm, e_tan)``.
        Each dataset is a list over all conditions containing the electric field component of interest

        * e.g.: ``len(e) = n_cond``
        * ``len(e[0]) = n_comp`` (e.g: ``e_mag = e[0])``)

    n_samples : int, default=100
        Number of data points to generate discrete mep and e curves

    Returns
    -------
    congruence_factor : np.ndarray of float [n_roi, n_datasets]
        Congruence factor in each element specified in elm_idx_list and for each input dataset
    """

    stepsize = 1e-1
    n_datasets = len(e[0])
    n_elm = len(elm_idx_list)
    n_conditions = len(mep)

    mep_params = np.array(mep_params).flatten()

    congruence_factor = np.empty((n_elm, n_datasets))

    # rearrange mep parameters to individual conditions
    mep_params_cond = []
    start_idx = 0
    for i_cond in range(n_conditions):
        mep_params_cond.append(mep_params[start_idx:(start_idx + mep[i_cond].popt.size)])
        start_idx = start_idx + mep[i_cond].popt.size

    del start_idx

    intensities = []
    intensities_min = []
    intensities_max = []
    stepsize_local_shift = []
    mep_curve = []

    # calculate mep curves per condition
    for i_cond in range(n_conditions):
        intensities.append(np.linspace(mep[i_cond].x_limits[0], mep[i_cond].x_limits[1], n_samples))
        mep_curve.append(mep[i_cond].eval(intensities[-1], mep_params_cond[i_cond]))
        intensities_min.append(mep[i_cond].x_limits[0])
        intensities_max.append(mep[i_cond].x_limits[1])

    for i_datasets in range(n_datasets):

        # calculate corresponding electric field values per condition
        for elm_idx, elmIdx in enumerate(elm_idx_list):

            e_curve = []
            stepsize_local_shift = []

            # get e-curves for reference solutions with n_samples
            for i_cond in range(n_conditions):
                e_curve.append(e[i_cond][i_datasets][elmIdx] * intensities[i_cond])
                stepsize_local_shift.append(e_curve[-1][1] - e_curve[-1][0])

            # KERNEL CODE STARTED HERE
            e_min = np.min(e_curve, axis=1)  # minima of electric field for every condition
            # ceil to .stepsize
            e_min = np.ceil(e_min / stepsize) * stepsize
            e_max = np.max(e_curve, axis=1)  # maxima of electric field for every condition
            e_max = np.floor(e_max / stepsize) * stepsize

            # find median mep cond
            e_mean = np.mean((e_max + e_min) / 2)

            # return NaN if xmax-xmin is smaller than stepsize
            if np.any(e_max - e_min <= stepsize):
                congruence_factor[elm_idx, i_datasets] = np.nan

            else:

                # find start and stop indices of e_x in global e array
                start_ind = np.empty(n_conditions, dtype=int)
                stop_ind = np.empty(n_conditions, dtype=int)
                e_x_global = np.arange(0, np.max(e_max) + stepsize, stepsize)

                for idx in range(n_conditions):
                    # lower boundary idx of e_x_cond in e_x_global
                    start_ind[idx] = pynibs.mesh.utils.find_nearest(e_x_global, e_min[idx])

                    # upper boundary idx of e_x_cond in e_x_global
                    stop_ind[idx] = pynibs.mesh.utils.find_nearest(e_x_global, e_max[idx])

                # get tau distances for all conditions vs reference condition
                # distances for ref,i == i,ref. i,i == 0. So only compute upper triangle of matrix
                ref_range = [0]  # np.arange(n_conditions)
                t_cond = np.zeros((n_conditions, n_conditions))
                idx_range = list(reversed(np.arange(n_conditions)))

                for reference_idx in ref_range:
                    # remove this reference index from idx_range
                    idx_range.pop()
                    # # as we always measure the distance of the shorter mep_cond, save idx to store in matrix
                    # reference_idx_backup = copy.deepcopy(reference_idx)

                    for idx in idx_range:
                        idx_save = idx

                        # resampled intensity axis of initially shifted mep curve
                        intens_mep = np.linspace(intensities_min[idx],
                                                 intensities_max[idx],
                                                 ((e_min[reference_idx] - stepsize_local_shift[reference_idx]) -
                                                  ((e_min[reference_idx] - stepsize_local_shift[reference_idx]) /
                                                   intensities_max[idx] * intensities_min[idx])) /
                                                 stepsize_local_shift[reference_idx])

                        # ficticious e_mep value for initial shift (e'_mep)
                        e_mep_initial_shift = (e_min[reference_idx] - stepsize_local_shift[reference_idx]) / \
                                              intensities_max[idx]

                        # start index of initially shifted and stretched mep curve
                        start_idx_mep_initial_shift = pynibs.mesh.utils.find_nearest(e_x_global,
                                                                                     e_mep_initial_shift * intensities_min[idx])

                        mep_shift = mep[idx].eval(intens_mep, mep_params_cond[idx])

                        # determine length of mep curve in dependence on its location
                        max_e_mep_end = (e_max[reference_idx] + stepsize_local_shift[reference_idx]) * \
                                        intensities_max[idx] / intensities_min[idx]
                        len_e_ref = n_samples
                        len_e_mep_start = mep_shift.size
                        len_e_mep_end = np.ceil((max_e_mep_end - e_max[reference_idx] +
                                                 stepsize_local_shift[reference_idx]) /
                                                stepsize_local_shift[reference_idx])
                        # len_total = (len_e_mep_start + len_e_ref + len_e_mep_end + 2).astype(int)

                        # length of shifted curve as a function of position (gets longer while shifting)
                        len_mep_idx_shift = np.round(np.linspace(
                                len_e_mep_start,
                                len_e_mep_end,
                                len_e_mep_start + len_e_ref + 2 * stepsize_local_shift[reference_idx]))

                        # construct shift array (there are less 0 at the beginning and more at the end because the mep
                        # curve is stretched during shifting)
                        stepsize_local_shift_intens = (intensities_max[reference_idx] -
                                                       intensities_min[reference_idx]) / \
                                                      float(n_samples - 1)
                        min_intens_ref_prime = intensities_min[reference_idx] - stepsize_local_shift_intens * \
                                               (1 + len_e_mep_start)
                        max_intens_ref_prime = intensities_max[reference_idx] + stepsize_local_shift_intens * \
                                               (1 + len_e_mep_end)

                        shift_array = mep[reference_idx].eval(np.arange(min_intens_ref_prime,
                                                                        max_intens_ref_prime,
                                                                        stepsize_local_shift_intens),
                                                              mep_params_cond[reference_idx])

                        # generate index shift list to compare curves
                        slice_indices = np.outer(len_mep_idx_shift[:, np.newaxis],
                                                 np.linspace(0, 1, len_e_mep_start)[np.newaxis, :])
                        slice_indices = np.round(
                                np.add(slice_indices, np.arange(slice_indices.shape[0])[:, np.newaxis])).astype(int)

                        # the error is y-difference between mep[idx] and mep[reference].zero_padded
                        err = np.sqrt(np.sum((shift_array[slice_indices] - mep_shift) ** 2, axis=1))

                        # which shift leads to minimum error. remember that we don't start at 0-shift, so add start idx
                        t_cond[reference_idx, idx_save] = (start_idx_mep_initial_shift - start_ind[idx]) * stepsize + \
                                                          np.argmin(err) * stepsize_local_shift[reference_idx]

                # sum all errors and divide by e_mean over all conditions
                congruence_factor[elm_idx, i_datasets] = 1 / (
                        np.var(t_cond[0, :]) / (e_mean ** 2))  # changed to squared e

    return congruence_factor


def cf_variance_workhorse(elm_idx_list, mep, mep_params, e, old_style=True):
    """
    Worker function for congruence factor computation - call from :py:class:`multiprocessing.Pool`.
    Calculates congruence factor for ``e = (E_mag, E_norm and/or E_tan)`` for given zaps and elements.

    Parameters
    ----------
    elm_idx_list : np.ndarray
        (chunksize) List of element indices, the congruence factor is computed for.
    mep: list of :py:class:`~pynibs.expio.Mep`
        (n_cond) List of fitted Mep object instances for all conditions.
    mep_params: np.ndarray of float
        (n_mep_params_total) List of all mep parameters used to calculate the MEP, accumulated into one array).

        * e.g. [``mep_#1_para_#1``, ``mep_#1_para_#2``, ``mep_#1_para_#3``, ``mep_#2_para_#1``,
          ``mep_#2_para_#1``, ...])

    e: list of list of np.ndarray of float
        [n_cond][n_datasets][n_elm] Tuple of ``n_datasets`` of the electric field to compute the congruence factor for,
        e.g. ``(e_mag, e_norm, e_tan)``.
        Each dataset is a list over all conditions containing the electric field component of interest

        * ``len(e) = n_cond``
        * ``len(e[0]) = n_comp`` (e.g: ``e_mag = e[0])``)

    old_style: boolean (default: True)
        True:  Weight ``var(x_0_prime(r))`` with ``mean(e(r) * mean(Stimulator Intensity)``, taken from ``mep``
        False: Weight ``var(x_0_prime(r))`` with ``mean(E(r))``, taken from `e`

    Returns
    -------
    congruence_factor: np.ndarray of float
        (n_roi, n_datasets) Congruence factor in each element specified in elm_idx_list and for each input dataset
    """
    n_datasets = len(e[0])
    n_elm = len(elm_idx_list)
    n_conditions = len(mep)

    mep_params = np.array(mep_params).flatten()

    congruence_factor = np.empty((n_elm, n_datasets))

    # rearrange mep parameters to individual conditions
    mep_params_cond = []
    start_idx = 0
    x0_vec = np.empty((1, n_conditions))
    x_mean = np.empty((1, n_conditions))

    for i_cond in range(n_conditions):
        mep_params_cond.append(mep_params[start_idx:(start_idx + mep[i_cond].popt.size)])
        start_idx = start_idx + mep[i_cond].popt.size
        x0_vec[0, i_cond] = mep_params_cond[i_cond][0]
        x_mean[0, i_cond] = (mep[i_cond].x_limits[0] + mep[i_cond].x_limits[1]) / 2

    e_arr = np.array(e)

    for i_dataset in range(n_datasets):

        e_mat = np.array(e_arr[:, i_dataset, np.array(elm_idx_list).astype(int)]).transpose()

        x0_prime = e_mat * x0_vec

        var_x0_prime = np.var(x0_prime, axis=1)

        e_mean_vec = np.mean(e_mat * x_mean, axis=1)

        if old_style:
            congruence_factor[:, i_dataset] = e_mean_vec ** 2 / var_x0_prime
        else:
            congruence_factor[:, i_dataset] = np.mean(e_mat, axis=1) ** 2 / var_x0_prime

    return congruence_factor


def cf_variance_sign_workhorse(elm_idx_list, mep, mep_params, e):
    """
    Worker function for congruence factor computation - call from :py:class:`multiprocessing.Pool`.
    Calculates congruence factor for ``e = (E_mag, E_norm and/or E_tan)`` for given zaps and elements.

    Parameters
    ----------
    elm_idx_list: np.ndarray
        (chunksize) List of element indices, the congruence factor is computed for.
    mep: list of :py:class:`~pynibs.expio.Mep`
        (n_cond) List of fitted Mep object instances for all conditions.
    mep_params: np.ndarray of float
        (n_mep_params_total) List of all mep parameters of curve fits used to calculate the MEP,
        accumulated into one array), e.g. [``mep_#1_para_#1``, ``mep_#1_para_#2``, ``mep_#1_para_#3``,
        ``mep_#2_para_#1``, ``mep_#2_para_#1``, ...])
    e: list of list of np.ndarray of float
        [n_cond][n_datasets][n_elm] Tuple of ``n_datasets`` of the electric field to compute the congruence factor for,
        e.g. ``(e_mag, e_norm, e_tan)``.
        Each dataset is a list over all conditions containing the electric field component of interest

        * ``len(e) = n_cond``
        * ``len(e[0]) = n_comp`` (e.g: ``e_mag = e[0])``)

    Returns
    -------
    congruence_factor: np.ndarray of float
        (n_roi, n_datasets) Congruence factor in each element specified in elm_idx_list and for each input dataset.
    """
    n_datasets = len(e[0])
    n_elm = len(elm_idx_list)
    n_conditions = len(mep)

    mep_params = np.array(mep_params).flatten()

    congruence_factor = np.empty((n_elm, n_datasets))

    # rearrange mep parameters to individual conditions
    mep_params_cond = []
    start_idx = 0
    x0_vec = np.empty((1, n_conditions))
    x_mean = np.empty((1, n_conditions))

    for i_cond in range(n_conditions):
        mep_params_cond.append(mep_params[start_idx:(start_idx + mep[i_cond].popt.size)])
        start_idx = start_idx + mep[i_cond].popt.size
        x0_vec[0, i_cond] = mep_params_cond[i_cond][0]
        x_mean[0, i_cond] = (mep[i_cond].x_limits[0] + mep[i_cond].x_limits[1]) / 2

    e_arr = np.array(e)

    for i_dataset in range(n_datasets):
        e_mat = np.array(e_arr[:, i_dataset, np.array(elm_idx_list).astype(int)]).transpose()

        mask_pos = e_mat > 0
        mask_neg = e_mat < 0

        mask_only_one_curve = np.logical_or(np.sum(mask_pos, axis=1) == 1, np.sum(mask_neg, axis=1) == 1)
        n_curves = np.ones(n_elm) * n_conditions
        n_curves[mask_only_one_curve] = n_conditions - 1

        x0_prime = e_mat * x0_vec

        var_pos = np.array([np.sum(mask_pos[i, :]) * np.var(row[mask_pos[i, :]]) for i, row in enumerate(x0_prime)])
        var_neg = np.array([np.sum(mask_neg[i, :]) * np.var(row[mask_neg[i, :]]) for i, row in enumerate(x0_prime)])

        var_pos[np.isnan(var_pos)] = 0
        var_neg[np.isnan(var_neg)] = 0

        mean_pos = np.array([np.mean(row[mask_pos[i, :]] * x_mean[0, mask_pos[i, :]]) for i, row in enumerate(e_mat)])
        mean_neg = np.array([np.mean(row[mask_neg[i, :]] * x_mean[0, mask_neg[i, :]]) for i, row in enumerate(e_mat)])

        mean_pos[np.isnan(mean_pos)] = np.inf
        mean_neg[np.isnan(mean_neg)] = np.inf

        mean_pos[np.isnan(var_pos)] = np.inf
        mean_neg[np.isnan(var_neg)] = np.inf

        var = (var_pos / mean_pos ** 2 + var_neg / mean_neg ** 2) / n_curves

        congruence_factor[:, i_dataset] = 1 / var

    return congruence_factor


def cf_curveshift_workhorse(elm_idx_list, mep, mep_params, e, n_samples=100):
    """
    Worker function for congruence factor computation - call from :py:class:`multiprocessing.Pool`.
    Calculates congruence factor for ``e = (E_mag, E_norm and/or E_tan)`` for given zaps and elements.
    The computations are parallelized in terms of element indices (``elm_idx_list``).
    n_samples are taken from fitted_mep, within the range of the :py:class:`~pynibs.expio.Mep`.

    Parameters
    ----------
    elm_idx_list : np.ndarray
        (chunksize) List of element indices, the congruence factor is computed for.
    mep: list of :py:class:`~pynibs.expio.Mep`
        (n_cond) List of fitted Mep object instances for all conditions.
    mep_params : np.ndarray of float
        (n_mep_params_total) List of all mep parameters of curve fits used to calculate the MEP,
        accumulated into one array.

        * e.g. [``mep_#1_para_#1``, ``mep_#1_para_#2``, ``mep_#1_para_#3``,
          ``mep_#2_para_#1``, ``mep_#2_para_#1``, ...]

    e : list of list of np.ndarray of float
        [n_cond][n_datasets][n_elm] Tuple of ``n_datasets`` of the electric field to compute the congruence factor for,
        e.g. ``(e_mag, e_norm, e_tan)``.
        Each dataset is a list over all conditions containing the electric field component of interest.

        * ``len(e) = n_cond``
        * ``len(e[0]) = n_comp`` (e.g: ``e_mag = e[0])``)

    n_samples : int, default=100
        Number of data points to generate discrete mep and e curves.

    Returns
    -------
    congruence_factor: np.ndarray of float
        (n_roi, n_datasets) Congruence factor in each element specified in elm_idx_list and for each input dataset.

    """
    n_datasets = len(e[0])
    n_elm = len(elm_idx_list)
    n_conditions = len(mep)

    mep_params = np.array(mep_params).flatten()

    congruence_factor = np.empty((n_elm, n_datasets))

    # rearrange mep parameters to individual conditions
    mep_params_cond = []
    start_idx = 0
    for i_cond in range(n_conditions):
        mep_params_cond.append(mep_params[start_idx:(start_idx + mep[i_cond].popt.size)])
        start_idx = start_idx + mep[i_cond].popt.size

    del start_idx

    intensities = []
    mep_curve = []

    # calculate mep curves per condition
    for i_cond in range(n_conditions):
        intensities.append(np.arange(mep[i_cond].x_limits[0],
                                     mep[i_cond].x_limits[1],
                                     step=(mep[i_cond].x_limits[1] - mep[i_cond].x_limits[0]) / float(n_samples)))
        mep_curve.append(mep[i_cond].eval(intensities[-1], mep_params_cond[i_cond]))

    for i_datasets in range(n_datasets):

        # calculate corresponding electric field values per condition
        for elm_idx, elmIdx in enumerate(elm_idx_list):

            e_curve = []

            for i_cond in range(n_conditions):
                e_curve.append(e[i_cond][i_datasets][elmIdx] * intensities[i_cond])

            congruence_factor[elm_idx, i_datasets] = cf_curveshift_kernel(e_curve, mep_curve)
            # print("{}:{}".format(idx, len(elm_idx_list)))
    return congruence_factor


def cf_curveshift_kernel(e_curve, mep_curve):
    """
    Curve congruence (overlap) measure for multiple MEP curves per element. Determines the average displacement
    between the MEP curves. The congruence factor is weighted by ``median(E)`` and summed up. This favors elements which
    have greater E, as these are more likely to produce MEPs.

    .. math::
        dE = \\begin{bmatrix}
        dE_{11} & dE_{12} & ... & dE_{1n} \\\\
        dE_{21} & dE_{22} & ... & dE_{2n} \\\\
        ...   & ...   & ... & ...   \\\\
        dE_{n1} & dE_{n2} & ... & dE_{nn} \\\\
        \\end{bmatrix}

    -> ``congruence_factor ~ np.linalg.norm(dE)/median(E)/n_cond/2``

    Parameters
    ----------
    e_curve: list of np.ndarray of float
        (n_cond) List over all conditions of electric field values corresponding to the mep amplitudes.
    mep_curve: list of np.ndarray of float
        (n_cond) List over all conditions of mep values corresponding to the electric field.

    Returns
    -------
    congruence_factor: float
        Congruence factor for the n_cond electric field and MEP curves.
    """

    stepsize = 1e-1
    n_condition = len(mep_curve)
    e_min = np.min(e_curve, axis=1)  # minima of electric field for every condition
    # ceil to .stepsize
    e_min = np.ceil(e_min / stepsize) * stepsize
    e_max = np.max(e_curve, axis=1)  # maxima of electric field for every condition
    e_max = np.floor(e_max / stepsize) * stepsize

    # return NaN if xmax-xmin is smaller than stepsize
    if np.any(e_max - e_min <= stepsize):
        return np.nan

    else:
        # stepsize-wise e over all conditions. we only need the length of this and first elm

        mep_y_all_cond = []
        start_ind = np.empty(n_condition, dtype=int)
        stop_ind = np.empty(n_condition, dtype=int)
        for idx in range(n_condition):
            # x range for e for conditions, stepsize wise
            e_x_cond = np.arange(e_min[idx], e_max[idx], stepsize)
            # e_x_cond_all.append(e_x_con   d)

            # interpolate mep values to stepsize width
            mep_y_all_cond.append(np.interp(e_x_cond, e_curve[idx], mep_curve[idx]))
            # mep_y_all_cond.append(mep_y_cond)

            # lower boundary idx of e_x_cond in e_arr
            start_idx = int((e_x_cond[0] - np.min(e_min)) / stepsize)
            stop_idx = start_idx + len(e_x_cond)
            stop_ind[idx] = stop_idx
            start_ind[idx] = start_idx

        # find median mep cond
        e_mean = np.mean((e_max + e_min) / 2)

        # get tau distances for all conditions vs median condition
        # distances for ref,i == i,ref. i,i == 0. So only compute upper triangle of matrix
        ref_range = np.arange(n_condition)
        t_cond = np.zeros((n_condition, n_condition))
        idx_range = list(reversed(np.arange(n_condition)))
        for reference_idx in ref_range:
            # remove this reference index from idx_range
            idx_range.pop()
            # as we always measure the distance of the shorter mep_cond, save idx to store in matrix
            reference_idx_backup = reference_idx
            for idx in idx_range:
                # print((reference_idx, idx))
                idx_save = idx
                # restore correct reference idx
                reference_idx = reference_idx_backup

                # get lengths of mep_y
                len_mep_idx = mep_y_all_cond[idx].shape[0]
                len_mep_ref = mep_y_all_cond[reference_idx].shape[0]

                # switch ref and idx, as we want to measure from short mep_y
                if len_mep_idx < len_mep_ref:
                    reference_idx, idx = idx, reference_idx
                    len_mep_idx, len_mep_ref = len_mep_ref, len_mep_idx

                # and paste reference mep values. errors will be measured against this array
                # create array: global e + 2* len(mep[idx])
                shift_array = np.zeros(2 * len_mep_idx + len_mep_ref)
                shift_array[len_mep_idx:(len_mep_idx + len_mep_ref)] = mep_y_all_cond[reference_idx]

                # instead of for loop, I'll use multple slices:
                # slice_indices[0] is 0-shifting
                # slice_indices[1] is 1-shifting,...
                # we start shifting at start_ind[reference_idx], because range left of that is only 0
                # we stop shifting after len_mep_idx + e_len - stop_ind[reference_idx] times
                # slice_indices.shape == (len_mep_idx + e_len - stop_ind[reference_idx], len_mep_idx)
                slice_indices = np.add(np.arange(len_mep_idx),
                                       np.arange(len_mep_idx + len_mep_ref)[:, np.newaxis])

                # compute error vectorized
                # the error is y-difference between mep[idx] and mep[reference].zero_padded
                err = np.sqrt(np.sum((shift_array[slice_indices] - mep_y_all_cond[idx]) ** 2, axis=1))

                # which shift leads to minimum error. remember that we don't start at 0-shift, so add start index
                if stop_ind[idx] >= start_ind[reference_idx]:
                    min_err_idx = np.abs(start_ind[reference_idx] - stop_ind[idx]) - np.argmin(err)
                else:
                    min_err_idx = np.abs(start_ind[reference_idx] - stop_ind[idx]) + np.argmin(err)

                # rescale min_error_idx to real E values
                t_cond[reference_idx_backup, idx_save] = min_err_idx * stepsize

        # sum all errors and divide by e_mean over all conditions
        congruence_factor = 1 / (np.sqrt(np.sum(np.square(t_cond) * 2)) / e_mean / n_condition / (n_condition - 1))

        return congruence_factor


def extract_condition_combination(fn_config_cfg, fn_results_hdf5, conds, fn_out_prefix):
    """
    Extract and plot congruence factor results for specific condition combinations from permutation analysis.

    Parameters
    ----------
    fn_config_cfg : str
        Filename of .cfg file the permutation study was cinducted with
    fn_results_hdf5 : str
        Filename of ``.hdf5`` results file generated by ``00_run_c_standard_compute_all_permutations.py``
        containing congruence factors and condition combinations.
    conds : list of str
        (n_cond) List containing condition combinations to extract and plot,
        e.g. ``['P_0', 'I_225', 'M1_0', 'I_675', 'P_225']``).
    fn_out_prefix : str
        Prefix of output filenames of *_data.xdmf, *_data.hdf5 and *_geo.hdf5.

    Returns
    -------
    <fn_out_prefix_data.xdmf> : .xdmf file
        Output file linking *_data.hdf5 and *_geo.hdf5 file to plot in paraview.
    <fn_out_prefix_data.hdf5> : .hdf5 file
        Output .hdf5 file containing the data.
    <fn_out_prefix_geo.xdmf> : .hdf5 file
        Output .hdf5 file containing the geometry information.
    """

    # Read config file
    with open(fn_config_cfg, 'r') as f:
        config = yaml.load(f)

    # Initialize parameters
    ###############################################
    fn_subject = config['fn_subject']
    roi_idx = config['roi_idx']
    mesh_idx = config['mesh_idx']
    e_qoi = ['mag', 'norm', 'tan']
    n_qoi = len(e_qoi)

    # load subject object
    subject = pynibs.load_subject(fn_subject)
    mesh_folder = subject.mesh[mesh_idx]["mesh_folder"]

    # loading roi
    roi = pynibs.load_roi_surface_obj_from_hdf5(subject.mesh[mesh_idx]['fn_mesh_hdf5'])

    # load results file
    c_extracted = []

    print((" > Loading results file: {} ...".format(fn_results_hdf5)))
    with h5py.File(fn_results_hdf5) as f:
        # extract condition combination
        print(' > Loading condition labels ...')
        cond_comb = f['conds'][:]

        print(' > Determining condition combination index ...')
        conds_idx = [idx for idx, c in enumerate(cond_comb) if set(c) == set(conds)][0]

        print(' > Loading corresponding congruence factor results ...')
        for qoi_idx, qoi in enumerate(e_qoi):
            e_tri_idx = list(range(0, f['c'].shape[0], n_qoi))
            e_tri_idx = [mag + qoi_idx for mag in e_tri_idx]
            c_extracted.append(f['c'][e_tri_idx, conds_idx][:])

    # map data to whole brain surface
    print(" > Mapping c-factor map to brain surface...")
    c_mapped = pynibs.mesh.transformations.map_data_to_surface(datasets=[c_extracted[qoi_idx][:, np.newaxis] for qoi_idx in range(n_qoi)],
                                                               points_datasets=[roi[roi_idx].node_coord_mid] * n_qoi,
                                                               con_datasets=[roi[roi_idx].node_number_list] * n_qoi,
                                                               fname_fsl_gm=os.path.join(mesh_folder, subject.mesh[mesh_idx]['fn_lh_gm']),
                                                               fname_fsl_wm=os.path.join(mesh_folder, subject.mesh[mesh_idx]['fn_lh_wm']),
                                                               delta=subject.roi[mesh_idx][roi_idx]['delta'],
                                                               input_data_in_center=True,
                                                               return_data_in_center=True,
                                                               data_substitute=-1)

    # recreate complete midlayer surface to write in .hdf5 geo file
    points_midlayer, con_midlayer = pynibs.make_GM_WM_surface(
            gm_surf_fname=os.path.join(mesh_folder, subject.mesh[mesh_idx]['fn_lh_gm']),
            wm_surf_fname=os.path.join(mesh_folder, subject.mesh[mesh_idx]['fn_lh_wm']),
            delta=subject.roi[mesh_idx][roi_idx]['delta'],
            x_roi=None,
            y_roi=None,
            z_roi=None,
            layer=1,
            fn_mask=None)

    # write output files
    # save .hdf5 _geo file
    print(" > Creating .hdf5 geo file of mapped and roi only data ...")
    pynibs.write_geo_hdf5_surf(out_fn=fn_out_prefix + '_geo.hdf5',
                               points=points_midlayer,
                               con=con_midlayer,
                               replace=True,
                               hdf5_path='/mesh')

    pynibs.write_geo_hdf5_surf(out_fn=fn_out_prefix + '_geo_roi.hdf5',
                               points=roi[roi_idx].node_coord_mid,
                               con=roi[roi_idx].node_number_list,
                               replace=True,
                               hdf5_path='/mesh')

    # save .hdf5 _data file
    print(" > Creating .hdf5 data file of mapped and roi only data ...")
    pynibs.write_data_hdf5_surf(data=c_mapped,
                                data_names=['c_' + e_qoi[qoi_idx] for qoi_idx in range(n_qoi)],
                                data_hdf_fn_out=fn_out_prefix + '_data.hdf5',
                                geo_hdf_fn=fn_out_prefix + '_geo.hdf5',
                                replace=True)

    pynibs.write_data_hdf5_surf(data=[c_extracted[qoi_idx][:, np.newaxis] for qoi_idx in range(n_qoi)],
                                data_names=['c_' + e_qoi[qoi_idx] for qoi_idx in range(n_qoi)],
                                data_hdf_fn_out=fn_out_prefix + '_data_roi.hdf5',
                                geo_hdf_fn=fn_out_prefix + '_geo_roi.hdf5',
                                replace=True)
