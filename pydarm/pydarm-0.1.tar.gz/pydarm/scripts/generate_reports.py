from pydarm.measurement import Measurement, ProcessSensingMeasurement
from pydarm.sensing import SensingModel
from pydarm.plot import BodePlot
from scipy.signal import freqresp
import os
import argparse
import numpy as np
import corner
from matplotlib.colors import colorConverter
from matplotlib.patches import Patch as mplpatches
from matplotlib.lines import Line2D
from matplotlib import pyplot as plt
from glob import glob
import re
from datetime import datetime


def print_mcmc_params(mcmcParams, quantileLevels):
    '''
    This function is just for printing MCMC parameters for easy copy/pasting
    to alog. Update of Jeff's existing code for prettier formatting.

    Prints in two formats: first the quantile values,
    then in the format 'X (+Y/-Z)'.

    Parameters
    ----------
    mcmcParams: dict
        Keys should be parameter names, values include quantiles, errbars, labels
        TODO improve documentation

    Returns
    -------
    tableQuant: str
        Printable table of values in quantile format
    tablePM: str
        Printable table of values in +/- format

    '''

    # Set up lists to hold the tables (will be joined with newline later)
    tableQuant = []
    tablePM = []

    # Define a column spacer
    spacer = " | "

    # Set up left column width for parameter labels
    ncharsLabel = max([len(p['label']) for p in mcmcParams.values()])

    # Set up widths for the quantiles section
    ncharsCol = max([len(f"{x:4.4g}") for p in mcmcParams.values()
                    for x in p['quantiles']])

    # Set up the header for the quantiles section
    tag = "(quantile)"
    pline = [f"{'Parameter':<{ncharsLabel-len(tag)}s}{tag}"]
    for x in quantileLevels:
        pline += [f"{str(x):<{ncharsCol}s}"]
    header = spacer.join(pline)
    tableQuant += [header]
    tableQuant += ["-"*len(header)]

    # Set up each line for the quantiles section
    for param in mcmcParams.values():
        pline = [f"{param['label']:<{ncharsLabel}s}"]
        for x in param['quantiles']:
            valstr = f"{x:4.4g}"
            pline += [f"{valstr:<{ncharsCol}s}"]
        tableQuant += [spacer.join(pline)]
    tableQuant += ["-"*len(header)]

    # Set up column widths for the +/- section
    ncharsCol = max([len(f"{param[key]:4.4g} ({abs(param[key]/param['median']):.2f}%)")
                    for param in mcmcParams.values()
                    for key in ['median', 'errplus', 'errminus']])

    # Set up head for the +/- section
    tag = "(value +/-)"
    pline = [f"{'Parameter':<{ncharsLabel-len(tag)}s}{tag}"]
    for x in ["value", " +", " -"]:
        pline += [f"{str(x):<{ncharsCol}s}"]
    header = spacer.join(pline)
    tablePM += [header]
    tablePM += ["-"*len(header)]

    # Set up each line for the +/- section
    for param in mcmcParams.values():
        pline = [f"{param['label']:<{ncharsLabel}s}"]
        for key in ['median', 'errplus', 'errminus']:
            if key == 'median':
                fmat = f"{param[key]:4.4g}"
            else:
                fmat = f"{param[key]:4.4g} ({(param[key]/param['median']):.2f}%)"
            pline += [f"{fmat:<{ncharsCol}s}"]
        tablePM += [spacer.join(pline)]

    tablePM = "\n".join(tablePM)
    tableQuant = "\n".join(tableQuant)

    return tableQuant, tablePM


def make_corner_plot(chains, mcmcParams, quantileLevels, outfile, title):
    '''
    Parameters
    ----------
    chains: 2D array
        size: (number of MCMC params),(number of steps in MCMC chain)

    mcmcParams: dict
        Keys should be parameter names, values include quantiles, errbars, labels

    quantileLevels: 1D array

    outfile
        Path to save corner plot

    title
        Plot title

    Returns
    -------
    None
        Just saves figures
    '''

    color = 'C3'  # base fill color for contours
    truthcolor = 'C0'  # color for median markers
    nbins = 100  # number of bins for histogram

    # === Create main plot
    cp = corner.corner(
        np.transpose(chains),
        bins=nbins,
        quantiles=[quantileLevels[0], quantileLevels[-1]],
        smooth=2.0,
        labels=[param['mathlabel'] for param in mcmcParams.values()],
        verbose=False,
        label_kwargs={'fontsize': 12},
        show_titles=True,
        title_fmt='.3e',
        title_kwargs={'fontsize': 12},
        plot_datapoints=False,
        plot_density=True,
        plot_contours=True,
        fill_contours=True,
        color=color,
        use_math_text=True,
        truths=[param['median'] for param in mcmcParams.values()],
        truth_color=truthcolor
        )
    cp.suptitle(title, fontsize=20)

    # ==== Reproducing the contour colors
    # Annoying as this is, corner does not provide a way to get
    # the contour fill color maps, nor the default levels.
    # We copy the following from its definition in
    # https://github.com/dfm/corner.py/blob/e65dd4cdeb7a9f7f75cbcecb4f07a07de65e2cea/src/corner/core.py
    levels = 1.0 - np.exp(-0.5 * np.arange(0.5, 2.1, 0.5) ** 2)
    rgba_color = colorConverter.to_rgba(color)
    contour_cmap = [list(rgba_color) for lev in levels] + [rgba_color]
    for i, l in enumerate(levels):
        contour_cmap[i][-1] *= float(i) / (len(levels) + 1)
    contour_cmap = contour_cmap[-3:][::-1]

    # === Generating custom legend

    # Shaded rectangle for each contour fill color
    legend_symbols = [mplpatches(
            facecolor=contour_cmap[i],
            edgecolor=contour_cmap[i]) for i in range(len(contour_cmap))]
    # Line for the "truth" values (mcmcParam median values)
    legend_symbols.append(Line2D([0], [0], color=truthcolor, lw=3))
    # Empty rectangle to make space for bin count label
    legend_symbols.append(mplpatches(alpha=0))

    # Create legend
    cp.legend(
            legend_symbols,
            [r'$1\sigma$',
                r'$2\sigma$',
                r'$3\sigma$',
                'MAP',
                f'({nbins} bins for 1D PDF)'],
            fontsize=15,
            title_fontsize=15,
            title="2D PDF contours",
            frameon=True,
            markerscale=20.0,
            )

    # === Fix up the histogram axes

    # Grab all subplot axes
    axes = cp.get_axes()

    # Determine which ones are histograms
    nparams = len(mcmcParams.values())
    length_sides = np.arange(nparams)
    histogram_indices = (nparams+1)*length_sides

    # Create right-side axis for each histogram
    for i in histogram_indices:
        ax = axes[i]
        ax2 = ax.twinx()
        ax2.set_ylabel('1D Norm. PDF \n (Percent per bin)')
        axes += [ax2]
        ax2.set_ylim(0, 1.1)

    # Resize the tick params to make them smaller
    for ax in axes:
        ax.tick_params(axis='both', labelsize=10)

    # Save figure
    cp.tight_layout()
    cp.savefig(outfile)


def sensing(args):

    # === General setup

    # Flatten list of lists from sensing input files argument
    sensing_xml_pairs = [
        item for sublist in args.sensing_xml_pair
        for item in sublist]

    # Select most recent ini file
    pydarmparams = sorted(
        glob(args.pydarmparams),
        key=lambda x: extract_date_general(x))[-1]

    print(f"Loading parameters from {pydarmparams}")
    # Sort pairs of xml files with most recent first, and limit
    # number of most recent files to process
    nmeas = min(args.sensing_n_meas, len(sensing_xml_pairs))
    sensing_xml_pairs = sorted(
        sensing_xml_pairs,
        key=lambda x: extract_date_general(x[0]))[::-1][:nmeas]

    # Create the output directory if it doesn't exist
    os.makedirs(args.sensing_output_dir, exist_ok=True)

    # Format the reference model date and filename
    refDateTag = extract_date_general(pydarmparams).strftime("%Y-%m-%d")
    subtitleText = f"All fixed parameters are drawn from {os.path.basename(pydarmparams)}"

    # Set up common title names
    tfp_title = "Optical response transfer functions"
    rp_title = "Optical response residuals"
    sp_titlesize = 12

    # === Plotting setup

    # main figure
    plt.clf()
    fig = plt.figure()
    fig.suptitle("Sensing model history\n", fontsize=20)
    fig.text(
        .5, .93,
        subtitleText,
        horizontalalignment='center',
        transform=fig.transFigure)

    # transfer function plot (comparison)
    tfp = BodePlot(fig=fig, spspec=[221, 223])
    tfp.ax_mag.set_title(tfp_title, fontsize=sp_titlesize)

    # residuals plot (comparison)
    rp = BodePlot(fig=fig, spspec=[222, 224])
    rp.ax_mag.set_title(rp_title, fontsize=sp_titlesize)

    # Create reference sensing model
    C_ref = SensingModel(pydarmparams)

    # Loop over measurement dates/times
    for im, measXMLpair in enumerate(sensing_xml_pairs):

        # Format the measurement date for this particular measurement
        measDateTag = extract_date_general(measXMLpair[0]).strftime("%Y-%m-%d")

        # Set up the measurements
        print(f"Loading data from {measXMLpair[1]}")
        loop_meas = Measurement(measXMLpair[0])
        print(f"Loading data from {measXMLpair[0]}")
        pcal_meas = Measurement(measXMLpair[1])

        # Process sensing measurement
        processedSensing = ProcessSensingMeasurement(
                            pydarmparams,
                            loop_meas,
                            pcal_meas,
                            ('H1:LSC-DARM1_IN2',
                                'H1:LSC-DARM1_EXC'),
                            ('H1:CAL-PCALY_RX_PD_OUT_DQ',
                                'H1:LSC-DARM_IN1_DQ'),
                            args.cohthresh_loop_meas,
                            args.cohthresh_pcal_meas
                            )

        # Get the common frequency axis and measurement info
        frequencies, measOpticalResponse, measOpticalResponseUnc = \
            processedSensing.get_processed_measurement_response()

        angular_frequencies = 2*np.pi*frequencies

        # Compute the optical response based on reference parameters
        # Note: this reference optical response needs to be computed for
        # each measurement pair despite the fact that it is only plotted
        # once. This is because the frequency axis could differ between
        # measurements, and `refOpticalResponse` must divide the measurement
        # in order to generate the residuals plot.

        refNormOpticalResponse = freqresp(
            SensingModel.optical_response(
                C_ref.coupled_cavity_pole_frequency,
                C_ref.detuned_spring_frequency,
                C_ref.detuned_spring_q,
                C_ref.is_pro_spring),
            angular_frequencies)[1]

        refOpticalResponse = refNormOpticalResponse * \
            C_ref.coupled_cavity_optical_gain

        # If this is the first measurement, we need to compute the
        # reference model response. (This can't be done ahead of time
        # because it relies on the common frequency axis)
        # If requested, we will also run the MCMC on this first measurement.
        if im == 0:

            # Note this first measurement date
            latestMeasDateTag = measDateTag

            # Select scaling for the plot
            expscale = int(np.floor(np.log10(C_ref.coupled_cavity_optical_gain)))
            tfp.ax_mag.set_ylabel(f'Magnitude (ct/m) x $10^{{{expscale}}}$')
            scale = 10**expscale

            # Add reference model curve
            tfp.plot(frequencies, refOpticalResponse/scale, label=f"{refDateTag} model")

            # Add a null curve to keep the color-coding consistent on the residuals plot
            rp.plot([], [])

            # If requested, run the MCMC at this point
            if args.run_mcmc:

                # Run, return parameters, and create corner plot
                mcmcParams, mcmcTableQuant, mcmcTablePM = run_sensing_MCMC(
                    processedSensing,
                    args,
                    measDateTag,
                    C_ref)

                # Compute the optical response based on MCMC parameters
                mcmcNormOpticalResponse = freqresp(
                                        SensingModel.optical_response(
                                            mcmcParams['cavityPole']['median'],
                                            mcmcParams['springF']['median'],
                                            mcmcParams['springQ']['median'],
                                            C_ref.is_pro_spring),
                                        angular_frequencies)[1]

                mcmcOpticalResponse = mcmcNormOpticalResponse * \
                    mcmcParams['opticalGain']['median'] * \
                    np.exp(
                        -2*np.pi*1j*mcmcParams['resDelay']['median'] *
                        frequencies)

                # We need an additional figure for the MCMC results comparison.
                # Setup is in the same format as the multi-measurement comparison.
                fig_mcmc = plt.figure()
                fig_mcmc.suptitle("Sensing model MCMC summary\n", fontsize=20)
                fig_mcmc.text(
                    .5, .93,
                    subtitleText,
                    in_layout=True,
                    horizontalalignment='center',
                    transform=fig_mcmc.transFigure)

                tfp_mcmc = BodePlot(fig=fig_mcmc, spspec=[221, 223])
                tfp_mcmc.ax_mag.set_title(tfp_title, fontsize=sp_titlesize)
                tfp_mcmc.ax_mag.set_ylabel(f'Magnitude (ct/m) x $10^{{{expscale}}}$')
                rp_mcmc = BodePlot(fig=fig_mcmc, spspec=[222, 224])
                rp_mcmc.ax_mag.set_title(rp_title, fontsize=sp_titlesize)

                # Add the curves to the plot
                tfp_mcmc.plot(
                    frequencies,
                    refOpticalResponse/scale,
                    label=f"Model w free params from\n {os.path.basename(pydarmparams)}")
                tfp_mcmc.plot(
                    frequencies,
                    mcmcOpticalResponse/scale,
                    label=f"Model w free params from\n MCMC fit to {measDateTag} data")
                tfp_mcmc.error(
                    frequencies,
                    measOpticalResponse/scale,
                    measOpticalResponseUnc,
                    label=f"{measDateTag} measurement / C_R",
                    fmt='.')

                rp_mcmc.error(
                    frequencies,
                    measOpticalResponse/mcmcOpticalResponse,
                    measOpticalResponseUnc,
                    label=(
                        f"{measDateTag} meas / model w free params\n"
                        f" from {os.path.basename(pydarmparams)}"),
                    fmt='.')
                rp_mcmc.error(
                    frequencies,
                    measOpticalResponse/refOpticalResponse,
                    measOpticalResponseUnc,
                    label=(
                        f"{measDateTag} meas / model w free params\n"
                        f" from {os.path.basename(pydarmparams)}"),
                    fmt='.')

                # Add vertical lines marking the fit range for the MCMC
                for p in [tfp_mcmc, rp_mcmc]:
                    p.vlines(
                        args.mcmc_fmin, color='k', lw=2,
                        label=f"Fit range {args.mcmc_fmin} to {args.mcmc_fmax} Hz")
                    p.vlines(args.mcmc_fmax, color='k', lw=2)
                    p.legend()

                fig_mcmc.subplots_adjust(bottom=0.3)
                coords = (
                    tfp_mcmc.ax_phase.get_tightbbox().x0,
                    tfp_mcmc.ax_phase.get_tightbbox().y0-10)
                fig_mcmc.text(
                    *coords,
                    mcmcTablePM,
                    fontfamily='monospace',
                    horizontalalignment='left',
                    verticalalignment='top',
                    transform=None,  # interpret coordinates as display units
                    )

                #  Wrap up and save figure
                fig_mcmc.savefig(
                    os.path.join(
                        args.sensing_output_dir,
                        f"sensing_mcmc_compare_{measDateTag}.png"),
                    )

        # Add meas curves to transfer function comparison plots
        tfp.error(
            frequencies,
            measOpticalResponse/scale,
            measOpticalResponseUnc,
            label=f"{measDateTag} measurement / C_R",
            fmt='.')

        # Add meas curves to residuals plot
        rp.error(
            frequencies,
            measOpticalResponse/refOpticalResponse,
            measOpticalResponseUnc,
            label=(
                f"{measDateTag} meas / model w free params\n"
                f" from {os.path.basename(pydarmparams)}"),
            fmt='.')

    # Add legends
    tfp.legend()
    rp.legend()

    # Wrap up and save figure
    plt.tight_layout()
    fig.savefig(
        os.path.join(
            args.sensing_output_dir,
            f"sensing_tf_history_{measDateTag}_{latestMeasDateTag}.png"))


def run_sensing_MCMC(processedSensing, args, measDateTag, C_ref):
    # Run the MCMC chain
    mcmcChains = np.transpose(
        processedSensing.run_mcmc(
            fmin=args.mcmc_fmin,
            fmax=args.mcmc_fmax,
            burn_in_steps=args.mcmc_burn_in,
            steps=args.mcmc_steps,
            save_to_file=os.path.join(
                args.sensing_output_dir,
                f"sensing_mcmc_params_{measDateTag}.json")))

    # Set up a dict of dicts to hold the mcmc parameter information
    mcmcParams = {
        'opticalGain': {
            'label': 'Optical gain, H_c (ct/m)',
            'mathlabel': r'$H_C$'},
        'cavityPole': {
            'label': 'Cavity_pole, f_cc (Hz)',
            'mathlabel': r'$f_{cc}$'},
        'springF': {
            'label': 'Detuned SRC spring frequency, f_s (Hz)',
            'mathlabel': r'$f_s$'},
        'springQ': {
            'label': 'Detuned SRC spring quality factor, Q_s',
            'mathlabel': r'$Q$'},
        'resDelay': {
            'label': 'Residual time delay, tau_c (s)',
            'mathlabel': r'$\Delta\tau_C$'},
        }

    # Set up the quantile levels
    quantileLevels = np.array([0.16, 0.5, 0.84])

    # Loop over params and store relevant information into the dict
    for i, param in enumerate(mcmcParams.values()):
        quantiles = corner.quantile(
                                mcmcChains[i],
                                quantileLevels)
        param['median'] = quantiles[1]
        param['errplus'] = quantiles[2]-quantiles[1]
        param['errminus'] = quantiles[1]-quantiles[0]
        param['quantiles'] = quantiles

    if mcmcParams['resDelay']['median'] >= 5e-3:  # TODO: make user arg
        print(
            "Warning: MCMC fit for residual delay is high"
            f" at {mcmcParams['resDelay']['median']:.2f} s")

    # Make corner plot
    make_corner_plot(
        mcmcChains, mcmcParams, quantileLevels,
        os.path.join(args.sensing_output_dir, f"sensing_mcmc_corner_{measDateTag}.png"),
        f"{measDateTag} sensing function MCMC corner plot")

    # Add additional entry for kappa_c so that values can be printed
    mcmcParams['kappa_c'] = {
        'label': 'kappa_c',
        'mathlabel': r'$kappa_c$'
        }

    for key in ['median', 'errplus', 'errminus', 'quantiles']:
        mcmcParams['kappa_c'][key] = (
            mcmcParams['opticalGain'][key]
            / C_ref.coupled_cavity_optical_gain)

    # Print out and parameter value table
    mcmcTableQuant, mcmcTablePM = print_mcmc_params(mcmcParams, quantileLevels)
    if args.mcmc_print:
        print(f"\n{mcmcTableQuant}")
        print(f"\n{mcmcTablePM}\n")

    return mcmcParams, mcmcTableQuant, mcmcTablePM


def str_to_bool(choice):
    # TODO docstring
    return bool(str(choice).lower() in ('yes', 'y', 'true', 't', '1'))


def str_path(s):
    # TODO docstringg
    return os.path.abspath(os.path.expanduser(s))


def path_tup(s):
    # TODO docstring
    pieces = s.split(",")
    assert len(pieces) == 2
    pieces = [str_path(p) for p in pieces]
    return tuple(pieces)


def extract_date_general(path):
    start = r"(?:(?<=^)|(?<=_))"
    end = r"(?:(?=$)|(?=_))"
    rexs = [r"(\d{4}-\d{2}-\d{2})", r"(\d{8})"]
    fmts = ["%Y-%m-%d", "%Y%m%d"]

    rexs = [start+r+end for r in rexs]
    matches = []
    matchfmts = []
    bname = os.path.splitext(os.path.basename(path))[0]
    for i, rex in enumerate(rexs):
        matchlist = re.findall(rex, bname)
        if len(matchlist) > 0:
            matches += matchlist
            matchfmts = [fmts[i]]
    if len(matches) == 1:
        dt = datetime.strptime(matches[0], matchfmts[0])
        return dt
    elif len(matchlist) > 1:
        raise Exception(f"Multiple date strings found in filename {path}")
    else:
        print(f"No date found in filename for {path}.")


def patterns_to_xml_pairs(s):
    patterns = s.split(",")
    if len(patterns) != 2:
        raise Exception(f"Could not process {s} as a pair of comma-separated patterns")
    fnames = []
    for pattern in patterns:
        pattern = str_path(pattern)
        fnames += [sorted(glob(pattern))]
    if len(fnames[0]) != len(fnames[1]):
        raise Exception(
            f"Pattern {patterns[0]} matches {len(fnames[0])} files while"
            f"{patterns[1]} matches {len(fnames[1])} files.")
    for i in range(len(fnames[0])):
        if extract_date_general(fnames[0][i]) != extract_date_general(fnames[1][i]):
            raise Exception(
                f"Matched file sets do not have aligned dates."
                f" {fnames[0][i]} and {fnames[1][i]} do not align.")
    return list(zip(fnames[0], fnames[1]))


def main():
    # TODO docstring
    # FUTURE amend to include actuation
    parser = argparse.ArgumentParser()
    parser.register('type', 'bool', str_to_bool)
    parser.register('type', 'path_tups', patterns_to_xml_pairs)
    parser.register('type', 'path', str_path)

    parser.add_argument("--pydarmparams", type='path', required=True)

    parser.add_argument(
        "--sensing-xml-pair", type='path_tups', required=True, nargs="+",
        help="Specify two measurement XML files from the same date follows:"
        " \"<loop measurement file>,<pcal measurement file>\" . Note that you"
        " can use wildcards (\"*\") in place of dates; the most recent"
        " measurement(s) will be used.")
    parser.add_argument(
        "--sensing-n-meas", type=int, default=5,
        help="N most recent measurements to plot from the matching patterns.")
    parser.add_argument("--sensing-output-dir", type='path', default=None)
    parser.add_argument("--cohthresh-loop-meas", type=float, default=0.9)
    parser.add_argument("--cohthresh-pcal-meas", default=0.9)

    parser.add_argument("--run-mcmc", default=True)
    parser.add_argument("--mcmc-burn-in", default=100)
    parser.add_argument("--mcmc-steps", type=int, default=900)
    parser.add_argument("--mcmc-fmin", type=float, default=20.0)
    parser.add_argument("--mcmc-fmax", type=float, default=1.2e3)
    parser.add_argument("--mcmc-print", type='bool', default=True)

    args = parser.parse_args()

    sensing(args)


if __name__ == "__main__":
    main()
