import h5py
import math
import warnings
import numpy as np
from tqdm import tqdm
import multiprocessing
from functools import partial
from numpy import cross as cycross
from scipy.spatial import Delaunay

import pynibs


def calc_tet_volume(points, abs=True):
    """
    Calculate tetrahedra volumes.

    Parameters
    ----------
    points: np.ndarray
        shape: (n_tets,4,3)
        [[[Ax, Ay, Az],
          [Bx, By, Bz],
          [Cx, Cy, Cz],
          [Dx, Dy, Dy]],

         [[Ax, Ay, Az],
          [Bx, By, Bz],
          [Cx, Cy, Cz],
          [Dx, Dy, Dy]],

        ...

        ]

    Returns
    -------
    volume: np.ndarray
        shape: (n_tets)

    Other Parameters
    ----------------
    abs : bool
        Return magnitude. Default: True.
    """
    if points.ndim == 2:
        points = np.atleast_3d(points).reshape(1, 4, 3)
    if points.ndim != 3:
        raise ValueError(f"Wrong dimensions for points: ({points.shape}). Expected: (n_tets,4,3))")

    a = np.zeros((points.shape[0], 4, 4))
    a[:, :, 3] = 1
    a[:, :, :3] = points
    a = a.swapaxes(1, 2)

    if abs:
        return np.abs(1 / 6 * np.linalg.det(a))
    else:
        return 1 / 6 * np.linalg.det(a)


def calc_tri_surface(points):
    """
    Calculate triangle surface areas.

    Parameters
    ----------
    points : np.ndarray
        (n_triangles,3,3)

    Returns
    -------
    triange_area : np.ndarray
    """
    a = np.linalg.norm(points[:, 0] - points[:, 1], axis=1)
    b = np.linalg.norm(points[:, 1] - points[:, 2], axis=1)
    c = np.linalg.norm(points[:, 0] - points[:, 2], axis=1)
    s = np.sum((a, b, c), axis=0) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5


def get_sphere(mesh=None, mesh_fn=None, target=None, radius=None, roi_idx=None, roi=None, elmtype='tris'):
    """
    Return element idx of elements within a certain distance to provided target.
    Element indices are 0-based (tris and tets start at 0, 'pynibs' style)
    Elements might be 'tris' (default) or 'tets'

    If roi object / idx and mesh fn is provided, the roi is expected to have midlayer information and the roi
    geometry is used.

    Parameters
    ----------
    mesh : pynibs.mesh.TetrahedraLinear, optional
    mesh_fn : str, optional
        Filename to SimNIBS .msh or pyNIBS .hdf5 mesh file
    target : np.ndarray of float, optional
        (3,) X, Y, Z coordinates of target
    radius : float, optional
        Sphere radius im mm
    roi_idx : str or int
        ROI name
    elmtype : str, optional
        Return triangles or tetrahedra in sphere around target. One of ('tris', 'tets')

    Returns
    -------
    elms_in_sphere : np.ndarray
        (n_elements): Indices of elements found in ROI
    """
    if mesh_fn is not None:
        if mesh is not None:
            raise ValueError("Either provide mesh or mesh_fn")
        if mesh_fn.endswith('.hdf5'):
            mesh = pynibs.load_mesh_hdf5(mesh_fn)
        elif mesh_fn.endswith('.msh'):
            mesh = pynibs.load_mesh_msh(mesh_fn)
    if roi is None and roi_idx is not None:
        if mesh_fn is None:
            raise ValueError("Provide mesh_fn to load roi from")
        roi = pynibs.load_roi_surface_obj_from_hdf5(mesh_fn)[roi_idx]
    if elmtype == 'tris':
        return tris_in_sphere(mesh=mesh, target=target, radius=radius, roi=roi)
    elif elmtype == 'tets':
        return tets_in_sphere(mesh=mesh, target=target, radius=radius, roi=roi)
    else:
        raise ValueError(f"Unknown elmtpye '{elmtype}'")


def tets_in_sphere(mesh, target, radius, roi):
    """
    Worker function for get_sphere()

    Returns element idx of elements within a certain distance to provided target.
    If roi object / idx and mesh fn is provided, the roi is expected to have midlayer information and the roi
    geometry is used.

    Parameters
    ----------
    mesh : pynibs.TetrahedraLinear, optional
    target : np.ndarray of float, optional
        (3,) X, Y, Z coordinates of target
    radius : float, optional
        Sphere radius im mm
    roi : pynibs.mesh.ROI, optional
        Region of interest

    Returns
    -------
    tets_in_sphere : np.ndarray
        (n_tets): Indices of elements found in ROI

    """
    if roi is None:
        if radius is None or radius == 0:
            return np.where(np.linalg.norm(mesh.tetrahedra_center - target, axis=1) ==
                            np.min(np.linalg.norm(mesh.tetrahedra_center - target, axis=1)))[0]

        else:
            return np.where(np.linalg.norm(mesh.tetrahedra_center - target, axis=1) <= radius)[0]

    else:
        warnings.warn("Sphere 'tets' extraction from ROI untested! Consider extracting 'tris' instead.")
        if radius is not None and radius > 0:
            tri_target_idx = np.where(np.linalg.norm(roi.tri_center_coord_mid - target, axis=1) <= radius)[0]
        else:
            tri_target_idx = np.where(np.linalg.norm(roi.tri_center_coord_mid - target, axis=1) == np.min(
                    np.linalg.norm(roi.tri_center_coord_mid - target, axis=1)))[0]
        tet_target_idx = roi.tet_idx_tri_center_mid[tri_target_idx]
        return tet_target_idx


def tris_in_sphere(mesh, target, radius, roi):
    """
    Worker function for get_sphere().

    Returns triangle idx of elements within a certain distance to provided target.
    If roi object / idx and mesh fn is provided, the roi is expected to have midlayer information and the roi
    geometry is used.

    Parameters
    ----------
    mesh : pynibs.mesh.TetrahedraLinear, optional
    target : np.ndarray of float, optional
        (3,) X, Y, Z coordinates of target
    radius : float, optional
        Sphere radius im mm
    roi : pynibs.mesh.ROI, optional
        ROI

    Returns
    -------
    tris_in_sphere : np.ndarray
        (n_triangles): Indices of elements found in sphere
    """
    if roi is None:
        if radius is None or radius == 0:
            tri_target_idx = np.where(np.linalg.norm(mesh.triangles_center - target, axis=1) ==
                                      np.min(np.linalg.norm(mesh.triangles_center - target, axis=1)))[0]
        else:
            tri_target_idx = np.where(np.linalg.norm(mesh.triangles_center - target, axis=1) <= radius)[0]
    else:
        if radius is not None and radius > 0:
            tri_target_idx = np.where(np.linalg.norm(roi.tri_center_coord_mid - target, axis=1) <= radius)[0]
        else:
            tri_target_idx = np.where(np.linalg.norm(roi.tri_center_coord_mid - target, axis=1) == np.min(
                    np.linalg.norm(roi.tri_center_coord_mid - target, axis=1)))[0]

    return tri_target_idx


def sample_sphere(n_points, r):
    """
    Creates n_points evenly spread in a sphere of radius r.

    Parameters
    ----------
    n_points: int
        Number of points to be spread, must be odd
    r: float
        Radius of sphere

    Returns
    -------
    points: np.ndarray of float [N x 3]
        Evenly spread points in a unit sphere
    """

    assert n_points % 2 == 1, "The number of points must be odd"
    points = []

    # The golden ratio
    phi = (1 + math.sqrt(5)) / 2.
    n = int((n_points - 1) / 2)

    for i in range(-n, n + 1):
        lat = math.asin(2 * i / n_points)
        lon = 2 * math.pi * i / phi
        x = r * math.cos(lat) * math.cos(lon)
        y = r * math.cos(lat) * math.sin(lon)
        z = r * math.sin(lat)
        points.append((x, y, z))

    points = np.array(points, dtype=float)

    return points


def get_indices_discontinuous_data(data, con, neighbor=False, deviation_factor=2,
                                   min_val=None, not_fitted_elms=None, crit='median', neigh_style='point'):
    """
    Get element indices (and the best neighbor index), where the data is discontinuous

    Parameters
    ----------
    data : np.ndarray of float [n_data]
        Data array to analyze given in the element center
    con : np.ndarray of float [n_data, 3 or 4]
        Connectivity matrix
    neighbor : boolean, optional, default=False
        Return also the element index of the "best" neighbor (w.r.t. median of data)
    deviation_factor : float
        Allows data deviation from 1/deviation_factor < data[i]/median < deviation_factor
    min_val : float, optional
        If given, only return elements which have a neighbor with data higher than min_val.
    not_fitted_elms : np.ndarray
        If given, these elements are not used as neighbors
    crit: str, default: median
        Criterium for best neighbor. Either median or max value
    neigh_style : str, default: 'point'
        Should neighbors share point or 'edge'

    Returns
    -------
    idx_disc : list of int [n_disc]
        Index list containing the indices of the discontinuous elements
    idx_neighbor : list of int [n_disc]
        Index list containing the indices of the "best" neighbors of the discontinuous elements
    """

    n_ele = con.shape[0]
    idx_disc, idx_neighbor = [], []

    data[data == 0] = 1e-12

    if neigh_style == 'point':
        def get_neigh(m):
            return np.logical_and(0 < mask, mask < 3)
    elif neigh_style == 'edge':
        def get_neigh(m):
            return mask == 2
    else:
        raise NotImplementedError(f"neigh_style {neigh_style} unknown.")

    if crit == 'median':
        def is_neigh():
            if not (1 / deviation_factor < data_i / median < deviation_factor):
                neighbor_indices = np.where(mask_neighbor)[0]
                best_neigh = neighbor_indices[(np.abs(data[neighbor_indices] - median)).argmin()]
                if min_val is None or data[best_neigh] > min_val:
                    idx_disc.append(elm_i)
                # if neighbor:
                idx_neighbor.append(best_neigh)
    elif crit == 'max':
        def is_neigh():
            if data_i / median < 1 / deviation_factor:
                neighbor_indices = np.where(mask_neighbor)[0]
                best_neigh = neighbor_indices[(data[neighbor_indices]).argmax()]
                if min_val is None or data[best_neigh] > min_val:
                    idx_disc.append(elm_i)

                # if neighbor:
                idx_neighbor.append(best_neigh)
    elif crit == 'randmax':
        def is_neigh():
            if data_i / median < 1 / deviation_factor:
                neighbor_indices = np.where(mask_neighbor)[0]
                best_neigh = np.random.choice(neighbor_indices[(data[neighbor_indices]) > 0], 1)
                if min_val is None or data[best_neigh] > min_val:
                    idx_disc.append(elm_i)

                # if neighbor:
                idx_neighbor.append(best_neigh)
    else:
        raise NotImplementedError(f"Criterium {crit} unknown. ")

    for elm_i, data_i in zip(range(n_ele), data):
        if elm_i in not_fitted_elms:
            continue

        # find neighbors
        mask = np.sum(np.isin(con, con[elm_i, :]), axis=1)
        mask_neighbor = get_neigh(mask)

        # best_values are set to 0 for bad elements and unfittable ones. do not use these as neighbors
        if not_fitted_elms is not None and len(not_fitted_elms) != 0:
            mask_neighbor[not_fitted_elms] = False

        # if the element is lonely floating and has no neighbors ... continue
        if not np.sum(mask_neighbor):
            continue

        # check if current value does not fit to neighbors
        median = np.median(data[mask_neighbor])

        if not median:
            median = 1e-12

        is_neigh()

        # if not (1 / deviation_factor < data_i / median < deviation_factor):
        #     # find best neighbor idx
        #     neighbor_indices = np.where(mask_neighbor)[0]
        #
        #     if crit == 'max':
        #         best_neigh = neighbor_indices[(data[neighbor_indices]).argmax()]
        #     elif crit == 'median':
        #         best_neigh = neighbor_indices[(np.abs(data[neighbor_indices] - median)).argmin()]
        #     else:
        #         raise  NotImplementedError(f"Criterium {crit} unknown. ")
        #     if min_val is None or data[best_neigh] > min_val:
        #         idx_disc.append(elm_i)
        #
        #     if neighbor:
        #         idx_neighbor.append(best_neigh)

        # stop = time.time()
        # print(stop-start)

    if neighbor:
        return idx_disc, idx_neighbor
    else:
        return idx_disc


def find_nearest(array, value):
    """
    Given an "array", and given a "value" , returns an index j such that "value" is between array[j]
    and array[j+1]. "array" must be monotonic increasing. j=-1 or j=len(array) is returned
    to indicate that "value" is out of range below and above respectively.

    Parameters
    ----------
    array : np.ndarray of float
        Monotonic increasing array
    value : float
        Target value the nearest neighbor index in "array" is computed for

    Returns
    -------
    idx : int
        Index j such that "value" is between array[j] and array[j+1]

    """
    n = len(array)
    if value < array[0]:
        return -1
    elif value > array[n - 1]:
        return n
    jl = 0  # Initialize lower
    ju = n - 1  # and upper limits.
    while ju - jl > 1:  # If we are not yet done,
        jm = (ju + jl) >> 1  # compute a midpoint with a bitshift
        if value >= array[jm]:
            jl = jm  # and replace either the lower limit
        else:
            ju = jm  # or the upper limit, as appropriate.
    # Repeat until the test condition is satisfied.
    if value == array[0]:  # edge cases at bottom
        return 0
    elif value == array[n - 1]:  # and top
        return n - 1
    else:
        return jl


def in_hull(points, hull):
    """
    Test if points in `points` are in `hull`.
    `points` should be a [N x K] coordinates of N points in K dimensions.
    `hull` is either a scipy.spatial.Delaunay object or the [M x K] array of the
    coordinates of M points in Kdimensions for which Delaunay triangulation
    will be computed.

    Parameters
    ----------
    points : np.ndarray
        (N_points x 3) Set of floating point data to test whether they are lying inside the hull or not
    hull : scipy.spatial.Delaunay  or np.ndarray
         (M x K) Surface data

    Returns
    -------
    inside : np.ndarray of bool
        TRUE: point inside the hull
        FALSE: point outside the hull
    """

    if not isinstance(hull, Delaunay):
        hull = Delaunay(hull)
    return hull.find_simplex(points) >= 0


def calc_tetrahedra_volume_cross(P1, P2, P3, P4):
    """
    Calculates volume of tetrahedra specified by the 4 points P1...P4
    multiple tetrahedra can be defined by P1...P4 as 2-D np.arrays
    using the cross and vector dot product

    .. math::
        P1=\\begin{bmatrix}
        x_{{tet}_1} & y_{{tet}_1} & z_{{tet}_1}   \\\\
        x_{{tet}_2} & y_{{tet}_2} & z_{{tet}_2}   \\\\
        ... & ... & ...    \\\\
        x_{{tet}_N} & y_{{tet}_N} & z_{{tet}_N}    \\\\
        \\end{bmatrix}

    Parameters
    ----------
    P1 : np.ndarray of float [N_tet x 3]
        Coordinates of first point of tetrahedra
    P2 : np.ndarray of float [N_tet x 3]
        Coordinates of second point of tetrahedra
    P3 : np.ndarray of float [N_tet x 3]
        Coordinates of third point of tetrahedra
    P4 : np.ndarray of float [N_tet x 3]
        Coordinates of fourth point of tetrahedra

    Returns
    -------
    tetrahedra_volume: np.ndarray of float [N_tet x 1]
        Volumes of tetrahedra
    """

    tetrahedra_volume = 1.0 / 6 * \
                        np.sum(np.multiply(cycross(P2 - P1, P3 - P1), P4 - P1), 1)
    tetrahedra_volume = tetrahedra_volume[:, np.newaxis]
    return tetrahedra_volume


def calc_tetrahedra_volume_det(P1, P2, P3, P4):
    """
    Calculate volume of tetrahedron specified by 4 points P1...P4
    multiple tetrahedra can be defined by P1...P4 as 2-D np.arrays
    using the determinant.


    .. math::
        P1=\\begin{bmatrix}
        x_{{tet}_1} & y_{{tet}_1} & z_{{tet}_1}   \\\\
        x_{{tet}_2} & y_{{tet}_2} & z_{{tet}_2}   \\\\
        ... & ... & ...    \\\\
        x_{{tet}_N} & y_{{tet}_N} & z_{{tet}_N}    \\\\
        \\end{bmatrix}

    Parameters
    ----------
    P1 : np.ndarray of float [N_tet x 3]
        Coordinates of first point of tetrahedra
    P2 : np.ndarray of float [N_tet x 3]
        Coordinates of second point of tetrahedra
    P3 : np.ndarray of float [N_tet x 3]
        Coordinates of third point of tetrahedra
    P4 : np.ndarray of float [N_tet x 3]
        Coordinates of fourth point of tetrahedra

    Returns
    -------
    tetrahedra_volume : np.ndarray of float [N_tet x 1]
        Volumes of tetrahedra
    """

    N_tets = P1.shape[0] if P1.ndim > 1 else 1

    # add ones
    j1 = np.hstack((np.ones((N_tets, 1)), P1))
    j2 = np.hstack((np.ones((N_tets, 1)), P2))
    j3 = np.hstack((np.ones((N_tets, 1)), P3))
    j4 = np.hstack((np.ones((N_tets, 1)), P4))

    j = np.zeros((P1.shape[0] if P1.ndim > 1 else 1, 4, 4))

    j[:, :, 0] = j1
    j[:, :, 1] = j2
    j[:, :, 2] = j3
    j[:, :, 3] = j4

    tetrahedra_volume = 1.0 / 6.0 * np.linalg.det(j)
    tetrahedra_volume = tetrahedra_volume[:, np.newaxis]
    return tetrahedra_volume


def calc_gradient_surface(phi, points, triangles):
    """
    Calculate gradient of potential phi on surface (i.e. tangential component) given in vertices of a triangular
    mesh forming a 2D surface.

    Parameters
    ----------
    phi : np.ndarray of float [N_points x 1]
        Potential in nodes
    points : np.ndarray of float [N_points x 3]
        Coordinates of nodes (x,y,z)
    triangles : np.ndarray of int32 [N_tri x 3]
        Connectivity of triangular mesh

    Returns
    -------
    grad_phi : np.ndarray of float [N_tri x 3]
        Gradient of potential phi on surface
    """

    grad_phi = np.zeros((triangles.shape[0], 3))

    for i in range(triangles.shape[0]):
        a = np.array([[points[triangles[i, 0], 0] - points[triangles[i, 2], 0],
                       points[triangles[i, 0], 1] - points[triangles[i, 2], 1],
                       points[triangles[i, 0], 2] - points[triangles[i, 2], 2]],
                      [points[triangles[i, 1], 0] - points[triangles[i, 2], 0],
                       points[triangles[i, 1], 1] - points[triangles[i, 2], 1],
                       points[triangles[i, 1], 2] - points[triangles[i, 2], 2]]])

        b = np.array([phi[triangles[i, 0]] - phi[triangles[i, 2]],
                      phi[triangles[i, 1]] - phi[triangles[i, 2]]])

        grad_phi[i, :] = np.dot(np.linalg.pinv(a), b).T

    return grad_phi


def determine_e_midlayer_workhorse(fn_e_results, subject, mesh_idx, midlayer_fun, fn_mesh_hdf5, roi_idx, phi_scaling=1.,
                                   verbose=False):
    """
    phi_scaling: float
        simnibs < 3.0  : 1000.
        simnibs >= 3.0 :    1. (Default)
    """

    if verbose:
        print(f"Loading Mesh and ROI {roi_idx} from {fn_mesh_hdf5}")

    msh = pynibs.load_mesh_hdf5(fn_mesh_hdf5)
    roi = pynibs.load_roi_surface_obj_from_hdf5(fn_mesh_hdf5)

    for fn_e in fn_e_results:

        with h5py.File(fn_e + ".hdf5", 'r') as f:
            phi = f['data/nodes/v'][:][:, np.newaxis]
            # phi = f['data/potential'][:][:, np.newaxis]
            dadt = f['data/nodes/D'][:]
            # dadt = np.reshape(f['data/dAdt'][:], (phi.shape[0], 3), order="c")

        # determine e_norm and e_tan for every simulation
        if verbose:
            print(f"Determine midlayer E-field for {fn_e}.hdf5")

        # choose which function to use for midlayer computation
        if midlayer_fun == "pynibs":
            e_norm_temp, e_tan_temp = msh.calc_E_on_GM_WM_surface3(phi=phi * phi_scaling,
                                                                   dAdt=dadt,
                                                                   roi=roi[roi_idx],
                                                                   verbose=False,
                                                                   mode='magnitude')

            e_norm_temp = e_norm_temp.flatten() * -1
            e_tan_temp = e_tan_temp.flatten()
            e_mag_temp = np.linalg.norm(np.vstack([e_norm_temp, e_tan_temp]).transpose(), axis=1).flatten()

        elif midlayer_fun == "simnibs":
            e_norm_temp_simnibs, e_tan_temp_simnibs = msh.calc_E_on_GM_WM_surface_simnibs_KW(phi=phi * phi_scaling,
                                                                                             dAdt=dadt,
                                                                                             roi=roi[roi_idx],
                                                                                             verbose=False,
                                                                                             subject=subject,
                                                                                             mesh_idx=mesh_idx)

            e_norm_temp_simnibs = e_norm_temp_simnibs.flatten()
            e_tan_temp_simnibs = e_tan_temp_simnibs.flatten()
            e_mag_temp_simnibs = np.linalg.norm(np.vstack([e_norm_temp_simnibs, e_tan_temp_simnibs]).transpose(),
                                                axis=1).flatten()
        else:
            raise ValueError(f"midlayer_fun {midlayer_fun} not implemented.")

        del phi, dadt

        with h5py.File(fn_e + ".hdf5", 'a') as f:
            try:
                del f['data/midlayer/roi_surface/{}/E_mag'.format(roi_idx)]
                del f['data/midlayer/roi_surface/{}/E_tan'.format(roi_idx)]
                del f['data/midlayer/roi_surface/{}/E_norm'.format(roi_idx)]
            except KeyError:
                pass

            f.create_dataset('data/midlayer/roi_surface/{}/E_mag'.format(roi_idx), data=e_mag_temp_simnibs)
            f.create_dataset('data/midlayer/roi_surface/{}/E_tan'.format(roi_idx), data=e_tan_temp_simnibs)
            f.create_dataset('data/midlayer/roi_surface/{}/E_norm'.format(roi_idx), data=e_norm_temp_simnibs)

        if verbose:
            print("\tAdding results to {}".format(fn_e + ".hdf5"))


def determine_e_midlayer(fn_e_results, fn_mesh_hdf5, subject, mesh_idx, roi_idx, n_cpu=4, midlayer_fun="simnibs",
                         phi_scaling=1., verbose=False):
    """
    Parallel version to determine the midlayer e-fields from a list of .hdf5 results files

    Parameters
    ----------
    fn_e_results : list of str
        List of results filenames (.hdf5 format)
    fn_mesh_hdf5 : str
        Filename of corresponding mesh file
    subject : pynibs.Subject
        Subject object
    mesh_idx : int
        Mesh index
    roi_idx : int
        ROI index
    n_cpu : int, optional, default: 4
        Number of parallel computations
    midlayer_fun : str, optional, default: "simnibs"
        Method to determine the midlayer e-fields ("pynibs" or "simnibs")
    phi_scaling : float, optional, default: 1.0
        Scaling factor of scalar potential to change between "m" and "mm"

    Returns
    -------
    <File> .hdf5 file
        Adds midlayer e-field results to ROI
    """

    # msh = pynibs.load_mesh_msh(subject.mesh[mesh_idx]['fn_mesh_msh'])

    n_cpu_available = multiprocessing.cpu_count()
    n_cpu = min(n_cpu, n_cpu_available)

    workhorse_partial = partial(determine_e_midlayer_workhorse,
                                subject=subject,
                                mesh_idx=mesh_idx,
                                midlayer_fun=midlayer_fun,
                                fn_mesh_hdf5=fn_mesh_hdf5,
                                roi_idx=roi_idx,
                                phi_scaling=phi_scaling,
                                verbose=verbose)

    fn_e_results_chunks = pynibs.compute_chunks(fn_e_results, n_cpu)
    pool = multiprocessing.Pool(n_cpu)
    pool.map(workhorse_partial, fn_e_results_chunks)
    pool.close()
    pool.join()


def find_element_idx_by_points(nodes, con, points):
    """
    Finds the tetrahedral element index of an arbitrary point in the FEM mesh.

    Parameters
    ----------
    nodes : np.ndarray [N_nodes x 3]
        Coordinates (x, y, z) of the nodes
    con : np.ndarray [N_tet x 4]
        Connectivity matrix
    points : np.ndarray [N_points x 3]
        Points for which the element indices are found.

    Returns
    -------
    ele_idx : np.ndarray [N_points]
        Element indices of tetrahedra where corresponding 'points' are lying in
    """

    node_idx = []
    for i in range(points.shape[0]):
        node_idx.append(np.where(np.linalg.norm(nodes - points[i, :], axis=1) < 1e-2)[0])

    # ele_idx = np.where((con == np.array(node_idx)).all(axis=1))[0]
    ele_idx = np.where(np.all(np.sort(con, axis=1) == np.sort(np.array(node_idx).flatten()), axis=1))[0]
    return ele_idx


def check_islands_for_single_elm(source_elm, connectivity=None, adjacency=None, island_crit=1):
    """
    This identifies islands in a mesh for a given element. An island is a set of elements, that is only connect
    via a single node to another set of elements.
    These islands usually crash the FEM solver and should be removed.

    1. Find all elements connect to source_elm via one node (1-node-neighbor)
    2. Start with source_elm and visit all 2-node-neighbors ('shared-edge)
    3. Continue recursively with all 2-node-neighbors and visit their 2-node-neighbors
    4. See if any 1-node-neighbors have not been visited with this strategy. If so, an island has been found

    Parameters
    ----------
    source_elm : int
        The source element to check
    connectivity : np.ndarray, optional
        Connectivity ('node_number_list') starting with 0. Can be triangles or tetrahedra
        (n_elms, 3) or (n_elms_4).
    adjacency : np.ndparray, optional
        Adjenceny matrix (n_elm, n_elm). Weights are supposed to be number of shared nodes.
        Computed from neighbors if not provided.
    island_crit : int, optional, default: 'any'
        How many nodes to define islands?
        'any' -> Elements connected via a single node or single edge are defined as an island.
        'node' -> Elements connected via a single _node_ are defined as an island.
        'edge' -> Elements connected via a single _edge_ are defined as an island.

    Returns
    -------
    n_visited : int
    n_not_visited : int
    neighbors_visited : dict, which neighbors have been visited and which have not
    """
    if adjacency is not None and connectivity is not None:
        raise ValueError(f"Provide either neighbors or connectivity, not both.")

    if adjacency is None:
        assert connectivity is not None
        adjacency = np.array([np.sum(np.isin(connectivity, elm), axis=1) for elm in connectivity])

    if island_crit == 'any':
        # find elements with only one node in common
        neighbors_visited = {i: False for i in np.where(adjacency[source_elm] >= 1)[0]}
        island_crit = 1
    elif island_crit == 'node':
        # find elements with only one node in common
        neighbors_visited = {i: False for i in np.where(adjacency[source_elm] == 1)[0]}
        island_crit = 1
    elif island_crit == 'edge':
        # find elements with only one node in common
        neighbors_visited = {i: False for i in np.where(adjacency[source_elm] == 2)[0]}
        island_crit = 2
    else:
        raise ValueError

    # now visit all elements with 2 or more neighboring elements recursivly.
    # everything that's left over between 1 and 2 neighbors is an island
    neighs_to_check = set(np.where(adjacency[source_elm] >= island_crit)[0].tolist())

    # add the starting element to the list
    neighs_to_check.add(source_elm)
    # go through all elements in list
    # print(neighs_to_check)
    while neighs_to_check:
        elm = neighs_to_check.pop()
        neighbors_visited[elm] = True

        # now add all 2-node neighbors for this element
        # for neigh in np.where(adjacency[elm] > 1)[0]:
        sort = (-adjacency[elm]).argsort()
        for idx in np.arange((np.bincount(adjacency[elm])[(island_crit):]).sum()):
            i = sort[idx]
            if i not in neighbors_visited or not neighbors_visited[i]:
                # print(i)
                neighs_to_check.add(i)

    return np.sum([v for v in neighbors_visited.values()]), \
           np.sum([not v for v in neighbors_visited.values()]), \
           neighbors_visited


def find_islands(connectivity=None, adjacency=None, island_crit='any', verbose=False, largest=False):
    """
    This identifies islands in a mesh. An island is a set of elements, that is only connect
    via a single node to another set of elements.
    These islands usually crash the FEM solver and should be removed.

    For each element:
        1. Find all elements connect to source_elm via one node (1-node-neighbor)
        2. Start with source_elm and visit all 2-node-neighbors ('shared-edge)
        3. Continue recursively with all 2-node-neighbors and visit their 2-node-neighbors
        4. See if any 1-node-neighbors have not been visited with this strategy. If so, an island has been found

    .. figure:: ../../doc/images/find_islands.png
       :scale: 50 %
       :alt: Island detection

       Islands are groups of elements that are only connected via a single node/edge to another group.

    Parameters
    ----------
    connectivity : np.ndarray, optional
        Connectivity ('node_number_list') starting with 0. Can be triangles or tetrahedra
        (n_elms, 3) or (n_elms_4).
    adjacency : np.ndparray, optional
        Adjenceny matrix (n_elm, n_elm). Weights are supposed to be number of shared nodes.
        Computed from neighbors if not provided.
    island_crit : int, optional, default: 'any'
        How many nodes to define islands?
        'any' -> Elements connected via a single node or single edge are defined as an island.
        'node' -> Elements connected via a single _node_ are defined as an island.
        'edge' -> Elements connected via a single _edge_ are defined as an island.
    largest : book, default: False
        Only return largest island, speeds up computation quite a bit if only one large, and many small islands exist.
    verbose : bool, optional
        Print some verbosity information. Default: False
    Returns
    -------
        elms_with_island : list
            Elements with neighboring islands
        counter_visited : np.ndarray
            shape = (n_elms). How often as each element been visited.
        counter_not_visited : np.ndarray
            shape = (n_elms). How often as each element not been visited.
    """
    elms_with_island = []
    if adjacency is not None and connectivity is not None:
        raise ValueError(f"Provide either neighbors or connectivity, not both.")
    if adjacency is None and connectivity is None:
        raise ValueError(f"Provide either neighbors or connectivity")
    if adjacency is None:
        assert connectivity is not None
        adjacency = np.array([np.sum(np.isin(connectivity, elm), axis=1) for elm in connectivity])

    counter_not_visited = np.zeros(adjacency.shape[0])
    counter_visited = np.zeros(adjacency.shape[0])

    size_island = 0
    visited_elms = set()
    # go through elements and check for islands
    for elm_source in tqdm(range(adjacency.shape[0]), desc="Checking for islands."):
        if largest and elm_source in visited_elms:
            continue
        _, n_not_visited, visited = check_islands_for_single_elm(elm_source,
                                                                 adjacency=adjacency,
                                                                 island_crit=island_crit)

        # add stats for each element how often it has been visited
        elms_visited = [i for i, v in visited.items() if v]

        if not largest:
            counter_visited[elms_visited] += 1
            elms_not_visited = [i for i, v in visited.items() if not v]
            counter_not_visited[elms_not_visited] += 1
        else:
            visited_elms.update(elms_visited)
            if len(elms_visited) > size_island:
                elms_not_visited = [i for i, v in visited.items() if not v]
                size_island = len(elms_visited)
                visited_elms.update(elms_visited)
                counter_visited = np.zeros(adjacency.shape[0])
                counter_not_visited = np.zeros(adjacency.shape[0])
                counter_visited[elms_visited] += 1
                counter_not_visited[elms_not_visited] += 1

        # if an island is found add it to results list
        if n_not_visited:
            if verbose:
                print(f"\nElement {elm_source: >4}: {n_not_visited} 1-node-neighbors not visited. ")
            elms_with_island.append(elm_source)

    return elms_with_island, counter_visited, counter_not_visited


def find_island_elms(connectivity=None, adjacency=None, verbose=False, island_crit='edge', decision='cumulative'):
    """
    Searches for islands in a mesh and returns element indices of the smallest island.
    Island is defines as a set of elements, which share a single node and/or single edge with the rest of the mesh.

    Parameters
    ----------
    connectivity : np.ndarray, optional
        Connectivity ('node_number_list') starting with 0. Can be triangles or tetrahedra
        (n_elms, 3) or (n_elms_4).
    adjacency : np.ndparray, optional
        Adjenceny matrix (n_elm, n_elm). Weights are supposed to be number of shared nodes.
        Computed from neighbors if not provided.
    island_crit : int, optional, default: 'edge'
        How many nodes to define islands?
        'node' -> Elements connected via a single _node_ are defined as an island.
        'edge' -> Elements connected via a single _edge_ are defined as an island.
    decision : string, optional, default: cumulative
        'cumulative' -> Return all element indices that are not visited any times
        'smallest'   -> Return smallest island.
    verbose : bool, optional
        Print some verbosity information. Default: False

    Returns
    -------
        island : list of island-elms
    """
    if adjacency is not None and connectivity is not None:
        raise ValueError(f"Provide either neighbors or connectivity, not both.")
    if adjacency is None:
        assert connectivity is not None
        adjacency = np.array([np.sum(np.isin(connectivity, elm), axis=1) for elm in connectivity])

    all_islands, counter_visited, counter_not_visited = find_islands(connectivity, verbose=verbose,
                                                                     island_crit=island_crit)

    if decision == 'smallest':
        # find the size of the islands
        one_node_neighs = {k: np.where(adjacency[k] == island_crit)[0] for k in all_islands}

        visited, not_visited = {}, {}
        for island, one_node_neigh in one_node_neighs.items():

            # two counters
            n_visited_i, n_not_visited_i = 0, 0

            for island_i in one_node_neigh:
                n_visited, n_not_visited, _ = check_islands_for_single_elm(island_i, adjacency=adjacency,
                                                                           island_crit=island_crit + 1)
                n_visited_i += n_visited
                n_not_visited_i += n_not_visited
            visited[island] = n_visited_i
            not_visited[island] = n_not_visited_i

        # choose the smallest island and get all 2-neighbors
        smallest_island_idx = np.argmin(list(visited.values()))
        smallest_island = list(visited.keys())[smallest_island_idx]

        _, _, elm_idx_from_smalles_island = check_islands_for_single_elm(smallest_island, island_crit=island_crit + 1,
                                                                         adjacency=adjacency)

        if verbose:
            print(f"Island with {len(list(elm_idx_from_smalles_island.keys()))} elements found.")
        return list(elm_idx_from_smalles_island.keys())

    elif decision == 'cumulative':
        return np.argwhere(counter_not_visited > 0)
