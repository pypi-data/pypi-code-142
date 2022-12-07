import tensorflow as tf
from tensorflow.keras.layers import Bidirectional, Flatten, Dense, Dropout, LSTM, Input


class BiLSTM(tf.keras.Model):
    def __init__(self, n_steps, n_features, n_outputs=1):
        super(BiLSTM, self).__init__()
        self.n_steps = n_steps
        self.n_features = n_features
        self.n_outputs = n_outputs
        self.blstm1 = Bidirectional(LSTM(128, activation='relu', return_sequences=True))
        self.blstm2 = Bidirectional(LSTM(64, activation='relu'))
        self.flatten = Flatten()
        self.fc1 = Dense(32, activation='relu')
        self.drp = Dropout(0.2)
        self.fc2 = Dense(self.n_outputs)

    def call(self, inputs):
        x = self.blstm1(inputs)
        x = self.blstm2(x)
        x = self.flatten(x)
        x = self.fc1(x)
        x = self.drp(x)
        x = self.fc2(x)
        return x

    def getModel(self):
        inp = Input(shape=(self.n_steps, self.n_features))
        x = BiLSTM(self.n_steps, self.n_features, self.n_outputs)(inp)
        model = tf.keras.Model(inputs=inp, outputs=x)
        return model



