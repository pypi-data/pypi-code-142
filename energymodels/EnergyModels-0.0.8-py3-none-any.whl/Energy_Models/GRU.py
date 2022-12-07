import tensorflow as tf
from tensorflow.keras.layers import  Dense, Dropout, Input, GRU


class GRU_model(tf.keras.Model):
    def __init__(self, n_steps, n_features, n_outputs=1):
        super(GRU_model, self).__init__()
        self.n_steps = n_steps
        self.n_features = n_features
        self.n_outputs = n_outputs
        self.gru_1 = GRU(300, activation='tanh', return_sequences=True)
        self.gru_2 = GRU(200, activation='tanh', return_sequences=True)
        self.dropout_1 = Dropout(0.2)
        self.gru_3 = GRU(100, activation='tanh', return_sequences=True)
        self.gru_4 = GRU(50, activation='tanh')
        self.dropout_2 = Dropout(0.2)
        self.dense_1 = Dense(20, activation='softmax')
        self.dense_2 = Dense(self.n_outputs)

    def call(self, x):
        x = self.gru_1(x)
        x = self.gru_2(x)
        x = self.dropout_1(x)
        x = self.gru_3(x)
        x = self.gru_4(x)
        x = self.dropout_2(x)
        x = self.dense_1(x)
        x = self.dense_2(x)
        return x

    def getModel(self):
        inp = Input(shape=(self.n_steps, self.n_features))
        x = GRU_model(self.n_steps, self.n_features, self.n_outputs)(inp)
        model = tf.keras.Model(inputs=inp, outputs=x)
        return model



