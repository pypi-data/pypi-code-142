import os
import sys 
import numpy as np
from inspect import getsourcefile

import pynibs

# path of create_subject_XXXXX.py file (has to be in subjects root directoy
subject_folder = os.path.split(os.path.abspath(getsourcefile(lambda: 0)))[0]

# subject information
###########################################################################################################
subject_id = 'testsub'
fn_subject_obj = subject_folder + f'/{subject_id}.hdf5'

# mri information
###########################################################################################################
mri = [dict()]

mri[0]['fn_mri_T1'] = subject_folder + f'/mri/0/original/nifti/t1/2_T1_mprage_iso.nii.gz'
mri[0]['fn_mri_T2'] = subject_folder + f'/mri/0/original/nifti/t2/5_T2_cube_iso.nii.gz'
mri[0]['fn_mri_DTI'] = subject_folder + f'/mri/0/original/nifti/dti/7_HB4_diff_64dir_PA0_112.nii.gz'
mri[0]['fn_mri_DTI_rev'] = subject_folder + f'/mri/0/original/nifti/dti/8_HB4_diff_AP1_slice2.nii.gz'
mri[0]['fn_mri_DTI_bvec'] = subject_folder + f'/mri/0/original/nifti/dti/7_HB4_diff_64dir_PA0_112.bvec'
mri[0]['fn_mri_DTI_bval'] = subject_folder + f'/mri/0/original/nifti/dti/7_HB4_diff_64dir_PA0_112.bval'
mri[0]['dti_readout_time'] = '0.08214'
mri[0]['dti_phase_direction'] = 'y'

# mesh information
###########################################################################################################
mesh = {'charm_refm1_sm': dict(), 'headreco': dict(), 'headreco_refined_m1': dict()}

mesh['charm_refm1_sm']['info'] = 'charm --v 1.0 (simnibs 4.0 beta)'
mesh['charm_refm1_sm']['approach'] = 'charm'
mesh['charm_refm1_sm']['mesh_folder'] = os.path.join(subject_folder, 'testsub/mesh', 'charm_refm1_sm')
mesh['charm_refm1_sm']['vertex_density'] = None
mesh['charm_refm1_sm']['fn_mesh_msh'] = os.path.join(mesh['charm_refm1_sm']['mesh_folder'] ,  f'm2m_{subject_id}', f'{subject_id}.msh')
mesh['charm_refm1_sm']['fn_mesh_hdf5'] = os.path.join(mesh['charm_refm1_sm']['mesh_folder'] , f'm2m_{subject_id}', f'{subject_id}.hdf5')
mesh['charm_refm1_sm']['fn_tensor_vn'] = f'm2m_{subject_id}/DTI_coregT1_tensor.nii.gz'
mesh['charm_refm1_sm']['mri_idx'] = 0
mesh['charm_refm1_sm']['fn_mri_conform'] = f"m2m_{subject_id}/T1.nii.gz"

mesh['charm_refm1_sm']['fn_lh_wm'] = None
mesh['charm_refm1_sm']['fn_rh_wm'] = None
mesh['charm_refm1_sm']['fn_lh_gm'] = None
mesh['charm_refm1_sm']['fn_rh_gm'] = None
mesh['charm_refm1_sm']['fn_lh_gm_curv'] = None
mesh['charm_refm1_sm']['fn_rh_gm_curv'] = None
mesh['charm_refm1_sm']['fn_lh_midlayer'] = f'm2m_{subject_id}/surfaces/lh.central.gii'
mesh['charm_refm1_sm']['fn_rh_midlayer'] = f'm2m_{subject_id}/surfaces/rh.central.gii'
mesh['charm_refm1_sm']['smooth_skin'] = .8
mesh['charm_refm1_sm']['refinement_roi'] = 'midlayer_m1s1pmd'
mesh['charm_refm1_sm']['refinemement_element_size'] = 1

mesh['headreco']['info'] = 'headreco --v 1.0 (simnibs 3.1)'
mesh['headreco']['approach'] = 'headreco'
mesh['headreco']['mesh_folder'] = os.path.join(subject_folder, 'testsub/mesh', 'headreco')
mesh['headreco']['vertex_density'] = 1.0
mesh['headreco']['fn_mesh_msh'] = os.path.join(mesh['headreco']['mesh_folder'] ,  f'{subject_id}.msh')
mesh['headreco']['fn_mesh_hdf5'] = os.path.join(mesh['headreco']['mesh_folder'] , f'{subject_id}.hdf5')
mesh['headreco']['fn_tensor_vn'] = f'd2c_{subject_id}_PA/CTI_vn_tensor.nii'
mesh['headreco']['mri_idx'] = 0
mesh['headreco']['fn_lh_wm'] = None
mesh['headreco']['fn_rh_wm'] = None
mesh['headreco']['fn_lh_gm'] = None
mesh['headreco']['fn_rh_gm'] = None
mesh['headreco']['fn_lh_gm_curv'] = None
mesh['headreco']['fn_rh_gm_curv'] = None
mesh['headreco']['fn_lh_midlayer'] = f'fs_{subject_id}/surf/lh.central'
mesh['headreco']['fn_rh_midlayer'] = f'fs_{subject_id}/surf/rh.central'

mesh['headreco_refined_m1']['info'] = 'headreco --v 1.0 (simnibs 3.1)'
mesh['headreco_refined_m1']['approach'] = 'headreco'
mesh['headreco_refined_m1']['mesh_folder'] = os.path.join(subject_folder, 'testsub/mesh', 'headreco_refined_m1')
mesh['headreco_refined_m1']['vertex_density'] = 1.0
mesh['headreco_refined_m1']['center'] = [-41.33, -49.37, 73.78]
mesh['headreco_refined_m1']['radius'] = 35
mesh['headreco_refined_m1']['element_size'] = 0.4
mesh['headreco_refined_m1']['refine_domains'] = ["wm", "gm", "csf"]
mesh['headreco_refined_m1']['fn_mesh_msh'] = os.path.join(mesh['headreco_refined_m1']['mesh_folder'], f"{subject_id}.msh")
mesh['headreco_refined_m1']['fn_mesh_hdf5'] = os.path.join(mesh['headreco_refined_m1']['mesh_folder'], f"{subject_id}.hdf5")
mesh['headreco_refined_m1']['fn_tensor_vn'] = f"d2c_{subject_id}/dti_results_T1space/DTI_conf_tensor.nii.gz"
mesh['headreco_refined_m1']['mri_idx'] = 0
mesh['headreco_refined_m1']['fn_mri_conform'] = f"{subject_id}_T1fs_conform.nii.gz"
mesh['headreco_refined_m1']['smooth_domains'] = ['skin']

mesh['headreco_refined_m1']['fn_lh_wm'] = None
mesh['headreco_refined_m1']['fn_rh_wm'] = None
mesh['headreco_refined_m1']['fn_lh_gm'] = None
mesh['headreco_refined_m1']['fn_rh_gm'] = None
mesh['headreco_refined_m1']['fn_lh_gm_curv'] = None
mesh['headreco_refined_m1']['fn_rh_gm_curv'] = None
mesh['headreco_refined_m1']['fn_lh_midlayer'] = f"fs_{subject_id}/surf/lh.central"
mesh['headreco_refined_m1']['fn_rh_midlayer'] = f"fs_{subject_id}/surf/rh.central"

# roi information (first index: mesh, second index: roi)
###########################################################################################################
roi = {'headreco': {'midlayer_lh_rh':dict(), 'midlayer_m1s1pmd':dict()},
       'headreco_refined_m1': {'midlayer_lh_rh':dict(), 'midlayer_m1s1pmd':dict(), 'midlayer_m1s1pmd_refined': dict()},
       'charm_refm1_sm': {'midlayer_lh_rh': dict(), 'midlayer_m1s1pmd': dict()}}

roi['charm_refm1_sm']['midlayer_lh_rh']['type'] = 'surface'
roi['charm_refm1_sm']['midlayer_lh_rh']['info'] = 'freesurfer lh + rh whole brain midlayer'
roi['charm_refm1_sm']['midlayer_lh_rh']['gm_surf_fname'] = [mesh['charm_refm1_sm']['fn_lh_gm'], mesh['charm_refm1_sm']['fn_rh_gm']]
roi['charm_refm1_sm']['midlayer_lh_rh']['wm_surf_fname'] = [mesh['charm_refm1_sm']['fn_lh_wm'], mesh['charm_refm1_sm']['fn_rh_wm']]
roi['charm_refm1_sm']['midlayer_lh_rh']['midlayer_surf_fname'] = [mesh['charm_refm1_sm']['fn_lh_midlayer'], mesh['charm_refm1_sm']['fn_rh_midlayer']]
roi['charm_refm1_sm']['midlayer_lh_rh']['delta'] = 0.5
roi['charm_refm1_sm']['midlayer_lh_rh']['refine'] = False
roi['charm_refm1_sm']['midlayer_lh_rh']['X_ROI'] = None
roi['charm_refm1_sm']['midlayer_lh_rh']['Y_ROI'] = None
roi['charm_refm1_sm']['midlayer_lh_rh']['Z_ROI'] = None
roi['charm_refm1_sm']['midlayer_lh_rh']['layer'] = 3
roi['charm_refm1_sm']['midlayer_lh_rh']['fn_mask'] = None
roi['charm_refm1_sm']['midlayer_lh_rh']['fn_mask_avg'] = None

roi['charm_refm1_sm']['midlayer_m1s1pmd']['type'] = 'surface'
roi['charm_refm1_sm']['midlayer_m1s1pmd']['info'] = 'freesurfer PMd, M1 and somatosensory cortex'
roi['charm_refm1_sm']['midlayer_m1s1pmd']['gm_surf_fname'] = mesh['charm_refm1_sm']['fn_lh_gm']
roi['charm_refm1_sm']['midlayer_m1s1pmd']['wm_surf_fname'] = mesh['charm_refm1_sm']['fn_lh_wm']
roi['charm_refm1_sm']['midlayer_m1s1pmd']['midlayer_surf_fname'] = mesh['charm_refm1_sm']['fn_lh_midlayer']
roi['charm_refm1_sm']['midlayer_m1s1pmd']['delta'] = 0.5
roi['charm_refm1_sm']['midlayer_m1s1pmd']['refine'] = False
roi['charm_refm1_sm']['midlayer_m1s1pmd']['X_ROI'] = None
roi['charm_refm1_sm']['midlayer_m1s1pmd']['Y_ROI'] = None
roi['charm_refm1_sm']['midlayer_m1s1pmd']['Z_ROI'] = None
roi['charm_refm1_sm']['midlayer_m1s1pmd']['layer'] = 3
roi['charm_refm1_sm']['midlayer_m1s1pmd']['fn_mask'] = f"roi/midlayer_m1s1pmd/mask_{subject_id}m1pmdss.mgh"
roi['charm_refm1_sm']['midlayer_m1s1pmd']['fn_mask_avg'] = '/lefthandknob_M1S1PMd.overlay'
roi['charm_refm1_sm']['midlayer_m1s1pmd']['hemisphere'] = "lh"

roi['headreco']['midlayer_lh_rh']['type'] = 'surface'
roi['headreco']['midlayer_lh_rh']['info'] = 'freesurfer lh + rh whole brain midlayer'
roi['headreco']['midlayer_lh_rh']['gm_surf_fname'] = [mesh['headreco']['fn_lh_gm'], mesh['headreco']['fn_rh_gm']]
roi['headreco']['midlayer_lh_rh']['wm_surf_fname'] = [mesh['headreco']['fn_lh_wm'], mesh['headreco']['fn_rh_wm']]
roi['headreco']['midlayer_lh_rh']['midlayer_surf_fname'] = [mesh['headreco']['fn_lh_midlayer'], mesh['headreco']['fn_rh_midlayer']]
roi['headreco']['midlayer_lh_rh']['delta'] = 0.5
roi['headreco']['midlayer_lh_rh']['refine'] = False
roi['headreco']['midlayer_lh_rh']['X_ROI'] = None
roi['headreco']['midlayer_lh_rh']['Y_ROI'] = None
roi['headreco']['midlayer_lh_rh']['Z_ROI'] = None
roi['headreco']['midlayer_lh_rh']['layer'] = 3
roi['headreco']['midlayer_lh_rh']['fn_mask'] = None
roi['headreco']['midlayer_lh_rh']['fn_mask_avg'] = None

roi['headreco']['midlayer_m1s1pmd']['type'] = 'surface'
roi['headreco']['midlayer_m1s1pmd']['info'] = 'freesurfer PMd, M1 and somatosensory cortex'
roi['headreco']['midlayer_m1s1pmd']['gm_surf_fname'] = mesh['headreco']['fn_lh_gm']
roi['headreco']['midlayer_m1s1pmd']['wm_surf_fname'] = mesh['headreco']['fn_lh_wm']
roi['headreco']['midlayer_m1s1pmd']['midlayer_surf_fname'] = mesh['headreco']['fn_lh_midlayer']
roi['headreco']['midlayer_m1s1pmd']['delta'] = 0.5
roi['headreco']['midlayer_m1s1pmd']['refine'] = False
roi['headreco']['midlayer_m1s1pmd']['X_ROI'] = None
roi['headreco']['midlayer_m1s1pmd']['Y_ROI'] = None
roi['headreco']['midlayer_m1s1pmd']['Z_ROI'] = None
roi['headreco']['midlayer_m1s1pmd']['layer'] = 3
roi['headreco']['midlayer_m1s1pmd']['fn_mask'] = f"roi/midlayer_m1s1pmd/mask_{subject_id}m1pmdss.mgh"
roi['headreco']['midlayer_m1s1pmd']['fn_mask_avg'] = '/masks/lefthandknob_M1S1PMd.overlay'
roi['headreco']['midlayer_m1s1pmd']['hemisphere'] = "lh"

roi['headreco_refined_m1']['midlayer_lh_rh']['type'] = 'surface'
roi['headreco_refined_m1']['midlayer_lh_rh']['info'] = 'freesurfer lh + rh whole brain midlayer'
roi['headreco_refined_m1']['midlayer_lh_rh']['gm_surf_fname'] = [mesh['headreco_refined_m1']['fn_lh_gm'], mesh['headreco_refined_m1']['fn_rh_gm']]
roi['headreco_refined_m1']['midlayer_lh_rh']['wm_surf_fname'] = [mesh['headreco_refined_m1']['fn_lh_wm'], mesh['headreco_refined_m1']['fn_rh_wm']]
roi['headreco_refined_m1']['midlayer_lh_rh']['midlayer_surf_fname'] = [mesh['headreco_refined_m1']['fn_lh_midlayer'], mesh['headreco_refined_m1']['fn_rh_midlayer']]
roi['headreco_refined_m1']['midlayer_lh_rh']['refine'] = False
roi['headreco_refined_m1']['midlayer_lh_rh']['delta'] = 0.5
roi['headreco_refined_m1']['midlayer_lh_rh']['X_ROI'] = None
roi['headreco_refined_m1']['midlayer_lh_rh']['Y_ROI'] = None
roi['headreco_refined_m1']['midlayer_lh_rh']['Z_ROI'] = None
roi['headreco_refined_m1']['midlayer_lh_rh']['layer'] = 3
roi['headreco_refined_m1']['midlayer_lh_rh']['fn_mask'] = None
roi['headreco_refined_m1']['midlayer_lh_rh']['fn_mask_avg'] = None

roi['headreco_refined_m1']['midlayer_m1s1pmd']['type'] = 'surface'
roi['headreco_refined_m1']['midlayer_m1s1pmd']['info'] = 'freesurfer PMd, M1 and somatosensory cortex'
roi['headreco_refined_m1']['midlayer_m1s1pmd']['gm_surf_fname'] = mesh['headreco_refined_m1']['fn_lh_gm']
roi['headreco_refined_m1']['midlayer_m1s1pmd']['wm_surf_fname'] = mesh['headreco_refined_m1']['fn_lh_wm']
roi['headreco_refined_m1']['midlayer_m1s1pmd']['midlayer_surf_fname'] = mesh['headreco_refined_m1']['fn_lh_midlayer']
roi['headreco_refined_m1']['midlayer_m1s1pmd']['refine'] = False
roi['headreco_refined_m1']['midlayer_m1s1pmd']['delta'] = 0.5
roi['headreco_refined_m1']['midlayer_m1s1pmd']['X_ROI'] = None
roi['headreco_refined_m1']['midlayer_m1s1pmd']['Y_ROI'] = None
roi['headreco_refined_m1']['midlayer_m1s1pmd']['Z_ROI'] = None
roi['headreco_refined_m1']['midlayer_m1s1pmd']['layer'] = 3
roi['headreco_refined_m1']['midlayer_m1s1pmd']['fn_mask'] = f"roi/midlayer_m1s1pmd/mask_{subject_id}m1pmdss.mgh"
roi['headreco_refined_m1']['midlayer_m1s1pmd']['fn_mask_avg'] = '//masks/lefthandknob_M1S1PMd.overlay'
roi['headreco_refined_m1']['midlayer_m1s1pmd']['hemisphere'] = "lh"

roi['headreco_refined_m1']['midlayer_m1s1pmd_refined']['type'] = 'surface'
roi['headreco_refined_m1']['midlayer_m1s1pmd_refined']['info'] = 'freesurfer PMd, M1 and somatosensory cortex'
roi['headreco_refined_m1']['midlayer_m1s1pmd_refined']['gm_surf_fname'] = mesh['headreco_refined_m1']['fn_lh_gm']
roi['headreco_refined_m1']['midlayer_m1s1pmd_refined']['wm_surf_fname'] = mesh['headreco_refined_m1']['fn_lh_wm']
roi['headreco_refined_m1']['midlayer_m1s1pmd_refined']['midlayer_surf_fname'] = mesh['headreco_refined_m1']['fn_lh_midlayer']
roi['headreco_refined_m1']['midlayer_m1s1pmd_refined']['refine'] = True
roi['headreco_refined_m1']['midlayer_m1s1pmd_refined']['delta'] = 0.5
roi['headreco_refined_m1']['midlayer_m1s1pmd_refined']['X_ROI'] = None
roi['headreco_refined_m1']['midlayer_m1s1pmd_refined']['Y_ROI'] = None
roi['headreco_refined_m1']['midlayer_m1s1pmd_refined']['Z_ROI'] = None
roi['headreco_refined_m1']['midlayer_m1s1pmd_refined']['layer'] = 3
roi['headreco_refined_m1']['midlayer_m1s1pmd_refined']['fn_mask'] = f"roi/midlayer_m1s1pmd/mask_{subject_id}m1pmdss.mgh"
roi['headreco_refined_m1']['midlayer_m1s1pmd_refined']['fn_mask_avg'] = '//masks/lefthandknob_M1S1PMd.overlay'
roi['headreco_refined_m1']['midlayer_m1s1pmd_refined']['hemisphere'] = "lh"

# experiment information
###########################################################################################################
exp = {'TMS_localite': dict(), 'TMS_ant': dict(), 'TMS_brainsight': dict()}

exp['TMS_localite']['info'] = ['TMS-MEP template Localite (MPI)']
exp['TMS_localite']['date'] = ['XX/XX/20XX']
exp['TMS_localite']['nnav_system'] = 'Localite'
exp['TMS_localite']['fn_tms_nav'] = [[subject_folder + '...xml', subject_folder + '...xml']]
exp['TMS_localite']['fn_data'] = [[subject_folder + '/exp/0/mep/...cfs']]
exp['TMS_localite']['fn_intensity'] = None
exp['TMS_localite']['mep_onsets'] = [[0]]
exp['TMS_localite']['fn_exp_csv'] = [subject_folder + '/exp/0/experiment.csv']
exp['TMS_localite']['fn_exp_hdf5'] = [subject_folder + '/exp/0/experiment.hdf5']
exp['TMS_localite']['fn_coil'] = [['.../MagStim_Alpha_Coil_70mm_Fig8.nii.gz']]
exp['TMS_localite']['fn_mri_nii'] = [[subject_folder + '/exp/0/..._conform.nii']]
exp['TMS_localite']['cond'] = [['']]
exp['TMS_localite']['tms_pulse_time'] = None
exp['TMS_localite']['experimenter'] = ''
exp['TMS_localite']['mep_fit_info'] = ['']
exp['TMS_localite']['incidents'] = ['']
exp['TMS_localite']['postproc'] = [dict()]
exp['TMS_localite']['postproc'][0]['info'] = ' '
exp['TMS_localite']['postproc'][0]['cmd'] = ' '

exp['TMS_ant']['info'] = ['TMS-MEP-EEG template (ANT)']
exp['TMS_ant']['date'] = ['XX/XX/20XX']
exp['TMS_ant']['nnav_system'] = 'Visor'
exp['TMS_ant']['fn_data'] = [[subject_folder + '/exp/2/...cnt']]
exp['TMS_ant']['fn_exp_hdf5'] = [subject_folder + '/exp/2/experiment.hdf5']
exp['TMS_ant']['fn_coil'] = [['.../MagStim_Alpha_Coil_70mm_Fig8.nii.gz']]
exp['TMS_ant']['fn_mri_nii'] = [[subject_folder + '/exp/2/..._conform.nii']]
exp['TMS_ant']['fn_visor_cnt'] = [subject_folder + '/exp/2/...pos.cnt']
exp['TMS_ant']['fn_visor_calibration'] = [subject_folder + '/exp/2/...calibration.xml']
exp['TMS_ant']['fn_eeg_cnt'] = [subject_folder + '/exp/2/eeg/...cnt']
exp['TMS_ant']['eeg_channels'] = ['all']
exp['TMS_ant']['fn_emg_cnt'] = [subject_folder + '/exp/2/emg/...cnt']
exp['TMS_ant']['emg_channels'] = [0]
exp['TMS_ant']['emg_max_duration'] = [10]
exp['TMS_ant']['eeg_max_duration'] = [10]
exp['TMS_ant']['emg_trigger_value'] = ['4']
exp['TMS_ant']['eeg_trigger_value'] = ['1']
exp['TMS_ant']['cond'] = [['M1_random']]
exp['TMS_ant']['tms_pulse_time'] = None
exp['TMS_ant']['experimenter'] = ' '
exp['TMS_ant']['mep_fit_info'] = [' ']
exp['TMS_ant']['incidents'] = [' ']
exp['TMS_ant']['fiducal_corr'] = [[0,0,0]]  # x,y,z in mm

exp['TMS_brainsight']['info'] = ['TMS-MEP-EEG template (Brainsight)']
exp['TMS_brainsight']['date'] = ['09/03/20222']
exp['TMS_brainsight']['nnav_system'] = 'Brainsight'
exp['TMS_brainsight']['fn_data'] = [subject_folder + '/Data_testsub.txt']
exp['TMS_brainsight']['fn_exp_hdf5'] = [subject_folder + '/exp/random/experiment.hdf5']
exp['TMS_brainsight']['fn_coil'] = [['.../Magstim_D70_AFC_force_sensor.ccd.nii.gz']]
exp['TMS_brainsight']['fn_mri_nii'] = [[subject_folder + '/exp/random/testsub_T1.nii.gz']]
exp['TMS_brainsight']['cond'] = [['M1_random']]
exp['TMS_brainsight']['tms_pulse_time'] = None
exp['TMS_brainsight']['experimenter'] = 'Zijian'
exp['TMS_brainsight']['mep_fit_info'] = [' ']
exp['TMS_brainsight']['incidents'] = [' ']
exp['TMS_brainsight']['fiducal_corr'] = [[0,0,0]]  # x,y,z in mm

# add plot settings
###########################################################################################################
ps = []

ps.append(pynibs.create_plot_settings_dict(plotfunction_type='surface_vector_plot'))
ps[0]['info'] = ' '
ps[0]['plot_function'] = 'surface_vector_plot'
ps[0]['fname_in'] = '..._data.xdmf'
ps[0]['fname_png'] = '...png'
ps[0]['png_resolution'] = 1.0
ps[0]['quantity'] = [' ']
ps[0]['vlabels'] = None
ps[0]['vscales'] = None
ps[0]['datarange'] = [None, None]
ps[0]['domain_label'] = 'tissue_type'
ps[0]['domain_IDs'] = 0
ps[0]['colorbar_label'] = ' '
ps[0]['colorbar_position'] = [0.45, -0.05]
ps[0]['colorbar_orientation'] = 'Horizontal'
ps[0]['colorbar_aspectratio'] = 20
ps[0]['colorbar_titlefontsize'] = 12
ps[0]['colorbar_labelfontsize'] = 12
ps[0]['colorbar_labelformat'] = '%-#6.1f'
ps[0]['colorbar_numberoflabels'] = 5
ps[0]['colorbar_labelcolor'] = [0, 0, 0]
ps[0]['view'] = [[-332.040630013204, -16.8948837495393, 256.721941018442],
                 [-35.3111635316966, -13.6999528376981, 36.4196465112876],
                 [0.588834647614276, -0.167617710066906, 0.790682022712606],
                 [30, 0, 0]]
ps[0]['interpolate'] = True
ps[0]['edges'] = False
ps[0]['axes'] = False
ps[0]['colormap'] = 'Rainbow Blended White'
ps[0]['opacitymap'] = None
ps[0]['vscale_mode'] = ['off']
ps[0]['vector_mode'] = {'Every Nth Point': 10}
ps[0]['vcolor'] = None
ps[0]['background_color'] = np.array([1, 1, 1])
ps[0]['viewsize'] = np.array([1000, 1000])

# save subject information in .hdf5 file
###########################################################################################################
pynibs.save_subject_hdf5(fname=fn_subject_obj,
                          mri_dict=mri,
                          mesh_dict=mesh,
                          roi_dict=roi,
                          exp_dict=exp,
                          ps_dict=ps,
                          subject_id=subject_id,
                          subject_folder=subject_folder
                         )

print(f'Created subject .hdf5 file: {fn_subject_obj}')
