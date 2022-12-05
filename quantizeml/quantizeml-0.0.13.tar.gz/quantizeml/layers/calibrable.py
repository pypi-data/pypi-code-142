#!/usr/bin/env python
# ******************************************************************************
# Copyright 2022 Brainchip Holdings Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ******************************************************************************
import keras
import tensorflow as tf


__all__ = ["Calibrable", "CalibrableVariable"]


class Calibrable():
    """A class that exhibits a 'calibration' property.

    All objects inheriting from this class share the same 'calibration' property.

    Setting the property on one instance will automatically set the property
    on all members of the class that are also Calibrable objects.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._calibration = False
        self.calibrables = []

    def __setattr__(self, name, value):
        super().__setattr__(name, value)
        if isinstance(value, Calibrable):
            self.calibrables.append(name)

    @property
    def calibration(self):
        """Flag to specify if the object is in calibration mode or not.

        Returns:
            bool: True if the object is in calibration mode, False otherwise.
        """
        return self._calibration

    @calibration.setter
    def calibration(self, value):
        """Set the calibration mode of the object, and all its members.

        Args:
            value (bool): True if the object will be in calibration mode, False otherwise.
        """
        self._calibration = value
        for name in self.calibrables:
            calibrable = getattr(self, name)
            calibrable.calibration = value


class CalibrableVariable(Calibrable, keras.layers.Layer):
    """Wrapper class to store and retrieve a calibrable variable, e.g.: shift
    information.
    """

    def build(self, input_shape):
        super().build(input_shape)
        self._var = self.add_weight(
            shape=input_shape,
            dtype=tf.float32,
            initializer="zeros",
            synchronization=tf.VariableSynchronization.ON_READ,
            trainable=False,
            aggregation=tf.VariableAggregation.MEAN,
            experimental_autocast=False,
        )

    @property
    def value(self):
        """Get to the variable value.

        Returns:
            :obj:`tf.Tensor`: value of the stored variable.
        """
        return self._var.value()

    def call(self, inputs):
        """Updates the value of the variable if calibration is True.

        Args:
            inputs (:obj:`tf.Tensor`): new values.

        Returns:
            :obj:`tf.Tensor`: value of the variable when calibration is True, None otherwise.
        """
        if not self.calibration:
            return None
        self._var.assign(inputs)
        return inputs
