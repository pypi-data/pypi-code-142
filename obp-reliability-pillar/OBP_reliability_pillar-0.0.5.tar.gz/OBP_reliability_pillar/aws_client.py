from OBP_reliability_pillar import compliance_functions as comp
from boto3 import session


class aws_client:
    def __init__(self, aws_access_key_id, aws_secret_access_key):
        self.session = session.Session(
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key
        )

    get_compliance = comp.get_compliance
    get_autoscaling_compliance = comp.autoscaling_compliance
    get_s3_compliance = comp.s3_compliance
    get_rds_compliance = comp.rds_compliance
    get_ec2_compliance = comp.ec2_compliance
    get_elb_compliance = comp.elb_compliance
    get_redshift_compliance = comp.redshift_compliance
    get_elastic_beanstalk_compliance = comp.elastic_beanstalk_compliance
    get_security_hub_compliance = comp.security_hub_enabled
    get_cloudwatch_compliance = comp.cloudwatch_compliance



