import unittest
import pydarm
import numpy as np
import math
import h5py
import os
from pydarm.FIR import (FIRfilter, createFIRfilter,
                        correctFIRfilter, two_tap_zero_filter_response,
                        check_td_vs_fd, check_td_vs_fd_response)


class TestFIRfilter(unittest.TestCase):

    def setUp(self):
        self.advance_array = np.array([ 1.+0.00000000e+00j, -1.+1.22464680e-16j,  1.-2.44929360e-16j,
                                        -1.+3.67394040e-16j,  1.-4.89858720e-16j, -1.+6.12323400e-16j,
                                         1.-7.34788079e-16j, -1.+8.57252759e-16j,  1.-9.79717439e-16j])
        self.delay_array = np.array([ 1.+0.00000000e+00j, -1.-1.22464680e-16j,  1.+2.44929360e-16j,
                                     -1.-3.67394040e-16j,  1.+4.89858720e-16j, -1.-6.12323400e-16j,
                                      1.+7.34788079e-16j, -1.-8.57252759e-16j,  1.+9.79717439e-16j])
        self.delay_samples = 8
        self.df = 1.0
        self.dt = 0.0625
        self.freq_array = np.array([0., 1., 2., 3., 4., 5., 6., 7., 8.])
        self.latency = 0.5
        self.samples_to_HPcorner = 1
        self.samples_to_LPcorner = 0
        self.window = np.array([0.00233883, 0.02623098, 0.09449865, 0.22677684, 0.42285187,
                       0.65247867, 0.85980208, 0.98349415, 0.98349415, 0.85980208,
                       0.65247867, 0.42285187, 0.22677684, 0.09449865, 0.02623098,
                       0.00233883])

    def tearDown(self):
        del self.window
        del self.advance_array
        del self.delay_array
        del self.delay_samples
        del self.df
        del self.dt
        del self.freq_array
        del self.latency
        del self.samples_to_HPcorner
        del self.samples_to_LPcorner

    def test_FIRfilter(self):
        test_FIRfilter = FIRfilter(fNyq=8, dur=1, highpass_fcut=4, lowpass_fcut=None,
                                latency=None, window_type='kaiser', freq_res=3.0)

        self.assertEqual(test_FIRfilter.delay_samples, self.delay_samples)
        self.assertEqual(test_FIRfilter.df, self.df)
        self.assertEqual(test_FIRfilter.dt, self.dt)
        self.assertEqual(test_FIRfilter.latency, self.latency)
        self.assertEqual(test_FIRfilter.samples_to_HPcorner, self.samples_to_HPcorner)
        self.assertEqual(test_FIRfilter.samples_to_LPcorner, self.samples_to_LPcorner)
        self.assertEqual(len(test_FIRfilter.advance_array), len(self.advance_array))
        for n in range(len(self.advance_array)):
            self.assertAlmostEqual(np.abs(test_FIRfilter.advance_array[n]) / np.abs(self.advance_array[n]), 1.0)
            self.assertAlmostEqual(np.angle(test_FIRfilter.advance_array[n], deg=True) - np.angle(self.advance_array[n], deg=True), 0.0)
        self.assertEqual(len(test_FIRfilter.delay_array), len(self.delay_array))
        for n in range(len(self.delay_array)):
            self.assertAlmostEqual(np.abs(test_FIRfilter.delay_array[n]) / np.abs(self.delay_array[n]), 1.0)
            self.assertAlmostEqual(np.angle(test_FIRfilter.delay_array[n], deg=True) - np.angle(self.delay_array[n], deg=True), 0.0)
        self.assertEqual(len(test_FIRfilter.freq_array), len(self.freq_array))
        for n in range(len(self.freq_array)):
            self.assertAlmostEqual(test_FIRfilter.freq_array[n], self.freq_array[n])
        self.assertEqual(len(test_FIRfilter.window), len(self.window))
        for n in range(len(self.window)):
            self.assertAlmostEqual(test_FIRfilter.window[n] / self.window[n], 1.0, places=5)


class TestCreateFIRfilter(unittest.TestCase):

    def setUp(self):
        self.FIRPars = FIRfilter(fNyq=8, dur=1, highpass_fcut=4, lowpass_fcut=None,
                                 latency=None, window_type='kaiser', freq_res=3.0)
        self.config = '''
[metadata]
[interferometer]
[sensing]
x_arm_length = 3994.4704
y_arm_length = 3994.4692
coupled_cavity_optical_gain = 3.22e6
coupled_cavity_pole_frequency = 410.6
detuned_spring_frequency = 4.468
detuned_spring_Q = 52.14
sensing_sign = 1
is_pro_spring = True
anti_aliasing_rate_string = 16k
anti_aliasing_method      = biquad
analog_anti_aliasing_file = test/H1aa.mat, test/H1aa.mat
whitening_mode_names = mode1, mode1
omc_meas_p_trans_amplifier_uncompensated   = 13.7e3, 17.8e3: 13.7e3, 17.8e3
omc_meas_p_whitening_uncompensated_mode1   = 11.346e3, 32.875e3, 32.875e3: 11.521e3, 32.863e3, 32.863e3
super_high_frequency_poles_apparent_delay = 0, 0
gain_ratio = 1, 1
balance_matrix = 1, 1
omc_path_names = A, B
single_pole_approximation_delay_correction = -12e-6
adc_gain = 1, 1
omc_filter_file = test/H1OMC_1239468752.txt
omc_filter_bank = OMC_DCPD_A, OMC_DCPD_B
omc_filter_noncompensating_modules =
omc_filter_gain = 1, 1
omc_front_end_trans_amplifier_compensation = ON, ON
omc_front_end_whitening_compensation_mode1 = ON, ON
'''
        self.known_Cfir = np.array([-6.63850419e+01,  8.93362543e+02,  8.56077110e+04, -2.27887893e+05,
                                    -8.86759535e+05,  1.61591927e+06,  1.23433242e+06, -2.69276290e+06,
                                     1.79904168e+06, -1.74942704e+06,  6.65554086e+05,  9.35475644e+05,
                                    -4.10502392e+05, -8.87882831e+04,  2.10864177e+04,  1.42418753e+02])

    def tearDown(self):
        del self.FIRPars
        del self.config
        del self.known_Cfir

    def test_createFIRfilter(self):
        C = pydarm.sensing.SensingModel(self.config)
        Cf = C.compute_sensing(self.FIRPars.freq_array)
        test_Cfir, test_Cmodel = createFIRfilter(self.FIRPars, Cf)

        for n in range(len(self.known_Cfir)):
            self.assertAlmostEqual(test_Cfir[n] /
                                   self.known_Cfir[n],
                                   1.0)

class TestCorrectFIRfilter(unittest.TestCase):

    def setUp(self):
        self.FIRPars = FIRfilter(fNyq=8, dur=1, highpass_fcut=4, lowpass_fcut=None,
                                 latency=None, window_type='kaiser', freq_res=3.0)
        self.config = '''
[metadata]
[interferometer]
[sensing]
x_arm_length = 3994.4704
y_arm_length = 3994.4692
coupled_cavity_optical_gain = 3.22e6
coupled_cavity_pole_frequency = 410.6
detuned_spring_frequency = 4.468
detuned_spring_Q = 52.14
sensing_sign = 1
is_pro_spring = True
anti_aliasing_rate_string = 16k
anti_aliasing_method      = biquad
analog_anti_aliasing_file = test/H1aa.mat, test/H1aa.mat
omc_meas_p_trans_amplifier_uncompensated   = 13.7e3, 17.8e3: 13.7e3, 17.8e3
whitening_mode_names = mode1, mode1
omc_meas_p_whitening_uncompensated_mode1   = 11.346e3, 32.875e3, 32.875e3: 11.521e3, 32.863e3, 32.863e3
super_high_frequency_poles_apparent_delay = 0, 0
gain_ratio = 1, 1
balance_matrix = 1, 1
omc_path_names = A, B
single_pole_approximation_delay_correction = -12e-6
adc_gain = 1, 1
omc_filter_file = test/H1OMC_1239468752.txt
omc_filter_bank = OMC_DCPD_A, OMC_DCPD_B
omc_filter_noncompensating_modules =
omc_filter_gain = 1, 1
omc_front_end_trans_amplifier_compensation = ON, ON
omc_front_end_whitening_compensation_mode1 = ON, ON
'''

        self.known_Corfir = np.array([-169801.88070367-2.19120483e+02j,
                               -698906.37183737-2.74819393e+04j,
                              -2030852.42623273+8.40205385e+03j,
                             -54502988.18785564+4.75790494e+07j,
                              47217941.0142496 +8.94536006e+06j,
                               6654278.33719367-1.81089469e+05j,
                               4974433.40023975-4.73425087e+05j,
                               4662225.0011754 -2.41147877e+05j])

    def tearDown(self):
        del self.FIRPars
        del self.config
        del self.known_Corfir

    def test_correctFIRfilter(self):
        C = pydarm.sensing.SensingModel(self.config)
        Cf = C.compute_sensing(self.FIRPars.freq_array)
        test_Cfir = createFIRfilter(self.FIRPars, Cf)[0]
        test_Corfir = correctFIRfilter(self.FIRPars, test_Cfir, Cf,  [2, 4, 7, 9])
        # The first element is zero so we will delete this one from the check
        # to avoid divide by zero errors
        test_Corfir = np.delete(test_Corfir, 0)

        self.assertEqual(len(test_Corfir), len(self.known_Corfir))
        for n in range(len(test_Corfir)):
            self.assertAlmostEqual(
                np.abs(test_Corfir[n])/np.abs(self.known_Corfir[n]), 1)
            self.assertAlmostEqual(
                np.angle(test_Corfir[n], deg=True) -
                np.angle(self.known_Corfir[n], deg=True), 0)


class Testtwo_tap_zero_filter(unittest.TestCase):

    def setUp(self):
        self.known_two_tap_zero_filt = np.array(
            [0.999999999999999889+0.000000000000000000j,
             0.944065144524670274-0.242141032019198316j,
             0.791790257603250391-0.430462197742083885j,
             0.584088546831189381-0.528606912083167346j,
             0.372528221948197957-0.528347694598477635j,
             0.201488911932644205-0.449462235973869528j,
             0.094304975193611695-0.329261396976028187j,
             0.048712779360778842-0.206416348868232596j,
             0.042948901676579269-0.105952738743734842j,
             0.049370136034108433-0.031598975501051528j])

    def tearDown(self):
        del self.known_two_tap_zero_filt

    def test_two_tap_zero_filt(self):
        test_ttzf = two_tap_zero_filter_response([1, 2], 1, np.linspace(1, 100, 10))

        for n in range(len(test_ttzf)):
            self.assertAlmostEqual(np.abs(test_ttzf[n]),
                                   np.abs(self.known_two_tap_zero_filt[n]), places=6)
            self.assertAlmostEqual(np.angle(test_ttzf[n], deg=True),
                                   np.angle(self.known_two_tap_zero_filt[n], deg=True),
                                   places=6)


class Testcheck_td_vs_fd(unittest.TestCase):

    def setUp(self):
        self.FIRPars = FIRfilter(fNyq=2048, dur=1, highpass_fcut=8, lowpass_fcut=None,
                                 latency=None, window_type='kaiser', freq_res=3.0)
        self.config = '''
[metadata]
[interferometer]
[sensing]
x_arm_length = 3994.4704
y_arm_length = 3994.4692
coupled_cavity_optical_gain = 3.22e6
coupled_cavity_pole_frequency = 410.6
detuned_spring_frequency = 4.468
detuned_spring_Q = 52.14
sensing_sign = 1
is_pro_spring = True
anti_aliasing_rate_string = 16k
anti_aliasing_method      = biquad
analog_anti_aliasing_file = test/H1aa.mat, test/H1aa.mat
whitening_mode_names = mode1, mode1
omc_meas_p_trans_amplifier_uncompensated   = 13.7e3, 17.8e3: 13.7e3, 17.8e3
omc_meas_p_whitening_uncompensated_mode1   = 11.346e3, 32.875e3, 32.875e3: 11.521e3, 32.863e3, 32.863e3
super_high_frequency_poles_apparent_delay = 0, 0
gain_ratio = 1, 1
balance_matrix = 1, 1
omc_path_names = A, B
single_pole_approximation_delay_correction = -12e-6
adc_gain = 1, 1
omc_filter_file = test/H1OMC_1239468752.txt
omc_filter_bank = OMC_DCPD_A, OMC_DCPD_B
omc_filter_noncompensating_modules =
omc_filter_gain = 1, 1
omc_front_end_trans_amplifier_compensation = ON, ON
omc_front_end_whitening_compensation_mode1 = ON, ON
'''

    def tearDown(self):
        del self.FIRPars
        del self.config

    def test_check_td_vs_fd(self):
        C = pydarm.sensing.SensingModel(self.config)
        Cf = C.compute_sensing(self.FIRPars.freq_array)
        test_Cfir = createFIRfilter(self.FIRPars, Cf)[0]
        ctvf = check_td_vs_fd(test_Cfir, Cf, fNyq=self.FIRPars.fNyquist,
                                   delay_samples=self.FIRPars.delay_samples)

        test_freq = ctvf[0][0]
        test_mag_ratios = ctvf[1][0]
        test_phase_diffs = ctvf[2][0]

        df = test_freq[1] - test_freq[0]
        # For this configuration, check that the magnitude and phase are close to
        # 1 and 0, respectively between 50 and 1000 Hz
        Nmin = math.ceil(40 / df)
        Nmax = math.ceil(1000 / df)
 
        for n in range(Nmin, Nmax):
            self.assertLess(np.abs(test_mag_ratios[n]), 1.01)
            self.assertLess(np.abs(test_phase_diffs[n]), 1)


class TestCheckTdVsFdResponse(unittest.TestCase):

    def setUp(self):
        self.FIRPars = FIRfilter(fNyq=2048, dur=1, highpass_fcut=8, lowpass_fcut=None,
                                 latency=None, window_type='kaiser', freq_res=3.0)
        self.config = '''
[metadata]
[interferometer]
[sensing]
x_arm_length = 3994.4704
y_arm_length = 3994.4692
coupled_cavity_optical_gain = 3.22e6
coupled_cavity_pole_frequency = 410.6
detuned_spring_frequency = 4.468
detuned_spring_Q = 52.14
sensing_sign = 1
is_pro_spring = True
anti_aliasing_rate_string = 16k
anti_aliasing_method      = biquad
analog_anti_aliasing_file = test/H1aa.mat, test/H1aa.mat
whitening_mode_names = mode1, mode1
omc_meas_p_trans_amplifier_uncompensated   = 13.7e3, 17.8e3: 13.7e3, 17.8e3
omc_meas_p_whitening_uncompensated_mode1   = 11.346e3, 32.875e3, 32.875e3: 11.521e3, 32.863e3, 32.863e3
super_high_frequency_poles_apparent_delay = 0, 0
gain_ratio = 1, 1
balance_matrix = 1, 1
omc_path_names = A, B
single_pole_approximation_delay_correction = -12e-6
adc_gain = 1, 1
omc_filter_file = test/H1OMC_1239468752.txt
omc_filter_bank = OMC_DCPD_A, OMC_DCPD_B
omc_filter_noncompensating_modules =
omc_filter_gain = 1, 1
omc_front_end_trans_amplifier_compensation = ON, ON
omc_front_end_whitening_compensation_mode1 = ON, ON

[digital]
digital_filter_file    = test/H1OMC_1239468752.txt
digital_filter_bank    = LSC_DARM1, LSC_DARM2
digital_filter_modules = 1,2,3,4,7,9,10: 3,4,5,6,7
digital_filter_gain    = 400,1

[actuation]
darm_output_matrix = 1.0, -1.0, 0.0, 0.0
darm_feedback_x    = OFF, ON, ON, ON
darm_feedback_y    = OFF, OFF, OFF, OFF

[actuation_x_arm]
darm_feedback_sign = -1
uim_NpA       = 1.634
pum_NpA       = 0.02947
tst_NpV2      = 4.427e-11
linearization = OFF
actuation_esd_bias_voltage = -9.3
sus_filter_file = test/H1SUSETMX_1236641144.txt
tst_isc_inf_bank    = ETMX_L3_ISCINF_L
tst_isc_inf_modules =
tst_isc_inf_gain    = 1.0
tst_lock_bank       = ETMX_L3_LOCK_L
tst_lock_modules    = 5,8,9,10
tst_lock_gain       = 1.0
tst_drive_align_bank     = ETMX_L3_DRIVEALIGN_L2L
tst_drive_align_modules  = 4,5
tst_drive_align_gain     = -35.7
pum_lock_bank    = ETMX_L2_LOCK_L
pum_lock_modules = 7
pum_lock_gain    = 23.0
pum_drive_align_bank    = ETMX_L2_DRIVEALIGN_L2L
pum_drive_align_modules = 6,7
pum_drive_align_gain    = 1.0
pum_coil_outf_signflip  = 1
uim_lock_bank    = ETMX_L1_LOCK_L
uim_lock_modules = 10
uim_lock_gain    = 1.06
uim_drive_align_bank    = ETMX_L1_DRIVEALIGN_L2L
uim_drive_align_modules =
uim_drive_align_gain    = 1.0
suspension_file = test/H1susdata_O3.mat
tst_driver_uncompensated_Z_UL = 129.7e3
tst_driver_uncompensated_Z_LL = 90.74e3
tst_driver_uncompensated_Z_UR = 93.52e3
tst_driver_uncompensated_Z_LR = 131.5e3
tst_driver_uncompensated_P_UL = 3.213e3, 31.5e3
tst_driver_uncompensated_P_LL = 3.177e3, 26.7e3
tst_driver_uncompensated_P_UR = 3.279e3, 26.6e3
tst_driver_uncompensated_P_LR = 3.238e3, 31.6e3
tst_driver_DC_gain_VpV_HV = 40
tst_driver_DC_gain_VpV_LV = 1.881
pum_driver_DC_trans_ApV = 2.6847e-4
uim_driver_DC_trans_ApV = 6.1535e-4
anti_imaging_rate_string = 16k
anti_imaging_method      = biquad
analog_anti_imaging_file = test/H1aa.mat
dac_gain = 7.62939453125e-05
unknown_actuation_delay = 15e-6
uim_delay = 0
pum_delay = 0
tst_delay = 0

[pcal]
pcal_filter_file           = test/H1CALEY_1123041152.txt
pcal_filter_bank           = PCALY_TX_PD
pcal_filter_modules_in_use = 6,8
pcal_filter_gain           = 1.0
pcal_dewhiten               = 1.0, 1.0
pcal_incidence_angle        = 8.8851
pcal_etm_watts_per_ofs_volt = 0.13535
ref_pcal_2_darm_act_sign    = -1.0
anti_aliasing_rate_string = 16k
anti_aliasing_method      = biquad
analog_anti_aliasing_file = test/H1aa.mat
'''
    def tearDown(self):
        del self.FIRPars
        del self.config

    def test_check_td_vs_fd_response(self):
        freq = self.FIRPars.freq_array
        # DARM model throws warnings when computed at 0 Hz, so remove that from frequency array
        freq = np.delete(freq, 0)
        darm = pydarm.darm.DARMModel(self.config)
        # To get frequency vectors correct, need to reinsert the zero frequency component after DARM components are computed
        # Just set this DC component to 0
        InvC = np.insert(1/darm.sensing.compute_sensing(freq), 0, 0)
        TST = np.insert(darm.actuation.xarm.compute_actuation_single_stage(freq, stage='TST'), 0, 0)
        PUM = np.insert(darm.actuation.xarm.compute_actuation_single_stage(freq, stage='PUM'), 0, 0)
        UIM = np.insert(darm.actuation.xarm.compute_actuation_single_stage(freq, stage='UIM'), 0, 0)
        D = np.insert(darm.digital.compute_response(freq), 0, 0)
        R = np.insert(darm.compute_response_function(freq), 0, 0)

        InvC_filt = createFIRfilter(self.FIRPars, InvC)[0]
        TST_filt = createFIRfilter(self.FIRPars, TST)[0]
        PUM_filt = createFIRfilter(self.FIRPars, PUM)[0]
        UIM_filt = createFIRfilter(self.FIRPars, UIM)[0]

        test_freq, test_ratio_mag, test_ratio_pha = check_td_vs_fd_response(InvC_filt,
                                            None,
                                            TST_filt,
                                            PUM_filt,
                                            UIM_filt,
                                            None,
                                            D,
                                            R,
                                            time_delay = 0.0,
                                            invsens_fNyq=self.FIRPars.fNyquist,
                                            act_fNyq=self.FIRPars.fNyquist,
                                            D_fNyq=self.FIRPars.fNyquist,
                                            R_fNyq=self.FIRPars.fNyquist)

        
        df = test_freq[1] - test_freq[0]
        # For this configuration, check that the magnitude and phase are close to
        # 1 and 0, respectively between 50 and 1000 Hz
        Nmin = math.ceil(40 / df)
        Nmax = math.ceil(1000 / df)
        
        for n in range(Nmin, Nmax):
            self.assertLess(np.abs(test_ratio_mag[n]), 1.05)
            self.assertLess(np.abs(test_ratio_pha[n]), 5)

class TestGDS_FIR_filter_generation(unittest.TestCase):
    def setUp(self):
        # Maddie test
        # Set up for control chain FIR filter generation
        self.FIRpars = FIRfilter(fNyq=1024, dur=3.5, highpass_fcut=10.5, lowpass_fcut=None,
                                 latency=None, window_type='dpss', freq_res=4.0)

        # Load in known transfer function and resulting FIR filter
        h5f = h5py.File('./test/FIR_unit_test_coeffs.h5', 'r')
        self.known_FIR_filter = h5f['FIR_filter'][:]
        self.known_tf = h5f['transfer_function'][:]

    def tearDown(self):
        del self.FIRpars
        del self.known_FIR_filter
        del self.known_tf

    def test_GDS_FIR_filter_generation(self):
        # Generate test FIR filter from frequency domain transfer function
        [test_FIR_filter, model] = createFIRfilter(self.FIRpars, self.known_tf)
        # FIXME: (Arif) Scipy and FIRtools have much different results under 10 Hz.
        # I changed the range and places. My local test could take higher places.
        for n in range(300, len(self.known_FIR_filter)-300):
            self.assertAlmostEqual(abs((self.known_FIR_filter[n] / test_FIR_filter[n])
                                       - 1), 0, places=3)


class TestFilterGeneration(unittest.TestCase):

    def setUp(self):
        self.arm_length = 3994.4698
        self.fcc = 410.6
        self.fs = 4.468
        self.fs_squared = 19.963024
        self.srcQ = 52.14
        self.ips = 1.0
        os.environ['CAL_DATA_ROOT'] = './test'

    def tearDown(self):
        del self.arm_length
        del self.fcc
        del self.fs
        del self.fs_squared
        del self.srcQ
        del self.ips
        del os.environ['CAL_DATA_ROOT']

    def test_FilterGeneration(self):
        config = './example_model_files/H1_20190416.ini'
        FG = pydarm.FIR.FilterGeneration(config)
        self.assertEqual(self.arm_length, FG.arm_length)
        self.assertEqual(self.fcc, FG.fcc)
        self.assertEqual(self.fs, FG.fs)
        self.assertEqual(self.fs_squared, FG.fs_squared)
        self.assertEqual(self.srcQ, FG.srcQ)
        self.assertEqual(self.ips, FG.ips)


class TestGDS(unittest.TestCase):

    def setUp(self):
        self.GDS_file = h5py.File('./test/GDS_test.h5', 'r')
        self.ctrl_corr_td = self.GDS_file['ctrl_corr_filter'][:]
        os.environ['CAL_DATA_ROOT'] = './test'

    def tearDown(self):
        del self.GDS_file
        del self.ctrl_corr_td
        del os.environ['CAL_DATA_ROOT']

    def test_GDS(self):
        config = './example_model_files/H1_20190416.ini'
        FG = pydarm.FIR.FilterGeneration(config)
        FG.GDS(ctrl_window_type='kaiser', res_window_type='kaiser',
               make_plot=False, output_filename='./test/GDS.npz',
               plots_directory='./examples/GDS_plots')
        gds = np.load('./test/GDS.npz')
        ctrl_td = gds['ctrl_corr_filter']
        for n in range(len(self.ctrl_corr_td)):
            self.assertAlmostEqual(abs((self.ctrl_corr_td[n] / ctrl_td[n])
                                       - 1), 0, places=3)


class TestDCS(unittest.TestCase):

    def setUp(self):
        self.DCS_file = h5py.File('./test/DCS_test.h5', 'r')
        self.known_act_tst = self.DCS_file['actuation_tst'][:]
        os.environ['CAL_DATA_ROOT'] = './test'

    def tearDown(self):
        del self.DCS_file
        del self.known_act_tst
        del os.environ['CAL_DATA_ROOT']

    def test_DCS(self):
        config = './example_model_files/H1_20190416.ini'
        FG = pydarm.FIR.FilterGeneration(config)
        FG.DCS(act_window_type='kaiser', invsens_window_type='kaiser',
               make_plot=False, output_filename='./test/DCS.npz',
               plots_directory='examples/DCS_plots')
        dcs = np.load('./test/DCS.npz')
        act_tst = dcs['actuation_tst']
        for n in range(len(self.known_act_tst)):
            self.assertAlmostEqual(abs((self.known_act_tst[n] / act_tst[n])
                                       - 1), 0, places=3)


if __name__ == '__main__':
    unittest.main()
