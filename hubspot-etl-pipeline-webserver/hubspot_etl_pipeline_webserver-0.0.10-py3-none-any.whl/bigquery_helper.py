import os

from datetime import datetime

import pandas as pd

from google.cloud import bigquery
from google.cloud.exceptions import NotFound

from super_eureka import logging

def upload_as_new_table(client: bigquery.Client, src_filepath: str, dst_table_id: str) -> bool:
    logging.info('Trying to submit file for BigQuery.')

    job_config = bigquery.LoadJobConfig(
        create_disposition='CREATE_IF_NEEDED',
        write_disposition='WRITE_TRUNCATE'
    )

    logging.info('Reading file...')
    df = pd.read_csv(src_filepath, na_values='(No value)')

    logging.info('Procesing...')
    df.columns = df.columns.str.replace(' ', '_')
    df.rename(columns={
        'ad_group_id': 'ad_group_id_new',
        'ad_id': 'ad_id_new'
    }, inplace=True)
    df.columns = df.columns.str.upper()

    logging.info('Uploading...')
    load_job = client.load_table_from_dataframe(df, dst_table_id, job_config=job_config)
    result = load_job.result()

    if not result.error_result:
        logging.info('Success!')
    else:
        logging.info('Failed with the following error(s):')
        for error in result.errors:
            logging.info(f'\t{repr(error)}')
        
        now = datetime.now()
        file_name = f'failure_{now.day}-{now.month}-{now.day} {now.hour}-{now.minute}-{now.second}.csv'
        folder = os.path.dirname(src_filepath)
        renamed_file_path = os.path.join(folder, file_name)
        os.rename(src_filepath, renamed_file_path)
        logging.info(f'The file will be renamed as {file_name} and kept for future upload.')
        return False

    return True

def get_table(client: bigquery.Client, table_id: str) -> bigquery.Table:
    try:
        table = client.get_table(table_id)
        return table
    except NotFound:
        return None
        

def submit_for_bigquery(filepath: str) -> None:
    client = bigquery.Client()
    
    dst_table_id = os.getenv('BIGQUERY_TABLE_ID') # final table with deduplicated rows
    upload_table_id = os.getenv('BIGQUERY_UPLOAD_TABLE_ID') # table where the csv will be uploaded

    if not upload_as_new_table(client, filepath, upload_table_id):
        return
    

    dst_table = get_table(dst_table_id)
    if dst_table:
        temp_table_id = os.getenv('BIGQUERY_TEMP_TABLE_ID')

        logging.info(f"Destination table '{dst_table_id}' already exists and will be merged with.")
        logging.info(f"Creating intermediary table with all rows.")
        union_query_str = f"create or replace table `{temp_table_id}` as select * from `{upload_table_id}` union all select * from `{dst_table_id}`"
        union_query_job = client.query(union_query_str)
        union_query_job.result() # wait for result before continuing

        logging.info(f"Deduplicating.")
        deduplicate_query_str = f"create or replace table `{dst_table_id}` as select distinct * from `{temp_table_id}`"
        deduplicate_query_job = client.query(deduplicate_query_str)
        deduplicate_query_job.result() # wait

        logging.info(f"Deleting temporary table.")
        drop_temp_query_str = f"drop table `{temp_table_id}`"
        drop_temp_query_job = client.query(drop_temp_query_str)
        drop_temp_query_job.result()
    else:
        logging.info(f"Target table '{dst_table_id}' does not exist yet. This operation will only select distinct rows from the uploaded file and create it.")
        deduplicate_query_str = f"create table `{dst_table_id}` as select distinct * from `{upload_table_id}`"
        deduplicate_query_job = client.query(deduplicate_query_str)
        deduplicate_query_job.result()
        logging.info('Query finished.')
    
    # upload table by default already has a 1 day expiration so no need to drop it

    


    



