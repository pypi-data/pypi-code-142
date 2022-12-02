from aws_cdk.aws_lambda import LayerVersion, Code
from aws_cdk.core import Stack


class NodeCdkLayer(LayerVersion):
    def __init__(self, scope: Stack, *args, **kwargs) -> None:
        """
        Constructor.

        :param scope: Cloudformation stack which will contain this layer resource.
        :param args: Other (unused) positional arguments.
        :param kwargs: Other (unused) named arguments.
        """
        super().__init__(
            scope=scope,
            id='NodeCdkLayer',
            code=Code.from_docker_build(path=self.get_source_path()),
        )

    @staticmethod
    def get_source_path() -> str:
        from . import root
        return root
