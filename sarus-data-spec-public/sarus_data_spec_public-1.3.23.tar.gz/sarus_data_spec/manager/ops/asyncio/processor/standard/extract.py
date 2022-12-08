from typing import AsyncIterator, cast

import pyarrow as pa

from sarus_data_spec.manager.asyncio.utils import async_iter
import sarus_data_spec.protobuf as sp
import sarus_data_spec.typing as st


async def arrow_extract(
    dataset: st.Dataset, batch_size: int
) -> AsyncIterator[pa.RecordBatch]:
    """Implementation of the extract transform
    At the moment is identical to slice but in the future it should it
    should be randomized
    """
    args, kwargs = dataset.parents()
    parents = args + list(kwargs.values())
    assert len(parents) == 1
    (parent,) = parents
    assert parent.prototype() == sp.Dataset
    ds_parent = cast(st.Dataset, parent)
    async_parent_batches = await ds_parent.async_to_arrow()
    parent_batches = [batch async for batch in async_parent_batches]
    parent_table = pa.Table.from_batches(parent_batches)
    size = dataset.transform().protobuf().spec.extract.size
    if size < 0:
        raise ValueError("Extract transform size parameter must be positive")
    batches = (
        parent_table.slice(offset=0, length=size)
        .combine_chunks()
        .to_batches(batch_size)
    )
    return async_iter(batches)
