"""sonusai calc_metric_spenh_targetf

usage: calc_metric_spenh_targetf [-hvptx] [-i MIXID] (-d PLOC) INPUT

options:
    -h, --help
    -v, --verbose               Be verbose.
    -i MIXID, --mixid MIXID     Mixture ID(s) to generate. [default: *].
    -d PLOC, --ploc PLOC        Location of SonusAI predict data.
    -p, --plot-enable           Generate PDF file of plots for each mixture.
    -t, --truth-est-mode        Calculate extraction using truth and include metrics.
    -x, --disable-wav           Disable WAV file generation.

Calculate speech enhancement metrics for prediction data in PLOC run with feature+truth data in INPUT.

Inputs:
    PLOC    SonusAI prediction data directory.
    INPUT   SonusAI mixture database directory containing feature+truth data.

Outputs the following to PLOC:
    <id>-target.wav
    <id>-target-est.wav
    <id>-spenh-metrics.txt
    <id>-noise.wav
    <id>-noise-est.wav
    <id>-mixture.wav
    <id>-spenh-plots.pdf
    spenh-metrics-estats-list.csv
    spenh-metrics-estats-tru-list.csv
    spenh-metrics-list.csv
    spenh-metrics-summary.csv
    spenh-metrics-summary.txt
    spenh-metrics-tru-list.csv

"""
from typing import Union

import matplotlib.pyplot as plt
import numpy as np

from sonusai import SonusAIError
from sonusai import logger
from sonusai.mixture import AudioF
from sonusai.mixture import AudioT
from sonusai.mixture import Feature
from sonusai.mixture import Predict


def mean_square_error(ytrue: np.ndarray, ypred: np.ndarray, squared=False) -> (np.ndarray, np.ndarray, np.ndarray):
    """ Calculate mean square error or root mean square error between ytrue, ypred

    Typical inputs expected to be size frames x classes/bins
    returns:
      err    mean over both dimensions
      err_c  mean-over-dim0 i.e. a value per class/bin
      err_f  mean-over-dim1 i.e. a value per frame
    """
    sqerr = np.square(ytrue - ypred)
    err_c = np.mean(sqerr, axis=0)  # mean over frames for value per class
    err_f = np.mean(sqerr, axis=1)  # mean over classes for value per frame
    err = np.mean(sqerr)  # mean over all
    if not squared:
        err_c = np.sqrt(err_c)
        err_f = np.sqrt(err_f)
        err = np.sqrt(err)

    return err, err_c, err_f


def mean_abs_percentage_error(ytrue: np.ndarray, ypred: np.ndarray) -> (np.ndarray, np.ndarray, np.ndarray):
    """ Calculate mean abs percentage error between ytrue, ypred

    Typical inputs expected to be size frames x classes/bins
    returns:
      err    mean over both dimensions
      err_c  mean-over-dim0 i.e. a value per class/bin
      err_f  mean-over-dim1 i.e. a value per frame
    """
    abserr = np.abs(ytrue - ypred) / (ytrue + np.finfo(np.float32).eps)
    err_c = np.mean(abserr, axis=0)  # mean over frames for value per class
    err_f = np.mean(abserr, axis=1)  # mean over classes for value per frame
    err = np.mean(abserr)  # mean over all

    return err, err_c, err_f


def log_error(ytrue: np.ndarray, ypred: np.ndarray) -> (np.ndarray, np.ndarray, np.ndarray):
    """ Calculate log error between ytrue, ypred which are complex or real float numpy arrays

    Typical inputs expected to be size frames x classes/bins
    returns:
      logerr    mean over both dimensions, scalar value
      logerr_c  mean-over-dim0 i.e. a value per class/bin
      logerr_f  mean-over-dim1 i.e. a value per frame
    """
    ytsq = np.real(ytrue * np.conjugate(ytrue))
    ypsq = np.real(ypred * np.conjugate(ypred))
    lgerr = abs(10 * np.log10((ytsq + np.finfo(np.float32).eps) / (ypsq + np.finfo(np.float32).eps)))
    # lgerr = abs(10*np.log10(ytsq / (ypsq + np.finfo(np.float32).eps)+np.finfo(np.float32).eps))
    logerr_c = np.mean(lgerr, axis=0)  # mean over frames for value per class
    logerr_f = np.mean(lgerr, axis=1)  # mean over classes for value per frame
    logerr = np.mean(lgerr)

    return logerr, logerr_c, logerr_f


def calculate_pesq(speech_ref: np.ndarray, speech_est: np.ndarray, error_value=0.0):
    """ Computes the PESQ score of speech estimate audio vs. the clean speech estimate audio

    Upon error, assigns a value of 0, or user specified value in error_value
    Argument/s:
      speech_ref - speech reference audio, np.ndarray vector of samples.
      speech_est - speech estimated audio, np.ndarray vector of samples.
    Returns:
      score - float value between -0.5 to 4.5.
   """
    from pesq import pesq

    try:
        score = pesq(16000, speech_ref, speech_est, mode='wb')
    except Exception as e:
        logger.debug(f'PESQ error {e}')
        score = error_value

    return score


def plot_mixpred(mixture: AudioT,
                 mixture_f: AudioF,
                 target: AudioT = None,
                 feature: Feature = None,
                 predict: Predict = None,
                 tp_title: str = '') -> plt.figure:
    from sonusai.mixture import SAMPLE_RATE

    num_plots = 2
    if feature is not None:
        num_plots += 1
    if predict is not None:
        num_plots += 1

    fig, ax = plt.subplots(num_plots, 1, constrained_layout=True, figsize=(11, 8.5))

    # Plot the waveform
    p = 0
    x_axis = np.arange(len(mixture), dtype=np.float32) / SAMPLE_RATE
    ax[p].plot(x_axis, mixture, label='Mixture', color='mistyrose')
    ax[0].set_ylabel('magnitude', color='tab:blue')
    ax[p].set_xlim(x_axis[0], x_axis[-1])
    # ax[p].set_ylim([-1.025, 1.025])
    if target is not None:  # Plot target time-domain waveform on top of mixture
        ax[0].plot(x_axis, target, label='Target', color='tab:blue')
        # ax[0].tick_params(axis='y', labelcolor=color)
    ax[p].set_title('Waveform')

    # Plot the mixture spectrogram
    p += 1
    ax[p].imshow(np.transpose(mixture_f), aspect='auto', interpolation='nearest', origin='lower')
    ax[p].set_title('Mixture')

    if feature is not None:
        p += 1
        ax[p].imshow(np.transpose(feature), aspect='auto', interpolation='nearest', origin='lower')
        ax[p].set_title('Feature')

    if predict is not None:
        p += 1
        ax[p].imshow(np.transpose(predict), aspect='auto', interpolation='nearest', origin='lower')
        ax[p].set_title('Predict ' + tp_title)

    return fig


def plot_pdb_predtruth(predict: np.ndarray,
                       truth_f: Union[np.ndarray, None] = None,
                       metric: Union[np.ndarray, None] = None,
                       tp_title: str = '') -> plt.figure:
    """ Plot predict and optionally truth and a metric in power db, e.g. applies 10*log10(predict)"""

    num_plots = 2
    if truth_f is not None:
        num_plots += 1

    fig, ax = plt.subplots(num_plots, 1, constrained_layout=True, figsize=(11, 8.5))

    # Plot the predict spectrogram
    p = 0
    tmp = 10 * np.log10(predict.transpose() + np.finfo(np.float32).eps)
    ax[p].imshow(tmp, aspect='auto', interpolation='nearest', origin='lower')
    ax[p].set_title('Predict')

    if truth_f is not None:
        p += 1
        tmp = 10 * np.log10(truth_f.transpose() + np.finfo(np.float32).eps)
        ax[p].imshow(tmp, aspect='auto', interpolation='nearest', origin='lower')
        ax[p].set_title('Truth')

    # Plot the predict avg, and optionally truth avg and metric lines
    pred_avg = 10 * np.log10(np.mean(predict, axis=-1) + np.finfo(np.float32).eps)
    p += 1
    x_axis = np.arange(len(pred_avg), dtype=np.float32)  # / SAMPLE_RATE
    ax[p].plot(x_axis, pred_avg, color='black', linestyle='dashed', label='Predict mean over freq.')
    ax[p].set_ylabel('mean db', color='black')
    ax[p].set_xlim(x_axis[0], x_axis[-1])
    if truth_f is not None:
        truth_avg = 10 * np.log10(np.mean(truth_f, axis=-1) + np.finfo(np.float32).eps)
        ax[p].plot(x_axis, truth_avg, color='green', linestyle='dashed', label='Truth mean over freq.')

    if metric is not None:  # instantiate 2nd y-axis that shares the same x-axis
        ax2 = ax[p].twinx()
        color2 = 'red'
        ax2.plot(x_axis, metric, color=color2, label='sig distortion (mse db)')
        ax2.set_xlim(x_axis[0], x_axis[-1])
        ax2.set_ylim([0, np.max(metric)])
        ax2.set_ylabel('spectral distortion (mse db)', color=color2)
        ax2.tick_params(axis='y', labelcolor=color2)
        ax[p].set_title('SNR and SNR mse (mean over freq. db)')
    else:
        ax[p].set_title('SNR (mean over freq. db)')
        # ax[0].tick_params(axis='y', labelcolor=color)
    return fig


def plot_epredtruth(predict: np.ndarray,
                    predict_wav: np.ndarray,
                    truth_f: Union[np.ndarray, None] = None,
                    truth_wav: Union[np.ndarray, None] = None,
                    metric: Union[np.ndarray, None] = None,
                    tp_title: str = '') -> plt.figure:
    """ Plot predict spectrogram and waveform and optionally truth and a metric)"""

    num_plots = 2
    if truth_f is not None:
        num_plots += 1
    if metric is not None:
        num_plots += 1

    fig, ax = plt.subplots(num_plots, 1, constrained_layout=True, figsize=(11, 8.5))

    # Plot the predict spectrogram
    p = 0
    ax[p].imshow(predict.transpose(), aspect='auto', interpolation='nearest', origin='lower')
    ax[p].set_title('Predict')

    if truth_f is not None:
        p += 1
        ax[p].imshow(truth_f.transpose(), aspect='auto', interpolation='nearest', origin='lower')
        ax[p].set_title('Truth')

    # Plot the predict wav, and optionally truth avg and metric lines
    p += 1
    x_axis = np.arange(len(predict_wav), dtype=np.float32)  # / SAMPLE_RATE
    ax[p].plot(x_axis, predict_wav, color='black', linestyle='dashed', label='Speech Estimate')
    ax[p].set_ylabel('Amplitude', color='black')
    ax[p].set_xlim(x_axis[0], x_axis[-1])
    if truth_wav is not None:
        ntrim = len(truth_wav) - len(predict_wav)
        if ntrim > 0:
            truth_wav = truth_wav[0:-ntrim]
        ax[p].plot(x_axis, truth_wav, color='green', linestyle='dashed', label='True Target')

    # Plot the metric lines
    if metric is not None:
        p += 1
        x_axis = np.arange(len(metric), dtype=np.float32)  # / SAMPLE_RATE
        ax[p].plot(x_axis, metric, color='red', label='Target LogErr')
        ax[p].set_ylabel('log error db', color='red')
        ax[p].set_xlim(x_axis[0], x_axis[-1])
        ax[p].set_ylim([-0.01, np.max(metric) + .01])

    return fig


def main():
    from docopt import docopt

    import sonusai
    from sonusai.utils import trim_docstring

    args = docopt(trim_docstring(__doc__), version=sonusai.__version__, options_first=True)

    verbose = args['--verbose']
    mixids = args['--mixid']
    predict_name = args['--ploc']
    truth_est_mode = args['--truth-est-mode']
    plot_enable = args['--plot-enable']
    disable_wav = args['--disable-wav']
    input_name = args['INPUT']

    from os.path import basename
    from os.path import join
    from os.path import splitext
    import pandas as pd

    import h5py

    from sonusai import create_file_handler
    from sonusai import initial_log_messages
    from sonusai import update_console_handler
    from sonusai.mixture import MixtureDatabase
    from sonusai.utils import int16_to_float
    from sonusai.utils import float_to_int16
    from sonusai.utils import stacked_complex_imag
    from sonusai.utils import stacked_complex_real
    from sonusai.utils import unstack_complex
    from sonusai.utils import write_wav

    # Setup logging file
    create_file_handler(join(predict_name, 'calc_metric_spenh_targetf.log'))
    update_console_handler(verbose)
    initial_log_messages('calc_metric_spenh_targetf')

    mixdb = MixtureDatabase(input_name)
    mixids = mixdb.mixids_to_list(mixids)
    logger.info(f'Found {len(mixids)} mixtures with {mixdb.num_classes} classes from {input_name}')

    all_metrics_table_1 = None
    all_metrics_table_2 = None
    all_metrics_table_3 = None
    all_metrics_table_4 = None

    target_truth_est_complex = None
    noise_truth_est_complex = None
    target_truth_est_audio = None
    noise_truth_est_audio = None
    lerr_tgtr_frame = None
    lerr_ntr_frame = None
    mtab_snr_summary_tr = None
    mtab_snr_summary_emtr = None

    for mi in mixids:
        # 1) Collect true target, noise, mixture data
        target = mixdb.mixture_target(mi)
        noise = mixdb.mixture_noise(mi)
        mixture = mixdb.mixture_mixture(mi, target=target, noise=noise)
        feature, truth_f = mixdb.mixture_ft(mi, mixture=mixture)
        mixture_f = mixdb.mixture_mixture_f(mi, mixture=mixture)
        target_f = mixdb.mixture_target_f(mi, target=target)
        noise_f = mixdb.mixture_noise_f(mi, noise=noise)

        target = int16_to_float(target)
        noise = int16_to_float(noise)
        mixture = int16_to_float(mixture)

        # 2)  Read predict data
        output_name = join(predict_name, mixdb.mixtures[mi].name)
        base_name = splitext(output_name)[0]
        with h5py.File(output_name, 'r') as f:
            predict = np.array(f['predict'])

        # 3) Extraction - for target_f truth, simply unstack as predict is estimating the target
        predict_complex = unstack_complex(predict)
        truth_f_complex = unstack_complex(truth_f)
        noise_est_complex = mixture_f - predict_complex
        target_est_wav = mixdb.inverse_transform(predict_complex)
        noise_est_wav = mixdb.inverse_transform(noise_est_complex)

        if truth_est_mode is True:
            # estimates using truth instead of prediction
            target_truth_est_complex = truth_f_complex
            noise_truth_est_complex = mixture_f - target_truth_est_complex
            target_truth_est_audio = mixdb.inverse_transform(target_truth_est_complex)
            noise_truth_est_audio = mixdb.inverse_transform(noise_truth_est_complex)

        # 4) Metrics
        # Mean absolute error (real and imag)
        mape_r_tg, mape_r_tg_bin, mape_r_tg_frame = mean_abs_percentage_error(stacked_complex_real(truth_f),
                                                                              stacked_complex_real(predict))
        mape_i_tg, mape_i_tg_bin, mape_i_tg_frame = mean_abs_percentage_error(stacked_complex_imag(truth_f),
                                                                              stacked_complex_imag(predict))
        cmape_tg = (mape_r_tg / 2) + (mape_i_tg / 2)
        cmape_tg_bin = (mape_r_tg_bin / 2) + (mape_i_tg_bin / 2)
        cmape_tg_frame = (mape_r_tg_frame / 2) + (mape_i_tg_frame / 2)

        # Target/Speech logerr - PSD estimation accuracy symmetric mean log-spectral distortion
        lerr_tg, lerr_tg_bin, lerr_tg_frame = log_error(truth_f_complex, predict_complex)
        # Noise logerr - PSD estimation accuracy
        lerr_n, lerr_n_bin, lerr_n_frame = log_error(noise_f, noise_est_complex)

        # Speech intelligibility measure - PESQ
        pesq_speech = calculate_pesq(target, target_est_wav)
        pesq_mixture = calculate_pesq(target, mixture)
        pesq_impr = pesq_speech - pesq_mixture  # pesq improvement
        pesq_impr_pc = pesq_impr / (pesq_mixture + np.finfo(np.float32).eps) * 100  # pesq improvement %

        # 5) Save per mixture metric results
        # Single row in table of scalar metrics per mixture
        mtable1_col = ['MXSNR', 'MXPESQ', 'PESQ', 'PESQi', 'PESQi%', 'SPCMAPE', 'SPLERR', 'NLERR', 'SPFILE', 'NFILE']
        ti = mixdb.mixtures[mi].target_file_index[0]
        ni = mixdb.mixtures[mi].noise_file_index
        metr1 = [mixdb.mixtures[mi].snr, pesq_mixture, pesq_speech, pesq_impr, pesq_impr_pc, cmape_tg, lerr_tg,
                 lerr_n, basename(mixdb.targets[ti].name), basename(mixdb.noises[ni].name)]
        mtab1 = pd.DataFrame([metr1], columns=mtable1_col, index=[mi])
        # Stats of per frame estimation metrics
        efs_table2_col = ['Max', 'Min', 'Avg', 'Median']
        efs_table2_row = ['SPCMAPE', 'SPLERR', 'NLERR']
        metr2 = [[np.max(cmape_tg_frame), np.min(cmape_tg_frame), np.mean(cmape_tg_frame), np.median(cmape_tg_frame)],
                 [np.max(lerr_tg_frame), np.min(lerr_tg_frame), np.mean(lerr_tg_frame), np.median(lerr_tg_frame)],
                 [np.max(lerr_n_frame), np.min(lerr_n_frame), np.mean(lerr_n_frame), np.median(lerr_n_frame)]]
        mtab2 = pd.DataFrame(metr2, columns=efs_table2_col, index=efs_table2_row)

        mtab2flat_col = ['MXSNR', 'SPCMAPE Max', 'SPCMAPE Min', 'SPCMAPE Avg', 'SPCMAPE Median',
                         'SPLERR Max', 'SPLERR Min', 'SPLERR Avg', 'SPLERR Median',
                         'NLERR Max', 'NLERR Min', 'NLERR Avg', 'NLERR Median']
        tmp = np.insert(np.array(metr2), 0, mixdb.mixtures[mi].snr).reshape(1, 13)
        mtab2_flat = pd.DataFrame(tmp, columns=mtab2flat_col, index=[mi])

        if all_metrics_table_1 is None:
            # create the table if it doesn't exist
            all_metrics_table_1 = mtab1
        else:
            # Update all mixture table
            all_metrics_table_1 = pd.concat([all_metrics_table_1, mtab1])

        if all_metrics_table_2 is None:
            # create the table if it doesn't exist
            all_metrics_table_2 = mtab2_flat
        else:
            # Update all mixture table
            all_metrics_table_2 = pd.concat([all_metrics_table_2, mtab2_flat])

        metric_name = base_name + '-spenh-metrics.txt'
        with open(metric_name, 'w') as f:
            print('Speech enhancement metrics:', file=f)
            print(mtab1.round(2).to_string(), file=f)
            print('', file=f)
            print(f'Extraction statistics over {mixture_f.shape[0]} frames:', file=f)
            print(mtab2.round(2).to_string(), file=f)
            print('', file=f)
            print(f'Target path: {mixdb.targets[ti].name}', file=f)
            print(f'Noise path: {mixdb.noises[ni].name}', file=f)
            # print(f'PESQ improvement: {pesq_impr:0.2f}, {pesq_impr_pc:0.1f}%', file=f)

        if truth_est_mode is True:
            # metrics of estimates using truth instead of prediction
            lerr_tgtr, lerr_tgtr_bin, lerr_tgtr_frame = log_error(truth_f_complex, target_truth_est_complex)
            lerr_ntr, lerr_ntr_bin, lerr_ntr_frame = log_error(noise_f, noise_truth_est_complex)
            pesq_speechtr = calculate_pesq(target, target_truth_est_audio)
            pesq_impr_sptr = pesq_speechtr - pesq_mixture  # pesq improvement
            pesq_impr_pctr = pesq_impr_sptr / (pesq_mixture + np.finfo(np.float32).eps) * 100  # pesq improvement %

            mtable3_col = ['MXSNR', 'MXPESQ', 'PESQ', 'PESQi', 'PESQi%', 'SPLERR', 'NLERR']
            metr3 = [mixdb.mixtures[mi].snr, pesq_mixture, pesq_speechtr, pesq_impr_sptr, pesq_impr_pctr, lerr_tgtr,
                     lerr_ntr]
            mtab3 = pd.DataFrame([metr3], columns=mtable3_col, index=[mi])

            # Stats of per frame estimation metrics
            efs_table4_col = ['Max', 'Min', 'Avg', 'Median']
            efs_table4_row = ['SPLERR', 'NLERR']
            metr4 = [[np.max(lerr_tgtr_frame), np.min(lerr_tgtr_frame), np.mean(lerr_tgtr_frame),
                      np.median(lerr_tgtr_frame)],
                     [np.max(lerr_ntr_frame), np.min(lerr_ntr_frame), np.mean(lerr_ntr_frame),
                      np.median(lerr_ntr_frame)]]
            mtab4 = pd.DataFrame(metr4, columns=efs_table4_col, index=efs_table4_row)

            # Append extraction metrics to metrics file:
            with open(metric_name, 'a') as f:
                print('', file=f)
                print('Speech enhancement metrics of extraction method using truth:', file=f)
                print(mtab3.round(2).to_string(), file=f)
                print('', file=f)
                print('Extraction (using Truth) statistics over frames:', file=f)
                print(mtab4.round(2).to_string(), file=f)

            # Append to all mixture table
            mtab4flat_col = ['MXSNR', 'SPLERR Max', 'SPLERR Min', 'SPLERR Avg', 'SPLERR Median',
                             'NLERR Max', 'NLERR Min', 'NLERR Avg', 'NLERR Median']
            tmp = np.insert(np.array(metr4), 0, mixdb.mixtures[mi].snr).reshape(1, 9)  # Insert MXSNR
            mtab4_flat = pd.DataFrame(tmp, columns=mtab4flat_col, index=[mi])

            if all_metrics_table_3 is None:
                all_metrics_table_3 = mtab3
            else:
                all_metrics_table_3 = pd.concat([all_metrics_table_3, mtab3])

            if all_metrics_table_4 is None:
                all_metrics_table_4 = mtab4_flat
            else:
                all_metrics_table_4 = pd.concat([all_metrics_table_4, mtab4_flat])

        # 7) write wav files
        if disable_wav is False:
            write_wav(name=base_name + '-mixture.wav', audio=float_to_int16(mixture))
            write_wav(name=base_name + '-target-est.wav', audio=float_to_int16(target_est_wav))
            write_wav(name=base_name + '-noise-est.wav', audio=float_to_int16(noise_est_wav))
            write_wav(name=base_name + '-target.wav', audio=float_to_int16(target))
            write_wav(name=base_name + '-noise.wav', audio=float_to_int16(noise))
            # debug code to test for perfect reconstruction of the extraction method
            # note both 75% olsa-hanns and 50% olsa-hann modes checked to have perfect reconstruction
            # target_r = mixdb.inverse_transform(target_f)
            # noise_r = mixdb.inverse_transform(noise_f)
            # _write_wav(name=base_name + '-target_r.wav', audio=float_to_int16(target_r))
            # _write_wav(name=base_name + '-noise_r.wav', audio=float_to_int16(noise_r)) # chk perfect rec
            if truth_est_mode is True:
                write_wav(name=base_name + '-target-trest.wav', audio=float_to_int16(target_truth_est_audio))
                write_wav(name=base_name + '-noise-trest.wav', audio=float_to_int16(noise_truth_est_audio))

        # 8) Write out plot file
        if plot_enable is True:
            from matplotlib.backends.backend_pdf import PdfPages
            plot_fname = base_name + '-spenh-plots.pdf'

            # Reshape feature to eliminate overlap redundancy for easier to understand spectrogram view
            # Original size (frames, stride, num_bands), decimates in stride dimension only if step is > 1
            # Reshape to get frames*decimated_stride, num_bands
            step = int(mixdb.feature_samples / mixdb.feature_step_samples)
            if feature.ndim != 3:
                raise SonusAIError(f'feature does not have 3 dimensions: frames, stride, num_bands')

            # for feature cn*00n**
            feat_sgram = unstack_complex(feature)
            feat_sgram = 20 * np.log10(abs(feat_sgram) + np.finfo(np.float32).eps)
            feat_sgram = feat_sgram[:, -step:, :]  # decimate,  Fx1xB
            feat_sgram = np.reshape(feat_sgram, (feat_sgram.shape[0] * feat_sgram.shape[1], feat_sgram.shape[2]))

            with PdfPages(plot_fname) as pdf:
                # page1 we always have a mixture and prediction, target optional if truth provided
                tfunc_name = mixdb.targets[0].truth_settings[0].function  # first target, assumes all have same
                if tfunc_name == 'mapped_snr_f':  # leave as unmapped snr
                    predplot = predict
                    tfunc_name = mixdb.targets[0].truth_settings[0].function
                elif tfunc_name == 'target_f':
                    predplot = 20 * np.log10(abs(predict_complex) + np.finfo(np.float32).eps)
                else:
                    predplot = 10 * np.log10(predict + np.finfo(np.float32).eps)  # use db scale
                    tfunc_name = tfunc_name + ' (db)'

                mixspec = 20 * np.log10(abs(mixture_f) + np.finfo(np.float32).eps)
                pdf.savefig(plot_mixpred(mixture=mixture,
                                         mixture_f=mixspec,
                                         target=target,
                                         feature=feat_sgram,
                                         predict=predplot,
                                         tp_title=tfunc_name))

                # ----- page 2, plot unmapped predict, opt truth reconstructed and line plots of mean-over-f
                # pdf.savefig(plot_pdb_predtruth(predict=pred_snr_f, tp_title='predict snr_f (db)'))

                # page3
                tg_spec = 20 * np.log10(abs(target_f) + np.finfo(np.float32).eps)
                tg_est_spec = 20 * np.log10(abs(predict_complex) + np.finfo(np.float32).eps)
                # n_spec = np.reshape(n_spec,(n_spec.shape[0] * n_spec.shape[1], n_spec.shape[2]))
                pdf.savefig(plot_epredtruth(predict=tg_est_spec,
                                            predict_wav=target_est_wav,
                                            truth_f=tg_spec,
                                            truth_wav=target,
                                            metric=lerr_tg_frame,
                                            tp_title='speech_est'))

                # page 4 noise extraction
                n_spec = 20 * np.log10(abs(noise_f) + np.finfo(np.float32).eps)
                n_est_spec = 20 * np.log10(abs(noise_est_complex) + np.finfo(np.float32).eps)
                pdf.savefig(plot_epredtruth(predict=n_est_spec,
                                            predict_wav=noise_est_wav,
                                            truth_f=n_spec,
                                            truth_wav=noise,
                                            metric=lerr_n_frame,
                                            tp_title='noise_est'))

                # page 5 truth-based speech extraction
                if truth_est_mode is True:
                    tg_trest_spec = 20 * np.log10(abs(target_truth_est_complex) + np.finfo(np.float32).eps)
                    pdf.savefig(plot_epredtruth(predict=tg_trest_spec,
                                                predict_wav=target_truth_est_audio,
                                                truth_f=tg_spec,
                                                truth_wav=target,
                                                metric=lerr_tgtr_frame,
                                                tp_title='speech_trest'))

                    # page 6 truth-based noise extraction
                    n_trest_spec = 20 * np.log10(abs(noise_truth_est_complex) + np.finfo(np.float32).eps)
                    pdf.savefig(plot_epredtruth(predict=n_trest_spec,
                                                predict_wav=noise_truth_est_audio,
                                                truth_f=n_spec,
                                                truth_wav=noise,
                                                metric=lerr_ntr_frame,
                                                tp_title='truth-based noise estimate'))

            plt.close('all')
            logger.info(f'Wrote plots to {plot_fname}')

    # 9) Done with mixtures, write out summary metrics
    # Calculate SNR summary for
    all_mtab1_sorted = all_metrics_table_1.sort_values(by=['MXSNR', 'SPFILE'])
    all_mtab2_sorted = all_metrics_table_2.sort_values(by=['MXSNR'])
    mtab_snr_summary = all_mtab1_sorted.query('MXSNR==' + str(mixdb.snrs[0])).mean(numeric_only=True).to_frame().T
    mtab_snr_summary_em = all_mtab2_sorted.query('MXSNR==' + str(mixdb.snrs[0])).mean(numeric_only=True).to_frame().T
    for snri in range(1, len(mixdb.snrs)):
        mtab_snr_summary = pd.concat([mtab_snr_summary,
                                      all_mtab1_sorted.query('MXSNR==' + str(mixdb.snrs[snri])).mean(
                                          numeric_only=True).to_frame().T])
        mtab_snr_summary_em = pd.concat([mtab_snr_summary_em,
                                         all_mtab2_sorted.query('MXSNR==' + str(mixdb.snrs[snri])).mean(
                                             numeric_only=True).to_frame().T])

    if truth_est_mode is True:
        all_mtab3_sorted = all_metrics_table_3.sort_values(by=['MXSNR'])
        all_mtab4_sorted = all_metrics_table_4.sort_values(by=['MXSNR'])
        mtab_snr_summary_tr = all_mtab3_sorted.query('MXSNR==' + str(mixdb.snrs[0])).mean(
            numeric_only=True).to_frame().T
        mtab_snr_summary_emtr = all_mtab4_sorted.query('MXSNR==' + str(mixdb.snrs[0])).mean(
            numeric_only=True).to_frame().T
        for snri in range(1, len(mixdb.snrs)):
            mtab_snr_summary_tr = pd.concat([mtab_snr_summary_tr,
                                             all_mtab3_sorted.query('MXSNR==' + str(mixdb.snrs[snri])).mean(
                                                 numeric_only=True).to_frame().T])
            mtab_snr_summary_emtr = pd.concat([mtab_snr_summary_emtr,
                                               all_mtab4_sorted.query('MXSNR==' + str(mixdb.snrs[snri])).mean(
                                                   numeric_only=True).to_frame().T])

    num_mix = len(mixids)
    if num_mix > 1:
        metric_summary_fname = join(predict_name, 'spenh-metrics-summary.txt')
        with open(metric_summary_fname, 'w') as f:
            print(f'Speech enhancement metrics avg over each SNR:', file=f)
            print(mtab_snr_summary.round(2).to_string(), file=f)
            print('', file=f)
            print(f'Extraction statistics stats avg over each SNR:', file=f)
            print(mtab_snr_summary_em.round(2).to_string(), file=f)
            print('', file=f)

            print(f'Speech enhancement metrics stats over all {num_mix} mixtures:', file=f)
            print(all_metrics_table_1.describe().round(2).to_string(), file=f)
            print('', file=f)
            print(f'Extraction statistics stats over all {num_mix} mixtures:', file=f)
            print(all_metrics_table_2.describe().round(2).to_string(), file=f)
            print('', file=f)

            if truth_est_mode is True:
                print(f'Truth-based speech enhancement metrics avg over each SNR:', file=f)
                print(mtab_snr_summary_tr.round(2).to_string(), file=f)
                print('', file=f)
                print(f'Truth-based extraction statistics stats avg over each SNR:', file=f)
                print(mtab_snr_summary_emtr.round(2).to_string(), file=f)
                print('', file=f)

                print(f'Truth-based speech enhancement metrics stats over all {num_mix} mixtures:', file=f)
                print(all_metrics_table_3.describe().round(2).to_string(), file=f)
                print('', file=f)
                print(f'Truth-based extraction statistic stats over all {num_mix} mixtures:', file=f)
                print(all_metrics_table_4.describe().round(2).to_string(), file=f)
                print('', file=f)

            print('Speech enhancement metrics all-mixtures list:', file=f)
            print(all_metrics_table_1.round(2).to_string(), file=f)
            print('', file=f)
            print('Extraction statistics all-mixtures list:', file=f)
            print(all_metrics_table_2.round(2).to_string(), file=f)

            # Write summary to .csv file
            csv_name = join(predict_name, 'spenh-metrics-summary.csv')
            header_args = {
                'mode': 'a',
                'encoding': 'utf-8',
                'index': False,
                'header': False,
            }
            table_args = {
                'mode': 'a',
                'encoding': 'utf-8',
            }
            pd.DataFrame([f'Speech enhancement metrics stats over {num_mix} mixtures:']).to_csv(csv_name, **header_args)
            all_metrics_table_1.describe().round(2).to_csv(csv_name, encoding='utf-8')
            pd.DataFrame(['']).to_csv(csv_name, **header_args)

            pd.DataFrame([f'Extraction statistics stats over {num_mix} mixtures:']).to_csv(csv_name, **header_args)
            all_metrics_table_2.describe().round(2).to_csv(csv_name, **table_args)
            pd.DataFrame(['']).to_csv(csv_name, **header_args)

            if truth_est_mode is True:
                pd.DataFrame(['Truth estimation metrics stats:']).to_csv(csv_name, **header_args)
                all_metrics_table_3.describe().round(2).to_csv(csv_name, **table_args)
                pd.DataFrame(['']).to_csv(csv_name, **header_args)

                pd.DataFrame(['Truth estimation extraction statistics stats:']).to_csv(csv_name, **header_args)
                all_metrics_table_4.describe().round(2).to_csv(csv_name, **table_args)
                pd.DataFrame(['']).to_csv(csv_name, **header_args)

            csv_name = join(predict_name, 'spenh-metrics-list.csv')
            pd.DataFrame(['Speech enhancement metrics list:']).to_csv(csv_name, **header_args)
            all_metrics_table_1.round(2).to_csv(csv_name, **table_args)

            csv_name = join(predict_name, 'spenh-metrics-estats-list.csv')
            pd.DataFrame(['Extraction statistics list:']).to_csv(csv_name, **header_args)
            all_metrics_table_2.round(2).to_csv(csv_name, **table_args)

            if truth_est_mode is True:
                csv_name = join(predict_name, 'spenh-metrics-tru-list.csv')
                pd.DataFrame(['Speech enhancement metrics list:']).to_csv(csv_name, **header_args)
                all_metrics_table_3.round(2).to_csv(csv_name, **table_args)

                csv_name = join(predict_name, 'spenh-metrics-estats-tru-list.csv')
                pd.DataFrame(['Extraction statistics list:']).to_csv(csv_name, **header_args)
                all_metrics_table_4.round(2).to_csv(csv_name, **table_args)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        logger.info('Canceled due to keyboard interrupt')
        exit()
