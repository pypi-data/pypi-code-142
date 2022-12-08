import os
import copy
import pynibs
import numpy as np
import _pickle as pickle
import multiprocessing.pool

from _functools import partial
from pynibs import compute_chunks
from scipy.special import logsumexp
from scipy.interpolate import LinearNDInterpolator


def workhorse_interp(idx_list, interp, params):
    """
    Single core workhorse to interpolate data.

    Parameters
    ----------
    idx_list : np.array or list of float [n_interpolations]
        Indices in params array where the interpolation has to be performed (subset of all indices in params array)
    interp : scipy.interpolate instance
        Interpolator instance
    params : np.array of float [N_interpolations x N_params]
        Array containing the parameters the function is evaluated (total array with all parameters)

    Returns
    -------
    res : np.array of float [n_interpolations]
        Interpolation results (subset params[idx_list, :])
    """
    return interp(params[idx_list, 0], params[idx_list, 1], params[idx_list, 2]) / 2.2  # 2.2


def load_cell_model(fn_csv):
    """
    Load interpolation points of the mean field model from the specified CSV file.

    Parameters
    ----------
    fn_csv : str
        Fully qualified path to the CSV containing the interpolation points of the mean field model.

    Returns
    -------
    - scipy.interpolate.LinearNDInterpolator
    - interpolation points 'theta'
    - interpolation points 'gradient'
    """
    cell_simulation_data = [np.genfromtxt(fn_csv, delimiter=',')]

    thresholds = cell_simulation_data[-1][:, 4]
    theta = cell_simulation_data[-1][:, 3]
    rel_grad = cell_simulation_data[-1][:, 2]

    return LinearNDInterpolator(list(zip(theta, rel_grad)), thresholds), theta, rel_grad

# TODO: implement the creation of a response interpolator
def _create_model_response_interpolator(fn_model_csv):
    return LinearNDInterpolator([(0,0),(0,1),(1,0),(1,1)],[1,1,1,1], fill_value=1)

def calc_e_threshold(layerid, theta, gradient=None, mep=None, neuronmodel="threshold", waveform="biphasic"):
    """
    Determine sensitivity map of electric field

    Parameters
    ----------
    layerid : str
        Choose from the neocortical layers (e.g. "L1", "L23", "L4", "L5", "L6"). The respective threshold model will
        be loaded.
    theta : np.ndarray
        Theta angle (matrix) [N_stim x N_ele] of electric field with respect to surface normal. in degrees [0 .. 180]
    gradient : np.ndarray, optional, default: None
        Electric field gradient (matrix) [N_stim x N_ele] between layer 1 and layer 6. Optional, the neuron mean field
        model is more accurate when provided. Percent [-100 .. 100]
    mep : np.array of float [N_stim], optional, default: None
        MEP data (required in case of "IOcurve" approach (neuronmodel)
    neuronmodel : str, optional, default: "threshold"
        Select neuron model to modify the electric field values
        - "threshold": subtract mean threshold from electric field
        - "IOcurve": subtract value read from precomputed neuron IO curve from electric field
    waveform : str, optional, default: biphasic
        Waveform of TMS pulse:
        - "monophasic"
        - "biphasic"

    Returns
    -------
    e_sens : np.ndarray
        Electric field sensitivity maps [N_stim x N_ele]
    """

    models_folder = os.path.join(pynibs.__datadir__, "neuron", "models")
    interp_folder = os.path.join(pynibs.__datadir__, "neuron", "interpolators")

    if waveform == "monophasic":
        models = {
            "L23": os.path.join(models_folder, "L23_PC_cADpyr_monophasic_0_0_21_3_6.csv"),
            "L5": os.path.join(models_folder, "L5_TTPC2_cADpyr_monophasic_0_0_21_3_6.csv")
        }

        models_io = {
            "L23": os.path.join(interp_folder, "L23_biphasic_recruitment_rate_interpolator_inverse.pkl"),
            "L5": os.path.join(interp_folder, "L5_biphasic_recruitment_rate_interpolator_inverse.pkl")
        }
    elif waveform == "biphasic":
        models = {
            "L23": os.path.join(models_folder, "L23_PC_cADpyr_biphasic_0_0_21_3_6.csv"),
            "L5": os.path.join(models_folder, "L5_TTPC2_cADpyr_biphasic_0_0_21_3_6.csv")
        }

        models_io = {
            "L23": os.path.join(interp_folder, "L23_biphasic_recruitment_rate_interpolator_inverse.pkl"),
            "L5": os.path.join(interp_folder, "L5_biphasic_recruitment_rate_interpolator_inverse.pkl")
        }
    else:
        NotImplementedError(f"Specified waveform {waveform} not implemented.")

    if neuronmodel == "threshold":
        interp, thetas, rel_gradients = load_cell_model(models[layerid])

    elif neuronmodel == "IOcurve":
        _, thetas, rel_gradients = load_cell_model(models[layerid])

        # TODO: not implemented yet
        if not os.path.exists(models_io[layerid]):
            raise NotImplementedError("[neuron_regression] Pickl files containing the response interpolators "
                                      f"do not exist (path checked: {models_io[layerid]}) and their creation "
                                      "is not implemented yet.")
            # interp = _create_model_response_interpolator(models[layerid])
            # with open(models_io[layerid], 'wb') as f:
            #    pickle.dump(interp, f)
        else:
            with open(models_io[layerid], 'rb') as f:
                interp = pickle.load(f)

    else:
        raise NotImplementedError(f"Specified neuronmodel {neuronmodel} not implemented!")

    # bound observed values to min/max values available in the model
    theta_bound = theta
    theta_bound[np.where(theta > np.max(thetas))] = np.max(thetas)
    theta_bound[np.where(theta < np.min(thetas))] = np.min(thetas)

    if gradient is None:
        gradient_bound = np.zeros(theta.shape)
    else:
        gradient_bound = gradient
        gradient_bound[np.where(gradient > np.max(rel_gradients))] = np.max(rel_gradients)
        gradient_bound[np.where(gradient < np.min(rel_gradients))] = np.min(rel_gradients)

    if neuronmodel == "threshold":
        e_thres = interp(theta_bound, gradient_bound) / 3

    elif neuronmodel == "IOcurve":
        # normalize MEPs between [0, 0.999]
        mep_threshold = 2
        mep_cropped = copy.deepcopy(mep)
        mep_cropped[mep > mep_threshold] = mep_threshold
        mep_norm = mep_cropped / (mep_threshold * 1.05)

        # calculate expected electric field at observed MEP
        params = np.zeros((theta.shape[0] * theta.shape[1], 3))
        params[:, 0] = gradient_bound.flatten()
        params[:, 1] = theta_bound.flatten()
        params[:, 2] = np.repeat(mep_norm, theta.shape[1])

        idx = np.arange(params.shape[0])
        idx_chunked = compute_chunks(list(idx), multiprocessing.cpu_count())

        pool = multiprocessing.Pool(multiprocessing.cpu_count())
        workhorse_partial = partial(workhorse_interp, interp=interp, params=params)
        res = np.hstack(pool.map(workhorse_partial, idx_chunked))
        e_thres = np.reshape(res, theta.shape)
        pool.close()
        pool.join()

    return e_thres


def calc_e_effective(e, layerid, theta, gradient=None, neuronmodel="threshold", mep=None, waveform="biphasic"):
    """
    Determines the effective electric field using a neuron mean field model.
    Transforms the electric field by subtracting the threshold map (in V/m) from the original electric field.
    The remaining field is the effective electric field (e_eff), generating the stimulation effect,
    i.e. behavioural effects start at e_eff > 0 because lower fields were not able to stimulate neurons.

    Parameters
    ----------
    e : np.ndarray
        Electric field (matrix) [N_stim x N_ele]
    layerid : str
        Choose from the neocortical layers (e.g. "L1", "L23", "L4", "L5", "L6")
    theta : np.ndarray
        Theta angle (matrix) [N_stim x N_ele] of electric field with respect to surface normal
    gradient : np.ndarray, optional, default: None
        Electric field gradient (matrix) [N_stim x N_ele] between layer 1 and layer 6. Optional, the neuron mean field
        model is more accurate when provided.
    neuronmodel : str, optional, default: "threshold"
        Select neuron model to modify the electric field values
        - "threshold": subtract mean threshold from electric field
        - "IOcurve": subtract value read from precomputed neuron IO curve from electric field
    mep : np.array of float [N_stim], optional, default: None
        MEP data (required in case of "IOcurve" approach (neuronmodel)
    waveform : str, optional, default: biphasic
        Waveform of TMS pulse:
        - "monophasic"
        - "biphasic"

    Returns
    -------
    e_eff : np.ndarray
        Effective electric field (matrix) [N_stim x N_ele] the regression analysis can be performed with.
    """
    # determine sensitivity map
    e_thres = calc_e_threshold(layerid=layerid,
                               theta=theta,
                               gradient=gradient,
                               neuronmodel=neuronmodel,
                               mep=mep,
                               waveform=waveform)

    # determine effective electric field
    e_eff = e - e_thres

    return e_eff
