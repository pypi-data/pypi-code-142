# Copyright 2021 Alibaba Group Holding Limited. All Rights Reserved.
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
# =============================================================================

r'''DeepRec EV backend of embedding tables.
'''

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import six

from tensorflow.python.ops import embedding_ops
from tensorflow.python.ops import variable_scope as vs
from tensorflow.python.ops import variables
from tensorflow.python.platform import tf_logging as logging

from hybridbackend.tensorflow.training.embedding import \
  EmbeddingLookupRewriting


class EmbeddingLookupRewritingForDeepRecEV(EmbeddingLookupRewriting):  # pylint: disable=useless-object-inheritance
  r'''Embedding lookup decorator for DeepRec EV.
  '''
  def __init__(self):
    super().__init__()
    self._prev_lookup = None
    self._prev_get_embedding_variable = None

  def build_unsharded_weights(self, fn, name, *args, **kwargs):
    r'''Build unsharded embedding weights.
    '''
    return fn(f'{name}/part_0', *args, **kwargs)

  def build_sharded_weights(
      self, shard, num_shards, shard_collections, fn, name, *args, **kwargs):
    r'''Build sharded embedding weights.
    '''
    kwargs['collections'] = shard_collections
    embedding_dim = kwargs.pop('embedding_dim', None)
    if embedding_dim is None:
      try:
        embedding_dim, = args
      except ValueError as ex:
        six.raise_from(
          ValueError('missing embedding_dim for tf.get_embedding_variable'),
          ex)
    embedding_weights = fn(f'{name}/part_{shard}', embedding_dim, **kwargs)
    full_name = embedding_weights.name.split(':')[0]
    full_name = full_name[:full_name.rfind('/part')]
    if hasattr(embedding_weights, '_set_save_slice_info'):
      embedding_weights._set_save_slice_info(  # pylint: disable=protected-access
        variables.Variable.SaveSliceInfo(
          full_name=full_name,
          full_shape=[num_shards, embedding_dim],
          var_offset=[shard, 0],
          var_shape=embedding_weights.shape))
    elif isinstance(embedding_weights, variables.PartitionedVariable):
      for pvar in embedding_weights:
        pvar._set_save_slice_info(  # pylint: disable=protected-access
          variables.Variable.SaveSliceInfo(
            full_name=full_name,
            full_shape=[num_shards, embedding_dim],
            var_offset=[shard, 0],
            var_shape=pvar.shape))
    else:
      logging.warning(
        f'Embedding weights {full_name} cannot be saved correctly')

    return embedding_weights

  def begin(self):
    r'''Rewrites API.
    '''
    try:
      import tensorflow as tf  # pylint: disable=import-outside-toplevel
      self._prev_lookup = embedding_ops.embedding_lookup
      embedding_ops.embedding_lookup = self.wraps_embedding_lookup(
        embedding_ops.embedding_lookup)
      tf.nn.embedding_lookup = self.wraps_embedding_lookup(
        embedding_ops.embedding_lookup)

      self._prev_get_embedding_variable = vs.get_embedding_variable
      vs.get_embedding_variable = self.wraps_build_embedding_weights(
        self._prev_get_embedding_variable)
      tf.get_embedding_variable = self.wraps_build_embedding_weights(
        self._prev_get_embedding_variable)
    except:  # pylint: disable=bare-except
      pass

  def end(self):
    r'''Revert API rewriting.
    '''
    try:
      import tensorflow as tf  # pylint: disable=import-outside-toplevel
      vs.get_embedding_variable = self._prev_get_embedding_variable
      tf.get_embedding_variable = self._prev_get_embedding_variable

      embedding_ops.embedding_lookup = self._prev_lookup
      tf.nn.embedding_lookup = self._prev_lookup
    except:  # pylint: disable=bare-except
      pass


EmbeddingLookupRewriting.register(EmbeddingLookupRewritingForDeepRecEV)
