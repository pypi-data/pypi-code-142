import logging

import botocore

from aws_recommendations.utils import *

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# Generates the recommendation to downsize underutilized rds instance
def downsize_underutilized_rds_recommendation(self) -> list:
    logger.info(" ---Inside downsize_underutilized_rds_recommendation()")

    recommendation = []
    regions = self.session.get_available_regions('rds')

    for region in regions:
        try:
            rds_instance_lst = list_rds_instances(self, region)

            for instance in rds_instance_lst:
                cpu_stats = get_metrics_stats(
                    self, region, namespace='AWS/RDS',
                    dimensions=[{'Name': 'DBInstanceIdentifier', 'Value': instance['DBInstanceIdentifier']}]
                )

                if len(cpu_stats['Datapoints']) >= 7:
                    flag = True
                    for points in cpu_stats['Datapoints']:
                        if points['Average'] > 30:
                            flag = False
                            break

                    if flag:
                        try:
                            Tags = instance['TagList']
                        except KeyError:
                            Tags = None
                        temp = {
                            'Service Name': 'RDS Instance',
                            'Id': instance['DBInstanceIdentifier'],
                            'Recommendation': 'Downsize underutilized rds instance',
                            'Description': '',
                            'Metadata': {
                                'Region': region,
                                'DBInstanceClass': instance['DBInstanceClass'],
                                'Engine': instance['Engine'],
                                'Tags': Tags,
                                'InstanceCreateTime': instance['InstanceCreateTime']
                            },
                            'Recommendation Reason': {
                                'Datapoints': cpu_stats['Datapoints']
                            }
                        }
                        recommendation.append(temp)

        except botocore.exceptions.ClientError as e:
            logger.info("Something wrong with the region {}: {}".format(region, e))

    return recommendation