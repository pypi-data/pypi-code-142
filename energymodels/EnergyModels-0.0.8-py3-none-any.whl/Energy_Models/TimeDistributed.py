import numpy as np
import keras.layers
import tensorflow as tf
from tensorflow.keras.layers import Flatten, Dense, Dropout, LSTM, TimeDistributed, Conv1D, MaxPooling1D



class TD (tf.keras.Model):
    def __init__(self,n_steps,n_features,n_outputs=1):
        super(TD, self).__init__()
        self.n_steps=n_steps
        self.n_features=n_features
        self.n_outputs=n_outputs
        self.td_1 = TimeDistributed(Conv1D(filters=64, kernel_size=3, activation='relu', padding='same'))
        self.td_2 = TimeDistributed(Conv1D(filters=32, kernel_size=2, activation='relu', padding='same'))
        self.dropout_1 =TimeDistributed(Dropout(0.2))
        self.max_pooling1D=TimeDistributed(MaxPooling1D(pool_size=2, padding='same')) 
        self.flatten=TimeDistributed(Flatten())
        self.lstm_1 = LSTM(75)
        self.dropout_2 = Dropout(0.2)
        self.dense_1 = Dense(50, activation='relu')
        self.dense_2 = Dense(self.n_outputs)
         
        
    def call(self, x):

        x = self.td_1(x)
        x = self.td_2(x)
        x = self.dropout_1(x)
        x = self.max_pooling1D(x)
        x = self.flatten(x)
        x = self.lstm_1(x)
        x = self.dropout_2(x)
        x = self.dense_1(x)
        x = self.dense_2(x)

        return x
    
    def getModel(self):
        inp = tf.keras.Input(shape=(None,self.n_steps,self.n_features))
        x = TD(self.n_steps, self.n_features,self.n_outputs)(inp)
        model = tf.keras.Model(inputs=inp, outputs=x)
        return model

