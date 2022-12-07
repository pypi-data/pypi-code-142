import tensorflow as tf
from tensorflow.keras.layers import  Dense, Dropout, LSTM, Input


class lstm(tf.keras.Model):
    def __init__(self, n_steps, n_features, n_outputs=1):
        super(lstm, self).__init__()
        self.n_steps = n_steps
        self.n_features = n_features
        self.n_outputs = n_outputs
        self.lstm_1 = LSTM(128, activation='relu', return_sequences=True)
        self.lstm_2 = LSTM(64, activation='relu', return_sequences=True)
        self.lstm_3 = LSTM(64, activation='relu')
        self.dropout_1 = Dropout(0.1)
        self.dropout_2 = Dropout(0.1)
        self.dense_1 = Dense(32, activation='relu')
        self.dense_2 = Dense(self.n_outputs)

    def call(self, x):
        x = self.lstm_1(x)
        x = self.dropout_1(x)
        x = self.lstm_2(x)
        x = self.lstm_3(x)
        x = self.dropout_2(x)
        x = self.dense_1(x)
        x = self.dense_2(x)

        return x

    def getModel(self):
        inp = Input(shape=(self.n_steps, self.n_features))
        x = lstm(self.n_steps, self.n_features, self.n_outputs)(inp)
        model = tf.keras.Model(inputs=inp, outputs=x)
        return model



