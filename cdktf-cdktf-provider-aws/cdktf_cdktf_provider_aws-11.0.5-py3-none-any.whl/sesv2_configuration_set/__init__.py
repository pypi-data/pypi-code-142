'''
# `aws_sesv2_configuration_set`

Refer to the Terraform Registory for docs: [`aws_sesv2_configuration_set`](https://www.terraform.io/docs/providers/aws/r/sesv2_configuration_set).
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


class Sesv2ConfigurationSet(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.sesv2ConfigurationSet.Sesv2ConfigurationSet",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/sesv2_configuration_set aws_sesv2_configuration_set}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        configuration_set_name: builtins.str,
        delivery_options: typing.Optional[typing.Union["Sesv2ConfigurationSetDeliveryOptions", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        reputation_options: typing.Optional[typing.Union["Sesv2ConfigurationSetReputationOptions", typing.Dict[str, typing.Any]]] = None,
        sending_options: typing.Optional[typing.Union["Sesv2ConfigurationSetSendingOptions", typing.Dict[str, typing.Any]]] = None,
        suppression_options: typing.Optional[typing.Union["Sesv2ConfigurationSetSuppressionOptions", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tracking_options: typing.Optional[typing.Union["Sesv2ConfigurationSetTrackingOptions", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/sesv2_configuration_set aws_sesv2_configuration_set} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param configuration_set_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sesv2_configuration_set#configuration_set_name Sesv2ConfigurationSet#configuration_set_name}.
        :param delivery_options: delivery_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sesv2_configuration_set#delivery_options Sesv2ConfigurationSet#delivery_options}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sesv2_configuration_set#id Sesv2ConfigurationSet#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param reputation_options: reputation_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sesv2_configuration_set#reputation_options Sesv2ConfigurationSet#reputation_options}
        :param sending_options: sending_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sesv2_configuration_set#sending_options Sesv2ConfigurationSet#sending_options}
        :param suppression_options: suppression_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sesv2_configuration_set#suppression_options Sesv2ConfigurationSet#suppression_options}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sesv2_configuration_set#tags Sesv2ConfigurationSet#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sesv2_configuration_set#tags_all Sesv2ConfigurationSet#tags_all}.
        :param tracking_options: tracking_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sesv2_configuration_set#tracking_options Sesv2ConfigurationSet#tracking_options}
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
                configuration_set_name: builtins.str,
                delivery_options: typing.Optional[typing.Union[Sesv2ConfigurationSetDeliveryOptions, typing.Dict[str, typing.Any]]] = None,
                id: typing.Optional[builtins.str] = None,
                reputation_options: typing.Optional[typing.Union[Sesv2ConfigurationSetReputationOptions, typing.Dict[str, typing.Any]]] = None,
                sending_options: typing.Optional[typing.Union[Sesv2ConfigurationSetSendingOptions, typing.Dict[str, typing.Any]]] = None,
                suppression_options: typing.Optional[typing.Union[Sesv2ConfigurationSetSuppressionOptions, typing.Dict[str, typing.Any]]] = None,
                tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                tracking_options: typing.Optional[typing.Union[Sesv2ConfigurationSetTrackingOptions, typing.Dict[str, typing.Any]]] = None,
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
        config = Sesv2ConfigurationSetConfig(
            configuration_set_name=configuration_set_name,
            delivery_options=delivery_options,
            id=id,
            reputation_options=reputation_options,
            sending_options=sending_options,
            suppression_options=suppression_options,
            tags=tags,
            tags_all=tags_all,
            tracking_options=tracking_options,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putDeliveryOptions")
    def put_delivery_options(
        self,
        *,
        sending_pool_name: typing.Optional[builtins.str] = None,
        tls_policy: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param sending_pool_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sesv2_configuration_set#sending_pool_name Sesv2ConfigurationSet#sending_pool_name}.
        :param tls_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sesv2_configuration_set#tls_policy Sesv2ConfigurationSet#tls_policy}.
        '''
        value = Sesv2ConfigurationSetDeliveryOptions(
            sending_pool_name=sending_pool_name, tls_policy=tls_policy
        )

        return typing.cast(None, jsii.invoke(self, "putDeliveryOptions", [value]))

    @jsii.member(jsii_name="putReputationOptions")
    def put_reputation_options(
        self,
        *,
        reputation_metrics_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param reputation_metrics_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sesv2_configuration_set#reputation_metrics_enabled Sesv2ConfigurationSet#reputation_metrics_enabled}.
        '''
        value = Sesv2ConfigurationSetReputationOptions(
            reputation_metrics_enabled=reputation_metrics_enabled
        )

        return typing.cast(None, jsii.invoke(self, "putReputationOptions", [value]))

    @jsii.member(jsii_name="putSendingOptions")
    def put_sending_options(
        self,
        *,
        sending_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param sending_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sesv2_configuration_set#sending_enabled Sesv2ConfigurationSet#sending_enabled}.
        '''
        value = Sesv2ConfigurationSetSendingOptions(sending_enabled=sending_enabled)

        return typing.cast(None, jsii.invoke(self, "putSendingOptions", [value]))

    @jsii.member(jsii_name="putSuppressionOptions")
    def put_suppression_options(
        self,
        *,
        suppressed_reasons: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param suppressed_reasons: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sesv2_configuration_set#suppressed_reasons Sesv2ConfigurationSet#suppressed_reasons}.
        '''
        value = Sesv2ConfigurationSetSuppressionOptions(
            suppressed_reasons=suppressed_reasons
        )

        return typing.cast(None, jsii.invoke(self, "putSuppressionOptions", [value]))

    @jsii.member(jsii_name="putTrackingOptions")
    def put_tracking_options(self, *, custom_redirect_domain: builtins.str) -> None:
        '''
        :param custom_redirect_domain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sesv2_configuration_set#custom_redirect_domain Sesv2ConfigurationSet#custom_redirect_domain}.
        '''
        value = Sesv2ConfigurationSetTrackingOptions(
            custom_redirect_domain=custom_redirect_domain
        )

        return typing.cast(None, jsii.invoke(self, "putTrackingOptions", [value]))

    @jsii.member(jsii_name="resetDeliveryOptions")
    def reset_delivery_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeliveryOptions", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetReputationOptions")
    def reset_reputation_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReputationOptions", []))

    @jsii.member(jsii_name="resetSendingOptions")
    def reset_sending_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSendingOptions", []))

    @jsii.member(jsii_name="resetSuppressionOptions")
    def reset_suppression_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSuppressionOptions", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetTrackingOptions")
    def reset_tracking_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTrackingOptions", []))

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
    @jsii.member(jsii_name="deliveryOptions")
    def delivery_options(self) -> "Sesv2ConfigurationSetDeliveryOptionsOutputReference":
        return typing.cast("Sesv2ConfigurationSetDeliveryOptionsOutputReference", jsii.get(self, "deliveryOptions"))

    @builtins.property
    @jsii.member(jsii_name="reputationOptions")
    def reputation_options(
        self,
    ) -> "Sesv2ConfigurationSetReputationOptionsOutputReference":
        return typing.cast("Sesv2ConfigurationSetReputationOptionsOutputReference", jsii.get(self, "reputationOptions"))

    @builtins.property
    @jsii.member(jsii_name="sendingOptions")
    def sending_options(self) -> "Sesv2ConfigurationSetSendingOptionsOutputReference":
        return typing.cast("Sesv2ConfigurationSetSendingOptionsOutputReference", jsii.get(self, "sendingOptions"))

    @builtins.property
    @jsii.member(jsii_name="suppressionOptions")
    def suppression_options(
        self,
    ) -> "Sesv2ConfigurationSetSuppressionOptionsOutputReference":
        return typing.cast("Sesv2ConfigurationSetSuppressionOptionsOutputReference", jsii.get(self, "suppressionOptions"))

    @builtins.property
    @jsii.member(jsii_name="trackingOptions")
    def tracking_options(self) -> "Sesv2ConfigurationSetTrackingOptionsOutputReference":
        return typing.cast("Sesv2ConfigurationSetTrackingOptionsOutputReference", jsii.get(self, "trackingOptions"))

    @builtins.property
    @jsii.member(jsii_name="configurationSetNameInput")
    def configuration_set_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "configurationSetNameInput"))

    @builtins.property
    @jsii.member(jsii_name="deliveryOptionsInput")
    def delivery_options_input(
        self,
    ) -> typing.Optional["Sesv2ConfigurationSetDeliveryOptions"]:
        return typing.cast(typing.Optional["Sesv2ConfigurationSetDeliveryOptions"], jsii.get(self, "deliveryOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="reputationOptionsInput")
    def reputation_options_input(
        self,
    ) -> typing.Optional["Sesv2ConfigurationSetReputationOptions"]:
        return typing.cast(typing.Optional["Sesv2ConfigurationSetReputationOptions"], jsii.get(self, "reputationOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="sendingOptionsInput")
    def sending_options_input(
        self,
    ) -> typing.Optional["Sesv2ConfigurationSetSendingOptions"]:
        return typing.cast(typing.Optional["Sesv2ConfigurationSetSendingOptions"], jsii.get(self, "sendingOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="suppressionOptionsInput")
    def suppression_options_input(
        self,
    ) -> typing.Optional["Sesv2ConfigurationSetSuppressionOptions"]:
        return typing.cast(typing.Optional["Sesv2ConfigurationSetSuppressionOptions"], jsii.get(self, "suppressionOptionsInput"))

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
    @jsii.member(jsii_name="trackingOptionsInput")
    def tracking_options_input(
        self,
    ) -> typing.Optional["Sesv2ConfigurationSetTrackingOptions"]:
        return typing.cast(typing.Optional["Sesv2ConfigurationSetTrackingOptions"], jsii.get(self, "trackingOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="configurationSetName")
    def configuration_set_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "configurationSetName"))

    @configuration_set_name.setter
    def configuration_set_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configurationSetName", value)

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
    jsii_type="@cdktf/provider-aws.sesv2ConfigurationSet.Sesv2ConfigurationSetConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "configuration_set_name": "configurationSetName",
        "delivery_options": "deliveryOptions",
        "id": "id",
        "reputation_options": "reputationOptions",
        "sending_options": "sendingOptions",
        "suppression_options": "suppressionOptions",
        "tags": "tags",
        "tags_all": "tagsAll",
        "tracking_options": "trackingOptions",
    },
)
class Sesv2ConfigurationSetConfig(cdktf.TerraformMetaArguments):
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
        configuration_set_name: builtins.str,
        delivery_options: typing.Optional[typing.Union["Sesv2ConfigurationSetDeliveryOptions", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        reputation_options: typing.Optional[typing.Union["Sesv2ConfigurationSetReputationOptions", typing.Dict[str, typing.Any]]] = None,
        sending_options: typing.Optional[typing.Union["Sesv2ConfigurationSetSendingOptions", typing.Dict[str, typing.Any]]] = None,
        suppression_options: typing.Optional[typing.Union["Sesv2ConfigurationSetSuppressionOptions", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tracking_options: typing.Optional[typing.Union["Sesv2ConfigurationSetTrackingOptions", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param configuration_set_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sesv2_configuration_set#configuration_set_name Sesv2ConfigurationSet#configuration_set_name}.
        :param delivery_options: delivery_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sesv2_configuration_set#delivery_options Sesv2ConfigurationSet#delivery_options}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sesv2_configuration_set#id Sesv2ConfigurationSet#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param reputation_options: reputation_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sesv2_configuration_set#reputation_options Sesv2ConfigurationSet#reputation_options}
        :param sending_options: sending_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sesv2_configuration_set#sending_options Sesv2ConfigurationSet#sending_options}
        :param suppression_options: suppression_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sesv2_configuration_set#suppression_options Sesv2ConfigurationSet#suppression_options}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sesv2_configuration_set#tags Sesv2ConfigurationSet#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sesv2_configuration_set#tags_all Sesv2ConfigurationSet#tags_all}.
        :param tracking_options: tracking_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sesv2_configuration_set#tracking_options Sesv2ConfigurationSet#tracking_options}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(delivery_options, dict):
            delivery_options = Sesv2ConfigurationSetDeliveryOptions(**delivery_options)
        if isinstance(reputation_options, dict):
            reputation_options = Sesv2ConfigurationSetReputationOptions(**reputation_options)
        if isinstance(sending_options, dict):
            sending_options = Sesv2ConfigurationSetSendingOptions(**sending_options)
        if isinstance(suppression_options, dict):
            suppression_options = Sesv2ConfigurationSetSuppressionOptions(**suppression_options)
        if isinstance(tracking_options, dict):
            tracking_options = Sesv2ConfigurationSetTrackingOptions(**tracking_options)
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
                configuration_set_name: builtins.str,
                delivery_options: typing.Optional[typing.Union[Sesv2ConfigurationSetDeliveryOptions, typing.Dict[str, typing.Any]]] = None,
                id: typing.Optional[builtins.str] = None,
                reputation_options: typing.Optional[typing.Union[Sesv2ConfigurationSetReputationOptions, typing.Dict[str, typing.Any]]] = None,
                sending_options: typing.Optional[typing.Union[Sesv2ConfigurationSetSendingOptions, typing.Dict[str, typing.Any]]] = None,
                suppression_options: typing.Optional[typing.Union[Sesv2ConfigurationSetSuppressionOptions, typing.Dict[str, typing.Any]]] = None,
                tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                tracking_options: typing.Optional[typing.Union[Sesv2ConfigurationSetTrackingOptions, typing.Dict[str, typing.Any]]] = None,
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
            check_type(argname="argument configuration_set_name", value=configuration_set_name, expected_type=type_hints["configuration_set_name"])
            check_type(argname="argument delivery_options", value=delivery_options, expected_type=type_hints["delivery_options"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument reputation_options", value=reputation_options, expected_type=type_hints["reputation_options"])
            check_type(argname="argument sending_options", value=sending_options, expected_type=type_hints["sending_options"])
            check_type(argname="argument suppression_options", value=suppression_options, expected_type=type_hints["suppression_options"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument tracking_options", value=tracking_options, expected_type=type_hints["tracking_options"])
        self._values: typing.Dict[str, typing.Any] = {
            "configuration_set_name": configuration_set_name,
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
        if delivery_options is not None:
            self._values["delivery_options"] = delivery_options
        if id is not None:
            self._values["id"] = id
        if reputation_options is not None:
            self._values["reputation_options"] = reputation_options
        if sending_options is not None:
            self._values["sending_options"] = sending_options
        if suppression_options is not None:
            self._values["suppression_options"] = suppression_options
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if tracking_options is not None:
            self._values["tracking_options"] = tracking_options

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
    def configuration_set_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sesv2_configuration_set#configuration_set_name Sesv2ConfigurationSet#configuration_set_name}.'''
        result = self._values.get("configuration_set_name")
        assert result is not None, "Required property 'configuration_set_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def delivery_options(
        self,
    ) -> typing.Optional["Sesv2ConfigurationSetDeliveryOptions"]:
        '''delivery_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sesv2_configuration_set#delivery_options Sesv2ConfigurationSet#delivery_options}
        '''
        result = self._values.get("delivery_options")
        return typing.cast(typing.Optional["Sesv2ConfigurationSetDeliveryOptions"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sesv2_configuration_set#id Sesv2ConfigurationSet#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def reputation_options(
        self,
    ) -> typing.Optional["Sesv2ConfigurationSetReputationOptions"]:
        '''reputation_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sesv2_configuration_set#reputation_options Sesv2ConfigurationSet#reputation_options}
        '''
        result = self._values.get("reputation_options")
        return typing.cast(typing.Optional["Sesv2ConfigurationSetReputationOptions"], result)

    @builtins.property
    def sending_options(self) -> typing.Optional["Sesv2ConfigurationSetSendingOptions"]:
        '''sending_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sesv2_configuration_set#sending_options Sesv2ConfigurationSet#sending_options}
        '''
        result = self._values.get("sending_options")
        return typing.cast(typing.Optional["Sesv2ConfigurationSetSendingOptions"], result)

    @builtins.property
    def suppression_options(
        self,
    ) -> typing.Optional["Sesv2ConfigurationSetSuppressionOptions"]:
        '''suppression_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sesv2_configuration_set#suppression_options Sesv2ConfigurationSet#suppression_options}
        '''
        result = self._values.get("suppression_options")
        return typing.cast(typing.Optional["Sesv2ConfigurationSetSuppressionOptions"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sesv2_configuration_set#tags Sesv2ConfigurationSet#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sesv2_configuration_set#tags_all Sesv2ConfigurationSet#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tracking_options(
        self,
    ) -> typing.Optional["Sesv2ConfigurationSetTrackingOptions"]:
        '''tracking_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sesv2_configuration_set#tracking_options Sesv2ConfigurationSet#tracking_options}
        '''
        result = self._values.get("tracking_options")
        return typing.cast(typing.Optional["Sesv2ConfigurationSetTrackingOptions"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Sesv2ConfigurationSetConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.sesv2ConfigurationSet.Sesv2ConfigurationSetDeliveryOptions",
    jsii_struct_bases=[],
    name_mapping={"sending_pool_name": "sendingPoolName", "tls_policy": "tlsPolicy"},
)
class Sesv2ConfigurationSetDeliveryOptions:
    def __init__(
        self,
        *,
        sending_pool_name: typing.Optional[builtins.str] = None,
        tls_policy: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param sending_pool_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sesv2_configuration_set#sending_pool_name Sesv2ConfigurationSet#sending_pool_name}.
        :param tls_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sesv2_configuration_set#tls_policy Sesv2ConfigurationSet#tls_policy}.
        '''
        if __debug__:
            def stub(
                *,
                sending_pool_name: typing.Optional[builtins.str] = None,
                tls_policy: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument sending_pool_name", value=sending_pool_name, expected_type=type_hints["sending_pool_name"])
            check_type(argname="argument tls_policy", value=tls_policy, expected_type=type_hints["tls_policy"])
        self._values: typing.Dict[str, typing.Any] = {}
        if sending_pool_name is not None:
            self._values["sending_pool_name"] = sending_pool_name
        if tls_policy is not None:
            self._values["tls_policy"] = tls_policy

    @builtins.property
    def sending_pool_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sesv2_configuration_set#sending_pool_name Sesv2ConfigurationSet#sending_pool_name}.'''
        result = self._values.get("sending_pool_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tls_policy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sesv2_configuration_set#tls_policy Sesv2ConfigurationSet#tls_policy}.'''
        result = self._values.get("tls_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Sesv2ConfigurationSetDeliveryOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Sesv2ConfigurationSetDeliveryOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.sesv2ConfigurationSet.Sesv2ConfigurationSetDeliveryOptionsOutputReference",
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

    @jsii.member(jsii_name="resetSendingPoolName")
    def reset_sending_pool_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSendingPoolName", []))

    @jsii.member(jsii_name="resetTlsPolicy")
    def reset_tls_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTlsPolicy", []))

    @builtins.property
    @jsii.member(jsii_name="sendingPoolNameInput")
    def sending_pool_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sendingPoolNameInput"))

    @builtins.property
    @jsii.member(jsii_name="tlsPolicyInput")
    def tls_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tlsPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="sendingPoolName")
    def sending_pool_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sendingPoolName"))

    @sending_pool_name.setter
    def sending_pool_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sendingPoolName", value)

    @builtins.property
    @jsii.member(jsii_name="tlsPolicy")
    def tls_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tlsPolicy"))

    @tls_policy.setter
    def tls_policy(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tlsPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[Sesv2ConfigurationSetDeliveryOptions]:
        return typing.cast(typing.Optional[Sesv2ConfigurationSetDeliveryOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Sesv2ConfigurationSetDeliveryOptions],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[Sesv2ConfigurationSetDeliveryOptions],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.sesv2ConfigurationSet.Sesv2ConfigurationSetReputationOptions",
    jsii_struct_bases=[],
    name_mapping={"reputation_metrics_enabled": "reputationMetricsEnabled"},
)
class Sesv2ConfigurationSetReputationOptions:
    def __init__(
        self,
        *,
        reputation_metrics_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param reputation_metrics_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sesv2_configuration_set#reputation_metrics_enabled Sesv2ConfigurationSet#reputation_metrics_enabled}.
        '''
        if __debug__:
            def stub(
                *,
                reputation_metrics_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument reputation_metrics_enabled", value=reputation_metrics_enabled, expected_type=type_hints["reputation_metrics_enabled"])
        self._values: typing.Dict[str, typing.Any] = {}
        if reputation_metrics_enabled is not None:
            self._values["reputation_metrics_enabled"] = reputation_metrics_enabled

    @builtins.property
    def reputation_metrics_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sesv2_configuration_set#reputation_metrics_enabled Sesv2ConfigurationSet#reputation_metrics_enabled}.'''
        result = self._values.get("reputation_metrics_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Sesv2ConfigurationSetReputationOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Sesv2ConfigurationSetReputationOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.sesv2ConfigurationSet.Sesv2ConfigurationSetReputationOptionsOutputReference",
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

    @jsii.member(jsii_name="resetReputationMetricsEnabled")
    def reset_reputation_metrics_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReputationMetricsEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="lastFreshStart")
    def last_fresh_start(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastFreshStart"))

    @builtins.property
    @jsii.member(jsii_name="reputationMetricsEnabledInput")
    def reputation_metrics_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "reputationMetricsEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="reputationMetricsEnabled")
    def reputation_metrics_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "reputationMetricsEnabled"))

    @reputation_metrics_enabled.setter
    def reputation_metrics_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "reputationMetricsEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[Sesv2ConfigurationSetReputationOptions]:
        return typing.cast(typing.Optional[Sesv2ConfigurationSetReputationOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Sesv2ConfigurationSetReputationOptions],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[Sesv2ConfigurationSetReputationOptions],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.sesv2ConfigurationSet.Sesv2ConfigurationSetSendingOptions",
    jsii_struct_bases=[],
    name_mapping={"sending_enabled": "sendingEnabled"},
)
class Sesv2ConfigurationSetSendingOptions:
    def __init__(
        self,
        *,
        sending_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param sending_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sesv2_configuration_set#sending_enabled Sesv2ConfigurationSet#sending_enabled}.
        '''
        if __debug__:
            def stub(
                *,
                sending_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument sending_enabled", value=sending_enabled, expected_type=type_hints["sending_enabled"])
        self._values: typing.Dict[str, typing.Any] = {}
        if sending_enabled is not None:
            self._values["sending_enabled"] = sending_enabled

    @builtins.property
    def sending_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sesv2_configuration_set#sending_enabled Sesv2ConfigurationSet#sending_enabled}.'''
        result = self._values.get("sending_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Sesv2ConfigurationSetSendingOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Sesv2ConfigurationSetSendingOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.sesv2ConfigurationSet.Sesv2ConfigurationSetSendingOptionsOutputReference",
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

    @jsii.member(jsii_name="resetSendingEnabled")
    def reset_sending_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSendingEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="sendingEnabledInput")
    def sending_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "sendingEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="sendingEnabled")
    def sending_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "sendingEnabled"))

    @sending_enabled.setter
    def sending_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sendingEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[Sesv2ConfigurationSetSendingOptions]:
        return typing.cast(typing.Optional[Sesv2ConfigurationSetSendingOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Sesv2ConfigurationSetSendingOptions],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[Sesv2ConfigurationSetSendingOptions],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.sesv2ConfigurationSet.Sesv2ConfigurationSetSuppressionOptions",
    jsii_struct_bases=[],
    name_mapping={"suppressed_reasons": "suppressedReasons"},
)
class Sesv2ConfigurationSetSuppressionOptions:
    def __init__(
        self,
        *,
        suppressed_reasons: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param suppressed_reasons: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sesv2_configuration_set#suppressed_reasons Sesv2ConfigurationSet#suppressed_reasons}.
        '''
        if __debug__:
            def stub(
                *,
                suppressed_reasons: typing.Optional[typing.Sequence[builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument suppressed_reasons", value=suppressed_reasons, expected_type=type_hints["suppressed_reasons"])
        self._values: typing.Dict[str, typing.Any] = {}
        if suppressed_reasons is not None:
            self._values["suppressed_reasons"] = suppressed_reasons

    @builtins.property
    def suppressed_reasons(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sesv2_configuration_set#suppressed_reasons Sesv2ConfigurationSet#suppressed_reasons}.'''
        result = self._values.get("suppressed_reasons")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Sesv2ConfigurationSetSuppressionOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Sesv2ConfigurationSetSuppressionOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.sesv2ConfigurationSet.Sesv2ConfigurationSetSuppressionOptionsOutputReference",
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

    @jsii.member(jsii_name="resetSuppressedReasons")
    def reset_suppressed_reasons(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSuppressedReasons", []))

    @builtins.property
    @jsii.member(jsii_name="suppressedReasonsInput")
    def suppressed_reasons_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "suppressedReasonsInput"))

    @builtins.property
    @jsii.member(jsii_name="suppressedReasons")
    def suppressed_reasons(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "suppressedReasons"))

    @suppressed_reasons.setter
    def suppressed_reasons(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "suppressedReasons", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Sesv2ConfigurationSetSuppressionOptions]:
        return typing.cast(typing.Optional[Sesv2ConfigurationSetSuppressionOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Sesv2ConfigurationSetSuppressionOptions],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[Sesv2ConfigurationSetSuppressionOptions],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.sesv2ConfigurationSet.Sesv2ConfigurationSetTrackingOptions",
    jsii_struct_bases=[],
    name_mapping={"custom_redirect_domain": "customRedirectDomain"},
)
class Sesv2ConfigurationSetTrackingOptions:
    def __init__(self, *, custom_redirect_domain: builtins.str) -> None:
        '''
        :param custom_redirect_domain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sesv2_configuration_set#custom_redirect_domain Sesv2ConfigurationSet#custom_redirect_domain}.
        '''
        if __debug__:
            def stub(*, custom_redirect_domain: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument custom_redirect_domain", value=custom_redirect_domain, expected_type=type_hints["custom_redirect_domain"])
        self._values: typing.Dict[str, typing.Any] = {
            "custom_redirect_domain": custom_redirect_domain,
        }

    @builtins.property
    def custom_redirect_domain(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sesv2_configuration_set#custom_redirect_domain Sesv2ConfigurationSet#custom_redirect_domain}.'''
        result = self._values.get("custom_redirect_domain")
        assert result is not None, "Required property 'custom_redirect_domain' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Sesv2ConfigurationSetTrackingOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Sesv2ConfigurationSetTrackingOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.sesv2ConfigurationSet.Sesv2ConfigurationSetTrackingOptionsOutputReference",
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
    @jsii.member(jsii_name="customRedirectDomainInput")
    def custom_redirect_domain_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customRedirectDomainInput"))

    @builtins.property
    @jsii.member(jsii_name="customRedirectDomain")
    def custom_redirect_domain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customRedirectDomain"))

    @custom_redirect_domain.setter
    def custom_redirect_domain(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customRedirectDomain", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[Sesv2ConfigurationSetTrackingOptions]:
        return typing.cast(typing.Optional[Sesv2ConfigurationSetTrackingOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Sesv2ConfigurationSetTrackingOptions],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[Sesv2ConfigurationSetTrackingOptions],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Sesv2ConfigurationSet",
    "Sesv2ConfigurationSetConfig",
    "Sesv2ConfigurationSetDeliveryOptions",
    "Sesv2ConfigurationSetDeliveryOptionsOutputReference",
    "Sesv2ConfigurationSetReputationOptions",
    "Sesv2ConfigurationSetReputationOptionsOutputReference",
    "Sesv2ConfigurationSetSendingOptions",
    "Sesv2ConfigurationSetSendingOptionsOutputReference",
    "Sesv2ConfigurationSetSuppressionOptions",
    "Sesv2ConfigurationSetSuppressionOptionsOutputReference",
    "Sesv2ConfigurationSetTrackingOptions",
    "Sesv2ConfigurationSetTrackingOptionsOutputReference",
]

publication.publish()
