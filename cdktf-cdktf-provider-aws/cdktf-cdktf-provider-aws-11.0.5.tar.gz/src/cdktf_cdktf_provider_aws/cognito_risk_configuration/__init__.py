'''
# `aws_cognito_risk_configuration`

Refer to the Terraform Registory for docs: [`aws_cognito_risk_configuration`](https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration).
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


class CognitoRiskConfiguration(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.cognitoRiskConfiguration.CognitoRiskConfiguration",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration aws_cognito_risk_configuration}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        user_pool_id: builtins.str,
        account_takeover_risk_configuration: typing.Optional[typing.Union["CognitoRiskConfigurationAccountTakeoverRiskConfiguration", typing.Dict[str, typing.Any]]] = None,
        client_id: typing.Optional[builtins.str] = None,
        compromised_credentials_risk_configuration: typing.Optional[typing.Union["CognitoRiskConfigurationCompromisedCredentialsRiskConfiguration", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        risk_exception_configuration: typing.Optional[typing.Union["CognitoRiskConfigurationRiskExceptionConfiguration", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration aws_cognito_risk_configuration} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param user_pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#user_pool_id CognitoRiskConfiguration#user_pool_id}.
        :param account_takeover_risk_configuration: account_takeover_risk_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#account_takeover_risk_configuration CognitoRiskConfiguration#account_takeover_risk_configuration}
        :param client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#client_id CognitoRiskConfiguration#client_id}.
        :param compromised_credentials_risk_configuration: compromised_credentials_risk_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#compromised_credentials_risk_configuration CognitoRiskConfiguration#compromised_credentials_risk_configuration}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#id CognitoRiskConfiguration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param risk_exception_configuration: risk_exception_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#risk_exception_configuration CognitoRiskConfiguration#risk_exception_configuration}
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
                user_pool_id: builtins.str,
                account_takeover_risk_configuration: typing.Optional[typing.Union[CognitoRiskConfigurationAccountTakeoverRiskConfiguration, typing.Dict[str, typing.Any]]] = None,
                client_id: typing.Optional[builtins.str] = None,
                compromised_credentials_risk_configuration: typing.Optional[typing.Union[CognitoRiskConfigurationCompromisedCredentialsRiskConfiguration, typing.Dict[str, typing.Any]]] = None,
                id: typing.Optional[builtins.str] = None,
                risk_exception_configuration: typing.Optional[typing.Union[CognitoRiskConfigurationRiskExceptionConfiguration, typing.Dict[str, typing.Any]]] = None,
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
        config = CognitoRiskConfigurationConfig(
            user_pool_id=user_pool_id,
            account_takeover_risk_configuration=account_takeover_risk_configuration,
            client_id=client_id,
            compromised_credentials_risk_configuration=compromised_credentials_risk_configuration,
            id=id,
            risk_exception_configuration=risk_exception_configuration,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAccountTakeoverRiskConfiguration")
    def put_account_takeover_risk_configuration(
        self,
        *,
        actions: typing.Union["CognitoRiskConfigurationAccountTakeoverRiskConfigurationActions", typing.Dict[str, typing.Any]],
        notify_configuration: typing.Union["CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfiguration", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param actions: actions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#actions CognitoRiskConfiguration#actions}
        :param notify_configuration: notify_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#notify_configuration CognitoRiskConfiguration#notify_configuration}
        '''
        value = CognitoRiskConfigurationAccountTakeoverRiskConfiguration(
            actions=actions, notify_configuration=notify_configuration
        )

        return typing.cast(None, jsii.invoke(self, "putAccountTakeoverRiskConfiguration", [value]))

    @jsii.member(jsii_name="putCompromisedCredentialsRiskConfiguration")
    def put_compromised_credentials_risk_configuration(
        self,
        *,
        actions: typing.Union["CognitoRiskConfigurationCompromisedCredentialsRiskConfigurationActions", typing.Dict[str, typing.Any]],
        event_filter: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param actions: actions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#actions CognitoRiskConfiguration#actions}
        :param event_filter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#event_filter CognitoRiskConfiguration#event_filter}.
        '''
        value = CognitoRiskConfigurationCompromisedCredentialsRiskConfiguration(
            actions=actions, event_filter=event_filter
        )

        return typing.cast(None, jsii.invoke(self, "putCompromisedCredentialsRiskConfiguration", [value]))

    @jsii.member(jsii_name="putRiskExceptionConfiguration")
    def put_risk_exception_configuration(
        self,
        *,
        blocked_ip_range_list: typing.Optional[typing.Sequence[builtins.str]] = None,
        skipped_ip_range_list: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param blocked_ip_range_list: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#blocked_ip_range_list CognitoRiskConfiguration#blocked_ip_range_list}.
        :param skipped_ip_range_list: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#skipped_ip_range_list CognitoRiskConfiguration#skipped_ip_range_list}.
        '''
        value = CognitoRiskConfigurationRiskExceptionConfiguration(
            blocked_ip_range_list=blocked_ip_range_list,
            skipped_ip_range_list=skipped_ip_range_list,
        )

        return typing.cast(None, jsii.invoke(self, "putRiskExceptionConfiguration", [value]))

    @jsii.member(jsii_name="resetAccountTakeoverRiskConfiguration")
    def reset_account_takeover_risk_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccountTakeoverRiskConfiguration", []))

    @jsii.member(jsii_name="resetClientId")
    def reset_client_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientId", []))

    @jsii.member(jsii_name="resetCompromisedCredentialsRiskConfiguration")
    def reset_compromised_credentials_risk_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCompromisedCredentialsRiskConfiguration", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetRiskExceptionConfiguration")
    def reset_risk_exception_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRiskExceptionConfiguration", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="accountTakeoverRiskConfiguration")
    def account_takeover_risk_configuration(
        self,
    ) -> "CognitoRiskConfigurationAccountTakeoverRiskConfigurationOutputReference":
        return typing.cast("CognitoRiskConfigurationAccountTakeoverRiskConfigurationOutputReference", jsii.get(self, "accountTakeoverRiskConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="compromisedCredentialsRiskConfiguration")
    def compromised_credentials_risk_configuration(
        self,
    ) -> "CognitoRiskConfigurationCompromisedCredentialsRiskConfigurationOutputReference":
        return typing.cast("CognitoRiskConfigurationCompromisedCredentialsRiskConfigurationOutputReference", jsii.get(self, "compromisedCredentialsRiskConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="riskExceptionConfiguration")
    def risk_exception_configuration(
        self,
    ) -> "CognitoRiskConfigurationRiskExceptionConfigurationOutputReference":
        return typing.cast("CognitoRiskConfigurationRiskExceptionConfigurationOutputReference", jsii.get(self, "riskExceptionConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="accountTakeoverRiskConfigurationInput")
    def account_takeover_risk_configuration_input(
        self,
    ) -> typing.Optional["CognitoRiskConfigurationAccountTakeoverRiskConfiguration"]:
        return typing.cast(typing.Optional["CognitoRiskConfigurationAccountTakeoverRiskConfiguration"], jsii.get(self, "accountTakeoverRiskConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="clientIdInput")
    def client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="compromisedCredentialsRiskConfigurationInput")
    def compromised_credentials_risk_configuration_input(
        self,
    ) -> typing.Optional["CognitoRiskConfigurationCompromisedCredentialsRiskConfiguration"]:
        return typing.cast(typing.Optional["CognitoRiskConfigurationCompromisedCredentialsRiskConfiguration"], jsii.get(self, "compromisedCredentialsRiskConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="riskExceptionConfigurationInput")
    def risk_exception_configuration_input(
        self,
    ) -> typing.Optional["CognitoRiskConfigurationRiskExceptionConfiguration"]:
        return typing.cast(typing.Optional["CognitoRiskConfigurationRiskExceptionConfiguration"], jsii.get(self, "riskExceptionConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="userPoolIdInput")
    def user_pool_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userPoolIdInput"))

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientId", value)

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
    @jsii.member(jsii_name="userPoolId")
    def user_pool_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userPoolId"))

    @user_pool_id.setter
    def user_pool_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userPoolId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.cognitoRiskConfiguration.CognitoRiskConfigurationAccountTakeoverRiskConfiguration",
    jsii_struct_bases=[],
    name_mapping={"actions": "actions", "notify_configuration": "notifyConfiguration"},
)
class CognitoRiskConfigurationAccountTakeoverRiskConfiguration:
    def __init__(
        self,
        *,
        actions: typing.Union["CognitoRiskConfigurationAccountTakeoverRiskConfigurationActions", typing.Dict[str, typing.Any]],
        notify_configuration: typing.Union["CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfiguration", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param actions: actions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#actions CognitoRiskConfiguration#actions}
        :param notify_configuration: notify_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#notify_configuration CognitoRiskConfiguration#notify_configuration}
        '''
        if isinstance(actions, dict):
            actions = CognitoRiskConfigurationAccountTakeoverRiskConfigurationActions(**actions)
        if isinstance(notify_configuration, dict):
            notify_configuration = CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfiguration(**notify_configuration)
        if __debug__:
            def stub(
                *,
                actions: typing.Union[CognitoRiskConfigurationAccountTakeoverRiskConfigurationActions, typing.Dict[str, typing.Any]],
                notify_configuration: typing.Union[CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfiguration, typing.Dict[str, typing.Any]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument actions", value=actions, expected_type=type_hints["actions"])
            check_type(argname="argument notify_configuration", value=notify_configuration, expected_type=type_hints["notify_configuration"])
        self._values: typing.Dict[str, typing.Any] = {
            "actions": actions,
            "notify_configuration": notify_configuration,
        }

    @builtins.property
    def actions(
        self,
    ) -> "CognitoRiskConfigurationAccountTakeoverRiskConfigurationActions":
        '''actions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#actions CognitoRiskConfiguration#actions}
        '''
        result = self._values.get("actions")
        assert result is not None, "Required property 'actions' is missing"
        return typing.cast("CognitoRiskConfigurationAccountTakeoverRiskConfigurationActions", result)

    @builtins.property
    def notify_configuration(
        self,
    ) -> "CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfiguration":
        '''notify_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#notify_configuration CognitoRiskConfiguration#notify_configuration}
        '''
        result = self._values.get("notify_configuration")
        assert result is not None, "Required property 'notify_configuration' is missing"
        return typing.cast("CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfiguration", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CognitoRiskConfigurationAccountTakeoverRiskConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.cognitoRiskConfiguration.CognitoRiskConfigurationAccountTakeoverRiskConfigurationActions",
    jsii_struct_bases=[],
    name_mapping={
        "high_action": "highAction",
        "low_action": "lowAction",
        "medium_action": "mediumAction",
    },
)
class CognitoRiskConfigurationAccountTakeoverRiskConfigurationActions:
    def __init__(
        self,
        *,
        high_action: typing.Optional[typing.Union["CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsHighAction", typing.Dict[str, typing.Any]]] = None,
        low_action: typing.Optional[typing.Union["CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsLowAction", typing.Dict[str, typing.Any]]] = None,
        medium_action: typing.Optional[typing.Union["CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumAction", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param high_action: high_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#high_action CognitoRiskConfiguration#high_action}
        :param low_action: low_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#low_action CognitoRiskConfiguration#low_action}
        :param medium_action: medium_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#medium_action CognitoRiskConfiguration#medium_action}
        '''
        if isinstance(high_action, dict):
            high_action = CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsHighAction(**high_action)
        if isinstance(low_action, dict):
            low_action = CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsLowAction(**low_action)
        if isinstance(medium_action, dict):
            medium_action = CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumAction(**medium_action)
        if __debug__:
            def stub(
                *,
                high_action: typing.Optional[typing.Union[CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsHighAction, typing.Dict[str, typing.Any]]] = None,
                low_action: typing.Optional[typing.Union[CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsLowAction, typing.Dict[str, typing.Any]]] = None,
                medium_action: typing.Optional[typing.Union[CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumAction, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument high_action", value=high_action, expected_type=type_hints["high_action"])
            check_type(argname="argument low_action", value=low_action, expected_type=type_hints["low_action"])
            check_type(argname="argument medium_action", value=medium_action, expected_type=type_hints["medium_action"])
        self._values: typing.Dict[str, typing.Any] = {}
        if high_action is not None:
            self._values["high_action"] = high_action
        if low_action is not None:
            self._values["low_action"] = low_action
        if medium_action is not None:
            self._values["medium_action"] = medium_action

    @builtins.property
    def high_action(
        self,
    ) -> typing.Optional["CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsHighAction"]:
        '''high_action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#high_action CognitoRiskConfiguration#high_action}
        '''
        result = self._values.get("high_action")
        return typing.cast(typing.Optional["CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsHighAction"], result)

    @builtins.property
    def low_action(
        self,
    ) -> typing.Optional["CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsLowAction"]:
        '''low_action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#low_action CognitoRiskConfiguration#low_action}
        '''
        result = self._values.get("low_action")
        return typing.cast(typing.Optional["CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsLowAction"], result)

    @builtins.property
    def medium_action(
        self,
    ) -> typing.Optional["CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumAction"]:
        '''medium_action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#medium_action CognitoRiskConfiguration#medium_action}
        '''
        result = self._values.get("medium_action")
        return typing.cast(typing.Optional["CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumAction"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CognitoRiskConfigurationAccountTakeoverRiskConfigurationActions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.cognitoRiskConfiguration.CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsHighAction",
    jsii_struct_bases=[],
    name_mapping={"event_action": "eventAction", "notify": "notify"},
)
class CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsHighAction:
    def __init__(
        self,
        *,
        event_action: builtins.str,
        notify: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param event_action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#event_action CognitoRiskConfiguration#event_action}.
        :param notify: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#notify CognitoRiskConfiguration#notify}.
        '''
        if __debug__:
            def stub(
                *,
                event_action: builtins.str,
                notify: typing.Union[builtins.bool, cdktf.IResolvable],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument event_action", value=event_action, expected_type=type_hints["event_action"])
            check_type(argname="argument notify", value=notify, expected_type=type_hints["notify"])
        self._values: typing.Dict[str, typing.Any] = {
            "event_action": event_action,
            "notify": notify,
        }

    @builtins.property
    def event_action(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#event_action CognitoRiskConfiguration#event_action}.'''
        result = self._values.get("event_action")
        assert result is not None, "Required property 'event_action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def notify(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#notify CognitoRiskConfiguration#notify}.'''
        result = self._values.get("notify")
        assert result is not None, "Required property 'notify' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsHighAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsHighActionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.cognitoRiskConfiguration.CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsHighActionOutputReference",
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
    @jsii.member(jsii_name="eventActionInput")
    def event_action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "eventActionInput"))

    @builtins.property
    @jsii.member(jsii_name="notifyInput")
    def notify_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "notifyInput"))

    @builtins.property
    @jsii.member(jsii_name="eventAction")
    def event_action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "eventAction"))

    @event_action.setter
    def event_action(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventAction", value)

    @builtins.property
    @jsii.member(jsii_name="notify")
    def notify(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "notify"))

    @notify.setter
    def notify(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notify", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsHighAction]:
        return typing.cast(typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsHighAction], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsHighAction],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsHighAction],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.cognitoRiskConfiguration.CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsLowAction",
    jsii_struct_bases=[],
    name_mapping={"event_action": "eventAction", "notify": "notify"},
)
class CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsLowAction:
    def __init__(
        self,
        *,
        event_action: builtins.str,
        notify: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param event_action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#event_action CognitoRiskConfiguration#event_action}.
        :param notify: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#notify CognitoRiskConfiguration#notify}.
        '''
        if __debug__:
            def stub(
                *,
                event_action: builtins.str,
                notify: typing.Union[builtins.bool, cdktf.IResolvable],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument event_action", value=event_action, expected_type=type_hints["event_action"])
            check_type(argname="argument notify", value=notify, expected_type=type_hints["notify"])
        self._values: typing.Dict[str, typing.Any] = {
            "event_action": event_action,
            "notify": notify,
        }

    @builtins.property
    def event_action(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#event_action CognitoRiskConfiguration#event_action}.'''
        result = self._values.get("event_action")
        assert result is not None, "Required property 'event_action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def notify(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#notify CognitoRiskConfiguration#notify}.'''
        result = self._values.get("notify")
        assert result is not None, "Required property 'notify' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsLowAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsLowActionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.cognitoRiskConfiguration.CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsLowActionOutputReference",
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
    @jsii.member(jsii_name="eventActionInput")
    def event_action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "eventActionInput"))

    @builtins.property
    @jsii.member(jsii_name="notifyInput")
    def notify_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "notifyInput"))

    @builtins.property
    @jsii.member(jsii_name="eventAction")
    def event_action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "eventAction"))

    @event_action.setter
    def event_action(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventAction", value)

    @builtins.property
    @jsii.member(jsii_name="notify")
    def notify(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "notify"))

    @notify.setter
    def notify(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notify", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsLowAction]:
        return typing.cast(typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsLowAction], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsLowAction],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsLowAction],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.cognitoRiskConfiguration.CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumAction",
    jsii_struct_bases=[],
    name_mapping={"event_action": "eventAction", "notify": "notify"},
)
class CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumAction:
    def __init__(
        self,
        *,
        event_action: builtins.str,
        notify: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param event_action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#event_action CognitoRiskConfiguration#event_action}.
        :param notify: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#notify CognitoRiskConfiguration#notify}.
        '''
        if __debug__:
            def stub(
                *,
                event_action: builtins.str,
                notify: typing.Union[builtins.bool, cdktf.IResolvable],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument event_action", value=event_action, expected_type=type_hints["event_action"])
            check_type(argname="argument notify", value=notify, expected_type=type_hints["notify"])
        self._values: typing.Dict[str, typing.Any] = {
            "event_action": event_action,
            "notify": notify,
        }

    @builtins.property
    def event_action(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#event_action CognitoRiskConfiguration#event_action}.'''
        result = self._values.get("event_action")
        assert result is not None, "Required property 'event_action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def notify(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#notify CognitoRiskConfiguration#notify}.'''
        result = self._values.get("notify")
        assert result is not None, "Required property 'notify' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumActionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.cognitoRiskConfiguration.CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumActionOutputReference",
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
    @jsii.member(jsii_name="eventActionInput")
    def event_action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "eventActionInput"))

    @builtins.property
    @jsii.member(jsii_name="notifyInput")
    def notify_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "notifyInput"))

    @builtins.property
    @jsii.member(jsii_name="eventAction")
    def event_action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "eventAction"))

    @event_action.setter
    def event_action(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventAction", value)

    @builtins.property
    @jsii.member(jsii_name="notify")
    def notify(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "notify"))

    @notify.setter
    def notify(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notify", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumAction]:
        return typing.cast(typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumAction], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumAction],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumAction],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.cognitoRiskConfiguration.CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsOutputReference",
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

    @jsii.member(jsii_name="putHighAction")
    def put_high_action(
        self,
        *,
        event_action: builtins.str,
        notify: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param event_action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#event_action CognitoRiskConfiguration#event_action}.
        :param notify: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#notify CognitoRiskConfiguration#notify}.
        '''
        value = CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsHighAction(
            event_action=event_action, notify=notify
        )

        return typing.cast(None, jsii.invoke(self, "putHighAction", [value]))

    @jsii.member(jsii_name="putLowAction")
    def put_low_action(
        self,
        *,
        event_action: builtins.str,
        notify: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param event_action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#event_action CognitoRiskConfiguration#event_action}.
        :param notify: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#notify CognitoRiskConfiguration#notify}.
        '''
        value = CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsLowAction(
            event_action=event_action, notify=notify
        )

        return typing.cast(None, jsii.invoke(self, "putLowAction", [value]))

    @jsii.member(jsii_name="putMediumAction")
    def put_medium_action(
        self,
        *,
        event_action: builtins.str,
        notify: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param event_action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#event_action CognitoRiskConfiguration#event_action}.
        :param notify: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#notify CognitoRiskConfiguration#notify}.
        '''
        value = CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumAction(
            event_action=event_action, notify=notify
        )

        return typing.cast(None, jsii.invoke(self, "putMediumAction", [value]))

    @jsii.member(jsii_name="resetHighAction")
    def reset_high_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHighAction", []))

    @jsii.member(jsii_name="resetLowAction")
    def reset_low_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLowAction", []))

    @jsii.member(jsii_name="resetMediumAction")
    def reset_medium_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMediumAction", []))

    @builtins.property
    @jsii.member(jsii_name="highAction")
    def high_action(
        self,
    ) -> CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsHighActionOutputReference:
        return typing.cast(CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsHighActionOutputReference, jsii.get(self, "highAction"))

    @builtins.property
    @jsii.member(jsii_name="lowAction")
    def low_action(
        self,
    ) -> CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsLowActionOutputReference:
        return typing.cast(CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsLowActionOutputReference, jsii.get(self, "lowAction"))

    @builtins.property
    @jsii.member(jsii_name="mediumAction")
    def medium_action(
        self,
    ) -> CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumActionOutputReference:
        return typing.cast(CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumActionOutputReference, jsii.get(self, "mediumAction"))

    @builtins.property
    @jsii.member(jsii_name="highActionInput")
    def high_action_input(
        self,
    ) -> typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsHighAction]:
        return typing.cast(typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsHighAction], jsii.get(self, "highActionInput"))

    @builtins.property
    @jsii.member(jsii_name="lowActionInput")
    def low_action_input(
        self,
    ) -> typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsLowAction]:
        return typing.cast(typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsLowAction], jsii.get(self, "lowActionInput"))

    @builtins.property
    @jsii.member(jsii_name="mediumActionInput")
    def medium_action_input(
        self,
    ) -> typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumAction]:
        return typing.cast(typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumAction], jsii.get(self, "mediumActionInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationActions]:
        return typing.cast(typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationActions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationActions],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationActions],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.cognitoRiskConfiguration.CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "source_arn": "sourceArn",
        "block_email": "blockEmail",
        "from_": "from",
        "mfa_email": "mfaEmail",
        "no_action_email": "noActionEmail",
        "reply_to": "replyTo",
    },
)
class CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfiguration:
    def __init__(
        self,
        *,
        source_arn: builtins.str,
        block_email: typing.Optional[typing.Union["CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmail", typing.Dict[str, typing.Any]]] = None,
        from_: typing.Optional[builtins.str] = None,
        mfa_email: typing.Optional[typing.Union["CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmail", typing.Dict[str, typing.Any]]] = None,
        no_action_email: typing.Optional[typing.Union["CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmail", typing.Dict[str, typing.Any]]] = None,
        reply_to: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param source_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#source_arn CognitoRiskConfiguration#source_arn}.
        :param block_email: block_email block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#block_email CognitoRiskConfiguration#block_email}
        :param from_: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#from CognitoRiskConfiguration#from}.
        :param mfa_email: mfa_email block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#mfa_email CognitoRiskConfiguration#mfa_email}
        :param no_action_email: no_action_email block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#no_action_email CognitoRiskConfiguration#no_action_email}
        :param reply_to: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#reply_to CognitoRiskConfiguration#reply_to}.
        '''
        if isinstance(block_email, dict):
            block_email = CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmail(**block_email)
        if isinstance(mfa_email, dict):
            mfa_email = CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmail(**mfa_email)
        if isinstance(no_action_email, dict):
            no_action_email = CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmail(**no_action_email)
        if __debug__:
            def stub(
                *,
                source_arn: builtins.str,
                block_email: typing.Optional[typing.Union[CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmail, typing.Dict[str, typing.Any]]] = None,
                from_: typing.Optional[builtins.str] = None,
                mfa_email: typing.Optional[typing.Union[CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmail, typing.Dict[str, typing.Any]]] = None,
                no_action_email: typing.Optional[typing.Union[CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmail, typing.Dict[str, typing.Any]]] = None,
                reply_to: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument source_arn", value=source_arn, expected_type=type_hints["source_arn"])
            check_type(argname="argument block_email", value=block_email, expected_type=type_hints["block_email"])
            check_type(argname="argument from_", value=from_, expected_type=type_hints["from_"])
            check_type(argname="argument mfa_email", value=mfa_email, expected_type=type_hints["mfa_email"])
            check_type(argname="argument no_action_email", value=no_action_email, expected_type=type_hints["no_action_email"])
            check_type(argname="argument reply_to", value=reply_to, expected_type=type_hints["reply_to"])
        self._values: typing.Dict[str, typing.Any] = {
            "source_arn": source_arn,
        }
        if block_email is not None:
            self._values["block_email"] = block_email
        if from_ is not None:
            self._values["from_"] = from_
        if mfa_email is not None:
            self._values["mfa_email"] = mfa_email
        if no_action_email is not None:
            self._values["no_action_email"] = no_action_email
        if reply_to is not None:
            self._values["reply_to"] = reply_to

    @builtins.property
    def source_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#source_arn CognitoRiskConfiguration#source_arn}.'''
        result = self._values.get("source_arn")
        assert result is not None, "Required property 'source_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def block_email(
        self,
    ) -> typing.Optional["CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmail"]:
        '''block_email block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#block_email CognitoRiskConfiguration#block_email}
        '''
        result = self._values.get("block_email")
        return typing.cast(typing.Optional["CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmail"], result)

    @builtins.property
    def from_(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#from CognitoRiskConfiguration#from}.'''
        result = self._values.get("from_")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mfa_email(
        self,
    ) -> typing.Optional["CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmail"]:
        '''mfa_email block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#mfa_email CognitoRiskConfiguration#mfa_email}
        '''
        result = self._values.get("mfa_email")
        return typing.cast(typing.Optional["CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmail"], result)

    @builtins.property
    def no_action_email(
        self,
    ) -> typing.Optional["CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmail"]:
        '''no_action_email block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#no_action_email CognitoRiskConfiguration#no_action_email}
        '''
        result = self._values.get("no_action_email")
        return typing.cast(typing.Optional["CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmail"], result)

    @builtins.property
    def reply_to(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#reply_to CognitoRiskConfiguration#reply_to}.'''
        result = self._values.get("reply_to")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.cognitoRiskConfiguration.CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmail",
    jsii_struct_bases=[],
    name_mapping={
        "html_body": "htmlBody",
        "subject": "subject",
        "text_body": "textBody",
    },
)
class CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmail:
    def __init__(
        self,
        *,
        html_body: builtins.str,
        subject: builtins.str,
        text_body: builtins.str,
    ) -> None:
        '''
        :param html_body: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#html_body CognitoRiskConfiguration#html_body}.
        :param subject: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#subject CognitoRiskConfiguration#subject}.
        :param text_body: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#text_body CognitoRiskConfiguration#text_body}.
        '''
        if __debug__:
            def stub(
                *,
                html_body: builtins.str,
                subject: builtins.str,
                text_body: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument html_body", value=html_body, expected_type=type_hints["html_body"])
            check_type(argname="argument subject", value=subject, expected_type=type_hints["subject"])
            check_type(argname="argument text_body", value=text_body, expected_type=type_hints["text_body"])
        self._values: typing.Dict[str, typing.Any] = {
            "html_body": html_body,
            "subject": subject,
            "text_body": text_body,
        }

    @builtins.property
    def html_body(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#html_body CognitoRiskConfiguration#html_body}.'''
        result = self._values.get("html_body")
        assert result is not None, "Required property 'html_body' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subject(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#subject CognitoRiskConfiguration#subject}.'''
        result = self._values.get("subject")
        assert result is not None, "Required property 'subject' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def text_body(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#text_body CognitoRiskConfiguration#text_body}.'''
        result = self._values.get("text_body")
        assert result is not None, "Required property 'text_body' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmail(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmailOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.cognitoRiskConfiguration.CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmailOutputReference",
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
    @jsii.member(jsii_name="htmlBodyInput")
    def html_body_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "htmlBodyInput"))

    @builtins.property
    @jsii.member(jsii_name="subjectInput")
    def subject_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subjectInput"))

    @builtins.property
    @jsii.member(jsii_name="textBodyInput")
    def text_body_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "textBodyInput"))

    @builtins.property
    @jsii.member(jsii_name="htmlBody")
    def html_body(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "htmlBody"))

    @html_body.setter
    def html_body(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "htmlBody", value)

    @builtins.property
    @jsii.member(jsii_name="subject")
    def subject(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subject"))

    @subject.setter
    def subject(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subject", value)

    @builtins.property
    @jsii.member(jsii_name="textBody")
    def text_body(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "textBody"))

    @text_body.setter
    def text_body(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "textBody", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmail]:
        return typing.cast(typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmail], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmail],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmail],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.cognitoRiskConfiguration.CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmail",
    jsii_struct_bases=[],
    name_mapping={
        "html_body": "htmlBody",
        "subject": "subject",
        "text_body": "textBody",
    },
)
class CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmail:
    def __init__(
        self,
        *,
        html_body: builtins.str,
        subject: builtins.str,
        text_body: builtins.str,
    ) -> None:
        '''
        :param html_body: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#html_body CognitoRiskConfiguration#html_body}.
        :param subject: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#subject CognitoRiskConfiguration#subject}.
        :param text_body: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#text_body CognitoRiskConfiguration#text_body}.
        '''
        if __debug__:
            def stub(
                *,
                html_body: builtins.str,
                subject: builtins.str,
                text_body: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument html_body", value=html_body, expected_type=type_hints["html_body"])
            check_type(argname="argument subject", value=subject, expected_type=type_hints["subject"])
            check_type(argname="argument text_body", value=text_body, expected_type=type_hints["text_body"])
        self._values: typing.Dict[str, typing.Any] = {
            "html_body": html_body,
            "subject": subject,
            "text_body": text_body,
        }

    @builtins.property
    def html_body(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#html_body CognitoRiskConfiguration#html_body}.'''
        result = self._values.get("html_body")
        assert result is not None, "Required property 'html_body' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subject(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#subject CognitoRiskConfiguration#subject}.'''
        result = self._values.get("subject")
        assert result is not None, "Required property 'subject' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def text_body(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#text_body CognitoRiskConfiguration#text_body}.'''
        result = self._values.get("text_body")
        assert result is not None, "Required property 'text_body' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmail(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmailOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.cognitoRiskConfiguration.CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmailOutputReference",
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
    @jsii.member(jsii_name="htmlBodyInput")
    def html_body_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "htmlBodyInput"))

    @builtins.property
    @jsii.member(jsii_name="subjectInput")
    def subject_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subjectInput"))

    @builtins.property
    @jsii.member(jsii_name="textBodyInput")
    def text_body_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "textBodyInput"))

    @builtins.property
    @jsii.member(jsii_name="htmlBody")
    def html_body(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "htmlBody"))

    @html_body.setter
    def html_body(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "htmlBody", value)

    @builtins.property
    @jsii.member(jsii_name="subject")
    def subject(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subject"))

    @subject.setter
    def subject(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subject", value)

    @builtins.property
    @jsii.member(jsii_name="textBody")
    def text_body(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "textBody"))

    @text_body.setter
    def text_body(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "textBody", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmail]:
        return typing.cast(typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmail], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmail],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmail],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.cognitoRiskConfiguration.CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmail",
    jsii_struct_bases=[],
    name_mapping={
        "html_body": "htmlBody",
        "subject": "subject",
        "text_body": "textBody",
    },
)
class CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmail:
    def __init__(
        self,
        *,
        html_body: builtins.str,
        subject: builtins.str,
        text_body: builtins.str,
    ) -> None:
        '''
        :param html_body: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#html_body CognitoRiskConfiguration#html_body}.
        :param subject: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#subject CognitoRiskConfiguration#subject}.
        :param text_body: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#text_body CognitoRiskConfiguration#text_body}.
        '''
        if __debug__:
            def stub(
                *,
                html_body: builtins.str,
                subject: builtins.str,
                text_body: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument html_body", value=html_body, expected_type=type_hints["html_body"])
            check_type(argname="argument subject", value=subject, expected_type=type_hints["subject"])
            check_type(argname="argument text_body", value=text_body, expected_type=type_hints["text_body"])
        self._values: typing.Dict[str, typing.Any] = {
            "html_body": html_body,
            "subject": subject,
            "text_body": text_body,
        }

    @builtins.property
    def html_body(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#html_body CognitoRiskConfiguration#html_body}.'''
        result = self._values.get("html_body")
        assert result is not None, "Required property 'html_body' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subject(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#subject CognitoRiskConfiguration#subject}.'''
        result = self._values.get("subject")
        assert result is not None, "Required property 'subject' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def text_body(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#text_body CognitoRiskConfiguration#text_body}.'''
        result = self._values.get("text_body")
        assert result is not None, "Required property 'text_body' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmail(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmailOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.cognitoRiskConfiguration.CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmailOutputReference",
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
    @jsii.member(jsii_name="htmlBodyInput")
    def html_body_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "htmlBodyInput"))

    @builtins.property
    @jsii.member(jsii_name="subjectInput")
    def subject_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subjectInput"))

    @builtins.property
    @jsii.member(jsii_name="textBodyInput")
    def text_body_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "textBodyInput"))

    @builtins.property
    @jsii.member(jsii_name="htmlBody")
    def html_body(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "htmlBody"))

    @html_body.setter
    def html_body(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "htmlBody", value)

    @builtins.property
    @jsii.member(jsii_name="subject")
    def subject(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subject"))

    @subject.setter
    def subject(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subject", value)

    @builtins.property
    @jsii.member(jsii_name="textBody")
    def text_body(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "textBody"))

    @text_body.setter
    def text_body(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "textBody", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmail]:
        return typing.cast(typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmail], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmail],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmail],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.cognitoRiskConfiguration.CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationOutputReference",
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

    @jsii.member(jsii_name="putBlockEmail")
    def put_block_email(
        self,
        *,
        html_body: builtins.str,
        subject: builtins.str,
        text_body: builtins.str,
    ) -> None:
        '''
        :param html_body: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#html_body CognitoRiskConfiguration#html_body}.
        :param subject: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#subject CognitoRiskConfiguration#subject}.
        :param text_body: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#text_body CognitoRiskConfiguration#text_body}.
        '''
        value = CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmail(
            html_body=html_body, subject=subject, text_body=text_body
        )

        return typing.cast(None, jsii.invoke(self, "putBlockEmail", [value]))

    @jsii.member(jsii_name="putMfaEmail")
    def put_mfa_email(
        self,
        *,
        html_body: builtins.str,
        subject: builtins.str,
        text_body: builtins.str,
    ) -> None:
        '''
        :param html_body: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#html_body CognitoRiskConfiguration#html_body}.
        :param subject: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#subject CognitoRiskConfiguration#subject}.
        :param text_body: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#text_body CognitoRiskConfiguration#text_body}.
        '''
        value = CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmail(
            html_body=html_body, subject=subject, text_body=text_body
        )

        return typing.cast(None, jsii.invoke(self, "putMfaEmail", [value]))

    @jsii.member(jsii_name="putNoActionEmail")
    def put_no_action_email(
        self,
        *,
        html_body: builtins.str,
        subject: builtins.str,
        text_body: builtins.str,
    ) -> None:
        '''
        :param html_body: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#html_body CognitoRiskConfiguration#html_body}.
        :param subject: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#subject CognitoRiskConfiguration#subject}.
        :param text_body: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#text_body CognitoRiskConfiguration#text_body}.
        '''
        value = CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmail(
            html_body=html_body, subject=subject, text_body=text_body
        )

        return typing.cast(None, jsii.invoke(self, "putNoActionEmail", [value]))

    @jsii.member(jsii_name="resetBlockEmail")
    def reset_block_email(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBlockEmail", []))

    @jsii.member(jsii_name="resetFrom")
    def reset_from(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFrom", []))

    @jsii.member(jsii_name="resetMfaEmail")
    def reset_mfa_email(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMfaEmail", []))

    @jsii.member(jsii_name="resetNoActionEmail")
    def reset_no_action_email(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNoActionEmail", []))

    @jsii.member(jsii_name="resetReplyTo")
    def reset_reply_to(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReplyTo", []))

    @builtins.property
    @jsii.member(jsii_name="blockEmail")
    def block_email(
        self,
    ) -> CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmailOutputReference:
        return typing.cast(CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmailOutputReference, jsii.get(self, "blockEmail"))

    @builtins.property
    @jsii.member(jsii_name="mfaEmail")
    def mfa_email(
        self,
    ) -> CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmailOutputReference:
        return typing.cast(CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmailOutputReference, jsii.get(self, "mfaEmail"))

    @builtins.property
    @jsii.member(jsii_name="noActionEmail")
    def no_action_email(
        self,
    ) -> CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmailOutputReference:
        return typing.cast(CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmailOutputReference, jsii.get(self, "noActionEmail"))

    @builtins.property
    @jsii.member(jsii_name="blockEmailInput")
    def block_email_input(
        self,
    ) -> typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmail]:
        return typing.cast(typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmail], jsii.get(self, "blockEmailInput"))

    @builtins.property
    @jsii.member(jsii_name="fromInput")
    def from_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fromInput"))

    @builtins.property
    @jsii.member(jsii_name="mfaEmailInput")
    def mfa_email_input(
        self,
    ) -> typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmail]:
        return typing.cast(typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmail], jsii.get(self, "mfaEmailInput"))

    @builtins.property
    @jsii.member(jsii_name="noActionEmailInput")
    def no_action_email_input(
        self,
    ) -> typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmail]:
        return typing.cast(typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmail], jsii.get(self, "noActionEmailInput"))

    @builtins.property
    @jsii.member(jsii_name="replyToInput")
    def reply_to_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "replyToInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceArnInput")
    def source_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceArnInput"))

    @builtins.property
    @jsii.member(jsii_name="from")
    def from_(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "from"))

    @from_.setter
    def from_(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "from", value)

    @builtins.property
    @jsii.member(jsii_name="replyTo")
    def reply_to(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "replyTo"))

    @reply_to.setter
    def reply_to(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replyTo", value)

    @builtins.property
    @jsii.member(jsii_name="sourceArn")
    def source_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceArn"))

    @source_arn.setter
    def source_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfiguration]:
        return typing.cast(typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfiguration],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfiguration],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CognitoRiskConfigurationAccountTakeoverRiskConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.cognitoRiskConfiguration.CognitoRiskConfigurationAccountTakeoverRiskConfigurationOutputReference",
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

    @jsii.member(jsii_name="putActions")
    def put_actions(
        self,
        *,
        high_action: typing.Optional[typing.Union[CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsHighAction, typing.Dict[str, typing.Any]]] = None,
        low_action: typing.Optional[typing.Union[CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsLowAction, typing.Dict[str, typing.Any]]] = None,
        medium_action: typing.Optional[typing.Union[CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumAction, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param high_action: high_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#high_action CognitoRiskConfiguration#high_action}
        :param low_action: low_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#low_action CognitoRiskConfiguration#low_action}
        :param medium_action: medium_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#medium_action CognitoRiskConfiguration#medium_action}
        '''
        value = CognitoRiskConfigurationAccountTakeoverRiskConfigurationActions(
            high_action=high_action, low_action=low_action, medium_action=medium_action
        )

        return typing.cast(None, jsii.invoke(self, "putActions", [value]))

    @jsii.member(jsii_name="putNotifyConfiguration")
    def put_notify_configuration(
        self,
        *,
        source_arn: builtins.str,
        block_email: typing.Optional[typing.Union[CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmail, typing.Dict[str, typing.Any]]] = None,
        from_: typing.Optional[builtins.str] = None,
        mfa_email: typing.Optional[typing.Union[CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmail, typing.Dict[str, typing.Any]]] = None,
        no_action_email: typing.Optional[typing.Union[CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmail, typing.Dict[str, typing.Any]]] = None,
        reply_to: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param source_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#source_arn CognitoRiskConfiguration#source_arn}.
        :param block_email: block_email block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#block_email CognitoRiskConfiguration#block_email}
        :param from_: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#from CognitoRiskConfiguration#from}.
        :param mfa_email: mfa_email block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#mfa_email CognitoRiskConfiguration#mfa_email}
        :param no_action_email: no_action_email block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#no_action_email CognitoRiskConfiguration#no_action_email}
        :param reply_to: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#reply_to CognitoRiskConfiguration#reply_to}.
        '''
        value = CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfiguration(
            source_arn=source_arn,
            block_email=block_email,
            from_=from_,
            mfa_email=mfa_email,
            no_action_email=no_action_email,
            reply_to=reply_to,
        )

        return typing.cast(None, jsii.invoke(self, "putNotifyConfiguration", [value]))

    @builtins.property
    @jsii.member(jsii_name="actions")
    def actions(
        self,
    ) -> CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsOutputReference:
        return typing.cast(CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsOutputReference, jsii.get(self, "actions"))

    @builtins.property
    @jsii.member(jsii_name="notifyConfiguration")
    def notify_configuration(
        self,
    ) -> CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationOutputReference:
        return typing.cast(CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationOutputReference, jsii.get(self, "notifyConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="actionsInput")
    def actions_input(
        self,
    ) -> typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationActions]:
        return typing.cast(typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationActions], jsii.get(self, "actionsInput"))

    @builtins.property
    @jsii.member(jsii_name="notifyConfigurationInput")
    def notify_configuration_input(
        self,
    ) -> typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfiguration]:
        return typing.cast(typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfiguration], jsii.get(self, "notifyConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfiguration]:
        return typing.cast(typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfiguration],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfiguration],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.cognitoRiskConfiguration.CognitoRiskConfigurationCompromisedCredentialsRiskConfiguration",
    jsii_struct_bases=[],
    name_mapping={"actions": "actions", "event_filter": "eventFilter"},
)
class CognitoRiskConfigurationCompromisedCredentialsRiskConfiguration:
    def __init__(
        self,
        *,
        actions: typing.Union["CognitoRiskConfigurationCompromisedCredentialsRiskConfigurationActions", typing.Dict[str, typing.Any]],
        event_filter: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param actions: actions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#actions CognitoRiskConfiguration#actions}
        :param event_filter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#event_filter CognitoRiskConfiguration#event_filter}.
        '''
        if isinstance(actions, dict):
            actions = CognitoRiskConfigurationCompromisedCredentialsRiskConfigurationActions(**actions)
        if __debug__:
            def stub(
                *,
                actions: typing.Union[CognitoRiskConfigurationCompromisedCredentialsRiskConfigurationActions, typing.Dict[str, typing.Any]],
                event_filter: typing.Optional[typing.Sequence[builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument actions", value=actions, expected_type=type_hints["actions"])
            check_type(argname="argument event_filter", value=event_filter, expected_type=type_hints["event_filter"])
        self._values: typing.Dict[str, typing.Any] = {
            "actions": actions,
        }
        if event_filter is not None:
            self._values["event_filter"] = event_filter

    @builtins.property
    def actions(
        self,
    ) -> "CognitoRiskConfigurationCompromisedCredentialsRiskConfigurationActions":
        '''actions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#actions CognitoRiskConfiguration#actions}
        '''
        result = self._values.get("actions")
        assert result is not None, "Required property 'actions' is missing"
        return typing.cast("CognitoRiskConfigurationCompromisedCredentialsRiskConfigurationActions", result)

    @builtins.property
    def event_filter(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#event_filter CognitoRiskConfiguration#event_filter}.'''
        result = self._values.get("event_filter")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CognitoRiskConfigurationCompromisedCredentialsRiskConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.cognitoRiskConfiguration.CognitoRiskConfigurationCompromisedCredentialsRiskConfigurationActions",
    jsii_struct_bases=[],
    name_mapping={"event_action": "eventAction"},
)
class CognitoRiskConfigurationCompromisedCredentialsRiskConfigurationActions:
    def __init__(self, *, event_action: builtins.str) -> None:
        '''
        :param event_action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#event_action CognitoRiskConfiguration#event_action}.
        '''
        if __debug__:
            def stub(*, event_action: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument event_action", value=event_action, expected_type=type_hints["event_action"])
        self._values: typing.Dict[str, typing.Any] = {
            "event_action": event_action,
        }

    @builtins.property
    def event_action(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#event_action CognitoRiskConfiguration#event_action}.'''
        result = self._values.get("event_action")
        assert result is not None, "Required property 'event_action' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CognitoRiskConfigurationCompromisedCredentialsRiskConfigurationActions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CognitoRiskConfigurationCompromisedCredentialsRiskConfigurationActionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.cognitoRiskConfiguration.CognitoRiskConfigurationCompromisedCredentialsRiskConfigurationActionsOutputReference",
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
    @jsii.member(jsii_name="eventActionInput")
    def event_action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "eventActionInput"))

    @builtins.property
    @jsii.member(jsii_name="eventAction")
    def event_action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "eventAction"))

    @event_action.setter
    def event_action(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventAction", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CognitoRiskConfigurationCompromisedCredentialsRiskConfigurationActions]:
        return typing.cast(typing.Optional[CognitoRiskConfigurationCompromisedCredentialsRiskConfigurationActions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CognitoRiskConfigurationCompromisedCredentialsRiskConfigurationActions],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CognitoRiskConfigurationCompromisedCredentialsRiskConfigurationActions],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CognitoRiskConfigurationCompromisedCredentialsRiskConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.cognitoRiskConfiguration.CognitoRiskConfigurationCompromisedCredentialsRiskConfigurationOutputReference",
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

    @jsii.member(jsii_name="putActions")
    def put_actions(self, *, event_action: builtins.str) -> None:
        '''
        :param event_action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#event_action CognitoRiskConfiguration#event_action}.
        '''
        value = CognitoRiskConfigurationCompromisedCredentialsRiskConfigurationActions(
            event_action=event_action
        )

        return typing.cast(None, jsii.invoke(self, "putActions", [value]))

    @jsii.member(jsii_name="resetEventFilter")
    def reset_event_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEventFilter", []))

    @builtins.property
    @jsii.member(jsii_name="actions")
    def actions(
        self,
    ) -> CognitoRiskConfigurationCompromisedCredentialsRiskConfigurationActionsOutputReference:
        return typing.cast(CognitoRiskConfigurationCompromisedCredentialsRiskConfigurationActionsOutputReference, jsii.get(self, "actions"))

    @builtins.property
    @jsii.member(jsii_name="actionsInput")
    def actions_input(
        self,
    ) -> typing.Optional[CognitoRiskConfigurationCompromisedCredentialsRiskConfigurationActions]:
        return typing.cast(typing.Optional[CognitoRiskConfigurationCompromisedCredentialsRiskConfigurationActions], jsii.get(self, "actionsInput"))

    @builtins.property
    @jsii.member(jsii_name="eventFilterInput")
    def event_filter_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "eventFilterInput"))

    @builtins.property
    @jsii.member(jsii_name="eventFilter")
    def event_filter(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "eventFilter"))

    @event_filter.setter
    def event_filter(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventFilter", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CognitoRiskConfigurationCompromisedCredentialsRiskConfiguration]:
        return typing.cast(typing.Optional[CognitoRiskConfigurationCompromisedCredentialsRiskConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CognitoRiskConfigurationCompromisedCredentialsRiskConfiguration],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CognitoRiskConfigurationCompromisedCredentialsRiskConfiguration],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.cognitoRiskConfiguration.CognitoRiskConfigurationConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "user_pool_id": "userPoolId",
        "account_takeover_risk_configuration": "accountTakeoverRiskConfiguration",
        "client_id": "clientId",
        "compromised_credentials_risk_configuration": "compromisedCredentialsRiskConfiguration",
        "id": "id",
        "risk_exception_configuration": "riskExceptionConfiguration",
    },
)
class CognitoRiskConfigurationConfig(cdktf.TerraformMetaArguments):
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
        user_pool_id: builtins.str,
        account_takeover_risk_configuration: typing.Optional[typing.Union[CognitoRiskConfigurationAccountTakeoverRiskConfiguration, typing.Dict[str, typing.Any]]] = None,
        client_id: typing.Optional[builtins.str] = None,
        compromised_credentials_risk_configuration: typing.Optional[typing.Union[CognitoRiskConfigurationCompromisedCredentialsRiskConfiguration, typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        risk_exception_configuration: typing.Optional[typing.Union["CognitoRiskConfigurationRiskExceptionConfiguration", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param user_pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#user_pool_id CognitoRiskConfiguration#user_pool_id}.
        :param account_takeover_risk_configuration: account_takeover_risk_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#account_takeover_risk_configuration CognitoRiskConfiguration#account_takeover_risk_configuration}
        :param client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#client_id CognitoRiskConfiguration#client_id}.
        :param compromised_credentials_risk_configuration: compromised_credentials_risk_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#compromised_credentials_risk_configuration CognitoRiskConfiguration#compromised_credentials_risk_configuration}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#id CognitoRiskConfiguration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param risk_exception_configuration: risk_exception_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#risk_exception_configuration CognitoRiskConfiguration#risk_exception_configuration}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(account_takeover_risk_configuration, dict):
            account_takeover_risk_configuration = CognitoRiskConfigurationAccountTakeoverRiskConfiguration(**account_takeover_risk_configuration)
        if isinstance(compromised_credentials_risk_configuration, dict):
            compromised_credentials_risk_configuration = CognitoRiskConfigurationCompromisedCredentialsRiskConfiguration(**compromised_credentials_risk_configuration)
        if isinstance(risk_exception_configuration, dict):
            risk_exception_configuration = CognitoRiskConfigurationRiskExceptionConfiguration(**risk_exception_configuration)
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
                user_pool_id: builtins.str,
                account_takeover_risk_configuration: typing.Optional[typing.Union[CognitoRiskConfigurationAccountTakeoverRiskConfiguration, typing.Dict[str, typing.Any]]] = None,
                client_id: typing.Optional[builtins.str] = None,
                compromised_credentials_risk_configuration: typing.Optional[typing.Union[CognitoRiskConfigurationCompromisedCredentialsRiskConfiguration, typing.Dict[str, typing.Any]]] = None,
                id: typing.Optional[builtins.str] = None,
                risk_exception_configuration: typing.Optional[typing.Union[CognitoRiskConfigurationRiskExceptionConfiguration, typing.Dict[str, typing.Any]]] = None,
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
            check_type(argname="argument user_pool_id", value=user_pool_id, expected_type=type_hints["user_pool_id"])
            check_type(argname="argument account_takeover_risk_configuration", value=account_takeover_risk_configuration, expected_type=type_hints["account_takeover_risk_configuration"])
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument compromised_credentials_risk_configuration", value=compromised_credentials_risk_configuration, expected_type=type_hints["compromised_credentials_risk_configuration"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument risk_exception_configuration", value=risk_exception_configuration, expected_type=type_hints["risk_exception_configuration"])
        self._values: typing.Dict[str, typing.Any] = {
            "user_pool_id": user_pool_id,
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
        if account_takeover_risk_configuration is not None:
            self._values["account_takeover_risk_configuration"] = account_takeover_risk_configuration
        if client_id is not None:
            self._values["client_id"] = client_id
        if compromised_credentials_risk_configuration is not None:
            self._values["compromised_credentials_risk_configuration"] = compromised_credentials_risk_configuration
        if id is not None:
            self._values["id"] = id
        if risk_exception_configuration is not None:
            self._values["risk_exception_configuration"] = risk_exception_configuration

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
    def user_pool_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#user_pool_id CognitoRiskConfiguration#user_pool_id}.'''
        result = self._values.get("user_pool_id")
        assert result is not None, "Required property 'user_pool_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def account_takeover_risk_configuration(
        self,
    ) -> typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfiguration]:
        '''account_takeover_risk_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#account_takeover_risk_configuration CognitoRiskConfiguration#account_takeover_risk_configuration}
        '''
        result = self._values.get("account_takeover_risk_configuration")
        return typing.cast(typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfiguration], result)

    @builtins.property
    def client_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#client_id CognitoRiskConfiguration#client_id}.'''
        result = self._values.get("client_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def compromised_credentials_risk_configuration(
        self,
    ) -> typing.Optional[CognitoRiskConfigurationCompromisedCredentialsRiskConfiguration]:
        '''compromised_credentials_risk_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#compromised_credentials_risk_configuration CognitoRiskConfiguration#compromised_credentials_risk_configuration}
        '''
        result = self._values.get("compromised_credentials_risk_configuration")
        return typing.cast(typing.Optional[CognitoRiskConfigurationCompromisedCredentialsRiskConfiguration], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#id CognitoRiskConfiguration#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def risk_exception_configuration(
        self,
    ) -> typing.Optional["CognitoRiskConfigurationRiskExceptionConfiguration"]:
        '''risk_exception_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#risk_exception_configuration CognitoRiskConfiguration#risk_exception_configuration}
        '''
        result = self._values.get("risk_exception_configuration")
        return typing.cast(typing.Optional["CognitoRiskConfigurationRiskExceptionConfiguration"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CognitoRiskConfigurationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.cognitoRiskConfiguration.CognitoRiskConfigurationRiskExceptionConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "blocked_ip_range_list": "blockedIpRangeList",
        "skipped_ip_range_list": "skippedIpRangeList",
    },
)
class CognitoRiskConfigurationRiskExceptionConfiguration:
    def __init__(
        self,
        *,
        blocked_ip_range_list: typing.Optional[typing.Sequence[builtins.str]] = None,
        skipped_ip_range_list: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param blocked_ip_range_list: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#blocked_ip_range_list CognitoRiskConfiguration#blocked_ip_range_list}.
        :param skipped_ip_range_list: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#skipped_ip_range_list CognitoRiskConfiguration#skipped_ip_range_list}.
        '''
        if __debug__:
            def stub(
                *,
                blocked_ip_range_list: typing.Optional[typing.Sequence[builtins.str]] = None,
                skipped_ip_range_list: typing.Optional[typing.Sequence[builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument blocked_ip_range_list", value=blocked_ip_range_list, expected_type=type_hints["blocked_ip_range_list"])
            check_type(argname="argument skipped_ip_range_list", value=skipped_ip_range_list, expected_type=type_hints["skipped_ip_range_list"])
        self._values: typing.Dict[str, typing.Any] = {}
        if blocked_ip_range_list is not None:
            self._values["blocked_ip_range_list"] = blocked_ip_range_list
        if skipped_ip_range_list is not None:
            self._values["skipped_ip_range_list"] = skipped_ip_range_list

    @builtins.property
    def blocked_ip_range_list(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#blocked_ip_range_list CognitoRiskConfiguration#blocked_ip_range_list}.'''
        result = self._values.get("blocked_ip_range_list")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def skipped_ip_range_list(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#skipped_ip_range_list CognitoRiskConfiguration#skipped_ip_range_list}.'''
        result = self._values.get("skipped_ip_range_list")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CognitoRiskConfigurationRiskExceptionConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CognitoRiskConfigurationRiskExceptionConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.cognitoRiskConfiguration.CognitoRiskConfigurationRiskExceptionConfigurationOutputReference",
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

    @jsii.member(jsii_name="resetBlockedIpRangeList")
    def reset_blocked_ip_range_list(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBlockedIpRangeList", []))

    @jsii.member(jsii_name="resetSkippedIpRangeList")
    def reset_skipped_ip_range_list(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSkippedIpRangeList", []))

    @builtins.property
    @jsii.member(jsii_name="blockedIpRangeListInput")
    def blocked_ip_range_list_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "blockedIpRangeListInput"))

    @builtins.property
    @jsii.member(jsii_name="skippedIpRangeListInput")
    def skipped_ip_range_list_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "skippedIpRangeListInput"))

    @builtins.property
    @jsii.member(jsii_name="blockedIpRangeList")
    def blocked_ip_range_list(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "blockedIpRangeList"))

    @blocked_ip_range_list.setter
    def blocked_ip_range_list(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "blockedIpRangeList", value)

    @builtins.property
    @jsii.member(jsii_name="skippedIpRangeList")
    def skipped_ip_range_list(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "skippedIpRangeList"))

    @skipped_ip_range_list.setter
    def skipped_ip_range_list(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "skippedIpRangeList", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CognitoRiskConfigurationRiskExceptionConfiguration]:
        return typing.cast(typing.Optional[CognitoRiskConfigurationRiskExceptionConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CognitoRiskConfigurationRiskExceptionConfiguration],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CognitoRiskConfigurationRiskExceptionConfiguration],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "CognitoRiskConfiguration",
    "CognitoRiskConfigurationAccountTakeoverRiskConfiguration",
    "CognitoRiskConfigurationAccountTakeoverRiskConfigurationActions",
    "CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsHighAction",
    "CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsHighActionOutputReference",
    "CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsLowAction",
    "CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsLowActionOutputReference",
    "CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumAction",
    "CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumActionOutputReference",
    "CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsOutputReference",
    "CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfiguration",
    "CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmail",
    "CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmailOutputReference",
    "CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmail",
    "CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmailOutputReference",
    "CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmail",
    "CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmailOutputReference",
    "CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationOutputReference",
    "CognitoRiskConfigurationAccountTakeoverRiskConfigurationOutputReference",
    "CognitoRiskConfigurationCompromisedCredentialsRiskConfiguration",
    "CognitoRiskConfigurationCompromisedCredentialsRiskConfigurationActions",
    "CognitoRiskConfigurationCompromisedCredentialsRiskConfigurationActionsOutputReference",
    "CognitoRiskConfigurationCompromisedCredentialsRiskConfigurationOutputReference",
    "CognitoRiskConfigurationConfig",
    "CognitoRiskConfigurationRiskExceptionConfiguration",
    "CognitoRiskConfigurationRiskExceptionConfigurationOutputReference",
]

publication.publish()
