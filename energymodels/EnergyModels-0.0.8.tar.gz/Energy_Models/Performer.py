from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import string
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import math
from functools import partial
from tensorflow import multiply, einsum
from tensorflow.keras.activations import softmax
from tensorflow.python.keras.layers import advanced_activations
from tensorflow.python.keras.layers import core
import collections


from tensorflow.python.framework import tensor_shape
from tensorflow.python.keras import constraints
from tensorflow.python.keras import initializers
from tensorflow.python.keras import regularizers
from tensorflow.python.keras.engine.base_layer import Layer
from tensorflow.keras.layers import EinsumDense
from tensorflow.python.keras.utils import tf_utils
from tensorflow.python.ops import array_ops
from tensorflow.python.ops import math_ops
from tensorflow.python.ops import special_math_ops
from tensorflow.python.util.tf_export import keras_export





def build_quadratic_attention_equation(rank, attn_axes):
    batch_dims = _get_index_of_batch_dims(rank, attn_axes)
    query_notation, value_notation = _get_query_and_value_notation(rank, batch_dims)
    key_notation = value_notation
    qk_product_notation = "".join([query_notation[i] for i in batch_dims] +
                                  [query_notation[i] for i in attn_axes] +
                                  [key_notation[i] for i in attn_axes])
    kq_product_equation = f"{key_notation},{query_notation}->{qk_product_notation}"
    qk_v_product_equation = f"{qk_product_notation},{value_notation}->{query_notation}"
    attn_scores_rank = len(qk_product_notation)
    return kq_product_equation, qk_v_product_equation, attn_scores_rank


def build_linear_attention_equation(rank, attn_axes):
    batch_dims = _get_index_of_batch_dims(rank, attn_axes)
    query_notation, value_notation = _get_query_and_value_notation(rank, batch_dims)

    query_hat_notation = query_notation[:-1] + 'r'
    key_hat_notation = value_notation[:-1] + 'r'
    key_value_notation = "".join([key_hat_notation[i] for i in batch_dims] +
                                 list('r' + value_notation[-1]))
    kv_product_equation = f"{key_hat_notation},{value_notation}->{key_value_notation}"
    q_kv_product_equation = f"{query_hat_notation},{key_value_notation}->{query_notation}"
    attn_scores_rank = len(key_value_notation)
    return kv_product_equation, q_kv_product_equation, attn_scores_rank


def _get_index_of_batch_dims(rank, attn_axes):
    batch_dims = tuple(np.delete(range(rank), attn_axes + (rank - 1,)))
    return batch_dims


def _get_query_and_value_notation(rank, batch_dims):
    chr_idx = string.ascii_lowercase
    query_notation = chr_idx[:rank]
    letter_offset = rank
    value_notation = ""
    for i in range(rank):
        if i in batch_dims or i == rank - 1:
            value_notation += query_notation[i]
        else:
            value_notation += chr_idx[letter_offset]
            letter_offset += 1
    return query_notation, value_notation


def build_normalisation_equation(rank, attn_axes):
    chr_idx = string.ascii_lowercase
    key_hat_notation = chr_idx[:rank]
    query_hat_notation = key_hat_notation
    ones_array_notation = key_hat_notation[:-1]
    key_ones_notation = "".join(np.delete(list(key_hat_notation), attn_axes, 0))
    k1_equation = f"{key_hat_notation},{ones_array_notation}->{key_ones_notation}"
    q_k1_equation = f"{query_hat_notation},{key_ones_notation}->{ones_array_notation}"
    qk1_q_equation = f"{ones_array_notation},{key_hat_notation}->{query_hat_notation}"
    return k1_equation, q_k1_equation, qk1_q_equation


def build_kernel_equation(rank):
    chr_idx = string.ascii_lowercase
    strings = chr_idx[:rank+1]
    data_notation = strings[:-1]
    sampling_matrix_notation = strings[:2] + strings[-1] + strings[-2]
    product = data_notation[:-1]+strings[-1]
    combine_equation = f"{data_notation},{sampling_matrix_notation}->{product}"
    return combine_equation

# Lint as: python3
# Copyright 2019 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Keras-based attention layer."""

_CHR_IDX = string.ascii_lowercase


def _build_attention_equation(rank, attn_axes):
  """Builds einsum equations for the attention computation.

  Query, key, value inputs after projection are expected to have the shape as:
  (bs, <non-attention dims>, <attention dims>, num_heads, channels).
  bs and <non-attention dims> are treated as <batch dims>.
  The attention operations can be generalized:
  (1) Query-key dot product:
  (<batch dims>, <query attention dims>, num_heads, channels), (<batch dims>,
  <key attention dims>, num_heads, channels) -> (<batch dims>,
  num_heads, <query attention dims>, <key attention dims>)
  (2) Combination:
  (<batch dims>, num_heads, <query attention dims>, <key attention dims>),
  (<batch dims>, <value attention dims>, num_heads, channels) -> (<batch dims>,
  <query attention dims>, num_heads, channels)

  Args:
    rank: the rank of query, key, value tensors.
    attn_axes: a list/tuple of axes, [-1, rank), that will do attention.

  Returns:
    Einsum equations.
  """
  target_notation = _CHR_IDX[:rank]
  # `batch_dims` includes the head dim.
  batch_dims = tuple(np.delete(range(rank), attn_axes + (rank - 1,)))
  letter_offset = rank
  source_notation = ""
  for i in range(rank):
    if i in batch_dims or i == rank - 1:
      source_notation += target_notation[i]
    else:
      source_notation += _CHR_IDX[letter_offset]
      letter_offset += 1

  product_notation = "".join([target_notation[i] for i in batch_dims] +
                             [target_notation[i] for i in attn_axes] +
                             [source_notation[i] for i in attn_axes])
  dot_product_equation = "%s,%s->%s" % (source_notation, target_notation,
                                        product_notation)
  attn_scores_rank = len(product_notation)
  combine_equation = "%s,%s->%s" % (product_notation, source_notation,
                                    target_notation)
  return dot_product_equation, combine_equation, attn_scores_rank


def _build_proj_equation(free_dims, bound_dims, output_dims):
  """Builds an einsum equation for projections inside multi-head attention."""
  input_str = ""
  kernel_str = ""
  output_str = ""
  bias_axes = ""
  letter_offset = 0
  for i in range(free_dims):
    char = _CHR_IDX[i + letter_offset]
    input_str += char
    output_str += char

  letter_offset += free_dims
  for i in range(bound_dims):
    char = _CHR_IDX[i + letter_offset]
    input_str += char
    kernel_str += char

  letter_offset += bound_dims
  for i in range(output_dims):
    char = _CHR_IDX[i + letter_offset]
    kernel_str += char
    output_str += char
    bias_axes += char
  equation = "%s,%s->%s" % (input_str, kernel_str, output_str)

  return equation, bias_axes, len(output_str)


def _get_output_shape(output_rank, known_last_dims):
  return [None] * (output_rank - len(known_last_dims)) + list(known_last_dims)


class MultiHeadAttention(Layer):
  def __init__(self,
               num_heads,
               key_dim,
               value_dim=None,
               dropout=0.0,
               use_bias=True,
               output_shape=None,
               attention_axes=None,
               kernel_initializer="glorot_uniform",
               bias_initializer="zeros",
               kernel_regularizer=None,
               bias_regularizer=None,
               activity_regularizer=None,
               kernel_constraint=None,
               bias_constraint=None,
               **kwargs):
    super(MultiHeadAttention, self).__init__(**kwargs)
    self._num_heads = num_heads
    self._key_dim = key_dim
    self._value_dim = value_dim if value_dim else key_dim
    self._dropout = dropout
    self._use_bias = use_bias
    self._output_shape = output_shape
    self._kernel_initializer = initializers.get(kernel_initializer)
    self._bias_initializer = initializers.get(bias_initializer)
    self._kernel_regularizer = regularizers.get(kernel_regularizer)
    self._bias_regularizer = regularizers.get(bias_regularizer)
    self._kernel_constraint = constraints.get(kernel_constraint)
    self._bias_constraint = constraints.get(bias_constraint)
    if attention_axes is not None and not isinstance(attention_axes,
                                                     collections.abc.Sized):
      self._attention_axes = (attention_axes,)
    else:
      self._attention_axes = attention_axes
    self._built_from_signature = False

  def get_config(self):
    config = {
        "num_heads":
            self._num_heads,
        "key_dim":
            self._key_dim,
        "value_dim":
            self._value_dim,
        "dropout":
            self._dropout,
        "use_bias":
            self._use_bias,
        "output_shape":
            self._output_shape,
        "attention_axes":
            self._attention_axes,
        "kernel_initializer":
            initializers.serialize(self._kernel_initializer),
        "bias_initializer":
            initializers.serialize(self._bias_initializer),
        "kernel_regularizer":
            regularizers.serialize(self._kernel_regularizer),
        "bias_regularizer":
            regularizers.serialize(self._bias_regularizer),
        "activity_regularizer":
            regularizers.serialize(self._activity_regularizer),
        "kernel_constraint":
            constraints.serialize(self._kernel_constraint),
        "bias_constraint":
            constraints.serialize(self._bias_constraint)
    }
    base_config = super(MultiHeadAttention, self).get_config()
    return dict(list(base_config.items()) + list(config.items()))

  def _build_from_signature(self, query, value, key=None):
    """Builds layers and variables.

    Once the method is called, self._built_from_signature will be set to True.

    Args:
      query: query tensor or TensorShape.
      value: value tensor or TensorShape.
      key: key tensor or TensorShape.
    """
    self._built_from_signature = True
    if hasattr(query, "shape"):
      query_shape = tensor_shape.TensorShape(query.shape)
    else:
      query_shape = query
    if hasattr(value, "shape"):
      value_shape = tensor_shape.TensorShape(value.shape)
    else:
      value_shape = value
    if key is None:
      key_shape = value_shape
    elif hasattr(key, "shape"):
      key_shape = tensor_shape.TensorShape(key.shape)
    else:
      key_shape = key

    common_kwargs = dict(
        kernel_initializer=self._kernel_initializer,
        bias_initializer=self._bias_initializer,
        kernel_regularizer=self._kernel_regularizer,
        bias_regularizer=self._bias_regularizer,
        activity_regularizer=self._activity_regularizer,
        kernel_constraint=self._kernel_constraint,
        bias_constraint=self._bias_constraint)
    # Any setup work performed only once should happen in an `init_scope`
    # to avoid creating symbolic Tensors that will later pollute any eager
    # operations.
    with tf_utils.maybe_init_scope(self):
      free_dims = query_shape.rank - 1
      einsum_equation, bias_axes, output_rank = _build_proj_equation(
          free_dims, bound_dims=1, output_dims=2)
      self._query_dense = EinsumDense(
          einsum_equation,
          output_shape=_get_output_shape(output_rank - 1,
                                         [self._num_heads, self._key_dim]),
          bias_axes=bias_axes if self._use_bias else None,
          name="query",
          **common_kwargs)
      einsum_equation, bias_axes, output_rank = _build_proj_equation(
          key_shape.rank - 1, bound_dims=1, output_dims=2)
      self._key_dense = EinsumDense(
          einsum_equation,
          output_shape=_get_output_shape(output_rank - 1,
                                         [self._num_heads, self._key_dim]),
          bias_axes=bias_axes if self._use_bias else None,
          name="key",
          **common_kwargs)
      einsum_equation, bias_axes, output_rank = _build_proj_equation(
          value_shape.rank - 1, bound_dims=1, output_dims=2)
      self._value_dense = EinsumDense(
          einsum_equation,
          output_shape=_get_output_shape(output_rank - 1,
                                         [self._num_heads, self._value_dim]),
          bias_axes=bias_axes if self._use_bias else None,
          name="value",
          **common_kwargs)

      # Builds the attention computations for multi-head dot product attention.
      # These computations could be wrapped into the keras attention layer once
      # it support mult-head einsum computations.
      self._build_attention(output_rank)
      if self._output_shape:
        if not isinstance(self._output_shape, collections.abc.Sized):
          output_shape = [self._output_shape]
        else:
          output_shape = self._output_shape
      else:
        output_shape = [query_shape[-1]]
      einsum_equation, bias_axes, output_rank = _build_proj_equation(
          free_dims, bound_dims=2, output_dims=len(output_shape))
      self._output_dense = EinsumDense(
          einsum_equation,
          output_shape=_get_output_shape(output_rank - 1, output_shape),
          bias_axes=bias_axes if self._use_bias else None,
          name="attention_output",
          **common_kwargs)

  def _build_attention(self, rank):
    """Builds multi-head dot-product attention computations.

    This function builds attributes necessary for `_compute_attention` to
    costomize attention computation to replace the default dot-product
    attention.

    Args:
      rank: the rank of query, key, value tensors.
    """
    if self._attention_axes is None:
      self._attention_axes = tuple(range(1, rank - 2))
    else:
      self._attention_axes = tuple(self._attention_axes)
    self._dot_product_equation, self._combine_equation, attn_scores_rank = (
        _build_attention_equation(rank, attn_axes=self._attention_axes))
    norm_axes = tuple(
        range(attn_scores_rank - len(self._attention_axes), attn_scores_rank))
    self._softmax = partial(softmax, axis=norm_axes)
    self._dropout_layer = core.Dropout(rate=self._dropout)

  def _compute_attention(self,
                         query,
                         key,
                         value,
                         training=None):
    """Applies Dot-product attention with query, key, value tensors.

    This function defines the computation inside `call` with projected
    multi-head Q, K, V inputs. Users can override this function for customized
    attention implementation.

    Args:
      query: Projected query `Tensor` of shape `[B, T, N, key_dim]`.
      key: Projected key `Tensor` of shape `[B, T, N, key_dim]`.
      value: Projected value `Tensor` of shape `[B, T, N, value_dim]`.
      training: Python boolean indicating whether the layer should behave in
        training mode (adding dropout) or in inference mode (doing nothing).

    Returns:
      attention_output: Multi-headed outputs of attention computation.
      attention_scores: Multi-headed attention weights.
    """
    # Note: Applying scalar multiply at the smaller end of einsum improves
    # XLA performance, but may introduce slight numeric differences in
    # the Transformer attention head.
    query = math_ops.multiply(query, 1.0 / math.sqrt(float(self._key_dim)))

    # Take the dot product between "query" and "key" to get the raw
    # attention scores.
    attention_scores = special_math_ops.einsum(self._dot_product_equation, key,
                                               query)

    attention_scores = self._softmax(attention_scores)

    # This is actually dropping out entire tokens to attend to, which might
    # seem a bit unusual, but is taken from the original Transformer paper.
    attention_scores_dropout = self._dropout_layer(
        attention_scores, training=training)

    # `context_layer` = [B, T, N, H]
    attention_output = special_math_ops.einsum(self._combine_equation,
                                               attention_scores_dropout, value)
    return attention_output, attention_scores


  def call(self, inputs, training=None):
    query = inputs[0]
    key = inputs[1]
    value = inputs[2] if len(inputs) > 2 else key

    if not self._built_from_signature:
      self._build_from_signature(query=query, value=value, key=key)
    if key is None:
      key = value

    query = self._query_dense(query)
    key = self._key_dense(key)
    value = self._value_dense(value)

    attention_output, attention_scores = self._compute_attention(
        query, key, value, training)
    attention_output = self._output_dense(attention_output)

    return attention_output




_CHR_IDX = string.ascii_lowercase


class GaussianOrthogonalRandomMatrix:
    def __init__(self, rows, columns, scaling=0):
        self.rows = rows
        self.columns = columns
        self.scaling = scaling
        assert self.scaling in [0, 1], 'Scaling must be one of {0, 1}'

    def sample(self):
        shape = (self.rows, self.columns)
        unstructured_block = tf.random.normal(shape=shape)
        q, r = tf.linalg.qr(unstructured_block)
        final_matrix = q if self.rows >= self.columns else r

        multiplier = self._get_multiplier()
        out = tf.matmul(tf.linalg.diag(multiplier), final_matrix)
        tf.stop_gradient(out)
        return out

    def _get_multiplier(self):
        if self.scaling == 0:
            shape = (self.rows, self.columns)
            multiplier = tf.linalg.norm(tf.random.normal(shape=shape), axis=1)
        elif self.scaling == 1:
            columns = tf.constant(self.columns, dtype=tf.dtypes.float32)
            rows = tf.constant(self.rows)
            multiplier = tf.math.sqrt(columns) * tf.ones(rows)
        return multiplier

    def __repr__(self):
        out = "GaussianOrthogonalRandomMatrix(rows={}, columns={}, scaling={})"
        out = out.format(self.rows, self.columns, self.scaling)
        return out


def kernel_feature_creator(data, projection_matrix, is_query):
    head_dim = tf.constant(data.shape[-1], dtype=tf.dtypes.float32)
    support_dim = tf.constant(projection_matrix.shape[0], dtype=tf.dtypes.float32)
    data_normalizer = 1.0 / (tf.math.sqrt(tf.math.sqrt(head_dim)))
    ratio = 1.0 / tf.math.sqrt(support_dim)
    data_mod_shape = tf.concat([tf.shape(data)[0:2], tf.shape(projection_matrix)], axis=0)
    random_matrix = tf.zeros(data_mod_shape) + projection_matrix

    normalised_data = data_normalizer * data
    dot_product_equation = build_kernel_equation(len(data.shape))
    data_hat = tf.einsum(dot_product_equation, normalised_data, random_matrix)

    diag_data = tf.math.square(data)
    diag_data = tf.math.reduce_sum(diag_data, axis=- 1)
    diag_data = (diag_data / 2.0) * data_normalizer * data_normalizer
    diag_data = tf.expand_dims(diag_data, axis=-1)

    if is_query:
        last_dims_t = len(data_hat.shape) - 1
        func = partial(tf.math.reduce_max, axis=last_dims_t, keepdims=True)
    else:
        func = tf.math.reduce_max
    out = ratio * (tf.math.exp(data_hat - diag_data - func(data_hat)) + 1e-4)
    return out






class Performer(MultiHeadAttention):
    """Performer Layer

    This is an implementation of multi-head attention with linear attention via
    positive orthogonal random features approach. Implemented to be fully
    compatable with tensorflow's existing MultiHeadAttention layer.

    Examples:
    >>> layer = Performer(num_heads=2, key_dim=2,
                          attention_method='linear', supports=2)
    >>> query = tf.keras.Input(shape=[8, 16])
    >>> key = tf.keras.Input(shape=[4, 16])
    >>> output_tensor = layer([query, key])
    >>> print(output_tensor.shape)
    (None, 8, 16)
    >>> print(weights.shape)
    (None, 2, 8, 4)
    """
    def __init__(self, *args, **kwargs):
        self.attention_method = kwargs.pop('attention_method', 'quadratic')
        self.scaling = kwargs.pop('scaling', 0)
        self.supports = kwargs.pop('supports', None)
        self._check_attention_method_is_valid()
        if self.attention_method == 'quadratic':
            self._compute_attention = self.quadratic_attention
            self._build_attention_equation = build_quadratic_attention_equation
        else:
            self._compute_attention = self.linear_attention
            self._build_attention_equation = build_linear_attention_equation
            self._check_supports_is_not_none()
            self.sampler = GaussianOrthogonalRandomMatrix(self.supports, kwargs['key_dim'], self.scaling)
            self._frozen_features = self._get_frozen_random_features(kwargs)
            self._build_normalisation_equation = build_normalisation_equation
        super().__init__(*args, **kwargs)

    def _get_frozen_random_features(self, kwargs):
        if '_frozen_features' in kwargs:
            frozen_features = kwargs.pop('_frozen_features')
        else:
            frozen_features = self.sampler.sample()
        return tf.constant(frozen_features, name='_frozen_features')

    def _check_supports_is_not_none(self):
        if self.supports is None:
            raise(RuntimeError('must have numbers of supports specified'))

    def _check_attention_method_is_valid(self):
        message = 'invalid attention method'
        assert self.attention_method in ['linear', 'quadratic'], message

    def _build_attention(self, rank):
        if self._attention_axes is None:
            self._attention_axes = tuple(range(1, rank - 2))
        else:
            self._attention_axes = tuple(self._attention_axes)
        self._add_attention_equation(rank)
        self._add_soft_max_and_dropout_layers()
        if hasattr(self, '_build_normalisation_equation'):
            self._add_normalisation_equation(rank)

    def _add_attention_equation(self, rank):
        result = self._build_attention_equation(rank, self._attention_axes)
        self._dot_product_equation, self._combine_equation, attn_scores_rank = result
        norm_axes = tuple(range(attn_scores_rank - len(self._attention_axes), attn_scores_rank))
        self._norm_axes = norm_axes

    def _add_soft_max_and_dropout_layers(self):
        self._softmax = partial(softmax, axis=self._norm_axes)
        self._dropout_layer = core.Dropout(rate=self._dropout)

    def _add_normalisation_equation(self, rank):
        result = self._build_normalisation_equation(rank, self._attention_axes)
        self._k1_equation, self._q_k1_equation, self._qk1_q_equation = result

    def quadratic_attention(self, query, key, value, training=None):
        query = multiply(query, 1. / math.sqrt(float(self._key_dim)))
        attention_scores = einsum(self._dot_product_equation, key, query)
        attention_scores = self._softmax(attention_scores)
        attention_scores_dropout = self._dropout_layer(attention_scores, training=training)
        attention_output = einsum(self._combine_equation, attention_scores_dropout, value)
        return attention_output, attention_scores

    def linear_attention(self, query, key, value, training=None):
        random_features = self._get_random_features(training)
        lifted_query = kernel_feature_creator(query, random_features, True)
        lifted_key = kernel_feature_creator(key, random_features, False)
        kv = einsum(self._dot_product_equation, lifted_key, value)
        qkv = einsum(self._combine_equation, lifted_query, kv)
        normalised_qkv = self._normalise(lifted_key, lifted_query, qkv)
        return normalised_qkv, None

    @tf.function
    def _get_random_features(self, train):
        out = self.sampler.sample() if train is None else self._frozen_features
        return out

    def _normalise(self, lifted_key, lifted_query, qkv):
        ones = tf.ones_like(lifted_key[..., 0])
        k_ones = einsum(self._k1_equation, lifted_key, ones)
        D = einsum(self._q_k1_equation, lifted_query, k_ones)
        D = 1. / (D + 1e-6)
        normalised_qkv = einsum(self._qk1_q_equation, D, qkv)
        return normalised_qkv

    def get_config(self):
        performer_config = {
            "attention_method":
                self.attention_method,
            "supports":
                self.supports,
            "scaling":
                self.scaling,
        }
        if hasattr(self, '_frozen_features'):
            random_features = self._frozen_features.numpy()
            performer_config['_frozen_features'] = random_features
        config = super().get_config()
        config.update(performer_config)
        return config




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
            [layers.Dense(ff_dim, activation="relu"), layers.Dense(embed_dim),]
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
