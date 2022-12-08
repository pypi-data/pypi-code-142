import numpy as np

import pynibs


def stimulation_threshold(elm_idx_list, mep, mep_params, n_samples, e, c_factor_percentile=95, mep_threshold=0.5,
                          c_factor=None, c_function=None, t_function=None):
    """
    Computes the stimulation threshold in terms of the electric field in [V/m]. The threshold is defined as the
    electric field value where the mep exceeds mep_threshold. The average value is taken over all mep curves in each
    condition and over an area where the congruence factor exceeds ``c_factor_percentile``.

    Parameters
    ----------
    elm_idx_list : np.ndarray
        (chunksize) List of element indices, the congruence factor is computed for.
    mep : list of Mep object instances
        (n_cond) List of fitted :py:class:`~pynibs.expio.Mep` object instances for all conditions.
    mep_params : np.ndarray of float [n_mep_params_total]
        List of all mep parameters of curve fits used to calculate the MEP (accumulated into one array)

        * e.g. [``mep_#1_para_#1``, ``mep_#1_para_#2``, ``mep_#1_para_#3``, ``mep_#2_para_#1``, ``mep_#2_para_#1``, ...]

    n_samples : int
        Number of data points to generate discrete mep and e curves.
    e : list of list of np.ndarray of float
        [n_cond][n_datasets][n_elm] Tuple of ``n_datasets`` of the electric field to compute the congruence factor for,
        e.g. ``(e_mag, e_norm, e_tan)``.
        Each dataset is a list over all conditions containing the electric field component of interest

        * e.g.: ``len(e) = n_cond``
        * ``len(e[0]) = n_comp`` (e.g: ``e_mag = e[0])``)
    c_factor_percentile : float
        Percentile of the c_factor taken into account for the threshold evaluation. Only c_factors are considered
        exceeding this.
    mep_threshold : float
        MEP value in [mV], which has to be exceeded for threshold definition.
    c_factor : np.ndarray of float
    (n_roi, n_datasets) Congruence factor in each element specified in elm_idx_list and for each input dataset.
    c_function : function
        Defines the function to use during c_gpc to calculate the congruence factor.

        * congruence_factor_curveshift_workhorse: determines the average curve shift
        * congruence_factor_curveshift_workhorse_stretch_correction: determines the average curve shift
        * congruence_factor_curveshift_workhorse_stretch_correction_variance: determines the average curve shift
        * congruence_factor_variance_workhorse: evaluates the variance of the shifting and stretching parameters

    t_function : function
        Defines the function to determine the stimulation_threshold.

        * stimulation_threshold_mean_mep_threshold: uses mep_threshold to determine the corresponding e_threshold over
          all conditions and takes the average values as the stimulation threshold
        * stimulation_threshold_pynibs.sigmoid: Fits a new pynibs.sigmoid using all datapoints in the mep-vs-E space and
          evaluates the threshold from the turning point or the intersection of the derivative in the crossing point
          with the e-axis

    Returns
    -------
    stim_threshold_avg: float
        Average stimulation threshold in [V/m] where c_factor is greater than ``c_factor_percentile``.
    """

    n_datasets = len(e[0])
    n_conditions = len(mep)
    mep_params = np.array(mep_params).flatten()

    # rearrange mep parameters to individual conditions
    mep_params_cond = []
    start_idx = 0

    for i_cond in range(n_conditions):
        mep_params_cond.append(mep_params[start_idx:(start_idx + mep[i_cond].popt.size)])
        start_idx = start_idx + mep[i_cond].popt.size

    # calculate mep curves per condition
    mep_curve = []
    intensities = []

    for i_cond in range(n_conditions):
        intensities.append(np.linspace(mep[i_cond].x_limits[0], mep[i_cond].x_limits[1], n_samples))
        mep_curve.append(mep[i_cond].eval(intensities[-1], mep_params_cond[i_cond]))

    # determine congruence factor, if not provided
    if not c_factor.any():
        if c_function == pynibs.congruence.cf_curveshift_workhorse or \
                c_function == pynibs.congruence.cf_curveshift_workhorse_stretch_correction or \
                c_function == pynibs.congruence.cf_curveshift_workhorse_stretch_correction_variance:
            c_factor = c_function(elm_idx_list,
                                  mep=mep,
                                  mep_params=mep_params,
                                  n_samples=n_samples,
                                  e=e)

        elif c_function == pynibs.congruence.cf_variance_workhorse:
            c_factor = c_function(elm_idx_list,
                                  mep=mep,
                                  mep_params=mep_params,
                                  e=e)

    # determine elements where the congruence factor exceeds c_factor_percentile
    elm_idx = []
    c_factor_percentile_value = []

    for i_data in range(n_datasets):
        c_factor_percentile_value.append(np.percentile(c_factor[np.logical_not(np.isnan(c_factor[:, i_data])), i_data],
                                                       c_factor_percentile))
        elm_idx.append(np.where(c_factor[:, i_data] > c_factor_percentile_value[i_data])[0])

    if t_function == mean_mep_threshold:
        stim_threshold_avg, stim_threshold_std = \
            mean_mep_threshold(elm_idx=elm_idx,
                               mep_curve=mep_curve,
                               intensities=intensities,
                               e=e,
                               mep_threshold=mep_threshold)

    elif t_function == sigmoid_thresh:
        stim_threshold_avg, stim_threshold_std = \
            sigmoid_thresh(elm_idx=elm_idx,
                           mep_curve=mep_curve,
                           intensities=intensities,
                           e=e,
                           mep_threshold=mep_threshold)

    elif t_function == intensity_thresh:
        stim_threshold_avg = \
            intensity_thresh(mep_curve=mep_curve,
                             intensities=intensities,
                             mep_threshold=mep_threshold)
        stim_threshold_std = np.nan

    else:
        raise NotImplementedError('Provided t_function not implemented yet!')

    return stim_threshold_avg, stim_threshold_std


def mean_mep_threshold(elm_idx, mep_curve, intensities, e, mep_threshold):
    """
    Determines the stimulation threshold by calculating the average electric field over all conditions, where the
    mep curves exceed the value of mep_threshold (in [mV]).

    Parameters
    ----------
    elm_idx : list of np.ndarray of int
        [n_datasets](n_elements) Element indices where the congruence factor exceeds a certain percentile,
        defined during the call of :py:meth:`stimulation_threshold`.
    mep_curve : list  of np.ndarray of float
        [n_conditions](n_samples) MEP curve values for every condition.
    intensities : list  of np.ndarray of float
        [n_conditions](n_samples) To the MEP values corresponding stimulator intensities in [A/us].
    e : list of list of np.ndarray of float
        [n_cond][n_datasets][n_elm] Tuple of n_datasets of the electric field to compute the congruence factor for,
        e.g. ``(e_mag, e_norm, e_tan)``.
        Each dataset is a list over all conditions containing the electric field component of interest

        * e.g.: ``len(e) = n_cond``
        * ``len(e[0]) = n_comp`` (e.g: ``e_mag = e[0])``)

    mep_threshold : float
        MEP value in [mV], which has to be exceeded for threshold definition.

    Returns
    -------
    stim_threshold_avg : float
        Average stimulation threshold in [V/m] where c_factor is greater than c_factor_percentile
    """

    n_conditions = len(mep_curve)
    n_datasets = len(e[0])

    # determine electric field values exceeding mep_threshold in this elements
    stim_threshold_cond = [np.zeros((elm_idx[i_data].size, n_conditions)) * np.nan for i_data in range(n_datasets)]
    stim_threshold_avg = [np.nan for _ in range(n_datasets)]
    stim_threshold_std = [np.nan for _ in range(n_datasets)]

    for i_cond in range(n_conditions):
        e_threshold_idx = np.where(mep_curve[i_cond] > mep_threshold)[0]

        if e_threshold_idx.any():
            for i_data in range(n_datasets):
                stim_threshold_cond[i_data][:, i_cond] = e[i_cond][i_data][elm_idx[i_data]] * \
                                                         intensities[i_cond][e_threshold_idx[0]]

    for i_data in range(n_datasets):
        stim_threshold_avg[i_data] = np.mean(
                stim_threshold_cond[i_data][np.logical_not(np.isnan(stim_threshold_cond[i_data]))])
        stim_threshold_std[i_data] = np.std(
                stim_threshold_cond[i_data][np.logical_not(np.isnan(stim_threshold_cond[i_data]))])

    return stim_threshold_avg, stim_threshold_std


def sigmoid_thresh(elm_idx, mep_curve, intensities, e, mep_threshold):
    """
    Determines the stimulation threshold by calculating an equivalent :py:class:`pynibs.expio.Mep.sigmoid`
    over all conditions. The stimulation threshold is the electric field value where the mep curves exceed the value of
    mep_threshold (in [mV]).

    Parameters
    ----------
    elm_idx : list of np.ndarray of int
        [n_datasets](n_elements) Element indices where the congruence factor exceeds a certain percentile,
        defined during the call of :py:meth:`stimulation_threshold`.
    mep_curve : list  of np.ndarray of float
        [n_conditions](n_samples) MEP curve values for every condition.
    intensities : list  of np.ndarray of float
        [n_conditions](n_samples) To the MEP values corresponding stimulator intensities in [A/us].
    e : list of list of np.ndarray of float
        [n_cond][n_datasets][n_elm] Tuple of n_datasets of the electric field to compute the congruence factor for,
        e.g. ``(e_mag, e_norm, e_tan)``.
        Each dataset is a list over all conditions containing the electric field component of interest

        * e.g.: ``len(e) = n_cond``
        * ``len(e[0]) = n_comp`` (e.g: ``e_mag = e[0])``)

    mep_threshold : float
        MEP value in [mV], which has to be exceeded for threshold definition

    Returns
    -------
    stim_threshold_avg : float
        Average stimulation threshold in [V/m] where c_factor is greater than c_factor_percentile
    """

    n_conditions = len(mep_curve)
    n_datasets = len(e[0])
    stim_threshold_elm = [[] for _ in range(n_datasets)]
    stim_threshold_avg = [[] for _ in range(n_datasets)]
    stim_threshold_std = [[] for _ in range(n_datasets)]

    # accumulate all data values in one array
    mep_curve_all = np.hstack(mep_curve)

    for i_data in range(n_datasets):
        print(('Evaluating stimulation threshold for dataset {}/{}'.format(i_data + 1, n_datasets)))
        n_elms = len(elm_idx[i_data])
        stim_threshold_elm[i_data] = np.zeros(n_elms) * np.nan

        for i_elm, elm in enumerate(elm_idx[i_data]):
            print((' > Element {}/{}'.format(i_elm, n_elms)))

            # accumulate all data values in one array
            e_all = []

            for i_cond in range(n_conditions):
                e_all.append(e[i_cond][i_data][elm] * intensities[i_cond])
            e_all = np.hstack(e_all)

            # fit data to function
            mep = pynibs.Mep(intensities=e_all, mep=mep_curve_all, intensity_min_threshold=0, mep_min_threshold=0)
            mep.fit = mep.run_fit_multistart(pynibs.sigmoid,
                                             x=e_all,
                                             y=mep_curve_all,
                                             p0=[70, 0.6, 2],
                                             constraints=None,
                                             verbose=False,
                                             n_multistart=20)

            # read out optimal function parameters from best fit
            try:
                for p in ['x0', 'r', 'amp']:
                    mep.popt.append(mep.fit.best_values[p])

                mep.popt = np.asarray(mep.popt)
                mep.cvar = np.asarray(mep.fit.covar)
                mep.pstd = np.sqrt(np.diag(mep.cvar))
                mep.fun = pynibs.sigmoid

                # determine stimulation threshold
                e_fit = np.linspace(np.min(e_all), np.max(e_all), 200)
                mep_fit = mep.eval_opt(e_fit)
                e_threshold_idx = np.where(mep_fit > mep_threshold)[0]

                if e_threshold_idx.any():
                    stim_threshold_elm[i_data][i_elm] = e_fit[e_threshold_idx[0]]

            except (AttributeError, ValueError):
                print(' > Warning: pynibs.sigmoid in element could not be fitted!')
                stim_threshold_elm[i_data][i_elm] = np.nan

        # determine mean threshold over all elements
        stim_threshold_avg[i_data] = np.mean(stim_threshold_elm[i_data]
                                             [np.logical_not(np.isnan(stim_threshold_elm[i_data]))])
        stim_threshold_std[i_data] = np.std(stim_threshold_elm[i_data]
                                            [np.logical_not(np.isnan(stim_threshold_elm[i_data]))])

    return stim_threshold_avg, stim_threshold_std


def intensity_thresh(mep_curve, intensities, mep_threshold):
    """
    Determines the stimulation threshold of one particular condition (usually the most sensitive e.g. M1-45). The
    stimulation threshold is the stimulator intensity value in [A/us] where the mep curves exceed the value of
    mep_threshold (in [mV]).

    Parameters
    ----------
    mep_curve: list [1] of np.ndarray of float [n_samples]
        MEP curve values for every conditions
    intensities: list [1] of np.ndarray of float [n_samples]
        To the MEP values corresponding stimulator intensities in [A/us]
    mep_threshold: float
        MEP value in [mV], which has to be exceeded for threshold definition

    Returns
    -------
    stim_threshold_avg: float
        Average stimulation threshold in [V/m] where c_factor is greater than c_factor_percentile
    """

    stim_threshold = np.nan
    i_threshold_idx = np.where(mep_curve[0] > mep_threshold)[0]

    if i_threshold_idx.any():
        stim_threshold = intensities[0][i_threshold_idx[0]]

    return stim_threshold
