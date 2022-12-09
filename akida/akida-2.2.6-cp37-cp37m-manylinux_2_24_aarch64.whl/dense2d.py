from akida.core import (Layer, LayerParams, LayerType)


class Dense2D(Layer):
    """Dense layer capable of working on 2D inputs.

    The 2D Dense operation is simply the repetition of a 1D
    FullyConnected/Dense operation over each input row.
    Inputs shape mush be in the form (1, X, Y). Being the result of a quantized
    operation, it is possible to apply some shifts to adjust the inputs/outputs
    scales to the equivalent operation performed on floats, while maintaining
    a limited usage of bits and performing the operations on integer values.

    The 2D Dense operation can be described as follows:

        >>> inputs = inputs << input_shift
        >>> prod = matmul(inputs, weights) * weights_scale
        >>> prod = prod << prod_shift
        >>> bias = bias << bias_shift
        >>> output = prod + bias
        >>> output = output >> output_shift

    Inputs shape must be (1, X, Y). Note that output values will be saturated
    on the range that can be represented with output_bits.

    Args:
        units (int): Positive integer, dimensionality of the output space.
        weights_bits (int, optional): number of bits used to quantize weights.
        weights_scale_bits (int, optional): number of bits used to quantize
            weights scales.
        bias_bits (int, optional): number of bits used to quantize bias.
        output_bits (int): output bitwidth.
        buffer_bits (int): buffer bitwidth.
        name (str, optional): name of the layer.

    """

    def __init__(self,
                 units,
                 weights_bits=4,
                 weights_scale_bits=8,
                 bias_bits=8,
                 output_bits=8,
                 buffer_bits=23,
                 name=""):
        try:
            params = LayerParams(
                LayerType.Dense2D, {
                    "units": units,
                    "weights_bits": weights_bits,
                    "weights_scale_bits": weights_scale_bits,
                    "bias_bits": bias_bits,
                    "output_bits": output_bits,
                    "buffer_bits": buffer_bits
                })
            # Call parent constructor to initialize C++ bindings
            # Note that we invoke directly __init__ instead of using super, as
            # specified in pybind documentation
            Layer.__init__(self, params, name)
        except BaseException:
            self = None
            raise
