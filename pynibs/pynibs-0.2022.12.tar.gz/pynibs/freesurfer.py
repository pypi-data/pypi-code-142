"""
This holds methods to interact with FreeSurfer ([1]_), for example to translate FreeSurfer files into Paraview readable
.vtk files.

References
----------
.. [1] Dale, A.M., Fischl, B., Sereno, M.I., 1999. Cortical surface-based analysis. I. Segmentation and surface
   reconstruction. Neuroimage 9, 179-194.
"""
import os
import h5py
import shutil
import meshio
import nibabel
import platform
import subprocess
import numpy as np
import nibabel as nib
import pynibs


def read_curv_data(fname_curv, fname_inf, raw=False):
    """
    Read curvature data provided by FreeSurfer with optional normalization.

    Parameters
    ----------
    fname_curv : str
        Filename of the FreeSurfer curvature file (e.g. ?h.curv), contains curvature data in nodes
        can be found in mri2mesh proband folder: ``proband_ID/fs_ID/surf/?h.curv``.
    fname_inf : str
        Filename of inflated brain surface (e.g. ``?h.inflated``), contains points and connectivity data of surface
        can be found in mri2mesh proband folder: ``proband_ID/fs_ID/surf/?h.inflated``.
    raw : bool
        If raw-data is returned or if the data is normalized to -1 for neg. and +1 for pos. curvature.

    Returns
    -------
    curv : np.ndarray of float or int
        Curvature data in element centers.
    """

    # load curvature data
    curv_points = nibabel.freesurfer.io.read_morph_data(fname_curv)

    # load inflated brain surface data
    points_inf, con_inf = nibabel.freesurfer.read_geometry(fname_inf)

    # interpolate point data to element centers
    curv = pynibs.data_nodes2elements(curv_points, con_inf)

    # normalize curvature data, optional
    if not raw:
        curv[curv > 0] = 1
        curv[curv < 0] = -1

    return curv


def make_group_average(subjects=None, subject_dir=None, average=None, hemi="lh", template="mytemplate", steps=3,
                       n_cpu=2, average_dir=None):
    """
    Creates a group average from scratch, based on one subject. This prevents for example the fsaverage problems of
    large elements at M1, etc.
    This is an implemntation of [2]_ 'Creating a registration template from scratch (GW)'.

    References
    ----------
    .. [2] https://surfer.nmr.mgh.harvard.edu/fswiki/SurfaceRegAndTemplates

    Parameters
    ----------
    subjects : list of str
        List of FreeSurfer subjects names.
    subject_dir : str
        Temporary subject directory of FreeSurfer (symlinks of subjects will be generated in there and average
        template will be temporarily stored before it is copied to ``average_dir``).
    average: str, default: ``subjects[0]``
        Which subject to base new average template on.
    hemi : str, default: 'lh'
        Which hemisphere: ``lh`` or ``rh``.

        .. deprecated:: 0.0.1
            Don't use any more.
    template : str, default: 'mytemplate'
        Basename of new template.
    steps : int, default: 2
        Number of iterations.
    n_cpu : int, default: 4
        How many cores for multithreading.
    average_dir : str
        Path to directory where average template will be stored,
        e.g. ``probands/avg_template_15/mesh/0/fs_avg_template_15``.

    Returns
    -------
    <File> : .tif file
        ``SUBJECT_DIR/TEMPLATE*.tif``, TEMPLATE0.tif based on AVERAGE, rest on all subjects.
    <File> : .myreg file
        ``SUBJECT_DIR/SUBJECT*/surf/HEMI.sphere.myreg*``.
    <File> : .tif file
        Subject wise sphere registration based on ``TEMPLATE*.tif``.
    """
    subject_names = [os.path.split(subjects[i])[1] for i in range(len(subjects))]

    # define $SUBJECT_DIR of FREESURFER
    if not os.path.exists(subject_dir):
        print(('Creating $SUBJECTS_DIR in {}'.format(subject_dir)))
        os.makedirs(subject_dir)
    print(('Set environment variable of FreeSurfer SUBJECTS_DIR={}'.format(subject_dir)))
    os.putenv('SUBJECTS_DIR', subject_dir)

    # make symlinks of subjects in $SUBJECT_DIR
    for i, subject in enumerate(subjects):
        if not os.path.exists(os.path.join(subject_dir, subject_names[i])):
            print(('Generating symlink of subject {} in {}'.format(subject_names[i], subject_dir)))
            pynibs.bash('ln -s ' + subject + ' ' + subject_dir)

    os.chdir(subject_dir)

    if not average:
        average = subjects[0]

    print("Creating initial template")
    "mris_make_template lh sphere fs_15484.08 ./templates.tif"

    command = "mris_make_template {} sphere {} lh{}0.tif".format("lh", os.path.split(average)[1], template)
    os.system(command)
    command = "mris_make_template {} sphere {} rh{}0.tif".format("rh", os.path.split(average)[1], template)
    os.system(command)

    processes = set()
    for i in range(steps):
        command = "mris_register"
        print("\n\nStep {}".format(i))
        print("############################################################################################")
        # start all subjects registrations to .tif* in parallel
        for subject in subjects:
            # print "{}/surf/{}.sphere {}{}.tif {}.sphere.myreg{}".format(subject, hemi, template, i, hemi, i)
            # print [command, "{}/surf/{}.sphere {}{}.tif {}.sphere.myreg{}".format(subject,
            # hemi, template, i, hemi, i)]
            processes.add(subprocess.Popen(
                    [f'{command} '
                     f'{os.path.split(subject)[1]}{os.sep}surf{os.sep}lh.sphere lh{template}{i}.tif '
                     f'{"lh"}.sphere.{template}{i}'],
                    shell=True))
            processes.add(subprocess.Popen(
                    [f"{command} "
                     f"{os.path.split(subject)[1]}{os.sep}surf{os.sep}rh.sphere rh{template}{i}.tif "
                     f"{'rh'}.sphere.{template}{i}"],
                    shell=True))

            # check if n_cpu processes are reached
            if len(processes) >= n_cpu:
                os.wait()
                processes.difference_update([p for p in processes if p.poll() is not None])

        while len(processes) > 0:
            os.wait()
            processes.difference_update([p for p in processes if p.poll() is not None])

        short_subjects = [os.path.split(subject)[1] for subject in subjects]
        print("        making template for step {}".format(i))
        command = f"mris_make_template {'rh'} sphere.{template}{i} {' '.join(short_subjects)} " \
                  f"rh{template}{i + 1}.tif"
        print(command)
        os.system(command)

        command = f"mris_make_template {'lh'} sphere.{template}{i} {' '.join(short_subjects)} " \
                  f"lh{template}{i + 1}.tif"
        print(command)
        os.system(command)

        print("##################### Iteration {} done. #####################\n".format(i))

    print('Creating average surfaces and volumes of average subject')
    make_average_subject(subjects=subjects,
                         subject_dir=subject_dir,
                         average_dir=average_dir,
                         fn_reg='sphere.{}{}'.format(template, steps - 1))


def make_average_subject(subjects, subject_dir, average_dir, fn_reg='sphere.reg'):
    """
    Generates the average template from a list of subjects using the FreeSurfer average.

    Parameters
    ----------
    subjects : list of str
        Paths of subjects directories, where the FreeSurfer files are located,
        e.g. for simnibs mri2mesh ``.../fs_SUBJECT_ID``.
    subject_dir : str
        Temporary subject directory of FreeSurfer (symlinks of subjects will be generated in there and average
        template will be temporarily stored before it is copied to ``average_dir``).
    average_dir : str
        path to directory where average template will be stored,
        e.g. probands/avg_template_15/mesh/0/fs_avg_template_15.
    fn_reg : str, default: 'sphere.reg' --> ?h.sphere.reg>
        Filename suffix of FreeSurfer registration file containing registration information to template.

    Returns
    -------
    <Files> : .tif and .reg files
        Average template in average_dir and registered curvature files, ``?h.sphere.reg`` in subjects/surf folders.
    """

    subject_names = [os.path.split(subjects[i])[1] for i in range(len(subjects))]

    # check for right operating system
    if platform.system() != 'Linux':
        raise OSError('Average template can only be generated with linux because of FreeSurfer requirements.')

    # define $SUBJECT_DIR of FREESURFER
    if not os.path.exists(subject_dir):
        print(('Creating $SUBJECTS_DIR in {}'.format(subject_dir)))
        os.makedirs(subject_dir)
    print(('Set environment variable of FreeSurfer SUBJECTS_DIR={}'.format(subject_dir)))
    os.putenv('SUBJECTS_DIR', subject_dir)

    # make symlinks of subjects in $SUBJECT_DIR
    for i, subject in enumerate(subjects):
        if not os.path.exists(os.path.join(subject_dir, subject_names[i])):
            print(('Generating symlink of subject {} in {}'.format(subject_names[i], subject_dir)))
            pynibs.bash('ln -s ' + subject + ' ' + subject_dir)

    # make average template
    if os.path.exists(f'{subject_dir}{os.sep}avg_template'):
        shutil.rmtree(f'{subject_dir}{os.sep}avg_template')
    print(('Generating average subject in {}/avg_template'.format(subject_dir)))
    print('==============================================')
    command = 'make_average_subject ' \
              '--out avg_template ' \
              ' --subjects ' + " ".join(subject_names) + \
              ' --surf-reg ' + fn_reg

    os.system(command)

    # copy average template to average_dir
    print(('Moving average template to {}'.format(average_dir)))
    os.system('mv $SUBJECTS_DIR/avg_template ' + average_dir)


def data_sub2avg(fn_subject_obj, fn_average_obj, hemisphere, fn_in_hdf5_data, data_hdf5_path, data_label,
                 fn_out_hdf5_geo, fn_out_hdf5_data, mesh_idx=0, roi_idx=0, subject_data_in_center=True,
                 data_substitute=-1, verbose=True, replace=True, reg_fn="sphere.reg"):
    """
    Maps the data from the subject space to the average template. If the data is given only in an ROI, the data is
    mapped to the whole brain surface.

    Parameters
    ----------
    fn_subject_obj : str
        Filename of subject object .hdf5 file (incl. path),
        e.g. ``.../probands/subjectID/subjectID.hdf5``
    fn_average_obj : str
        Filename of average template object .pkl file (incl. path),
        e.g. ``.../probands/avg_template/avg_template.hdf5``.
    hemisphere : str
        Define hemisphere to work on (``'lh'`` or ``'rh'`` for left or right hemisphere, respectively).
    fn_in_hdf5_data : str
        Filename of .hdf5 data input file containing the subject data.
    data_hdf5_path : str
        Path in .hdf5 data file where data is stored (e.g. ``'/data/tris/'``).
    data_label : str or list of str
        Label of datasets contained in hdf5 input file to map.
    fn_out_hdf5_geo : str
        Filename of .hdf5 geo output file containing the geometry information.
    fn_out_hdf5_data : str
        Filename of .hdf5 data output file containing the mapped data.
    mesh_idx : int
        Index of mesh used in the simulations.
    roi_idx : int
        Index of region of interest used in the simulations.
    subject_data_in_center : bool, default: True
        Specify if the data is given in the center of the triangles or in the nodes.
    data_substitute : float
        Data substitute with this number for all points outside the ROI mask
    verbose : bool
        Verbose output (Default: True)
    replace : bool
        Replace output files (Default: True)
    reg_fn : str
        Sphere.reg fn

    Returns
    -------
    <Files> : .hdf5 files
        Geometry and corresponding data files to plot with Paraview:

        * fn_out_hdf5_geo.hdf5: geometry file containing the geometry information of the average template
        * fn_out_hdf5_data.hdf5: geometry file containing the data
    """

    subject = pynibs.load_subject(fname=fn_subject_obj)
    average = pynibs.load_subject(fname=fn_average_obj)

    mesh_folder_avg = average.mesh["0"]["mesh_folder"]
    mesh_folder_sub = subject.mesh[mesh_idx]["mesh_folder"]

    fn_sub_gm = subject.mesh[mesh_idx]['fn_' + hemisphere + '_gm']
    fn_sub_wm = subject.mesh[mesh_idx]['fn_' + hemisphere + '_wm']
    fn_avg_gm = average.mesh[mesh_idx]['fn_' + hemisphere + '_gm']
    fn_avg_wm = average.mesh[mesh_idx]['fn_' + hemisphere + '_wm']

    # freesurfer folder, e.g.: /data/pt_01756/probands/subject[i].id + '/mesh/0/fs_' + subject[i].id
    subject_dir = os.path.split(os.path.split(fn_sub_gm)[0])[0]
    average_dir = os.path.split(os.path.split(fn_avg_gm)[0])[0]

    # filename of mapped subject data in nodes in .curv format for freesurfer (will be generated)
    fn_data_sub_nodes_mapped_curv = [os.path.join(
            os.path.split(fn_out_hdf5_geo)[0],
            hemisphere + '.' +
            os.path.split(subject_dir)[1] +
            '_' +
            data_label[i] +
            '.curv')
        for i in range(len(data_label))]

    # filename of mapped subject data in nodes on average template in .curv format for freesurfer (will be generated)
    fn_data_sub_nodes_mapped_avg_curv = [os.path.join(
            os.path.split(fn_data_sub_nodes_mapped_curv[i])[0],
            os.path.splitext(os.path.split(fn_data_sub_nodes_mapped_curv[i])[1])[0] +
            '_avg.curv')
        for i in range(len(data_label))]

    if verbose:
        print('> Generating GM/WM surface on average template')
    points_avg, con_avg = pynibs.make_GM_WM_surface(gm_surf_fname=fn_avg_gm,
                                                    wm_surf_fname=fn_avg_wm,
                                                    mesh_folder=mesh_folder_avg,
                                                    delta=subject.roi[mesh_idx][roi_idx]['delta'],
                                                    layer=1)
    files_not_exist = not np.array([os.path.exists(fn_data_sub_nodes_mapped_avg_curv[i]) for
                                    i in range(len(data_label))]).all()

    if files_not_exist or replace:

        # Generate WM/GM surfaces of subject and average template
        if verbose:
            print(("> Reading ROI #{} of subject ...".format(roi_idx)))

        with h5py.File(subject.mesh[mesh_idx]['fn_mesh_hdf5'], 'r') as f:
            points_roi = np.array(f['roi_surface/' + str(roi_idx) + '/node_coord_mid'])
            con_roi = np.array(f['roi_surface/' + str(roi_idx) + '/node_number_list'])

        # Read subject data
        if verbose:
            print(('> Reading subject data: {}'.format(data_label)))
        data_sub = [h5py.File(fn_in_hdf5_data, 'r')[data_hdf5_path + data_label[i]][:] for i in range(len(data_label))]

        # Transform data when given in element centers to nodes
        if subject_data_in_center:
            if verbose:
                print('> Transforming subject data from element centers to nodes')
            # data_sub_nodes = [pynibs.data_elements2nodes(data_sub[i], con_ROI) for i in range(len(data_label))]
            data_sub_nodes = pynibs.data_elements2nodes(data_sub, con_roi)

        else:
            data_sub_nodes = data_sub

        del data_sub

        # map data given in nodes to brain surface since this is needed for mapping the subject data to the avg template
        # (subject space)
        if subject.roi[mesh_idx][roi_idx]['fn_mask']:
            if verbose:
                print('> Mapping point data of ROI to whole brain surface')
            data_sub_nodes_mapped = pynibs.map_data_to_surface(datasets=data_sub_nodes,
                                                               points_datasets=[points_roi] * len(data_sub_nodes),
                                                               con_datasets=[con_roi] * len(data_sub_nodes),
                                                               fname_fsl_gm=os.path.join(mesh_folder_sub, fn_sub_gm),
                                                               fname_fsl_wm=os.path.join(mesh_folder_sub, fn_sub_wm),
                                                               delta=subject.roi[mesh_idx][roi_idx]['delta'],
                                                               input_data_in_center=False,
                                                               return_data_in_center=False,
                                                               data_substitute=data_substitute)
        else:
            data_sub_nodes_mapped = data_sub_nodes

        del data_sub_nodes

        # Saving mapped subject data in nodes to .curv format for freesurfer (subject space)
        if verbose:
            print('> Saving mapped subject data in nodes in .curv format for FreeSurfer')
        for i in range(len(data_label)):
            nibabel.freesurfer.io.write_morph_data(fn_data_sub_nodes_mapped_curv[i], data_sub_nodes_mapped[i])

        # Set $SUBJECT_DIR of freesurfer
        if verbose:
            print(('> Set environment variable of FreeSurfer SUBJECTS_DIR={}'.format(subject_dir)))
        os.putenv('SUBJECTS_DIR', os.path.split(subject_dir)[0])

        # Make temporary symlink of average_dir in subject_dir
        if verbose:
            print("> Generating temporary symlink from average template to $SUBJECTS_DIR")
            fn_avg_template_symlink_dest = os.path.join(os.path.split(subject_dir)[0], os.path.split(average_dir)[1])
            if os.path.exists(fn_avg_template_symlink_dest):
                os.system('rm -f ' + fn_avg_template_symlink_dest)
            os.system('ln -s ' + average_dir + ' ' + fn_avg_template_symlink_dest)

        # map data on it using FreeSurfer
        if verbose:
            print('> Mapping subject data to average template using FreeSurfer mri_surf2surf')
        for i in range(len(data_label)):
            fs_cmd = "mri_surf2surf --srcsubject " + os.path.split(subject_dir)[1] + \
                     " --trgsubject " + os.path.split(average_dir)[1] + \
                     " --srcsurfval " + fn_data_sub_nodes_mapped_curv[i] + \
                     " --trgsurfval " + fn_data_sub_nodes_mapped_avg_curv[i] + \
                     " --hemi " + hemisphere + \
                     " --src_type curv " + \
                     " --trg_type curv " + \
                     " --surfreg " + reg_fn

            os.system(fs_cmd)

    else:
        print(('> Mapped *_avg.curv files found in {}'.format(os.path.split(fn_data_sub_nodes_mapped_avg_curv[0])[0])))

    # read mapped data
    data_avg_nodes_mapped = [0] * len(data_label)
    if verbose:
        print('> Reading mapped data from .curv files')
    for i in range(len(data_label)):
        data_avg_nodes_mapped[i] = nibabel.freesurfer.read_morph_data(fn_data_sub_nodes_mapped_avg_curv[i])

    # transform data from nodes to centers
    data_avg_centers_mapped = [0] * len(data_label)
    if verbose:
        print('> Transforming mapped nodal data to element centers')
    for i in range(len(data_label)):
        data_avg_centers_mapped[i] = pynibs.data_nodes2elements(data_avg_nodes_mapped[i], con_avg)[:, np.newaxis]

    # create .hdf5 geometry file
    if verbose:
        print('> Creating .hdf5 geometry file of mapped data')
    pynibs.write_geo_hdf5_surf(out_fn=fn_out_hdf5_geo, points=points_avg, con=con_avg, replace=True, hdf5_path='/mesh')

    # create .hdf5 data file
    if verbose:
        print('> Creating .hdf5 data files')
    pynibs.write_data_hdf5_surf(data=data_avg_centers_mapped,
                                data_names=data_label,
                                data_hdf_fn_out=fn_out_hdf5_data,
                                geo_hdf_fn=fn_out_hdf5_geo,
                                replace=True)

    if verbose:
        print('> Done.\n')


def freesurfer2vtk(in_fns, out_folder, hem='lh', surf='pial', prefix=None, fs_subject='fsaverage',
                   fs_subjects_dir=None):
    """
    Transform multiple FreeSurfer .mgh files into one .vtk file.
    This can be read with Paraview and others.

    Parameters
    ----------
    in_fns : list of str or str
        Input filenames.
    out_folder : str
        Output folder.
    hem : str, default: 'lh'
        Which hemisphere: ``'lh'`` or ``'rh'``.
    surf : str, default:  'pial'
        Which FreeSurfer surface: ``'pial'``, ``'inflated'``, ...
    prefix : str, optional
        Prefix to add to each filename.
    fs_subject : str, default: 'fsaverage'
        FreeSurfer subject.
    fs_subjects_dir : str, optional
        FreeSurfer subjects directory. If not provided, read from environment.

    Returns
    -------
    <File>: out_folder/{prefix}_{hem}_{surf}.vtk
        One .vtk file with data as overlays from all .mgh files provided
    """
    if not isinstance(in_fns, list):
        in_fns = [in_fns]

    if prefix is not None and not prefix.endswith('_'):
        prefix += '_'

    if fs_subjects_dir is None:
        try:
            fs_subjects_dir = os.environ['SUBJECTS_DIR']
        except KeyError:
            print(f"Freesurfer not loaded and 'fs_subjects_dir' not provided.")

    output_fn = f"{out_folder}/{prefix}{hem}_{surf}.vtk"

    # create a dict with fn as key, data as value. keys will be vtk data array names
    point_data = {}
    for fn in in_fns:
        point_data[os.path.split(fn)[1].replace('.mgh', '')] = nib.load(fn).get_fdata()

    # read FreeSurfer surface mesh
    coords, faces = nib.freesurfer.read_geometry(f"{fs_subjects_dir}/{fs_subject}/surf/{hem}.{surf}")

    # write all dataarrays + mesh geometry into one .vtk
    meshio.Mesh(np.squeeze(coords), [('triangle', faces)], point_data=point_data).write(output_fn)
