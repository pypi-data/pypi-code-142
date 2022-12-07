from tensorflow import keras
from tensorflow.keras import layers
class Transformer:  
    
    def __init__(self,
           input_shape,
           n_outputs,
           head_size,
           num_heads,
           ff_dim,
           num_transformer_blocks,
           mlp_units,
           dropout=0,
           mlp_dropout=0,):
        self.input_shape=input_shape
        self.n_outputs=n_outputs
        self.head_size=head_size
        self.num_heads=num_heads
        self.ff_dim=ff_dim
        self.num_transformer_blocks=num_transformer_blocks
        self.mlp_dropout=mlp_dropout
        self.dropout=dropout
        self.mlp_units=mlp_units
    
    def transformer_encoder(inputs, head_size, num_heads, ff_dim, dropout=0):
        # Normalization and Attention
        x = layers.LayerNormalization()(inputs)
        x = layers.MultiHeadAttention(
            key_dim=head_size, num_heads=num_heads, dropout=dropout
        )(x, x)
        x = layers.Dropout(dropout)(x)
        res = x + inputs
    
        # Feed Forward Part
        x = layers.LayerNormalization()(res)
        x = layers.Conv1D(filters=ff_dim, kernel_size=1, activation="relu")(x)
        x = layers.Dropout(dropout)(x)
        x = layers.Conv1D(filters=inputs.shape[-1], kernel_size=1)(x)
        return x + res
    def build_model(self):
        inputs = keras.Input(shape=self.input_shape)
        x = inputs
        for _ in range(self.num_transformer_blocks):
            x = Transformer.transformer_encoder(x, self.head_size, self.num_heads, self.ff_dim, self.dropout)
    
        x = layers.GlobalAveragePooling1D()(x)
        for dim in self.mlp_units:
            x = layers.Dense(dim, activation="relu")(x)
            x = layers.Dropout(self.mlp_dropout)(x)
        outputs = layers.Dense(self.n_outputs, activation="linear")(x)
        return keras.Model(inputs, outputs)