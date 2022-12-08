"""
:py:class:`pynibs.congruence` holds the initial congruence factor implementation as described in Weise, Numssen, et al., 2020 [1]_.
This code is mainly stored here for reproducibility reasons. The current approach (Numssen et al., 2021; [2]_) uses
the :py:class:`pynibs.regression` methods.

References
----------
.. [1] Weise, K., Numssen, O., Thielscher, A., Hartwigsen, G., & Knösche, T. R. (2020).
   A novel approach to localize cortical TMS effects. Neuroimage, 209, 116486.
.. [2] Numssen, O., Zier, A. L., Thielscher, A., Hartwigsen, G., Knösche, T. R., & Weise, K. (2021).
   Efficient high-resolution TMS mapping of the human motor cortex by nonlinear regression. NeuroImage, 245, 118654.
"""
from .congruence import *
from .ext_metrics import *
from .stimulation_threshold import *
