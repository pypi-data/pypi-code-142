import tensorflow as tf
from tensorflow.keras.layers import Bidirectional, Flatten, Dense, Dropout, Input, GRU


class BiGRU(tf.keras.Model):
    def __init__(self, n_steps, n_features, n_outputs=1):
        super(BiGRU, self).__init__()
        self.n_steps = n_steps
        self.n_features = n_features
        self.n_outputs = n_outputs
        self.bigru_1 = Bidirectional(GRU(256, activation='tanh', return_sequences=True))
        self.dropout_1 = Dropout(0.3)
        self.bigru_2 = Bidirectional(GRU(128, activation='tanh', return_sequences=True))
        self.bigru_3 = Bidirectional(GRU(64, activation='tanh', return_sequences=True))
        self.dropout_2 = Dropout(0.2)
        self.bigru_4 = Bidirectional(GRU(32, activation='tanh'))
        self.flatten_1 = Flatten()
        self.dropout_3 = Dropout(0.2)
        self.dense_1 = Dense(10, activation='softmax')
        self.flatten_2 = Flatten()
        self.dropout_4 = Dropout(0.1)
        self.dense_2 = Dense(self.n_outputs)

    def call(self, x):
        x = self.bigru_1(x)
        x = self.dropout_1(x)
        x = self.bigru_2(x)
        x = self.bigru_3(x)
        x = self.dropout_2(x)
        x = self.bigru_4(x)
        x = self.flatten_1(x)
        x = self.dropout_3(x)
        x = self.dense_1(x)
        x = self.flatten_2(x)
        x = self.dropout_4(x)
        x = self.dense_2(x)
        return x

    def getModel(self):
        inp = Input(shape=(self.n_steps, self.n_features))
        x = BiGRU(self.n_steps, self.n_features, self.n_outputs)(inp)
        model = tf.keras.Model(inputs=inp, outputs=x)
        return model


