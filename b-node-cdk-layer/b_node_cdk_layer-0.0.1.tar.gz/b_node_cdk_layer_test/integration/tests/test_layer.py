import json

import boto3

from b_node_cdk_layer_test.integration.infrastructure.main_stack import MainStack


def test_FUNCTION_custom_node_function_WITH_node_cdk_layer_EXPECT_user_created() -> None:
    """
    Check whether created lambda function with node cdk layer can run CDK CLI commands.

    :return: No return.
    """
    function_name = MainStack.get_output(MainStack.LAMBDA_FUNCTION_KEY)

    response = boto3.client('lambda').invoke(
        FunctionName=function_name,
        InvocationType='RequestResponse'
    )

    output = json.loads(response['Payload'].read())
    print(output)

    assert output['output'] is not None
