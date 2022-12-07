"""Initializers for PyTorch similar to torch.nn.init, but for use with functorch.

All the initializers in this module take in a `generator` argument, which expects a
torch.Generator object. This is necessary because the initializers in this module
are used in conjunction with functorch, which requires that modules be stateless.

The typical use case is to create a generator object, seed it, and then pass it to
the initializers to generate the initial parameters for a module. For example:

```python
import torch
import functorch as ft

# Create a generator and seed it.
generator = torch.Generator(device='cpu')
generator.manual_seed(0)

# Create a functorch extracted module.
module = torch.nn.Sequential(...)
module_func, params, buffers = ft.make_functional_with_buffers(module)

# Create params for the module like this:
# TODO: Document the behaviour of how the generator's device affects the device of
# the generated parameters.
new_params = init_like_params(params, generator, uniform_like, a=-0.1, b=0.1)
x = torch.randn(3, 5)
output = module_func(new_params, buffers, x)
```
"""
from torchsilk.init.core import *  # noqa: F401, F403
from torchsilk.init.orthogonal import *  # noqa: F401, F403
from torchsilk.init.type_defs import *  # noqa: F401, F403
from torchsilk.init.uniform import *  # noqa: F401, F403
from torchsilk.init.xavier import *  # noqa: F401, F403
