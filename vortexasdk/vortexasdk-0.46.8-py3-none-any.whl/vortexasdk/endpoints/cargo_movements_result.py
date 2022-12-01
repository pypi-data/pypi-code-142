import functools
import os
from multiprocessing.pool import Pool
from typing import List
import pandas as pd

from vortexasdk.api import CargoMovement
from vortexasdk.api.entity_flattening import (
    convert_cargo_movement_to_flat_dict,
)
from vortexasdk.api.search_result import Result
from vortexasdk.result_conversions import create_dataframe, create_list
from vortexasdk.logger import get_logger

logger = get_logger(__name__)


class CargoMovementsResult(Result):

    """
    Container class holdings search results returns from the cargo movements endpoint.

    This class has two methods, `to_list()`, and `to_df()`, allowing search results to be represented as a list of `CargoMovements`,
     or as a `pd.DataFrame` , respectively.
    """

    def to_list(self) -> List[CargoMovement]:
        """Represent cargo movements as a list of `CargoMovementEntity`s."""
        # noinspection PyTypeChecker
        return create_list(super().to_list(), CargoMovement)

    def to_df(self, columns=None) -> pd.DataFrame:
        """
        Represent cargo movements as a `pd.DataFrame`.

        # Arguments
            columns: Output columns present in the `pd.DataFrame`.
            Enter `columns='all'` to return all available columns.
            Enter `columns=None` to use `cargo_movements.DEFAULT_COLUMNS`.

        # Returns
        `pd.DataFrame`, one row per cargo movement.


        ## Notes

        A cargo movement is a complicated, nested structure. Between it's point of loading and discharge, a cargo
         movement may be carried by _N_ or more vessels, with _N-1_ associated STS events. Each of these _N_ vessels
         could have an associated corporate owner, charterer, time charterer... etc.

         In order to represent a cargo movement as a flat (not nested) record in a dataframe, the sdk flattens the cargo
         movement, generating many columns in the process.

         The columns are logically named. Let's say that a cargo is transferred between 4 vessels en route from a load
         in Rotterdam to a discharge in New York. This is represented as 1 `cargo_port_unload_event`, followed by
          3 `cargo_sts_event`s, and finally 1 `cargo_port_unload_event`.

         In this example the name of the 1st vessel, is found in the `vessels.0.name` column (we're using zero-based
         numbering indexes). Likewise, the imo of the second vessel is found in the `vessels.1.imo` column.

         To find the name of the country in which the second STS event occured, we'd use the
         `events.cargo_sts_event.1.location.country.layer` column.

         Similarly, to find out when the first vessel started
         loading the cargo from Rotterdam, we'd use the `events.cargo_port_load_event.0.start_timestamp` column.

        By default, the columns returned are something along the lines of.
        ```python
        DEFAULT_COLUMNS = [
            'events.cargo_port_load_event.0.location.port.label',
            'events.cargo_port_unload_event.0.location.port.label',
            'product.group.label',
            'product.grade.label',
            'quantity',
            'vessels.0.name',
            'events.cargo_port_load_event.0.end_timestamp',
            'events.cargo_port_unload_event.0.start_timestamp',
        ]
        ```
        The exact default columns used can be found at `cargo_movements.DEFAULT_COLUMNS`

        A near complete list of columns is given below
        ```
        [
            'cargo_movement_id',
            'events.cargo_fso_load_event.0.end_timestamp',
            'events.cargo_fso_load_event.0.event_type',
            'events.cargo_fso_load_event.0.fso_vessel_id',
            'events.cargo_fso_load_event.0.fso_vessel_name',
            'events.cargo_fso_load_event.0.location.country.id',
            'events.cargo_fso_load_event.0.location.country.label',
            'events.cargo_fso_load_event.0.location.country.layer',
            'events.cargo_fso_load_event.0.location.country.probability',
            'events.cargo_fso_load_event.0.location.country.source',
            'events.cargo_fso_load_event.0.location.region.id',
            'events.cargo_fso_load_event.0.location.region.label',
            'events.cargo_fso_load_event.0.location.region.layer',
            'events.cargo_fso_load_event.0.location.region.probability',
            'events.cargo_fso_load_event.0.location.region.source',
            'events.cargo_fso_load_event.0.location.shipping_region.id',
            'events.cargo_fso_load_event.0.location.shipping_region.label',
            'events.cargo_fso_load_event.0.location.shipping_region.layer',
            'events.cargo_fso_load_event.0.location.shipping_region.probability',
            'events.cargo_fso_load_event.0.location.shipping_region.source',
            'events.cargo_fso_load_event.0.location.sts_zone.id',
            'events.cargo_fso_load_event.0.location.sts_zone.label',
            'events.cargo_fso_load_event.0.location.sts_zone.layer',
            'events.cargo_fso_load_event.0.location.sts_zone.probability',
            'events.cargo_fso_load_event.0.location.sts_zone.source',
            'events.cargo_fso_load_event.0.location.trading_block.id',
            'events.cargo_fso_load_event.0.location.trading_block.label',
            'events.cargo_fso_load_event.0.location.trading_block.layer',
            'events.cargo_fso_load_event.0.location.trading_block.probability',
            'events.cargo_fso_load_event.0.location.trading_block.source',
            'events.cargo_fso_load_event.0.location.trading_region.id',
            'events.cargo_fso_load_event.0.location.trading_region.label',
            'events.cargo_fso_load_event.0.location.trading_region.layer',
            'events.cargo_fso_load_event.0.location.trading_region.probability',
            'events.cargo_fso_load_event.0.location.trading_region.source',
            'events.cargo_fso_load_event.0.location.trading_subregion.id',
            'events.cargo_fso_load_event.0.location.trading_subregion.label',
            'events.cargo_fso_load_event.0.location.trading_subregion.layer',
            'events.cargo_fso_load_event.0.location.trading_subregion.probability',
            'events.cargo_fso_load_event.0.location.trading_subregion.source',
            'events.cargo_fso_load_event.0.pos.0',
            'events.cargo_fso_load_event.0.pos.1',
            'events.cargo_fso_load_event.0.probability',
            'events.cargo_fso_load_event.0.start_timestamp',
            'events.cargo_fso_load_event.0.to_vessel_id',
            'events.cargo_fso_load_event.0.to_vessel_name',
            'events.cargo_fso_unload_event.0.end_timestamp',
            'events.cargo_fso_unload_event.0.event_type',
            'events.cargo_fso_unload_event.0.from_vessel_id',
            'events.cargo_fso_unload_event.0.from_vessel_name',
            'events.cargo_fso_unload_event.0.fso_vessel_id',
            'events.cargo_fso_unload_event.0.fso_vessel_name',
            'events.cargo_fso_unload_event.0.location.country.id',
            'events.cargo_fso_unload_event.0.location.country.label',
            'events.cargo_fso_unload_event.0.location.country.layer',
            'events.cargo_fso_unload_event.0.location.country.probability',
            'events.cargo_fso_unload_event.0.location.country.source',
            'events.cargo_fso_unload_event.0.location.region.id',
            'events.cargo_fso_unload_event.0.location.region.label',
            'events.cargo_fso_unload_event.0.location.region.layer',
            'events.cargo_fso_unload_event.0.location.region.probability',
            'events.cargo_fso_unload_event.0.location.region.source',
            'events.cargo_fso_unload_event.0.location.shipping_region.id',
            'events.cargo_fso_unload_event.0.location.shipping_region.label',
            'events.cargo_fso_unload_event.0.location.shipping_region.layer',
            'events.cargo_fso_unload_event.0.location.shipping_region.probability',
            'events.cargo_fso_unload_event.0.location.shipping_region.source',
            'events.cargo_fso_unload_event.0.location.sts_zone.id',
            'events.cargo_fso_unload_event.0.location.sts_zone.label',
            'events.cargo_fso_unload_event.0.location.sts_zone.layer',
            'events.cargo_fso_unload_event.0.location.sts_zone.probability',
            'events.cargo_fso_unload_event.0.location.sts_zone.source',
            'events.cargo_fso_unload_event.0.location.trading_block.id',
            'events.cargo_fso_unload_event.0.location.trading_block.label',
            'events.cargo_fso_unload_event.0.location.trading_block.layer',
            'events.cargo_fso_unload_event.0.location.trading_block.probability',
            'events.cargo_fso_unload_event.0.location.trading_block.source',
            'events.cargo_fso_unload_event.0.location.trading_region.id',
            'events.cargo_fso_unload_event.0.location.trading_region.label',
            'events.cargo_fso_unload_event.0.location.trading_region.layer',
            'events.cargo_fso_unload_event.0.location.trading_region.probability',
            'events.cargo_fso_unload_event.0.location.trading_region.source',
            'events.cargo_fso_unload_event.0.location.trading_subregion.id',
            'events.cargo_fso_unload_event.0.location.trading_subregion.label',
            'events.cargo_fso_unload_event.0.location.trading_subregion.layer',
            'events.cargo_fso_unload_event.0.location.trading_subregion.probability',
            'events.cargo_fso_unload_event.0.location.trading_subregion.source',
            'events.cargo_fso_unload_event.0.pos.0',
            'events.cargo_fso_unload_event.0.pos.1',
            'events.cargo_fso_unload_event.0.probability',
            'events.cargo_fso_unload_event.0.start_timestamp',
            'events.cargo_port_load_event.0.end_timestamp',
            'events.cargo_port_load_event.0.event_type',
            'events.cargo_port_load_event.0.location.country.id',
            'events.cargo_port_load_event.0.location.country.label',
            'events.cargo_port_load_event.0.location.country.layer',
            'events.cargo_port_load_event.0.location.country.probability',
            'events.cargo_port_load_event.0.location.country.source',
            'events.cargo_port_load_event.0.location.port.id',
            'events.cargo_port_load_event.0.location.port.label',
            'events.cargo_port_load_event.0.location.port.layer',
            'events.cargo_port_load_event.0.location.port.probability',
            'events.cargo_port_load_event.0.location.port.source',
            'events.cargo_port_load_event.0.location.region.id',
            'events.cargo_port_load_event.0.location.region.label',
            'events.cargo_port_load_event.0.location.region.layer',
            'events.cargo_port_load_event.0.location.region.probability',
            'events.cargo_port_load_event.0.location.region.source',
            'events.cargo_port_load_event.0.location.shipping_region.id',
            'events.cargo_port_load_event.0.location.shipping_region.label',
            'events.cargo_port_load_event.0.location.shipping_region.layer',
            'events.cargo_port_load_event.0.location.shipping_region.probability',
            'events.cargo_port_load_event.0.location.shipping_region.source',
            'events.cargo_port_load_event.0.location.terminal.id',
            'events.cargo_port_load_event.0.location.terminal.label',
            'events.cargo_port_load_event.0.location.terminal.layer',
            'events.cargo_port_load_event.0.location.terminal.probability',
            'events.cargo_port_load_event.0.location.terminal.source',
            'events.cargo_port_load_event.0.location.trading_block.id',
            'events.cargo_port_load_event.0.location.trading_block.label',
            'events.cargo_port_load_event.0.location.trading_block.layer',
            'events.cargo_port_load_event.0.location.trading_block.probability',
            'events.cargo_port_load_event.0.location.trading_block.source',
            'events.cargo_port_load_event.0.location.trading_region.id',
            'events.cargo_port_load_event.0.location.trading_region.label',
            'events.cargo_port_load_event.0.location.trading_region.layer',
            'events.cargo_port_load_event.0.location.trading_region.probability',
            'events.cargo_port_load_event.0.location.trading_region.source',
            'events.cargo_port_load_event.0.location.trading_subregion.id',
            'events.cargo_port_load_event.0.location.trading_subregion.label',
            'events.cargo_port_load_event.0.location.trading_subregion.layer',
            'events.cargo_port_load_event.0.location.trading_subregion.probability',
            'events.cargo_port_load_event.0.location.trading_subregion.source',
            'events.cargo_port_load_event.0.pos.0',
            'events.cargo_port_load_event.0.pos.1',
            'events.cargo_port_load_event.0.probability',
            'events.cargo_port_load_event.0.start_timestamp',
            'events.cargo_port_unload_event.0.end_timestamp',
            'events.cargo_port_unload_event.0.event_type',
            'events.cargo_port_unload_event.0.location.country.id',
            'events.cargo_port_unload_event.0.location.country.label',
            'events.cargo_port_unload_event.0.location.country.layer',
            'events.cargo_port_unload_event.0.location.country.probability',
            'events.cargo_port_unload_event.0.location.country.source',
            'events.cargo_port_unload_event.0.location.port.id',
            'events.cargo_port_unload_event.0.location.port.label',
            'events.cargo_port_unload_event.0.location.port.layer',
            'events.cargo_port_unload_event.0.location.port.probability',
            'events.cargo_port_unload_event.0.location.port.source',
            'events.cargo_port_unload_event.0.location.region.id',
            'events.cargo_port_unload_event.0.location.region.label',
            'events.cargo_port_unload_event.0.location.region.layer',
            'events.cargo_port_unload_event.0.location.region.probability',
            'events.cargo_port_unload_event.0.location.region.source',
            'events.cargo_port_unload_event.0.location.shipping_region.id',
            'events.cargo_port_unload_event.0.location.shipping_region.label',
            'events.cargo_port_unload_event.0.location.shipping_region.layer',
            'events.cargo_port_unload_event.0.location.shipping_region.probability',
            'events.cargo_port_unload_event.0.location.shipping_region.source',
            'events.cargo_port_unload_event.0.location.sts_zone.id',
            'events.cargo_port_unload_event.0.location.sts_zone.label',
            'events.cargo_port_unload_event.0.location.sts_zone.layer',
            'events.cargo_port_unload_event.0.location.sts_zone.probability',
            'events.cargo_port_unload_event.0.location.sts_zone.source',
            'events.cargo_port_unload_event.0.location.terminal.id',
            'events.cargo_port_unload_event.0.location.terminal.label',
            'events.cargo_port_unload_event.0.location.terminal.layer',
            'events.cargo_port_unload_event.0.location.terminal.probability',
            'events.cargo_port_unload_event.0.location.terminal.source',
            'events.cargo_port_unload_event.0.location.trading_block.id',
            'events.cargo_port_unload_event.0.location.trading_block.label',
            'events.cargo_port_unload_event.0.location.trading_block.layer',
            'events.cargo_port_unload_event.0.location.trading_block.probability',
            'events.cargo_port_unload_event.0.location.trading_block.source',
            'events.cargo_port_unload_event.0.location.trading_region.id',
            'events.cargo_port_unload_event.0.location.trading_region.label',
            'events.cargo_port_unload_event.0.location.trading_region.layer',
            'events.cargo_port_unload_event.0.location.trading_region.probability',
            'events.cargo_port_unload_event.0.location.trading_region.source',
            'events.cargo_port_unload_event.0.location.trading_subregion.id',
            'events.cargo_port_unload_event.0.location.trading_subregion.label',
            'events.cargo_port_unload_event.0.location.trading_subregion.layer',
            'events.cargo_port_unload_event.0.location.trading_subregion.probability',
            'events.cargo_port_unload_event.0.location.trading_subregion.source',
            'events.cargo_port_unload_event.0.pos.0',
            'events.cargo_port_unload_event.0.pos.1',
            'events.cargo_port_unload_event.0.probability',
            'events.cargo_port_unload_event.0.start_timestamp',
            'events.cargo_storage_event.0.end_timestamp',
            'events.cargo_storage_event.0.event_type',
            'events.cargo_storage_event.0.location.country.id',
            'events.cargo_storage_event.0.location.country.label',
            'events.cargo_storage_event.0.location.country.layer',
            'events.cargo_storage_event.0.location.country.probability',
            'events.cargo_storage_event.0.location.country.source',
            'events.cargo_storage_event.0.location.region.id',
            'events.cargo_storage_event.0.location.region.label',
            'events.cargo_storage_event.0.location.region.layer',
            'events.cargo_storage_event.0.location.region.probability',
            'events.cargo_storage_event.0.location.region.source',
            'events.cargo_storage_event.0.location.shipping_region.id',
            'events.cargo_storage_event.0.location.shipping_region.label',
            'events.cargo_storage_event.0.location.shipping_region.layer',
            'events.cargo_storage_event.0.location.shipping_region.probability',
            'events.cargo_storage_event.0.location.shipping_region.source',
            'events.cargo_storage_event.0.location.trading_block.id',
            'events.cargo_storage_event.0.location.trading_block.label',
            'events.cargo_storage_event.0.location.trading_block.layer',
            'events.cargo_storage_event.0.location.trading_block.probability',
            'events.cargo_storage_event.0.location.trading_block.source',
            'events.cargo_storage_event.0.location.trading_region.id',
            'events.cargo_storage_event.0.location.trading_region.label',
            'events.cargo_storage_event.0.location.trading_region.layer',
            'events.cargo_storage_event.0.location.trading_region.probability',
            'events.cargo_storage_event.0.location.trading_region.source',
            'events.cargo_storage_event.0.location.trading_subregion.id',
            'events.cargo_storage_event.0.location.trading_subregion.label',
            'events.cargo_storage_event.0.location.trading_subregion.layer',
            'events.cargo_storage_event.0.location.trading_subregion.probability',
            'events.cargo_storage_event.0.location.trading_subregion.source',
            'events.cargo_storage_event.0.pos.0',
            'events.cargo_storage_event.0.pos.1',
            'events.cargo_storage_event.0.start_timestamp',
            'events.cargo_storage_event.0.vessel_id',
            'events.cargo_sts_event.0.end_timestamp',
            'events.cargo_sts_event.0.event_type',
            'events.cargo_sts_event.0.from_vessel_id',
            'events.cargo_sts_event.0.from_vessel_name',
            'events.cargo_sts_event.0.location.country.id',
            'events.cargo_sts_event.0.location.country.label',
            'events.cargo_sts_event.0.location.country.layer',
            'events.cargo_sts_event.0.location.country.probability',
            'events.cargo_sts_event.0.location.country.source',
            'events.cargo_sts_event.0.location.port.id',
            'events.cargo_sts_event.0.location.port.label',
            'events.cargo_sts_event.0.location.port.layer',
            'events.cargo_sts_event.0.location.port.probability',
            'events.cargo_sts_event.0.location.port.source',
            'events.cargo_sts_event.0.location.region.id',
            'events.cargo_sts_event.0.location.region.label',
            'events.cargo_sts_event.0.location.region.layer',
            'events.cargo_sts_event.0.location.region.probability',
            'events.cargo_sts_event.0.location.region.source',
            'events.cargo_sts_event.0.location.shipping_region.id',
            'events.cargo_sts_event.0.location.shipping_region.label',
            'events.cargo_sts_event.0.location.shipping_region.layer',
            'events.cargo_sts_event.0.location.shipping_region.probability',
            'events.cargo_sts_event.0.location.shipping_region.source',
            'events.cargo_sts_event.0.location.sts_zone.id',
            'events.cargo_sts_event.0.location.sts_zone.label',
            'events.cargo_sts_event.0.location.sts_zone.layer',
            'events.cargo_sts_event.0.location.sts_zone.probability',
            'events.cargo_sts_event.0.location.sts_zone.source',
            'events.cargo_sts_event.0.location.trading_block.id',
            'events.cargo_sts_event.0.location.trading_block.label',
            'events.cargo_sts_event.0.location.trading_block.layer',
            'events.cargo_sts_event.0.location.trading_block.probability',
            'events.cargo_sts_event.0.location.trading_block.source',
            'events.cargo_sts_event.0.location.trading_region.id',
            'events.cargo_sts_event.0.location.trading_region.label',
            'events.cargo_sts_event.0.location.trading_region.layer',
            'events.cargo_sts_event.0.location.trading_region.probability',
            'events.cargo_sts_event.0.location.trading_region.source',
            'events.cargo_sts_event.0.location.trading_subregion.id',
            'events.cargo_sts_event.0.location.trading_subregion.label',
            'events.cargo_sts_event.0.location.trading_subregion.layer',
            'events.cargo_sts_event.0.location.trading_subregion.probability',
            'events.cargo_sts_event.0.location.trading_subregion.source',
            'events.cargo_sts_event.0.pos.0',
            'events.cargo_sts_event.0.pos.1',
            'events.cargo_sts_event.0.start_timestamp',
            'events.cargo_sts_event.0.to_vessel_id',
            'events.cargo_sts_event.0.to_vessel_name',
            'events.cargo_sts_event.1.end_timestamp',
            'events.cargo_sts_event.1.event_type',
            'events.cargo_sts_event.1.from_vessel_id',
            'events.cargo_sts_event.1.from_vessel_name',
            'events.cargo_sts_event.1.location.country.id',
            'events.cargo_sts_event.1.location.country.label',
            'events.cargo_sts_event.1.location.country.layer',
            'events.cargo_sts_event.1.location.country.probability',
            'events.cargo_sts_event.1.location.country.source',
            'events.cargo_sts_event.1.location.region.id',
            'events.cargo_sts_event.1.location.region.label',
            'events.cargo_sts_event.1.location.region.layer',
            'events.cargo_sts_event.1.location.region.probability',
            'events.cargo_sts_event.1.location.region.source',
            'events.cargo_sts_event.1.location.shipping_region.id',
            'events.cargo_sts_event.1.location.shipping_region.label',
            'events.cargo_sts_event.1.location.shipping_region.layer',
            'events.cargo_sts_event.1.location.shipping_region.probability',
            'events.cargo_sts_event.1.location.shipping_region.source',
            'events.cargo_sts_event.1.location.sts_zone.id',
            'events.cargo_sts_event.1.location.sts_zone.label',
            'events.cargo_sts_event.1.location.sts_zone.layer',
            'events.cargo_sts_event.1.location.sts_zone.probability',
            'events.cargo_sts_event.1.location.sts_zone.source',
            'events.cargo_sts_event.1.location.trading_block.id',
            'events.cargo_sts_event.1.location.trading_block.label',
            'events.cargo_sts_event.1.location.trading_block.layer',
            'events.cargo_sts_event.1.location.trading_block.probability',
            'events.cargo_sts_event.1.location.trading_block.source',
            'events.cargo_sts_event.1.location.trading_region.id',
            'events.cargo_sts_event.1.location.trading_region.label',
            'events.cargo_sts_event.1.location.trading_region.layer',
            'events.cargo_sts_event.1.location.trading_region.probability',
            'events.cargo_sts_event.1.location.trading_region.source',
            'events.cargo_sts_event.1.location.trading_subregion.id',
            'events.cargo_sts_event.1.location.trading_subregion.label',
            'events.cargo_sts_event.1.location.trading_subregion.layer',
            'events.cargo_sts_event.1.location.trading_subregion.probability',
            'events.cargo_sts_event.1.location.trading_subregion.source',
            'events.cargo_sts_event.1.pos.0',
            'events.cargo_sts_event.1.pos.1',
            'events.cargo_sts_event.1.start_timestamp',
            'events.cargo_sts_event.1.to_vessel_id',
            'events.cargo_sts_event.1.to_vessel_name',
            'product.category.id',
            'product.category.label',
            'product.category.layer',
            'product.category.probability',
            'product.category.source',
            'product.grade.id',
            'product.grade.label',
            'product.grade.layer',
            'product.grade.probability',
            'product.grade.source',
            'product.group.id',
            'product.group.label',
            'product.group.layer',
            'product.group.probability',
            'product.group.source',
            'product.group_product.id',
            'product.group_product.label',
            'product.group_product.layer',
            'product.group_product.probability',
            'product.group_product.source',
            'quantity',
            'status',
            'vessels.0.corporate_entities.charterer.id',
            'vessels.0.corporate_entities.charterer.label',
            'vessels.0.corporate_entities.charterer.layer',
            'vessels.0.corporate_entities.charterer.probability',
            'vessels.0.corporate_entities.charterer.source',
            'vessels.0.corporate_entities.commercial_owner.id',
            'vessels.0.corporate_entities.commercial_owner.label',
            'vessels.0.corporate_entities.commercial_owner.layer',
            'vessels.0.corporate_entities.commercial_owner.probability',
            'vessels.0.corporate_entities.commercial_owner.source',
            'vessels.0.corporate_entities.time_charterer.end_timestamp',
            'vessels.0.corporate_entities.time_charterer.id',
            'vessels.0.corporate_entities.time_charterer.label',
            'vessels.0.corporate_entities.time_charterer.layer',
            'vessels.0.corporate_entities.time_charterer.probability',
            'vessels.0.corporate_entities.time_charterer.source',
            'vessels.0.corporate_entities.time_charterer.start_timestamp',
            'vessels.0.cubic_capacity',
            'vessels.0.dwt',
            'vessels.0.end_timestamp',
            'vessels.0.fixture_fulfilled',
            'vessels.0.fixture_id',
            'vessels.0.id',
            'vessels.0.imo',
            'vessels.0.mmsi',
            'vessels.0.name',
            'vessels.0.start_timestamp',
            'vessels.0.status',
            'vessels.0.tags.0.end_timestamp',
            'vessels.0.tags.0.start_timestamp',
            'vessels.0.tags.0.tag',
            'vessels.0.vessel_class',
            'vessels.0.voyage_id',
            'vessels.1.corporate_entities.charterer.id',
            'vessels.1.corporate_entities.charterer.label',
            'vessels.1.corporate_entities.charterer.layer',
            'vessels.1.corporate_entities.charterer.probability',
            'vessels.1.corporate_entities.charterer.source',
            'vessels.1.corporate_entities.commercial_owner.id',
            'vessels.1.corporate_entities.commercial_owner.label',
            'vessels.1.corporate_entities.commercial_owner.layer',
            'vessels.1.corporate_entities.commercial_owner.probability',
            'vessels.1.corporate_entities.commercial_owner.source',
            'vessels.1.corporate_entities.time_charterer.end_timestamp',
            'vessels.1.corporate_entities.time_charterer.id',
            'vessels.1.corporate_entities.time_charterer.label',
            'vessels.1.corporate_entities.time_charterer.layer',
            'vessels.1.corporate_entities.time_charterer.probability',
            'vessels.1.corporate_entities.time_charterer.source',
            'vessels.1.corporate_entities.time_charterer.start_timestamp',
            'vessels.1.cubic_capacity',
            'vessels.1.dwt',
            'vessels.1.end_timestamp',
            'vessels.1.fixture_fulfilled',
            'vessels.1.id',
            'vessels.1.imo',
            'vessels.1.mmsi',
            'vessels.1.name',
            'vessels.1.start_timestamp',
            'vessels.1.status',
            'vessels.1.tags.0.end_timestamp',
            'vessels.1.tags.0.start_timestamp',
            'vessels.1.tags.0.tag',
            'vessels.1.vessel_class',
            'vessels.1.voyage_id',
            'vessels.2.corporate_entities.charterer.id',
            'vessels.2.corporate_entities.charterer.label',
            'vessels.2.corporate_entities.charterer.layer',
            'vessels.2.corporate_entities.charterer.probability',
            'vessels.2.corporate_entities.charterer.source',
            'vessels.2.corporate_entities.commercial_owner.id',
            'vessels.2.corporate_entities.commercial_owner.label',
            'vessels.2.corporate_entities.commercial_owner.layer',
            'vessels.2.corporate_entities.commercial_owner.probability',
            'vessels.2.corporate_entities.commercial_owner.source',
            'vessels.2.corporate_entities.time_charterer.end_timestamp',
            'vessels.2.corporate_entities.time_charterer.id',
            'vessels.2.corporate_entities.time_charterer.label',
            'vessels.2.corporate_entities.time_charterer.layer',
            'vessels.2.corporate_entities.time_charterer.probability',
            'vessels.2.corporate_entities.time_charterer.source',
            'vessels.2.corporate_entities.time_charterer.start_timestamp',
            'vessels.2.cubic_capacity',
            'vessels.2.dwt',
            'vessels.2.end_timestamp',
            'vessels.2.id',
            'vessels.2.imo',
            'vessels.2.mmsi',
            'vessels.2.name',
            'vessels.2.start_timestamp',
            'vessels.2.status',
            'vessels.2.tags.0.start_timestamp',
            'vessels.2.tags.0.tag',
            'vessels.2.vessel_class',
            'vessels.2.voyage_id',
            'vessels.3.corporate_entities.commercial_owner.id',
            'vessels.3.corporate_entities.commercial_owner.label',
            'vessels.3.corporate_entities.commercial_owner.layer',
            'vessels.3.corporate_entities.commercial_owner.probability',
            'vessels.3.corporate_entities.commercial_owner.source',
            'vessels.3.cubic_capacity',
            'vessels.3.dwt',
            'vessels.3.id',
            'vessels.3.imo',
            'vessels.3.mmsi',
            'vessels.3.name',
            'vessels.3.start_timestamp',
            'vessels.3.status',
            'vessels.3.vessel_class',
            'vessels.3.voyage_id',
            'parent_ids.0.id',
            'parent_ids.0.splinter_timestamp',
            'parent_ids.1.id',
            'parent_ids.1.splinter_timestamp',
        ]
        ```

        """
        if columns is None:
            columns = DEFAULT_COLUMNS

        flatten = functools.partial(
            convert_cargo_movement_to_flat_dict, cols=columns
        )

        logger.debug("Converting each CargoMovement to a flat dictionary")
        with Pool(os.cpu_count()) as pool:
            records = pool.map(flatten, super().to_list())

        return create_dataframe(
            columns=columns,
            default_columns=DEFAULT_COLUMNS,
            data=records,
            logger_description="CargoMovements",
        )


DEFAULT_COLUMNS = [
    "events.cargo_port_load_event.0.location.port.label",
    "events.cargo_port_unload_event.0.location.port.label",
    "product.group.label",
    "product.grade.label",
    "quantity",
    "vessels.0.name",
    "events.cargo_port_load_event.0.end_timestamp",
    "events.cargo_port_unload_event.0.start_timestamp",
]
