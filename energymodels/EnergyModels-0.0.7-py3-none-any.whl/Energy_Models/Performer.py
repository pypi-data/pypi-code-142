import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

from performer.networks.linear_attention import Performer


class TokenAndPositionEmbedding(layers.Layer):
    def __init__(self, maxlen, vocab_size, embed_dim):
        super(TokenAndPositionEmbedding, self).__init__()
        self.token_emb = layers.Embedding(input_dim=vocab_size, output_dim=embed_dim)
        self.pos_emb = layers.Embedding(input_dim=maxlen, output_dim=embed_dim)

    def call(self, x):
        maxlen = tf.shape(x)[-1]
        positions = tf.range(start=0, limit=maxlen, delta=1)
        positions = self.pos_emb(positions)
        x = self.token_emb(x)
        return x + positions


class TransformerBlock(layers.Layer):
    def __init__(self, embed_dim, num_heads, ff_dim, method, supports, rate=0.1):
        super(TransformerBlock, self).__init__()
        self.att = Performer(num_heads=num_heads, key_dim=embed_dim,
                             attention_method=method, supports=supports)
        self.ffn = keras.Sequential(
            [layers.Dense(ff_dim, activation="relu"), layers.Dense(embed_dim), ]
        )
        self.layernorm1 = layers.LayerNormalization(epsilon=1e-6)
        self.layernorm2 = layers.LayerNormalization(epsilon=1e-6)
        self.dropout1 = layers.Dropout(rate)
        self.dropout2 = layers.Dropout(rate)

    def call(self, inputs, training):
        attn_output = self.att([inputs, inputs])
        attn_output = self.dropout1(attn_output, training=training)
        out1 = self.layernorm1(inputs + attn_output)
        ffn_output = self.ffn(out1)
        ffn_output = self.dropout2(ffn_output, training=training)
        return self.layernorm2(out1 + ffn_output)


class Performer_model(tf.keras.Model):
    def __init__(self,
                 maxlen,
                 n_features,
                 n_outputs,
                 vocab_size,
                 embed_dim,
                 num_heads,
                 ff_dim,
                 method="linear",
                 supports=10,
                 rate=0.1):
        super(Performer_model, self).__init__()

        self.maxlen = maxlen
        self.n_features = n_features
        self.n_outputs = n_outputs
        self.vocab_size = vocab_size
        self.embed_dim = embed_dim
        self.num_heads = num_heads
        self.ff_dim = ff_dim
        self.method = method
        self.supports = supports
        self.rate = rate

    def getModel(self):
        inp = layers.Input(shape=(self.n_features,))
        x = TokenAndPositionEmbedding(self.maxlen, self.vocab_size, self.embed_dim)(inp)
        x = TransformerBlock(self.embed_dim, self.num_heads, self.ff_dim, self.method, self.supports, self.rate)(x)
        x = layers.GlobalAveragePooling1D()(x)
        x = layers.Dropout(0.1)(x)
        x = layers.Dense(20, activation="relu")(x)
        x = layers.Dropout(0.1)(x)
        x = layers.Dense(self.n_outputs, activation="relu")(x)

        model = tf.keras.Model(inputs=inp, outputs=x)
        return model


