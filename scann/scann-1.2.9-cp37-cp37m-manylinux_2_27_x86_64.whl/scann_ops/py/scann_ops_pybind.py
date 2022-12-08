"""Wrapper around pybind module that provides convenience functions for instantiating ScaNN searchers."""

import os

# needed because of C++ dependency on TF headers
import tensorflow as _tf
import sys

sys.path.append(
    os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "cc/python"))
import scann_pybind
from scann.scann_ops.py import scann_builder
from scann.scann_ops.py import scann_ops_pybind_backcompat


class ScannSearcher(object):
  """Wrapper class around pybind module that provides a cleaner interface."""

  def __init__(self, searcher):
    self.searcher = searcher

  def search(self,
             q,
             final_num_neighbors=None,
             pre_reorder_num_neighbors=None,
             leaves_to_search=None):
    final_nn = -1 if final_num_neighbors is None else final_num_neighbors
    pre_nn = -1 if pre_reorder_num_neighbors is None else pre_reorder_num_neighbors
    leaves = -1 if leaves_to_search is None else leaves_to_search
    return self.searcher.search(q, final_nn, pre_nn, leaves)

  def search_batched(self,
                     queries,
                     final_num_neighbors=None,
                     pre_reorder_num_neighbors=None,
                     leaves_to_search=None):
    final_nn = -1 if final_num_neighbors is None else final_num_neighbors
    pre_nn = -1 if pre_reorder_num_neighbors is None else pre_reorder_num_neighbors
    leaves = -1 if leaves_to_search is None else leaves_to_search
    return self.searcher.search_batched(queries, final_nn, pre_nn, leaves,
                                        False)

  def search_batched_parallel(self,
                              queries,
                              final_num_neighbors=None,
                              pre_reorder_num_neighbors=None,
                              leaves_to_search=None):
    final_nn = -1 if final_num_neighbors is None else final_num_neighbors
    pre_nn = -1 if pre_reorder_num_neighbors is None else pre_reorder_num_neighbors
    leaves = -1 if leaves_to_search is None else leaves_to_search
    return self.searcher.search_batched(queries, final_nn, pre_nn, leaves, True)

  def serialize(self, artifacts_dir):
    self.searcher.serialize(artifacts_dir)


def builder(db, num_neighbors, distance_measure):
  """pybind analogue of builder() in scann_ops.py; see docstring there."""

  def builder_lambda(db, config, training_threads, **kwargs):
    return create_searcher(db, config, training_threads, **kwargs)

  return scann_builder.ScannBuilder(
      db, num_neighbors, distance_measure).set_builder_lambda(builder_lambda)


def create_searcher(db, scann_config, training_threads=0):
  return ScannSearcher(
      scann_pybind.ScannNumpy(db, scann_config, training_threads))


def load_searcher(artifacts_dir, assets_backcompat_shim=True):
  """Loads searcher assets from artifacts_dir and returns a ScaNN searcher."""
  is_dir = os.path.isdir(artifacts_dir)
  if not is_dir:
    raise ValueError(f"{artifacts_dir} is not a directory.")

  assets_pbtxt = os.path.join(artifacts_dir, "scann_assets.pbtxt")
  if not scann_ops_pybind_backcompat.path_exists(assets_pbtxt):
    if not assets_backcompat_shim:
      raise ValueError("No scann_assets.pbtxt found.")
    print("No scann_assets.pbtxt found. ScaNN assumes this searcher was from an"
          " earlier release, and is calling `populate_and_save_assets_proto`"
          "from `scann_ops_pybind_backcompat` to create a scann_assets.pbtxt. "
          "Note this compatibility shim may be removed in the future.")
    scann_ops_pybind_backcompat.populate_and_save_assets_proto(artifacts_dir)
  with open(assets_pbtxt, "r") as f:
    return ScannSearcher(scann_pybind.ScannNumpy(artifacts_dir, f.read()))
