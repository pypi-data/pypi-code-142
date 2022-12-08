import os
import trimesh
import warnings
import nibabel
import numpy as np
from tqdm import tqdm
from scipy.interpolate import griddata

import pynibs


def cell_data_to_point_data(tris, data_tris, nodes, method='nearest'):
    """
    A wrapper for scipy.interpolate.griddata to interpolate cell data to node data.

    Parameters
    ----------

    tris : np.ndarray
        element number list, (n_tri, 3)
    data_tris : np.ndarray
        data in tris, (n_tri x 3)
    nodes : np.ndarray
        nodes coordinates, (n_nodes, 3
    method: str, default: 'nearest'
        Which method to use for interpolation. Default uses NearestNDInterpolator

    Returns
    -------
    data_nodes : np.ndarray
        Data in nodes
    """
    elms_center = np.mean(nodes[tris], axis=1)
    return griddata(elms_center, data_tris, nodes, method)


def data_nodes2elements(data, con):
    """
    Transforms data in nodes to elements (triangles or tetrahedra)

    Parameters
    ----------
    data : np.ndarray of float
        (N_nodes, N_data)
        Data given in the nodes
    con : np.ndarray of int
        triangles: (N_elements, 3)
        tetrahedra: (N_elements, 4)
        Connectivity index list forming the elements

    Returns
    -------
    out : np.ndarray of float
        (N_elements, N_data)
        Data given in the element scenters
    """

    return np.average(data[con], axis=1)


def data_elements2nodes(data, con, precise=False):
    """
    Transforms data in elements (triangles or tetrahedra) to nodes.
    Data can be list of multiple data arrays.

    Parameters
    ----------
    data : np.ndarray of float or list of np.ndarray
        (N_elements, N_data)
        Data given in the elements (multiple datasets who fit to con may be passed in a list)
    con : np.ndarray of int
        triangles: (N_elements. 3)
        tetrahedra: (N_elements, 4)
        Connectivity index list forming the elements
    precise : bool, default: False
        Compute data transformation precisely but slow. Better for near-0 values.

    Returns
    -------
    out : np.ndarray of float or list of np.ndarray
        (N_nodes, N_data)
        Data in nodes
    """

    # check if single dataset or a list of multiple datasets is passed
    if type(data) is not list:
        single_array_input = True
        data = [data]
    else:
        single_array_input = False

    n_elements = data[0].shape[0]
    n_nodes = con.max() - con.min() + 1
    if con.min() != 0:
        warnings.warn("Node number list is not zero based")

    # built connectivity matrix
    if not precise:
        try:
            c = np.zeros([n_elements, n_nodes])

            for i in range(n_elements):
                c[i, (con[i])] = 1.0 / con.shape[1]

            # filter out NaN from dataset
            for i in range(len(data)):
                data[i][np.isnan(data[i])] = 0

            # determine inverse of node matrix
            cinv = np.linalg.pinv(c)
            # transform data from element center to element nodes
            data_in_nodes = [np.dot(cinv, d) for d in data]

            # if single array was provided, return array as well
            if single_array_input:
                data_in_nodes = np.array(data_in_nodes)

            return data_in_nodes

        except np.core._exceptions._ArrayMemoryError:
            warnings.warn("Cannot allocate enough RAM to do fast data->nodes conversion. "
                          "Falling back to (slow) iterative mapping.")
    data_in_nodes = []

    con_flat = con.flatten()
    n_dims = con.shape[1]

    for d in data:
        data_flat = np.repeat(d, n_dims)
        # data_nodes = np.zeros(n_nodes, )
        # for i in tqdm(range(n_nodes), desc="Mapping elements to node data"):
        # data_nodes[i] = d[np.argwhere(con == i)[:, 0]].mean()

        data_in_nodes.append(np.array([data_flat[con_flat == i].mean() for i in range(n_nodes)]))

    # if single array was provided, return array as well
    if single_array_input:
        data_in_nodes = np.array(data_in_nodes)
    return data_in_nodes


def project_on_scalp_hdf5(coords, mesh, scalp_tag=1005):
    """
    Find the node in the scalp closest to each coordinate

    Parameters
    -------
    coords: nx3 np.ndarray
        Vectors to be transformed
    mesh: str or pynibs.TetrahedraLinear
        Filename of mesh in .hdf5 format or Mesh structure
    scalp_tag: int (optional)
        Tag in the mesh where the scalp is to be set. Default: 1005

    Returns
    ------
    points_closest: nx3 np.ndarray
        coordinates projected scalp (closest skin points)
    """

    # read head mesh and extract skin surface
    if isinstance(mesh, str):
        mesh = pynibs.load_mesh_hdf5(mesh)

    if coords.ndim == 1:
        coords = coords[np.newaxis,]

    # crop to skin surface
    triangles_skin = mesh.triangles[mesh.triangles_regions == scalp_tag]
    point_idx_skin = np.unique(triangles_skin)
    points_skin = mesh.points[point_idx_skin]

    # find points with smalled euclidean distance
    points_closest = np.zeros(coords.shape)
    for i, c in enumerate(coords):
        points_closest[i,] = points_skin[np.argmin(np.linalg.norm(points_skin - c, axis=1)),]

    return points_closest


def project_on_scalp(coords, mesh, scalp_tag=1005):
    """
    Find the node in the scalp closest to each coordinate

    Parameters
    ----------
    coords: nx3 np.ndarray
        Vectors to be transformed
    mesh: pynibs.TetrahedraLinear or simnibs.msh.mesh_io.Msh
        Mesh structure in simnibs or pynibs format
    scalp_tag: int, optional, default: 1005
        Tag in the mesh where the scalp is to be set. Default: 1005

    Returns
    -------
    points_closest: np.ndarry
        (n, 3) coordinates projected scalp (closest skin points)
    """
    from simnibs.msh.transformations import project_on_scalp as project_on_scalp_msh
    from simnibs.msh.mesh_io import Msh

    if isinstance(mesh, pynibs.TetrahedraLinear):
        points_closest = project_on_scalp_hdf5(coords=coords, mesh=mesh, scalp_tag=scalp_tag)
    elif isinstance(mesh, Msh):
        points_closest = project_on_scalp_msh(coords=coords, mesh=mesh, scalp_tag=scalp_tag, distance=0.)
    else:
        raise ValueError(f"Unknown mesh type: {type(mesh)}.")

    return points_closest


def refine_surface(fn_surf, fn_surf_refined, center, radius, repair=True, remesh=True, verbose=True):
    """
    Refines surface (.stl) in spherical ROI an saves as .stl file.

    Parameters
    ----------
    fn_surf : str
        Input filename (.stl)
    fn_surf_refined : str
        Output filename (.stl)
    center : np.ndarray of float (3)
        Center of spherical ROI (x,y,z)
    radius : float
        Radius of ROI
    repair : bool, optional, default: True
        Repair surface mesh to ensure that it is watertight and forms a volume
    remesh : bool, optional, default:False
        Perform remeshing with meshfix (also removes possibly overlapping facets and intersections)
    verbose : bool, optional, default: True
        Print output messages
    Returns
    -------
    <file>: .stl file
    """
    radius_ = radius + 2
    refine = True

    while refine:
        if verbose:
            print(f"Loading {fn_surf} ...")
        # reading original .stl file
        wm = trimesh.load(fn_surf)

        tris = wm.faces
        tris_center = wm.triangles_center
        points = wm.vertices

        # Splitting elements by adding tris_center to points in ROI
        mask_roi = np.linalg.norm(tris_center - center, axis=1) < radius
        ele_idx_roi = np.where(np.linalg.norm(tris_center - center, axis=1) < radius)[0]
        points_refine = points
        tris_refine = tris

        if verbose:
            print(f"Splitting elements ...")

        for ele_idx in tqdm(ele_idx_roi):
            points_idx_ele = tris[ele_idx, :]
            p_0 = points[points_idx_ele[0], :]
            p_1 = points[points_idx_ele[1], :]
            p_2 = points[points_idx_ele[2], :]
            p_01 = p_0 + 0.5 * (p_1 - p_0)
            p_02 = p_0 + 0.5 * (p_2 - p_0)
            p_12 = p_1 + 0.5 * (p_2 - p_1)

            points_refine = np.vstack((points_refine, p_01, p_02, p_12))

            mask_roi = np.hstack((mask_roi, False, False, False, False))

            # add 6 new triangles
            p_0_idx = points_idx_ele[0]
            p_1_idx = points_idx_ele[1]
            p_2_idx = points_idx_ele[2]
            p_01_idx = points_refine.shape[0] - 3
            p_02_idx = points_refine.shape[0] - 2
            p_12_idx = points_refine.shape[0] - 1

            # adding 4 elements
            tris_refine = np.vstack((tris_refine, np.array([[p_0_idx, p_01_idx, p_02_idx],
                                                            [p_01_idx, p_1_idx, p_12_idx],
                                                            [p_02_idx, p_12_idx, p_2_idx],
                                                            [p_01_idx, p_12_idx, p_02_idx]])))

        ele_idx_del = []

        if radius != np.inf:
            if verbose:
                print(f"Adding triangles in surrounding elements ...")
            # add triangles in surrounding elements
            ele_sur_idx = np.where(np.logical_and(np.linalg.norm(tris_center - center, axis=1) < radius_,
                                                  np.linalg.norm(tris_center - center, axis=1) >= radius))[0]

            for ele_sur in tqdm(ele_sur_idx):
                points_idx_ele = tris[ele_sur, :]
                p_0 = points[points_idx_ele[0], :]
                p_1 = points[points_idx_ele[1], :]
                p_2 = points[points_idx_ele[2], :]
                p_01 = p_0 + 0.5 * (p_1 - p_0)
                p_02 = p_0 + 0.5 * (p_2 - p_0)
                p_12 = p_1 + 0.5 * (p_2 - p_1)

                p_0_idx = points_idx_ele[0]
                p_1_idx = points_idx_ele[1]
                p_2_idx = points_idx_ele[2]

                p_on_02 = False
                p_on_12 = False
                p_on_01 = False

                if (np.sum(p_01 == points_refine, axis=1) == 3).any():
                    p_on_01 = True

                if (np.sum(p_02 == points_refine, axis=1) == 3).any():
                    p_on_02 = True

                if (np.sum(p_12 == points_refine, axis=1) == 3).any():
                    p_on_12 = True

                # no edge with point
                if not p_on_01 and not p_on_02 and not p_on_12:
                    pass

                # one edge with point
                elif p_on_01 and not p_on_02 and not p_on_12:
                    ele_idx_del.append(ele_sur)
                    p_01_idx = np.where(np.sum(points_refine == p_01, axis=1) == 3)[0][0]
                    tris_refine = np.vstack((tris_refine, np.array([[p_0_idx, p_01_idx, p_2_idx],
                                                                    [p_01_idx, p_1_idx, p_2_idx]])))

                elif p_on_02 and not p_on_01 and not p_on_12:
                    ele_idx_del.append(ele_sur)
                    p_02_idx = np.where(np.sum(points_refine == p_02, axis=1) == 3)[0][0]
                    tris_refine = np.vstack((tris_refine, np.array([[p_0_idx, p_1_idx, p_02_idx],
                                                                    [p_02_idx, p_1_idx, p_2_idx]])))

                elif p_on_12 and not p_on_02 and not p_on_01:
                    ele_idx_del.append(ele_sur)
                    p_12_idx = np.where(np.sum(points_refine == p_12, axis=1) == 3)[0][0]
                    tris_refine = np.vstack((tris_refine, np.array([[p_0_idx, p_1_idx, p_12_idx],
                                                                    [p_0_idx, p_12_idx, p_2_idx]])))

                # 2 edges with points
                elif p_on_02 and p_on_12 and not p_on_01:
                    ele_idx_del.append(ele_sur)
                    p_12_idx = np.where(np.sum(points_refine == p_12, axis=1) == 3)[0][0]
                    p_02_idx = np.where(np.sum(points_refine == p_02, axis=1) == 3)[0][0]
                    tris_refine = np.vstack((tris_refine, np.array([[p_0_idx, p_1_idx, p_02_idx],
                                                                    [p_1_idx, p_12_idx, p_02_idx],
                                                                    [p_02_idx, p_12_idx, p_2_idx]])))

                elif p_on_02 and p_on_01 and not p_on_12:
                    ele_idx_del.append(ele_sur)
                    p_01_idx = np.where(np.sum(points_refine == p_01, axis=1) == 3)[0][0]
                    p_02_idx = np.where(np.sum(points_refine == p_02, axis=1) == 3)[0][0]
                    tris_refine = np.vstack((tris_refine, np.array([[p_0_idx, p_01_idx, p_02_idx],
                                                                    [p_01_idx, p_2_idx, p_02_idx],
                                                                    [p_01_idx, p_1_idx, p_2_idx]])))

                elif p_on_01 and p_on_12 and not p_on_02:
                    ele_idx_del.append(ele_sur)
                    p_01_idx = np.where(np.sum(points_refine == p_01, axis=1) == 3)[0][0]
                    p_12_idx = np.where(np.sum(points_refine == p_12, axis=1) == 3)[0][0]
                    tris_refine = np.vstack((tris_refine, np.array([[p_0_idx, p_01_idx, p_2_idx],
                                                                    [p_01_idx, p_12_idx, p_2_idx],
                                                                    [p_01_idx, p_1_idx, p_12_idx]])))

        if verbose:
            print("Deleting old triangles ...")

        # delete old triangles
        ele_idx_roi = np.where(mask_roi)[0]
        ele_idx_lst_del = ele_idx_del + list(ele_idx_roi)
        tris_refine = np.delete(tris_refine, ele_idx_lst_del, 0)

        points_refine = np.round_(points_refine, 5)

        # # delete duplicate points
        # p_added = points_refine[points.shape[0]:, :]
        #
        # point_idx_del = np.array([])
        # for i_p, p in tqdm(enumerate(p_added)):
        #
        #     p_idx = np.where(np.sum(p == points_refine, axis=1) == 3)[0]
        #
        #     if len(p_idx) > 1:
        #         if p_idx[1] not in point_idx_del:
        #             point_idx_del = np.hstack((point_idx_del, p_idx[1:]))
        #
        #             # loop over point_idx_del and replace with first point idx
        #             for p_d_idx in p_idx[1:]:
        #                 tris_refine[tris_refine == p_d_idx] = p_idx[0]
        #
        # point_idx_keep = [i for i in range(points_refine.shape[0]) if i not in point_idx_del]
        # point_idx_new = [i for i in range(len(point_idx_keep))]
        # points_refine = points_refine[point_idx_keep, :]
        #
        # # renumber
        # for p_idx_keep, p_idx_new in zip(point_idx_keep[points.shape[0]:], point_idx_new[points.shape[0]:]):
        #     tris_refine[tris_refine == p_idx_keep] = p_idx_new

        # create new trimesh
        mesh = trimesh.Trimesh(vertices=points_refine,
                               faces=tris_refine)

        if repair:
            if mesh.is_watertight:
                if verbose:
                    print(f"Surface is watertight ...")
                mesh_ok = True
            else:
                if verbose:
                    print(f"Surface is NOT watertight ... trying to repair mesh ... ")
                # repair mesh
                trimesh.repair.fill_holes(mesh)

                if mesh.is_watertight:
                    if verbose:
                        print(f"Surface repaired ...")
                    mesh_ok = True

                else:
                    mesh_ok = False
                    radius -= 1
                    radius_ = radius + 2

                    if verbose:
                        print(f"WARNING: Could not repair refined surface ... "
                              f"shrinking radius by 1 mm to {radius} mm")
        else:
            mesh_ok = True

        if mesh_ok:
            if verbose:
                print(f"Saving {fn_surf_refined} ...")
            mesh.export(fn_surf_refined, file_type='stl_ascii')

            if remesh:
                # remesh surface
                print(f"Remeshing {fn_surf_refined} ...")
                command = f"meshfix {fn_surf_refined} -a 2.0 -u 1 -q --shells 9 " \
                          f"--stl -o {fn_surf_refined}"
                os.popen(command).read()

            refine = False


def map_data_to_surface(datasets, points_datasets, con_datasets, fname_fsl_gm, fname_fsl_wm, fname_midlayer=None,
                        delta=0.5, input_data_in_center=True, return_data_in_center=True, data_substitute=-1):
    """
    Maps data from ROI of fsl surface (wm, gm, or midlayer) to given Freesurfer brain surface (wm, gm, inflated).

    Parameters
    ----------
    datasets : np.ndarray of float [N_points x N_data] or list of np.ndarray
        Data in nodes or center of triangles in ROI (specify this in "data_in_center")
    points_datasets : np.ndarray of float [N_points x 3] or list of np.ndarray
        Point coordinates (x,y,z) of ROI where data in datasets list is given, the points have to be a subset of the
        GM/WM surface (has to be provided for each dataset)
    con_datasets : np.ndarray of int [N_tri x 3] or list of np.ndarray
        Connectivity matrix of dataset points (has to be provided for each dataset)
    fname_fsl_gm : str or list of str or list of None
        Filename of pial surface fsl file(s) (one or two hemispheres)
        e.g. in mri2msh: .../fs_ID/surf/lh.pial
    fname_fsl_wm : str or list of str or list of None
        Filename of wm surface fsl file(s) (one or two hemispheres)
        e.g. in mri2msh: .../fs_ID/surf/lh.white
    fname_midlayer : str or list of str
        Filename of midlayer surface fsl file(s) (one or two hemispheres)
        e.g. in headreco: .../fs_ID/surf/lh.central
    delta : float
        Distance parameter where gm-wm surface was generated 0...1 (default: 0.5)
        0 -> WM surface
        1 -> GM surface
    input_data_in_center : bool
        Flag if data in datasets in given in triangle centers or in points (Default: True)
    return_data_in_center : bool
        Flag if data should be returned in nodes or in elements (Default: True)
    data_substitute : float
        Data substitute with this number for all points in the inflated brain, which do not belong to the given data set

    Returns
    -------
    data_mapped : np.ndarray of float [N_points_inf x N_data]
        Mapped data to target brain surface. In points or elements
    """

    if type(fname_fsl_gm) is not list:
        fname_fsl_gm = [fname_fsl_gm]

    if type(fname_fsl_wm) is not list:
        fname_fsl_wm = [fname_fsl_wm]

    if type(fname_midlayer) is not list:
        fname_midlayer = [fname_midlayer]

    if fname_midlayer[0] is None:
        # load all freesurfer surfaces of gm and wm (hemispheres) and create midlayer
        points_gm = []
        con_target = []
        points_wm = []
        con_idx = 0

        for f_gm, f_wm in zip(fname_fsl_gm, fname_fsl_wm):
            p_gm, c_tar = nibabel.freesurfer.read_geometry(f_gm)
            p_wm, _ = nibabel.freesurfer.read_geometry(f_wm)

            points_gm.append(p_gm)
            points_wm.append(p_wm)
            con_target.append(c_tar + con_idx)
            con_idx += np.max(c_tar) + 1  # c_tar.shape[0]

        points_gm = np.vstack(points_gm)
        points_wm = np.vstack(points_wm)
        con_target = np.vstack(con_target)

        # regenerate the gm-wm surface w/o cropping in order to find congruent points
        wm_gm_vector = points_gm - points_wm

        # determine wm-gm surface (midlayer)
        points = points_wm + wm_gm_vector * delta

    else:
        # load directly all freesurfer midlayer surfaces (hemispheres)
        points = []
        con_target = []
        con_idx = 0

        for f_mid in fname_midlayer:
            if f_mid.endswith('.gii'):
                img = nibabel.gifti.giftiio.read(f_mid)
                p_mid = img.agg_data('pointset')
                c_tar = img.agg_data('triangle')
            else:
                p_mid, c_tar = nibabel.freesurfer.read_geometry(f_mid)

            points.append(p_mid)
            con_target.append(c_tar + con_idx)
            con_idx += np.max(c_tar) + 1  # c_tar.shape[0]

        points = np.vstack(points)
        con_target = np.vstack(con_target)

    # check datasets
    if type(datasets) is not list:
        datasets = [datasets]

    for i in range(len(datasets)):
        if datasets[i].ndim == 1:
            datasets[i] = datasets[i][:, np.newaxis]
        elif datasets[i].shape[0] < datasets[i].shape[1]:
            raise Warning("Datasets #{} shape[0] dimension is smaller than shape[1] (less points than dataset"
                          "components). Input dimension should be [N_points x N_data] ")

    if type(points_datasets) is not list:
        points_datasets = [points_datasets]

    if type(con_datasets) is not list:
        con_datasets = [con_datasets]
    # check if all points and all con are the same (if so, just map once and reuse results)
    all_points_equal = all([(points_datasets[i] == points_datasets[i + 1]).all()
                            for i in range(len(points_datasets) - 1)])

    all_con_equal = all([(con_datasets[i] == con_datasets[i + 1]).all()
                         for i in range(len(con_datasets) - 1)])

    if all_points_equal and all_con_equal:
        n_main_iter = 1
        n_sub_iter = len(datasets)
    else:
        n_main_iter = len(datasets)
        n_sub_iter = 1

    # check if indexation starts with value greater zero
    if np.min(con_target) > 0:
        con_target = con_target - np.min(con_target)

    n_points = points.shape[0]

    data_mapped = []

    # for i, data in enumerate(datasets):
    for i in range(n_main_iter):
        n_data = datasets[i].shape[1] if datasets[i].ndim > 1 else 1

        n_points_cropped = points_datasets[i].shape[0]

        # check if indexation starts with value greater zero
        if np.min(con_datasets[i]) > 0:
            con_datasets[i] = con_datasets[i] - np.min(con_datasets[i])

        if datasets[i].ndim == 1:
            datasets[i] = datasets[i][:, np.newaxis]

        if input_data_in_center and return_data_in_center:
            # determine triangle center of dataset
            triangle_center_datasets = np.average(points_datasets[i][con_datasets[i]], axis=1)

            # determine triangle center of whole surface
            triangle_center_surface = np.average(points[con_target], axis=1)

            # loop over all points to get index list
            point_idx_target = []
            point_idx_data = []

            point_idx_target = np.zeros(datasets[i].shape[0])
            point_idx_data = np.arange(datasets[i].shape[0])
            for j in tqdm(range(datasets[i].shape[0]), desc="Mapping ROI to surface"):
                point_idx_target[j] = np.where(np.all(np.isclose(triangle_center_datasets[j,], triangle_center_surface),
                                                      axis=1))[0]
            point_idx_target = point_idx_target.astype(int).tolist()
            point_idx_data = point_idx_data.astype(int).tolist()

            # run subiterations (if all points and cons are equal, we save a lot of time here)
            for k in range(n_sub_iter):
                data_mapped.append(np.zeros([triangle_center_surface.shape[0], n_data]) + data_substitute * 1.0)
                data_mapped[k][point_idx_target, :] = datasets[k][point_idx_data, :]

        else:
            # loop over all points to get index list
            point_idx_target = []
            point_idx_data = list(range(datasets[i].shape[0]))

            for j in range(datasets[i].shape[0]):
                point_idx_target.append(np.where(np.all(np.isclose(points_datasets[i][j,], points), axis=1))[0])

            point_idx_target = [int(p) for p in point_idx_target]
            point_idx_data = [int(p) for p in point_idx_data]

            # run subiterations (if all points and cons are equal, we save a lot of time here)
            for k in range(n_sub_iter):
                # transform data from triangle center to triangle nodes if necessary
                if input_data_in_center:
                    data_nodes = data_elements2nodes(datasets[k], con_datasets[k])
                else:
                    data_nodes = datasets[k]

                # find and map data points
                data_mapped.append(np.zeros([n_points, n_data]) + data_substitute * 1.0)
                data_mapped[k][point_idx_target] = data_nodes[point_idx_data]

                # return data in elements instead of points
                if return_data_in_center:
                    data_mapped[k] = data_nodes2elements(data_mapped[k], con_target)

    return data_mapped


def midlayer_2_surf(midlayer_data, coords_target, coords_midlayer, midlayer_con=None, midlayer_data_in_nodes=False, max_dist=5,
                    outside_roi_val=0, precise_map=True):
    """
    Convert midlayer data to whole-brain surface data, e.g. grey matter.
    Output is returned as data in nodes.

    Parameters
    ----------
    midlayer_data : np.ndarray of float
        (n_elm_midlayer,) or (n_nodes_midlayer,), the data in the midlayer.
    coords_target : np.ndarray of float
        (n_nodes_target, 3) Coordinates of the nodes of the target surface.
    coords_midlayer : np.ndarray of float
        (n_nodes_midlayer, 3) Coordinates of the nodes of the midlayer surface.
    midlayer_con : np.ndarray of int, optional
        (n_elm_midlayer, 3) Connectivity of the midlayer elements. Provide if data_in_points == True.
    midlayer_data_in_nodes : bool, default=False
        If midlayer data is provided in nodes, set to True and provide midlayer_con.
    max_dist : float, default=5
        Maximum distance between target and midlayer nodes to pull data from midlayer_data for.
    outside_roi_val : float, default=0
        Areas outside of max_dist are filled with outside_roi_val.
    precise_map : bool, default=True
        If elements to nodes mapping is done, perform this precise and slow or not.

    Returns:
    --------
    data_target : np.ndarray
        (n_nodes_target, 1) The data in nodes of the target surface.
    """
    if not midlayer_data_in_nodes:
        assert midlayer_con is not None
        midlayer_data = np.squeeze(pynibs.data_elements2nodes(midlayer_data, midlayer_con, precise=precise_map))

    data_target = np.zeros((coords_target.shape[0]))
    for i in tqdm(range(data_target.shape[0]), desc='Mapping midlayer2surface'):
        idx = np.linalg.norm(coords_target[i] - coords_midlayer, axis=1).argmin()
        if np.linalg.norm(coords_target[i] - coords_midlayer[idx]) > max_dist:
            data_target[i] = outside_roi_val
        else:
            data_target[i] = midlayer_data[idx]

    return data_target
