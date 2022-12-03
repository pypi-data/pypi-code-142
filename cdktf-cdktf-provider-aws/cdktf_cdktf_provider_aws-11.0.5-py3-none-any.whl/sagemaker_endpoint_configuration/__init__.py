'''
# `aws_sagemaker_endpoint_configuration`

Refer to the Terraform Registory for docs: [`aws_sagemaker_endpoint_configuration`](https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration).
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

from .._jsii import *

import cdktf
import constructs


class SagemakerEndpointConfiguration(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.sagemakerEndpointConfiguration.SagemakerEndpointConfiguration",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration aws_sagemaker_endpoint_configuration}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        production_variants: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SagemakerEndpointConfigurationProductionVariants", typing.Dict[str, typing.Any]]]],
        async_inference_config: typing.Optional[typing.Union["SagemakerEndpointConfigurationAsyncInferenceConfig", typing.Dict[str, typing.Any]]] = None,
        data_capture_config: typing.Optional[typing.Union["SagemakerEndpointConfigurationDataCaptureConfig", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration aws_sagemaker_endpoint_configuration} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param production_variants: production_variants block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#production_variants SagemakerEndpointConfiguration#production_variants}
        :param async_inference_config: async_inference_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#async_inference_config SagemakerEndpointConfiguration#async_inference_config}
        :param data_capture_config: data_capture_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#data_capture_config SagemakerEndpointConfiguration#data_capture_config}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#id SagemakerEndpointConfiguration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param kms_key_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#kms_key_arn SagemakerEndpointConfiguration#kms_key_arn}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#name SagemakerEndpointConfiguration#name}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#tags SagemakerEndpointConfiguration#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#tags_all SagemakerEndpointConfiguration#tags_all}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                id_: builtins.str,
                *,
                production_variants: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[SagemakerEndpointConfigurationProductionVariants, typing.Dict[str, typing.Any]]]],
                async_inference_config: typing.Optional[typing.Union[SagemakerEndpointConfigurationAsyncInferenceConfig, typing.Dict[str, typing.Any]]] = None,
                data_capture_config: typing.Optional[typing.Union[SagemakerEndpointConfigurationDataCaptureConfig, typing.Dict[str, typing.Any]]] = None,
                id: typing.Optional[builtins.str] = None,
                kms_key_arn: typing.Optional[builtins.str] = None,
                name: typing.Optional[builtins.str] = None,
                tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
                count: typing.Optional[jsii.Number] = None,
                depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
                for_each: typing.Optional[cdktf.ITerraformIterator] = None,
                lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
                provider: typing.Optional[cdktf.TerraformProvider] = None,
                provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SagemakerEndpointConfigurationConfig(
            production_variants=production_variants,
            async_inference_config=async_inference_config,
            data_capture_config=data_capture_config,
            id=id,
            kms_key_arn=kms_key_arn,
            name=name,
            tags=tags,
            tags_all=tags_all,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAsyncInferenceConfig")
    def put_async_inference_config(
        self,
        *,
        output_config: typing.Union["SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfig", typing.Dict[str, typing.Any]],
        client_config: typing.Optional[typing.Union["SagemakerEndpointConfigurationAsyncInferenceConfigClientConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param output_config: output_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#output_config SagemakerEndpointConfiguration#output_config}
        :param client_config: client_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#client_config SagemakerEndpointConfiguration#client_config}
        '''
        value = SagemakerEndpointConfigurationAsyncInferenceConfig(
            output_config=output_config, client_config=client_config
        )

        return typing.cast(None, jsii.invoke(self, "putAsyncInferenceConfig", [value]))

    @jsii.member(jsii_name="putDataCaptureConfig")
    def put_data_capture_config(
        self,
        *,
        capture_options: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SagemakerEndpointConfigurationDataCaptureConfigCaptureOptions", typing.Dict[str, typing.Any]]]],
        destination_s3_uri: builtins.str,
        initial_sampling_percentage: jsii.Number,
        capture_content_type_header: typing.Optional[typing.Union["SagemakerEndpointConfigurationDataCaptureConfigCaptureContentTypeHeader", typing.Dict[str, typing.Any]]] = None,
        enable_capture: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param capture_options: capture_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#capture_options SagemakerEndpointConfiguration#capture_options}
        :param destination_s3_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#destination_s3_uri SagemakerEndpointConfiguration#destination_s3_uri}.
        :param initial_sampling_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#initial_sampling_percentage SagemakerEndpointConfiguration#initial_sampling_percentage}.
        :param capture_content_type_header: capture_content_type_header block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#capture_content_type_header SagemakerEndpointConfiguration#capture_content_type_header}
        :param enable_capture: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#enable_capture SagemakerEndpointConfiguration#enable_capture}.
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#kms_key_id SagemakerEndpointConfiguration#kms_key_id}.
        '''
        value = SagemakerEndpointConfigurationDataCaptureConfig(
            capture_options=capture_options,
            destination_s3_uri=destination_s3_uri,
            initial_sampling_percentage=initial_sampling_percentage,
            capture_content_type_header=capture_content_type_header,
            enable_capture=enable_capture,
            kms_key_id=kms_key_id,
        )

        return typing.cast(None, jsii.invoke(self, "putDataCaptureConfig", [value]))

    @jsii.member(jsii_name="putProductionVariants")
    def put_production_variants(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SagemakerEndpointConfigurationProductionVariants", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[SagemakerEndpointConfigurationProductionVariants, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putProductionVariants", [value]))

    @jsii.member(jsii_name="resetAsyncInferenceConfig")
    def reset_async_inference_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAsyncInferenceConfig", []))

    @jsii.member(jsii_name="resetDataCaptureConfig")
    def reset_data_capture_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataCaptureConfig", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetKmsKeyArn")
    def reset_kms_key_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKeyArn", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="asyncInferenceConfig")
    def async_inference_config(
        self,
    ) -> "SagemakerEndpointConfigurationAsyncInferenceConfigOutputReference":
        return typing.cast("SagemakerEndpointConfigurationAsyncInferenceConfigOutputReference", jsii.get(self, "asyncInferenceConfig"))

    @builtins.property
    @jsii.member(jsii_name="dataCaptureConfig")
    def data_capture_config(
        self,
    ) -> "SagemakerEndpointConfigurationDataCaptureConfigOutputReference":
        return typing.cast("SagemakerEndpointConfigurationDataCaptureConfigOutputReference", jsii.get(self, "dataCaptureConfig"))

    @builtins.property
    @jsii.member(jsii_name="productionVariants")
    def production_variants(
        self,
    ) -> "SagemakerEndpointConfigurationProductionVariantsList":
        return typing.cast("SagemakerEndpointConfigurationProductionVariantsList", jsii.get(self, "productionVariants"))

    @builtins.property
    @jsii.member(jsii_name="asyncInferenceConfigInput")
    def async_inference_config_input(
        self,
    ) -> typing.Optional["SagemakerEndpointConfigurationAsyncInferenceConfig"]:
        return typing.cast(typing.Optional["SagemakerEndpointConfigurationAsyncInferenceConfig"], jsii.get(self, "asyncInferenceConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="dataCaptureConfigInput")
    def data_capture_config_input(
        self,
    ) -> typing.Optional["SagemakerEndpointConfigurationDataCaptureConfig"]:
        return typing.cast(typing.Optional["SagemakerEndpointConfigurationDataCaptureConfig"], jsii.get(self, "dataCaptureConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArnInput")
    def kms_key_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyArnInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="productionVariantsInput")
    def production_variants_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SagemakerEndpointConfigurationProductionVariants"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SagemakerEndpointConfigurationProductionVariants"]]], jsii.get(self, "productionVariantsInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsAllInput")
    def tags_all_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsAllInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArn")
    def kms_key_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyArn"))

    @kms_key_arn.setter
    def kms_key_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyArn", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.Mapping[builtins.str, builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.Mapping[builtins.str, builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.sagemakerEndpointConfiguration.SagemakerEndpointConfigurationAsyncInferenceConfig",
    jsii_struct_bases=[],
    name_mapping={"output_config": "outputConfig", "client_config": "clientConfig"},
)
class SagemakerEndpointConfigurationAsyncInferenceConfig:
    def __init__(
        self,
        *,
        output_config: typing.Union["SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfig", typing.Dict[str, typing.Any]],
        client_config: typing.Optional[typing.Union["SagemakerEndpointConfigurationAsyncInferenceConfigClientConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param output_config: output_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#output_config SagemakerEndpointConfiguration#output_config}
        :param client_config: client_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#client_config SagemakerEndpointConfiguration#client_config}
        '''
        if isinstance(output_config, dict):
            output_config = SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfig(**output_config)
        if isinstance(client_config, dict):
            client_config = SagemakerEndpointConfigurationAsyncInferenceConfigClientConfig(**client_config)
        if __debug__:
            def stub(
                *,
                output_config: typing.Union[SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfig, typing.Dict[str, typing.Any]],
                client_config: typing.Optional[typing.Union[SagemakerEndpointConfigurationAsyncInferenceConfigClientConfig, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument output_config", value=output_config, expected_type=type_hints["output_config"])
            check_type(argname="argument client_config", value=client_config, expected_type=type_hints["client_config"])
        self._values: typing.Dict[str, typing.Any] = {
            "output_config": output_config,
        }
        if client_config is not None:
            self._values["client_config"] = client_config

    @builtins.property
    def output_config(
        self,
    ) -> "SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfig":
        '''output_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#output_config SagemakerEndpointConfiguration#output_config}
        '''
        result = self._values.get("output_config")
        assert result is not None, "Required property 'output_config' is missing"
        return typing.cast("SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfig", result)

    @builtins.property
    def client_config(
        self,
    ) -> typing.Optional["SagemakerEndpointConfigurationAsyncInferenceConfigClientConfig"]:
        '''client_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#client_config SagemakerEndpointConfiguration#client_config}
        '''
        result = self._values.get("client_config")
        return typing.cast(typing.Optional["SagemakerEndpointConfigurationAsyncInferenceConfigClientConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerEndpointConfigurationAsyncInferenceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.sagemakerEndpointConfiguration.SagemakerEndpointConfigurationAsyncInferenceConfigClientConfig",
    jsii_struct_bases=[],
    name_mapping={
        "max_concurrent_invocations_per_instance": "maxConcurrentInvocationsPerInstance",
    },
)
class SagemakerEndpointConfigurationAsyncInferenceConfigClientConfig:
    def __init__(
        self,
        *,
        max_concurrent_invocations_per_instance: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max_concurrent_invocations_per_instance: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#max_concurrent_invocations_per_instance SagemakerEndpointConfiguration#max_concurrent_invocations_per_instance}.
        '''
        if __debug__:
            def stub(
                *,
                max_concurrent_invocations_per_instance: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument max_concurrent_invocations_per_instance", value=max_concurrent_invocations_per_instance, expected_type=type_hints["max_concurrent_invocations_per_instance"])
        self._values: typing.Dict[str, typing.Any] = {}
        if max_concurrent_invocations_per_instance is not None:
            self._values["max_concurrent_invocations_per_instance"] = max_concurrent_invocations_per_instance

    @builtins.property
    def max_concurrent_invocations_per_instance(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#max_concurrent_invocations_per_instance SagemakerEndpointConfiguration#max_concurrent_invocations_per_instance}.'''
        result = self._values.get("max_concurrent_invocations_per_instance")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerEndpointConfigurationAsyncInferenceConfigClientConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerEndpointConfigurationAsyncInferenceConfigClientConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.sagemakerEndpointConfiguration.SagemakerEndpointConfigurationAsyncInferenceConfigClientConfigOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMaxConcurrentInvocationsPerInstance")
    def reset_max_concurrent_invocations_per_instance(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxConcurrentInvocationsPerInstance", []))

    @builtins.property
    @jsii.member(jsii_name="maxConcurrentInvocationsPerInstanceInput")
    def max_concurrent_invocations_per_instance_input(
        self,
    ) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxConcurrentInvocationsPerInstanceInput"))

    @builtins.property
    @jsii.member(jsii_name="maxConcurrentInvocationsPerInstance")
    def max_concurrent_invocations_per_instance(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxConcurrentInvocationsPerInstance"))

    @max_concurrent_invocations_per_instance.setter
    def max_concurrent_invocations_per_instance(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxConcurrentInvocationsPerInstance", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerEndpointConfigurationAsyncInferenceConfigClientConfig]:
        return typing.cast(typing.Optional[SagemakerEndpointConfigurationAsyncInferenceConfigClientConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerEndpointConfigurationAsyncInferenceConfigClientConfig],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[SagemakerEndpointConfigurationAsyncInferenceConfigClientConfig],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.sagemakerEndpointConfiguration.SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfig",
    jsii_struct_bases=[],
    name_mapping={
        "s3_output_path": "s3OutputPath",
        "kms_key_id": "kmsKeyId",
        "notification_config": "notificationConfig",
    },
)
class SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfig:
    def __init__(
        self,
        *,
        s3_output_path: builtins.str,
        kms_key_id: typing.Optional[builtins.str] = None,
        notification_config: typing.Optional[typing.Union["SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfigNotificationConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param s3_output_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#s3_output_path SagemakerEndpointConfiguration#s3_output_path}.
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#kms_key_id SagemakerEndpointConfiguration#kms_key_id}.
        :param notification_config: notification_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#notification_config SagemakerEndpointConfiguration#notification_config}
        '''
        if isinstance(notification_config, dict):
            notification_config = SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfigNotificationConfig(**notification_config)
        if __debug__:
            def stub(
                *,
                s3_output_path: builtins.str,
                kms_key_id: typing.Optional[builtins.str] = None,
                notification_config: typing.Optional[typing.Union[SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfigNotificationConfig, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument s3_output_path", value=s3_output_path, expected_type=type_hints["s3_output_path"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            check_type(argname="argument notification_config", value=notification_config, expected_type=type_hints["notification_config"])
        self._values: typing.Dict[str, typing.Any] = {
            "s3_output_path": s3_output_path,
        }
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if notification_config is not None:
            self._values["notification_config"] = notification_config

    @builtins.property
    def s3_output_path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#s3_output_path SagemakerEndpointConfiguration#s3_output_path}.'''
        result = self._values.get("s3_output_path")
        assert result is not None, "Required property 's3_output_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#kms_key_id SagemakerEndpointConfiguration#kms_key_id}.'''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def notification_config(
        self,
    ) -> typing.Optional["SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfigNotificationConfig"]:
        '''notification_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#notification_config SagemakerEndpointConfiguration#notification_config}
        '''
        result = self._values.get("notification_config")
        return typing.cast(typing.Optional["SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfigNotificationConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.sagemakerEndpointConfiguration.SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfigNotificationConfig",
    jsii_struct_bases=[],
    name_mapping={"error_topic": "errorTopic", "success_topic": "successTopic"},
)
class SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfigNotificationConfig:
    def __init__(
        self,
        *,
        error_topic: typing.Optional[builtins.str] = None,
        success_topic: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param error_topic: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#error_topic SagemakerEndpointConfiguration#error_topic}.
        :param success_topic: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#success_topic SagemakerEndpointConfiguration#success_topic}.
        '''
        if __debug__:
            def stub(
                *,
                error_topic: typing.Optional[builtins.str] = None,
                success_topic: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument error_topic", value=error_topic, expected_type=type_hints["error_topic"])
            check_type(argname="argument success_topic", value=success_topic, expected_type=type_hints["success_topic"])
        self._values: typing.Dict[str, typing.Any] = {}
        if error_topic is not None:
            self._values["error_topic"] = error_topic
        if success_topic is not None:
            self._values["success_topic"] = success_topic

    @builtins.property
    def error_topic(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#error_topic SagemakerEndpointConfiguration#error_topic}.'''
        result = self._values.get("error_topic")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def success_topic(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#success_topic SagemakerEndpointConfiguration#success_topic}.'''
        result = self._values.get("success_topic")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfigNotificationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfigNotificationConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.sagemakerEndpointConfiguration.SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfigNotificationConfigOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetErrorTopic")
    def reset_error_topic(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetErrorTopic", []))

    @jsii.member(jsii_name="resetSuccessTopic")
    def reset_success_topic(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSuccessTopic", []))

    @builtins.property
    @jsii.member(jsii_name="errorTopicInput")
    def error_topic_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "errorTopicInput"))

    @builtins.property
    @jsii.member(jsii_name="successTopicInput")
    def success_topic_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "successTopicInput"))

    @builtins.property
    @jsii.member(jsii_name="errorTopic")
    def error_topic(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "errorTopic"))

    @error_topic.setter
    def error_topic(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "errorTopic", value)

    @builtins.property
    @jsii.member(jsii_name="successTopic")
    def success_topic(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "successTopic"))

    @success_topic.setter
    def success_topic(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "successTopic", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfigNotificationConfig]:
        return typing.cast(typing.Optional[SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfigNotificationConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfigNotificationConfig],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfigNotificationConfig],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.sagemakerEndpointConfiguration.SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfigOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putNotificationConfig")
    def put_notification_config(
        self,
        *,
        error_topic: typing.Optional[builtins.str] = None,
        success_topic: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param error_topic: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#error_topic SagemakerEndpointConfiguration#error_topic}.
        :param success_topic: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#success_topic SagemakerEndpointConfiguration#success_topic}.
        '''
        value = SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfigNotificationConfig(
            error_topic=error_topic, success_topic=success_topic
        )

        return typing.cast(None, jsii.invoke(self, "putNotificationConfig", [value]))

    @jsii.member(jsii_name="resetKmsKeyId")
    def reset_kms_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKeyId", []))

    @jsii.member(jsii_name="resetNotificationConfig")
    def reset_notification_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotificationConfig", []))

    @builtins.property
    @jsii.member(jsii_name="notificationConfig")
    def notification_config(
        self,
    ) -> SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfigNotificationConfigOutputReference:
        return typing.cast(SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfigNotificationConfigOutputReference, jsii.get(self, "notificationConfig"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyIdInput")
    def kms_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="notificationConfigInput")
    def notification_config_input(
        self,
    ) -> typing.Optional[SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfigNotificationConfig]:
        return typing.cast(typing.Optional[SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfigNotificationConfig], jsii.get(self, "notificationConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="s3OutputPathInput")
    def s3_output_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3OutputPathInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="s3OutputPath")
    def s3_output_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "s3OutputPath"))

    @s3_output_path.setter
    def s3_output_path(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3OutputPath", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfig]:
        return typing.cast(typing.Optional[SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfig],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfig],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SagemakerEndpointConfigurationAsyncInferenceConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.sagemakerEndpointConfiguration.SagemakerEndpointConfigurationAsyncInferenceConfigOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putClientConfig")
    def put_client_config(
        self,
        *,
        max_concurrent_invocations_per_instance: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max_concurrent_invocations_per_instance: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#max_concurrent_invocations_per_instance SagemakerEndpointConfiguration#max_concurrent_invocations_per_instance}.
        '''
        value = SagemakerEndpointConfigurationAsyncInferenceConfigClientConfig(
            max_concurrent_invocations_per_instance=max_concurrent_invocations_per_instance,
        )

        return typing.cast(None, jsii.invoke(self, "putClientConfig", [value]))

    @jsii.member(jsii_name="putOutputConfig")
    def put_output_config(
        self,
        *,
        s3_output_path: builtins.str,
        kms_key_id: typing.Optional[builtins.str] = None,
        notification_config: typing.Optional[typing.Union[SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfigNotificationConfig, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param s3_output_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#s3_output_path SagemakerEndpointConfiguration#s3_output_path}.
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#kms_key_id SagemakerEndpointConfiguration#kms_key_id}.
        :param notification_config: notification_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#notification_config SagemakerEndpointConfiguration#notification_config}
        '''
        value = SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfig(
            s3_output_path=s3_output_path,
            kms_key_id=kms_key_id,
            notification_config=notification_config,
        )

        return typing.cast(None, jsii.invoke(self, "putOutputConfig", [value]))

    @jsii.member(jsii_name="resetClientConfig")
    def reset_client_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientConfig", []))

    @builtins.property
    @jsii.member(jsii_name="clientConfig")
    def client_config(
        self,
    ) -> SagemakerEndpointConfigurationAsyncInferenceConfigClientConfigOutputReference:
        return typing.cast(SagemakerEndpointConfigurationAsyncInferenceConfigClientConfigOutputReference, jsii.get(self, "clientConfig"))

    @builtins.property
    @jsii.member(jsii_name="outputConfig")
    def output_config(
        self,
    ) -> SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfigOutputReference:
        return typing.cast(SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfigOutputReference, jsii.get(self, "outputConfig"))

    @builtins.property
    @jsii.member(jsii_name="clientConfigInput")
    def client_config_input(
        self,
    ) -> typing.Optional[SagemakerEndpointConfigurationAsyncInferenceConfigClientConfig]:
        return typing.cast(typing.Optional[SagemakerEndpointConfigurationAsyncInferenceConfigClientConfig], jsii.get(self, "clientConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="outputConfigInput")
    def output_config_input(
        self,
    ) -> typing.Optional[SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfig]:
        return typing.cast(typing.Optional[SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfig], jsii.get(self, "outputConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerEndpointConfigurationAsyncInferenceConfig]:
        return typing.cast(typing.Optional[SagemakerEndpointConfigurationAsyncInferenceConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerEndpointConfigurationAsyncInferenceConfig],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[SagemakerEndpointConfigurationAsyncInferenceConfig],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.sagemakerEndpointConfiguration.SagemakerEndpointConfigurationConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "production_variants": "productionVariants",
        "async_inference_config": "asyncInferenceConfig",
        "data_capture_config": "dataCaptureConfig",
        "id": "id",
        "kms_key_arn": "kmsKeyArn",
        "name": "name",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class SagemakerEndpointConfigurationConfig(cdktf.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
        production_variants: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SagemakerEndpointConfigurationProductionVariants", typing.Dict[str, typing.Any]]]],
        async_inference_config: typing.Optional[typing.Union[SagemakerEndpointConfigurationAsyncInferenceConfig, typing.Dict[str, typing.Any]]] = None,
        data_capture_config: typing.Optional[typing.Union["SagemakerEndpointConfigurationDataCaptureConfig", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param production_variants: production_variants block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#production_variants SagemakerEndpointConfiguration#production_variants}
        :param async_inference_config: async_inference_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#async_inference_config SagemakerEndpointConfiguration#async_inference_config}
        :param data_capture_config: data_capture_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#data_capture_config SagemakerEndpointConfiguration#data_capture_config}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#id SagemakerEndpointConfiguration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param kms_key_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#kms_key_arn SagemakerEndpointConfiguration#kms_key_arn}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#name SagemakerEndpointConfiguration#name}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#tags SagemakerEndpointConfiguration#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#tags_all SagemakerEndpointConfiguration#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(async_inference_config, dict):
            async_inference_config = SagemakerEndpointConfigurationAsyncInferenceConfig(**async_inference_config)
        if isinstance(data_capture_config, dict):
            data_capture_config = SagemakerEndpointConfigurationDataCaptureConfig(**data_capture_config)
        if __debug__:
            def stub(
                *,
                connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
                count: typing.Optional[jsii.Number] = None,
                depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
                for_each: typing.Optional[cdktf.ITerraformIterator] = None,
                lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
                provider: typing.Optional[cdktf.TerraformProvider] = None,
                provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
                production_variants: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[SagemakerEndpointConfigurationProductionVariants, typing.Dict[str, typing.Any]]]],
                async_inference_config: typing.Optional[typing.Union[SagemakerEndpointConfigurationAsyncInferenceConfig, typing.Dict[str, typing.Any]]] = None,
                data_capture_config: typing.Optional[typing.Union[SagemakerEndpointConfigurationDataCaptureConfig, typing.Dict[str, typing.Any]]] = None,
                id: typing.Optional[builtins.str] = None,
                kms_key_arn: typing.Optional[builtins.str] = None,
                name: typing.Optional[builtins.str] = None,
                tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument production_variants", value=production_variants, expected_type=type_hints["production_variants"])
            check_type(argname="argument async_inference_config", value=async_inference_config, expected_type=type_hints["async_inference_config"])
            check_type(argname="argument data_capture_config", value=data_capture_config, expected_type=type_hints["data_capture_config"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[str, typing.Any] = {
            "production_variants": production_variants,
        }
        if connection is not None:
            self._values["connection"] = connection
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if provisioners is not None:
            self._values["provisioners"] = provisioners
        if async_inference_config is not None:
            self._values["async_inference_config"] = async_inference_config
        if data_capture_config is not None:
            self._values["data_capture_config"] = data_capture_config
        if id is not None:
            self._values["id"] = id
        if kms_key_arn is not None:
            self._values["kms_key_arn"] = kms_key_arn
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[cdktf.SSHProvisionerConnection, cdktf.WinrmProvisionerConnection]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[cdktf.SSHProvisionerConnection, cdktf.WinrmProvisionerConnection]], result)

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(self) -> typing.Optional[typing.List[cdktf.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[cdktf.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[cdktf.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[cdktf.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[cdktf.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[cdktf.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[cdktf.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[cdktf.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[typing.List[typing.Union[cdktf.FileProvisioner, cdktf.LocalExecProvisioner, cdktf.RemoteExecProvisioner]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provisioners")
        return typing.cast(typing.Optional[typing.List[typing.Union[cdktf.FileProvisioner, cdktf.LocalExecProvisioner, cdktf.RemoteExecProvisioner]]], result)

    @builtins.property
    def production_variants(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["SagemakerEndpointConfigurationProductionVariants"]]:
        '''production_variants block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#production_variants SagemakerEndpointConfiguration#production_variants}
        '''
        result = self._values.get("production_variants")
        assert result is not None, "Required property 'production_variants' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["SagemakerEndpointConfigurationProductionVariants"]], result)

    @builtins.property
    def async_inference_config(
        self,
    ) -> typing.Optional[SagemakerEndpointConfigurationAsyncInferenceConfig]:
        '''async_inference_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#async_inference_config SagemakerEndpointConfiguration#async_inference_config}
        '''
        result = self._values.get("async_inference_config")
        return typing.cast(typing.Optional[SagemakerEndpointConfigurationAsyncInferenceConfig], result)

    @builtins.property
    def data_capture_config(
        self,
    ) -> typing.Optional["SagemakerEndpointConfigurationDataCaptureConfig"]:
        '''data_capture_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#data_capture_config SagemakerEndpointConfiguration#data_capture_config}
        '''
        result = self._values.get("data_capture_config")
        return typing.cast(typing.Optional["SagemakerEndpointConfigurationDataCaptureConfig"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#id SagemakerEndpointConfiguration#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#kms_key_arn SagemakerEndpointConfiguration#kms_key_arn}.'''
        result = self._values.get("kms_key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#name SagemakerEndpointConfiguration#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#tags SagemakerEndpointConfiguration#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#tags_all SagemakerEndpointConfiguration#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerEndpointConfigurationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.sagemakerEndpointConfiguration.SagemakerEndpointConfigurationDataCaptureConfig",
    jsii_struct_bases=[],
    name_mapping={
        "capture_options": "captureOptions",
        "destination_s3_uri": "destinationS3Uri",
        "initial_sampling_percentage": "initialSamplingPercentage",
        "capture_content_type_header": "captureContentTypeHeader",
        "enable_capture": "enableCapture",
        "kms_key_id": "kmsKeyId",
    },
)
class SagemakerEndpointConfigurationDataCaptureConfig:
    def __init__(
        self,
        *,
        capture_options: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SagemakerEndpointConfigurationDataCaptureConfigCaptureOptions", typing.Dict[str, typing.Any]]]],
        destination_s3_uri: builtins.str,
        initial_sampling_percentage: jsii.Number,
        capture_content_type_header: typing.Optional[typing.Union["SagemakerEndpointConfigurationDataCaptureConfigCaptureContentTypeHeader", typing.Dict[str, typing.Any]]] = None,
        enable_capture: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param capture_options: capture_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#capture_options SagemakerEndpointConfiguration#capture_options}
        :param destination_s3_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#destination_s3_uri SagemakerEndpointConfiguration#destination_s3_uri}.
        :param initial_sampling_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#initial_sampling_percentage SagemakerEndpointConfiguration#initial_sampling_percentage}.
        :param capture_content_type_header: capture_content_type_header block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#capture_content_type_header SagemakerEndpointConfiguration#capture_content_type_header}
        :param enable_capture: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#enable_capture SagemakerEndpointConfiguration#enable_capture}.
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#kms_key_id SagemakerEndpointConfiguration#kms_key_id}.
        '''
        if isinstance(capture_content_type_header, dict):
            capture_content_type_header = SagemakerEndpointConfigurationDataCaptureConfigCaptureContentTypeHeader(**capture_content_type_header)
        if __debug__:
            def stub(
                *,
                capture_options: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[SagemakerEndpointConfigurationDataCaptureConfigCaptureOptions, typing.Dict[str, typing.Any]]]],
                destination_s3_uri: builtins.str,
                initial_sampling_percentage: jsii.Number,
                capture_content_type_header: typing.Optional[typing.Union[SagemakerEndpointConfigurationDataCaptureConfigCaptureContentTypeHeader, typing.Dict[str, typing.Any]]] = None,
                enable_capture: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                kms_key_id: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument capture_options", value=capture_options, expected_type=type_hints["capture_options"])
            check_type(argname="argument destination_s3_uri", value=destination_s3_uri, expected_type=type_hints["destination_s3_uri"])
            check_type(argname="argument initial_sampling_percentage", value=initial_sampling_percentage, expected_type=type_hints["initial_sampling_percentage"])
            check_type(argname="argument capture_content_type_header", value=capture_content_type_header, expected_type=type_hints["capture_content_type_header"])
            check_type(argname="argument enable_capture", value=enable_capture, expected_type=type_hints["enable_capture"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "capture_options": capture_options,
            "destination_s3_uri": destination_s3_uri,
            "initial_sampling_percentage": initial_sampling_percentage,
        }
        if capture_content_type_header is not None:
            self._values["capture_content_type_header"] = capture_content_type_header
        if enable_capture is not None:
            self._values["enable_capture"] = enable_capture
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id

    @builtins.property
    def capture_options(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["SagemakerEndpointConfigurationDataCaptureConfigCaptureOptions"]]:
        '''capture_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#capture_options SagemakerEndpointConfiguration#capture_options}
        '''
        result = self._values.get("capture_options")
        assert result is not None, "Required property 'capture_options' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["SagemakerEndpointConfigurationDataCaptureConfigCaptureOptions"]], result)

    @builtins.property
    def destination_s3_uri(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#destination_s3_uri SagemakerEndpointConfiguration#destination_s3_uri}.'''
        result = self._values.get("destination_s3_uri")
        assert result is not None, "Required property 'destination_s3_uri' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def initial_sampling_percentage(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#initial_sampling_percentage SagemakerEndpointConfiguration#initial_sampling_percentage}.'''
        result = self._values.get("initial_sampling_percentage")
        assert result is not None, "Required property 'initial_sampling_percentage' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def capture_content_type_header(
        self,
    ) -> typing.Optional["SagemakerEndpointConfigurationDataCaptureConfigCaptureContentTypeHeader"]:
        '''capture_content_type_header block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#capture_content_type_header SagemakerEndpointConfiguration#capture_content_type_header}
        '''
        result = self._values.get("capture_content_type_header")
        return typing.cast(typing.Optional["SagemakerEndpointConfigurationDataCaptureConfigCaptureContentTypeHeader"], result)

    @builtins.property
    def enable_capture(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#enable_capture SagemakerEndpointConfiguration#enable_capture}.'''
        result = self._values.get("enable_capture")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#kms_key_id SagemakerEndpointConfiguration#kms_key_id}.'''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerEndpointConfigurationDataCaptureConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.sagemakerEndpointConfiguration.SagemakerEndpointConfigurationDataCaptureConfigCaptureContentTypeHeader",
    jsii_struct_bases=[],
    name_mapping={
        "csv_content_types": "csvContentTypes",
        "json_content_types": "jsonContentTypes",
    },
)
class SagemakerEndpointConfigurationDataCaptureConfigCaptureContentTypeHeader:
    def __init__(
        self,
        *,
        csv_content_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        json_content_types: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param csv_content_types: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#csv_content_types SagemakerEndpointConfiguration#csv_content_types}.
        :param json_content_types: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#json_content_types SagemakerEndpointConfiguration#json_content_types}.
        '''
        if __debug__:
            def stub(
                *,
                csv_content_types: typing.Optional[typing.Sequence[builtins.str]] = None,
                json_content_types: typing.Optional[typing.Sequence[builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument csv_content_types", value=csv_content_types, expected_type=type_hints["csv_content_types"])
            check_type(argname="argument json_content_types", value=json_content_types, expected_type=type_hints["json_content_types"])
        self._values: typing.Dict[str, typing.Any] = {}
        if csv_content_types is not None:
            self._values["csv_content_types"] = csv_content_types
        if json_content_types is not None:
            self._values["json_content_types"] = json_content_types

    @builtins.property
    def csv_content_types(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#csv_content_types SagemakerEndpointConfiguration#csv_content_types}.'''
        result = self._values.get("csv_content_types")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def json_content_types(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#json_content_types SagemakerEndpointConfiguration#json_content_types}.'''
        result = self._values.get("json_content_types")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerEndpointConfigurationDataCaptureConfigCaptureContentTypeHeader(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerEndpointConfigurationDataCaptureConfigCaptureContentTypeHeaderOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.sagemakerEndpointConfiguration.SagemakerEndpointConfigurationDataCaptureConfigCaptureContentTypeHeaderOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCsvContentTypes")
    def reset_csv_content_types(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCsvContentTypes", []))

    @jsii.member(jsii_name="resetJsonContentTypes")
    def reset_json_content_types(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJsonContentTypes", []))

    @builtins.property
    @jsii.member(jsii_name="csvContentTypesInput")
    def csv_content_types_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "csvContentTypesInput"))

    @builtins.property
    @jsii.member(jsii_name="jsonContentTypesInput")
    def json_content_types_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "jsonContentTypesInput"))

    @builtins.property
    @jsii.member(jsii_name="csvContentTypes")
    def csv_content_types(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "csvContentTypes"))

    @csv_content_types.setter
    def csv_content_types(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "csvContentTypes", value)

    @builtins.property
    @jsii.member(jsii_name="jsonContentTypes")
    def json_content_types(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "jsonContentTypes"))

    @json_content_types.setter
    def json_content_types(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jsonContentTypes", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerEndpointConfigurationDataCaptureConfigCaptureContentTypeHeader]:
        return typing.cast(typing.Optional[SagemakerEndpointConfigurationDataCaptureConfigCaptureContentTypeHeader], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerEndpointConfigurationDataCaptureConfigCaptureContentTypeHeader],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[SagemakerEndpointConfigurationDataCaptureConfigCaptureContentTypeHeader],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.sagemakerEndpointConfiguration.SagemakerEndpointConfigurationDataCaptureConfigCaptureOptions",
    jsii_struct_bases=[],
    name_mapping={"capture_mode": "captureMode"},
)
class SagemakerEndpointConfigurationDataCaptureConfigCaptureOptions:
    def __init__(self, *, capture_mode: builtins.str) -> None:
        '''
        :param capture_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#capture_mode SagemakerEndpointConfiguration#capture_mode}.
        '''
        if __debug__:
            def stub(*, capture_mode: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument capture_mode", value=capture_mode, expected_type=type_hints["capture_mode"])
        self._values: typing.Dict[str, typing.Any] = {
            "capture_mode": capture_mode,
        }

    @builtins.property
    def capture_mode(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#capture_mode SagemakerEndpointConfiguration#capture_mode}.'''
        result = self._values.get("capture_mode")
        assert result is not None, "Required property 'capture_mode' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerEndpointConfigurationDataCaptureConfigCaptureOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerEndpointConfigurationDataCaptureConfigCaptureOptionsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.sagemakerEndpointConfiguration.SagemakerEndpointConfigurationDataCaptureConfigCaptureOptionsList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
                wraps_set: builtins.bool,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "SagemakerEndpointConfigurationDataCaptureConfigCaptureOptionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SagemakerEndpointConfigurationDataCaptureConfigCaptureOptionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            def stub(value: cdktf.IInterpolatingParent) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            def stub(value: builtins.bool) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SagemakerEndpointConfigurationDataCaptureConfigCaptureOptions]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SagemakerEndpointConfigurationDataCaptureConfigCaptureOptions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SagemakerEndpointConfigurationDataCaptureConfigCaptureOptions]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SagemakerEndpointConfigurationDataCaptureConfigCaptureOptions]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SagemakerEndpointConfigurationDataCaptureConfigCaptureOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.sagemakerEndpointConfiguration.SagemakerEndpointConfigurationDataCaptureConfigCaptureOptionsOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
                complex_object_index: jsii.Number,
                complex_object_is_from_set: builtins.bool,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="captureModeInput")
    def capture_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "captureModeInput"))

    @builtins.property
    @jsii.member(jsii_name="captureMode")
    def capture_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "captureMode"))

    @capture_mode.setter
    def capture_mode(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "captureMode", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SagemakerEndpointConfigurationDataCaptureConfigCaptureOptions, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SagemakerEndpointConfigurationDataCaptureConfigCaptureOptions, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SagemakerEndpointConfigurationDataCaptureConfigCaptureOptions, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[SagemakerEndpointConfigurationDataCaptureConfigCaptureOptions, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SagemakerEndpointConfigurationDataCaptureConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.sagemakerEndpointConfiguration.SagemakerEndpointConfigurationDataCaptureConfigOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCaptureContentTypeHeader")
    def put_capture_content_type_header(
        self,
        *,
        csv_content_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        json_content_types: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param csv_content_types: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#csv_content_types SagemakerEndpointConfiguration#csv_content_types}.
        :param json_content_types: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#json_content_types SagemakerEndpointConfiguration#json_content_types}.
        '''
        value = SagemakerEndpointConfigurationDataCaptureConfigCaptureContentTypeHeader(
            csv_content_types=csv_content_types, json_content_types=json_content_types
        )

        return typing.cast(None, jsii.invoke(self, "putCaptureContentTypeHeader", [value]))

    @jsii.member(jsii_name="putCaptureOptions")
    def put_capture_options(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[SagemakerEndpointConfigurationDataCaptureConfigCaptureOptions, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[SagemakerEndpointConfigurationDataCaptureConfigCaptureOptions, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCaptureOptions", [value]))

    @jsii.member(jsii_name="resetCaptureContentTypeHeader")
    def reset_capture_content_type_header(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCaptureContentTypeHeader", []))

    @jsii.member(jsii_name="resetEnableCapture")
    def reset_enable_capture(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableCapture", []))

    @jsii.member(jsii_name="resetKmsKeyId")
    def reset_kms_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKeyId", []))

    @builtins.property
    @jsii.member(jsii_name="captureContentTypeHeader")
    def capture_content_type_header(
        self,
    ) -> SagemakerEndpointConfigurationDataCaptureConfigCaptureContentTypeHeaderOutputReference:
        return typing.cast(SagemakerEndpointConfigurationDataCaptureConfigCaptureContentTypeHeaderOutputReference, jsii.get(self, "captureContentTypeHeader"))

    @builtins.property
    @jsii.member(jsii_name="captureOptions")
    def capture_options(
        self,
    ) -> SagemakerEndpointConfigurationDataCaptureConfigCaptureOptionsList:
        return typing.cast(SagemakerEndpointConfigurationDataCaptureConfigCaptureOptionsList, jsii.get(self, "captureOptions"))

    @builtins.property
    @jsii.member(jsii_name="captureContentTypeHeaderInput")
    def capture_content_type_header_input(
        self,
    ) -> typing.Optional[SagemakerEndpointConfigurationDataCaptureConfigCaptureContentTypeHeader]:
        return typing.cast(typing.Optional[SagemakerEndpointConfigurationDataCaptureConfigCaptureContentTypeHeader], jsii.get(self, "captureContentTypeHeaderInput"))

    @builtins.property
    @jsii.member(jsii_name="captureOptionsInput")
    def capture_options_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SagemakerEndpointConfigurationDataCaptureConfigCaptureOptions]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SagemakerEndpointConfigurationDataCaptureConfigCaptureOptions]]], jsii.get(self, "captureOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationS3UriInput")
    def destination_s3_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationS3UriInput"))

    @builtins.property
    @jsii.member(jsii_name="enableCaptureInput")
    def enable_capture_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableCaptureInput"))

    @builtins.property
    @jsii.member(jsii_name="initialSamplingPercentageInput")
    def initial_sampling_percentage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "initialSamplingPercentageInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyIdInput")
    def kms_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationS3Uri")
    def destination_s3_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destinationS3Uri"))

    @destination_s3_uri.setter
    def destination_s3_uri(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationS3Uri", value)

    @builtins.property
    @jsii.member(jsii_name="enableCapture")
    def enable_capture(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableCapture"))

    @enable_capture.setter
    def enable_capture(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableCapture", value)

    @builtins.property
    @jsii.member(jsii_name="initialSamplingPercentage")
    def initial_sampling_percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "initialSamplingPercentage"))

    @initial_sampling_percentage.setter
    def initial_sampling_percentage(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "initialSamplingPercentage", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerEndpointConfigurationDataCaptureConfig]:
        return typing.cast(typing.Optional[SagemakerEndpointConfigurationDataCaptureConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerEndpointConfigurationDataCaptureConfig],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[SagemakerEndpointConfigurationDataCaptureConfig],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.sagemakerEndpointConfiguration.SagemakerEndpointConfigurationProductionVariants",
    jsii_struct_bases=[],
    name_mapping={
        "model_name": "modelName",
        "accelerator_type": "acceleratorType",
        "initial_instance_count": "initialInstanceCount",
        "initial_variant_weight": "initialVariantWeight",
        "instance_type": "instanceType",
        "serverless_config": "serverlessConfig",
        "variant_name": "variantName",
    },
)
class SagemakerEndpointConfigurationProductionVariants:
    def __init__(
        self,
        *,
        model_name: builtins.str,
        accelerator_type: typing.Optional[builtins.str] = None,
        initial_instance_count: typing.Optional[jsii.Number] = None,
        initial_variant_weight: typing.Optional[jsii.Number] = None,
        instance_type: typing.Optional[builtins.str] = None,
        serverless_config: typing.Optional[typing.Union["SagemakerEndpointConfigurationProductionVariantsServerlessConfig", typing.Dict[str, typing.Any]]] = None,
        variant_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param model_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#model_name SagemakerEndpointConfiguration#model_name}.
        :param accelerator_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#accelerator_type SagemakerEndpointConfiguration#accelerator_type}.
        :param initial_instance_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#initial_instance_count SagemakerEndpointConfiguration#initial_instance_count}.
        :param initial_variant_weight: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#initial_variant_weight SagemakerEndpointConfiguration#initial_variant_weight}.
        :param instance_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#instance_type SagemakerEndpointConfiguration#instance_type}.
        :param serverless_config: serverless_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#serverless_config SagemakerEndpointConfiguration#serverless_config}
        :param variant_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#variant_name SagemakerEndpointConfiguration#variant_name}.
        '''
        if isinstance(serverless_config, dict):
            serverless_config = SagemakerEndpointConfigurationProductionVariantsServerlessConfig(**serverless_config)
        if __debug__:
            def stub(
                *,
                model_name: builtins.str,
                accelerator_type: typing.Optional[builtins.str] = None,
                initial_instance_count: typing.Optional[jsii.Number] = None,
                initial_variant_weight: typing.Optional[jsii.Number] = None,
                instance_type: typing.Optional[builtins.str] = None,
                serverless_config: typing.Optional[typing.Union[SagemakerEndpointConfigurationProductionVariantsServerlessConfig, typing.Dict[str, typing.Any]]] = None,
                variant_name: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument model_name", value=model_name, expected_type=type_hints["model_name"])
            check_type(argname="argument accelerator_type", value=accelerator_type, expected_type=type_hints["accelerator_type"])
            check_type(argname="argument initial_instance_count", value=initial_instance_count, expected_type=type_hints["initial_instance_count"])
            check_type(argname="argument initial_variant_weight", value=initial_variant_weight, expected_type=type_hints["initial_variant_weight"])
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            check_type(argname="argument serverless_config", value=serverless_config, expected_type=type_hints["serverless_config"])
            check_type(argname="argument variant_name", value=variant_name, expected_type=type_hints["variant_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "model_name": model_name,
        }
        if accelerator_type is not None:
            self._values["accelerator_type"] = accelerator_type
        if initial_instance_count is not None:
            self._values["initial_instance_count"] = initial_instance_count
        if initial_variant_weight is not None:
            self._values["initial_variant_weight"] = initial_variant_weight
        if instance_type is not None:
            self._values["instance_type"] = instance_type
        if serverless_config is not None:
            self._values["serverless_config"] = serverless_config
        if variant_name is not None:
            self._values["variant_name"] = variant_name

    @builtins.property
    def model_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#model_name SagemakerEndpointConfiguration#model_name}.'''
        result = self._values.get("model_name")
        assert result is not None, "Required property 'model_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def accelerator_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#accelerator_type SagemakerEndpointConfiguration#accelerator_type}.'''
        result = self._values.get("accelerator_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def initial_instance_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#initial_instance_count SagemakerEndpointConfiguration#initial_instance_count}.'''
        result = self._values.get("initial_instance_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def initial_variant_weight(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#initial_variant_weight SagemakerEndpointConfiguration#initial_variant_weight}.'''
        result = self._values.get("initial_variant_weight")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def instance_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#instance_type SagemakerEndpointConfiguration#instance_type}.'''
        result = self._values.get("instance_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def serverless_config(
        self,
    ) -> typing.Optional["SagemakerEndpointConfigurationProductionVariantsServerlessConfig"]:
        '''serverless_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#serverless_config SagemakerEndpointConfiguration#serverless_config}
        '''
        result = self._values.get("serverless_config")
        return typing.cast(typing.Optional["SagemakerEndpointConfigurationProductionVariantsServerlessConfig"], result)

    @builtins.property
    def variant_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#variant_name SagemakerEndpointConfiguration#variant_name}.'''
        result = self._values.get("variant_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerEndpointConfigurationProductionVariants(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerEndpointConfigurationProductionVariantsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.sagemakerEndpointConfiguration.SagemakerEndpointConfigurationProductionVariantsList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
                wraps_set: builtins.bool,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "SagemakerEndpointConfigurationProductionVariantsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SagemakerEndpointConfigurationProductionVariantsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            def stub(value: cdktf.IInterpolatingParent) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            def stub(value: builtins.bool) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SagemakerEndpointConfigurationProductionVariants]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SagemakerEndpointConfigurationProductionVariants]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SagemakerEndpointConfigurationProductionVariants]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SagemakerEndpointConfigurationProductionVariants]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SagemakerEndpointConfigurationProductionVariantsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.sagemakerEndpointConfiguration.SagemakerEndpointConfigurationProductionVariantsOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
                complex_object_index: jsii.Number,
                complex_object_is_from_set: builtins.bool,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putServerlessConfig")
    def put_serverless_config(
        self,
        *,
        max_concurrency: jsii.Number,
        memory_size_in_mb: jsii.Number,
    ) -> None:
        '''
        :param max_concurrency: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#max_concurrency SagemakerEndpointConfiguration#max_concurrency}.
        :param memory_size_in_mb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#memory_size_in_mb SagemakerEndpointConfiguration#memory_size_in_mb}.
        '''
        value = SagemakerEndpointConfigurationProductionVariantsServerlessConfig(
            max_concurrency=max_concurrency, memory_size_in_mb=memory_size_in_mb
        )

        return typing.cast(None, jsii.invoke(self, "putServerlessConfig", [value]))

    @jsii.member(jsii_name="resetAcceleratorType")
    def reset_accelerator_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAcceleratorType", []))

    @jsii.member(jsii_name="resetInitialInstanceCount")
    def reset_initial_instance_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInitialInstanceCount", []))

    @jsii.member(jsii_name="resetInitialVariantWeight")
    def reset_initial_variant_weight(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInitialVariantWeight", []))

    @jsii.member(jsii_name="resetInstanceType")
    def reset_instance_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceType", []))

    @jsii.member(jsii_name="resetServerlessConfig")
    def reset_serverless_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServerlessConfig", []))

    @jsii.member(jsii_name="resetVariantName")
    def reset_variant_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVariantName", []))

    @builtins.property
    @jsii.member(jsii_name="serverlessConfig")
    def serverless_config(
        self,
    ) -> "SagemakerEndpointConfigurationProductionVariantsServerlessConfigOutputReference":
        return typing.cast("SagemakerEndpointConfigurationProductionVariantsServerlessConfigOutputReference", jsii.get(self, "serverlessConfig"))

    @builtins.property
    @jsii.member(jsii_name="acceleratorTypeInput")
    def accelerator_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "acceleratorTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="initialInstanceCountInput")
    def initial_instance_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "initialInstanceCountInput"))

    @builtins.property
    @jsii.member(jsii_name="initialVariantWeightInput")
    def initial_variant_weight_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "initialVariantWeightInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceTypeInput")
    def instance_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="modelNameInput")
    def model_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modelNameInput"))

    @builtins.property
    @jsii.member(jsii_name="serverlessConfigInput")
    def serverless_config_input(
        self,
    ) -> typing.Optional["SagemakerEndpointConfigurationProductionVariantsServerlessConfig"]:
        return typing.cast(typing.Optional["SagemakerEndpointConfigurationProductionVariantsServerlessConfig"], jsii.get(self, "serverlessConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="variantNameInput")
    def variant_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "variantNameInput"))

    @builtins.property
    @jsii.member(jsii_name="acceleratorType")
    def accelerator_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "acceleratorType"))

    @accelerator_type.setter
    def accelerator_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "acceleratorType", value)

    @builtins.property
    @jsii.member(jsii_name="initialInstanceCount")
    def initial_instance_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "initialInstanceCount"))

    @initial_instance_count.setter
    def initial_instance_count(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "initialInstanceCount", value)

    @builtins.property
    @jsii.member(jsii_name="initialVariantWeight")
    def initial_variant_weight(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "initialVariantWeight"))

    @initial_variant_weight.setter
    def initial_variant_weight(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "initialVariantWeight", value)

    @builtins.property
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceType"))

    @instance_type.setter
    def instance_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceType", value)

    @builtins.property
    @jsii.member(jsii_name="modelName")
    def model_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "modelName"))

    @model_name.setter
    def model_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "modelName", value)

    @builtins.property
    @jsii.member(jsii_name="variantName")
    def variant_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "variantName"))

    @variant_name.setter
    def variant_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "variantName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SagemakerEndpointConfigurationProductionVariants, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SagemakerEndpointConfigurationProductionVariants, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SagemakerEndpointConfigurationProductionVariants, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[SagemakerEndpointConfigurationProductionVariants, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.sagemakerEndpointConfiguration.SagemakerEndpointConfigurationProductionVariantsServerlessConfig",
    jsii_struct_bases=[],
    name_mapping={
        "max_concurrency": "maxConcurrency",
        "memory_size_in_mb": "memorySizeInMb",
    },
)
class SagemakerEndpointConfigurationProductionVariantsServerlessConfig:
    def __init__(
        self,
        *,
        max_concurrency: jsii.Number,
        memory_size_in_mb: jsii.Number,
    ) -> None:
        '''
        :param max_concurrency: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#max_concurrency SagemakerEndpointConfiguration#max_concurrency}.
        :param memory_size_in_mb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#memory_size_in_mb SagemakerEndpointConfiguration#memory_size_in_mb}.
        '''
        if __debug__:
            def stub(
                *,
                max_concurrency: jsii.Number,
                memory_size_in_mb: jsii.Number,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument max_concurrency", value=max_concurrency, expected_type=type_hints["max_concurrency"])
            check_type(argname="argument memory_size_in_mb", value=memory_size_in_mb, expected_type=type_hints["memory_size_in_mb"])
        self._values: typing.Dict[str, typing.Any] = {
            "max_concurrency": max_concurrency,
            "memory_size_in_mb": memory_size_in_mb,
        }

    @builtins.property
    def max_concurrency(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#max_concurrency SagemakerEndpointConfiguration#max_concurrency}.'''
        result = self._values.get("max_concurrency")
        assert result is not None, "Required property 'max_concurrency' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def memory_size_in_mb(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#memory_size_in_mb SagemakerEndpointConfiguration#memory_size_in_mb}.'''
        result = self._values.get("memory_size_in_mb")
        assert result is not None, "Required property 'memory_size_in_mb' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerEndpointConfigurationProductionVariantsServerlessConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerEndpointConfigurationProductionVariantsServerlessConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.sagemakerEndpointConfiguration.SagemakerEndpointConfigurationProductionVariantsServerlessConfigOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="maxConcurrencyInput")
    def max_concurrency_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxConcurrencyInput"))

    @builtins.property
    @jsii.member(jsii_name="memorySizeInMbInput")
    def memory_size_in_mb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "memorySizeInMbInput"))

    @builtins.property
    @jsii.member(jsii_name="maxConcurrency")
    def max_concurrency(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxConcurrency"))

    @max_concurrency.setter
    def max_concurrency(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxConcurrency", value)

    @builtins.property
    @jsii.member(jsii_name="memorySizeInMb")
    def memory_size_in_mb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "memorySizeInMb"))

    @memory_size_in_mb.setter
    def memory_size_in_mb(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memorySizeInMb", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerEndpointConfigurationProductionVariantsServerlessConfig]:
        return typing.cast(typing.Optional[SagemakerEndpointConfigurationProductionVariantsServerlessConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerEndpointConfigurationProductionVariantsServerlessConfig],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[SagemakerEndpointConfigurationProductionVariantsServerlessConfig],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "SagemakerEndpointConfiguration",
    "SagemakerEndpointConfigurationAsyncInferenceConfig",
    "SagemakerEndpointConfigurationAsyncInferenceConfigClientConfig",
    "SagemakerEndpointConfigurationAsyncInferenceConfigClientConfigOutputReference",
    "SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfig",
    "SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfigNotificationConfig",
    "SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfigNotificationConfigOutputReference",
    "SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfigOutputReference",
    "SagemakerEndpointConfigurationAsyncInferenceConfigOutputReference",
    "SagemakerEndpointConfigurationConfig",
    "SagemakerEndpointConfigurationDataCaptureConfig",
    "SagemakerEndpointConfigurationDataCaptureConfigCaptureContentTypeHeader",
    "SagemakerEndpointConfigurationDataCaptureConfigCaptureContentTypeHeaderOutputReference",
    "SagemakerEndpointConfigurationDataCaptureConfigCaptureOptions",
    "SagemakerEndpointConfigurationDataCaptureConfigCaptureOptionsList",
    "SagemakerEndpointConfigurationDataCaptureConfigCaptureOptionsOutputReference",
    "SagemakerEndpointConfigurationDataCaptureConfigOutputReference",
    "SagemakerEndpointConfigurationProductionVariants",
    "SagemakerEndpointConfigurationProductionVariantsList",
    "SagemakerEndpointConfigurationProductionVariantsOutputReference",
    "SagemakerEndpointConfigurationProductionVariantsServerlessConfig",
    "SagemakerEndpointConfigurationProductionVariantsServerlessConfigOutputReference",
]

publication.publish()
