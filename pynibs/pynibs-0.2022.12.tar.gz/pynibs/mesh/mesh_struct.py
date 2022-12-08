""" """
import json
import os
import time
import nibabel
import numpy as np
from numpy import cross as cycross
import pynibs

__package__ = "pynibs"


def __path__():
    return os.path.dirname(__file__)


class TetrahedraLinear:
    """
    Mesh, consisting of linear tetrahedra.

    Parameters
    ----------
    points : array of float [N_points x 3]
        Vertices of FE mesh
    triangles : np.ndarray of int [N_tri x 3]
        Connectivity of points forming triangles
    triangles_regions : np.ndarray of int [N_tri x 1]
        Region identifiers of triangles
    tetrahedra : np.ndarray of int [N_tet x 4]
        Connectivity of points forming tetrahedra
    tetrahedra_regions : np.ndarray of int [N_tet x 1]
        Region identifiers of tetrahedra

    Attributes
    ----------
    N_points : int
        Number of vertices
    N_tet : int
        Number of tetrahedra
    N_tri : int
        Number of triangles
    N_region : int
        Number of regions
    region : np.ndarray of int
        Region labels
    tetrahedra_volume : np.ndarray of float [N_tet x 1]
        Volumes of tetrahedra
    tetrahedra_center : np.ndarray of float [N_tet x 1]
        Center of tetrahedra
    triangles_center : np.ndarray of float [N_tri x 1]
        Center of triangles
    triangles_normal : np.ndarray of float [N_tri x 3]
        Normal components of triangles pointing outwards
    """

    def __init__(self, points, triangles, triangles_regions, tetrahedra, tetrahedra_regions):
        """ Initialize TetrahedraLinear class """
        self.points = points
        self.triangles = triangles
        self.triangles_regions = triangles_regions
        self.tetrahedra = tetrahedra
        self.tetrahedra_regions = tetrahedra_regions
        # index of points in "tetrahedra" start with 0 or 1

        self.tetrahedra_triangle_surface_idx = - np.ones((self.triangles.shape[0], 2))

        # shift index to start always from 0 (python)
        if self.tetrahedra.size != 0:
            self.idx_start = np.min(self.tetrahedra)
            self.tetrahedra = self.tetrahedra - self.idx_start
            self.N_tet = self.tetrahedra.shape[0]
            p1_tet = self.points[self.tetrahedra[:, 0], :]  # [P1x P1y P1z]
            p2_tet = self.points[self.tetrahedra[:, 1], :]
            p3_tet = self.points[self.tetrahedra[:, 2], :]
            p4_tet = self.points[self.tetrahedra[:, 3], :]
            self.tetrahedra_volume = pynibs.calc_tetrahedra_volume_cross(p1_tet, p2_tet, p3_tet, p4_tet)
            self.tetrahedra_center = 1.0 / 4 * (p1_tet + p2_tet + p3_tet + p4_tet)

        else:
            self.N_tet = 0
            self.idx_start = 0
        self.triangles = self.triangles - self.idx_start

        self.region = np.unique(self.tetrahedra_regions)

        # number of elements and points etc
        self.N_points = self.points.shape[0]
        self.N_tri = self.triangles.shape[0]
        self.N_region = len(self.region)

        # count index lists of elements [0,1,2,....]
        self.tetrahedra_index = np.arange(self.N_tet)
        self.triangles_index = np.arange(self.N_tri)

        if self.N_tri > 0:
            p1_tri = self.points[self.triangles[:, 0], :]
            p2_tri = self.points[self.triangles[:, 1], :]
            p3_tri = self.points[self.triangles[:, 2], :]

            self.triangles_center = 1.0 / 3 * (p1_tri + p2_tri + p3_tri)
            self.triangles_normal = cycross(p2_tri - p1_tri, p3_tri - p1_tri)
            normal_norm = np.linalg.norm(self.triangles_normal, axis=1)
            normal_norm = normal_norm[:, np.newaxis]
            self.triangles_normal = self.triangles_normal / np.tile(normal_norm, (1, 3))
            self.triangles_area = 0.5 * np.linalg.norm(np.cross(p2_tri - p1_tri, p3_tri - p1_tri), axis=1)

    def calc_E_on_GM_WM_surface_simnibs(self, phi, dAdt, roi, subject, verbose=False, mesh_idx=0):
        """
        Determines the normal and tangential component of the induced electric field on a GM-WM surface by recalculating
        phi and dA/dt in an epsilon environment around the GM/WM surface (upper and lower GM-WM surface) or by using
        the Simnibs interpolation function.

        Parameters
        ----------
        phi : np.ndarray of float [N_nodes x 1]
            Scalar electric potential given in the nodes of the mesh
        dAdt : np.ndarray of float [N_nodes x 3]
            Magnetic vector potential given in the nodes of the mesh
        roi : object instance
            RegionOfInterestSurface object class instance
        subject : Subject object
            Subject object loaded from .hdf5 file
        verbose : boolean
            Print information to stdout
        mesh_idx : int
            Mesh index

        Returns
        -------
        E_normal : np.ndarray of float [N_points x 3]
            Normal vector of electric field on GM-WM surface
        E_tangential : np.ndarray of float [N_points x 3]
            Tangential vector of electric field on GM-WM surface
        """
        import tempfile
        import simnibs.msh.mesh_io as mesh_io
        import simnibs.simulation.fem as fem
        import simnibs.msh.transformations as transformations

        mesh_folder = subject.mesh[mesh_idx]["mesh_folder"]

        # load mesh
        mesh = mesh_io.read_msh(subject.mesh[mesh_idx]["fn_mesh_msh"])

        # write phi and dAdt in msh
        dAdt_SimNIBS = mesh_io.NodeData(dAdt, name='D', mesh=mesh)
        phi_SimNIBS = mesh_io.NodeData(phi.flatten(), name='v', mesh=mesh)

        if verbose:
            print("Calculating e-field")
        out = fem.calc_fields(phi_SimNIBS, "vDEe", cond=None, dadt=dAdt_SimNIBS)

        with tempfile.TemporaryDirectory() as f:
            fn_res_tmp = os.path.join(f, "res.msh")
            # mesh_io.write_msh(out, fn_res_tmp)

            if verbose:
                print("Interpolating values to midlayer of GM")
            # determine e in midlayer
            transformations.middle_gm_interpolation(mesh_fn=out,
                                                    m2m_folder=os.path.join(mesh_folder, "m2m_" + subject.id),
                                                    out_folder=f,
                                                    out_fsaverage=None,
                                                    depth=0.5,
                                                    quantities=['norm', 'normal', 'tangent', 'angle'],
                                                    fields=None,
                                                    open_in_gmsh=False,
                                                    write_msh=False)  #

            # load freesurfer surface
            if type(roi.gm_surf_fname) is not list:
                roi.gm_surf_fname = [roi.gm_surf_fname]

            points_gm = [None for _ in range(len(roi.gm_surf_fname))]
            con_gm = [None for _ in range(len(roi.gm_surf_fname))]

            max_idx_gm = 0

            if (roi.gm_surf_fname is list and len(roi.gm_surf_fname) > 0) or (roi.gm_surf_fname is str):
                fn_surface = list(roi.gm_surf_fname)
            elif (roi.midlayer_surf_fname is list and len(roi.gm_surf_fname) > 0) or (roi.midlayer_surf_fname is str):
                fn_surface = list(roi.midlayer_surf_fname)

            for i in range(len(fn_surface)):
                points_gm[i], con_gm[i] = nibabel.freesurfer.read_geometry(os.path.join(mesh_folder, fn_surface[i]))

                con_gm[i] = con_gm[i] + max_idx_gm

                max_idx_gm = max_idx_gm + points_gm[i].shape[0]  # np.max(con_gm[i]) + 2

            points_gm = np.vstack(points_gm)
            con_gm = np.vstack(con_gm)

            if verbose:
                print("Processing data to ROI")
            if roi.fn_mask is None or roi.fn_mask == []:

                if roi.X_ROI is None or roi.X_ROI == []:
                    roi.X_ROI = [-np.inf, np.inf]
                if roi.Y_ROI is None or roi.Y_ROI == []:
                    roi.Y_ROI = [-np.inf, np.inf]
                if roi.Z_ROI is None or roi.Z_ROI == []:
                    roi.Z_ROI = [-np.inf, np.inf]

                roi_mask_bool = (roi.node_coord_mid[:, 0] > min(roi.X_ROI)) & (
                        roi.node_coord_mid[:, 0] < max(roi.X_ROI)) & \
                                (roi.node_coord_mid[:, 1] > min(roi.Y_ROI)) & (
                                        roi.node_coord_mid[:, 1] < max(roi.Y_ROI)) & \
                                (roi.node_coord_mid[:, 2] > min(roi.Z_ROI)) & (
                                        roi.node_coord_mid[:, 2] < max(roi.Z_ROI))
                roi_mask_idx = np.where(roi_mask_bool)

            else:
                if type(roi.fn_mask) is np.ndarray:
                    if roi.fn_mask.ndim == 0:
                        roi.fn_mask = roi.fn_mask.astype(str).tolist()

                # read mask from freesurfer mask file
                mask = nibabel.freesurfer.mghformat.MGHImage.from_filename(
                        os.path.join(mesh_folder, roi.fn_mask)).dataobj[:]
                roi_mask_idx = np.where(mask > 0.5)

            # read results data
            if verbose:
                print("Reading SimNIBS midlayer data")
            e_normal = []
            e_tan = []

            for fn_surf in fn_surface:
                if "lh" in os.path.split(fn_surf)[1]:
                    e_normal.append(nibabel.freesurfer.read_morph_data(
                            os.path.join(f, "lh.res.central.E." + "normal")).flatten()[:, np.newaxis])
                    e_tan.append(nibabel.freesurfer.read_morph_data(
                            os.path.join(f, "lh.res.central.E." + "tangent")).flatten()[:, np.newaxis])

                if "rh" in os.path.split(fn_surf)[1]:
                    e_normal.append(nibabel.freesurfer.read_morph_data(
                            os.path.join(f, "rh.res.central.E." + "normal")).flatten()[:, np.newaxis])
                    e_tan.append(nibabel.freesurfer.read_morph_data(
                            os.path.join(f, "rh.res.central.E." + "tangent")).flatten()[:, np.newaxis])

            e_normal = np.vstack(e_normal)
            e_tan = np.vstack(e_tan)

            # transform point data to element data
            if verbose:
                print("Transforming point data to element data")
            e_normal = pynibs.data_nodes2elements(data=e_normal, con=con_gm)
            e_tan = pynibs.data_nodes2elements(data=e_tan, con=con_gm)

            # crop results data to ROI
            # if not roi_mask_bool.all():
            if roi_mask_idx:
                if verbose:
                    print("Cropping results data to ROI")

                # get row index where all points are lying inside ROI
                con_row_idx = [i for i in range(con_gm.shape[0]) if len(np.intersect1d(con_gm[i,], roi_mask_idx)) == 3]

                e_normal = e_normal[con_row_idx, :]
                e_tan = e_tan[con_row_idx, :]

        return e_normal, e_tan

    def calc_E_on_GM_WM_surface_simnibs_KW(self, phi, dAdt, roi, subject, verbose=False, mesh_idx=0):
        """
        Determines the normal and tangential component of the induced electric field on a GM-WM surface by recalculating
        phi and dA/dt in an epsilon environment around the GM/WM surface (upper and lower GM-WM surface) or by using
        the Simnibs interpolation function.

        Parameters
        ----------
        phi : np.ndarray of float [N_nodes x 1]
            Scalar electric potential given in the nodes of the mesh
        dAdt : np.ndarray of float [N_nodes x 3]
            Magnetic vector potential given in the nodes of the mesh
        roi : object instance
            RegionOfInterestSurface object class instance
        subject : Subject object
            Subject object loaded from .hdf5 file
        verbose : boolean
            Print information to stdout
        mesh_idx : int
            Mesh index

        Returns
        -------
        E_normal : np.ndarray of float [N_points x 3]
            Normal vector of electric field on GM-WM surface
        E_tangential : np.ndarray of float [N_points x 3]
            Tangential vector of electric field on GM-WM surface
        """
        import tempfile
        import simnibs.msh.mesh_io as mesh_io
        import simnibs.simulation.fem as fem
        import simnibs.msh.transformations as transformations

        mesh_folder = subject.mesh[mesh_idx]["mesh_folder"]

        # load mesh
        mesh = mesh_io.read_msh(subject.mesh[mesh_idx]["fn_mesh_msh"])

        # write phi and dAdt in msh
        dAdt_SimNIBS = mesh_io.NodeData(dAdt, name='D', mesh=mesh)
        phi_SimNIBS = mesh_io.NodeData(phi.flatten(), name='v', mesh=mesh)

        if verbose:
            print("Calculating e-field")
        out = fem.calc_fields(phi_SimNIBS, "vDEe", cond=None, dadt=dAdt_SimNIBS)

        with tempfile.TemporaryDirectory() as f:
            fn_res_tmp = os.path.join(f, "res.msh")
            mesh_io.write_msh(out, fn_res_tmp)

            if verbose:
                print("Interpolating values to midlayer of GM")
            # determine e in midlayer
            transformations.middle_gm_interpolation(mesh_fn=fn_res_tmp,
                                                    m2m_folder=os.path.join(mesh_folder, "m2m_" + subject.id),
                                                    out_folder=f,
                                                    out_fsaverage=None,
                                                    depth=0.5,
                                                    quantities=['norm', 'normal', 'tangent', 'angle'],
                                                    fields=None,
                                                    open_in_gmsh=False)  # write_msh=False

            # load freesurfer surface
            if type(roi.gm_surf_fname) is not list:
                roi.gm_surf_fname = [roi.gm_surf_fname]

            points_gm = [None for _ in range(len(roi.gm_surf_fname))]
            con_gm = [None for _ in range(len(roi.gm_surf_fname))]

            max_idx_gm = 0

            if (type(roi.gm_surf_fname) is list and roi.gm_surf_fname[0] is not None) or \
                    (type(roi.gm_surf_fname) is str):
                if type(roi.gm_surf_fname) is str:
                    fn_surface = [roi.gm_surf_fname]
                else:
                    fn_surface = roi.gm_surf_fname

            elif (type(roi.midlayer_surf_fname) is list and roi.gm_surf_fname is not None) or \
                    (type(roi.midlayer_surf_fname) is str):
                if type(roi.midlayer_surf_fname) is str:
                    fn_surface = [roi.midlayer_surf_fname]
                else:
                    fn_surface = roi.midlayer_surf_fname

            for i in range(len(fn_surface)):
                points_gm[i], con_gm[i] = nibabel.freesurfer.read_geometry(os.path.join(mesh_folder, fn_surface[i]))

                con_gm[i] = con_gm[i] + max_idx_gm

                max_idx_gm = max_idx_gm + points_gm[i].shape[0]  # np.max(con_gm[i]) + 2

            points_gm = np.vstack(points_gm)
            con_gm = np.vstack(con_gm)

            if verbose:
                print("Processing data to ROI")
            if roi.fn_mask is None or roi.fn_mask == []:

                if roi.X_ROI is None or roi.X_ROI == []:
                    roi.X_ROI = [-np.inf, np.inf]
                if roi.Y_ROI is None or roi.Y_ROI == []:
                    roi.Y_ROI = [-np.inf, np.inf]
                if roi.Z_ROI is None or roi.Z_ROI == []:
                    roi.Z_ROI = [-np.inf, np.inf]

                roi_mask_bool = (roi.node_coord_mid[:, 0] > min(roi.X_ROI)) & (
                        roi.node_coord_mid[:, 0] < max(roi.X_ROI)) & \
                                (roi.node_coord_mid[:, 1] > min(roi.Y_ROI)) & (
                                        roi.node_coord_mid[:, 1] < max(roi.Y_ROI)) & \
                                (roi.node_coord_mid[:, 2] > min(roi.Z_ROI)) & (
                                        roi.node_coord_mid[:, 2] < max(roi.Z_ROI))
                roi_mask_idx = np.where(roi_mask_bool)

            else:
                if type(roi.fn_mask) is np.ndarray:
                    if roi.fn_mask.ndim == 0:
                        roi.fn_mask = roi.fn_mask.astype(str).tolist()

                # read mask from freesurfer mask file
                mask = nibabel.freesurfer.mghformat.MGHImage.from_filename(
                        os.path.join(mesh_folder, roi.fn_mask)).dataobj[:]
                roi_mask_idx = np.where(mask > 0.5)

            # read results data
            if verbose:
                print("Reading SimNIBS midlayer data")
            e_normal = []
            e_tan = []

            for fn_surf in fn_surface:
                if "lh" in os.path.split(fn_surf)[1]:
                    e_normal.append(nibabel.freesurfer.read_morph_data(
                            os.path.join(f, "lh.res.central.E." + "normal")).flatten()[:, np.newaxis])
                    e_tan.append(nibabel.freesurfer.read_morph_data(
                            os.path.join(f, "lh.res.central.E." + "tangent")).flatten()[:, np.newaxis])

                if "rh" in os.path.split(fn_surf)[1]:
                    e_normal.append(nibabel.freesurfer.read_morph_data(
                            os.path.join(f, "rh.res.central.E." + "normal")).flatten()[:, np.newaxis])
                    e_tan.append(nibabel.freesurfer.read_morph_data(
                            os.path.join(f, "rh.res.central.E." + "tangent")).flatten()[:, np.newaxis])

            e_normal = np.vstack(e_normal)
            e_tan = np.vstack(e_tan)

            # transform point data to element data
            if verbose:
                print("Transforming point data to element data")
            e_normal = pynibs.data_nodes2elements(data=e_normal, con=con_gm)
            e_tan = pynibs.data_nodes2elements(data=e_tan, con=con_gm)

            # crop results data to ROI
            # if not roi_mask_bool.all():
            if roi_mask_idx:
                if verbose:
                    print("Cropping results data to ROI")

                # get row index where all points are lying inside ROI
                con_row_idx = [i for i in range(con_gm.shape[0]) if len(np.intersect1d(con_gm[i,], roi_mask_idx)) == 3]

                e_normal = e_normal[con_row_idx, :]
                e_tan = e_tan[con_row_idx, :]

        return e_normal, e_tan

    def calc_E_on_GM_WM_surface3(self, phi, dAdt, roi, verbose=True, mode="components"):
        """
        Determines the normal and tangential component of the induced electric field on a GM-WM surface by recalculating
        phi and dA/dt in an epsilon environment around the GM/WM surface (upper and lower GM-WM surface).

        Parameters
        ----------
        phi : np.ndarray of float [N_nodes x 1]
            Scalar electric potential given in the nodes of the mesh
        dAdt : np.ndarray of float [N_nodes x 3]
            Magnetic vector potential given in the nodes of the mesh
        roi : object instance
            RegionOfInterestSurface object class instance
        verbose : boolean
            Print information to stdout
        mode : str
            Select mode of output:
            - "components" : return x, y, and z component of tangential and normal components
            - "magnitude" : return magnitude of tangential and normal component (normal with sign for direction)

        Returns
        -------
        E_normal : np.ndarray of float [N_points x 3]
            Normal vector of electric field on GM-WM surface
        E_tangential : np.ndarray of float [N_points x 3]
            Tangential vector of electric field on GM-WM surface
        """
        # check if dimension are fitting
        assert phi.shape[0] == dAdt.shape[0]
        assert dAdt.shape[1] == 3

        # interpolate electric scalar potential to central points of upper and lower surface triangles
        if verbose:
            print("Interpolating electric scalar potential to central points of upper and lower surface triangles")
        phi_gm_wm_surface_up = self.calc_QOI_in_points_tet_idx(qoi=phi,
                                                               points_out=roi.tri_center_coord_up,
                                                               tet_idx=roi.tet_idx_tri_center_up.flatten())

        phi_gm_wm_surface_low = self.calc_QOI_in_points_tet_idx(qoi=phi,
                                                                points_out=roi.tri_center_coord_low,
                                                                tet_idx=roi.tet_idx_tri_center_low.flatten())

        # determine distance between upper and lower surface (in m!)
        d = np.linalg.norm(roi.tri_center_coord_up - roi.tri_center_coord_low, axis=1)[:, np.newaxis] * 1E-3
        d[np.argwhere(d == 0)[:, 0]] = 1e-6  # delete zero distances

        # determine surface normal vector (normalized)
        # n = ((points_up - points_low) / np.tile(d, (1, 3)))*1E-3
        # n = (points_up - points_low) * 1E-3

        p1_tri = roi.node_coord_mid[roi.node_number_list[:, 0], :]
        p2_tri = roi.node_coord_mid[roi.node_number_list[:, 1], :]
        p3_tri = roi.node_coord_mid[roi.node_number_list[:, 2], :]

        n = cycross(p2_tri - p1_tri, p3_tri - p1_tri)
        normal_norm = np.linalg.norm(n, axis=1)
        normal_norm = normal_norm[:, np.newaxis]
        n = n / np.tile(normal_norm, (1, 3))

        # interpolate magnetic vector potential to central surface points (primary electric field)
        # E_pri = griddata(self.points, dAdt, surf_mid, method='linear', fill_value=np.NaN, rescale=False)
        if verbose:
            print("Interpolating magnetic vector potential to central surface points (primary electric field)")
        e_pri = self.calc_QOI_in_points_tet_idx(qoi=dAdt,
                                                points_out=roi.tri_center_coord_mid,
                                                tet_idx=roi.tet_idx_tri_center_mid.flatten())

        # determine its normal component
        e_pri_normal = np.multiply(np.sum(np.multiply(e_pri, n), axis=1)[:, np.newaxis], n)

        # determine gradient of phi and multiply with surface normal (secondary electric field)
        e_sec_normal = np.multiply((phi_gm_wm_surface_up - phi_gm_wm_surface_low) * 1E-3 / d, n)

        # combine (normal) primary and secondary electric field
        e_normal = self.calc_E(e_sec_normal, e_pri_normal)

        # compute tangential component of secondary electric field on surface
        if verbose:
            print("Interpolating scalar electric potential to nodes of midlayer (primary electric field)")
        phi_surf_mid_nodes = self.calc_QOI_in_points_tet_idx(qoi=phi,
                                                             points_out=roi.node_coord_mid,
                                                             tet_idx=roi.tet_idx_node_coord_mid.flatten())

        if verbose:
            print("Determine gradient of scalar electric potential on midlayer surface (E_sec_tangential)")
        e_sec_tan = pynibs.calc_gradient_surface(phi=phi_surf_mid_nodes,
                                                 points=roi.node_coord_mid,
                                                 triangles=roi.node_number_list)

        # compute tangential component of primary electric field on surface
        e_pri_tan = e_pri - e_pri_normal

        # compute tangential component of total electric field
        e_tan = self.calc_E(e_sec_tan, e_pri_tan)

        # determine total E on surface (sanity check)
        # E = self.calc_QOI_in_points(E, surf_mid)

        if mode == "magnitude":
            # get sign info of normal component
            e_normal_dir = (np.sum(e_normal * n, axis=1) > 0)[:, np.newaxis].astype(int)

            e_normal_dir[e_normal_dir == 1] = 1
            e_normal_dir[e_normal_dir == 0] = -1

            # determine magnitude of vectors and assign sign info
            e_tan = np.linalg.norm(e_tan, axis=1)[:, np.newaxis]
            e_normal = np.linalg.norm(e_normal, axis=1)[:, np.newaxis] * e_normal_dir

        return e_normal, e_tan

    def calc_E_on_GM_WM_surface(self, E, roi):
        """
        Determines the normal and tangential component of the induced electric field on a GM-WM surface using
        nearest neighbour principle.

        Parameters
        ----------
        E : np.ndarray of float [N_tri x 3]
            Induced electric field given in the tetrahedra centre of the mesh instance
        roi : pynibs.roi.RegionOfInterestSurface
            RegionOfInterestSurface object class instance

        Returns
        -------
        E_normal : np.ndarray of float [N_points x 3]
            Normal vector of electric field on GM-WM surface
        E_tangential : np.ndarray of float [N_points x 3]
            Tangential vector of electric field on GM-WM surface
        """

        e_gm_wm_surface = E[roi.tet_idx_nodes_mid, :]

        # determine surface normal vector (normalized)
        n = cycross(roi.node_coord_mid[roi.node_number_list[:, 1]] - roi.node_coord_mid[roi.node_number_list[:, 0]],
                    roi.node_coord_mid[roi.node_number_list[:, 2]] - roi.node_coord_mid[roi.node_number_list[:, 0]])
        n = n / np.linalg.norm(n, axis=1)[:, np.newaxis]

        # determine its normal component
        e_normal = np.multiply(np.sum(np.multiply(e_gm_wm_surface, n), axis=1)[:, np.newaxis], n)

        # compute tangential component of total electric field
        e_tan = e_gm_wm_surface - e_normal

        # determine total E on surface (sanity check)
        # E = self.calc_QOI_in_points(E, surf_mid)

        return e_normal, e_tan

    def calc_QOI_in_points(self, qoi, points_out):
        """
        Calculate QOI_out in points_out using the mesh instance and the quantity of interest (QOI).

        Parameters
        ----------
        qoi : np.ndarray of float
            Quantity of interest in nodes of tetrahedra mesh instance
        points_out : np.ndarray of float
            Point coordinates (x, y, z) where the qoi is going to be interpolated by linear basis functions

        Returns
        -------
        qoi_out : np.ndarray of float
            Quantity of interest in points_out

        """

        N_phi_points_out = points_out.shape[0]
        qoi_out = np.zeros(
                [N_phi_points_out, qoi.shape[1] if qoi.ndim > 1 else 1])

        P1_all = self.points[self.tetrahedra[:, 0], :]
        P2_all = self.points[self.tetrahedra[:, 1], :]
        P3_all = self.points[self.tetrahedra[:, 2], :]
        P4_all = self.points[self.tetrahedra[:, 3], :]

        # identify  in which tetrahedron the point lies
        # (all other volumes have at least one negative sub-volume)

        # determine all volumes (replacing points with points_out)
        # find the element where all volumes are > 0 (not inverted element)
        # get index of this tetrahedron
        # do it successively to decrease amount of volume calculations for all
        # 4 points in tetrahedra
        for i in range(N_phi_points_out):
            start = time.time()
            Vtest1 = pynibs.calc_tetrahedra_volume_cross(np.tile(points_out[i, :], (P1_all.shape[0], 1)),
                                                         P2_all,
                                                         P3_all,
                                                         P4_all)
            tet_idx_bool_1 = (Vtest1 >= 0)
            tet_idx_1 = np.nonzero(tet_idx_bool_1)[0]

            Vtest2 = pynibs.calc_tetrahedra_volume_cross(P1_all[tet_idx_1, :],
                                                         np.tile(
                                                                 points_out[i, :], (tet_idx_1.shape[0], 1)),
                                                         P3_all[tet_idx_1, :],
                                                         P4_all[tet_idx_1, :])
            tet_idx_bool_2 = (Vtest2 >= 0)
            tet_idx_2 = tet_idx_1[np.nonzero(tet_idx_bool_2)[0]]

            Vtest3 = pynibs.calc_tetrahedra_volume_cross(P1_all[tet_idx_2, :],
                                                         P2_all[tet_idx_2, :],
                                                         np.tile(
                                                                 points_out[i, :], (tet_idx_2.shape[0], 1)),
                                                         P4_all[tet_idx_2, :])
            tet_idx_bool_3 = (Vtest3 >= 0)
            tet_idx_3 = tet_idx_2[np.nonzero(tet_idx_bool_3)[0]]

            Vtest4 = pynibs.calc_tetrahedra_volume_cross(P1_all[tet_idx_3, :],
                                                         P2_all[tet_idx_3, :],
                                                         P3_all[tet_idx_3, :],
                                                         np.tile(points_out[i, :], (tet_idx_3.shape[0], 1)))
            tet_idx_bool_4 = (Vtest4 >= 0)
            tet_idx = tet_idx_3[np.nonzero(tet_idx_bool_4)[0]]

            # calculate subvolumes of final tetrahedron and its total volume
            Vsub1 = pynibs.calc_tetrahedra_volume_cross(points_out[i, :][np.newaxis],
                                                        P2_all[tet_idx, :],
                                                        P3_all[tet_idx, :],
                                                        P4_all[tet_idx, :])
            Vsub2 = pynibs.calc_tetrahedra_volume_cross(P1_all[tet_idx, :],
                                                        points_out[i, :][np.newaxis],
                                                        P3_all[tet_idx, :],
                                                        P4_all[tet_idx, :])
            Vsub3 = pynibs.calc_tetrahedra_volume_cross(P1_all[tet_idx, :],
                                                        P2_all[tet_idx, :],
                                                        points_out[i, :][np.newaxis],
                                                        P4_all[tet_idx, :])
            Vsub4 = pynibs.calc_tetrahedra_volume_cross(P1_all[tet_idx, :],
                                                        P2_all[tet_idx, :],
                                                        P3_all[tet_idx, :],
                                                        points_out[i, :][np.newaxis], )

            vsub = np.array([Vsub1, Vsub2, Vsub3, Vsub4])
            vtot = np.sum(vsub)

            # calculate phi_out
            qoi_out[i,] = 1.0 * np.dot(vsub.T, qoi[self.tetrahedra[tet_idx[0], :],]) / vtot

            stop = time.time()
            print(('Total: Point: {:d}/{:d} [{} sec]\n'.format(i + 1, N_phi_points_out, stop - start)))

        return qoi_out

    def calc_QOI_in_points_tet_idx(self, qoi, points_out, tet_idx):
        """
        Calculate QOI_out in points_out sitting in tet_idx using the mesh instance and the quantity of interest (QOI).

        Parameters
        ----------
        qoi : np.ndarray of float
            Quantity of interest in nodes of tetrahedra mesh instance
        points_out : np.ndarray of float
            Point coordinates (x, y, z) where the qoi is going to be interpolated by linear basis functions
        tet_idx : np.ndarray of int
            Element indices where the points_out are sitting

        Returns
        -------
        qoi_out : np.ndarray of float
            Quantity of interest in points_out

        """

        N_phi_points_out = points_out.shape[0]
        qoi_out = np.zeros([N_phi_points_out, qoi.shape[1] if qoi.ndim > 1 else 1])

        P1_all = self.points[self.tetrahedra[:, 0], :]
        P2_all = self.points[self.tetrahedra[:, 1], :]
        P3_all = self.points[self.tetrahedra[:, 2], :]
        P4_all = self.points[self.tetrahedra[:, 3], :]

        # determine sub-volumes
        Vsub1 = pynibs.calc_tetrahedra_volume_cross(points_out,
                                                    P2_all[tet_idx, :],
                                                    P3_all[tet_idx, :],
                                                    P4_all[tet_idx, :])
        Vsub2 = pynibs.calc_tetrahedra_volume_cross(P1_all[tet_idx, :],
                                                    points_out,
                                                    P3_all[tet_idx, :],
                                                    P4_all[tet_idx, :])
        Vsub3 = pynibs.calc_tetrahedra_volume_cross(P1_all[tet_idx, :],
                                                    P2_all[tet_idx, :],
                                                    points_out,
                                                    P4_all[tet_idx, :])
        Vsub4 = pynibs.calc_tetrahedra_volume_cross(P1_all[tet_idx, :],
                                                    P2_all[tet_idx, :],
                                                    P3_all[tet_idx, :],
                                                    points_out)
        Vsub = np.hstack([Vsub1, Vsub2, Vsub3, Vsub4])
        Vtot = np.sum(Vsub, axis=1)

        # calculate the QOIs in the tetrahedron of interest
        for i in range(qoi.shape[1]):
            qoi_out[:, i] = 1.0 * np.sum(np.multiply(Vsub, qoi[self.tetrahedra[tet_idx, :], i]), axis=1) / Vtot

        # for i in range(N_phi_points_out):
        #     # calculate subvolumes of final tetrahedron and its total volume
        #     Vsub1 = pynibs.calc_tetrahedra_volume_cross(points_out[i, :][np.newaxis],
        #                                               P2_all[tet_idx[i], :][np.newaxis],
        #                                               P3_all[tet_idx[i], :][np.newaxis],
        #                                               P4_all[tet_idx[i], :][np.newaxis])
        #     Vsub2 = pynibs.calc_tetrahedra_volume_cross(P1_all[tet_idx[i], :][np.newaxis],
        #                                               points_out[i, :][np.newaxis],
        #                                               P3_all[tet_idx[i], :][np.newaxis],
        #                                               P4_all[tet_idx[i], :][np.newaxis])
        #     Vsub3 = pynibs.calc_tetrahedra_volume_cross(P1_all[tet_idx[i], :][np.newaxis],
        #                                               P2_all[tet_idx[i], :][np.newaxis],
        #                                               points_out[i, :][np.newaxis],
        #                                               P4_all[tet_idx[i], :][np.newaxis])
        #     Vsub4 = pynibs.calc_tetrahedra_volume_cross(P1_all[tet_idx[i], :][np.newaxis],
        #                                               P2_all[tet_idx[i], :][np.newaxis],
        #                                               P3_all[tet_idx[i], :][np.newaxis],
        #                                               points_out[i, :][np.newaxis])
        #
        #     Vtot = np.sum([Vsub1, Vsub2, Vsub3, Vsub4])
        #
        #     # calculate the QOIs in the tetrahedron of interest
        #     qoi_out[i,] = 1.0 * np.dot(Vsub.T, qoi[self.tetrahedra[tet_idx[i], :],]) / Vtot

        return qoi_out

    def data_nodes2elements(self, data):
        """
        Interpolate data given in the nodes to the tetrahedra center.

        Parameters
        ----------
        data : np.ndarray [N_nodes x N_data]
            Data in nodes

        Returns
        -------
        data_elements : np.ndarray [N_elements x N_data]
            Data in elements
        """
        data_elements = np.sum(data[self.tetrahedra[:, i]] for i in range(4)) / 4.0

        return data_elements

    def data_elements2nodes(self, data):
        """
        Transforms an data in tetrahedra into the nodes after Zienkiewicz et al. (1992) [1]_.
        Can only transform volume data, i.e. needs the data in the surrounding tetrahedra to average it to the nodes.
        Will not work well for discontinuous fields (like E, if several tissues are used).

        Parameters
        ----------
        data : np.ndarray [N_elements x N_data]
            Data in tetrahedra

        Returns
        -------
        data_nodes : np.ndarray [N_nodes x N_data]
            Data in nodes

        Notes
        -----
        .. [1] Zienkiewicz, Olgierd Cecil, and Jian Zhong Zhu. "The superconvergent patch recovery and a
           posteriori error estimates. Part 1: The recovery technique." International Journal for
           Numerical Methods in Engineering 33.7 (1992): 1331-1364.
        """

        # check dimension of input data
        if data.ndim == 1:
            data = data[:, np.newaxis]

        N_data = data.shape[1]
        data_nodes = np.zeros((self.N_points, N_data))

        if self.N_tet != data.shape[0]:
            raise ValueError("The number of data points in the data has to be equal to the number"
                             "of elements in the mesh")

        value = np.atleast_2d(data)
        if value.shape[0] < value.shape[1]:
            value = value.T

        # nd = np.zeros((self.N_points, N_data))

        # get all nodes used in tetrahedra, creates the NodeData structure
        # uq = np.unique(msh.elm[msh.elm.tetrahedra])
        # nd = NodeData(np.zeros((len(uq), self.nr_comp)), self.field_name, mesh=msh)
        # nd.node_number = uq

        # Get the point in the outside surface
        points_outside = np.unique(self.get_outside_faces())
        outside_points_mask = np.in1d(self.tetrahedra, points_outside).reshape(-1, 4)
        masked_th_nodes = np.copy(self.tetrahedra)
        masked_th_nodes[outside_points_mask] = -1

        # Calculates the quantities needed for the superconvergent patch recovery
        uq_in, th_nodes = np.unique(masked_th_nodes, return_inverse=True)

        baricenters = self.tetrahedra_center
        volumes = self.tetrahedra_volume
        baricenters = np.hstack([np.ones((baricenters.shape[0], 1)), baricenters])

        A = np.empty((len(uq_in), 4, 4))
        b = np.empty((len(uq_in), 4, N_data), 'float64')
        for i in range(4):
            for j in range(i, 4):
                A[:, i, j] = np.bincount(th_nodes.reshape(-1),
                                         np.repeat(baricenters[:, i], 4) *
                                         np.repeat(baricenters[:, j], 4))
        A[:, 1, 0] = A[:, 0, 1]
        A[:, 2, 0] = A[:, 0, 2]
        A[:, 3, 0] = A[:, 0, 3]
        A[:, 2, 1] = A[:, 1, 2]
        A[:, 3, 1] = A[:, 1, 3]
        A[:, 3, 2] = A[:, 2, 3]

        for j in range(N_data):
            for i in range(4):
                b[:, i, j] = np.bincount(th_nodes.reshape(-1),
                                         np.repeat(baricenters[:, i], 4) *
                                         np.repeat(value[:, j], 4))

        a = np.linalg.solve(A[1:], b[1:])
        p = np.hstack([np.ones((len(uq_in) - 1, 1)), self.points[uq_in[1:]]])
        f = np.einsum('ij, ijk -> ik', p, a)
        data_nodes[uq_in[1:]] = f

        # Assigns the average value to the points in the outside surface
        masked_th_nodes = np.copy(self.tetrahedra)
        masked_th_nodes[~outside_points_mask] = -1
        uq_out, th_nodes_out = np.unique(masked_th_nodes, return_inverse=True)

        sum_vals = np.empty((len(uq_out), N_data), 'float64')

        for j in range(N_data):
            sum_vals[:, j] = np.bincount(th_nodes_out.reshape(-1),
                                         np.repeat(value[:, j], 4) *
                                         np.repeat(volumes, 4))

        sum_vols = np.bincount(th_nodes_out.reshape(-1), np.repeat(volumes, 4))

        data_nodes[uq_out[1:]] = (sum_vals / sum_vols[:, None])[1:]

        return data_nodes

    def get_outside_faces(self, tetrahedra_indexes=None):
        """
        Creates a list of nodes in each face that are in the outer volume.

        Parameters
        ----------
        tetrahedra_indices : np.ndarray
            Indices of the tetrehedra where the outer volume is to be determined (default: all tetrahedra)

        Returns
        -------
        faces : np.ndarray
            List of nodes in faces in arbitrary order
        """

        if tetrahedra_indexes is None:
            tetrahedra_indexes = self.tetrahedra_index

        th = self.tetrahedra[tetrahedra_indexes]
        faces = th[:, [[0, 2, 1], [0, 1, 3], [0, 3, 2], [1, 2, 3]]]
        faces = faces.reshape(-1, 3)
        hash_array = np.array([hash(f.tobytes()) for f in np.sort(faces, axis=1)])
        unique, idx, inv, count = np.unique(hash_array, return_index=True,
                                            return_inverse=True, return_counts=True)

        # if np.any(count > 2):
        #     raise ValueError('Invalid Mesh: Found a face with more than 2 adjacent'
        #                      ' tetrahedra!')

        outside_faces = faces[idx[count == 1]]

        return outside_faces

    def calc_gradient(self, phi):
        """
        Calculate gradient of scalar DOF in tetrahedra center.

        Parameters
        ----------
        phi : np.ndarray of float [N_nodes]
            Scalar DOF the gradient is calculated for

        Returns
        -------
        grad_phi : np.ndarray of float [N_tet x 3]
            Gradient of Scalar DOF in tetrahedra center
        """

        a1 = np.vstack((self.points[self.tetrahedra[:, 3], :] - self.points[self.tetrahedra[:, 1], :],
                        self.points[self.tetrahedra[:, 2], :] -
                        self.points[self.tetrahedra[:, 0], :],
                        self.points[self.tetrahedra[:, 3], :] -
                        self.points[self.tetrahedra[:, 0], :],
                        self.points[self.tetrahedra[:, 1], :] - self.points[self.tetrahedra[:, 0], :]))

        a2 = np.vstack((self.points[self.tetrahedra[:, 2], :] - self.points[self.tetrahedra[:, 1], :],
                        self.points[self.tetrahedra[:, 3], :] -
                        self.points[self.tetrahedra[:, 0], :],
                        self.points[self.tetrahedra[:, 1], :] -
                        self.points[self.tetrahedra[:, 0], :],
                        self.points[self.tetrahedra[:, 2], :] - self.points[self.tetrahedra[:, 0], :]))

        a3 = np.vstack((self.points[self.tetrahedra[:, 0], :] - self.points[self.tetrahedra[:, 1], :],
                        self.points[self.tetrahedra[:, 1], :] -
                        self.points[self.tetrahedra[:, 0], :],
                        self.points[self.tetrahedra[:, 2], :] -
                        self.points[self.tetrahedra[:, 0], :],
                        self.points[self.tetrahedra[:, 3], :] - self.points[self.tetrahedra[:, 0], :]))

        volumes = np.sum(np.multiply(cycross(a1, a2), a3), 1)
        volumes = volumes[:, np.newaxis]
        Dlambda = np.transpose(np.reshape(cycross(
                a1, a2) / np.tile(volumes, (1, 3)), (self.N_tet, 4, 3), order='F'), (0, 2, 1))

        grad_phi = np.zeros((self.N_tet, 3))
        # calculate gradient at barycenters of tetrahedra
        for j in range(4):
            grad_phi = grad_phi + Dlambda[:, :, j] * np.tile(phi[self.tetrahedra[:, j]], (1, 3))

        return grad_phi

    def calc_E(self, grad_phi, omegaA):
        """
        Calculate electric field with gradient of electric potential and omega-scaled magnetic vector potential A.

        .. math:: \mathbf{E}=-\\nabla\\varphi-\omega\mathbf{A}

        Parameters
        ----------
        grad_phi : np.ndarray of float [N_tet x 3]
            Gradient of Scalar DOF in tetrahedra center
        omegaA : np.ndarray of float [N_tet x 3]
            Magnetic vector potential in tetrahedra center (scaled with angular frequency omega)

        Returns
        -------
        E : np.ndarray of float [N_tet x 3]
            Electric field in tetrahedra center
        """

        E = -grad_phi - omegaA

        return E

    def calc_J(self, E, sigma):
        """ Calculate current density J. The conductivity sigma is a list of np.arrays containing conductivities of
        regions (scalar and/or tensor).

        .. math::
            \mathbf{J} = [\sigma]\mathbf{E}

        Parameters
        ----------
        E : np.ndarray of float [N_tet x 3]
            Electric field in tetrahedra center
        sigma : list of np.ndarray of float [N_regions][3 x 3]
            Conductivities of regions (scalar and/or tensor).

        Returns
        -------
        E : np.ndarray of float [N_tet x 3]
            Electric field in tetrahedra center
        """

        J = np.zeros((E.shape[0], 3))

        for i in range(self.N_region):
            tet_bool_idx = self.tetrahedra_regions == self.region[i]
            J[tet_bool_idx[:, 0], :] = np.dot(
                    sigma[i], E[tet_bool_idx[:, 0], :].T).T
        return J

    def calc_surface_adjacent_tetrahedra_idx_list(self, fname):
        """
        Determine the indices of the tetrahedra touching the surfaces and save the indices into a .txt file specified
        with fname.

        Parameters
        ----------
        fname : str
            Filename of output .txt file

        Returns
        -------
        <File> : .txt file
            Element indices of the tetrahedra touching the surfaces (outer-most elements)
        """

        # determine indices of the 2 adjacent tetrahedra with common face on
        # surface
        P1_idx = np.zeros((self.N_tet, 1), dtype=bool)
        P2_idx = np.zeros((self.N_tet, 1), dtype=bool)
        P3_idx = np.zeros((self.N_tet, 1), dtype=bool)
        tet_idx_pos = np.zeros((self.N_tri, 1)).astype(int)
        tet_idx_neg = np.zeros((self.N_tri, 1)).astype(int)

        start = time.time()

        tetrahedra0 = self.tetrahedra[:, 0]
        tetrahedra1 = self.tetrahedra[:, 1]
        tetrahedra2 = self.tetrahedra[:, 2]
        tetrahedra3 = self.tetrahedra[:, 3]

        for i in range(self.N_tri):

            if (not (i % 100) and i > 0):
                stop = time.time()
                print(('Tri: {:d}/{:d} [{} sec]\n'.format(i, self.N_tri, stop - start)))
                start = time.time()

            triangle = set(self.triangles[i, :])

            triangle0 = self.triangles[i, 0]
            triangle1 = self.triangles[i, 1]
            triangle2 = self.triangles[i, 2]

            P1_idx = (tetrahedra0 == triangle0) | (tetrahedra1 == triangle0) | (
                    tetrahedra2 == triangle0) | (tetrahedra3 == triangle0)
            P2_idx = (tetrahedra0 == triangle1) | (tetrahedra1 == triangle1) | (
                    tetrahedra2 == triangle1) | (tetrahedra3 == triangle1)
            P3_idx = (tetrahedra0 == triangle2) | (tetrahedra1 == triangle2) | (
                    tetrahedra2 == triangle2) | (tetrahedra3 == triangle2)

            tet_bool_idx = P1_idx & P2_idx & P3_idx
            tet_idx = np.where(tet_bool_idx)[0][:]

            # get 4th (test) point of e.g. first tetrahedron which is not in
            # plane
            P4_idx = list(set(self.tetrahedra[tet_idx[0], :]) - triangle)

            # calculate projection of the line between:
            # center of triangle -> 4th point
            # and
            # normal of the triangle
            c = np.dot(
                    self.points[P4_idx, :] - self.triangles_center[i, :], self.triangles_normal[i, :])

            # positive projection: normal points to the 4th (test) point of first tetrahedron
            # and first tetrahedron is on "positive" side

            # outermost surface (has only one adjacent tetrahedron)
            if len(tet_idx) == 1:
                if c > 0:
                    tet_idx_pos[i] = tet_idx[0]
                    tet_idx_neg[i] = -1

                else:
                    tet_idx_pos[i] = -1
                    tet_idx_neg[i] = tet_idx[0]

            # inner surfaces have 2 adjacent tetrahedra
            else:
                if c > 0:
                    tet_idx_pos[i] = tet_idx[0]
                    tet_idx_neg[i] = tet_idx[1]
                else:
                    tet_idx_pos[i] = tet_idx[1]
                    tet_idx_neg[i] = tet_idx[0]

        # save the indices of the tetrahedra sharing the surfaces (negative,
        # i.e. bottom side first)
        self.tetrahedra_triangle_surface_idx = np.hstack(
                [tet_idx_neg, tet_idx_pos])
        f = open(fname, 'w')
        np.savetxt(f, self.tetrahedra_triangle_surface_idx, '%d')
        f.close()

    def calc_E_normal_tangential_surface(self, E, fname):
        """
        Calculate normal and tangential component of electric field on given surfaces of mesh instance.

        Parameters
        ----------
        E : np.ndarray of float [N_tri x 3]
            Electric field data on surfaces
        fname : str
            Filename of the .txt file containing the tetrahedra indices, which are adjacent to the surface triangles
            generated by the method "calc_surface_adjacent_tetrahedra_idx_list(self, fname)"

        Returns
        -------
        En_pos : np.ndarray of float [N_tri x 3]
            Normal component of electric field of top side (outside) of surface
        En_neg : np.ndarray of float [N_tri x 3]
            Normal component of electric field of bottom side (inside) of surface
        n : np.ndarray of float [N_tri x 3]
            Normal vector
        Et : np.ndarray of float [N_tri x 3]
            Tangential component of electric field lying in surface
        t : np.ndarray of float [N_tri x 3]
            Tangential vector
        """

        n = self.triangles_normal
        En_pos = np.zeros((self.N_tri, 1))
        En_neg = np.zeros((self.N_tri, 1))
        Et = np.zeros((self.N_tri, 1))
        t = np.zeros((self.N_tri, 3))
        self.tetrahedra_triangle_surface_idx = np.loadtxt(fname).astype(int)

        for i in range(self.N_tri):
            En_neg[i, 0] = np.dot(
                    E[self.tetrahedra_triangle_surface_idx[i, 0], :], n[i, :])

            if self.tetrahedra_triangle_surface_idx[i, 1] > -1:
                En_pos[i, 0] = np.dot(
                        E[self.tetrahedra_triangle_surface_idx[i, 1], :], n[i, :])
            else:
                En_pos[i, 0] = np.nan

            t[i, :] = E[self.tetrahedra_triangle_surface_idx[i, 0], :] - \
                      1.0 * En_neg[i, 0] * n[i, :]
            Et[i, 0] = np.linalg.norm(t[i, :])
            t[i, :] = t[i, :] / Et[i, 0] if Et[i, 0] > 0 else np.zeros(3)

        return En_pos, En_neg, n, Et, t

    def get_faces(self, tetrahedra_indexes=None):
        """
        Creates a list of nodes in each face and a list of faces in each tetrahedra.

        Parameters
        ----------
        tetrahedra_indexes : np.ndarray
            Indices of the tetrehedra where the faces are to be determined (default: all tetrahedra)

        Returns
        -------
        faces : np.ndarray
            List of nodes in faces, in arbitrary order
        th_faces : np.ndarray
            List of faces in each tetrahedra, starts at 0, order=((0, 2, 1), (0, 1, 3), (0, 3, 2), (1, 2, 3))
        face_adjacency_list : np.ndarray
            List of tetrahedron adjacent to each face, filled with -1 if a face is in a
            single tetrahedron. Not in the normal element ordering, but only in the order
            the tetrahedra are presented
        """

        if tetrahedra_indexes is None:
            tetrahedra_indexes = np.arange(self.tetrahedra.shape[0])
        # th = self[tetrahedra_indexes]
        th = self.tetrahedra[tetrahedra_indexes, :]
        faces = th[:, [[0, 2, 1], [0, 1, 3], [0, 3, 2], [1, 2, 3]]]
        faces = faces.reshape(-1, 3)
        hash_array = np.array([hash(f.tobytes()) for f in np.sort(faces, axis=1)])
        unique, idx, inv, count = np.unique(hash_array, return_index=True,
                                            return_inverse=True, return_counts=True)
        faces = faces[idx]
        face_adjacency_list = -np.ones((len(unique), 2), dtype=int)
        face_adjacency_list[:, 0] = idx // 4

        # if np.any(count > 2):
        #     raise ValueError('Invalid Mesh: Found a face with more than 2 adjacent'
        #                      ' tetrahedra!')

        # Remove the faces already seen from consideration
        # Second round in order to make adjacency list
        # create a new array with a mask in the elements already seen
        mask = unique[-1] + 1
        hash_array_masked = np.copy(hash_array)
        hash_array_masked[idx] = mask
        # make another array, where we delete the elements we have already seen
        hash_array_reduced = np.delete(hash_array, idx)
        # Finds where each element of the second array is in the first array
        # (https://stackoverflow.com/a/8251668)
        hash_array_masked_sort = hash_array_masked.argsort()
        hash_array_repeated_pos = hash_array_masked_sort[
            np.searchsorted(hash_array_masked[hash_array_masked_sort], hash_array_reduced)]
        # Now find the index of the face corresponding to each element in the
        # hash_array_reduced
        faces_repeated = np.searchsorted(unique, hash_array_reduced)
        # Finally, fill out the second column in the adjacency list
        face_adjacency_list[faces_repeated, 1] = hash_array_repeated_pos // 4

        return faces, inv.reshape(-1, 4), face_adjacency_list


class Mesh:
    """"
    Mesh class to initialize default attributes.
    """

    def __init__(self, mesh_name, subject_id, subject_folder):
        self.subject_id = subject_id
        self.subject_folder = subject_folder
        self.name = mesh_name
        self.info = None
        self.approach = None  # 'mri2mesh', 'headreco', 'charm'
        self.mri_idx = None

        # default parameters
        self.mesh_folder = os.path.join(subject_folder, 'mesh', mesh_name)
        self.fn_mesh_msh = os.path.join(self.mesh_folder, f"{subject_id}.msh")
        self.fn_mesh_hdf5 = os.path.join(self.mesh_folder, f"{subject_id}.hdf5")
        self.fn_tensor_vn = f"d2c_{subject_id}{os.sep}dti_results_T1space{os.sep}DTI_conf_tensor.nii.gz"
        self.fn_mri_conform = f"{subject_id}_T1fs_conform.nii.gz"
        self.fn_lh_midlayer = f"fs_{subject_id}{os.sep}surf{os.sep}lh.central"
        self.fn_rh_midlayer = f"fs_{subject_id}{os.sep}surf{os.sep}rh.central"
        self.vertex_density = 1.0  # headreco
        self.numvertices = 100000  # mri2mesh

        # refinement parameters
        self.center = None
        self.radius = None
        self.element_size = None
        self.refine_domains = None
        self.smooth_domains = None

        self.fn_lh_wm = None
        self.fn_rh_wm = None
        self.fn_lh_gm = None
        self.fn_rh_gm = None
        self.fn_lh_gm_curv = None
        self.fn_rh_gm_curv = None

        # charm meshes
        self.smooth_skin = None
        self.refinement_roi = None
        self.refinemement_element_size = None

    def fill_defaults(self, approach):
        """
        Initializes attributes for a headreco mesh.

        Parameters
        ----------
        approach: str
            'headreco'
            'mri2mesh'
            'charm'
        """
        self.approach = approach
        if approach == 'headreco':
            self.fn_mesh_msh = os.path.join(self.mesh_folder, f"{self.subject_id}.msh")
            self.fn_mesh_hdf5 = os.path.join(self.mesh_folder, f"{self.subject_id}.hdf5")
            self.fn_tensor_vn = f"d2c_{self.subject_id}{os.sep}dti_results_T1space{os.sep}DTI_conf_tensor.nii.gz"
            self.fn_mri_conform = f"{self.subject_id}_T1fs_conform.nii.gz"
            self.fn_lh_midlayer = f"fs_{self.subject_id}{os.sep}surf{os.sep}lh.central"
            self.fn_rh_midlayer = f"fs_{self.subject_id}{os.sep}surf{os.sep}rh.central"

        elif approach == 'mri2mesh':
            self.fn_mesh_msh = os.path.join(self.mesh_folder, f"{self.subject_id}.msh")
            self.fn_mesh_hdf5 = os.path.join(self.mesh_folder, f"{self.subject_id}.hdf5")
            self.fn_tensor_vn = f"d2c_{self.subject_id}{os.sep}dti_results_T1space{os.sep}DTI_conf_tensor.nii.gz"
            self.fn_mri_conform = f"{self.subject_id}_T1fs_conform.nii.gz"
            self.fn_lh_gm_curv = f"fs_{self.subject_id}{os.sep}surf{os.sep}lh.curv.pial"
            self.fn_rh_gm_curv = f"fs_{self.subject_id}{os.sep}surf{os.sep}rh.curv.pial"

        elif approach == 'charm':
            self.fn_mesh_msh = os.path.join(self.mesh_folder, f"{self.subject_id}.msh")
            self.fn_mesh_hdf5 = os.path.join(self.mesh_folder, f"{self.subject_id}.hdf5")
            self.fn_tensor_vn = f"d2c_{self.subject_id}{os.sep}dti_results_T1space{os.sep}DTI_conf_tensor.nii.gz"
            self.fn_mri_conform = f"{self.subject_id}_T1.nii.gz"
            self.fn_lh_midlayer = f"m2m_{self.subject_id}{os.sep}surfaces{os.sep}lh.central.gii"
            self.fn_rh_midlayer = f"m2m_{self.subject_id}{os.sep}surfaces{os.sep}rh.central.gii"

        else:
            raise NotImplementedError(f"Approach {approach} not implemented.")

    def write_to_hdf5(self, fn_hdf5, check_file_exist=False, verbose=False):
        """
        Write this mesh' attributes to .hdf5 file.

        Parameters
        ----------
        fn_hdf5 : str
        check_file_exist : bool
            Check if provided filenames exist, warn if not.
        verbose : bool
            Print self information
        """

        pynibs.write_dict_to_hdf5(fn_hdf5=fn_hdf5, data=self.__dict__, folder=f"mesh/{self.name}",
                                  check_file_exist=check_file_exist)
        if verbose:
            self.print()

    def print(self):
        """
        Print self information.
        """
        n_left, n_right = int(32 - np.floor((len(self.name) + 10) / 2)), int(32 - np.ceil((len(self.name) + 10) / 2))
        n_left, n_right = np.max(n_left, 0), np.max(n_right, 0)
        print("    " + "=" * n_left + f"  Mesh {self.name}:  " + "=" * n_right)
        print("\t" + json.dumps(self.__dict__, sort_keys=False, indent="\t", ))
        print("    " + "=" * 64 + "\n")


class ROI:
    """"
    Region of interest class to initialize default attributes.

    """

    def __init__(self, subject_id, roi_name, mesh_name):
        self.subject_id = subject_id
        self.name = roi_name
        self.mesh_name = mesh_name
        self.type = None  # 'surface' or 'volume'
        self.info = None
        self.template = None  # None, 'MNI', 'fsaverage', 'subject'
        self.gm_surf_fname = None
        self.wm_surf_fname = None
        self.midlayer_surf_fname = None
        self.delta = 0.5
        self.refine = False
        self.X_ROI = None
        self.Y_ROI = None
        self.Z_ROI = None
        self.center = None
        self.radius = None
        self.layer = 3
        self.fn_mask = None
        self.fn_mask_avg = None
        self.hemisphere = None
        self.midlayer_surf_fname = None
        self.tri_center_coord_mid = None

    def write_to_hdf5(self, fn_hdf5, check_file_exist=False, verbose=False):
        """
        Write this mesh' attributes to .hdf5 file.

        Parameters
        ----------
        fn_hdf5 : str
        check_file_exist : bool
            Check if provided filenames exist, warn if not.
        verbose : bool
            Print self information
        """

        pynibs.write_dict_to_hdf5(fn_hdf5=fn_hdf5, data=self.__dict__, folder=f"roi/{self.mesh_name}/{self.name}",
                                  check_file_exist=check_file_exist)
        if verbose:
            self.print()

    def print(self):
        """
        Print self information.
        """
        n_left, n_right = int(32 - np.floor((len(self.name) + 10) / 2)), int(32 - np.ceil((len(self.name) + 10) / 2))
        n_left, n_right = np.max(n_left, 0), np.max(n_right, 0)
        print("    " + "=" * n_left + f"  ROI {self.name}:  " + "=" * n_right)
        print("\t" + json.dumps(self.__dict__, sort_keys=False, indent="\t", ))
        print("    " + "=" * 64 + "\n")
