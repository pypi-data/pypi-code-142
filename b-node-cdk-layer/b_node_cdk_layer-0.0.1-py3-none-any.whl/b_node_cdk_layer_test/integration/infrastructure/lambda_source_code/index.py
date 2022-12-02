import subprocess

# This is the path to AWS CDK CLI. It comes from a NodeCDK layer, that is a custom-built layer using docker.
CDK_CLI_PATH = '/opt/bin/node_modules/aws-cdk/bin/cdk'


def handler(*args, **kwargs):
    output = subprocess.check_output([
        CDK_CLI_PATH,
        '--version',
    ])

    print(output)

    return {
        'output': output
    }
