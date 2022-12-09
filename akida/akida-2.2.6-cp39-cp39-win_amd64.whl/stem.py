from akida.core import (Layer, LayerParams, LayerType)


class Stem(Layer):
    """Stem layer corresponding to the Stem block of Transformer models.

    It's composed of the following layers:

        - The Embedding layer
        - The Reshape layer
        - The ClassToken (+ DistToken for distilled model) layer(s)
        - The AddPosEmbedding layer

    This layer covers all the above layers operations.

    Note that final output values will be saturated on the range that can
    be represented with output_bits.

    Note: For now only the convolution operation of the Embedding layer
    is covered and the final output quantization.

    Args:
        input_shape (tuple): the spatially square 3D input shape.
        filters (int, optional): Positive integer, dimensionality of the output space.
            Defaults to 192.
        kernel_size (int, optional): kernel size. Defaults to 16.
        weights_bits (int, optional): number of bits used to quantize weights.
            Defaults to 4.
        weights_scale_bits (int, optional): number of bits used to quantize
            weights scales. Defaults to 8.
        bias_bits (int, optional): number of bits used to quantize the bias.
            Defaults to 8.
        output_bits (int, optional): output bitwidth. Defaults to 8.
        buffer_bits (int, optional): buffer bitwidth. Defaults to 31.
        collapse_spatial_dims (bool, optional): boolean to trigger the output spatial
            dimensions collapse. Defaults to True.
        name (str, optional): name of the layer. Defaults to 'Stem'.

    """

    def __init__(self,
                 input_shape,
                 filters=192,
                 kernel_size=16,
                 weights_bits=4,
                 weights_scale_bits=8,
                 bias_bits=8,
                 output_bits=8,
                 buffer_bits=31,
                 collapse_spatial_dims=True,
                 name="Stem"):
        try:
            if (input_shape[0] != input_shape[1]):
                raise ValueError(
                    "input should have square spatial dimensions."
                    f"Receives x_size={input_shape[0]} and y_size={input_shape[1]}"
                )

            params = LayerParams(
                LayerType.Stem, {
                    "input_spatial_size": input_shape[0],
                    "input_channels": input_shape[2],
                    "filters": filters,
                    "kernel_size": kernel_size,
                    "weights_bits": weights_bits,
                    "weights_scale_bits": weights_scale_bits,
                    "bias_bits": bias_bits,
                    "output_bits": output_bits,
                    "buffer_bits": buffer_bits,
                    "collapse_spatial_dims": collapse_spatial_dims
                })
            # Call parent constructor to initialize C++ bindings
            # Note that we invoke directly __init__ instead of using super, as
            # specified in pybind documentation
            Layer.__init__(self, params, name)
        except BaseException:
            self = None
            raise
