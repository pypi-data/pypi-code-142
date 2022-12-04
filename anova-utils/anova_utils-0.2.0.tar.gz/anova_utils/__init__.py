"""EFA Utilities (efa_utils)
Custom utility functions for conducting ANOVAs (or ANCOVAs).

Functions:
tukey_outliers: Function to identify outliers using the Tukey method.
qqs_over_groups_and_vars: Function to plot QQ subplots for each variable in a list of variables, over groups in a categorical variable.
check_homoscedacity: Function to check for homoscedacity using heuristics recommended by Blanca et al. (2018).
compare_var_mult_groups: Function to compare the variance of a variable across multiple groups (omnibus test & posthoc).
"""

from anova_utils.anova_utils_functions import *