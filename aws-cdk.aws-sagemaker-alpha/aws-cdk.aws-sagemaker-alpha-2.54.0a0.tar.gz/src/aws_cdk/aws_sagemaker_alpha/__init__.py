'''
# Amazon SageMaker Construct Library

<!--BEGIN STABILITY BANNER-->---


![cdk-constructs: Experimental](https://img.shields.io/badge/cdk--constructs-experimental-important.svg?style=for-the-badge)

> The APIs of higher level constructs in this module are experimental and under active development.
> They are subject to non-backward compatible changes or removal in any future version. These are
> not subject to the [Semantic Versioning](https://semver.org/) model and breaking changes will be
> announced in the release notes. This means that while you may use them, you may need to update
> your source code when upgrading to a newer version of this package.

---
<!--END STABILITY BANNER-->

Amazon SageMaker provides every developer and data scientist with the ability to build, train, and
deploy machine learning models quickly. Amazon SageMaker is a fully-managed service that covers the
entire machine learning workflow to label and prepare your data, choose an algorithm, train the
model, tune and optimize it for deployment, make predictions, and take action. Your models get to
production faster with much less effort and lower cost.

## Model

To create a machine learning model with Amazon Sagemaker, use the `Model` construct. This construct
includes properties that can be configured to define model components, including the model inference
code as a Docker image and an optional set of separate model data artifacts. See the [AWS
documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-marketplace-develop.html)
to learn more about SageMaker models.

### Single Container Model

In the event that a single container is sufficient for your inference use-case, you can define a
single-container model:

```python
import aws_cdk.aws_sagemaker_alpha as sagemaker
import path as path


image = sagemaker.ContainerImage.from_asset(path.join("path", "to", "Dockerfile", "directory"))
model_data = sagemaker.ModelData.from_asset(path.join("path", "to", "artifact", "file.tar.gz"))

model = sagemaker.Model(self, "PrimaryContainerModel",
    containers=[sagemaker.ContainerDefinition(
        image=image,
        model_data=model_data
    )
    ]
)
```

### Inference Pipeline Model

An inference pipeline is an Amazon SageMaker model that is composed of a linear sequence of multiple
containers that process requests for inferences on data. See the [AWS
documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-pipelines.html) to learn
more about SageMaker inference pipelines. To define an inference pipeline, you can provide
additional containers for your model:

```python
import aws_cdk.aws_sagemaker_alpha as sagemaker

# image1: sagemaker.ContainerImage
# model_data1: sagemaker.ModelData
# image2: sagemaker.ContainerImage
# model_data2: sagemaker.ModelData
# image3: sagemaker.ContainerImage
# model_data3: sagemaker.ModelData


model = sagemaker.Model(self, "InferencePipelineModel",
    containers=[sagemaker.ContainerDefinition(image=image1, model_data=model_data1), sagemaker.ContainerDefinition(image=image2, model_data=model_data2), sagemaker.ContainerDefinition(image=image3, model_data=model_data3)
    ]
)
```

### Container Images

Inference code can be stored in the Amazon EC2 Container Registry (Amazon ECR), which is specified
via `ContainerDefinition`'s `image` property which accepts a class that extends the `ContainerImage`
abstract base class.

#### Asset Image

Reference a local directory containing a Dockerfile:

```python
import aws_cdk.aws_sagemaker_alpha as sagemaker
import path as path


image = sagemaker.ContainerImage.from_asset(path.join("path", "to", "Dockerfile", "directory"))
```

#### ECR Image

Reference an image available within ECR:

```python
import aws_cdk.aws_ecr as ecr
import aws_cdk.aws_sagemaker_alpha as sagemaker


repository = ecr.Repository.from_repository_name(self, "Repository", "repo")
image = sagemaker.ContainerImage.from_ecr_repository(repository, "tag")
```

### Model Artifacts

If you choose to decouple your model artifacts from your inference code (as is natural given
different rates of change between inference code and model artifacts), the artifacts can be
specified via the `modelData` property which accepts a class that extends the `ModelData` abstract
base class. The default is to have no model artifacts associated with a model.

#### Asset Model Data

Reference local model data:

```python
import aws_cdk.aws_sagemaker_alpha as sagemaker
import path as path


model_data = sagemaker.ModelData.from_asset(path.join("path", "to", "artifact", "file.tar.gz"))
```

#### S3 Model Data

Reference an S3 bucket and object key as the artifacts for a model:

```python
import aws_cdk.aws_s3 as s3
import aws_cdk.aws_sagemaker_alpha as sagemaker


bucket = s3.Bucket(self, "MyBucket")
model_data = sagemaker.ModelData.from_bucket(bucket, "path/to/artifact/file.tar.gz")
```

## Model Hosting

Amazon SageMaker provides model hosting services for model deployment. Amazon SageMaker provides an
HTTPS endpoint where your machine learning model is available to provide inferences.

### Endpoint Configuration

By using the `EndpointConfig` construct, you can define a set of endpoint configuration which can be
used to provision one or more endpoints. In this configuration, you identify one or more models to
deploy and the resources that you want Amazon SageMaker to provision. You define one or more
production variants, each of which identifies a model. Each production variant also describes the
resources that you want Amazon SageMaker to provision. If you are hosting multiple models, you also
assign a variant weight to specify how much traffic you want to allocate to each model. For example,
suppose that you want to host two models, A and B, and you assign traffic weight 2 for model A and 1
for model B. Amazon SageMaker distributes two-thirds of the traffic to Model A, and one-third to
model B:

```python
import aws_cdk.aws_sagemaker_alpha as sagemaker

# model_a: sagemaker.Model
# model_b: sagemaker.Model


endpoint_config = sagemaker.EndpointConfig(self, "EndpointConfig",
    instance_production_variants=[sagemaker.InstanceProductionVariantProps(
        model=model_a,
        variant_name="modelA",
        initial_variant_weight=2
    ), sagemaker.InstanceProductionVariantProps(
        model=model_b,
        variant_name="variantB",
        initial_variant_weight=1
    )
    ]
)
```

### Endpoint

When you create an endpoint from an `EndpointConfig`, Amazon SageMaker launches the ML compute
instances and deploys the model or models as specified in the configuration. To get inferences from
the model, client applications send requests to the Amazon SageMaker Runtime HTTPS endpoint. For
more information about the API, see the
[InvokeEndpoint](https://docs.aws.amazon.com/sagemaker/latest/dg/API_runtime_InvokeEndpoint.html)
API. Defining an endpoint requires at minimum the associated endpoint configuration:

```python
import aws_cdk.aws_sagemaker_alpha as sagemaker

# endpoint_config: sagemaker.EndpointConfig


endpoint = sagemaker.Endpoint(self, "Endpoint", endpoint_config=endpoint_config)
```

### AutoScaling

To enable autoscaling on the production variant, use the `autoScaleInstanceCount` method:

```python
import aws_cdk.aws_sagemaker_alpha as sagemaker

# model: sagemaker.Model


variant_name = "my-variant"
endpoint_config = sagemaker.EndpointConfig(self, "EndpointConfig",
    instance_production_variants=[sagemaker.InstanceProductionVariantProps(
        model=model,
        variant_name=variant_name
    )
    ]
)

endpoint = sagemaker.Endpoint(self, "Endpoint", endpoint_config=endpoint_config)
production_variant = endpoint.find_instance_production_variant(variant_name)
instance_count = production_variant.auto_scale_instance_count(
    max_capacity=3
)
instance_count.scale_on_invocations("LimitRPS",
    max_requests_per_second=30
)
```

For load testing guidance on determining the maximum requests per second per instance, please see
this [documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/endpoint-scaling-loadtest.html).

### Metrics

To monitor CloudWatch metrics for a production variant, use one or more of the metric convenience
methods:

```python
import aws_cdk.aws_sagemaker_alpha as sagemaker

# endpoint_config: sagemaker.EndpointConfig


endpoint = sagemaker.Endpoint(self, "Endpoint", endpoint_config=endpoint_config)
production_variant = endpoint.find_instance_production_variant("my-variant")
production_variant.metric_model_latency().create_alarm(self, "ModelLatencyAlarm",
    threshold=100000,
    evaluation_periods=3
)
```
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from ._jsii import *

import aws_cdk
import aws_cdk.aws_applicationautoscaling
import aws_cdk.aws_cloudwatch
import aws_cdk.aws_ec2
import aws_cdk.aws_ecr
import aws_cdk.aws_ecr_assets
import aws_cdk.aws_iam
import aws_cdk.aws_kms
import aws_cdk.aws_s3
import aws_cdk.aws_s3_assets
import constructs


class AcceleratorType(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker-alpha.AcceleratorType",
):
    '''(experimental) Supported Elastic Inference (EI) instance types for SageMaker instance-based production variants.

    EI instances provide on-demand GPU computing for inference.

    :stability: experimental
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_sagemaker_alpha as sagemaker_alpha
        
        accelerator_type = sagemaker_alpha.AcceleratorType.EIA1_LARGE
    '''

    def __init__(self, accelerator_type: builtins.str) -> None:
        '''
        :param accelerator_type: -

        :stability: experimental
        '''
        if __debug__:
            def stub(accelerator_type: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument accelerator_type", value=accelerator_type, expected_type=type_hints["accelerator_type"])
        jsii.create(self.__class__, self, [accelerator_type])

    @jsii.member(jsii_name="of")
    @builtins.classmethod
    def of(cls, accelerator_type: builtins.str) -> "AcceleratorType":
        '''(experimental) Builds an AcceleratorType from a given string or token (such as a CfnParameter).

        :param accelerator_type: An accelerator type as string.

        :return: A strongly typed AcceleratorType

        :stability: experimental
        '''
        if __debug__:
            def stub(accelerator_type: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument accelerator_type", value=accelerator_type, expected_type=type_hints["accelerator_type"])
        return typing.cast("AcceleratorType", jsii.sinvoke(cls, "of", [accelerator_type]))

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        '''(experimental) Return the accelerator type as a string.

        :return: The accelerator type as a string

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.invoke(self, "toString", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EIA1_LARGE")
    def EIA1_LARGE(cls) -> "AcceleratorType":
        '''(experimental) ml.eia1.large.

        :stability: experimental
        '''
        return typing.cast("AcceleratorType", jsii.sget(cls, "EIA1_LARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EIA1_MEDIUM")
    def EIA1_MEDIUM(cls) -> "AcceleratorType":
        '''(experimental) ml.eia1.medium.

        :stability: experimental
        '''
        return typing.cast("AcceleratorType", jsii.sget(cls, "EIA1_MEDIUM"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EIA1_XLARGE")
    def EIA1_XLARGE(cls) -> "AcceleratorType":
        '''(experimental) ml.eia1.xlarge.

        :stability: experimental
        '''
        return typing.cast("AcceleratorType", jsii.sget(cls, "EIA1_XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EIA2_LARGE")
    def EIA2_LARGE(cls) -> "AcceleratorType":
        '''(experimental) ml.eia2.large.

        :stability: experimental
        '''
        return typing.cast("AcceleratorType", jsii.sget(cls, "EIA2_LARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EIA2_MEDIUM")
    def EIA2_MEDIUM(cls) -> "AcceleratorType":
        '''(experimental) ml.eia2.medium.

        :stability: experimental
        '''
        return typing.cast("AcceleratorType", jsii.sget(cls, "EIA2_MEDIUM"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EIA2_XLARGE")
    def EIA2_XLARGE(cls) -> "AcceleratorType":
        '''(experimental) ml.eia2.xlarge.

        :stability: experimental
        '''
        return typing.cast("AcceleratorType", jsii.sget(cls, "EIA2_XLARGE"))


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker-alpha.ContainerDefinition",
    jsii_struct_bases=[],
    name_mapping={
        "image": "image",
        "container_hostname": "containerHostname",
        "environment": "environment",
        "model_data": "modelData",
    },
)
class ContainerDefinition:
    def __init__(
        self,
        *,
        image: "ContainerImage",
        container_hostname: typing.Optional[builtins.str] = None,
        environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        model_data: typing.Optional["ModelData"] = None,
    ) -> None:
        '''(experimental) Describes the container, as part of model definition.

        :param image: (experimental) The image used to start a container.
        :param container_hostname: (experimental) Hostname of the container within an inference pipeline. For single container models, this field is ignored. When specifying a hostname for one ContainerDefinition in a pipeline, hostnames must be specified for all other ContainerDefinitions in that pipeline. Default: - Amazon SageMaker will automatically assign a unique name based on the position of this ContainerDefinition in an inference pipeline.
        :param environment: (experimental) A map of environment variables to pass into the container. Default: - none
        :param model_data: (experimental) S3 path to the model artifacts. Default: - none

        :stability: experimental
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_sagemaker_alpha as sagemaker_alpha
            
            # container_image: sagemaker_alpha.ContainerImage
            # model_data: sagemaker_alpha.ModelData
            
            container_definition = sagemaker_alpha.ContainerDefinition(
                image=container_image,
            
                # the properties below are optional
                container_hostname="containerHostname",
                environment={
                    "environment_key": "environment"
                },
                model_data=model_data
            )
        '''
        if __debug__:
            def stub(
                *,
                image: ContainerImage,
                container_hostname: typing.Optional[builtins.str] = None,
                environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                model_data: typing.Optional[ModelData] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument image", value=image, expected_type=type_hints["image"])
            check_type(argname="argument container_hostname", value=container_hostname, expected_type=type_hints["container_hostname"])
            check_type(argname="argument environment", value=environment, expected_type=type_hints["environment"])
            check_type(argname="argument model_data", value=model_data, expected_type=type_hints["model_data"])
        self._values: typing.Dict[str, typing.Any] = {
            "image": image,
        }
        if container_hostname is not None:
            self._values["container_hostname"] = container_hostname
        if environment is not None:
            self._values["environment"] = environment
        if model_data is not None:
            self._values["model_data"] = model_data

    @builtins.property
    def image(self) -> "ContainerImage":
        '''(experimental) The image used to start a container.

        :stability: experimental
        '''
        result = self._values.get("image")
        assert result is not None, "Required property 'image' is missing"
        return typing.cast("ContainerImage", result)

    @builtins.property
    def container_hostname(self) -> typing.Optional[builtins.str]:
        '''(experimental) Hostname of the container within an inference pipeline.

        For single container models, this field
        is ignored. When specifying a hostname for one ContainerDefinition in a pipeline, hostnames
        must be specified for all other ContainerDefinitions in that pipeline.

        :default:

        - Amazon SageMaker will automatically assign a unique name based on the position of
        this ContainerDefinition in an inference pipeline.

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition.html#cfn-sagemaker-model-containerdefinition-containerhostname
        :stability: experimental
        '''
        result = self._values.get("container_hostname")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def environment(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''(experimental) A map of environment variables to pass into the container.

        :default: - none

        :stability: experimental
        '''
        result = self._values.get("environment")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def model_data(self) -> typing.Optional["ModelData"]:
        '''(experimental) S3 path to the model artifacts.

        :default: - none

        :stability: experimental
        '''
        result = self._values.get("model_data")
        return typing.cast(typing.Optional["ModelData"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerImage(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="@aws-cdk/aws-sagemaker-alpha.ContainerImage",
):
    '''(experimental) Constructs for types of container images.

    :stability: experimental
    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_sagemaker_alpha as sagemaker
        import path as path
        
        
        image = sagemaker.ContainerImage.from_asset(path.join("path", "to", "Dockerfile", "directory"))
        model_data = sagemaker.ModelData.from_asset(path.join("path", "to", "artifact", "file.tar.gz"))
        
        model = sagemaker.Model(self, "PrimaryContainerModel",
            containers=[sagemaker.ContainerDefinition(
                image=image,
                model_data=model_data
            )
            ]
        )
    '''

    def __init__(self) -> None:
        '''
        :stability: experimental
        '''
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="fromAsset")
    @builtins.classmethod
    def from_asset(
        cls,
        directory: builtins.str,
        *,
        build_args: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        file: typing.Optional[builtins.str] = None,
        invalidation: typing.Optional[typing.Union[aws_cdk.aws_ecr_assets.DockerImageAssetInvalidationOptions, typing.Dict[str, typing.Any]]] = None,
        network_mode: typing.Optional[aws_cdk.aws_ecr_assets.NetworkMode] = None,
        platform: typing.Optional[aws_cdk.aws_ecr_assets.Platform] = None,
        target: typing.Optional[builtins.str] = None,
        extra_hash: typing.Optional[builtins.str] = None,
        exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
        follow_symlinks: typing.Optional[aws_cdk.SymlinkFollowMode] = None,
        ignore_mode: typing.Optional[aws_cdk.IgnoreMode] = None,
    ) -> "ContainerImage":
        '''(experimental) Reference an image that's constructed directly from sources on disk.

        :param directory: The directory where the Dockerfile is stored.
        :param build_args: Build args to pass to the ``docker build`` command. Since Docker build arguments are resolved before deployment, keys and values cannot refer to unresolved tokens (such as ``lambda.functionArn`` or ``queue.queueUrl``). Default: - no build args are passed
        :param file: Path to the Dockerfile (relative to the directory). Default: 'Dockerfile'
        :param invalidation: Options to control which parameters are used to invalidate the asset hash. Default: - hash all parameters
        :param network_mode: Networking mode for the RUN commands during build. Support docker API 1.25+. Default: - no networking mode specified (the default networking mode ``NetworkMode.DEFAULT`` will be used)
        :param platform: Platform to build for. *Requires Docker Buildx*. Default: - no platform specified (the current machine architecture will be used)
        :param target: Docker target to build to. Default: - no target
        :param extra_hash: Extra information to encode into the fingerprint (e.g. build instructions and other inputs). Default: - hash is only based on source content
        :param exclude: File paths matching the patterns will be excluded. See ``ignoreMode`` to set the matching behavior. Has no effect on Assets bundled using the ``bundling`` property. Default: - nothing is excluded
        :param follow_symlinks: A strategy for how to handle symlinks. Default: SymlinkFollowMode.NEVER
        :param ignore_mode: The ignore behavior to use for ``exclude`` patterns. Default: IgnoreMode.GLOB

        :stability: experimental
        '''
        if __debug__:
            def stub(
                directory: builtins.str,
                *,
                build_args: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                file: typing.Optional[builtins.str] = None,
                invalidation: typing.Optional[typing.Union[aws_cdk.aws_ecr_assets.DockerImageAssetInvalidationOptions, typing.Dict[str, typing.Any]]] = None,
                network_mode: typing.Optional[aws_cdk.aws_ecr_assets.NetworkMode] = None,
                platform: typing.Optional[aws_cdk.aws_ecr_assets.Platform] = None,
                target: typing.Optional[builtins.str] = None,
                extra_hash: typing.Optional[builtins.str] = None,
                exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
                follow_symlinks: typing.Optional[aws_cdk.SymlinkFollowMode] = None,
                ignore_mode: typing.Optional[aws_cdk.IgnoreMode] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument directory", value=directory, expected_type=type_hints["directory"])
        options = aws_cdk.aws_ecr_assets.DockerImageAssetOptions(
            build_args=build_args,
            file=file,
            invalidation=invalidation,
            network_mode=network_mode,
            platform=platform,
            target=target,
            extra_hash=extra_hash,
            exclude=exclude,
            follow_symlinks=follow_symlinks,
            ignore_mode=ignore_mode,
        )

        return typing.cast("ContainerImage", jsii.sinvoke(cls, "fromAsset", [directory, options]))

    @jsii.member(jsii_name="fromEcrRepository")
    @builtins.classmethod
    def from_ecr_repository(
        cls,
        repository: aws_cdk.aws_ecr.IRepository,
        tag: typing.Optional[builtins.str] = None,
    ) -> "ContainerImage":
        '''(experimental) Reference an image in an ECR repository.

        :param repository: -
        :param tag: -

        :stability: experimental
        '''
        if __debug__:
            def stub(
                repository: aws_cdk.aws_ecr.IRepository,
                tag: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument repository", value=repository, expected_type=type_hints["repository"])
            check_type(argname="argument tag", value=tag, expected_type=type_hints["tag"])
        return typing.cast("ContainerImage", jsii.sinvoke(cls, "fromEcrRepository", [repository, tag]))

    @jsii.member(jsii_name="bind")
    @abc.abstractmethod
    def bind(
        self,
        scope: constructs.Construct,
        model: "Model",
    ) -> "ContainerImageConfig":
        '''(experimental) Called when the image is used by a Model.

        :param scope: -
        :param model: -

        :stability: experimental
        '''
        ...


class _ContainerImageProxy(ContainerImage):
    @jsii.member(jsii_name="bind")
    def bind(
        self,
        scope: constructs.Construct,
        model: "Model",
    ) -> "ContainerImageConfig":
        '''(experimental) Called when the image is used by a Model.

        :param scope: -
        :param model: -

        :stability: experimental
        '''
        if __debug__:
            def stub(scope: constructs.Construct, model: Model) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument model", value=model, expected_type=type_hints["model"])
        return typing.cast("ContainerImageConfig", jsii.invoke(self, "bind", [scope, model]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, ContainerImage).__jsii_proxy_class__ = lambda : _ContainerImageProxy


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker-alpha.ContainerImageConfig",
    jsii_struct_bases=[],
    name_mapping={"image_name": "imageName"},
)
class ContainerImageConfig:
    def __init__(self, *, image_name: builtins.str) -> None:
        '''(experimental) The configuration for creating a container image.

        :param image_name: (experimental) The image name. Images in Amazon ECR repositories can be specified by either using the full registry/repository:tag or registry/repository@digest. For example, ``012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name>:latest`` or ``012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name>@sha256:94afd1f2e64d908bc90dbca0035a5b567EXAMPLE``.

        :stability: experimental
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_sagemaker_alpha as sagemaker_alpha
            
            container_image_config = sagemaker_alpha.ContainerImageConfig(
                image_name="imageName"
            )
        '''
        if __debug__:
            def stub(*, image_name: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument image_name", value=image_name, expected_type=type_hints["image_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "image_name": image_name,
        }

    @builtins.property
    def image_name(self) -> builtins.str:
        '''(experimental) The image name. Images in Amazon ECR repositories can be specified by either using the full registry/repository:tag or registry/repository@digest.

        For example, ``012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name>:latest`` or
        ``012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name>@sha256:94afd1f2e64d908bc90dbca0035a5b567EXAMPLE``.

        :stability: experimental
        '''
        result = self._values.get("image_name")
        assert result is not None, "Required property 'image_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerImageConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker-alpha.EndpointAttributes",
    jsii_struct_bases=[],
    name_mapping={"endpoint_arn": "endpointArn"},
)
class EndpointAttributes:
    def __init__(self, *, endpoint_arn: builtins.str) -> None:
        '''(experimental) Represents an Endpoint resource defined outside this stack.

        :param endpoint_arn: (experimental) The ARN of this endpoint.

        :stability: experimental
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_sagemaker_alpha as sagemaker_alpha
            
            endpoint_attributes = sagemaker_alpha.EndpointAttributes(
                endpoint_arn="endpointArn"
            )
        '''
        if __debug__:
            def stub(*, endpoint_arn: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument endpoint_arn", value=endpoint_arn, expected_type=type_hints["endpoint_arn"])
        self._values: typing.Dict[str, typing.Any] = {
            "endpoint_arn": endpoint_arn,
        }

    @builtins.property
    def endpoint_arn(self) -> builtins.str:
        '''(experimental) The ARN of this endpoint.

        :stability: experimental
        '''
        result = self._values.get("endpoint_arn")
        assert result is not None, "Required property 'endpoint_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EndpointAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker-alpha.EndpointConfigProps",
    jsii_struct_bases=[],
    name_mapping={
        "encryption_key": "encryptionKey",
        "endpoint_config_name": "endpointConfigName",
        "instance_production_variants": "instanceProductionVariants",
    },
)
class EndpointConfigProps:
    def __init__(
        self,
        *,
        encryption_key: typing.Optional[aws_cdk.aws_kms.IKey] = None,
        endpoint_config_name: typing.Optional[builtins.str] = None,
        instance_production_variants: typing.Optional[typing.Sequence[typing.Union["InstanceProductionVariantProps", typing.Dict[str, typing.Any]]]] = None,
    ) -> None:
        '''(experimental) Construction properties for a SageMaker EndpointConfig.

        :param encryption_key: (experimental) Optional KMS encryption key associated with this stream. Default: - none
        :param endpoint_config_name: (experimental) Name of the endpoint configuration. Default: - AWS CloudFormation generates a unique physical ID and uses that ID for the endpoint configuration's name.
        :param instance_production_variants: (experimental) A list of instance production variants. You can always add more variants later by calling {@link EndpointConfig#addInstanceProductionVariant}. Default: - none

        :stability: experimental
        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_sagemaker_alpha as sagemaker
            
            # model_a: sagemaker.Model
            # model_b: sagemaker.Model
            
            
            endpoint_config = sagemaker.EndpointConfig(self, "EndpointConfig",
                instance_production_variants=[sagemaker.InstanceProductionVariantProps(
                    model=model_a,
                    variant_name="modelA",
                    initial_variant_weight=2
                ), sagemaker.InstanceProductionVariantProps(
                    model=model_b,
                    variant_name="variantB",
                    initial_variant_weight=1
                )
                ]
            )
        '''
        if __debug__:
            def stub(
                *,
                encryption_key: typing.Optional[aws_cdk.aws_kms.IKey] = None,
                endpoint_config_name: typing.Optional[builtins.str] = None,
                instance_production_variants: typing.Optional[typing.Sequence[typing.Union[InstanceProductionVariantProps, typing.Dict[str, typing.Any]]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument encryption_key", value=encryption_key, expected_type=type_hints["encryption_key"])
            check_type(argname="argument endpoint_config_name", value=endpoint_config_name, expected_type=type_hints["endpoint_config_name"])
            check_type(argname="argument instance_production_variants", value=instance_production_variants, expected_type=type_hints["instance_production_variants"])
        self._values: typing.Dict[str, typing.Any] = {}
        if encryption_key is not None:
            self._values["encryption_key"] = encryption_key
        if endpoint_config_name is not None:
            self._values["endpoint_config_name"] = endpoint_config_name
        if instance_production_variants is not None:
            self._values["instance_production_variants"] = instance_production_variants

    @builtins.property
    def encryption_key(self) -> typing.Optional[aws_cdk.aws_kms.IKey]:
        '''(experimental) Optional KMS encryption key associated with this stream.

        :default: - none

        :stability: experimental
        '''
        result = self._values.get("encryption_key")
        return typing.cast(typing.Optional[aws_cdk.aws_kms.IKey], result)

    @builtins.property
    def endpoint_config_name(self) -> typing.Optional[builtins.str]:
        '''(experimental) Name of the endpoint configuration.

        :default:

        - AWS CloudFormation generates a unique physical ID and uses that ID for the endpoint
        configuration's name.

        :stability: experimental
        '''
        result = self._values.get("endpoint_config_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_production_variants(
        self,
    ) -> typing.Optional[typing.List["InstanceProductionVariantProps"]]:
        '''(experimental) A list of instance production variants.

        You can always add more variants later by calling
        {@link EndpointConfig#addInstanceProductionVariant}.

        :default: - none

        :stability: experimental
        '''
        result = self._values.get("instance_production_variants")
        return typing.cast(typing.Optional[typing.List["InstanceProductionVariantProps"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EndpointConfigProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker-alpha.EndpointProps",
    jsii_struct_bases=[],
    name_mapping={
        "endpoint_config": "endpointConfig",
        "endpoint_name": "endpointName",
    },
)
class EndpointProps:
    def __init__(
        self,
        *,
        endpoint_config: "IEndpointConfig",
        endpoint_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Construction properties for a SageMaker Endpoint.

        :param endpoint_config: (experimental) The endpoint configuration to use for this endpoint.
        :param endpoint_name: (experimental) Name of the endpoint. Default: - AWS CloudFormation generates a unique physical ID and uses that ID for the endpoint's name.

        :stability: experimental
        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_sagemaker_alpha as sagemaker
            
            # endpoint_config: sagemaker.EndpointConfig
            
            
            endpoint = sagemaker.Endpoint(self, "Endpoint", endpoint_config=endpoint_config)
            production_variant = endpoint.find_instance_production_variant("my-variant")
            production_variant.metric_model_latency().create_alarm(self, "ModelLatencyAlarm",
                threshold=100000,
                evaluation_periods=3
            )
        '''
        if __debug__:
            def stub(
                *,
                endpoint_config: IEndpointConfig,
                endpoint_name: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument endpoint_config", value=endpoint_config, expected_type=type_hints["endpoint_config"])
            check_type(argname="argument endpoint_name", value=endpoint_name, expected_type=type_hints["endpoint_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "endpoint_config": endpoint_config,
        }
        if endpoint_name is not None:
            self._values["endpoint_name"] = endpoint_name

    @builtins.property
    def endpoint_config(self) -> "IEndpointConfig":
        '''(experimental) The endpoint configuration to use for this endpoint.

        :stability: experimental
        '''
        result = self._values.get("endpoint_config")
        assert result is not None, "Required property 'endpoint_config' is missing"
        return typing.cast("IEndpointConfig", result)

    @builtins.property
    def endpoint_name(self) -> typing.Optional[builtins.str]:
        '''(experimental) Name of the endpoint.

        :default:

        - AWS CloudFormation generates a unique physical ID and uses that ID for the
        endpoint's name.

        :stability: experimental
        '''
        result = self._values.get("endpoint_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EndpointProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="@aws-cdk/aws-sagemaker-alpha.IEndpoint")
class IEndpoint(aws_cdk.IResource, typing_extensions.Protocol):
    '''(experimental) The interface for a SageMaker Endpoint resource.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="endpointArn")
    def endpoint_arn(self) -> builtins.str:
        '''(experimental) The ARN of the endpoint.

        :stability: experimental
        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="endpointName")
    def endpoint_name(self) -> builtins.str:
        '''(experimental) The name of the endpoint.

        :stability: experimental
        :attribute: true
        '''
        ...

    @jsii.member(jsii_name="grantInvoke")
    def grant_invoke(
        self,
        grantee: aws_cdk.aws_iam.IGrantable,
    ) -> aws_cdk.aws_iam.Grant:
        '''(experimental) Permits an IAM principal to invoke this endpoint.

        :param grantee: The principal to grant access to.

        :stability: experimental
        '''
        ...


class _IEndpointProxy(
    jsii.proxy_for(aws_cdk.IResource), # type: ignore[misc]
):
    '''(experimental) The interface for a SageMaker Endpoint resource.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/aws-sagemaker-alpha.IEndpoint"

    @builtins.property
    @jsii.member(jsii_name="endpointArn")
    def endpoint_arn(self) -> builtins.str:
        '''(experimental) The ARN of the endpoint.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "endpointArn"))

    @builtins.property
    @jsii.member(jsii_name="endpointName")
    def endpoint_name(self) -> builtins.str:
        '''(experimental) The name of the endpoint.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "endpointName"))

    @jsii.member(jsii_name="grantInvoke")
    def grant_invoke(
        self,
        grantee: aws_cdk.aws_iam.IGrantable,
    ) -> aws_cdk.aws_iam.Grant:
        '''(experimental) Permits an IAM principal to invoke this endpoint.

        :param grantee: The principal to grant access to.

        :stability: experimental
        '''
        if __debug__:
            def stub(grantee: aws_cdk.aws_iam.IGrantable) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(aws_cdk.aws_iam.Grant, jsii.invoke(self, "grantInvoke", [grantee]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEndpoint).__jsii_proxy_class__ = lambda : _IEndpointProxy


@jsii.interface(jsii_type="@aws-cdk/aws-sagemaker-alpha.IEndpointConfig")
class IEndpointConfig(aws_cdk.IResource, typing_extensions.Protocol):
    '''(experimental) The interface for a SageMaker EndpointConfig resource.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="endpointConfigArn")
    def endpoint_config_arn(self) -> builtins.str:
        '''(experimental) The ARN of the endpoint configuration.

        :stability: experimental
        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="endpointConfigName")
    def endpoint_config_name(self) -> builtins.str:
        '''(experimental) The name of the endpoint configuration.

        :stability: experimental
        :attribute: true
        '''
        ...


class _IEndpointConfigProxy(
    jsii.proxy_for(aws_cdk.IResource), # type: ignore[misc]
):
    '''(experimental) The interface for a SageMaker EndpointConfig resource.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/aws-sagemaker-alpha.IEndpointConfig"

    @builtins.property
    @jsii.member(jsii_name="endpointConfigArn")
    def endpoint_config_arn(self) -> builtins.str:
        '''(experimental) The ARN of the endpoint configuration.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "endpointConfigArn"))

    @builtins.property
    @jsii.member(jsii_name="endpointConfigName")
    def endpoint_config_name(self) -> builtins.str:
        '''(experimental) The name of the endpoint configuration.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "endpointConfigName"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEndpointConfig).__jsii_proxy_class__ = lambda : _IEndpointConfigProxy


@jsii.interface(
    jsii_type="@aws-cdk/aws-sagemaker-alpha.IEndpointInstanceProductionVariant"
)
class IEndpointInstanceProductionVariant(typing_extensions.Protocol):
    '''(experimental) Represents an instance production variant that has been associated with an endpoint.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="variantName")
    def variant_name(self) -> builtins.str:
        '''(experimental) The name of the production variant.

        :stability: experimental
        '''
        ...

    @jsii.member(jsii_name="autoScaleInstanceCount")
    def auto_scale_instance_count(
        self,
        *,
        max_capacity: jsii.Number,
        min_capacity: typing.Optional[jsii.Number] = None,
    ) -> "ScalableInstanceCount":
        '''(experimental) Enable autoscaling for SageMaker Endpoint production variant.

        :param max_capacity: Maximum capacity to scale to.
        :param min_capacity: Minimum capacity to scale to. Default: 1

        :stability: experimental
        '''
        ...

    @jsii.member(jsii_name="metric")
    def metric(
        self,
        namespace: builtins.str,
        metric_name: builtins.str,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[aws_cdk.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
    ) -> aws_cdk.aws_cloudwatch.Metric:
        '''(experimental) Return the given named metric for Endpoint.

        :param namespace: -
        :param metric_name: -
        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Use the factory functions on the ``Stats`` object to construct valid input strings. Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: - sum over 5 minutes

        :stability: experimental
        '''
        ...

    @jsii.member(jsii_name="metricCpuUtilization")
    def metric_cpu_utilization(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[aws_cdk.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
    ) -> aws_cdk.aws_cloudwatch.Metric:
        '''(experimental) Metric for CPU utilization.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Use the factory functions on the ``Stats`` object to construct valid input strings. Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: - average over 5 minutes

        :stability: experimental
        '''
        ...

    @jsii.member(jsii_name="metricDiskUtilization")
    def metric_disk_utilization(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[aws_cdk.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
    ) -> aws_cdk.aws_cloudwatch.Metric:
        '''(experimental) Metric for disk utilization.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Use the factory functions on the ``Stats`` object to construct valid input strings. Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: - average over 5 minutes

        :stability: experimental
        '''
        ...

    @jsii.member(jsii_name="metricGpuMemoryUtilization")
    def metric_gpu_memory_utilization(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[aws_cdk.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
    ) -> aws_cdk.aws_cloudwatch.Metric:
        '''(experimental) Metric for GPU memory utilization.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Use the factory functions on the ``Stats`` object to construct valid input strings. Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: - average over 5 minutes

        :stability: experimental
        '''
        ...

    @jsii.member(jsii_name="metricGpuUtilization")
    def metric_gpu_utilization(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[aws_cdk.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
    ) -> aws_cdk.aws_cloudwatch.Metric:
        '''(experimental) Metric for GPU utilization.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Use the factory functions on the ``Stats`` object to construct valid input strings. Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: - average over 5 minutes

        :stability: experimental
        '''
        ...

    @jsii.member(jsii_name="metricInvocationResponseCode")
    def metric_invocation_response_code(
        self,
        response_code: "InvocationHttpResponseCode",
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[aws_cdk.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
    ) -> aws_cdk.aws_cloudwatch.Metric:
        '''(experimental) Metric for the number of invocations by HTTP response code.

        :param response_code: -
        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Use the factory functions on the ``Stats`` object to construct valid input strings. Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: - sum over 5 minutes

        :stability: experimental
        '''
        ...

    @jsii.member(jsii_name="metricInvocations")
    def metric_invocations(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[aws_cdk.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
    ) -> aws_cdk.aws_cloudwatch.Metric:
        '''(experimental) Metric for the number of invocations.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Use the factory functions on the ``Stats`` object to construct valid input strings. Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: - sum over 5 minutes

        :stability: experimental
        '''
        ...

    @jsii.member(jsii_name="metricInvocationsPerInstance")
    def metric_invocations_per_instance(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[aws_cdk.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
    ) -> aws_cdk.aws_cloudwatch.Metric:
        '''(experimental) Metric for the number of invocations per instance.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Use the factory functions on the ``Stats`` object to construct valid input strings. Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: - sum over 5 minutes

        :stability: experimental
        '''
        ...

    @jsii.member(jsii_name="metricMemoryUtilization")
    def metric_memory_utilization(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[aws_cdk.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
    ) -> aws_cdk.aws_cloudwatch.Metric:
        '''(experimental) Metric for memory utilization.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Use the factory functions on the ``Stats`` object to construct valid input strings. Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: - average over 5 minutes

        :stability: experimental
        '''
        ...

    @jsii.member(jsii_name="metricModelLatency")
    def metric_model_latency(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[aws_cdk.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
    ) -> aws_cdk.aws_cloudwatch.Metric:
        '''(experimental) Metric for model latency.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Use the factory functions on the ``Stats`` object to construct valid input strings. Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: - average over 5 minutes

        :stability: experimental
        '''
        ...

    @jsii.member(jsii_name="metricOverheadLatency")
    def metric_overhead_latency(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[aws_cdk.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
    ) -> aws_cdk.aws_cloudwatch.Metric:
        '''(experimental) Metric for overhead latency.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Use the factory functions on the ``Stats`` object to construct valid input strings. Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: - average over 5 minutes

        :stability: experimental
        '''
        ...


class _IEndpointInstanceProductionVariantProxy:
    '''(experimental) Represents an instance production variant that has been associated with an endpoint.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/aws-sagemaker-alpha.IEndpointInstanceProductionVariant"

    @builtins.property
    @jsii.member(jsii_name="variantName")
    def variant_name(self) -> builtins.str:
        '''(experimental) The name of the production variant.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "variantName"))

    @jsii.member(jsii_name="autoScaleInstanceCount")
    def auto_scale_instance_count(
        self,
        *,
        max_capacity: jsii.Number,
        min_capacity: typing.Optional[jsii.Number] = None,
    ) -> "ScalableInstanceCount":
        '''(experimental) Enable autoscaling for SageMaker Endpoint production variant.

        :param max_capacity: Maximum capacity to scale to.
        :param min_capacity: Minimum capacity to scale to. Default: 1

        :stability: experimental
        '''
        scaling_props = aws_cdk.aws_applicationautoscaling.EnableScalingProps(
            max_capacity=max_capacity, min_capacity=min_capacity
        )

        return typing.cast("ScalableInstanceCount", jsii.invoke(self, "autoScaleInstanceCount", [scaling_props]))

    @jsii.member(jsii_name="metric")
    def metric(
        self,
        namespace: builtins.str,
        metric_name: builtins.str,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[aws_cdk.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
    ) -> aws_cdk.aws_cloudwatch.Metric:
        '''(experimental) Return the given named metric for Endpoint.

        :param namespace: -
        :param metric_name: -
        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Use the factory functions on the ``Stats`` object to construct valid input strings. Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: - sum over 5 minutes

        :stability: experimental
        '''
        if __debug__:
            def stub(
                namespace: builtins.str,
                metric_name: builtins.str,
                *,
                account: typing.Optional[builtins.str] = None,
                color: typing.Optional[builtins.str] = None,
                dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                label: typing.Optional[builtins.str] = None,
                period: typing.Optional[aws_cdk.Duration] = None,
                region: typing.Optional[builtins.str] = None,
                statistic: typing.Optional[builtins.str] = None,
                unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
        props = aws_cdk.aws_cloudwatch.MetricOptions(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(aws_cdk.aws_cloudwatch.Metric, jsii.invoke(self, "metric", [namespace, metric_name, props]))

    @jsii.member(jsii_name="metricCpuUtilization")
    def metric_cpu_utilization(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[aws_cdk.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
    ) -> aws_cdk.aws_cloudwatch.Metric:
        '''(experimental) Metric for CPU utilization.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Use the factory functions on the ``Stats`` object to construct valid input strings. Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: - average over 5 minutes

        :stability: experimental
        '''
        props = aws_cdk.aws_cloudwatch.MetricOptions(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(aws_cdk.aws_cloudwatch.Metric, jsii.invoke(self, "metricCpuUtilization", [props]))

    @jsii.member(jsii_name="metricDiskUtilization")
    def metric_disk_utilization(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[aws_cdk.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
    ) -> aws_cdk.aws_cloudwatch.Metric:
        '''(experimental) Metric for disk utilization.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Use the factory functions on the ``Stats`` object to construct valid input strings. Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: - average over 5 minutes

        :stability: experimental
        '''
        props = aws_cdk.aws_cloudwatch.MetricOptions(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(aws_cdk.aws_cloudwatch.Metric, jsii.invoke(self, "metricDiskUtilization", [props]))

    @jsii.member(jsii_name="metricGpuMemoryUtilization")
    def metric_gpu_memory_utilization(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[aws_cdk.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
    ) -> aws_cdk.aws_cloudwatch.Metric:
        '''(experimental) Metric for GPU memory utilization.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Use the factory functions on the ``Stats`` object to construct valid input strings. Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: - average over 5 minutes

        :stability: experimental
        '''
        props = aws_cdk.aws_cloudwatch.MetricOptions(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(aws_cdk.aws_cloudwatch.Metric, jsii.invoke(self, "metricGpuMemoryUtilization", [props]))

    @jsii.member(jsii_name="metricGpuUtilization")
    def metric_gpu_utilization(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[aws_cdk.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
    ) -> aws_cdk.aws_cloudwatch.Metric:
        '''(experimental) Metric for GPU utilization.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Use the factory functions on the ``Stats`` object to construct valid input strings. Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: - average over 5 minutes

        :stability: experimental
        '''
        props = aws_cdk.aws_cloudwatch.MetricOptions(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(aws_cdk.aws_cloudwatch.Metric, jsii.invoke(self, "metricGpuUtilization", [props]))

    @jsii.member(jsii_name="metricInvocationResponseCode")
    def metric_invocation_response_code(
        self,
        response_code: "InvocationHttpResponseCode",
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[aws_cdk.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
    ) -> aws_cdk.aws_cloudwatch.Metric:
        '''(experimental) Metric for the number of invocations by HTTP response code.

        :param response_code: -
        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Use the factory functions on the ``Stats`` object to construct valid input strings. Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: - sum over 5 minutes

        :stability: experimental
        '''
        if __debug__:
            def stub(
                response_code: InvocationHttpResponseCode,
                *,
                account: typing.Optional[builtins.str] = None,
                color: typing.Optional[builtins.str] = None,
                dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                label: typing.Optional[builtins.str] = None,
                period: typing.Optional[aws_cdk.Duration] = None,
                region: typing.Optional[builtins.str] = None,
                statistic: typing.Optional[builtins.str] = None,
                unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument response_code", value=response_code, expected_type=type_hints["response_code"])
        props = aws_cdk.aws_cloudwatch.MetricOptions(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(aws_cdk.aws_cloudwatch.Metric, jsii.invoke(self, "metricInvocationResponseCode", [response_code, props]))

    @jsii.member(jsii_name="metricInvocations")
    def metric_invocations(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[aws_cdk.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
    ) -> aws_cdk.aws_cloudwatch.Metric:
        '''(experimental) Metric for the number of invocations.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Use the factory functions on the ``Stats`` object to construct valid input strings. Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: - sum over 5 minutes

        :stability: experimental
        '''
        props = aws_cdk.aws_cloudwatch.MetricOptions(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(aws_cdk.aws_cloudwatch.Metric, jsii.invoke(self, "metricInvocations", [props]))

    @jsii.member(jsii_name="metricInvocationsPerInstance")
    def metric_invocations_per_instance(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[aws_cdk.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
    ) -> aws_cdk.aws_cloudwatch.Metric:
        '''(experimental) Metric for the number of invocations per instance.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Use the factory functions on the ``Stats`` object to construct valid input strings. Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: - sum over 5 minutes

        :stability: experimental
        '''
        props = aws_cdk.aws_cloudwatch.MetricOptions(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(aws_cdk.aws_cloudwatch.Metric, jsii.invoke(self, "metricInvocationsPerInstance", [props]))

    @jsii.member(jsii_name="metricMemoryUtilization")
    def metric_memory_utilization(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[aws_cdk.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
    ) -> aws_cdk.aws_cloudwatch.Metric:
        '''(experimental) Metric for memory utilization.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Use the factory functions on the ``Stats`` object to construct valid input strings. Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: - average over 5 minutes

        :stability: experimental
        '''
        props = aws_cdk.aws_cloudwatch.MetricOptions(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(aws_cdk.aws_cloudwatch.Metric, jsii.invoke(self, "metricMemoryUtilization", [props]))

    @jsii.member(jsii_name="metricModelLatency")
    def metric_model_latency(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[aws_cdk.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
    ) -> aws_cdk.aws_cloudwatch.Metric:
        '''(experimental) Metric for model latency.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Use the factory functions on the ``Stats`` object to construct valid input strings. Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: - average over 5 minutes

        :stability: experimental
        '''
        props = aws_cdk.aws_cloudwatch.MetricOptions(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(aws_cdk.aws_cloudwatch.Metric, jsii.invoke(self, "metricModelLatency", [props]))

    @jsii.member(jsii_name="metricOverheadLatency")
    def metric_overhead_latency(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[aws_cdk.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
    ) -> aws_cdk.aws_cloudwatch.Metric:
        '''(experimental) Metric for overhead latency.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Use the factory functions on the ``Stats`` object to construct valid input strings. Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: - average over 5 minutes

        :stability: experimental
        '''
        props = aws_cdk.aws_cloudwatch.MetricOptions(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(aws_cdk.aws_cloudwatch.Metric, jsii.invoke(self, "metricOverheadLatency", [props]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEndpointInstanceProductionVariant).__jsii_proxy_class__ = lambda : _IEndpointInstanceProductionVariantProxy


@jsii.interface(jsii_type="@aws-cdk/aws-sagemaker-alpha.IModel")
class IModel(
    aws_cdk.IResource,
    aws_cdk.aws_iam.IGrantable,
    aws_cdk.aws_ec2.IConnectable,
    typing_extensions.Protocol,
):
    '''(experimental) Interface that defines a Model resource.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="modelArn")
    def model_arn(self) -> builtins.str:
        '''(experimental) Returns the ARN of this model.

        :stability: experimental
        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="modelName")
    def model_name(self) -> builtins.str:
        '''(experimental) Returns the name of this model.

        :stability: experimental
        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> typing.Optional[aws_cdk.aws_iam.IRole]:
        '''(experimental) The IAM role associated with this Model.

        :stability: experimental
        '''
        ...

    @jsii.member(jsii_name="addToRolePolicy")
    def add_to_role_policy(self, statement: aws_cdk.aws_iam.PolicyStatement) -> None:
        '''(experimental) Adds a statement to the IAM role assumed by the instance.

        :param statement: -

        :stability: experimental
        '''
        ...


class _IModelProxy(
    jsii.proxy_for(aws_cdk.IResource), # type: ignore[misc]
    jsii.proxy_for(aws_cdk.aws_iam.IGrantable), # type: ignore[misc]
    jsii.proxy_for(aws_cdk.aws_ec2.IConnectable), # type: ignore[misc]
):
    '''(experimental) Interface that defines a Model resource.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/aws-sagemaker-alpha.IModel"

    @builtins.property
    @jsii.member(jsii_name="modelArn")
    def model_arn(self) -> builtins.str:
        '''(experimental) Returns the ARN of this model.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "modelArn"))

    @builtins.property
    @jsii.member(jsii_name="modelName")
    def model_name(self) -> builtins.str:
        '''(experimental) Returns the name of this model.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "modelName"))

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> typing.Optional[aws_cdk.aws_iam.IRole]:
        '''(experimental) The IAM role associated with this Model.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[aws_cdk.aws_iam.IRole], jsii.get(self, "role"))

    @jsii.member(jsii_name="addToRolePolicy")
    def add_to_role_policy(self, statement: aws_cdk.aws_iam.PolicyStatement) -> None:
        '''(experimental) Adds a statement to the IAM role assumed by the instance.

        :param statement: -

        :stability: experimental
        '''
        if __debug__:
            def stub(statement: aws_cdk.aws_iam.PolicyStatement) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument statement", value=statement, expected_type=type_hints["statement"])
        return typing.cast(None, jsii.invoke(self, "addToRolePolicy", [statement]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IModel).__jsii_proxy_class__ = lambda : _IModelProxy


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker-alpha.InstanceProductionVariantProps",
    jsii_struct_bases=[],
    name_mapping={
        "model": "model",
        "variant_name": "variantName",
        "accelerator_type": "acceleratorType",
        "initial_instance_count": "initialInstanceCount",
        "initial_variant_weight": "initialVariantWeight",
        "instance_type": "instanceType",
    },
)
class InstanceProductionVariantProps:
    def __init__(
        self,
        *,
        model: IModel,
        variant_name: builtins.str,
        accelerator_type: typing.Optional[AcceleratorType] = None,
        initial_instance_count: typing.Optional[jsii.Number] = None,
        initial_variant_weight: typing.Optional[jsii.Number] = None,
        instance_type: typing.Optional["InstanceType"] = None,
    ) -> None:
        '''(experimental) Construction properties for an instance production variant.

        :param model: (experimental) The model to host.
        :param variant_name: (experimental) Name of the production variant.
        :param accelerator_type: (experimental) The size of the Elastic Inference (EI) instance to use for the production variant. EI instances provide on-demand GPU computing for inference. Default: - none
        :param initial_instance_count: (experimental) Number of instances to launch initially. Default: 1
        :param initial_variant_weight: (experimental) Determines initial traffic distribution among all of the models that you specify in the endpoint configuration. The traffic to a production variant is determined by the ratio of the variant weight to the sum of all variant weight values across all production variants. Default: 1.0
        :param instance_type: (experimental) Instance type of the production variant. Default: InstanceType.T2_MEDIUM

        :stability: experimental
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_sagemaker_alpha as sagemaker_alpha
            
            # accelerator_type: sagemaker_alpha.AcceleratorType
            # instance_type: sagemaker_alpha.InstanceType
            # model: sagemaker_alpha.Model
            
            instance_production_variant_props = sagemaker_alpha.InstanceProductionVariantProps(
                model=model,
                variant_name="variantName",
            
                # the properties below are optional
                accelerator_type=accelerator_type,
                initial_instance_count=123,
                initial_variant_weight=123,
                instance_type=instance_type
            )
        '''
        if __debug__:
            def stub(
                *,
                model: IModel,
                variant_name: builtins.str,
                accelerator_type: typing.Optional[AcceleratorType] = None,
                initial_instance_count: typing.Optional[jsii.Number] = None,
                initial_variant_weight: typing.Optional[jsii.Number] = None,
                instance_type: typing.Optional[InstanceType] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument model", value=model, expected_type=type_hints["model"])
            check_type(argname="argument variant_name", value=variant_name, expected_type=type_hints["variant_name"])
            check_type(argname="argument accelerator_type", value=accelerator_type, expected_type=type_hints["accelerator_type"])
            check_type(argname="argument initial_instance_count", value=initial_instance_count, expected_type=type_hints["initial_instance_count"])
            check_type(argname="argument initial_variant_weight", value=initial_variant_weight, expected_type=type_hints["initial_variant_weight"])
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
        self._values: typing.Dict[str, typing.Any] = {
            "model": model,
            "variant_name": variant_name,
        }
        if accelerator_type is not None:
            self._values["accelerator_type"] = accelerator_type
        if initial_instance_count is not None:
            self._values["initial_instance_count"] = initial_instance_count
        if initial_variant_weight is not None:
            self._values["initial_variant_weight"] = initial_variant_weight
        if instance_type is not None:
            self._values["instance_type"] = instance_type

    @builtins.property
    def model(self) -> IModel:
        '''(experimental) The model to host.

        :stability: experimental
        '''
        result = self._values.get("model")
        assert result is not None, "Required property 'model' is missing"
        return typing.cast(IModel, result)

    @builtins.property
    def variant_name(self) -> builtins.str:
        '''(experimental) Name of the production variant.

        :stability: experimental
        '''
        result = self._values.get("variant_name")
        assert result is not None, "Required property 'variant_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def accelerator_type(self) -> typing.Optional[AcceleratorType]:
        '''(experimental) The size of the Elastic Inference (EI) instance to use for the production variant.

        EI instances
        provide on-demand GPU computing for inference.

        :default: - none

        :stability: experimental
        '''
        result = self._values.get("accelerator_type")
        return typing.cast(typing.Optional[AcceleratorType], result)

    @builtins.property
    def initial_instance_count(self) -> typing.Optional[jsii.Number]:
        '''(experimental) Number of instances to launch initially.

        :default: 1

        :stability: experimental
        '''
        result = self._values.get("initial_instance_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def initial_variant_weight(self) -> typing.Optional[jsii.Number]:
        '''(experimental) Determines initial traffic distribution among all of the models that you specify in the endpoint configuration.

        The traffic to a production variant is determined by the ratio of the
        variant weight to the sum of all variant weight values across all production variants.

        :default: 1.0

        :stability: experimental
        '''
        result = self._values.get("initial_variant_weight")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def instance_type(self) -> typing.Optional["InstanceType"]:
        '''(experimental) Instance type of the production variant.

        :default: InstanceType.T2_MEDIUM

        :stability: experimental
        '''
        result = self._values.get("instance_type")
        return typing.cast(typing.Optional["InstanceType"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InstanceProductionVariantProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class InstanceType(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker-alpha.InstanceType",
):
    '''(experimental) Supported instance types for SageMaker instance-based production variants.

    :stability: experimental
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_sagemaker_alpha as sagemaker_alpha
        
        instance_type = sagemaker_alpha.InstanceType.C4_2XLARGE
    '''

    def __init__(self, instance_type: builtins.str) -> None:
        '''
        :param instance_type: -

        :stability: experimental
        '''
        if __debug__:
            def stub(instance_type: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
        jsii.create(self.__class__, self, [instance_type])

    @jsii.member(jsii_name="of")
    @builtins.classmethod
    def of(cls, instance_type: builtins.str) -> "InstanceType":
        '''(experimental) Builds an InstanceType from a given string or token (such as a CfnParameter).

        :param instance_type: An instance type as string.

        :return: A strongly typed InstanceType

        :stability: experimental
        '''
        if __debug__:
            def stub(instance_type: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
        return typing.cast("InstanceType", jsii.sinvoke(cls, "of", [instance_type]))

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        '''(experimental) Return the instance type as a string.

        :return: The instance type as a string

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.invoke(self, "toString", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="C4_2XLARGE")
    def C4_2_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.c4.2xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "C4_2XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="C4_4XLARGE")
    def C4_4_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.c4.4xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "C4_4XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="C4_8XLARGE")
    def C4_8_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.c4.8xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "C4_8XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="C4_LARGE")
    def C4_LARGE(cls) -> "InstanceType":
        '''(experimental) ml.c4.large.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "C4_LARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="C4_XLARGE")
    def C4_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.c4.xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "C4_XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="C5_18XLARGE")
    def C5_18_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.c5.18xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "C5_18XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="C5_2XLARGE")
    def C5_2_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.c5.2xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "C5_2XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="C5_4XLARGE")
    def C5_4_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.c5.4xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "C5_4XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="C5_9XLARGE")
    def C5_9_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.c5.9xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "C5_9XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="C5_LARGE")
    def C5_LARGE(cls) -> "InstanceType":
        '''(experimental) ml.c5.large.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "C5_LARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="C5_XLARGE")
    def C5_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.c5.xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "C5_XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="C5D_18XLARGE")
    def C5_D_18_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.c5d.18xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "C5D_18XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="C5D_2XLARGE")
    def C5_D_2_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.c5d.2xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "C5D_2XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="C5D_4XLARGE")
    def C5_D_4_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.c5d.4xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "C5D_4XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="C5D_9XLARGE")
    def C5_D_9_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.c5d.9xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "C5D_9XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="C5D_LARGE")
    def C5_D_LARGE(cls) -> "InstanceType":
        '''(experimental) ml.c5d.large.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "C5D_LARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="C5D_XLARGE")
    def C5_D_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.c5d.xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "C5D_XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="C6I_12XLARGE")
    def C6_I_12_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.c6i.12xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "C6I_12XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="C6I_16XLARGE")
    def C6_I_16_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.c6i.16xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "C6I_16XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="C6I_24XLARGE")
    def C6_I_24_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.c6i.24xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "C6I_24XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="C6I_2XLARGE")
    def C6_I_2_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.c6i.2xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "C6I_2XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="C6I_32XLARGE")
    def C6_I_32_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.c6i.32xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "C6I_32XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="C6I_4XLARGE")
    def C6_I_4_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.c6i.4xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "C6I_4XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="C6I_8XLARGE")
    def C6_I_8_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.c6i.8xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "C6I_8XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="C6I_LARGE")
    def C6_I_LARGE(cls) -> "InstanceType":
        '''(experimental) ml.c6i.large.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "C6I_LARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="C6I_XLARGE")
    def C6_I_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.c6i.xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "C6I_XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="G4DN_12XLARGE")
    def G4_DN_12_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.g4dn.12xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "G4DN_12XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="G4DN_16XLARGE")
    def G4_DN_16_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.g4dn.16xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "G4DN_16XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="G4DN_2XLARGE")
    def G4_DN_2_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.g4dn.2xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "G4DN_2XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="G4DN_4XLARGE")
    def G4_DN_4_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.g4dn.4xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "G4DN_4XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="G4DN_8XLARGE")
    def G4_DN_8_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.g4dn.8xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "G4DN_8XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="G4DN_XLARGE")
    def G4_DN_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.g4dn.xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "G4DN_XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="G5_12XLARGE")
    def G5_12_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.g5.12xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "G5_12XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="G5_16XLARGE")
    def G5_16_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.g5.16xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "G5_16XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="G5_24XLARGE")
    def G5_24_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.g5.24xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "G5_24XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="G5_2XLARGE")
    def G5_2_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.g5.2xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "G5_2XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="G5_48XLARGE")
    def G5_48_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.g5.48xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "G5_48XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="G5_4XLARGE")
    def G5_4_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.g5.4xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "G5_4XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="G5_8XLARGE")
    def G5_8_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.g5.8xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "G5_8XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="G5_XLARGE")
    def G5_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.g5.xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "G5_XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="INF1_24XLARGE")
    def INF1_24_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.inf1.24xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "INF1_24XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="INF1_2XLARGE")
    def INF1_2_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.inf1.2xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "INF1_2XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="INF1_6XLARGE")
    def INF1_6_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.inf1.6xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "INF1_6XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="INF1_XLARGE")
    def INF1_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.inf1.xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "INF1_XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="M4_10XLARGE")
    def M4_10_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.m4.10xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "M4_10XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="M4_16XLARGE")
    def M4_16_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.m4.16xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "M4_16XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="M4_2XLARGE")
    def M4_2_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.m4.2xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "M4_2XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="M4_4XLARGE")
    def M4_4_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.m4.4xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "M4_4XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="M4_XLARGE")
    def M4_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.m4.xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "M4_XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="M5_12XLARGE")
    def M5_12_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.m5.12xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "M5_12XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="M5_24XLARGE")
    def M5_24_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.m5.24xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "M5_24XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="M5_2XLARGE")
    def M5_2_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.m5.2xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "M5_2XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="M5_4XLARGE")
    def M5_4_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.m5.4xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "M5_4XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="M5_LARGE")
    def M5_LARGE(cls) -> "InstanceType":
        '''(experimental) ml.m5.large.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "M5_LARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="M5_XLARGE")
    def M5_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.m5.xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "M5_XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="M5D_12XLARGE")
    def M5_D_12_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.m5d.12xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "M5D_12XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="M5D_24XLARGE")
    def M5_D_24_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.m5d.24xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "M5D_24XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="M5D_2XLARGE")
    def M5_D_2_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.m5d.2xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "M5D_2XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="M5D_4XLARGE")
    def M5_D_4_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.m5d.4xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "M5D_4XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="M5D_LARGE")
    def M5_D_LARGE(cls) -> "InstanceType":
        '''(experimental) ml.m5d.large.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "M5D_LARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="M5D_XLARGE")
    def M5_D_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.m5d.xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "M5D_XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="P2_16XLARGE")
    def P2_16_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.p2.16xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "P2_16XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="P2_8XLARGE")
    def P2_8_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.p2.8xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "P2_8XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="P2_XLARGE")
    def P2_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.p2.xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "P2_XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="P3_16XLARGE")
    def P3_16_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.p3.16xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "P3_16XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="P3_2XLARGE")
    def P3_2_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.p3.2xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "P3_2XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="P3_8XLARGE")
    def P3_8_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.p3.8xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "P3_8XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="P4D_24XLARGE")
    def P4_D_24_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.p4d.24xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "P4D_24XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="R5_12XLARGE")
    def R5_12_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.r5.12xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "R5_12XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="R5_24XLARGE")
    def R5_24_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.r5.24xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "R5_24XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="R5_2XLARGE")
    def R5_2_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.r5.2xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "R5_2XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="R5_4XLARGE")
    def R5_4_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.r5.4xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "R5_4XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="R5_LARGE")
    def R5_LARGE(cls) -> "InstanceType":
        '''(experimental) ml.r5.large.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "R5_LARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="R5_XLARGE")
    def R5_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.r5.xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "R5_XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="R5D_12XLARGE")
    def R5_D_12_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.r5d.12xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "R5D_12XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="R5D_24XLARGE")
    def R5_D_24_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.r5d.24xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "R5D_24XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="R5D_2XLARGE")
    def R5_D_2_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.r5d.2xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "R5D_2XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="R5D_4XLARGE")
    def R5_D_4_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.r5d.4xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "R5D_4XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="R5D_LARGE")
    def R5_D_LARGE(cls) -> "InstanceType":
        '''(experimental) ml.r5d.large.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "R5D_LARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="R5D_XLARGE")
    def R5_D_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.r5d.xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "R5D_XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="T2_2XLARGE")
    def T2_2_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.t2.2xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "T2_2XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="T2_LARGE")
    def T2_LARGE(cls) -> "InstanceType":
        '''(experimental) ml.t2.large.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "T2_LARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="T2_MEDIUM")
    def T2_MEDIUM(cls) -> "InstanceType":
        '''(experimental) ml.t2.medium.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "T2_MEDIUM"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="T2_XLARGE")
    def T2_XLARGE(cls) -> "InstanceType":
        '''(experimental) ml.t2.xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "T2_XLARGE"))


@jsii.enum(jsii_type="@aws-cdk/aws-sagemaker-alpha.InvocationHttpResponseCode")
class InvocationHttpResponseCode(enum.Enum):
    '''(experimental) HTTP response codes for Endpoint invocations.

    :stability: experimental
    '''

    INVOCATION_4XX_ERRORS = "INVOCATION_4XX_ERRORS"
    '''(experimental) 4xx response codes from Endpoint invocations.

    :stability: experimental
    '''
    INVOCATION_5XX_ERRORS = "INVOCATION_5XX_ERRORS"
    '''(experimental) 5xx response codes from Endpoint invocations.

    :stability: experimental
    '''


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker-alpha.InvocationsScalingProps",
    jsii_struct_bases=[aws_cdk.aws_applicationautoscaling.BaseTargetTrackingProps],
    name_mapping={
        "disable_scale_in": "disableScaleIn",
        "policy_name": "policyName",
        "scale_in_cooldown": "scaleInCooldown",
        "scale_out_cooldown": "scaleOutCooldown",
        "max_requests_per_second": "maxRequestsPerSecond",
        "safety_factor": "safetyFactor",
    },
)
class InvocationsScalingProps(
    aws_cdk.aws_applicationautoscaling.BaseTargetTrackingProps,
):
    def __init__(
        self,
        *,
        disable_scale_in: typing.Optional[builtins.bool] = None,
        policy_name: typing.Optional[builtins.str] = None,
        scale_in_cooldown: typing.Optional[aws_cdk.Duration] = None,
        scale_out_cooldown: typing.Optional[aws_cdk.Duration] = None,
        max_requests_per_second: jsii.Number,
        safety_factor: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''(experimental) Properties for enabling SageMaker Endpoint utilization tracking.

        :param disable_scale_in: Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won't remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the scalable resource. Default: false
        :param policy_name: A name for the scaling policy. Default: - Automatically generated name.
        :param scale_in_cooldown: Period after a scale in activity completes before another scale in activity can start. Default: Duration.seconds(300) for the following scalable targets: ECS services, Spot Fleet requests, EMR clusters, AppStream 2.0 fleets, Aurora DB clusters, Amazon SageMaker endpoint variants, Custom resources. For all other scalable targets, the default value is Duration.seconds(0): DynamoDB tables, DynamoDB global secondary indexes, Amazon Comprehend document classification endpoints, Lambda provisioned concurrency
        :param scale_out_cooldown: Period after a scale out activity completes before another scale out activity can start. Default: Duration.seconds(300) for the following scalable targets: ECS services, Spot Fleet requests, EMR clusters, AppStream 2.0 fleets, Aurora DB clusters, Amazon SageMaker endpoint variants, Custom resources. For all other scalable targets, the default value is Duration.seconds(0): DynamoDB tables, DynamoDB global secondary indexes, Amazon Comprehend document classification endpoints, Lambda provisioned concurrency
        :param max_requests_per_second: (experimental) Max RPS per instance used for calculating the target SageMaker variant invocation per instance. More documentation available here: https://docs.aws.amazon.com/sagemaker/latest/dg/endpoint-scaling-loadtest.html
        :param safety_factor: (experimental) Safty factor for calculating the target SageMaker variant invocation per instance. More documentation available here: https://docs.aws.amazon.com/sagemaker/latest/dg/endpoint-scaling-loadtest.html Default: 0.5

        :stability: experimental
        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_sagemaker_alpha as sagemaker
            
            # model: sagemaker.Model
            
            
            variant_name = "my-variant"
            endpoint_config = sagemaker.EndpointConfig(self, "EndpointConfig",
                instance_production_variants=[sagemaker.InstanceProductionVariantProps(
                    model=model,
                    variant_name=variant_name
                )
                ]
            )
            
            endpoint = sagemaker.Endpoint(self, "Endpoint", endpoint_config=endpoint_config)
            production_variant = endpoint.find_instance_production_variant(variant_name)
            instance_count = production_variant.auto_scale_instance_count(
                max_capacity=3
            )
            instance_count.scale_on_invocations("LimitRPS",
                max_requests_per_second=30
            )
        '''
        if __debug__:
            def stub(
                *,
                disable_scale_in: typing.Optional[builtins.bool] = None,
                policy_name: typing.Optional[builtins.str] = None,
                scale_in_cooldown: typing.Optional[aws_cdk.Duration] = None,
                scale_out_cooldown: typing.Optional[aws_cdk.Duration] = None,
                max_requests_per_second: jsii.Number,
                safety_factor: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument disable_scale_in", value=disable_scale_in, expected_type=type_hints["disable_scale_in"])
            check_type(argname="argument policy_name", value=policy_name, expected_type=type_hints["policy_name"])
            check_type(argname="argument scale_in_cooldown", value=scale_in_cooldown, expected_type=type_hints["scale_in_cooldown"])
            check_type(argname="argument scale_out_cooldown", value=scale_out_cooldown, expected_type=type_hints["scale_out_cooldown"])
            check_type(argname="argument max_requests_per_second", value=max_requests_per_second, expected_type=type_hints["max_requests_per_second"])
            check_type(argname="argument safety_factor", value=safety_factor, expected_type=type_hints["safety_factor"])
        self._values: typing.Dict[str, typing.Any] = {
            "max_requests_per_second": max_requests_per_second,
        }
        if disable_scale_in is not None:
            self._values["disable_scale_in"] = disable_scale_in
        if policy_name is not None:
            self._values["policy_name"] = policy_name
        if scale_in_cooldown is not None:
            self._values["scale_in_cooldown"] = scale_in_cooldown
        if scale_out_cooldown is not None:
            self._values["scale_out_cooldown"] = scale_out_cooldown
        if safety_factor is not None:
            self._values["safety_factor"] = safety_factor

    @builtins.property
    def disable_scale_in(self) -> typing.Optional[builtins.bool]:
        '''Indicates whether scale in by the target tracking policy is disabled.

        If the value is true, scale in is disabled and the target tracking policy
        won't remove capacity from the scalable resource. Otherwise, scale in is
        enabled and the target tracking policy can remove capacity from the
        scalable resource.

        :default: false
        '''
        result = self._values.get("disable_scale_in")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def policy_name(self) -> typing.Optional[builtins.str]:
        '''A name for the scaling policy.

        :default: - Automatically generated name.
        '''
        result = self._values.get("policy_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scale_in_cooldown(self) -> typing.Optional[aws_cdk.Duration]:
        '''Period after a scale in activity completes before another scale in activity can start.

        :default:

        Duration.seconds(300) for the following scalable targets: ECS services,
        Spot Fleet requests, EMR clusters, AppStream 2.0 fleets, Aurora DB clusters,
        Amazon SageMaker endpoint variants, Custom resources. For all other scalable
        targets, the default value is Duration.seconds(0): DynamoDB tables, DynamoDB
        global secondary indexes, Amazon Comprehend document classification endpoints,
        Lambda provisioned concurrency
        '''
        result = self._values.get("scale_in_cooldown")
        return typing.cast(typing.Optional[aws_cdk.Duration], result)

    @builtins.property
    def scale_out_cooldown(self) -> typing.Optional[aws_cdk.Duration]:
        '''Period after a scale out activity completes before another scale out activity can start.

        :default:

        Duration.seconds(300) for the following scalable targets: ECS services,
        Spot Fleet requests, EMR clusters, AppStream 2.0 fleets, Aurora DB clusters,
        Amazon SageMaker endpoint variants, Custom resources. For all other scalable
        targets, the default value is Duration.seconds(0): DynamoDB tables, DynamoDB
        global secondary indexes, Amazon Comprehend document classification endpoints,
        Lambda provisioned concurrency
        '''
        result = self._values.get("scale_out_cooldown")
        return typing.cast(typing.Optional[aws_cdk.Duration], result)

    @builtins.property
    def max_requests_per_second(self) -> jsii.Number:
        '''(experimental) Max RPS per instance used for calculating the target SageMaker variant invocation per instance.

        More documentation available here: https://docs.aws.amazon.com/sagemaker/latest/dg/endpoint-scaling-loadtest.html

        :stability: experimental
        '''
        result = self._values.get("max_requests_per_second")
        assert result is not None, "Required property 'max_requests_per_second' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def safety_factor(self) -> typing.Optional[jsii.Number]:
        '''(experimental) Safty factor for calculating the target SageMaker variant invocation per instance.

        More documentation available here: https://docs.aws.amazon.com/sagemaker/latest/dg/endpoint-scaling-loadtest.html

        :default: 0.5

        :stability: experimental
        '''
        result = self._values.get("safety_factor")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InvocationsScalingProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IModel)
class Model(
    aws_cdk.Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker-alpha.Model",
):
    '''(experimental) Defines a SageMaker Model.

    :stability: experimental
    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_sagemaker_alpha as sagemaker
        import path as path
        
        
        image = sagemaker.ContainerImage.from_asset(path.join("path", "to", "Dockerfile", "directory"))
        model_data = sagemaker.ModelData.from_asset(path.join("path", "to", "artifact", "file.tar.gz"))
        
        model = sagemaker.Model(self, "PrimaryContainerModel",
            containers=[sagemaker.ContainerDefinition(
                image=image,
                model_data=model_data
            )
            ]
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        allow_all_outbound: typing.Optional[builtins.bool] = None,
        containers: typing.Optional[typing.Sequence[typing.Union[ContainerDefinition, typing.Dict[str, typing.Any]]]] = None,
        model_name: typing.Optional[builtins.str] = None,
        role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
        security_groups: typing.Optional[typing.Sequence[aws_cdk.aws_ec2.ISecurityGroup]] = None,
        vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
        vpc_subnets: typing.Optional[typing.Union[aws_cdk.aws_ec2.SubnetSelection, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param allow_all_outbound: (experimental) Whether to allow the SageMaker Model to send all network traffic. If set to false, you must individually add traffic rules to allow the SageMaker Model to connect to network targets. Only used if 'vpc' is supplied. Default: true
        :param containers: (experimental) Specifies the container definitions for this model, consisting of either a single primary container or an inference pipeline of multiple containers. Default: - none
        :param model_name: (experimental) Name of the SageMaker Model. Default: - AWS CloudFormation generates a unique physical ID and uses that ID for the model's name.
        :param role: (experimental) The IAM role that the Amazon SageMaker service assumes. Default: - a new IAM role will be created with the ``AmazonSageMakerFullAccess`` policy attached.
        :param security_groups: (experimental) The security groups to associate to the Model. If no security groups are provided and 'vpc' is configured, one security group will be created automatically. Default: - A security group will be automatically created if 'vpc' is supplied
        :param vpc: (experimental) The VPC to deploy model containers to. Default: - none
        :param vpc_subnets: (experimental) The VPC subnets to use when deploying model containers. Default: - none

        :stability: experimental
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                id: builtins.str,
                *,
                allow_all_outbound: typing.Optional[builtins.bool] = None,
                containers: typing.Optional[typing.Sequence[typing.Union[ContainerDefinition, typing.Dict[str, typing.Any]]]] = None,
                model_name: typing.Optional[builtins.str] = None,
                role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
                security_groups: typing.Optional[typing.Sequence[aws_cdk.aws_ec2.ISecurityGroup]] = None,
                vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
                vpc_subnets: typing.Optional[typing.Union[aws_cdk.aws_ec2.SubnetSelection, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ModelProps(
            allow_all_outbound=allow_all_outbound,
            containers=containers,
            model_name=model_name,
            role=role,
            security_groups=security_groups,
            vpc=vpc,
            vpc_subnets=vpc_subnets,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromModelArn")
    @builtins.classmethod
    def from_model_arn(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        model_arn: builtins.str,
    ) -> IModel:
        '''(experimental) Imports a Model defined either outside the CDK or in a different CDK stack.

        :param scope: the Construct scope.
        :param id: the resource id.
        :param model_arn: the ARN of the model.

        :stability: experimental
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                id: builtins.str,
                model_arn: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument model_arn", value=model_arn, expected_type=type_hints["model_arn"])
        return typing.cast(IModel, jsii.sinvoke(cls, "fromModelArn", [scope, id, model_arn]))

    @jsii.member(jsii_name="fromModelAttributes")
    @builtins.classmethod
    def from_model_attributes(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        model_arn: builtins.str,
        role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
        security_groups: typing.Optional[typing.Sequence[aws_cdk.aws_ec2.ISecurityGroup]] = None,
    ) -> IModel:
        '''(experimental) Imports a Model defined either outside the CDK or in a different CDK stack.

        :param scope: the Construct scope.
        :param id: the resource id.
        :param model_arn: (experimental) The ARN of this model.
        :param role: (experimental) The IAM execution role associated with this model. Default: - When not provided, any role-related operations will no-op.
        :param security_groups: (experimental) The security groups for this model, if in a VPC. Default: - When not provided, the connections to/from this model cannot be managed.

        :stability: experimental
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                id: builtins.str,
                *,
                model_arn: builtins.str,
                role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
                security_groups: typing.Optional[typing.Sequence[aws_cdk.aws_ec2.ISecurityGroup]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        attrs = ModelAttributes(
            model_arn=model_arn, role=role, security_groups=security_groups
        )

        return typing.cast(IModel, jsii.sinvoke(cls, "fromModelAttributes", [scope, id, attrs]))

    @jsii.member(jsii_name="fromModelName")
    @builtins.classmethod
    def from_model_name(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        model_name: builtins.str,
    ) -> IModel:
        '''(experimental) Imports a Model defined either outside the CDK or in a different CDK stack.

        :param scope: the Construct scope.
        :param id: the resource id.
        :param model_name: the name of the model.

        :stability: experimental
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                id: builtins.str,
                model_name: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument model_name", value=model_name, expected_type=type_hints["model_name"])
        return typing.cast(IModel, jsii.sinvoke(cls, "fromModelName", [scope, id, model_name]))

    @jsii.member(jsii_name="addContainer")
    def add_container(
        self,
        *,
        image: ContainerImage,
        container_hostname: typing.Optional[builtins.str] = None,
        environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        model_data: typing.Optional["ModelData"] = None,
    ) -> None:
        '''(experimental) Add containers to the model.

        :param image: (experimental) The image used to start a container.
        :param container_hostname: (experimental) Hostname of the container within an inference pipeline. For single container models, this field is ignored. When specifying a hostname for one ContainerDefinition in a pipeline, hostnames must be specified for all other ContainerDefinitions in that pipeline. Default: - Amazon SageMaker will automatically assign a unique name based on the position of this ContainerDefinition in an inference pipeline.
        :param environment: (experimental) A map of environment variables to pass into the container. Default: - none
        :param model_data: (experimental) S3 path to the model artifacts. Default: - none

        :stability: experimental
        '''
        container = ContainerDefinition(
            image=image,
            container_hostname=container_hostname,
            environment=environment,
            model_data=model_data,
        )

        return typing.cast(None, jsii.invoke(self, "addContainer", [container]))

    @jsii.member(jsii_name="addToRolePolicy")
    def add_to_role_policy(self, statement: aws_cdk.aws_iam.PolicyStatement) -> None:
        '''(experimental) Adds a statement to the IAM role assumed by the instance.

        :param statement: -

        :stability: experimental
        '''
        if __debug__:
            def stub(statement: aws_cdk.aws_iam.PolicyStatement) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument statement", value=statement, expected_type=type_hints["statement"])
        return typing.cast(None, jsii.invoke(self, "addToRolePolicy", [statement]))

    @builtins.property
    @jsii.member(jsii_name="connections")
    def connections(self) -> aws_cdk.aws_ec2.Connections:
        '''(experimental) An accessor for the Connections object that will fail if this Model does not have a VPC configured.

        :stability: experimental
        '''
        return typing.cast(aws_cdk.aws_ec2.Connections, jsii.get(self, "connections"))

    @builtins.property
    @jsii.member(jsii_name="grantPrincipal")
    def grant_principal(self) -> aws_cdk.aws_iam.IPrincipal:
        '''(experimental) The principal this Model is running as.

        :stability: experimental
        '''
        return typing.cast(aws_cdk.aws_iam.IPrincipal, jsii.get(self, "grantPrincipal"))

    @builtins.property
    @jsii.member(jsii_name="modelArn")
    def model_arn(self) -> builtins.str:
        '''(experimental) Returns the ARN of this model.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "modelArn"))

    @builtins.property
    @jsii.member(jsii_name="modelName")
    def model_name(self) -> builtins.str:
        '''(experimental) Returns the name of the model.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "modelName"))

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> typing.Optional[aws_cdk.aws_iam.IRole]:
        '''(experimental) Execution role for SageMaker Model.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[aws_cdk.aws_iam.IRole], jsii.get(self, "role"))


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker-alpha.ModelAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "model_arn": "modelArn",
        "role": "role",
        "security_groups": "securityGroups",
    },
)
class ModelAttributes:
    def __init__(
        self,
        *,
        model_arn: builtins.str,
        role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
        security_groups: typing.Optional[typing.Sequence[aws_cdk.aws_ec2.ISecurityGroup]] = None,
    ) -> None:
        '''(experimental) Represents a Model resource defined outside this stack.

        :param model_arn: (experimental) The ARN of this model.
        :param role: (experimental) The IAM execution role associated with this model. Default: - When not provided, any role-related operations will no-op.
        :param security_groups: (experimental) The security groups for this model, if in a VPC. Default: - When not provided, the connections to/from this model cannot be managed.

        :stability: experimental
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_sagemaker_alpha as sagemaker_alpha
            from aws_cdk import aws_ec2 as ec2
            from aws_cdk import aws_iam as iam
            
            # role: iam.Role
            # security_group: ec2.SecurityGroup
            
            model_attributes = sagemaker_alpha.ModelAttributes(
                model_arn="modelArn",
            
                # the properties below are optional
                role=role,
                security_groups=[security_group]
            )
        '''
        if __debug__:
            def stub(
                *,
                model_arn: builtins.str,
                role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
                security_groups: typing.Optional[typing.Sequence[aws_cdk.aws_ec2.ISecurityGroup]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument model_arn", value=model_arn, expected_type=type_hints["model_arn"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
        self._values: typing.Dict[str, typing.Any] = {
            "model_arn": model_arn,
        }
        if role is not None:
            self._values["role"] = role
        if security_groups is not None:
            self._values["security_groups"] = security_groups

    @builtins.property
    def model_arn(self) -> builtins.str:
        '''(experimental) The ARN of this model.

        :stability: experimental
        '''
        result = self._values.get("model_arn")
        assert result is not None, "Required property 'model_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role(self) -> typing.Optional[aws_cdk.aws_iam.IRole]:
        '''(experimental) The IAM execution role associated with this model.

        :default: - When not provided, any role-related operations will no-op.

        :stability: experimental
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[aws_cdk.aws_iam.IRole], result)

    @builtins.property
    def security_groups(
        self,
    ) -> typing.Optional[typing.List[aws_cdk.aws_ec2.ISecurityGroup]]:
        '''(experimental) The security groups for this model, if in a VPC.

        :default: - When not provided, the connections to/from this model cannot be managed.

        :stability: experimental
        '''
        result = self._values.get("security_groups")
        return typing.cast(typing.Optional[typing.List[aws_cdk.aws_ec2.ISecurityGroup]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ModelAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ModelData(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="@aws-cdk/aws-sagemaker-alpha.ModelData",
):
    '''(experimental) Model data represents the source of model artifacts, which will ultimately be loaded from an S3 location.

    :stability: experimental
    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_sagemaker_alpha as sagemaker
        import path as path
        
        
        image = sagemaker.ContainerImage.from_asset(path.join("path", "to", "Dockerfile", "directory"))
        model_data = sagemaker.ModelData.from_asset(path.join("path", "to", "artifact", "file.tar.gz"))
        
        model = sagemaker.Model(self, "PrimaryContainerModel",
            containers=[sagemaker.ContainerDefinition(
                image=image,
                model_data=model_data
            )
            ]
        )
    '''

    def __init__(self) -> None:
        '''
        :stability: experimental
        '''
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="fromAsset")
    @builtins.classmethod
    def from_asset(
        cls,
        path: builtins.str,
        *,
        readers: typing.Optional[typing.Sequence[aws_cdk.aws_iam.IGrantable]] = None,
        asset_hash: typing.Optional[builtins.str] = None,
        asset_hash_type: typing.Optional[aws_cdk.AssetHashType] = None,
        bundling: typing.Optional[typing.Union[aws_cdk.BundlingOptions, typing.Dict[str, typing.Any]]] = None,
        exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
        follow_symlinks: typing.Optional[aws_cdk.SymlinkFollowMode] = None,
        ignore_mode: typing.Optional[aws_cdk.IgnoreMode] = None,
    ) -> "ModelData":
        '''(experimental) Constructs model data that will be uploaded to S3 as part of the CDK app deployment.

        :param path: The local path to a model artifact file as a gzipped tar file.
        :param readers: A list of principals that should be able to read this asset from S3. You can use ``asset.grantRead(principal)`` to grant read permissions later. Default: - No principals that can read file asset.
        :param asset_hash: Specify a custom hash for this asset. If ``assetHashType`` is set it must be set to ``AssetHashType.CUSTOM``. For consistency, this custom hash will be SHA256 hashed and encoded as hex. The resulting hash will be the asset hash. NOTE: the hash is used in order to identify a specific revision of the asset, and used for optimizing and caching deployment activities related to this asset such as packaging, uploading to Amazon S3, etc. If you chose to customize the hash, you will need to make sure it is updated every time the asset changes, or otherwise it is possible that some deployments will not be invalidated. Default: - based on ``assetHashType``
        :param asset_hash_type: Specifies the type of hash to calculate for this asset. If ``assetHash`` is configured, this option must be ``undefined`` or ``AssetHashType.CUSTOM``. Default: - the default is ``AssetHashType.SOURCE``, but if ``assetHash`` is explicitly specified this value defaults to ``AssetHashType.CUSTOM``.
        :param bundling: Bundle the asset by executing a command in a Docker container or a custom bundling provider. The asset path will be mounted at ``/asset-input``. The Docker container is responsible for putting content at ``/asset-output``. The content at ``/asset-output`` will be zipped and used as the final asset. Default: - uploaded as-is to S3 if the asset is a regular file or a .zip file, archived into a .zip file and uploaded to S3 otherwise
        :param exclude: File paths matching the patterns will be excluded. See ``ignoreMode`` to set the matching behavior. Has no effect on Assets bundled using the ``bundling`` property. Default: - nothing is excluded
        :param follow_symlinks: A strategy for how to handle symlinks. Default: SymlinkFollowMode.NEVER
        :param ignore_mode: The ignore behavior to use for ``exclude`` patterns. Default: IgnoreMode.GLOB

        :stability: experimental
        '''
        if __debug__:
            def stub(
                path: builtins.str,
                *,
                readers: typing.Optional[typing.Sequence[aws_cdk.aws_iam.IGrantable]] = None,
                asset_hash: typing.Optional[builtins.str] = None,
                asset_hash_type: typing.Optional[aws_cdk.AssetHashType] = None,
                bundling: typing.Optional[typing.Union[aws_cdk.BundlingOptions, typing.Dict[str, typing.Any]]] = None,
                exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
                follow_symlinks: typing.Optional[aws_cdk.SymlinkFollowMode] = None,
                ignore_mode: typing.Optional[aws_cdk.IgnoreMode] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        options = aws_cdk.aws_s3_assets.AssetOptions(
            readers=readers,
            asset_hash=asset_hash,
            asset_hash_type=asset_hash_type,
            bundling=bundling,
            exclude=exclude,
            follow_symlinks=follow_symlinks,
            ignore_mode=ignore_mode,
        )

        return typing.cast("ModelData", jsii.sinvoke(cls, "fromAsset", [path, options]))

    @jsii.member(jsii_name="fromBucket")
    @builtins.classmethod
    def from_bucket(
        cls,
        bucket: aws_cdk.aws_s3.IBucket,
        object_key: builtins.str,
    ) -> "ModelData":
        '''(experimental) Constructs model data which is already available within S3.

        :param bucket: The S3 bucket within which the model artifacts are stored.
        :param object_key: The S3 object key at which the model artifacts are stored.

        :stability: experimental
        '''
        if __debug__:
            def stub(bucket: aws_cdk.aws_s3.IBucket, object_key: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument object_key", value=object_key, expected_type=type_hints["object_key"])
        return typing.cast("ModelData", jsii.sinvoke(cls, "fromBucket", [bucket, object_key]))

    @jsii.member(jsii_name="bind")
    @abc.abstractmethod
    def bind(self, scope: constructs.Construct, model: IModel) -> "ModelDataConfig":
        '''(experimental) This method is invoked by the SageMaker Model construct when it needs to resolve the model data to a URI.

        :param scope: The scope within which the model data is resolved.
        :param model: The Model construct performing the URI resolution.

        :stability: experimental
        '''
        ...


class _ModelDataProxy(ModelData):
    @jsii.member(jsii_name="bind")
    def bind(self, scope: constructs.Construct, model: IModel) -> "ModelDataConfig":
        '''(experimental) This method is invoked by the SageMaker Model construct when it needs to resolve the model data to a URI.

        :param scope: The scope within which the model data is resolved.
        :param model: The Model construct performing the URI resolution.

        :stability: experimental
        '''
        if __debug__:
            def stub(scope: constructs.Construct, model: IModel) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument model", value=model, expected_type=type_hints["model"])
        return typing.cast("ModelDataConfig", jsii.invoke(self, "bind", [scope, model]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, ModelData).__jsii_proxy_class__ = lambda : _ModelDataProxy


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker-alpha.ModelDataConfig",
    jsii_struct_bases=[],
    name_mapping={"uri": "uri"},
)
class ModelDataConfig:
    def __init__(self, *, uri: builtins.str) -> None:
        '''(experimental) The configuration needed to reference model artifacts.

        :param uri: (experimental) The S3 path where the model artifacts, which result from model training, are stored. This path must point to a single gzip compressed tar archive (.tar.gz suffix).

        :stability: experimental
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_sagemaker_alpha as sagemaker_alpha
            
            model_data_config = sagemaker_alpha.ModelDataConfig(
                uri="uri"
            )
        '''
        if __debug__:
            def stub(*, uri: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument uri", value=uri, expected_type=type_hints["uri"])
        self._values: typing.Dict[str, typing.Any] = {
            "uri": uri,
        }

    @builtins.property
    def uri(self) -> builtins.str:
        '''(experimental) The S3 path where the model artifacts, which result from model training, are stored.

        This path
        must point to a single gzip compressed tar archive (.tar.gz suffix).

        :stability: experimental
        '''
        result = self._values.get("uri")
        assert result is not None, "Required property 'uri' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ModelDataConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker-alpha.ModelProps",
    jsii_struct_bases=[],
    name_mapping={
        "allow_all_outbound": "allowAllOutbound",
        "containers": "containers",
        "model_name": "modelName",
        "role": "role",
        "security_groups": "securityGroups",
        "vpc": "vpc",
        "vpc_subnets": "vpcSubnets",
    },
)
class ModelProps:
    def __init__(
        self,
        *,
        allow_all_outbound: typing.Optional[builtins.bool] = None,
        containers: typing.Optional[typing.Sequence[typing.Union[ContainerDefinition, typing.Dict[str, typing.Any]]]] = None,
        model_name: typing.Optional[builtins.str] = None,
        role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
        security_groups: typing.Optional[typing.Sequence[aws_cdk.aws_ec2.ISecurityGroup]] = None,
        vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
        vpc_subnets: typing.Optional[typing.Union[aws_cdk.aws_ec2.SubnetSelection, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''(experimental) Construction properties for a SageMaker Model.

        :param allow_all_outbound: (experimental) Whether to allow the SageMaker Model to send all network traffic. If set to false, you must individually add traffic rules to allow the SageMaker Model to connect to network targets. Only used if 'vpc' is supplied. Default: true
        :param containers: (experimental) Specifies the container definitions for this model, consisting of either a single primary container or an inference pipeline of multiple containers. Default: - none
        :param model_name: (experimental) Name of the SageMaker Model. Default: - AWS CloudFormation generates a unique physical ID and uses that ID for the model's name.
        :param role: (experimental) The IAM role that the Amazon SageMaker service assumes. Default: - a new IAM role will be created with the ``AmazonSageMakerFullAccess`` policy attached.
        :param security_groups: (experimental) The security groups to associate to the Model. If no security groups are provided and 'vpc' is configured, one security group will be created automatically. Default: - A security group will be automatically created if 'vpc' is supplied
        :param vpc: (experimental) The VPC to deploy model containers to. Default: - none
        :param vpc_subnets: (experimental) The VPC subnets to use when deploying model containers. Default: - none

        :stability: experimental
        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_sagemaker_alpha as sagemaker
            import path as path
            
            
            image = sagemaker.ContainerImage.from_asset(path.join("path", "to", "Dockerfile", "directory"))
            model_data = sagemaker.ModelData.from_asset(path.join("path", "to", "artifact", "file.tar.gz"))
            
            model = sagemaker.Model(self, "PrimaryContainerModel",
                containers=[sagemaker.ContainerDefinition(
                    image=image,
                    model_data=model_data
                )
                ]
            )
        '''
        if isinstance(vpc_subnets, dict):
            vpc_subnets = aws_cdk.aws_ec2.SubnetSelection(**vpc_subnets)
        if __debug__:
            def stub(
                *,
                allow_all_outbound: typing.Optional[builtins.bool] = None,
                containers: typing.Optional[typing.Sequence[typing.Union[ContainerDefinition, typing.Dict[str, typing.Any]]]] = None,
                model_name: typing.Optional[builtins.str] = None,
                role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
                security_groups: typing.Optional[typing.Sequence[aws_cdk.aws_ec2.ISecurityGroup]] = None,
                vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
                vpc_subnets: typing.Optional[typing.Union[aws_cdk.aws_ec2.SubnetSelection, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument allow_all_outbound", value=allow_all_outbound, expected_type=type_hints["allow_all_outbound"])
            check_type(argname="argument containers", value=containers, expected_type=type_hints["containers"])
            check_type(argname="argument model_name", value=model_name, expected_type=type_hints["model_name"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
            check_type(argname="argument vpc_subnets", value=vpc_subnets, expected_type=type_hints["vpc_subnets"])
        self._values: typing.Dict[str, typing.Any] = {}
        if allow_all_outbound is not None:
            self._values["allow_all_outbound"] = allow_all_outbound
        if containers is not None:
            self._values["containers"] = containers
        if model_name is not None:
            self._values["model_name"] = model_name
        if role is not None:
            self._values["role"] = role
        if security_groups is not None:
            self._values["security_groups"] = security_groups
        if vpc is not None:
            self._values["vpc"] = vpc
        if vpc_subnets is not None:
            self._values["vpc_subnets"] = vpc_subnets

    @builtins.property
    def allow_all_outbound(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Whether to allow the SageMaker Model to send all network traffic.

        If set to false, you must individually add traffic rules to allow the
        SageMaker Model to connect to network targets.

        Only used if 'vpc' is supplied.

        :default: true

        :stability: experimental
        '''
        result = self._values.get("allow_all_outbound")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def containers(self) -> typing.Optional[typing.List[ContainerDefinition]]:
        '''(experimental) Specifies the container definitions for this model, consisting of either a single primary container or an inference pipeline of multiple containers.

        :default: - none

        :stability: experimental
        '''
        result = self._values.get("containers")
        return typing.cast(typing.Optional[typing.List[ContainerDefinition]], result)

    @builtins.property
    def model_name(self) -> typing.Optional[builtins.str]:
        '''(experimental) Name of the SageMaker Model.

        :default:

        - AWS CloudFormation generates a unique physical ID and uses that ID for the model's
        name.

        :stability: experimental
        '''
        result = self._values.get("model_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role(self) -> typing.Optional[aws_cdk.aws_iam.IRole]:
        '''(experimental) The IAM role that the Amazon SageMaker service assumes.

        :default: - a new IAM role will be created with the ``AmazonSageMakerFullAccess`` policy attached.

        :see: https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles.html#sagemaker-roles-createmodel-perms
        :stability: experimental
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[aws_cdk.aws_iam.IRole], result)

    @builtins.property
    def security_groups(
        self,
    ) -> typing.Optional[typing.List[aws_cdk.aws_ec2.ISecurityGroup]]:
        '''(experimental) The security groups to associate to the Model.

        If no security groups are provided and 'vpc' is
        configured, one security group will be created automatically.

        :default: - A security group will be automatically created if 'vpc' is supplied

        :stability: experimental
        '''
        result = self._values.get("security_groups")
        return typing.cast(typing.Optional[typing.List[aws_cdk.aws_ec2.ISecurityGroup]], result)

    @builtins.property
    def vpc(self) -> typing.Optional[aws_cdk.aws_ec2.IVpc]:
        '''(experimental) The VPC to deploy model containers to.

        :default: - none

        :stability: experimental
        '''
        result = self._values.get("vpc")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.IVpc], result)

    @builtins.property
    def vpc_subnets(self) -> typing.Optional[aws_cdk.aws_ec2.SubnetSelection]:
        '''(experimental) The VPC subnets to use when deploying model containers.

        :default: - none

        :stability: experimental
        '''
        result = self._values.get("vpc_subnets")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.SubnetSelection], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ModelProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ScalableInstanceCount(
    aws_cdk.aws_applicationautoscaling.BaseScalableAttribute,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker-alpha.ScalableInstanceCount",
):
    '''(experimental) A scalable sagemaker endpoint attribute.

    :stability: experimental
    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_sagemaker_alpha as sagemaker
        
        # model: sagemaker.Model
        
        
        variant_name = "my-variant"
        endpoint_config = sagemaker.EndpointConfig(self, "EndpointConfig",
            instance_production_variants=[sagemaker.InstanceProductionVariantProps(
                model=model,
                variant_name=variant_name
            )
            ]
        )
        
        endpoint = sagemaker.Endpoint(self, "Endpoint", endpoint_config=endpoint_config)
        production_variant = endpoint.find_instance_production_variant(variant_name)
        instance_count = production_variant.auto_scale_instance_count(
            max_capacity=3
        )
        instance_count.scale_on_invocations("LimitRPS",
            max_requests_per_second=30
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        dimension: builtins.str,
        resource_id: builtins.str,
        role: aws_cdk.aws_iam.IRole,
        service_namespace: aws_cdk.aws_applicationautoscaling.ServiceNamespace,
        max_capacity: jsii.Number,
        min_capacity: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''(experimental) Constructs a new instance of the ScalableInstanceCount class.

        :param scope: -
        :param id: -
        :param dimension: Scalable dimension of the attribute.
        :param resource_id: Resource ID of the attribute.
        :param role: Role to use for scaling.
        :param service_namespace: Service namespace of the scalable attribute.
        :param max_capacity: Maximum capacity to scale to.
        :param min_capacity: Minimum capacity to scale to. Default: 1

        :stability: experimental
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                id: builtins.str,
                *,
                dimension: builtins.str,
                resource_id: builtins.str,
                role: aws_cdk.aws_iam.IRole,
                service_namespace: aws_cdk.aws_applicationautoscaling.ServiceNamespace,
                max_capacity: jsii.Number,
                min_capacity: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ScalableInstanceCountProps(
            dimension=dimension,
            resource_id=resource_id,
            role=role,
            service_namespace=service_namespace,
            max_capacity=max_capacity,
            min_capacity=min_capacity,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="scaleOnInvocations")
    def scale_on_invocations(
        self,
        id: builtins.str,
        *,
        max_requests_per_second: jsii.Number,
        safety_factor: typing.Optional[jsii.Number] = None,
        disable_scale_in: typing.Optional[builtins.bool] = None,
        policy_name: typing.Optional[builtins.str] = None,
        scale_in_cooldown: typing.Optional[aws_cdk.Duration] = None,
        scale_out_cooldown: typing.Optional[aws_cdk.Duration] = None,
    ) -> None:
        '''(experimental) Scales in or out to achieve a target requests per second per instance.

        :param id: -
        :param max_requests_per_second: (experimental) Max RPS per instance used for calculating the target SageMaker variant invocation per instance. More documentation available here: https://docs.aws.amazon.com/sagemaker/latest/dg/endpoint-scaling-loadtest.html
        :param safety_factor: (experimental) Safty factor for calculating the target SageMaker variant invocation per instance. More documentation available here: https://docs.aws.amazon.com/sagemaker/latest/dg/endpoint-scaling-loadtest.html Default: 0.5
        :param disable_scale_in: Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won't remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the scalable resource. Default: false
        :param policy_name: A name for the scaling policy. Default: - Automatically generated name.
        :param scale_in_cooldown: Period after a scale in activity completes before another scale in activity can start. Default: Duration.seconds(300) for the following scalable targets: ECS services, Spot Fleet requests, EMR clusters, AppStream 2.0 fleets, Aurora DB clusters, Amazon SageMaker endpoint variants, Custom resources. For all other scalable targets, the default value is Duration.seconds(0): DynamoDB tables, DynamoDB global secondary indexes, Amazon Comprehend document classification endpoints, Lambda provisioned concurrency
        :param scale_out_cooldown: Period after a scale out activity completes before another scale out activity can start. Default: Duration.seconds(300) for the following scalable targets: ECS services, Spot Fleet requests, EMR clusters, AppStream 2.0 fleets, Aurora DB clusters, Amazon SageMaker endpoint variants, Custom resources. For all other scalable targets, the default value is Duration.seconds(0): DynamoDB tables, DynamoDB global secondary indexes, Amazon Comprehend document classification endpoints, Lambda provisioned concurrency

        :stability: experimental
        '''
        if __debug__:
            def stub(
                id: builtins.str,
                *,
                max_requests_per_second: jsii.Number,
                safety_factor: typing.Optional[jsii.Number] = None,
                disable_scale_in: typing.Optional[builtins.bool] = None,
                policy_name: typing.Optional[builtins.str] = None,
                scale_in_cooldown: typing.Optional[aws_cdk.Duration] = None,
                scale_out_cooldown: typing.Optional[aws_cdk.Duration] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = InvocationsScalingProps(
            max_requests_per_second=max_requests_per_second,
            safety_factor=safety_factor,
            disable_scale_in=disable_scale_in,
            policy_name=policy_name,
            scale_in_cooldown=scale_in_cooldown,
            scale_out_cooldown=scale_out_cooldown,
        )

        return typing.cast(None, jsii.invoke(self, "scaleOnInvocations", [id, props]))


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker-alpha.ScalableInstanceCountProps",
    jsii_struct_bases=[aws_cdk.aws_applicationautoscaling.BaseScalableAttributeProps],
    name_mapping={
        "max_capacity": "maxCapacity",
        "min_capacity": "minCapacity",
        "dimension": "dimension",
        "resource_id": "resourceId",
        "role": "role",
        "service_namespace": "serviceNamespace",
    },
)
class ScalableInstanceCountProps(
    aws_cdk.aws_applicationautoscaling.BaseScalableAttributeProps,
):
    def __init__(
        self,
        *,
        max_capacity: jsii.Number,
        min_capacity: typing.Optional[jsii.Number] = None,
        dimension: builtins.str,
        resource_id: builtins.str,
        role: aws_cdk.aws_iam.IRole,
        service_namespace: aws_cdk.aws_applicationautoscaling.ServiceNamespace,
    ) -> None:
        '''(experimental) The properties of a scalable attribute representing task count.

        :param max_capacity: Maximum capacity to scale to.
        :param min_capacity: Minimum capacity to scale to. Default: 1
        :param dimension: Scalable dimension of the attribute.
        :param resource_id: Resource ID of the attribute.
        :param role: Role to use for scaling.
        :param service_namespace: Service namespace of the scalable attribute.

        :stability: experimental
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_sagemaker_alpha as sagemaker_alpha
            from aws_cdk import aws_applicationautoscaling as appscaling
            from aws_cdk import aws_iam as iam
            
            # role: iam.Role
            
            scalable_instance_count_props = sagemaker_alpha.ScalableInstanceCountProps(
                dimension="dimension",
                max_capacity=123,
                resource_id="resourceId",
                role=role,
                service_namespace=appscaling.ServiceNamespace.ECS,
            
                # the properties below are optional
                min_capacity=123
            )
        '''
        if __debug__:
            def stub(
                *,
                max_capacity: jsii.Number,
                min_capacity: typing.Optional[jsii.Number] = None,
                dimension: builtins.str,
                resource_id: builtins.str,
                role: aws_cdk.aws_iam.IRole,
                service_namespace: aws_cdk.aws_applicationautoscaling.ServiceNamespace,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument max_capacity", value=max_capacity, expected_type=type_hints["max_capacity"])
            check_type(argname="argument min_capacity", value=min_capacity, expected_type=type_hints["min_capacity"])
            check_type(argname="argument dimension", value=dimension, expected_type=type_hints["dimension"])
            check_type(argname="argument resource_id", value=resource_id, expected_type=type_hints["resource_id"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument service_namespace", value=service_namespace, expected_type=type_hints["service_namespace"])
        self._values: typing.Dict[str, typing.Any] = {
            "max_capacity": max_capacity,
            "dimension": dimension,
            "resource_id": resource_id,
            "role": role,
            "service_namespace": service_namespace,
        }
        if min_capacity is not None:
            self._values["min_capacity"] = min_capacity

    @builtins.property
    def max_capacity(self) -> jsii.Number:
        '''Maximum capacity to scale to.'''
        result = self._values.get("max_capacity")
        assert result is not None, "Required property 'max_capacity' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def min_capacity(self) -> typing.Optional[jsii.Number]:
        '''Minimum capacity to scale to.

        :default: 1
        '''
        result = self._values.get("min_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def dimension(self) -> builtins.str:
        '''Scalable dimension of the attribute.'''
        result = self._values.get("dimension")
        assert result is not None, "Required property 'dimension' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_id(self) -> builtins.str:
        '''Resource ID of the attribute.'''
        result = self._values.get("resource_id")
        assert result is not None, "Required property 'resource_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role(self) -> aws_cdk.aws_iam.IRole:
        '''Role to use for scaling.'''
        result = self._values.get("role")
        assert result is not None, "Required property 'role' is missing"
        return typing.cast(aws_cdk.aws_iam.IRole, result)

    @builtins.property
    def service_namespace(self) -> aws_cdk.aws_applicationautoscaling.ServiceNamespace:
        '''Service namespace of the scalable attribute.'''
        result = self._values.get("service_namespace")
        assert result is not None, "Required property 'service_namespace' is missing"
        return typing.cast(aws_cdk.aws_applicationautoscaling.ServiceNamespace, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ScalableInstanceCountProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IEndpoint)
class Endpoint(
    aws_cdk.Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker-alpha.Endpoint",
):
    '''(experimental) Defines a SageMaker endpoint.

    :stability: experimental
    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_sagemaker_alpha as sagemaker
        
        # endpoint_config: sagemaker.EndpointConfig
        
        
        endpoint = sagemaker.Endpoint(self, "Endpoint", endpoint_config=endpoint_config)
        production_variant = endpoint.find_instance_production_variant("my-variant")
        production_variant.metric_model_latency().create_alarm(self, "ModelLatencyAlarm",
            threshold=100000,
            evaluation_periods=3
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        endpoint_config: IEndpointConfig,
        endpoint_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param endpoint_config: (experimental) The endpoint configuration to use for this endpoint.
        :param endpoint_name: (experimental) Name of the endpoint. Default: - AWS CloudFormation generates a unique physical ID and uses that ID for the endpoint's name.

        :stability: experimental
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                id: builtins.str,
                *,
                endpoint_config: IEndpointConfig,
                endpoint_name: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = EndpointProps(
            endpoint_config=endpoint_config, endpoint_name=endpoint_name
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromEndpointArn")
    @builtins.classmethod
    def from_endpoint_arn(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        endpoint_arn: builtins.str,
    ) -> IEndpoint:
        '''(experimental) Imports an Endpoint defined either outside the CDK or in a different CDK stack.

        :param scope: the Construct scope.
        :param id: the resource id.
        :param endpoint_arn: the ARN of the endpoint.

        :stability: experimental
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                id: builtins.str,
                endpoint_arn: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument endpoint_arn", value=endpoint_arn, expected_type=type_hints["endpoint_arn"])
        return typing.cast(IEndpoint, jsii.sinvoke(cls, "fromEndpointArn", [scope, id, endpoint_arn]))

    @jsii.member(jsii_name="fromEndpointAttributes")
    @builtins.classmethod
    def from_endpoint_attributes(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        endpoint_arn: builtins.str,
    ) -> IEndpoint:
        '''(experimental) Imports an Endpoint defined either outside the CDK or in a different CDK stack.

        :param scope: the Construct scope.
        :param id: the resource id.
        :param endpoint_arn: (experimental) The ARN of this endpoint.

        :stability: experimental
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                id: builtins.str,
                *,
                endpoint_arn: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        attrs = EndpointAttributes(endpoint_arn=endpoint_arn)

        return typing.cast(IEndpoint, jsii.sinvoke(cls, "fromEndpointAttributes", [scope, id, attrs]))

    @jsii.member(jsii_name="fromEndpointName")
    @builtins.classmethod
    def from_endpoint_name(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        endpoint_name: builtins.str,
    ) -> IEndpoint:
        '''(experimental) Imports an Endpoint defined either outside the CDK or in a different CDK stack.

        :param scope: the Construct scope.
        :param id: the resource id.
        :param endpoint_name: the name of the endpoint.

        :stability: experimental
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                id: builtins.str,
                endpoint_name: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument endpoint_name", value=endpoint_name, expected_type=type_hints["endpoint_name"])
        return typing.cast(IEndpoint, jsii.sinvoke(cls, "fromEndpointName", [scope, id, endpoint_name]))

    @jsii.member(jsii_name="findInstanceProductionVariant")
    def find_instance_production_variant(
        self,
        name: builtins.str,
    ) -> IEndpointInstanceProductionVariant:
        '''(experimental) Find instance production variant based on variant name.

        :param name: Variant name from production variant.

        :stability: experimental
        '''
        if __debug__:
            def stub(name: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        return typing.cast(IEndpointInstanceProductionVariant, jsii.invoke(self, "findInstanceProductionVariant", [name]))

    @jsii.member(jsii_name="grantInvoke")
    def grant_invoke(
        self,
        grantee: aws_cdk.aws_iam.IGrantable,
    ) -> aws_cdk.aws_iam.Grant:
        '''(experimental) Permits an IAM principal to invoke this endpoint.

        :param grantee: The principal to grant access to.

        :stability: experimental
        '''
        if __debug__:
            def stub(grantee: aws_cdk.aws_iam.IGrantable) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(aws_cdk.aws_iam.Grant, jsii.invoke(self, "grantInvoke", [grantee]))

    @builtins.property
    @jsii.member(jsii_name="endpointArn")
    def endpoint_arn(self) -> builtins.str:
        '''(experimental) The ARN of the endpoint.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "endpointArn"))

    @builtins.property
    @jsii.member(jsii_name="endpointName")
    def endpoint_name(self) -> builtins.str:
        '''(experimental) The name of the endpoint.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "endpointName"))

    @builtins.property
    @jsii.member(jsii_name="instanceProductionVariants")
    def instance_production_variants(
        self,
    ) -> typing.List[IEndpointInstanceProductionVariant]:
        '''(experimental) Get instance production variants associated with endpoint.

        :stability: experimental
        '''
        return typing.cast(typing.List[IEndpointInstanceProductionVariant], jsii.get(self, "instanceProductionVariants"))


@jsii.implements(IEndpointConfig)
class EndpointConfig(
    aws_cdk.Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker-alpha.EndpointConfig",
):
    '''(experimental) Defines a SageMaker EndpointConfig.

    :stability: experimental
    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_sagemaker_alpha as sagemaker
        
        # model_a: sagemaker.Model
        # model_b: sagemaker.Model
        
        
        endpoint_config = sagemaker.EndpointConfig(self, "EndpointConfig",
            instance_production_variants=[sagemaker.InstanceProductionVariantProps(
                model=model_a,
                variant_name="modelA",
                initial_variant_weight=2
            ), sagemaker.InstanceProductionVariantProps(
                model=model_b,
                variant_name="variantB",
                initial_variant_weight=1
            )
            ]
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        encryption_key: typing.Optional[aws_cdk.aws_kms.IKey] = None,
        endpoint_config_name: typing.Optional[builtins.str] = None,
        instance_production_variants: typing.Optional[typing.Sequence[typing.Union[InstanceProductionVariantProps, typing.Dict[str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param encryption_key: (experimental) Optional KMS encryption key associated with this stream. Default: - none
        :param endpoint_config_name: (experimental) Name of the endpoint configuration. Default: - AWS CloudFormation generates a unique physical ID and uses that ID for the endpoint configuration's name.
        :param instance_production_variants: (experimental) A list of instance production variants. You can always add more variants later by calling {@link EndpointConfig#addInstanceProductionVariant}. Default: - none

        :stability: experimental
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                id: builtins.str,
                *,
                encryption_key: typing.Optional[aws_cdk.aws_kms.IKey] = None,
                endpoint_config_name: typing.Optional[builtins.str] = None,
                instance_production_variants: typing.Optional[typing.Sequence[typing.Union[InstanceProductionVariantProps, typing.Dict[str, typing.Any]]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = EndpointConfigProps(
            encryption_key=encryption_key,
            endpoint_config_name=endpoint_config_name,
            instance_production_variants=instance_production_variants,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromEndpointConfigArn")
    @builtins.classmethod
    def from_endpoint_config_arn(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        endpoint_config_arn: builtins.str,
    ) -> IEndpointConfig:
        '''(experimental) Imports an EndpointConfig defined either outside the CDK or in a different CDK stack.

        :param scope: the Construct scope.
        :param id: the resource id.
        :param endpoint_config_arn: the ARN of the endpoint configuration.

        :stability: experimental
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                id: builtins.str,
                endpoint_config_arn: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument endpoint_config_arn", value=endpoint_config_arn, expected_type=type_hints["endpoint_config_arn"])
        return typing.cast(IEndpointConfig, jsii.sinvoke(cls, "fromEndpointConfigArn", [scope, id, endpoint_config_arn]))

    @jsii.member(jsii_name="fromEndpointConfigName")
    @builtins.classmethod
    def from_endpoint_config_name(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        endpoint_config_name: builtins.str,
    ) -> IEndpointConfig:
        '''(experimental) Imports an EndpointConfig defined either outside the CDK or in a different CDK stack.

        :param scope: the Construct scope.
        :param id: the resource id.
        :param endpoint_config_name: the name of the endpoint configuration.

        :stability: experimental
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                id: builtins.str,
                endpoint_config_name: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument endpoint_config_name", value=endpoint_config_name, expected_type=type_hints["endpoint_config_name"])
        return typing.cast(IEndpointConfig, jsii.sinvoke(cls, "fromEndpointConfigName", [scope, id, endpoint_config_name]))

    @jsii.member(jsii_name="addInstanceProductionVariant")
    def add_instance_production_variant(
        self,
        *,
        model: IModel,
        variant_name: builtins.str,
        accelerator_type: typing.Optional[AcceleratorType] = None,
        initial_instance_count: typing.Optional[jsii.Number] = None,
        initial_variant_weight: typing.Optional[jsii.Number] = None,
        instance_type: typing.Optional[InstanceType] = None,
    ) -> None:
        '''(experimental) Add production variant to the endpoint configuration.

        :param model: (experimental) The model to host.
        :param variant_name: (experimental) Name of the production variant.
        :param accelerator_type: (experimental) The size of the Elastic Inference (EI) instance to use for the production variant. EI instances provide on-demand GPU computing for inference. Default: - none
        :param initial_instance_count: (experimental) Number of instances to launch initially. Default: 1
        :param initial_variant_weight: (experimental) Determines initial traffic distribution among all of the models that you specify in the endpoint configuration. The traffic to a production variant is determined by the ratio of the variant weight to the sum of all variant weight values across all production variants. Default: 1.0
        :param instance_type: (experimental) Instance type of the production variant. Default: InstanceType.T2_MEDIUM

        :stability: experimental
        '''
        props = InstanceProductionVariantProps(
            model=model,
            variant_name=variant_name,
            accelerator_type=accelerator_type,
            initial_instance_count=initial_instance_count,
            initial_variant_weight=initial_variant_weight,
            instance_type=instance_type,
        )

        return typing.cast(None, jsii.invoke(self, "addInstanceProductionVariant", [props]))

    @builtins.property
    @jsii.member(jsii_name="endpointConfigArn")
    def endpoint_config_arn(self) -> builtins.str:
        '''(experimental) The ARN of the endpoint configuration.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "endpointConfigArn"))

    @builtins.property
    @jsii.member(jsii_name="endpointConfigName")
    def endpoint_config_name(self) -> builtins.str:
        '''(experimental) The name of the endpoint configuration.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "endpointConfigName"))


__all__ = [
    "AcceleratorType",
    "ContainerDefinition",
    "ContainerImage",
    "ContainerImageConfig",
    "Endpoint",
    "EndpointAttributes",
    "EndpointConfig",
    "EndpointConfigProps",
    "EndpointProps",
    "IEndpoint",
    "IEndpointConfig",
    "IEndpointInstanceProductionVariant",
    "IModel",
    "InstanceProductionVariantProps",
    "InstanceType",
    "InvocationHttpResponseCode",
    "InvocationsScalingProps",
    "Model",
    "ModelAttributes",
    "ModelData",
    "ModelDataConfig",
    "ModelProps",
    "ScalableInstanceCount",
    "ScalableInstanceCountProps",
]

publication.publish()
