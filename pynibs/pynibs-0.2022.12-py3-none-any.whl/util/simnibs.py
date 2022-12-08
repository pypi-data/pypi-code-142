import gc
import re
import copy
import trimesh
import simnibs
import warnings
import collections
import numpy as np

import pynibs


def e_field_gradient_between_wm_gm(
        roi_surf,
        mesh,
        gm_nodes,
        wm_nodes,
        gm_center_distance,
        wm_center_distance
):
    """
    Compute local the E-field gradient at the ROI nodes between the gray and white matter boundary sufaces.
    Adapted from neuronibs/cortical_layer.py/add_e_field_gradient_between_wm_gm_field

    Parameters
    ----------
    roi_surf : simnibs.Msh
        The surface object representing the ROI.
    volumetric_mesh: simnibs.Msh
        The (volumetric) head mesh.

    Returns
    -------
    e_field_gradient_per_mm : simnibs.mesh.mesh_io.ElementData
        The E-field gradient from the GM to the WM surface normalized to 1 mm with respect to the gray matter thickness.
        per ROI node
    """
    #roi_nodes = roi_surf.nodes.node_coord
    roi_centers = roi_surf.elements_baricenters().value

    # concatenate the point lists to avoid re-building the (simnibs-internal) data structures
    # for interpolation upon consecutive calls
    to_be_interpolated = np.concatenate((gm_nodes, roi_centers, wm_nodes))
    try:
        interpolated = mesh.field['magnE'].interpolate_scattered( to_be_interpolated )
    except KeyError:
        magE = mesh.field['E'].norm()
        interpolated = magE.interpolate_scattered( to_be_interpolated )

    num_nodes = gm_nodes.shape[0]
    num_nodes_x2 = num_nodes*2
    num_nodes_x3 = num_nodes*3
    e_field_gm = interpolated[:num_nodes]
    e_field_center = interpolated[num_nodes:num_nodes_x2]
    e_field_wm = interpolated[num_nodes_x2:num_nodes_x3]

    e_field_gradient = e_field_gm - e_field_wm
    gray_matter_thickness = gm_center_distance + wm_center_distance
    #distance_offset = gm_distance / gray_matter_thickness      # = Midlayer offset, may be needed later (?)
    e_field_gradient_per_mm = e_field_gradient / gray_matter_thickness
    relative_e_field_gradient_per_mm = e_field_gradient_per_mm / e_field_center * 100

    return simnibs.ElementData(relative_e_field_gradient_per_mm, name='rel_gradient_per_mm', mesh=roi_surf)


def e_field_angle_theta(surface, mesh):
    """
     Compute angle between local the E-field vector and surface vector at the ROI nodes.

     Parameters
     ----------
     surface : simnibs.Msh
         The surface object representing the ROI.
     mesh: simnibs.Msh
         The (volumetric) head mesh.

     Returns
     -------
     theta : simnibs.mesh.mesh_io.ElementData
         The angle between local the E-field vector and surface vector for each surface element of the ROI.
     """
    layer_centers = surface.elements_baricenters().value
    interpolated_cell_centers = mesh.field['E'].interpolate_scattered(layer_centers, out_fill='nearest')
    tri_normal = surface.triangle_normals(smooth=30).value
    e_at_roi_cell_centers_normalized = np.divide(
        interpolated_cell_centers,
        np.linalg.norm(interpolated_cell_centers, axis=1)[:, np.newaxis]
    )
    angle = np.array([np.arccos(np.dot(a, b)) / np.pi * 180 for a, b in
                      zip(tri_normal, e_at_roi_cell_centers_normalized)])

    return simnibs.ElementData(angle, name="theta", mesh=surface)


def precompute_geo_info_for_layer_field_interpolation(simnibs_mesh, roi):
    """
    Precomputes geometric properties of the corresponding GM and WM nodes
    in the 'simnibs_mesh' of each node of each layer in 'roi'.
    > The corresponding point on the GM and WM surface to each vertex of te ROI surface
      are determined (by raycasting and nearest neighbour search as fallback)
      (interpolation will take place between these nodes)
    > The nodes are moved inside the gray matter by 20 % of their total distance from the GM/WM
      boundary to the midlayer.
    > The distance of the relocated GM and WM nodes to the ROI nodes is determined (required to
      computed the gradient per mm).

     Parameters
     ----------
     simnibs_mesh : simnibs.Msh
         The head model volume mesh.
     roi: pynibs.roi.RegionOfInterestSurface
         The ROI object containing the layers.

     Returns
     -------
     layer_gm_wm_info : dict[str, dict[str,np.ndarray]]
        For each layer defined in the mesh (outer dict key: layer_id),
        provide pre-computed geometrical information as a dictionary (outer dict value):
        - key: gm_nodes
          For each layer node, the corresponding point on the GM surface.
        - key: wm_nodes
          For each layer node, the corresponding point on the WM surface.
        - key: gm_center_distance
          The distance between the layer nodes and the corresponding points on the GM.
        - key: wm_center_distance
          The distance between the layer nodes and the corresponding points on the WM.
    """
    WHITE_MATTER_SURFACE_LABEL = 1001
    GRAY_MATTER_SURFACE_LABEL = 1002

    import vtk
    def make_vtkpolydata( pts, tris ):
        # prepare vertices
        pts_vtk = vtk.vtkPoints()
        pts_vtk.SetNumberOfPoints(pts.shape[0])
        for i in range(pts.shape[0]):
            pts_vtk.SetPoint(i, pts[i][0], pts[i][1], pts[i][2])

        # prepare triangles
        tris_vtk = vtk.vtkCellArray()
        for tri in tris:
            tris_vtk.InsertNextCell(3)
            for v in tri:
                tris_vtk.InsertCellPoint( v )

        # prepare GM polygonal surface
        surf_vtk = vtk.vtkPolyData()
        surf_vtk.SetPoints(pts_vtk)
        surf_vtk.SetPolys(tris_vtk)

        return surf_vtk

    gray_matter_surface = simnibs_mesh.crop_mesh(GRAY_MATTER_SURFACE_LABEL)
    white_matter_surface = simnibs_mesh.crop_mesh(WHITE_MATTER_SURFACE_LABEL)

    gm_nodes = gray_matter_surface.nodes.node_coord
    gm_tris = gray_matter_surface.elm.node_number_list
    wm_nodes = white_matter_surface.nodes.node_coord
    wm_tris = white_matter_surface.elm.node_number_list

    # for each point on the layer find corresponding points on the GM/WM surfaces
    # using the VTK implementation of Raycasting
                                        # make zero indexed and shape (n,3) instead of (n,4), with -1 in the 4th column
    gm_surf_vtk = make_vtkpolydata(gm_nodes, gm_tris[:,:3] - 1)
    wm_surf_vtk = make_vtkpolydata(wm_nodes, wm_tris[:,:3] - 1)

    gm_intersector = vtk.vtkOBBTree()
    gm_intersector.SetDataSet(gm_surf_vtk)
    gm_intersector.BuildLocator()

    wm_intersector = vtk.vtkOBBTree()
    wm_intersector.SetDataSet(wm_surf_vtk)
    wm_intersector.BuildLocator()

    intersectors = [gm_intersector, wm_intersector]
    normal_sign  = [1,-1]

    layer_gm_wm_info = dict()
    for layer_idx in range(len(roi.layers)):
        intersec_pts = [[], []]
        layer_id      = roi.layers[layer_idx].id
        layer_surf    = roi.layers[layer_idx].surface
        layer_centers = layer_surf.elements_baricenters().value
        layer_normals = roi.layers[layer_idx].get_smoothed_normals()

        for pt,normal in zip(layer_centers, layer_normals):
            for idx in range(len(intersectors)):
                intersection_pts = vtk.vtkPoints()
                intersected_tris = vtk.vtkIdList()

                intersector = intersectors[idx]

                intersector.IntersectWithLine(pt, normal_sign[idx]*100*normal+pt, intersection_pts, intersected_tris)
                if intersection_pts.GetNumberOfPoints() > 0:
                    intersec_pts[idx].append(intersection_pts.GetPoint(0))
                else:
                    intersec_pts[idx].append([np.iinfo(np.uint16).max]*3)

        gm_intersec_pts = np.array(intersec_pts[0])
        wm_intersec_pts = np.array(intersec_pts[1])

        # Check the distances of the found points on the GM/WM surface to the layer nodes.
        # If the distance is too high, raycasting failed (e.g. no intersection found or too far away).
        # In this case, we determine the nearest neighbor for these nodes.
        layer_gm_distance = np.linalg.norm(layer_centers - gm_intersec_pts, ord=2, axis=1)
        layer_wm_distance = np.linalg.norm(layer_centers - wm_intersec_pts, ord=2, axis=1)

        # TODO: consider using a relative distance depending on the local GM thickness
        raycast_error_nodes_gm = np.argwhere(layer_gm_distance > 2)  # mm
        raycast_error_nodes_wm = np.argwhere(layer_wm_distance > 2)  # mm

        closest_gm_nodes, _ = gray_matter_surface.nodes.find_closest_node(layer_centers[raycast_error_nodes_gm], return_index=True)
        closest_wm_nodes, _ = white_matter_surface.nodes.find_closest_node(layer_centers[raycast_error_nodes_wm], return_index=True)

        gm_intersec_pts[raycast_error_nodes_gm] = closest_gm_nodes
        wm_intersec_pts[raycast_error_nodes_wm] = closest_wm_nodes

        layer_gm_distance = np.linalg.norm(layer_centers - gm_intersec_pts, ord=2, axis=1)
        layer_wm_distance = np.linalg.norm(layer_centers - wm_intersec_pts, ord=2, axis=1)

        center_to_gm_vecs = gm_intersec_pts - layer_centers
        center_to_wm_vecs = wm_intersec_pts - layer_centers

        associated_gray_matter_points = gm_intersec_pts - \
                                        np.multiply( # multiply unit-normals by individual gm thickness, then scale to 20%
                                            center_to_gm_vecs,
                                            layer_gm_distance[:, np.newaxis]
                                        ) * 0.1
        associated_white_matter_points = wm_intersec_pts - \
                                         np.multiply( # multiply unit-normals by individual wm thickness, then scale to 20%
                                             center_to_wm_vecs,
                                             layer_wm_distance[:, np.newaxis]
                                         ) * 0.1

        layer_gm_wm_info[layer_id] = {
            "assoc_gm_points" : associated_gray_matter_points,
            "assoc_wm_points" : associated_white_matter_points,
            "layer_gm_dist" : layer_gm_distance,
            "layer_wm_dist" : layer_wm_distance
        }

    return layer_gm_wm_info


def calc_e_in_midlayer_roi(
    phi_dadt,
    roi,
    subject,
    phi_scaling=1.,
    mesh_idx=0,
    mesh=None,
    roi_hem='lh',
    depth=.5,
    qoi=None,
    layer_gm_wm_info=None
):
    """
    This is to be called by Simnibs as postprocessing function per FEM solve.

    Parameters
    ----------
    phi_dadt : (array-like, elmdata)
    roi : pynibs.roi.RegionOfInterestSurface()
    subject : pynibs.subject.Subject()
    phi_scaling : float
    mesh_idx : int
    mesh : simnibs.msh.Mesh()
    roi_hem : 'lh'
    depth : float
    qoi : list of str
        List of identifiers of the to-be calculated quantities of interest.
    layer_gm_wm_info : dict[str, dict[str,np.ndarray]]
        For each layer defined in the mesh (outer dict key: layer_id),
        provide pre-computed geometrical information as a dictionary (outer dict value):
        - key: gm_nodes
          For each layer node, the corresponding point on the GM surface.
        - key: wm_nodes
          For each layer node, the corresponding point on the WM surface.
        - key: gm_center_distance
          The distance between the layer nodes and the corresponding points on the GM.
        - key: wm_center_distance
          The distance between the layer nodes and the corresponding points on the WM.

    Returns
    -------
    (roi.n_tris,4) : np.vstack((e_mag, e_norm, e_tan, e_angle)).transpose() for the midlayer
    (len(roi.layers)x(roi.layers[idx].surface.n_tris,4)) : np.vstack((e_mag, e_norm, e_tan, e_angle)).transpose()
    """
    if depth != .5:
        raise NotImplementedError(f"depth={depth} != 0.5 not implemented")

    import simnibs.simulation.fem as fem
    # mesh_folder = subject.mesh[mesh_idx]["mesh_folder"]

    # set default return quantities
    if qoi is None:
        qoi = ['E', 'mag', 'norm', 'tan', 'angle']
    qois_midlayer = copy.copy(qoi)
    ret_arr_num_components = len(qoi)
    # special care for E
    if 'E' in qoi:
        ret_arr_num_components += 2         # E is a 3D quantity whose components are stored individually
        qois_midlayer.remove('E')  # we don't need this to be computed, it already is

    qois_layers = []            # the QOIs computed for the cortical layers (not midlayer)
    max_num_elmts = roi.n_tris  # number of midlayer elements to define the shape of the output data structure
    interpolation_surfaces = {  # initialize the ROI surfaces the QOIs will be interpolated onto
        "midlayer" : simnibs.Msh(
            nodes=simnibs.Nodes(node_coord=roi.node_coord_mid),
            elements=simnibs.Elements(triangles=roi.node_number_list + 1)
        )
    }
    # check if interpolation must be done for the cortical layers and initialize accordingly
    if len(roi.layers) > 0 and layer_gm_wm_info is not None:
        if len(layer_gm_wm_info.keys()) == len(roi.layers):
            qois_layers = ['mag', 'theta', 'gradient'] # = parameters of the neuronal meanfield model

            for layer in roi.layers:
                # Do the cortical layers have more elements than the midlayer?
                max_num_elmts = np.max((max_num_elmts, layer.surface.elm.node_number_list.shape[0]))
                # Expand shape of output data structure by the number of QOIs computed for this layer
                ret_arr_num_components += len(qois_layers)
                # Add this layer to the interpolation surfaces.
                interpolation_surfaces[layer.id] = layer.surface
        else:
            print("[calc_e_in_midlayer] Computation of parameters for neuronal meanfield model was requested,"
                  "but number of layer information in 'layer_gm_wm_info' does not match the number of layers"
                  "found in the mesh. Skipping computation of neuronal model parameters...")

    # simnibs calls this with empty data so find out about the results dimensions
    if isinstance(phi_dadt, tuple):
        # SimNIBS 4 includes 'phi/v' last in the tuple of the to-be computed fields
        phi = phi_dadt[-1] * phi_scaling
        # dadt = phi_dadt[1].elm_data2node_data().value
    else:
        return np.zeros((max_num_elmts, ret_arr_num_components))

    # prepare mesh_local
    mesh_local = copy.deepcopy(mesh)

    # write phi and dAdt in msh
    # dadt = mesh_io.NodeData(dadt, name='D', mesh=mesh_local)
    try:
        dadt = phi_dadt[0].value
    except AttributeError:
        dadt = phi_dadt[0]
    dadt = simnibs.ElementData(dadt, name='D', mesh=mesh_local)
    phi = simnibs.NodeData(phi.flatten(), name='v', mesh=mesh_local)

    mesh_local = fem.calc_fields(phi, "vDEe", cond=None, dadt=dadt)

    # get folder names and such
    # m2m_folder = os.path.join(mesh_folder, "m2m_" + subject.id)
    # m2m_folder = os.path.abspath(os.path.normpath(m2m_folder))

    # if v_simnibs == 3:
    #     names, segtype = get_surface_names_from_folder_structure(m2m_folder)
    #     # middle_surf = {}
    #
    #     # get midlayer
    #     if segtype == 'mri2mesh':
    #         # for hemi in ['lh', 'rh']:
    #         wm_surface = mesh_io.read_freesurfer_surface(names[roi_hem + '_wm'])
    #         gm_surface = mesh_io.read_freesurfer_surface(names[roi_hem + '_gm'])
    #         # middle_surf = mesh_io._middle_surface(wm_surface, gm_surface, depth)
    #     elif segtype == 'headreco':
    #         pass
    #         # for hemi in ['lh', 'rh']:
    #         # middle_surf = mesh_io.read_gifti_surface(names[roi_hem + '_midgm'])
    #     else:
    #         raise NotImplementedError(f"segtype {segtype} unknown.")

    # calc QOIs
    data = mesh_local.field['E']
    data = data.as_nodedata()
    interp_res_per_surface = dict()

    for id, surface in interpolation_surfaces.items():
        interpolated = data.interpolate_to_surface(surface)
        qois_calculated = collections.OrderedDict() # maintain order of calculation with OrderedDict

        if id == "midlayer":
            qois_to_calc = qois_midlayer
            # E is the result of the FEM; all other quantities are secondary QOIs computed from E
            if 'E' in qoi:
                qois_calculated['E'] = interpolated.value
                qois_calculated['E'] = pynibs.data_nodes2elements(data=qois_calculated['E'],
                                                                  con=(surface.elm.node_number_list - 1))
        elif id != "midlayer" and len(qois_layers) > 0:
            qois_to_calc = qois_layers
        else:
            continue

        for quant in qois_to_calc:
            if quant == 'mag':
                qois_calculated[quant] = interpolated.norm().value
            elif quant == 'norm':
                qois_calculated[quant] = interpolated.normal().value
                qois_calculated[quant] *= -1
            elif quant == 'tan':
                qois_calculated[quant] = interpolated.tangent().value
            elif quant == 'angle':
                qois_calculated[quant] = interpolated.angle().value
            elif quant == 'theta':  # basically 'angle' but we want it in degrees for the meanfield model
                qois_calculated[quant] = e_field_angle_theta(surface, mesh_local).value
            elif quant == 'gradient':
                qois_calculated[quant] = e_field_gradient_between_wm_gm(
                    surface,
                    mesh_local,
                    layer_gm_wm_info[id]["assoc_gm_points"],
                    layer_gm_wm_info[id]["assoc_wm_points"],
                    layer_gm_wm_info[id]["layer_gm_dist"],
                    layer_gm_wm_info[id]["layer_wm_dist"],
                ).value
            else:
                raise ValueError('Invalid quantity: {0}'.format(quant))

            # pos-processing of the QOIs
            # - transform point data to element data, theta and gradient already are element data.
            if quant not in ["theta", "gradient"]:
                qois_calculated[quant] = pynibs.data_nodes2elements(data=qois_calculated[quant],
                                                                    con=(surface.elm.node_number_list-1))

            # - wrap 1D data in array
            try:
                if qois_calculated[quant].ndim == 1:
                    qois_calculated[quant] = qois_calculated[quant][:, np.newaxis]
            except KeyError:
                pass

        # OrderedDict has maintained the order of the QOI-list.
        interp_res_per_surface[id] = [*qois_calculated.values()]

    del qois_calculated, surface, interpolated, mesh_local, phi, mesh, data
    gc.collect()

    # 0-pad midlayer & layer data to have the same number of columns (hstack not possible otherwise),
    # according to the layer with the highest number of elements.
    for id in interp_res_per_surface.keys():
        num_values_to_be_padded = max_num_elmts  - interp_res_per_surface[id][0].shape[0]
        for q in range(len(interp_res_per_surface[id])):
            interp_res_per_surface[id][q] = np.pad(interp_res_per_surface[id][q], ((0,num_values_to_be_padded),(0,0)))

    # Stack all result fields column-wise; each column = 1-result array (or in case of E, a component of E)
    # For midlayer + 5 layers, there will be 21 columns and max_num_elements rows
    # 21 = midlayer(3x for E, 1x each for magE, tanE, normE) + 3*layer(1x each for magE, theta, gradient)
    return np.hstack([np.hstack(surf_data) for surf_data in interp_res_per_surface.values()])


def read_coil_geo(fn_coil_geo):
    """
    Reads a coil .geo file.

    Parameters
    ----------
    fn_coil_geo : str
        Filename of .geo file created from SimNIBS containing the dipole information

    Returns
    -------
    dipole_pos : np.ndarray of float
    (n_dip, 3) Dipole positions ``(x, y, z)``.
    dipole_mag : np.ndarray of float
    (n_dip, 1) Dipole magnitude.
    """
    regex = r"SP\((.*?)\)\{(.*?)\}"
    with open(fn_coil_geo, 'r') as file:
        dipole_pos = []
        dipole_mag = []
        while file:
            te = file.readline()

            if te == "":
                break

            try:
                pos, mag = re.findall(regex, te)[0]
                pos = [float(x) for x in pos.split(',')]
                mag = float(mag)
                dipole_pos.append(pos)
                dipole_mag.append(mag)
            except IndexError:
                pass

        dipole_pos = np.vstack(dipole_pos)
        dipole_mag = np.array(dipole_mag)[:, np.newaxis]

    return dipole_pos, dipole_mag


def check_mesh(mesh, verbose=False):
    """
    Check a simmibs.Mesh for degenerated elements:
        * zero surface triangles
        * zerso volume tetrahedra
        * negative volume tetrahedra

    Parameters
    ----------
    mesh : str or simnibs.Mesh

    Other parameters
    ----------------
    verbose : book, default: False
        Print some verbosity messages.

    Returns
    -------
    zero_tris : np.ndarray
        Element indices for zero surface tris (0-indexed)
    zero_tets : np.ndarray
        Element indices for zero volume tets (0-indexed)
    neg_tets : np.ndarray
        Element indicies for negative volume tets (0-indexed)
    """
    if isinstance(mesh, str):
        mesh = simnibs.read_msh(mesh)
    tris = mesh.elm.node_number_list[mesh.elm.triangles - 1][:, :3]
    points_tri = mesh.nodes[tris]
    tri_area = pynibs.calc_tri_surface(points_tri)
    zero_tris = np.argwhere(np.isclose(tri_area, 0, atol=1e-13))
    if verbose:
        print(f"{len(zero_tris)} zero surface triangles found.")

    tets = mesh.elm.node_number_list[mesh.elm.tetrahedra - 1]
    points_tets = mesh.nodes[tets]
    tets_volume = pynibs.calc_tet_volume(points_tets)
    zero_tets = np.argwhere(np.isclose(tets_volume, 0, atol=1e-13))
    if verbose:
        print(f"{len(zero_tets)} zero volume tetrahedra found.")

    tet_idx = mesh.elm.node_number_list[mesh.elm.tetrahedra - 1]
    vol = pynibs.calc_tet_volume(mesh.nodes.node_coord[tet_idx - 1], abs=False)
    neg_idx = np.argwhere(vol > 0)
    if verbose:
        print(f"{len(neg_idx)} negative tets found.")
    neg_idx_in_full_arr = mesh.elm.tetrahedra[neg_idx] - 1

    return zero_tris, zero_tets + len(mesh.elm.triangles), neg_idx_in_full_arr


def fix_mesh(mesh, verbose=False):
    """
    Fixes simnibs.Mesh by removing any zero surface tris and zero volume tets and by fixing negative volume tets.

    Parameters
    ----------
    mesh : str or simnibs.Mesh
        Filename of mesh or mesh object.

    Other parameters
    ----------------
    verbose : bool, default: False
        Print some verbosity messages.

    Returns
    -------
    fixed_mesh : simnibs.Mesh
    """
    if isinstance(mesh, str):
        mesh = simnibs.read_msh(mesh)

    zero_tris, zero_tets, neg_tets = check_mesh(mesh, verbose=verbose)

    if neg_tets.size:
        mesh.elm.node_number_list[neg_tets, [0, 1, 2, 3]] = mesh.elm.node_number_list[neg_tets, [0, 1, 3, 2]]

    if zero_tris.size:
        mesh = mesh.remove_from_mesh(elements=zero_tris + 1)

    if zero_tets.size:
        mesh = mesh.remove_from_mesh(elements=zero_tets + 1 - zero_tris.size)

    # check again
    zero_tris, zero_tets, neg_tets = check_mesh(mesh)

    if zero_tris.size or zero_tets.size or neg_tets.size:
        warnings.warn(f"Couldn't fix mesh: zero_tris: "
                      f"{zero_tris.size} zero tris, {zero_tets.size} zero_tets, {neg_tets.size} neg_tets left over.")

    return mesh


def smooth_mesh(mesh, output_fn, smooth=.8, approach='taubin', skin_only_output=False, smooth_tissue='skin'):
    """
    Smoothes the skin compartment of a simnibs mesh. Uses one of three trimesh.smoothing approaches.
    Because tetrahedra and triangle share the same nodes, this also smoothes the volume domain.

    Parameters
    ----------
    mesh : str or simnibs.Mesh
    output_fn : str
    smooth : float, default: 0.8
        Smoothing aggressiveness. [0, ..., 1]
    approach: str, default: 'taubin'
        Which smoothing approach to use. One of ('taubin', laplacian', 'humphrey)
    smooth_tissue : str or list of int, default: 'skin'
        Which tissue type to smooth. E.g. 'gm' or [2, 1002].

    Other parameters
    ----------------
    skin_only_output : bool, default: True
        If true, a skin only mesh is written out instead of the full mesh.

    Returns
    -------
    <file> : The smoothed mesh.


    .. figure:: ../../doc/images/smooth_mesh.png
       :scale: 50 %
       :alt: Original and smoothed surfaces and volumes.

       Left: original, spiky mesh. Right: smoothed mesh.
    """
    if isinstance(mesh, str):
        mesh = simnibs.mesh_io.read_msh(mesh)

    # only triangles
    mesh_cropped = mesh.crop_mesh(elm_type=2)
    if smooth_tissue == 'skin':
        smooth_tissue = [5, 1005]
    elif smooth_tissue == 'gm':
        smooth_tissue = [2, 1002]
    elif smooth_tissue == 'wm':
        smooth_tissue = [1, 1001]
    elif type(smooth_tissue) == str:
        raise ValueError(f"Don't know smooth_tissue='{smooth_tissue}'.")

    # only triangles + only specific tissue type
    mesh_cropped = mesh_cropped.crop_mesh(smooth_tissue)

    # simnibs node indexing is 1-based
    tri_node_nr = mesh_cropped.elm.node_number_list[mesh_cropped.elm.triangles - 1] - 1
    tri_node_nr = tri_node_nr[:, :3]  # triangles only have 3 dimensions

    assert output_fn.endswith('.msh'), f"Wrong file suffix: {output_fn}. Use .msh"
    assert 0 <= smooth <= 1, f"'smooth={smooth}' parameter must be within  [0,1]. "

    # create a Trimesh object based on the skin tris
    mesh_trimesh = trimesh.Trimesh(vertices=mesh_cropped.nodes.node_coord,
                                   faces=tri_node_nr,
                                   process=False)  # process=False keeps original ordering
    if approach == 'taubin':
        smoothed_mesh = trimesh.smoothing.filter_taubin(mesh_trimesh.copy(), lamb=smooth)  # do smoothing
    elif approach == 'laplacian':
        smoothed_mesh = trimesh.smoothing.filter_laplacian(mesh_trimesh.copy(), lamb=smooth)  # do smoothing
    elif approach == 'humphrey':
        smoothed_mesh = trimesh.smoothing.filter_humphrey(mesh_trimesh.copy(), alpha=smooth)  # do smoothing
    else:
        raise NotImplementedError(f"Approach {approach} not implemented. Use 'taubin', laplacian', or 'humphrey'.")

    # find indices of nodes in original mesh
    ind_nodes = np.in1d(mesh.nodes.node_coord[:, 0], mesh_cropped.nodes.node_coord[:, 0]) + \
                np.in1d(mesh.nodes.node_coord[:, 1], mesh_cropped.nodes.node_coord[:, 1]) + \
                np.in1d(mesh.nodes.node_coord[:, 2], mesh_cropped.nodes.node_coord[:, 2])
    ind_nodes = np.where(ind_nodes)[0]

    # This doesn't work if several nodes are at the same location
    if ind_nodes.shape[0] != mesh_cropped.nodes.node_coord.shape[0]:
        # probably some duplicate nodes
        if mesh_cropped.nodes.node_coord.shape[0] != np.unique(mesh_cropped.nodes.node_coord, axis=0).shape[0]:
            # Some other problem
            raise ValueError("Duplicate nodes found in cropped mesh.")

        # Find the duplicate notes in mesh and remove from ind_nodes list
        unique_elms, dup_elms = np.unique(mesh.nodes.node_coord, axis=0, return_counts=True)
        assert unique_elms.shape[0] == dup_elms.shape[0]

        # go over nodes that have been found twice
        for dup_idx in np.where(dup_elms != 1)[0]:
            found_dup_idx = np.argwhere(np.sum(mesh.nodes.node_coord == unique_elms[dup_idx], axis=1) == 3)
            for i in range(1, len(found_dup_idx)):
                try:
                    dup_2_rem = np.argwhere(ind_nodes == found_dup_idx[i])[0]
                    ind_nodes = np.delete(ind_nodes, dup_2_rem)
                except IndexError:
                    pass

    if skin_only_output:
        # replace smoothed nodes in skin only mesh and write to disk
        mesh_cropped.nodes.node_coord = smoothed_mesh.vertices  # overwrite simnibs Mesh object's nodes
        mesh_cropped.write(output_fn)
    else:
        # replace surface node_number list in full mesh and write to disk
        mesh.nodes.node_coord[ind_nodes, :] = smoothed_mesh.vertices
        mesh.write(output_fn)
