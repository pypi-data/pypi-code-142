import boto3
import botocore
from dateutil.relativedelta import relativedelta
import datetime as dt
import pytz
import logging
from aws_recommendations.utils import *

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


# Generates recommendation to delete idle instances
def delete_or_downsize_instance_recommendation(self) -> list:
    logger.info(" ---Inside delete_or_downsize_instance_recommendation()")

    recommendation = []
    regions = self.session.get_available_regions('ec2')

    # iterating through all the available regions
    for region in regions:
        try:
            instance_lst = list_instances(self, region)

            for instance in instance_lst:
                response_cpu = get_metrics_stats(self, region, "AWS/EC2", [{'Name': 'InstanceId', 'Value': instance['InstanceId']}])
                # response_mem = get_metics_stats(session, region, "AWS/EC2", {'Name': 'InstanceId', 'Value': instance},
                # metric_name=) response_net_in = get_metrics_stats(region, "AWS/EC2", [{'Name': 'InstanceId',
                # 'Value': instance}], metric_name='NetworkIn') response_net_out = get_metrics_stats(region, "AWS/EC2",
                # [{'Name': 'InstanceId', 'Value': instance}], metric_name='NetworkOut') # print(response_net_in) print(
                # response_net_out) for r in response_net_in['Datapoints']: print(r['Average'])

                tmp_lst_cpu = []

                for r in response_cpu['Datapoints']:
                    tmp_lst_cpu.append(r['Average'])

                if len(tmp_lst_cpu) >= 7:
                    if max(tmp_lst_cpu) < 3:
                        try:
                            tags = instance['Tags']
                        except KeyError:
                            tags = None
                        temp = {
                            'Service Name': 'EC2 Instance',
                            'Id': instance['InstanceId'],
                            'Recommendation': 'Delete idle compute instance',
                            'Description': 'The Delete idle compute instances recommendation indicates that some compute instances are unused. Deleting unused compute instances saves you from paying for instances that you are not using.',
                            'Metadata': {
                                'Region': region,
                                'Instance Type': instance['InstanceType'],
                                'Tags': tags,
                                'LaunchTime': instance['LaunchTime']
                            },
                            'Recommendation Reason': {
                                'Average CPU Datapoints(7 days)': [float('{:.2f}'.format(x)) for x in tmp_lst_cpu]
                            }
                        }
                        recommendation.append(temp)
                    else:
                        avg = 0
                        for v in tmp_lst_cpu:
                            avg = avg + v
                        avg = avg / len(tmp_lst_cpu)

                        if avg < 5:
                            try:
                                tags = instance['Tags']
                            except KeyError:
                                tags = None
                            temp = {
                                'Service Name': 'EC2 Instance',
                                'Id': instance['InstanceId'],
                                'Recommendation': 'Downsize underutilized compute instances',
                                'Description': 'The Downsize underutilized compute instances recommendation indicates that some compute instances are bigger than needed. Implementing this recommendation saves you money without degrading performance.',
                                'Metadata': {
                                    'Region': region,
                                    'Instance Type': instance['InstanceType'],
                                    'Tags': tags,
                                    'LaunchTime': instance['LaunchTime']
                                },
                                'Recommendation Reason': {
                                    'Average CPU Datapoints(7 days)': [float('{:.2f}'.format(x)) for x in tmp_lst_cpu]
                                }
                            }
                            recommendation.append(temp)

        except botocore.exceptions.ClientError as e:
            logger.info("Something wrong with the region {}: {}".format(region, e))

    return recommendation


# generates the recommendation to delete unattached volumes
def purge_unattached_vol_recommendation(self) -> list:
    logger.info(" ---Inside purge_unattached_vol_recommendation()")

    recommendation = []
    regions = self.session.get_available_regions('ec2')

    # iterating through all the available regions
    for region in regions:
        try:
            vol_data = {}
            client = self.session.client('ec2', region_name=region)
            marker = ''
            while True:
                response = client.describe_volumes(
                    MaxResults=500,
                    NextToken=marker
                )
                for item in response['Volumes']:
                    create_time = item['CreateTime']
                    datetime_4_weeks_ago = dt.datetime.now() - dt.timedelta(weeks=4)
                    timezone = pytz.timezone("UTC")
                    datetime_4_weeks_ago = timezone.localize(datetime_4_weeks_ago)

                    older = create_time <= datetime_4_weeks_ago
                    if older:
                        # vol_data[item['VolumeId']] = item['Attachments']
                        if len(item['Attachments']) == 0:
                            try:
                                tags = item['Tags']
                            except KeyError:
                                tags = None
                            temp = {
                                'Service Name': 'Volume',
                                'Id': item['VolumeId'],
                                'Recommendation': 'Purge unattached volume',
                                'Description': 'The Delete unattached volumes recommendation indicates that unattached volumes exists. Attaching or deleting unattached volumes reduces costs.',
                                'Metadata': {
                                    'Region': region,
                                    'Instance Type': item['VolumeType'],
                                    'Tags': tags,
                                    'CreateTime': item['CreateTime']
                                },
                                'Recommendation Reason': {
                                    'This Volume is 4 weeks older and is not attached to any instance'
                                }
                            }
                            recommendation.append(temp)
                try:
                    marker = response['NextToken']
                    if marker == '':
                        break
                except KeyError:
                    break

        except botocore.exceptions.ClientError as e:
            logger.info("Something wrong with the region {}: {}".format(region, e))

    return recommendation


# Generates the recommendation to purge the snapshots which are older than 8 weeks
def purge_8_weeks_older_snapshots(self) -> list:
    logger.info(" ---Inside purge_8_weeks_older_snapshots()")

    recommendation = []
    regions = self.session.get_available_regions('ec2')

    datetime_8_weeks_ago = dt.datetime.now() - dt.timedelta(weeks=8)
    timezone = pytz.timezone("UTC")
    datetime_8_weeks_ago = timezone.localize(datetime_8_weeks_ago)

    for region in regions:
        try:
            client = self.session.client('ec2', region_name=region)
            marker = ''
            while True:
                response = client.describe_snapshots(
                    MaxResults=1000,
                    OwnerIds=['self'],
                    NextToken=marker
                )
                for snapshot in response['Snapshots']:
                    start_time = snapshot['StartTime']
                    older = start_time <= datetime_8_weeks_ago

                    if older:
                        service_name = 'Snanshot'
                        r_id =  snapshot['SnapshotId']
                        recom = 'Purge 8 week older snapshot'
                        desc = 'The Delete 8 weeks older snapshot recommendation indicates that snapshots is older than 8 weeks exists. Deleting older snapshots reduces costs.'

                        try:
                            tags = snapshot['Tags']
                        except KeyError:
                            tags = None

                        metadata = {
                            'Region': region,
                            # 'StorageTier': snapshot['StorageTier'],
                            'Tags': tags,
                            'CreateTime': snapshot['StartTime']
                        }
                        reason = {
                            'This snapshot is 8 weeks older'
                        }
                        temp = {
                            'Service Name': service_name,
                            'Id': r_id,
                            'Recommendation': recom,
                            'Description': desc,
                            'Metadata': metadata,
                            'Recommendation Reason': reason
                        }
                        recommendation.append(temp)

                try:
                    marker = response['NextToken']
                    if marker == '':
                        break
                except KeyError:
                    break
        except botocore.exceptions.ClientError as e:
            logger.info("Something wrong with the region {}: {}".format(region, e))
    return recommendation








