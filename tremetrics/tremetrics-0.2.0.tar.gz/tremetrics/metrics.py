import matplotlib.pyplot as plt
import numpy as np
import sklearn.metrics as skmetrics
from sklearn.utils.multiclass import unique_labels


class ConfusionMatrix:

    def __init__(self, y_true=None, y_pred=None):
        self.y_true_ = y_true
        self.y_pred_ = y_pred
        self.labels_ = None

    @staticmethod
    def unique_labels(*ys):
        return unique_labels(*ys)

    @classmethod
    def from_pred(cls, y_true, y_pred):
        """
        Initialize a new ConfusionMatrix object with the given observations.
        Parameters
        ----------
        y_true : ndarray
            Ground-truth observations.
        y_pred : ndarray
            Predictions.

        Returns
        -------
        cm : ConfusionMatrix
            A new ConfusionMatrix object.
        """
        cm = ConfusionMatrix()
        cm.y_true_ = y_true
        cm.y_pred_ = y_pred
        return cm

    @classmethod
    def from_pred_prob(cls, y_true, y_pred_prob, decision=None):
        """
        Initialize a new ConfusionMatrix object with the given observations.
        Parameters
        ----------
        y_true : ndarray
            Ground-truth observations.
        y_pred_prob : ndarray
            Predicted probabilities.
        decision : func
            A decision function that accepts a row from `y_pred_prob` and returns a prediction value.

        Returns
        -------
        cm : ConfusionMatrix
            A new ConfusionMatrix object.
        """
        if decision is None:
            decision = lambda p: int(p >= 0.5)
        decision = np.vectorize(decision)

        cm = ConfusionMatrix()
        cm.y_true_ = y_true
        cm.y_pred_ = decision(y_pred_prob)
        return cm

    def set_labels(self, labels):
        self.labels_ = labels
        return self

    def _get_array(self, labels=None):
        if self.y_true_ is not None and self.y_pred_ is not None:
            return skmetrics.confusion_matrix(self.y_true_, self.y_pred_, labels=labels)
        else:
            raise ValueError("No y_true or y_pred specified. "
                             "Use ConfusionMatrix.from_pred(y_true, y_pred) as constructor.")

    def _get_binary_array(self):
        try:
            return self._get_array(labels=[1, 0])
        except ValueError as e:
            if str(e) != "At least one label specified must be in y_true": raise e
            else:
                try:
                    return self._get_array(labels=[True, False])
                except ValueError as e:
                    if str(e) != "At least one label specified must be in y_true": raise e
                    else:
                        raise ValueError("Input is not binary. Use (0, 1) or boolean values instead.")

    @property
    def array(self):
        if self.labels_ is None:
            # Try to make sure True Positives are in the upper-left.
            # Otherwise, default to standard sklearn sorted order.
            try:
                return self._get_binary_array()
            except ValueError as e:
                if str(e) != "Input is not binary. Use (0, 1) or boolean values instead.": raise e
                else:
                    return self._get_array()
        else:
            return self._get_array(labels=self.labels_)

    def __repr__(self):
        return repr(self.array)

    @property
    def _values(self):
        """
        Get binary matrix values as a contiguous flattened array.
        Returns
        -------
        y : ndarray
            A 1-D array containing binary matrix values.
        """
        return self._get_binary_array().ravel()

    @property
    def tp(self):
        """
        True positives (TP).
        """
        return self._values[0]

    @property
    def fn(self):
        """
        False negatives (FN).
        """
        return self._values[1]

    @property
    def fp(self):
        """
        False positives (FP).
        """
        return self._values[2]

    @property
    def tn(self):
        """
        True negatives (TN).
        """
        return self._values[3]

    @property
    def total(self):
        return np.sum(self._values)

    def get_latex_table(self, multirow=True):
        """
        Generate Latex code to insert this confusion matrix as a table.

        Parameters
        ----------
        multirow : bool, default=True
            Whether to use the Latex package `multirow`, which is needed for rotating the left-hand table labels.
            If so, include `usepackage{multirow}` in your Latex preamble.

        Returns
        -------
        code : str
            Latex code to use in your tex file.
        """
        if multirow:
            actual = "\\multirow[c]{2}{*}{\\rotatebox[origin=center]{90}{Actual}}"
        else:
            actual = "{Actual}"

        code = "\\begin{tabular}{cc|cc}\n" \
               "\\multicolumn{2}{c}{} & \\multicolumn{2}{c}{Predicted} \\\\\n" \
               "& & Positive & Negative \\\\\n" \
               "\\cline{2-4}\n" \
               "%(actual)s\n" \
               "& Positive & %(tp)d & %(fn)d \\\\[1ex]\n" \
               "& Negative & %(fp)d & %(tn)d \\\\\n" \
               "\\cline{2-4}\n" \
               "\\end{tabular}" % {'tp': self.tp, 'fn': self.fn, 'fp': self.fp, 'tn': self.tn, 'actual': actual}
        return code

    def plot(self, ax=None, cmap=plt.cm.Blues):
        if self.labels_ is None:
            try:
                return skmetrics.ConfusionMatrixDisplay(self._get_binary_array(), display_labels=[True, False]).plot(ax=ax, cmap=cmap)
            except ValueError: pass
        return skmetrics.ConfusionMatrixDisplay(self.array, display_labels=self.unique_labels(self.y_true_, self.y_pred_)).plot(ax=ax, cmap=cmap)

    def __getattr__(self, name):
        """
        Forward unknown method calls to sklearn.metrics, supplying y_true and y_pred as additional attributes.

        Example
        -------
            self.recall_score(average='micro') -> sklearn.metrics.recall_score(self.y_true_, self.y_pred_, average='micro')
        """
        def _missing(*args, **kwargs):
            method = getattr(skmetrics, name)
            return method(self.y_true_, self.y_pred_, *args, **kwargs)

        return _missing


class ROCCurve:

    def __init__(self):
        self.classifier_ = None
        self.y_true_ = None
        self.y_pred_ = None
        self.y_pred_prob_ = None
        self.pos_label_ = 1
        self.convex_ = None

    @classmethod
    def from_pred_prob(cls, y_true, y_pred_prob, convex=False):
        # y_pred_prob can be:
        #     - scores, can be probabilities or pseudo-probabilities
        #     - predicted values (only binary)
        rc = ROCCurve()
        rc.y_true_ = y_true
        rc.y_pred_prob_ = y_pred_prob
        rc.convex_ = convex
        return rc

    def set_pos_label(self, value):
        self.pos_label_ = value
        return self

    @staticmethod
    def roc_curve(y_true, y_pred_prob, pos_label=None, drop_intermediate=True):
        fprs, tprs, thresholds = skmetrics.roc_curve(y_true, y_pred_prob, pos_label=pos_label, drop_intermediate=drop_intermediate)
        if not drop_intermediate:
            return fprs, tprs, thresholds

        # Filter out unnecessary ROC thresholds
        # See https://gitlab.com/BCLegon/tremetrics/-/snippets/2467111
        fprs_new, tprs_new, thresholds_new = [], [], []
        for i in range(len(thresholds)):
            if i >= 2 and fprs[i] == fprs_new[-1] and fprs[i] == fprs_new[-2] and tprs[i] >= tprs_new[-1]:
                tprs_new[-1] = tprs[i]
                thresholds_new[-1] = thresholds[i]
            else:
                fprs_new.append(fprs[i])
                tprs_new.append(tprs[i])
                thresholds_new.append(thresholds[i])

        return fprs_new, tprs_new, thresholds_new

    @staticmethod
    def convex_roc_curve(y_true, y_pred_prob, pos_label=None):
        fprs, tprs, thresholds = ROCCurve.roc_curve(y_true, y_pred_prob, pos_label=pos_label, drop_intermediate=True)
        args_convex, thresholds = ROCCurve._args_convex_roc_curve(y_true, y_pred_prob, pos_label=pos_label)
        return np.array(fprs)[args_convex], np.array(tprs)[args_convex], np.array(thresholds)[args_convex]

    @staticmethod
    def _args_convex_roc_curve(y_true, y_pred_prob, pos_label=None):
        # Implementation of Graham Scan for ROC thresholds
        fprs, tprs, thresholds = ROCCurve.roc_curve(y_true, y_pred_prob, pos_label=pos_label, drop_intermediate=True)

        args = []
        for i in range(len(thresholds)):
            while True:
                if len(args) < 2:
                    break
                orientation = ROCCurve._get_orientation(
                    (fprs[args[-1]], tprs[args[-1]]),
                    (fprs[i], tprs[i]),
                    (fprs[args[-2]], tprs[args[-2]])
                )
                if orientation > 0:
                    args.pop()
                else:
                    break
            args.append(i)
        return np.array(args), np.array(thresholds)

    @staticmethod
    def _get_orientation(origin, point_a, point_b):
        # vector product of v(origin, point_a) and v(origin, point_b)
        # only valid in two dimensions
        return (point_a[0] - origin[0]) * (point_b[1] - origin[1])\
               - (point_a[1] - origin[1]) * (point_b[0] - origin[0])

    @property
    def _values(self):
        if self.convex_:
            return self.convex_roc_curve(self.y_true_, self.y_pred_prob_, pos_label=self.pos_label_)
        else:
            return self.roc_curve(self.y_true_, self.y_pred_prob_, pos_label=self.pos_label_)

    @property
    def fprs(self):
        return self._values[0]

    @property
    def tprs(self):
        return self._values[1]

    @property
    def thresholds(self):
        return self._values[2]

    @property
    def roc_auc(self):
        if self.convex_:
            # Sort ground-truth and probabilities in ascending order of probabilities, then descending order of GT
            inverse_y_true_ = (np.array(self.y_true_) != self.pos_label_)
            sort_args = np.lexsort((inverse_y_true_, self.y_pred_prob_))
            adjusted_true, adjusted_prob = np.array(self.y_true_)[sort_args], np.array(self.y_pred_prob_)[sort_args]
            # Find the thresholds that determine the convex hull
            args_convex, thresholds = ROCCurve._args_convex_roc_curve(adjusted_true, adjusted_prob, pos_label=self.pos_label_)

            # Set all probabilities to values that determine the convex hull
            last_threshold = adjusted_prob[0]
            for i in range(0, len(adjusted_prob)):
                if adjusted_prob[i] in thresholds[args_convex]:
                    last_threshold = adjusted_prob[i]
                else:
                    adjusted_prob[i] = last_threshold

            # Compute the AUC in the traditional way using the adjusted probabilities
            return skmetrics.roc_auc_score(adjusted_true, adjusted_prob)
        else:
            return skmetrics.roc_auc_score(self.y_true_, self.y_pred_prob_)

    def plot(self, label=None, ax=None, alpha=0.75, show_thresholds=True, show_random=True, thresholds_above=True):
        if ax is None:
            ax = plt.gca()
        if label is None:
            label = 'AUC = %0.2f' % (self.roc_auc,)
        else:
            label = '%s (AUC = %0.2f)' % (label, self.roc_auc)
        plot_ = ax.plot(
            self.fprs, self.tprs,
            label=label,
            marker='.', alpha=alpha
        )
        color = plot_[-1].get_color()
        if show_random:
            ax.plot([0, 1], [0, 1], linestyle='--', color='grey', label='Random Generator')
        if show_thresholds:
            for x, y, s in zip(self.fprs, self.tprs, self.thresholds):
                if thresholds_above:
                    x, y = x - 0.07, y + 0.02  # top-left
                else:
                    x, y = x + 0.005, y - 0.05  # bottom-right
                plt.text(x, y, '%0.2f' % (s,), fontdict={'size': 10}, color=color, alpha=alpha)
        ax.set_xlabel('False Positive Rate')
        ax.set_ylabel('True Positive Rate')
        ax.legend(loc='lower right')
