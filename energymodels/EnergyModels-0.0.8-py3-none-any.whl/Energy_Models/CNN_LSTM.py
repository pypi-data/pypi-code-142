import tensorflow as tf
from keras.layers import  Activation, Embedding
from tensorflow.keras.layers import Dense, Dropout, LSTM, Input, Conv1D, MaxPooling1D


class CNN_LSTM(tf.keras.Model):
    def __init__(self, n_features, n_outputs=1):
        super(CNN_LSTM, self).__init__()

        self.n_features = n_features
        self.n_outputs = n_outputs

        self.Embedding = Embedding(10000, 128)
        self.dropout_1 = Dropout(0.25)
        self.conv1d = Conv1D(64, 5, padding='valid', activation='relu', strides=1)
        self.maxpool1d = MaxPooling1D(pool_size=4)
        self.lstm_1 = LSTM(70)
        self.dense_1 = (Dense(n_outputs))
        self.activation = (Activation('relu'))

    def call(self, x):
        x = self.Embedding(x)
        x = self.dropout_1(x)
        x = self.conv1d(x)
        x = self.maxpool1d(x)
        x = self.lstm_1(x)
        x = self.dense_1(x)
        x = self.activation(x)

        return x

    def getModel(self):
        inp = Input(shape=(self.n_features,))
        x = CNN_LSTM(self.n_features, self.n_outputs)(inp)
        model = tf.keras.Model(inputs=inp, outputs=x)
        return model
