import pymongo
class Mixin:
    def search_transfers_mongo(self, transfer_type, gte, lte, start_date, end_date, 
        skip, limit, sort_on='amount', sort_direction=-1, memo_only=False):
        
        sort_direction = pymongo.ASCENDING if sort_direction == 1 else pymongo.DESCENDING
        sort_condition = { '$sort':      { 'amount_ccd': sort_direction} } if sort_on =='amount' else { '$sort':      { 'blockInfo.blockSlotTime': sort_direction} }
        type_contents_condition = ['transferWithMemo'] if memo_only else ['transfer','transferWithMemo']
        pipeline = [
            {
                '$match': { 'type.contents': { '$in': type_contents_condition } }
            }, 
            { '$addFields': 
                { 'amount_ccd': 
                { '$first' :
                    {
                    '$map':
                        {
                        'input': "$result.events",
                        'as': "events",
                        'in': { '$trunc': { '$divide': [{'$toDouble': '$$events.amount'}, 1000000] } }
                        }
                    }
                }
                }
            },
            { '$match':     { 'amount_ccd': { '$gte': gte } } },
            { '$match':     { 'amount_ccd': { '$lte': lte } } },
            { "$match":     {"blockInfo.blockSlotTime": {"$gte": start_date, "$lt": end_date } } },
            sort_condition,
            {'$facet': {
            'metadata': [ { '$count': 'total' } ],
            'data': [ { '$skip': int(skip) }, { '$limit': int(limit) } ]
            }},
            {'$project': { 
                'data': 1,
                'total': { '$arrayElemAt': [ '$metadata.total', 0 ] }
            }
            }
        ]

        return pipeline