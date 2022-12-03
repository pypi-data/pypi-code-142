'''
# `aws_lambda_function_event_invoke_config`

Refer to the Terraform Registory for docs: [`aws_lambda_function_event_invoke_config`](https://www.terraform.io/docs/providers/aws/r/lambda_function_event_invoke_config).
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


class LambdaFunctionEventInvokeConfig(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lambdaFunctionEventInvokeConfig.LambdaFunctionEventInvokeConfig",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/lambda_function_event_invoke_config aws_lambda_function_event_invoke_config}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        function_name: builtins.str,
        destination_config: typing.Optional[typing.Union["LambdaFunctionEventInvokeConfigDestinationConfig", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        maximum_event_age_in_seconds: typing.Optional[jsii.Number] = None,
        maximum_retry_attempts: typing.Optional[jsii.Number] = None,
        qualifier: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/lambda_function_event_invoke_config aws_lambda_function_event_invoke_config} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param function_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function_event_invoke_config#function_name LambdaFunctionEventInvokeConfig#function_name}.
        :param destination_config: destination_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function_event_invoke_config#destination_config LambdaFunctionEventInvokeConfig#destination_config}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function_event_invoke_config#id LambdaFunctionEventInvokeConfig#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param maximum_event_age_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function_event_invoke_config#maximum_event_age_in_seconds LambdaFunctionEventInvokeConfig#maximum_event_age_in_seconds}.
        :param maximum_retry_attempts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function_event_invoke_config#maximum_retry_attempts LambdaFunctionEventInvokeConfig#maximum_retry_attempts}.
        :param qualifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function_event_invoke_config#qualifier LambdaFunctionEventInvokeConfig#qualifier}.
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
                function_name: builtins.str,
                destination_config: typing.Optional[typing.Union[LambdaFunctionEventInvokeConfigDestinationConfig, typing.Dict[str, typing.Any]]] = None,
                id: typing.Optional[builtins.str] = None,
                maximum_event_age_in_seconds: typing.Optional[jsii.Number] = None,
                maximum_retry_attempts: typing.Optional[jsii.Number] = None,
                qualifier: typing.Optional[builtins.str] = None,
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
        config = LambdaFunctionEventInvokeConfigConfig(
            function_name=function_name,
            destination_config=destination_config,
            id=id,
            maximum_event_age_in_seconds=maximum_event_age_in_seconds,
            maximum_retry_attempts=maximum_retry_attempts,
            qualifier=qualifier,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putDestinationConfig")
    def put_destination_config(
        self,
        *,
        on_failure: typing.Optional[typing.Union["LambdaFunctionEventInvokeConfigDestinationConfigOnFailure", typing.Dict[str, typing.Any]]] = None,
        on_success: typing.Optional[typing.Union["LambdaFunctionEventInvokeConfigDestinationConfigOnSuccess", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param on_failure: on_failure block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function_event_invoke_config#on_failure LambdaFunctionEventInvokeConfig#on_failure}
        :param on_success: on_success block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function_event_invoke_config#on_success LambdaFunctionEventInvokeConfig#on_success}
        '''
        value = LambdaFunctionEventInvokeConfigDestinationConfig(
            on_failure=on_failure, on_success=on_success
        )

        return typing.cast(None, jsii.invoke(self, "putDestinationConfig", [value]))

    @jsii.member(jsii_name="resetDestinationConfig")
    def reset_destination_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestinationConfig", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMaximumEventAgeInSeconds")
    def reset_maximum_event_age_in_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaximumEventAgeInSeconds", []))

    @jsii.member(jsii_name="resetMaximumRetryAttempts")
    def reset_maximum_retry_attempts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaximumRetryAttempts", []))

    @jsii.member(jsii_name="resetQualifier")
    def reset_qualifier(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQualifier", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="destinationConfig")
    def destination_config(
        self,
    ) -> "LambdaFunctionEventInvokeConfigDestinationConfigOutputReference":
        return typing.cast("LambdaFunctionEventInvokeConfigDestinationConfigOutputReference", jsii.get(self, "destinationConfig"))

    @builtins.property
    @jsii.member(jsii_name="destinationConfigInput")
    def destination_config_input(
        self,
    ) -> typing.Optional["LambdaFunctionEventInvokeConfigDestinationConfig"]:
        return typing.cast(typing.Optional["LambdaFunctionEventInvokeConfigDestinationConfig"], jsii.get(self, "destinationConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="functionNameInput")
    def function_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "functionNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="maximumEventAgeInSecondsInput")
    def maximum_event_age_in_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maximumEventAgeInSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="maximumRetryAttemptsInput")
    def maximum_retry_attempts_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maximumRetryAttemptsInput"))

    @builtins.property
    @jsii.member(jsii_name="qualifierInput")
    def qualifier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "qualifierInput"))

    @builtins.property
    @jsii.member(jsii_name="functionName")
    def function_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "functionName"))

    @function_name.setter
    def function_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "functionName", value)

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
    @jsii.member(jsii_name="maximumEventAgeInSeconds")
    def maximum_event_age_in_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maximumEventAgeInSeconds"))

    @maximum_event_age_in_seconds.setter
    def maximum_event_age_in_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maximumEventAgeInSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="maximumRetryAttempts")
    def maximum_retry_attempts(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maximumRetryAttempts"))

    @maximum_retry_attempts.setter
    def maximum_retry_attempts(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maximumRetryAttempts", value)

    @builtins.property
    @jsii.member(jsii_name="qualifier")
    def qualifier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "qualifier"))

    @qualifier.setter
    def qualifier(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "qualifier", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lambdaFunctionEventInvokeConfig.LambdaFunctionEventInvokeConfigConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "function_name": "functionName",
        "destination_config": "destinationConfig",
        "id": "id",
        "maximum_event_age_in_seconds": "maximumEventAgeInSeconds",
        "maximum_retry_attempts": "maximumRetryAttempts",
        "qualifier": "qualifier",
    },
)
class LambdaFunctionEventInvokeConfigConfig(cdktf.TerraformMetaArguments):
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
        function_name: builtins.str,
        destination_config: typing.Optional[typing.Union["LambdaFunctionEventInvokeConfigDestinationConfig", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        maximum_event_age_in_seconds: typing.Optional[jsii.Number] = None,
        maximum_retry_attempts: typing.Optional[jsii.Number] = None,
        qualifier: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param function_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function_event_invoke_config#function_name LambdaFunctionEventInvokeConfig#function_name}.
        :param destination_config: destination_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function_event_invoke_config#destination_config LambdaFunctionEventInvokeConfig#destination_config}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function_event_invoke_config#id LambdaFunctionEventInvokeConfig#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param maximum_event_age_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function_event_invoke_config#maximum_event_age_in_seconds LambdaFunctionEventInvokeConfig#maximum_event_age_in_seconds}.
        :param maximum_retry_attempts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function_event_invoke_config#maximum_retry_attempts LambdaFunctionEventInvokeConfig#maximum_retry_attempts}.
        :param qualifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function_event_invoke_config#qualifier LambdaFunctionEventInvokeConfig#qualifier}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(destination_config, dict):
            destination_config = LambdaFunctionEventInvokeConfigDestinationConfig(**destination_config)
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
                function_name: builtins.str,
                destination_config: typing.Optional[typing.Union[LambdaFunctionEventInvokeConfigDestinationConfig, typing.Dict[str, typing.Any]]] = None,
                id: typing.Optional[builtins.str] = None,
                maximum_event_age_in_seconds: typing.Optional[jsii.Number] = None,
                maximum_retry_attempts: typing.Optional[jsii.Number] = None,
                qualifier: typing.Optional[builtins.str] = None,
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
            check_type(argname="argument function_name", value=function_name, expected_type=type_hints["function_name"])
            check_type(argname="argument destination_config", value=destination_config, expected_type=type_hints["destination_config"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument maximum_event_age_in_seconds", value=maximum_event_age_in_seconds, expected_type=type_hints["maximum_event_age_in_seconds"])
            check_type(argname="argument maximum_retry_attempts", value=maximum_retry_attempts, expected_type=type_hints["maximum_retry_attempts"])
            check_type(argname="argument qualifier", value=qualifier, expected_type=type_hints["qualifier"])
        self._values: typing.Dict[str, typing.Any] = {
            "function_name": function_name,
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
        if destination_config is not None:
            self._values["destination_config"] = destination_config
        if id is not None:
            self._values["id"] = id
        if maximum_event_age_in_seconds is not None:
            self._values["maximum_event_age_in_seconds"] = maximum_event_age_in_seconds
        if maximum_retry_attempts is not None:
            self._values["maximum_retry_attempts"] = maximum_retry_attempts
        if qualifier is not None:
            self._values["qualifier"] = qualifier

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
    def function_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function_event_invoke_config#function_name LambdaFunctionEventInvokeConfig#function_name}.'''
        result = self._values.get("function_name")
        assert result is not None, "Required property 'function_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def destination_config(
        self,
    ) -> typing.Optional["LambdaFunctionEventInvokeConfigDestinationConfig"]:
        '''destination_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function_event_invoke_config#destination_config LambdaFunctionEventInvokeConfig#destination_config}
        '''
        result = self._values.get("destination_config")
        return typing.cast(typing.Optional["LambdaFunctionEventInvokeConfigDestinationConfig"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function_event_invoke_config#id LambdaFunctionEventInvokeConfig#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def maximum_event_age_in_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function_event_invoke_config#maximum_event_age_in_seconds LambdaFunctionEventInvokeConfig#maximum_event_age_in_seconds}.'''
        result = self._values.get("maximum_event_age_in_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def maximum_retry_attempts(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function_event_invoke_config#maximum_retry_attempts LambdaFunctionEventInvokeConfig#maximum_retry_attempts}.'''
        result = self._values.get("maximum_retry_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def qualifier(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function_event_invoke_config#qualifier LambdaFunctionEventInvokeConfig#qualifier}.'''
        result = self._values.get("qualifier")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LambdaFunctionEventInvokeConfigConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lambdaFunctionEventInvokeConfig.LambdaFunctionEventInvokeConfigDestinationConfig",
    jsii_struct_bases=[],
    name_mapping={"on_failure": "onFailure", "on_success": "onSuccess"},
)
class LambdaFunctionEventInvokeConfigDestinationConfig:
    def __init__(
        self,
        *,
        on_failure: typing.Optional[typing.Union["LambdaFunctionEventInvokeConfigDestinationConfigOnFailure", typing.Dict[str, typing.Any]]] = None,
        on_success: typing.Optional[typing.Union["LambdaFunctionEventInvokeConfigDestinationConfigOnSuccess", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param on_failure: on_failure block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function_event_invoke_config#on_failure LambdaFunctionEventInvokeConfig#on_failure}
        :param on_success: on_success block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function_event_invoke_config#on_success LambdaFunctionEventInvokeConfig#on_success}
        '''
        if isinstance(on_failure, dict):
            on_failure = LambdaFunctionEventInvokeConfigDestinationConfigOnFailure(**on_failure)
        if isinstance(on_success, dict):
            on_success = LambdaFunctionEventInvokeConfigDestinationConfigOnSuccess(**on_success)
        if __debug__:
            def stub(
                *,
                on_failure: typing.Optional[typing.Union[LambdaFunctionEventInvokeConfigDestinationConfigOnFailure, typing.Dict[str, typing.Any]]] = None,
                on_success: typing.Optional[typing.Union[LambdaFunctionEventInvokeConfigDestinationConfigOnSuccess, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument on_failure", value=on_failure, expected_type=type_hints["on_failure"])
            check_type(argname="argument on_success", value=on_success, expected_type=type_hints["on_success"])
        self._values: typing.Dict[str, typing.Any] = {}
        if on_failure is not None:
            self._values["on_failure"] = on_failure
        if on_success is not None:
            self._values["on_success"] = on_success

    @builtins.property
    def on_failure(
        self,
    ) -> typing.Optional["LambdaFunctionEventInvokeConfigDestinationConfigOnFailure"]:
        '''on_failure block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function_event_invoke_config#on_failure LambdaFunctionEventInvokeConfig#on_failure}
        '''
        result = self._values.get("on_failure")
        return typing.cast(typing.Optional["LambdaFunctionEventInvokeConfigDestinationConfigOnFailure"], result)

    @builtins.property
    def on_success(
        self,
    ) -> typing.Optional["LambdaFunctionEventInvokeConfigDestinationConfigOnSuccess"]:
        '''on_success block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function_event_invoke_config#on_success LambdaFunctionEventInvokeConfig#on_success}
        '''
        result = self._values.get("on_success")
        return typing.cast(typing.Optional["LambdaFunctionEventInvokeConfigDestinationConfigOnSuccess"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LambdaFunctionEventInvokeConfigDestinationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lambdaFunctionEventInvokeConfig.LambdaFunctionEventInvokeConfigDestinationConfigOnFailure",
    jsii_struct_bases=[],
    name_mapping={"destination": "destination"},
)
class LambdaFunctionEventInvokeConfigDestinationConfigOnFailure:
    def __init__(self, *, destination: builtins.str) -> None:
        '''
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function_event_invoke_config#destination LambdaFunctionEventInvokeConfig#destination}.
        '''
        if __debug__:
            def stub(*, destination: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
        self._values: typing.Dict[str, typing.Any] = {
            "destination": destination,
        }

    @builtins.property
    def destination(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function_event_invoke_config#destination LambdaFunctionEventInvokeConfig#destination}.'''
        result = self._values.get("destination")
        assert result is not None, "Required property 'destination' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LambdaFunctionEventInvokeConfigDestinationConfigOnFailure(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LambdaFunctionEventInvokeConfigDestinationConfigOnFailureOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lambdaFunctionEventInvokeConfig.LambdaFunctionEventInvokeConfigDestinationConfigOnFailureOutputReference",
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
    @jsii.member(jsii_name="destinationInput")
    def destination_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationInput"))

    @builtins.property
    @jsii.member(jsii_name="destination")
    def destination(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destination"))

    @destination.setter
    def destination(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destination", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LambdaFunctionEventInvokeConfigDestinationConfigOnFailure]:
        return typing.cast(typing.Optional[LambdaFunctionEventInvokeConfigDestinationConfigOnFailure], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LambdaFunctionEventInvokeConfigDestinationConfigOnFailure],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[LambdaFunctionEventInvokeConfigDestinationConfigOnFailure],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lambdaFunctionEventInvokeConfig.LambdaFunctionEventInvokeConfigDestinationConfigOnSuccess",
    jsii_struct_bases=[],
    name_mapping={"destination": "destination"},
)
class LambdaFunctionEventInvokeConfigDestinationConfigOnSuccess:
    def __init__(self, *, destination: builtins.str) -> None:
        '''
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function_event_invoke_config#destination LambdaFunctionEventInvokeConfig#destination}.
        '''
        if __debug__:
            def stub(*, destination: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
        self._values: typing.Dict[str, typing.Any] = {
            "destination": destination,
        }

    @builtins.property
    def destination(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function_event_invoke_config#destination LambdaFunctionEventInvokeConfig#destination}.'''
        result = self._values.get("destination")
        assert result is not None, "Required property 'destination' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LambdaFunctionEventInvokeConfigDestinationConfigOnSuccess(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LambdaFunctionEventInvokeConfigDestinationConfigOnSuccessOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lambdaFunctionEventInvokeConfig.LambdaFunctionEventInvokeConfigDestinationConfigOnSuccessOutputReference",
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
    @jsii.member(jsii_name="destinationInput")
    def destination_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationInput"))

    @builtins.property
    @jsii.member(jsii_name="destination")
    def destination(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destination"))

    @destination.setter
    def destination(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destination", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LambdaFunctionEventInvokeConfigDestinationConfigOnSuccess]:
        return typing.cast(typing.Optional[LambdaFunctionEventInvokeConfigDestinationConfigOnSuccess], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LambdaFunctionEventInvokeConfigDestinationConfigOnSuccess],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[LambdaFunctionEventInvokeConfigDestinationConfigOnSuccess],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LambdaFunctionEventInvokeConfigDestinationConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lambdaFunctionEventInvokeConfig.LambdaFunctionEventInvokeConfigDestinationConfigOutputReference",
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

    @jsii.member(jsii_name="putOnFailure")
    def put_on_failure(self, *, destination: builtins.str) -> None:
        '''
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function_event_invoke_config#destination LambdaFunctionEventInvokeConfig#destination}.
        '''
        value = LambdaFunctionEventInvokeConfigDestinationConfigOnFailure(
            destination=destination
        )

        return typing.cast(None, jsii.invoke(self, "putOnFailure", [value]))

    @jsii.member(jsii_name="putOnSuccess")
    def put_on_success(self, *, destination: builtins.str) -> None:
        '''
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function_event_invoke_config#destination LambdaFunctionEventInvokeConfig#destination}.
        '''
        value = LambdaFunctionEventInvokeConfigDestinationConfigOnSuccess(
            destination=destination
        )

        return typing.cast(None, jsii.invoke(self, "putOnSuccess", [value]))

    @jsii.member(jsii_name="resetOnFailure")
    def reset_on_failure(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOnFailure", []))

    @jsii.member(jsii_name="resetOnSuccess")
    def reset_on_success(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOnSuccess", []))

    @builtins.property
    @jsii.member(jsii_name="onFailure")
    def on_failure(
        self,
    ) -> LambdaFunctionEventInvokeConfigDestinationConfigOnFailureOutputReference:
        return typing.cast(LambdaFunctionEventInvokeConfigDestinationConfigOnFailureOutputReference, jsii.get(self, "onFailure"))

    @builtins.property
    @jsii.member(jsii_name="onSuccess")
    def on_success(
        self,
    ) -> LambdaFunctionEventInvokeConfigDestinationConfigOnSuccessOutputReference:
        return typing.cast(LambdaFunctionEventInvokeConfigDestinationConfigOnSuccessOutputReference, jsii.get(self, "onSuccess"))

    @builtins.property
    @jsii.member(jsii_name="onFailureInput")
    def on_failure_input(
        self,
    ) -> typing.Optional[LambdaFunctionEventInvokeConfigDestinationConfigOnFailure]:
        return typing.cast(typing.Optional[LambdaFunctionEventInvokeConfigDestinationConfigOnFailure], jsii.get(self, "onFailureInput"))

    @builtins.property
    @jsii.member(jsii_name="onSuccessInput")
    def on_success_input(
        self,
    ) -> typing.Optional[LambdaFunctionEventInvokeConfigDestinationConfigOnSuccess]:
        return typing.cast(typing.Optional[LambdaFunctionEventInvokeConfigDestinationConfigOnSuccess], jsii.get(self, "onSuccessInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LambdaFunctionEventInvokeConfigDestinationConfig]:
        return typing.cast(typing.Optional[LambdaFunctionEventInvokeConfigDestinationConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LambdaFunctionEventInvokeConfigDestinationConfig],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[LambdaFunctionEventInvokeConfigDestinationConfig],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "LambdaFunctionEventInvokeConfig",
    "LambdaFunctionEventInvokeConfigConfig",
    "LambdaFunctionEventInvokeConfigDestinationConfig",
    "LambdaFunctionEventInvokeConfigDestinationConfigOnFailure",
    "LambdaFunctionEventInvokeConfigDestinationConfigOnFailureOutputReference",
    "LambdaFunctionEventInvokeConfigDestinationConfigOnSuccess",
    "LambdaFunctionEventInvokeConfigDestinationConfigOnSuccessOutputReference",
    "LambdaFunctionEventInvokeConfigDestinationConfigOutputReference",
]

publication.publish()
