import contextlib
import datetime
import logging
import time

import pandas as pd

from tableconv.adapters.df.base import Adapter, register_adapter
from tableconv.exceptions import InvalidQueryError
from tableconv.parse_time import parse_input_time
from tableconv.uri import parse_uri

logger = logging.getLogger(__name__)


@register_adapter(['awslogs'], read_only=True)
class AWSDynamoDB(Adapter):
    @staticmethod
    def get_example_url(scheme):
        return f'{scheme}://eu-central-1/example_table'

    @staticmethod
    def load(uri, query):
        import boto3
        uri = parse_uri(uri)
        aws_region = uri.authority

        # /aws/lambda/mensa-ree-prod-web

        from_time = parse_input_time(uri.query['from'])
        if 'to' in uri.query:
            to_time = parse_input_time(uri.query['to'])
        else:
            to_time = datetime.datetime.now(tz=datetime.timezone.utc)
        client = boto3.client('logs', region_name=aws_region)

        if query:
            query_id = client.start_query(
                logGroupName=uri.path,
                startTime=int(from_time.timestamp()),
                endTime=int(to_time.timestamp()),
                queryString=query,
                limit=uri.query.get('limit', 1000)
            )['queryId']

            try:
                while True:
                    results = client.get_query_results(queryId=query_id)
                    if results['status'] in ('Failed', 'Timeout', 'Unknown'):
                        raise InvalidQueryError(f'AWS CloudWatch Logs Insights Query {results["status"]}.')
                    elif results['status'] == 'Complete':
                        break
                    else:
                        assert results['status'] in ('Running', 'Scheduled')
                        POLL_INTERVAL = datetime.timedelta(seconds=2)
                        time.sleep(POLL_INTERVAL.total_seconds())
                    raw_array = [{item['field']: item['value'] for item in row.items()} for row in results['results']]
                    break
            except Exception as exc:
                with contextlib.suppress(Exception):
                    client.stop_query(query_id)
                raise exc
        else:
            # scan_results = client.get_log_events
            # raw_array = []
            # for response in scan_results:
            #     raw_array.extend(response['Items'])
            raise NotImplementedError

        return pd.DataFrame.from_records(raw_array)
