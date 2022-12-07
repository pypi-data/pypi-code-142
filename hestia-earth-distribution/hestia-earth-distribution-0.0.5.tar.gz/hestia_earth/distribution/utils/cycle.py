from hestia_earth.utils.api import search, download_hestia
from hestia_earth.utils.tools import non_empty_list

from ..log import logger


def find_cycles(country_id: str, product_id: str, limit: int, recalculated: bool = False):
    country_name = download_hestia(country_id).get('name')
    product_name = download_hestia(product_id).get('name')
    cycles = search({
        'bool': {
            'must': [
                {
                    'match': {'@type': 'Cycle'}
                },
                {
                    'nested': {
                        'path': 'products',
                        'query': {
                            'bool': {
                                'must': [
                                    {'match': {'products.term.name.keyword': product_name}},
                                    {'match': {'products.primary': 'true'}}
                                ]
                            }
                        }
                    }
                },
                {
                    'match': {
                        'site.country.name.keyword': country_name
                    }
                }
            ],
            'must_not': [{'match': {'aggregated': True}}]
        }
    }, limit=limit)
    logger.info(f"Found {len(cycles)} non-aggregated cycles with primary product '{product_name}' in '{country_name}'.")
    cycles = [download_hestia(c['@id'], 'Cycle', 'recalculated' if recalculated else None) for c in cycles]
    return non_empty_list(cycles)
