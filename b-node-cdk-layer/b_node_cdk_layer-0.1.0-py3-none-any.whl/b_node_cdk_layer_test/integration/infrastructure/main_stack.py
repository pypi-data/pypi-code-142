from aws_cdk.aws_lambda import Function, Runtime, Code
from aws_cdk.core import Construct, Duration
from b_aws_testing_framework.tools.cdk_testing.testing_stack import TestingStack

from b_node_cdk_layer.node_cdk_layer import NodeCdkLayer
from b_node_cdk_layer_test.integration.infrastructure.lambda_source_code import root


class MainStack(TestingStack):
    LAMBDA_FUNCTION_KEY = 'LambdaFunctionWithNodeCdkLayer'

    def __init__(self, scope: Construct) -> None:
        super().__init__(scope=scope)

        prefix = TestingStack.global_prefix()

        f = Function(
            scope=self,
            id='Function',
            function_name=f'{prefix}CustomNodeFunction',
            runtime=Runtime.PYTHON_3_9,
            handler='index.handler',
            code=Code.from_asset(root),
            layers=[NodeCdkLayer(self)],
            timeout=Duration.minutes(1),
            memory_size=512
        )

        self.add_output(self.LAMBDA_FUNCTION_KEY, value=f.function_name)
