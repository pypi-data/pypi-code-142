from singer import metadata
import singer
from ankit_db.sync_strategies import log_based
from ankit_db.sync_strategies import full_table

LOGGER = singer.get_logger()


def sync_stream(config, state, stream):
    table_name = stream['tap_stream_id']

    md_map = metadata.to_map(stream['metadata'])

    key_properties = metadata.get(md_map, (), 'table-key-properties')

    # write state message with currently_syncing bookmark
    state = singer.set_currently_syncing(state, table_name)
    singer.write_state(state)

    singer.write_message(singer.SchemaMessage(
        stream=table_name,
        schema=stream['schema'],
        key_properties=key_properties))

    rows_saved = 0

    LOGGER.info("Syncing log based for stream: %s", table_name)

    if log_based.has_stream_aged_out(state, table_name):
        LOGGER.info("Clearing state because stream has aged out")
        state.get('bookmarks', {}).pop(table_name)

    if not singer.get_bookmark(state, table_name, 'initial_full_table_complete'):
        msg = 'Must complete full table sync before replicating from dynamodb streams for %s'
        LOGGER.info(msg, table_name)

        state = log_based.get_initial_bookmarks(config, state, table_name)
        singer.write_state(state)

        rows_saved += full_table.sync(config, state, stream)

    rows_saved += log_based.sync(config, state, stream)
   
    state = singer.write_bookmark(state, table_name, 'success_timestamp', singer.utils.strftime(singer.utils.now()))
    singer.write_state(state)

    return rows_saved
