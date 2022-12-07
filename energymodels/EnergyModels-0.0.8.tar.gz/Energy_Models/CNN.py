import tensorflow as tf
from tensorflow.keras.layers import  Flatten, Dense, Dropout, Input, Conv1D, MaxPooling1D


class CNN(tf.keras.Model):
    def __init__(self, n_steps, n_features, n_outputs=1):
        super(CNN, self).__init__()
        self.n_steps = n_steps
        self.n_features = n_features
        self.n_outputs = n_outputs
        self.CNN_L1 = (Conv1D(filters=64, kernel_size=4, activation='relu', padding='same'))
        self.CNN_L2 = (Conv1D(filters=32, kernel_size=3, padding='same', activation='relu'))
        self.CNN_L3 = (Conv1D(filters=16, kernel_size=2, padding='same', activation='relu'))
        self.CNN_maxpooling = (MaxPooling1D(pool_size=1))
        self.CNN_flatten = (Flatten())
        self.CNN_dense1 = (Dense(100, activation='relu'))
        self.CNN_droupout = (Dropout(0.3))
        self.CNN_dense2 = (Dense(20, activation='relu'))
        self.CNN_dense3 = (Dense(self.n_outputs))

    def call(self, x):
        x = self.CNN_L1(x)
        x = self.CNN_L2(x)
        x = self.CNN_L3(x)
        x = self.CNN_maxpooling(x)
        x = self.CNN_flatten(x)
        x = self.CNN_dense1(x)
        x = self.CNN_droupout(x)
        x = self.CNN_dense2(x)
        x = self.CNN_dense3(x)
        return x

    def getModel(self):
        inp = Input(shape=(self.n_steps, self.n_features))
        x = CNN(self.n_steps, self.n_features, self.n_outputs)(inp)
        model = tf.keras.Model(inputs=inp, outputs=x)
        return model


