import botocore
import logging
from OBP_reliability_pillar.utils import *

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


# EC2 compliance
def ec2_compliance(self) -> dict:
    logger.info(" ---Inside ec2_compliance()")
    regions = self.session.get_available_regions('ec2')

    res = {}
    for region in regions:
        try:
            client = self.session.client('ec2', region_name=region)
            marker = ''
            while True:
                response = client.describe_instances(
                    MaxResults=1000,
                    NextToken=marker
                )
                if len(response['Reservations']) > 0:
                    for i in response['Reservations'][0]['Instances']:
                        com = i['Monitoring']['State']
                        if com == 'enabled':
                            res = insert_to_res(res, i['InstanceId'], 'EC2 Instance', 'Instance Detailed Monitoring Enabled',
                                          'Compliant')
                        else:
                            res = insert_to_res(res, i['InstanceId'], 'EC2 Instance', 'Instance Detailed Monitoring Enabled',
                                          'Not Compliant')

                try:
                    marker = response['NextToken']
                    if marker == '':
                        break
                except KeyError:
                    break
        except botocore.exceptions.ClientError:
            pass


    return res if res else None


# Check RDS compliance
def rds_compliance(self) -> dict:
    logger.info(" ---Inside rds_compliance()")
    regions = self.session.get_available_regions('rds')

    res = {}

    def automatic_minor_version_enabled(i, r) -> dict:
        logger.info(" ---Inside rds_compliance() :: automatic_minor_version_enabled()")
        com = i['AutoMinorVersionUpgrade']
        if com:
            r = insert_to_res(r, i['DBInstanceIdentifier'], 'RDS Instance', 'RDS Automatic Minor Version Enabled',
                          'Compliant')
        else:
            r = insert_to_res(r, i['DBInstanceIdentifier'], 'RDS Instance', 'RDS Automatic Minor Version Enabled',
                          'Non Compliant')
        return r

    def instance_backup_enabled(i, r) -> dict:
        logger.info(" ---Inside rds_compliance() :: instance_backup_enabled()")

        com = i['AutoMinorVersionUpgrade']
        if com:
            r = insert_to_res(r, i['DBInstanceIdentifier'], 'RDS Instance', 'RDS Instance Backup Enabled',
                          'Compliant')
        else:
            r = insert_to_res(r, i['DBInstanceIdentifier'], 'RDS Instance', 'RDS Instance Backup Enabled',
                          'Not Compliant')
        return r

    def instance_deletion_protection_enabled(i, r) -> dict:
        logger.info(" ---Inside rds_compliance() :: instance_deletion_protection_enabled()")

        com = i['DeletionProtection']
        if com:
            r = insert_to_res(r, i['DBInstanceIdentifier'], 'RDS Instance', 'RDS Instance Deletion Protection Enabled',
                          'Compliant')
        else:
            r = insert_to_res(r, i['DBInstanceIdentifier'], 'RDS Instance', 'RDS Instance Deletion Protection Enabled',
                          'Not Compliant')
        return r

    def multi_az_support_enabled(i, r) -> dict:
        logger.info(" ---Inside rds_compliance() :: multi_az_support_enabled()")

        com = i['MultiAZ']
        if com:
            r = insert_to_res(r, i['DBInstanceIdentifier'], 'RDS Instance', 'RDS Instance Multi AZ support',
                          'Compliant')
        else:
            r = insert_to_res(r, i['DBInstanceIdentifier'], 'RDS Instance', 'RDS Instance Multi AZ support',
                          'Not Compliant')
        return r

    def enhanced_monitoring_enable(i, r) -> dict:
        logger.info(" ---Inside rds_compliance() :: enhanced_monitoring_enable()")

        monitoring_interval = int(i['MonitoringInterval'])
        if monitoring_interval > 0:
            r = insert_to_res(r, i['DBInstanceIdentifier'], 'RDS Instance', 'RDS Enhanced Monitoring Enabled',
                          'Compliant')
        else:
            r = insert_to_res(r, i['DBInstanceIdentifier'], 'RDS Instance', 'RDS Enhanced Monitoring Enabled',
                          'Not Compliant')
        return r

    for region in regions:
        try:
            client = self.session.client('rds', region_name=region)
            marker = ''
            while True:
                response = client.describe_db_instances(
                    MaxRecords=100,
                    Marker=marker
                )
                for instance in response['DBInstances']:
                    res = automatic_minor_version_enabled(instance, res)
                    res = instance_backup_enabled(instance, res)
                    res = instance_deletion_protection_enabled(instance, res)
                    res = multi_az_support_enabled(instance, res)
                    res = enhanced_monitoring_enable(instance, res)

                try:
                    marker = response['Marker']
                    if marker == '':
                        break
                except KeyError:
                    break
        except botocore.exceptions.ClientError:
            pass
    return res if res else None


# Check S3 Compliance
def s3_compliance(self) -> dict:
    logger.info(" ---Inside s3_compliance()")
    client = self.session.client('s3')
    response = client.list_buckets()
    res = {}

    def bucket_versioning(r: dict, bucket_name: str) -> dict:
        logger.info(" ---Inside s3_compliance() :: bucket_versioning()")

        try:
            resp = client.get_bucket_versioning(
                Bucket=bucket_name,
            )
            status = resp['Status']
            if status == 'Enabled':
                r = insert_to_res(r, bucket['Name'], 'S3 Bucket', 'Bucket Versioning Enabled',
                              'Compliant', 'Configuration found, status="enabled"')
            else:
                r = insert_to_res(r, bucket['Name'], 'S3 Bucket', 'Bucket Versioning Enabled',
                              'Not Compliant', 'Configuration found, status="Disabled"')
        except:
            r = insert_to_res(r, bucket['Name'], 'S3 Bucket', 'Bucket Versioning Enabled',
                          'Not Compliant', 'Configuration Not found')
        return r

    def bucket_replication(r: dict, bucket_name: str) -> dict:
        logger.info(" ---Inside s3_compliance() :: bucket_replication()")

        try:
            resp = client.get_bucket_replication(
                Bucket=bucket_name
            )

            status = resp['ReplicationConfiguration']['Rules'][0]['Status']
            if status == 'Enabled':
                r = insert_to_res(r, bucket['Name'], 'S3 Bucket', 'Bucket Replication Enabled',
                                  'Compliant', 'Configuration Found, stats="Enabled"')
            else:
                r = insert_to_res(r, bucket['Name'], 'S3 Bucket', 'Bucket Replication Enabled',
                                  'Not Compliant', 'Configuration found, status="Disabled"')
        except:
            r = insert_to_res(r, bucket['Name'], 'S3 Bucket', 'Bucket Replication Enabled',
                              'Not Compliant', 'Configuration Not found')
        return r

    for bucket in response['Buckets']:
        res = bucket_versioning(res, bucket['Name'])
        res = bucket_replication(res, bucket['Name'])

    return res if res else None


# checks autoscaling compliance
def autoscaling_compliance(self) -> dict:
    logger.info(" ---Inside autoscaling_compliance()")
    regions = self.session.get_available_regions('autoscaling')

    res = {}

    def asg_elb_healthcheck_required(group, r) -> dict:
        logger.info(" ---Inside autoscaling_compliance() :: asg_elb_healthcheck_required()")

        if group['HealthCheckType'] == 'ELB':
            r = insert_to_res(r, group['AutoScalingGroupName'],
                          'Auto Scaling Group',
                          'Auto Scaling Group ELB health check required',
                          'Compliant')
        else:
            r = insert_to_res(r, group['AutoScalingGroupName'],
                          'Auto Scaling Group',
                          'Auto Scaling Group ELB health check required',
                          'Not Compliant')
        return r

    def launch_config_public_ip_disabled(r, reg) -> dict:
        logger.info(" ---Inside autoscaling_compliance() :: launch_config_public_ip_disabled()")

        client_asg = self.session.client('autoscaling', region_name=reg)

        n_token = ''
        while True:
            if n_token == '' or n_token is None:
                autoscaling_response = client_asg.describe_launch_configurations()
            else:
                autoscaling_response = client_asg.describe_launch_configurations(
                    NextToken = n_token
                )
            for lc in autoscaling_response['LaunchConfigurations']:
                if lc['AssociatePublicIpAddress']:
                    r = insert_to_res(r, lc['LaunchConfigurationARN'],
                                      'Auto Scaling Launch Configuration',
                                      'Launch configuration public ip disabled',
                                      'Not Compliant',
                                      'Launch configuration public ip is enabled, disable it')
                else:
                    r = insert_to_res(r, lc['LaunchConfigurationARN'],
                                      'Auto Scaling Launch Configuration',
                                      'Launch configuration public ip disabled',
                                      'Compliant',
                                      'Launch configuration public ip is disabled')
            try:
                n_token = autoscaling_response['NextToken']
                if n_token == '':
                    break
            except KeyError:
                break

        return r

    for region in regions:
        try:
            client = self.session.client('autoscaling', region_name = region)
            marker = ''
            while True:
                if marker == '':
                    response = client.describe_auto_scaling_groups(
                        MaxRecords=100
                    )
                else:
                    response = client.describe_auto_scaling_groups(
                        NextToken=marker,
                        MaxRecords=100
                    )
                for asg in response['AutoScalingGroups']:
                    res = asg_elb_healthcheck_required(asg, res)

                res = launch_config_public_ip_disabled(res, region)
                try:
                    marker = response['NextToken']
                    if marker == '':
                        break
                except KeyError:
                    break
        except botocore.exceptions.ClientError:
            pass

    return res if res else None


# checks elb compliance
def elb_compliance(self) -> dict:
    logger.info(" ---Inside elb_compliance()")

    res = {}
    regions = self.session.get_available_regions('elb')

    def cross_zone_load_balancing_enabled(r: dict, elb_name: str, reg: str) -> dict:
        logger.info(" ---Inside elb_compliance() :: cross_zone_load_balancing_enabled()")

        client = self.session.client('elb', region_name=reg)
        response = client.describe_load_balancer_attributes(
            LoadBalancerName=elb_name
        )
        if response['LoadBalancerAttributes']['CrossZoneLoadBalancing']['Enabled']:
            r = insert_to_res(r, elb_name, 'Load Balancer', 'Cross Zone Load Balancing Enabled', 'Compliant', 'Configuration found, status="enabled"')
        else:
            r = insert_to_res(r, elb_name, 'Load Balancer', 'Cross Zone Load Balancing Enabled', 'Non Compliant',
                              'Configuration found, status="Disabled"')

        return r

    for region in regions:
        try:
            elb_lst = list_elb(self, region)
            for elb in elb_lst:
                res = cross_zone_load_balancing_enabled(res, elb, region)
        except botocore.exceptions.ClientError:
            pass

    return res if res else None


# checks redshift compliance
def redshift_compliance(self) -> dict:
    logger.info(" ---Inside redshift_compliance()")
    res = {}
    regions = self.session.get_available_regions('redshift')

    def redshift_backup_enabled(r: dict) -> dict:
        logger.info(" ---Inside redshift_compliance() :: redshift_backup_enabled()")

        marker = ''
        while True:
            if marker == '' or marker is None:
                response = client.describe_clusters()
            else:
                response = client.describe_clusters(
                    Marker=marker
                )
            for cluster in response['Clusters']:
                retention_period = cluster['AutomatedSnapshotRetentionPeriod']
                if retention_period > 0:
                    r = insert_to_res(r, cluster['ClusterIdentifier'], 'Redshift Cluster', 'Backup Enabled', 'Compliant', 'Configuration found, "AutomatedSnapshotRetentionPeriod" > 0')
                else:
                    r = insert_to_res(r, cluster['ClusterIdentifier'], 'Redshift Cluster', 'Backup Enabled', 'Non Compliant', 'Configuration found, "AutomatedSnapshotRetentionPeriod" <= 0')

            try:
                marker = response['Marker']
                if marker == '':
                    break
            except KeyError:
                break

        return r

    for region in regions:
        try:
            client = self.session.client('redshift', region_name=region)
            res = redshift_backup_enabled(res)
        except botocore.exceptions.ClientError:
            pass

    return res if res else None


# checks compliance for security hub enabled
def security_hub_enabled(self) ->dict:
    logger.info(" ---Inside security_hub_enabled()")
    res = {}
    client = self.session.client('securityhub')
    try:
        response = client.describe_hub()
        # Scenario 1: SecurityHub is enabled for an AWS Account
        if response:
            res = insert_to_res(res, response['HubArn'], 'SecurityHub', 'SecurityHub enabled',
                                'Compliant', 'SecurityHub is enabled')
    except botocore.exceptions.ClientError as error:
        # Scenario 2: SecurityHub is not enabled for an AWS account.
        if error.response['Error']['Code'] == 'InvalidAccessException':
            res = insert_to_res(res, None, 'SecurityHub', 'SecurityHub enabled',
                                'Non Compliant', 'SecurityHub is disabled')

    return res if res else None


# checks compliance for elastic beanstalk
def elastic_beanstalk_compliance(self) -> dict:
    logger.info(" ---Inside elastic_beanstalk_compliance()")
    response = {}
    regions = self.session.get_available_regions('elasticbeanstalk')

    def enhanced_health_reporting_enabled(res, reg) -> dict:
        logger.info(" ---Inside elastic_beanstalk_compliance() :: enhanced_health_reporting_enabled()")

        client = self.session.client('elasticbeanstalk', region_name=reg)

        marker = ''
        while True:
            if marker == '' or marker is None:
                response_describe_eb = client.describe_environments()
            else:
                response_describe_eb = client.describe_environments(
                    NextToken=marker
                )
            for env in response_describe_eb['Environments']:
                if len(env['HealthStatus']) == 0:
                    res = insert_to_res(res, env['EnvironmentId'],
                                        'Elastic Beanstalk Environment', 'Enhanced Health Reporting Enabled', 'Non Compliant', 'Enhanced health reporting is disabled')
                else:
                    res = insert_to_res(res, env['EnvironmentId'],
                                        'Elastic Beanstalk Environment', 'Enhanced Health Reporting Enabled',
                                        'Compliant', 'Enhanced health reporting is Enabled')

            try:
                marker = response_describe_eb['NextToken']
                if marker == '':
                    break
            except KeyError:
                break
        return res

    for region in regions:
        try:
            response = enhanced_health_reporting_enabled(response, region)
        except botocore.exceptions.ClientError:
            pass

    return response if response else None


# checks compliance for cloudwatch
def cloudwatch_compliance(self) -> dict:
    logger.info(" ---Inside cloudwatch_compliance()")
    response = {}
    regions = self.session.get_available_regions('cloudwatch')

    def alarm_action_check(res, reg) -> dict:
        logger.info(" ---Inside cloudwatch_compliance() :: alarm_action_check()")

        client = self.session.client('cloudwatch', region_name=reg)
        marker = ''
        while True:
            if marker == '' or marker is None:
                response_describe_alarms = client.describe_alarms()
            else:
                response_describe_alarms = client.describe_alarms(
                    NextToken=marker
                )
            for alarm in response_describe_alarms['CompositeAlarms']:
                alarm_action = len(alarm['AlarmActions'])
                insufficient_data_action = len(alarm['InsufficientDataActions'])
                ok_action = len(alarm['OKActions'])

                if alarm_action or insufficient_data_action or ok_action:
                    res = insert_to_res(res, alarm['AlarmName'], 'CloudWatch Alarm', 'Cloudwatch alarm action check', 'Compliant', 'Checks whether CloudWatch alarms have at least one alarm action, one INSUFFICIENT_DATA action, or one OK action enabled.')

            for alarm in response_describe_alarms['MetricAlarms']:
                alarm_action = len(alarm['AlarmActions'])
                insufficient_data_action = len(alarm['InsufficientDataActions'])
                ok_action = len(alarm['OKActions'])

                if alarm_action or insufficient_data_action or ok_action:
                    res = insert_to_res(res, alarm['AlarmName'], 'CloudWatch Alarm', 'Cloudwatch alarm action check', 'Compliant',
                            'Checks whether CloudWatch alarms have at least one alarm action, one INSUFFICIENT_DATA action, or one OK action enabled.')

            try:
                marker = response_describe_alarms['NextToken']
                if marker == '':
                    break
            except KeyError:
                break

        return res

    for region in regions:
        try:
            response = alarm_action_check(response, region)
        except botocore.exceptions.ClientError:
            pass

    return response if response else None


# combines all compliance details and return
def get_compliance(self) -> dict:
    logger.info(" ---Inside get_compliance()")
    res = {}

    comp_lst = [
        ec2_compliance(self),
        rds_compliance(self),
        s3_compliance(self),
        autoscaling_compliance(self),
        redshift_compliance(self),
        cloudwatch_compliance(self),
        elastic_beanstalk_compliance(self),
        elb_compliance(self),
        security_hub_enabled(self)
    ]
    # print(str(comp_lst))
    res = extend_res(res, comp_lst)

    return res
# end of the code
