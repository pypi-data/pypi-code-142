import numpy as np

try:
    from mayavi.mlab import *
except ModuleNotFoundError:
    pass


def plot_surface(data, con, points):
    """
    Plots data in triangle center

    Parameters
    ----------
    data : np.array of float [n_tris]
        Data in triangular center
    con : np.array of float [n_tris x 3]
        Connectivity list of triangles
    points : np.array of float [n_points x 3]
        Points (vertices) of surface mesh
    """
    mesh = triangular_mesh(points[:, 0], points[:, 1], points[:, 2], con, representation='wireframe', opacity=0)
    mesh.mlab_source.dataset.cell_data.scalars = data
    mesh.mlab_source.dataset.cell_data.scalars.name = 'Cell data'
    mesh.mlab_source.update()
    mesh.parent.update()
    mesh2 = pipeline.set_active_attribute(mesh, cell_scalars='Cell data')
    s2 = pipeline.surface(mesh2)
    view(azimuth=-175, elevation=66, distance=100,
         focalpoint=np.array([-24.48263809, -27.14163951,  72.43553454]),
         roll=None, reset_roll=None, figure=None)
