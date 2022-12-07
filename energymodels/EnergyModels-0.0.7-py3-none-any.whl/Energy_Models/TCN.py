import numpy as np
import keras.layers
import tensorflow as tf
import keras.backend as K
from keras.models import Model
from keras.layers import Lambda, SpatialDropout1D, Activation, Convolution1D, GlobalMaxPooling1D
from tensorflow.keras.layers import Dense, Dropout, Input, Conv1D


class TCN_Model:
    class TCN_layer:
        def channel_normalization(self, x):
            max_values = K.max(K.abs(x), 2, keepdims=True) + 1e-5
            out = x / max_values
            return out

        def residual_block(self, x, s, i, activation, nb_filters, kernel_size, padding, dropout_rate=0, name=''):
            original_x = x
            conv = Conv1D(filters=nb_filters, kernel_size=kernel_size,
                          dilation_rate=i, padding=padding,
                          name=name + '_dilated_conv_%d_tanh_s%d' % (i, s))(x)
            if activation == 'norm_relu':
                x = Activation('relu')(conv)
                x = Lambda(self.channel_normalization)(x)
            else:
                x = Activation(activation)(conv)

            x = SpatialDropout1D(dropout_rate, name=name + '_spatial_dropout1d_%d_s%d_%f' % (i, s, dropout_rate))(x)

            # 1x1 conv.
            x = Convolution1D(nb_filters, 1, padding='same')(x)
            res_x = keras.layers.add([original_x, x])
            return res_x, x

        def __init__(self,
                     nb_filters=64,
                     kernel_size=2,
                     nb_stacks=1,
                     dilations=None,
                     activation='norm_relu',
                     padding='causal',
                     use_skip_connections=True,
                     dropout_rate=0.0,
                     return_sequences=True,
                     name='tcn'):

            self.name = name
            self.return_sequences = return_sequences
            self.dropout_rate = dropout_rate
            self.use_skip_connections = use_skip_connections
            self.activation = activation
            self.dilations = dilations
            self.nb_stacks = nb_stacks
            self.kernel_size = kernel_size
            self.nb_filters = nb_filters
            self.padding = padding

            if padding != 'causal' and padding != 'same':
                raise ValueError("Only 'causal' or 'same' paddings are compatible for this layer.")

            if not isinstance(nb_filters, int):
                print('An interface change occurred after the version 2.1.2.')
                print('Before: tcn.TCN(i, return_sequences=False, ...)')
                print('Now should be: tcn.TCN(return_sequences=False, ...)(i)')
                print('Second solution is to pip install keras-tcn==2.1.2 to downgrade.')
                raise Exception()

        def __call__(self, inputs):
            if self.dilations is None:
                self.dilations = [1, 2, 4, 8, 16, 32]
            x = inputs
            x = Convolution1D(self.nb_filters, 1, padding=self.padding, name=self.name + '_initial_conv')(x)
            skip_connections = []
            for s in range(self.nb_stacks):
                for i in self.dilations:
                    x, skip_out = self.residual_block(x, s, i, self.activation, self.nb_filters,
                                                      self.kernel_size, self.padding, self.dropout_rate, name=self.name)
                    skip_connections.append(skip_out)
            if self.use_skip_connections:
                x = keras.layers.add(skip_connections)
            x = Activation('relu')(x)

            if not self.return_sequences:
                output_slice_index = -1
                x = Lambda(lambda tt: tt[:, output_slice_index, :])(x)
            return x

    def getModel(self,
                 n_steps,
                 n_features,
                 n_outputs=1,
                 #  X, y,
                 tcn1_units=128,
                 tcn2_units=64,
                 tcn1_kernel_size=5,
                 tcn2_kernel_size=1,
                 activation="relu",
                 return_sequences=True,
                 dropout=0.2):

        input = Input(shape=(n_steps, n_features))
        output = n_outputs

        x = SpatialDropout1D(dropout)(input)

        x = TCN_Model.TCN_layer(tcn1_units,
                                dilations=[1, 2, 4, 8, 16],
                                kernel_size=tcn1_kernel_size,
                                return_sequences=return_sequences,
                                name='tnc1')(x)

        x = TCN_Model.TCN_layer(tcn2_units,
                                dilations=[1, 2, 4],
                                kernel_size=tcn2_kernel_size,
                                return_sequences=return_sequences,
                                name='tnc2')(x)

        max_pool = GlobalMaxPooling1D()(x)
        x = Dense(tcn2_units, activation=activation)(max_pool)
        x = Dropout(dropout)(x)
        output = Dense(output)(x)
        model = Model(inputs=input, outputs=output)

        return model


