'''
# `aws_lb_listener_rule`

Refer to the Terraform Registory for docs: [`aws_lb_listener_rule`](https://www.terraform.io/docs/providers/aws/r/lb_listener_rule).
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


class LbListenerRule(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lbListenerRule.LbListenerRule",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule aws_lb_listener_rule}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        action: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LbListenerRuleAction", typing.Dict[str, typing.Any]]]],
        condition: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LbListenerRuleCondition", typing.Dict[str, typing.Any]]]],
        listener_arn: builtins.str,
        id: typing.Optional[builtins.str] = None,
        priority: typing.Optional[jsii.Number] = None,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule aws_lb_listener_rule} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param action: action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#action LbListenerRule#action}
        :param condition: condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#condition LbListenerRule#condition}
        :param listener_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#listener_arn LbListenerRule#listener_arn}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#id LbListenerRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#priority LbListenerRule#priority}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#tags LbListenerRule#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#tags_all LbListenerRule#tags_all}.
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
                action: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LbListenerRuleAction, typing.Dict[str, typing.Any]]]],
                condition: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LbListenerRuleCondition, typing.Dict[str, typing.Any]]]],
                listener_arn: builtins.str,
                id: typing.Optional[builtins.str] = None,
                priority: typing.Optional[jsii.Number] = None,
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
        config = LbListenerRuleConfig(
            action=action,
            condition=condition,
            listener_arn=listener_arn,
            id=id,
            priority=priority,
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

    @jsii.member(jsii_name="putAction")
    def put_action(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LbListenerRuleAction", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LbListenerRuleAction, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAction", [value]))

    @jsii.member(jsii_name="putCondition")
    def put_condition(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LbListenerRuleCondition", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LbListenerRuleCondition, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCondition", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPriority")
    def reset_priority(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPriority", []))

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
    @jsii.member(jsii_name="action")
    def action(self) -> "LbListenerRuleActionList":
        return typing.cast("LbListenerRuleActionList", jsii.get(self, "action"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="condition")
    def condition(self) -> "LbListenerRuleConditionList":
        return typing.cast("LbListenerRuleConditionList", jsii.get(self, "condition"))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LbListenerRuleAction"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LbListenerRuleAction"]]], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="conditionInput")
    def condition_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LbListenerRuleCondition"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LbListenerRuleCondition"]]], jsii.get(self, "conditionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="listenerArnInput")
    def listener_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "listenerArnInput"))

    @builtins.property
    @jsii.member(jsii_name="priorityInput")
    def priority_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "priorityInput"))

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
    @jsii.member(jsii_name="listenerArn")
    def listener_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "listenerArn"))

    @listener_arn.setter
    def listener_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "listenerArn", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

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
    jsii_type="@cdktf/provider-aws.lbListenerRule.LbListenerRuleAction",
    jsii_struct_bases=[],
    name_mapping={
        "type": "type",
        "authenticate_cognito": "authenticateCognito",
        "authenticate_oidc": "authenticateOidc",
        "fixed_response": "fixedResponse",
        "forward": "forward",
        "order": "order",
        "redirect": "redirect",
        "target_group_arn": "targetGroupArn",
    },
)
class LbListenerRuleAction:
    def __init__(
        self,
        *,
        type: builtins.str,
        authenticate_cognito: typing.Optional[typing.Union["LbListenerRuleActionAuthenticateCognito", typing.Dict[str, typing.Any]]] = None,
        authenticate_oidc: typing.Optional[typing.Union["LbListenerRuleActionAuthenticateOidc", typing.Dict[str, typing.Any]]] = None,
        fixed_response: typing.Optional[typing.Union["LbListenerRuleActionFixedResponse", typing.Dict[str, typing.Any]]] = None,
        forward: typing.Optional[typing.Union["LbListenerRuleActionForward", typing.Dict[str, typing.Any]]] = None,
        order: typing.Optional[jsii.Number] = None,
        redirect: typing.Optional[typing.Union["LbListenerRuleActionRedirect", typing.Dict[str, typing.Any]]] = None,
        target_group_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#type LbListenerRule#type}.
        :param authenticate_cognito: authenticate_cognito block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#authenticate_cognito LbListenerRule#authenticate_cognito}
        :param authenticate_oidc: authenticate_oidc block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#authenticate_oidc LbListenerRule#authenticate_oidc}
        :param fixed_response: fixed_response block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#fixed_response LbListenerRule#fixed_response}
        :param forward: forward block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#forward LbListenerRule#forward}
        :param order: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#order LbListenerRule#order}.
        :param redirect: redirect block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#redirect LbListenerRule#redirect}
        :param target_group_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#target_group_arn LbListenerRule#target_group_arn}.
        '''
        if isinstance(authenticate_cognito, dict):
            authenticate_cognito = LbListenerRuleActionAuthenticateCognito(**authenticate_cognito)
        if isinstance(authenticate_oidc, dict):
            authenticate_oidc = LbListenerRuleActionAuthenticateOidc(**authenticate_oidc)
        if isinstance(fixed_response, dict):
            fixed_response = LbListenerRuleActionFixedResponse(**fixed_response)
        if isinstance(forward, dict):
            forward = LbListenerRuleActionForward(**forward)
        if isinstance(redirect, dict):
            redirect = LbListenerRuleActionRedirect(**redirect)
        if __debug__:
            def stub(
                *,
                type: builtins.str,
                authenticate_cognito: typing.Optional[typing.Union[LbListenerRuleActionAuthenticateCognito, typing.Dict[str, typing.Any]]] = None,
                authenticate_oidc: typing.Optional[typing.Union[LbListenerRuleActionAuthenticateOidc, typing.Dict[str, typing.Any]]] = None,
                fixed_response: typing.Optional[typing.Union[LbListenerRuleActionFixedResponse, typing.Dict[str, typing.Any]]] = None,
                forward: typing.Optional[typing.Union[LbListenerRuleActionForward, typing.Dict[str, typing.Any]]] = None,
                order: typing.Optional[jsii.Number] = None,
                redirect: typing.Optional[typing.Union[LbListenerRuleActionRedirect, typing.Dict[str, typing.Any]]] = None,
                target_group_arn: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument authenticate_cognito", value=authenticate_cognito, expected_type=type_hints["authenticate_cognito"])
            check_type(argname="argument authenticate_oidc", value=authenticate_oidc, expected_type=type_hints["authenticate_oidc"])
            check_type(argname="argument fixed_response", value=fixed_response, expected_type=type_hints["fixed_response"])
            check_type(argname="argument forward", value=forward, expected_type=type_hints["forward"])
            check_type(argname="argument order", value=order, expected_type=type_hints["order"])
            check_type(argname="argument redirect", value=redirect, expected_type=type_hints["redirect"])
            check_type(argname="argument target_group_arn", value=target_group_arn, expected_type=type_hints["target_group_arn"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if authenticate_cognito is not None:
            self._values["authenticate_cognito"] = authenticate_cognito
        if authenticate_oidc is not None:
            self._values["authenticate_oidc"] = authenticate_oidc
        if fixed_response is not None:
            self._values["fixed_response"] = fixed_response
        if forward is not None:
            self._values["forward"] = forward
        if order is not None:
            self._values["order"] = order
        if redirect is not None:
            self._values["redirect"] = redirect
        if target_group_arn is not None:
            self._values["target_group_arn"] = target_group_arn

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#type LbListenerRule#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def authenticate_cognito(
        self,
    ) -> typing.Optional["LbListenerRuleActionAuthenticateCognito"]:
        '''authenticate_cognito block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#authenticate_cognito LbListenerRule#authenticate_cognito}
        '''
        result = self._values.get("authenticate_cognito")
        return typing.cast(typing.Optional["LbListenerRuleActionAuthenticateCognito"], result)

    @builtins.property
    def authenticate_oidc(
        self,
    ) -> typing.Optional["LbListenerRuleActionAuthenticateOidc"]:
        '''authenticate_oidc block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#authenticate_oidc LbListenerRule#authenticate_oidc}
        '''
        result = self._values.get("authenticate_oidc")
        return typing.cast(typing.Optional["LbListenerRuleActionAuthenticateOidc"], result)

    @builtins.property
    def fixed_response(self) -> typing.Optional["LbListenerRuleActionFixedResponse"]:
        '''fixed_response block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#fixed_response LbListenerRule#fixed_response}
        '''
        result = self._values.get("fixed_response")
        return typing.cast(typing.Optional["LbListenerRuleActionFixedResponse"], result)

    @builtins.property
    def forward(self) -> typing.Optional["LbListenerRuleActionForward"]:
        '''forward block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#forward LbListenerRule#forward}
        '''
        result = self._values.get("forward")
        return typing.cast(typing.Optional["LbListenerRuleActionForward"], result)

    @builtins.property
    def order(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#order LbListenerRule#order}.'''
        result = self._values.get("order")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def redirect(self) -> typing.Optional["LbListenerRuleActionRedirect"]:
        '''redirect block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#redirect LbListenerRule#redirect}
        '''
        result = self._values.get("redirect")
        return typing.cast(typing.Optional["LbListenerRuleActionRedirect"], result)

    @builtins.property
    def target_group_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#target_group_arn LbListenerRule#target_group_arn}.'''
        result = self._values.get("target_group_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LbListenerRuleAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lbListenerRule.LbListenerRuleActionAuthenticateCognito",
    jsii_struct_bases=[],
    name_mapping={
        "user_pool_arn": "userPoolArn",
        "user_pool_client_id": "userPoolClientId",
        "user_pool_domain": "userPoolDomain",
        "authentication_request_extra_params": "authenticationRequestExtraParams",
        "on_unauthenticated_request": "onUnauthenticatedRequest",
        "scope": "scope",
        "session_cookie_name": "sessionCookieName",
        "session_timeout": "sessionTimeout",
    },
)
class LbListenerRuleActionAuthenticateCognito:
    def __init__(
        self,
        *,
        user_pool_arn: builtins.str,
        user_pool_client_id: builtins.str,
        user_pool_domain: builtins.str,
        authentication_request_extra_params: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        on_unauthenticated_request: typing.Optional[builtins.str] = None,
        scope: typing.Optional[builtins.str] = None,
        session_cookie_name: typing.Optional[builtins.str] = None,
        session_timeout: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param user_pool_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#user_pool_arn LbListenerRule#user_pool_arn}.
        :param user_pool_client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#user_pool_client_id LbListenerRule#user_pool_client_id}.
        :param user_pool_domain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#user_pool_domain LbListenerRule#user_pool_domain}.
        :param authentication_request_extra_params: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#authentication_request_extra_params LbListenerRule#authentication_request_extra_params}.
        :param on_unauthenticated_request: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#on_unauthenticated_request LbListenerRule#on_unauthenticated_request}.
        :param scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#scope LbListenerRule#scope}.
        :param session_cookie_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#session_cookie_name LbListenerRule#session_cookie_name}.
        :param session_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#session_timeout LbListenerRule#session_timeout}.
        '''
        if __debug__:
            def stub(
                *,
                user_pool_arn: builtins.str,
                user_pool_client_id: builtins.str,
                user_pool_domain: builtins.str,
                authentication_request_extra_params: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                on_unauthenticated_request: typing.Optional[builtins.str] = None,
                scope: typing.Optional[builtins.str] = None,
                session_cookie_name: typing.Optional[builtins.str] = None,
                session_timeout: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument user_pool_arn", value=user_pool_arn, expected_type=type_hints["user_pool_arn"])
            check_type(argname="argument user_pool_client_id", value=user_pool_client_id, expected_type=type_hints["user_pool_client_id"])
            check_type(argname="argument user_pool_domain", value=user_pool_domain, expected_type=type_hints["user_pool_domain"])
            check_type(argname="argument authentication_request_extra_params", value=authentication_request_extra_params, expected_type=type_hints["authentication_request_extra_params"])
            check_type(argname="argument on_unauthenticated_request", value=on_unauthenticated_request, expected_type=type_hints["on_unauthenticated_request"])
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument session_cookie_name", value=session_cookie_name, expected_type=type_hints["session_cookie_name"])
            check_type(argname="argument session_timeout", value=session_timeout, expected_type=type_hints["session_timeout"])
        self._values: typing.Dict[str, typing.Any] = {
            "user_pool_arn": user_pool_arn,
            "user_pool_client_id": user_pool_client_id,
            "user_pool_domain": user_pool_domain,
        }
        if authentication_request_extra_params is not None:
            self._values["authentication_request_extra_params"] = authentication_request_extra_params
        if on_unauthenticated_request is not None:
            self._values["on_unauthenticated_request"] = on_unauthenticated_request
        if scope is not None:
            self._values["scope"] = scope
        if session_cookie_name is not None:
            self._values["session_cookie_name"] = session_cookie_name
        if session_timeout is not None:
            self._values["session_timeout"] = session_timeout

    @builtins.property
    def user_pool_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#user_pool_arn LbListenerRule#user_pool_arn}.'''
        result = self._values.get("user_pool_arn")
        assert result is not None, "Required property 'user_pool_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_pool_client_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#user_pool_client_id LbListenerRule#user_pool_client_id}.'''
        result = self._values.get("user_pool_client_id")
        assert result is not None, "Required property 'user_pool_client_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_pool_domain(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#user_pool_domain LbListenerRule#user_pool_domain}.'''
        result = self._values.get("user_pool_domain")
        assert result is not None, "Required property 'user_pool_domain' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def authentication_request_extra_params(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#authentication_request_extra_params LbListenerRule#authentication_request_extra_params}.'''
        result = self._values.get("authentication_request_extra_params")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def on_unauthenticated_request(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#on_unauthenticated_request LbListenerRule#on_unauthenticated_request}.'''
        result = self._values.get("on_unauthenticated_request")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scope(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#scope LbListenerRule#scope}.'''
        result = self._values.get("scope")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def session_cookie_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#session_cookie_name LbListenerRule#session_cookie_name}.'''
        result = self._values.get("session_cookie_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def session_timeout(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#session_timeout LbListenerRule#session_timeout}.'''
        result = self._values.get("session_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LbListenerRuleActionAuthenticateCognito(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LbListenerRuleActionAuthenticateCognitoOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lbListenerRule.LbListenerRuleActionAuthenticateCognitoOutputReference",
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

    @jsii.member(jsii_name="resetAuthenticationRequestExtraParams")
    def reset_authentication_request_extra_params(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthenticationRequestExtraParams", []))

    @jsii.member(jsii_name="resetOnUnauthenticatedRequest")
    def reset_on_unauthenticated_request(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOnUnauthenticatedRequest", []))

    @jsii.member(jsii_name="resetScope")
    def reset_scope(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScope", []))

    @jsii.member(jsii_name="resetSessionCookieName")
    def reset_session_cookie_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSessionCookieName", []))

    @jsii.member(jsii_name="resetSessionTimeout")
    def reset_session_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSessionTimeout", []))

    @builtins.property
    @jsii.member(jsii_name="authenticationRequestExtraParamsInput")
    def authentication_request_extra_params_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "authenticationRequestExtraParamsInput"))

    @builtins.property
    @jsii.member(jsii_name="onUnauthenticatedRequestInput")
    def on_unauthenticated_request_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "onUnauthenticatedRequestInput"))

    @builtins.property
    @jsii.member(jsii_name="scopeInput")
    def scope_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scopeInput"))

    @builtins.property
    @jsii.member(jsii_name="sessionCookieNameInput")
    def session_cookie_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sessionCookieNameInput"))

    @builtins.property
    @jsii.member(jsii_name="sessionTimeoutInput")
    def session_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sessionTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="userPoolArnInput")
    def user_pool_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userPoolArnInput"))

    @builtins.property
    @jsii.member(jsii_name="userPoolClientIdInput")
    def user_pool_client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userPoolClientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="userPoolDomainInput")
    def user_pool_domain_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userPoolDomainInput"))

    @builtins.property
    @jsii.member(jsii_name="authenticationRequestExtraParams")
    def authentication_request_extra_params(
        self,
    ) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "authenticationRequestExtraParams"))

    @authentication_request_extra_params.setter
    def authentication_request_extra_params(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            def stub(value: typing.Mapping[builtins.str, builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authenticationRequestExtraParams", value)

    @builtins.property
    @jsii.member(jsii_name="onUnauthenticatedRequest")
    def on_unauthenticated_request(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "onUnauthenticatedRequest"))

    @on_unauthenticated_request.setter
    def on_unauthenticated_request(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "onUnauthenticatedRequest", value)

    @builtins.property
    @jsii.member(jsii_name="scope")
    def scope(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scope"))

    @scope.setter
    def scope(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scope", value)

    @builtins.property
    @jsii.member(jsii_name="sessionCookieName")
    def session_cookie_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sessionCookieName"))

    @session_cookie_name.setter
    def session_cookie_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sessionCookieName", value)

    @builtins.property
    @jsii.member(jsii_name="sessionTimeout")
    def session_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sessionTimeout"))

    @session_timeout.setter
    def session_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sessionTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="userPoolArn")
    def user_pool_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userPoolArn"))

    @user_pool_arn.setter
    def user_pool_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userPoolArn", value)

    @builtins.property
    @jsii.member(jsii_name="userPoolClientId")
    def user_pool_client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userPoolClientId"))

    @user_pool_client_id.setter
    def user_pool_client_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userPoolClientId", value)

    @builtins.property
    @jsii.member(jsii_name="userPoolDomain")
    def user_pool_domain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userPoolDomain"))

    @user_pool_domain.setter
    def user_pool_domain(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userPoolDomain", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LbListenerRuleActionAuthenticateCognito]:
        return typing.cast(typing.Optional[LbListenerRuleActionAuthenticateCognito], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LbListenerRuleActionAuthenticateCognito],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[LbListenerRuleActionAuthenticateCognito],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lbListenerRule.LbListenerRuleActionAuthenticateOidc",
    jsii_struct_bases=[],
    name_mapping={
        "authorization_endpoint": "authorizationEndpoint",
        "client_id": "clientId",
        "client_secret": "clientSecret",
        "issuer": "issuer",
        "token_endpoint": "tokenEndpoint",
        "user_info_endpoint": "userInfoEndpoint",
        "authentication_request_extra_params": "authenticationRequestExtraParams",
        "on_unauthenticated_request": "onUnauthenticatedRequest",
        "scope": "scope",
        "session_cookie_name": "sessionCookieName",
        "session_timeout": "sessionTimeout",
    },
)
class LbListenerRuleActionAuthenticateOidc:
    def __init__(
        self,
        *,
        authorization_endpoint: builtins.str,
        client_id: builtins.str,
        client_secret: builtins.str,
        issuer: builtins.str,
        token_endpoint: builtins.str,
        user_info_endpoint: builtins.str,
        authentication_request_extra_params: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        on_unauthenticated_request: typing.Optional[builtins.str] = None,
        scope: typing.Optional[builtins.str] = None,
        session_cookie_name: typing.Optional[builtins.str] = None,
        session_timeout: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param authorization_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#authorization_endpoint LbListenerRule#authorization_endpoint}.
        :param client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#client_id LbListenerRule#client_id}.
        :param client_secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#client_secret LbListenerRule#client_secret}.
        :param issuer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#issuer LbListenerRule#issuer}.
        :param token_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#token_endpoint LbListenerRule#token_endpoint}.
        :param user_info_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#user_info_endpoint LbListenerRule#user_info_endpoint}.
        :param authentication_request_extra_params: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#authentication_request_extra_params LbListenerRule#authentication_request_extra_params}.
        :param on_unauthenticated_request: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#on_unauthenticated_request LbListenerRule#on_unauthenticated_request}.
        :param scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#scope LbListenerRule#scope}.
        :param session_cookie_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#session_cookie_name LbListenerRule#session_cookie_name}.
        :param session_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#session_timeout LbListenerRule#session_timeout}.
        '''
        if __debug__:
            def stub(
                *,
                authorization_endpoint: builtins.str,
                client_id: builtins.str,
                client_secret: builtins.str,
                issuer: builtins.str,
                token_endpoint: builtins.str,
                user_info_endpoint: builtins.str,
                authentication_request_extra_params: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                on_unauthenticated_request: typing.Optional[builtins.str] = None,
                scope: typing.Optional[builtins.str] = None,
                session_cookie_name: typing.Optional[builtins.str] = None,
                session_timeout: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument authorization_endpoint", value=authorization_endpoint, expected_type=type_hints["authorization_endpoint"])
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument client_secret", value=client_secret, expected_type=type_hints["client_secret"])
            check_type(argname="argument issuer", value=issuer, expected_type=type_hints["issuer"])
            check_type(argname="argument token_endpoint", value=token_endpoint, expected_type=type_hints["token_endpoint"])
            check_type(argname="argument user_info_endpoint", value=user_info_endpoint, expected_type=type_hints["user_info_endpoint"])
            check_type(argname="argument authentication_request_extra_params", value=authentication_request_extra_params, expected_type=type_hints["authentication_request_extra_params"])
            check_type(argname="argument on_unauthenticated_request", value=on_unauthenticated_request, expected_type=type_hints["on_unauthenticated_request"])
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument session_cookie_name", value=session_cookie_name, expected_type=type_hints["session_cookie_name"])
            check_type(argname="argument session_timeout", value=session_timeout, expected_type=type_hints["session_timeout"])
        self._values: typing.Dict[str, typing.Any] = {
            "authorization_endpoint": authorization_endpoint,
            "client_id": client_id,
            "client_secret": client_secret,
            "issuer": issuer,
            "token_endpoint": token_endpoint,
            "user_info_endpoint": user_info_endpoint,
        }
        if authentication_request_extra_params is not None:
            self._values["authentication_request_extra_params"] = authentication_request_extra_params
        if on_unauthenticated_request is not None:
            self._values["on_unauthenticated_request"] = on_unauthenticated_request
        if scope is not None:
            self._values["scope"] = scope
        if session_cookie_name is not None:
            self._values["session_cookie_name"] = session_cookie_name
        if session_timeout is not None:
            self._values["session_timeout"] = session_timeout

    @builtins.property
    def authorization_endpoint(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#authorization_endpoint LbListenerRule#authorization_endpoint}.'''
        result = self._values.get("authorization_endpoint")
        assert result is not None, "Required property 'authorization_endpoint' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#client_id LbListenerRule#client_id}.'''
        result = self._values.get("client_id")
        assert result is not None, "Required property 'client_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_secret(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#client_secret LbListenerRule#client_secret}.'''
        result = self._values.get("client_secret")
        assert result is not None, "Required property 'client_secret' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def issuer(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#issuer LbListenerRule#issuer}.'''
        result = self._values.get("issuer")
        assert result is not None, "Required property 'issuer' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def token_endpoint(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#token_endpoint LbListenerRule#token_endpoint}.'''
        result = self._values.get("token_endpoint")
        assert result is not None, "Required property 'token_endpoint' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_info_endpoint(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#user_info_endpoint LbListenerRule#user_info_endpoint}.'''
        result = self._values.get("user_info_endpoint")
        assert result is not None, "Required property 'user_info_endpoint' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def authentication_request_extra_params(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#authentication_request_extra_params LbListenerRule#authentication_request_extra_params}.'''
        result = self._values.get("authentication_request_extra_params")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def on_unauthenticated_request(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#on_unauthenticated_request LbListenerRule#on_unauthenticated_request}.'''
        result = self._values.get("on_unauthenticated_request")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scope(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#scope LbListenerRule#scope}.'''
        result = self._values.get("scope")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def session_cookie_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#session_cookie_name LbListenerRule#session_cookie_name}.'''
        result = self._values.get("session_cookie_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def session_timeout(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#session_timeout LbListenerRule#session_timeout}.'''
        result = self._values.get("session_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LbListenerRuleActionAuthenticateOidc(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LbListenerRuleActionAuthenticateOidcOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lbListenerRule.LbListenerRuleActionAuthenticateOidcOutputReference",
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

    @jsii.member(jsii_name="resetAuthenticationRequestExtraParams")
    def reset_authentication_request_extra_params(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthenticationRequestExtraParams", []))

    @jsii.member(jsii_name="resetOnUnauthenticatedRequest")
    def reset_on_unauthenticated_request(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOnUnauthenticatedRequest", []))

    @jsii.member(jsii_name="resetScope")
    def reset_scope(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScope", []))

    @jsii.member(jsii_name="resetSessionCookieName")
    def reset_session_cookie_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSessionCookieName", []))

    @jsii.member(jsii_name="resetSessionTimeout")
    def reset_session_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSessionTimeout", []))

    @builtins.property
    @jsii.member(jsii_name="authenticationRequestExtraParamsInput")
    def authentication_request_extra_params_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "authenticationRequestExtraParamsInput"))

    @builtins.property
    @jsii.member(jsii_name="authorizationEndpointInput")
    def authorization_endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authorizationEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="clientIdInput")
    def client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="clientSecretInput")
    def client_secret_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientSecretInput"))

    @builtins.property
    @jsii.member(jsii_name="issuerInput")
    def issuer_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "issuerInput"))

    @builtins.property
    @jsii.member(jsii_name="onUnauthenticatedRequestInput")
    def on_unauthenticated_request_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "onUnauthenticatedRequestInput"))

    @builtins.property
    @jsii.member(jsii_name="scopeInput")
    def scope_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scopeInput"))

    @builtins.property
    @jsii.member(jsii_name="sessionCookieNameInput")
    def session_cookie_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sessionCookieNameInput"))

    @builtins.property
    @jsii.member(jsii_name="sessionTimeoutInput")
    def session_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sessionTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenEndpointInput")
    def token_endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="userInfoEndpointInput")
    def user_info_endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userInfoEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="authenticationRequestExtraParams")
    def authentication_request_extra_params(
        self,
    ) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "authenticationRequestExtraParams"))

    @authentication_request_extra_params.setter
    def authentication_request_extra_params(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            def stub(value: typing.Mapping[builtins.str, builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authenticationRequestExtraParams", value)

    @builtins.property
    @jsii.member(jsii_name="authorizationEndpoint")
    def authorization_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authorizationEndpoint"))

    @authorization_endpoint.setter
    def authorization_endpoint(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorizationEndpoint", value)

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
    @jsii.member(jsii_name="clientSecret")
    def client_secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecret"))

    @client_secret.setter
    def client_secret(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecret", value)

    @builtins.property
    @jsii.member(jsii_name="issuer")
    def issuer(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "issuer"))

    @issuer.setter
    def issuer(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "issuer", value)

    @builtins.property
    @jsii.member(jsii_name="onUnauthenticatedRequest")
    def on_unauthenticated_request(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "onUnauthenticatedRequest"))

    @on_unauthenticated_request.setter
    def on_unauthenticated_request(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "onUnauthenticatedRequest", value)

    @builtins.property
    @jsii.member(jsii_name="scope")
    def scope(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scope"))

    @scope.setter
    def scope(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scope", value)

    @builtins.property
    @jsii.member(jsii_name="sessionCookieName")
    def session_cookie_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sessionCookieName"))

    @session_cookie_name.setter
    def session_cookie_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sessionCookieName", value)

    @builtins.property
    @jsii.member(jsii_name="sessionTimeout")
    def session_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sessionTimeout"))

    @session_timeout.setter
    def session_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sessionTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="tokenEndpoint")
    def token_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tokenEndpoint"))

    @token_endpoint.setter
    def token_endpoint(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="userInfoEndpoint")
    def user_info_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userInfoEndpoint"))

    @user_info_endpoint.setter
    def user_info_endpoint(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userInfoEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LbListenerRuleActionAuthenticateOidc]:
        return typing.cast(typing.Optional[LbListenerRuleActionAuthenticateOidc], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LbListenerRuleActionAuthenticateOidc],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[LbListenerRuleActionAuthenticateOidc],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lbListenerRule.LbListenerRuleActionFixedResponse",
    jsii_struct_bases=[],
    name_mapping={
        "content_type": "contentType",
        "message_body": "messageBody",
        "status_code": "statusCode",
    },
)
class LbListenerRuleActionFixedResponse:
    def __init__(
        self,
        *,
        content_type: builtins.str,
        message_body: typing.Optional[builtins.str] = None,
        status_code: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param content_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#content_type LbListenerRule#content_type}.
        :param message_body: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#message_body LbListenerRule#message_body}.
        :param status_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#status_code LbListenerRule#status_code}.
        '''
        if __debug__:
            def stub(
                *,
                content_type: builtins.str,
                message_body: typing.Optional[builtins.str] = None,
                status_code: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument content_type", value=content_type, expected_type=type_hints["content_type"])
            check_type(argname="argument message_body", value=message_body, expected_type=type_hints["message_body"])
            check_type(argname="argument status_code", value=status_code, expected_type=type_hints["status_code"])
        self._values: typing.Dict[str, typing.Any] = {
            "content_type": content_type,
        }
        if message_body is not None:
            self._values["message_body"] = message_body
        if status_code is not None:
            self._values["status_code"] = status_code

    @builtins.property
    def content_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#content_type LbListenerRule#content_type}.'''
        result = self._values.get("content_type")
        assert result is not None, "Required property 'content_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def message_body(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#message_body LbListenerRule#message_body}.'''
        result = self._values.get("message_body")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status_code(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#status_code LbListenerRule#status_code}.'''
        result = self._values.get("status_code")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LbListenerRuleActionFixedResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LbListenerRuleActionFixedResponseOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lbListenerRule.LbListenerRuleActionFixedResponseOutputReference",
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

    @jsii.member(jsii_name="resetMessageBody")
    def reset_message_body(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMessageBody", []))

    @jsii.member(jsii_name="resetStatusCode")
    def reset_status_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatusCode", []))

    @builtins.property
    @jsii.member(jsii_name="contentTypeInput")
    def content_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="messageBodyInput")
    def message_body_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "messageBodyInput"))

    @builtins.property
    @jsii.member(jsii_name="statusCodeInput")
    def status_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="contentType")
    def content_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentType"))

    @content_type.setter
    def content_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentType", value)

    @builtins.property
    @jsii.member(jsii_name="messageBody")
    def message_body(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "messageBody"))

    @message_body.setter
    def message_body(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "messageBody", value)

    @builtins.property
    @jsii.member(jsii_name="statusCode")
    def status_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "statusCode"))

    @status_code.setter
    def status_code(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "statusCode", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LbListenerRuleActionFixedResponse]:
        return typing.cast(typing.Optional[LbListenerRuleActionFixedResponse], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LbListenerRuleActionFixedResponse],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[LbListenerRuleActionFixedResponse]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lbListenerRule.LbListenerRuleActionForward",
    jsii_struct_bases=[],
    name_mapping={"target_group": "targetGroup", "stickiness": "stickiness"},
)
class LbListenerRuleActionForward:
    def __init__(
        self,
        *,
        target_group: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LbListenerRuleActionForwardTargetGroup", typing.Dict[str, typing.Any]]]],
        stickiness: typing.Optional[typing.Union["LbListenerRuleActionForwardStickiness", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param target_group: target_group block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#target_group LbListenerRule#target_group}
        :param stickiness: stickiness block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#stickiness LbListenerRule#stickiness}
        '''
        if isinstance(stickiness, dict):
            stickiness = LbListenerRuleActionForwardStickiness(**stickiness)
        if __debug__:
            def stub(
                *,
                target_group: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LbListenerRuleActionForwardTargetGroup, typing.Dict[str, typing.Any]]]],
                stickiness: typing.Optional[typing.Union[LbListenerRuleActionForwardStickiness, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument target_group", value=target_group, expected_type=type_hints["target_group"])
            check_type(argname="argument stickiness", value=stickiness, expected_type=type_hints["stickiness"])
        self._values: typing.Dict[str, typing.Any] = {
            "target_group": target_group,
        }
        if stickiness is not None:
            self._values["stickiness"] = stickiness

    @builtins.property
    def target_group(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["LbListenerRuleActionForwardTargetGroup"]]:
        '''target_group block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#target_group LbListenerRule#target_group}
        '''
        result = self._values.get("target_group")
        assert result is not None, "Required property 'target_group' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["LbListenerRuleActionForwardTargetGroup"]], result)

    @builtins.property
    def stickiness(self) -> typing.Optional["LbListenerRuleActionForwardStickiness"]:
        '''stickiness block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#stickiness LbListenerRule#stickiness}
        '''
        result = self._values.get("stickiness")
        return typing.cast(typing.Optional["LbListenerRuleActionForwardStickiness"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LbListenerRuleActionForward(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LbListenerRuleActionForwardOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lbListenerRule.LbListenerRuleActionForwardOutputReference",
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

    @jsii.member(jsii_name="putStickiness")
    def put_stickiness(
        self,
        *,
        duration: jsii.Number,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#duration LbListenerRule#duration}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#enabled LbListenerRule#enabled}.
        '''
        value = LbListenerRuleActionForwardStickiness(
            duration=duration, enabled=enabled
        )

        return typing.cast(None, jsii.invoke(self, "putStickiness", [value]))

    @jsii.member(jsii_name="putTargetGroup")
    def put_target_group(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LbListenerRuleActionForwardTargetGroup", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LbListenerRuleActionForwardTargetGroup, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTargetGroup", [value]))

    @jsii.member(jsii_name="resetStickiness")
    def reset_stickiness(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStickiness", []))

    @builtins.property
    @jsii.member(jsii_name="stickiness")
    def stickiness(self) -> "LbListenerRuleActionForwardStickinessOutputReference":
        return typing.cast("LbListenerRuleActionForwardStickinessOutputReference", jsii.get(self, "stickiness"))

    @builtins.property
    @jsii.member(jsii_name="targetGroup")
    def target_group(self) -> "LbListenerRuleActionForwardTargetGroupList":
        return typing.cast("LbListenerRuleActionForwardTargetGroupList", jsii.get(self, "targetGroup"))

    @builtins.property
    @jsii.member(jsii_name="stickinessInput")
    def stickiness_input(
        self,
    ) -> typing.Optional["LbListenerRuleActionForwardStickiness"]:
        return typing.cast(typing.Optional["LbListenerRuleActionForwardStickiness"], jsii.get(self, "stickinessInput"))

    @builtins.property
    @jsii.member(jsii_name="targetGroupInput")
    def target_group_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LbListenerRuleActionForwardTargetGroup"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LbListenerRuleActionForwardTargetGroup"]]], jsii.get(self, "targetGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LbListenerRuleActionForward]:
        return typing.cast(typing.Optional[LbListenerRuleActionForward], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LbListenerRuleActionForward],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[LbListenerRuleActionForward]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lbListenerRule.LbListenerRuleActionForwardStickiness",
    jsii_struct_bases=[],
    name_mapping={"duration": "duration", "enabled": "enabled"},
)
class LbListenerRuleActionForwardStickiness:
    def __init__(
        self,
        *,
        duration: jsii.Number,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#duration LbListenerRule#duration}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#enabled LbListenerRule#enabled}.
        '''
        if __debug__:
            def stub(
                *,
                duration: jsii.Number,
                enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument duration", value=duration, expected_type=type_hints["duration"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[str, typing.Any] = {
            "duration": duration,
        }
        if enabled is not None:
            self._values["enabled"] = enabled

    @builtins.property
    def duration(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#duration LbListenerRule#duration}.'''
        result = self._values.get("duration")
        assert result is not None, "Required property 'duration' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#enabled LbListenerRule#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LbListenerRuleActionForwardStickiness(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LbListenerRuleActionForwardStickinessOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lbListenerRule.LbListenerRuleActionForwardStickinessOutputReference",
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

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="durationInput")
    def duration_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "durationInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="duration")
    def duration(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "duration"))

    @duration.setter
    def duration(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "duration", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LbListenerRuleActionForwardStickiness]:
        return typing.cast(typing.Optional[LbListenerRuleActionForwardStickiness], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LbListenerRuleActionForwardStickiness],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[LbListenerRuleActionForwardStickiness],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lbListenerRule.LbListenerRuleActionForwardTargetGroup",
    jsii_struct_bases=[],
    name_mapping={"arn": "arn", "weight": "weight"},
)
class LbListenerRuleActionForwardTargetGroup:
    def __init__(
        self,
        *,
        arn: builtins.str,
        weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#arn LbListenerRule#arn}.
        :param weight: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#weight LbListenerRule#weight}.
        '''
        if __debug__:
            def stub(
                *,
                arn: builtins.str,
                weight: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
            check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
        self._values: typing.Dict[str, typing.Any] = {
            "arn": arn,
        }
        if weight is not None:
            self._values["weight"] = weight

    @builtins.property
    def arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#arn LbListenerRule#arn}.'''
        result = self._values.get("arn")
        assert result is not None, "Required property 'arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def weight(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#weight LbListenerRule#weight}.'''
        result = self._values.get("weight")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LbListenerRuleActionForwardTargetGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LbListenerRuleActionForwardTargetGroupList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lbListenerRule.LbListenerRuleActionForwardTargetGroupList",
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
    ) -> "LbListenerRuleActionForwardTargetGroupOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LbListenerRuleActionForwardTargetGroupOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LbListenerRuleActionForwardTargetGroup]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LbListenerRuleActionForwardTargetGroup]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LbListenerRuleActionForwardTargetGroup]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LbListenerRuleActionForwardTargetGroup]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LbListenerRuleActionForwardTargetGroupOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lbListenerRule.LbListenerRuleActionForwardTargetGroupOutputReference",
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

    @jsii.member(jsii_name="resetWeight")
    def reset_weight(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWeight", []))

    @builtins.property
    @jsii.member(jsii_name="arnInput")
    def arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "arnInput"))

    @builtins.property
    @jsii.member(jsii_name="weightInput")
    def weight_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "weightInput"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @arn.setter
    def arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "arn", value)

    @builtins.property
    @jsii.member(jsii_name="weight")
    def weight(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "weight"))

    @weight.setter
    def weight(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "weight", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LbListenerRuleActionForwardTargetGroup, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LbListenerRuleActionForwardTargetGroup, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LbListenerRuleActionForwardTargetGroup, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[LbListenerRuleActionForwardTargetGroup, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LbListenerRuleActionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lbListenerRule.LbListenerRuleActionList",
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
    def get(self, index: jsii.Number) -> "LbListenerRuleActionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LbListenerRuleActionOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LbListenerRuleAction]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LbListenerRuleAction]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LbListenerRuleAction]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LbListenerRuleAction]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LbListenerRuleActionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lbListenerRule.LbListenerRuleActionOutputReference",
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

    @jsii.member(jsii_name="putAuthenticateCognito")
    def put_authenticate_cognito(
        self,
        *,
        user_pool_arn: builtins.str,
        user_pool_client_id: builtins.str,
        user_pool_domain: builtins.str,
        authentication_request_extra_params: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        on_unauthenticated_request: typing.Optional[builtins.str] = None,
        scope: typing.Optional[builtins.str] = None,
        session_cookie_name: typing.Optional[builtins.str] = None,
        session_timeout: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param user_pool_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#user_pool_arn LbListenerRule#user_pool_arn}.
        :param user_pool_client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#user_pool_client_id LbListenerRule#user_pool_client_id}.
        :param user_pool_domain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#user_pool_domain LbListenerRule#user_pool_domain}.
        :param authentication_request_extra_params: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#authentication_request_extra_params LbListenerRule#authentication_request_extra_params}.
        :param on_unauthenticated_request: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#on_unauthenticated_request LbListenerRule#on_unauthenticated_request}.
        :param scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#scope LbListenerRule#scope}.
        :param session_cookie_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#session_cookie_name LbListenerRule#session_cookie_name}.
        :param session_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#session_timeout LbListenerRule#session_timeout}.
        '''
        value = LbListenerRuleActionAuthenticateCognito(
            user_pool_arn=user_pool_arn,
            user_pool_client_id=user_pool_client_id,
            user_pool_domain=user_pool_domain,
            authentication_request_extra_params=authentication_request_extra_params,
            on_unauthenticated_request=on_unauthenticated_request,
            scope=scope,
            session_cookie_name=session_cookie_name,
            session_timeout=session_timeout,
        )

        return typing.cast(None, jsii.invoke(self, "putAuthenticateCognito", [value]))

    @jsii.member(jsii_name="putAuthenticateOidc")
    def put_authenticate_oidc(
        self,
        *,
        authorization_endpoint: builtins.str,
        client_id: builtins.str,
        client_secret: builtins.str,
        issuer: builtins.str,
        token_endpoint: builtins.str,
        user_info_endpoint: builtins.str,
        authentication_request_extra_params: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        on_unauthenticated_request: typing.Optional[builtins.str] = None,
        scope: typing.Optional[builtins.str] = None,
        session_cookie_name: typing.Optional[builtins.str] = None,
        session_timeout: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param authorization_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#authorization_endpoint LbListenerRule#authorization_endpoint}.
        :param client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#client_id LbListenerRule#client_id}.
        :param client_secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#client_secret LbListenerRule#client_secret}.
        :param issuer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#issuer LbListenerRule#issuer}.
        :param token_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#token_endpoint LbListenerRule#token_endpoint}.
        :param user_info_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#user_info_endpoint LbListenerRule#user_info_endpoint}.
        :param authentication_request_extra_params: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#authentication_request_extra_params LbListenerRule#authentication_request_extra_params}.
        :param on_unauthenticated_request: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#on_unauthenticated_request LbListenerRule#on_unauthenticated_request}.
        :param scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#scope LbListenerRule#scope}.
        :param session_cookie_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#session_cookie_name LbListenerRule#session_cookie_name}.
        :param session_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#session_timeout LbListenerRule#session_timeout}.
        '''
        value = LbListenerRuleActionAuthenticateOidc(
            authorization_endpoint=authorization_endpoint,
            client_id=client_id,
            client_secret=client_secret,
            issuer=issuer,
            token_endpoint=token_endpoint,
            user_info_endpoint=user_info_endpoint,
            authentication_request_extra_params=authentication_request_extra_params,
            on_unauthenticated_request=on_unauthenticated_request,
            scope=scope,
            session_cookie_name=session_cookie_name,
            session_timeout=session_timeout,
        )

        return typing.cast(None, jsii.invoke(self, "putAuthenticateOidc", [value]))

    @jsii.member(jsii_name="putFixedResponse")
    def put_fixed_response(
        self,
        *,
        content_type: builtins.str,
        message_body: typing.Optional[builtins.str] = None,
        status_code: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param content_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#content_type LbListenerRule#content_type}.
        :param message_body: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#message_body LbListenerRule#message_body}.
        :param status_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#status_code LbListenerRule#status_code}.
        '''
        value = LbListenerRuleActionFixedResponse(
            content_type=content_type,
            message_body=message_body,
            status_code=status_code,
        )

        return typing.cast(None, jsii.invoke(self, "putFixedResponse", [value]))

    @jsii.member(jsii_name="putForward")
    def put_forward(
        self,
        *,
        target_group: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LbListenerRuleActionForwardTargetGroup, typing.Dict[str, typing.Any]]]],
        stickiness: typing.Optional[typing.Union[LbListenerRuleActionForwardStickiness, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param target_group: target_group block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#target_group LbListenerRule#target_group}
        :param stickiness: stickiness block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#stickiness LbListenerRule#stickiness}
        '''
        value = LbListenerRuleActionForward(
            target_group=target_group, stickiness=stickiness
        )

        return typing.cast(None, jsii.invoke(self, "putForward", [value]))

    @jsii.member(jsii_name="putRedirect")
    def put_redirect(
        self,
        *,
        status_code: builtins.str,
        host: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
        port: typing.Optional[builtins.str] = None,
        protocol: typing.Optional[builtins.str] = None,
        query: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param status_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#status_code LbListenerRule#status_code}.
        :param host: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#host LbListenerRule#host}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#path LbListenerRule#path}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#port LbListenerRule#port}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#protocol LbListenerRule#protocol}.
        :param query: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#query LbListenerRule#query}.
        '''
        value = LbListenerRuleActionRedirect(
            status_code=status_code,
            host=host,
            path=path,
            port=port,
            protocol=protocol,
            query=query,
        )

        return typing.cast(None, jsii.invoke(self, "putRedirect", [value]))

    @jsii.member(jsii_name="resetAuthenticateCognito")
    def reset_authenticate_cognito(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthenticateCognito", []))

    @jsii.member(jsii_name="resetAuthenticateOidc")
    def reset_authenticate_oidc(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthenticateOidc", []))

    @jsii.member(jsii_name="resetFixedResponse")
    def reset_fixed_response(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFixedResponse", []))

    @jsii.member(jsii_name="resetForward")
    def reset_forward(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForward", []))

    @jsii.member(jsii_name="resetOrder")
    def reset_order(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOrder", []))

    @jsii.member(jsii_name="resetRedirect")
    def reset_redirect(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedirect", []))

    @jsii.member(jsii_name="resetTargetGroupArn")
    def reset_target_group_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetGroupArn", []))

    @builtins.property
    @jsii.member(jsii_name="authenticateCognito")
    def authenticate_cognito(
        self,
    ) -> LbListenerRuleActionAuthenticateCognitoOutputReference:
        return typing.cast(LbListenerRuleActionAuthenticateCognitoOutputReference, jsii.get(self, "authenticateCognito"))

    @builtins.property
    @jsii.member(jsii_name="authenticateOidc")
    def authenticate_oidc(self) -> LbListenerRuleActionAuthenticateOidcOutputReference:
        return typing.cast(LbListenerRuleActionAuthenticateOidcOutputReference, jsii.get(self, "authenticateOidc"))

    @builtins.property
    @jsii.member(jsii_name="fixedResponse")
    def fixed_response(self) -> LbListenerRuleActionFixedResponseOutputReference:
        return typing.cast(LbListenerRuleActionFixedResponseOutputReference, jsii.get(self, "fixedResponse"))

    @builtins.property
    @jsii.member(jsii_name="forward")
    def forward(self) -> LbListenerRuleActionForwardOutputReference:
        return typing.cast(LbListenerRuleActionForwardOutputReference, jsii.get(self, "forward"))

    @builtins.property
    @jsii.member(jsii_name="redirect")
    def redirect(self) -> "LbListenerRuleActionRedirectOutputReference":
        return typing.cast("LbListenerRuleActionRedirectOutputReference", jsii.get(self, "redirect"))

    @builtins.property
    @jsii.member(jsii_name="authenticateCognitoInput")
    def authenticate_cognito_input(
        self,
    ) -> typing.Optional[LbListenerRuleActionAuthenticateCognito]:
        return typing.cast(typing.Optional[LbListenerRuleActionAuthenticateCognito], jsii.get(self, "authenticateCognitoInput"))

    @builtins.property
    @jsii.member(jsii_name="authenticateOidcInput")
    def authenticate_oidc_input(
        self,
    ) -> typing.Optional[LbListenerRuleActionAuthenticateOidc]:
        return typing.cast(typing.Optional[LbListenerRuleActionAuthenticateOidc], jsii.get(self, "authenticateOidcInput"))

    @builtins.property
    @jsii.member(jsii_name="fixedResponseInput")
    def fixed_response_input(
        self,
    ) -> typing.Optional[LbListenerRuleActionFixedResponse]:
        return typing.cast(typing.Optional[LbListenerRuleActionFixedResponse], jsii.get(self, "fixedResponseInput"))

    @builtins.property
    @jsii.member(jsii_name="forwardInput")
    def forward_input(self) -> typing.Optional[LbListenerRuleActionForward]:
        return typing.cast(typing.Optional[LbListenerRuleActionForward], jsii.get(self, "forwardInput"))

    @builtins.property
    @jsii.member(jsii_name="orderInput")
    def order_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "orderInput"))

    @builtins.property
    @jsii.member(jsii_name="redirectInput")
    def redirect_input(self) -> typing.Optional["LbListenerRuleActionRedirect"]:
        return typing.cast(typing.Optional["LbListenerRuleActionRedirect"], jsii.get(self, "redirectInput"))

    @builtins.property
    @jsii.member(jsii_name="targetGroupArnInput")
    def target_group_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetGroupArnInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="order")
    def order(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "order"))

    @order.setter
    def order(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "order", value)

    @builtins.property
    @jsii.member(jsii_name="targetGroupArn")
    def target_group_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetGroupArn"))

    @target_group_arn.setter
    def target_group_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetGroupArn", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LbListenerRuleAction, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LbListenerRuleAction, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LbListenerRuleAction, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[LbListenerRuleAction, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lbListenerRule.LbListenerRuleActionRedirect",
    jsii_struct_bases=[],
    name_mapping={
        "status_code": "statusCode",
        "host": "host",
        "path": "path",
        "port": "port",
        "protocol": "protocol",
        "query": "query",
    },
)
class LbListenerRuleActionRedirect:
    def __init__(
        self,
        *,
        status_code: builtins.str,
        host: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
        port: typing.Optional[builtins.str] = None,
        protocol: typing.Optional[builtins.str] = None,
        query: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param status_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#status_code LbListenerRule#status_code}.
        :param host: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#host LbListenerRule#host}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#path LbListenerRule#path}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#port LbListenerRule#port}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#protocol LbListenerRule#protocol}.
        :param query: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#query LbListenerRule#query}.
        '''
        if __debug__:
            def stub(
                *,
                status_code: builtins.str,
                host: typing.Optional[builtins.str] = None,
                path: typing.Optional[builtins.str] = None,
                port: typing.Optional[builtins.str] = None,
                protocol: typing.Optional[builtins.str] = None,
                query: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument status_code", value=status_code, expected_type=type_hints["status_code"])
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument query", value=query, expected_type=type_hints["query"])
        self._values: typing.Dict[str, typing.Any] = {
            "status_code": status_code,
        }
        if host is not None:
            self._values["host"] = host
        if path is not None:
            self._values["path"] = path
        if port is not None:
            self._values["port"] = port
        if protocol is not None:
            self._values["protocol"] = protocol
        if query is not None:
            self._values["query"] = query

    @builtins.property
    def status_code(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#status_code LbListenerRule#status_code}.'''
        result = self._values.get("status_code")
        assert result is not None, "Required property 'status_code' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def host(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#host LbListenerRule#host}.'''
        result = self._values.get("host")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#path LbListenerRule#path}.'''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#port LbListenerRule#port}.'''
        result = self._values.get("port")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def protocol(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#protocol LbListenerRule#protocol}.'''
        result = self._values.get("protocol")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def query(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#query LbListenerRule#query}.'''
        result = self._values.get("query")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LbListenerRuleActionRedirect(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LbListenerRuleActionRedirectOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lbListenerRule.LbListenerRuleActionRedirectOutputReference",
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

    @jsii.member(jsii_name="resetHost")
    def reset_host(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHost", []))

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @jsii.member(jsii_name="resetPort")
    def reset_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPort", []))

    @jsii.member(jsii_name="resetProtocol")
    def reset_protocol(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProtocol", []))

    @jsii.member(jsii_name="resetQuery")
    def reset_query(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQuery", []))

    @builtins.property
    @jsii.member(jsii_name="hostInput")
    def host_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="queryInput")
    def query_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryInput"))

    @builtins.property
    @jsii.member(jsii_name="statusCodeInput")
    def status_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="host")
    def host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "host"))

    @host.setter
    def host(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "host", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "port"))

    @port.setter
    def port(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="query")
    def query(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "query"))

    @query.setter
    def query(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "query", value)

    @builtins.property
    @jsii.member(jsii_name="statusCode")
    def status_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "statusCode"))

    @status_code.setter
    def status_code(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "statusCode", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LbListenerRuleActionRedirect]:
        return typing.cast(typing.Optional[LbListenerRuleActionRedirect], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LbListenerRuleActionRedirect],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[LbListenerRuleActionRedirect]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lbListenerRule.LbListenerRuleCondition",
    jsii_struct_bases=[],
    name_mapping={
        "host_header": "hostHeader",
        "http_header": "httpHeader",
        "http_request_method": "httpRequestMethod",
        "path_pattern": "pathPattern",
        "query_string": "queryString",
        "source_ip": "sourceIp",
    },
)
class LbListenerRuleCondition:
    def __init__(
        self,
        *,
        host_header: typing.Optional[typing.Union["LbListenerRuleConditionHostHeader", typing.Dict[str, typing.Any]]] = None,
        http_header: typing.Optional[typing.Union["LbListenerRuleConditionHttpHeader", typing.Dict[str, typing.Any]]] = None,
        http_request_method: typing.Optional[typing.Union["LbListenerRuleConditionHttpRequestMethod", typing.Dict[str, typing.Any]]] = None,
        path_pattern: typing.Optional[typing.Union["LbListenerRuleConditionPathPattern", typing.Dict[str, typing.Any]]] = None,
        query_string: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LbListenerRuleConditionQueryString", typing.Dict[str, typing.Any]]]]] = None,
        source_ip: typing.Optional[typing.Union["LbListenerRuleConditionSourceIp", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param host_header: host_header block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#host_header LbListenerRule#host_header}
        :param http_header: http_header block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#http_header LbListenerRule#http_header}
        :param http_request_method: http_request_method block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#http_request_method LbListenerRule#http_request_method}
        :param path_pattern: path_pattern block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#path_pattern LbListenerRule#path_pattern}
        :param query_string: query_string block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#query_string LbListenerRule#query_string}
        :param source_ip: source_ip block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#source_ip LbListenerRule#source_ip}
        '''
        if isinstance(host_header, dict):
            host_header = LbListenerRuleConditionHostHeader(**host_header)
        if isinstance(http_header, dict):
            http_header = LbListenerRuleConditionHttpHeader(**http_header)
        if isinstance(http_request_method, dict):
            http_request_method = LbListenerRuleConditionHttpRequestMethod(**http_request_method)
        if isinstance(path_pattern, dict):
            path_pattern = LbListenerRuleConditionPathPattern(**path_pattern)
        if isinstance(source_ip, dict):
            source_ip = LbListenerRuleConditionSourceIp(**source_ip)
        if __debug__:
            def stub(
                *,
                host_header: typing.Optional[typing.Union[LbListenerRuleConditionHostHeader, typing.Dict[str, typing.Any]]] = None,
                http_header: typing.Optional[typing.Union[LbListenerRuleConditionHttpHeader, typing.Dict[str, typing.Any]]] = None,
                http_request_method: typing.Optional[typing.Union[LbListenerRuleConditionHttpRequestMethod, typing.Dict[str, typing.Any]]] = None,
                path_pattern: typing.Optional[typing.Union[LbListenerRuleConditionPathPattern, typing.Dict[str, typing.Any]]] = None,
                query_string: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LbListenerRuleConditionQueryString, typing.Dict[str, typing.Any]]]]] = None,
                source_ip: typing.Optional[typing.Union[LbListenerRuleConditionSourceIp, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument host_header", value=host_header, expected_type=type_hints["host_header"])
            check_type(argname="argument http_header", value=http_header, expected_type=type_hints["http_header"])
            check_type(argname="argument http_request_method", value=http_request_method, expected_type=type_hints["http_request_method"])
            check_type(argname="argument path_pattern", value=path_pattern, expected_type=type_hints["path_pattern"])
            check_type(argname="argument query_string", value=query_string, expected_type=type_hints["query_string"])
            check_type(argname="argument source_ip", value=source_ip, expected_type=type_hints["source_ip"])
        self._values: typing.Dict[str, typing.Any] = {}
        if host_header is not None:
            self._values["host_header"] = host_header
        if http_header is not None:
            self._values["http_header"] = http_header
        if http_request_method is not None:
            self._values["http_request_method"] = http_request_method
        if path_pattern is not None:
            self._values["path_pattern"] = path_pattern
        if query_string is not None:
            self._values["query_string"] = query_string
        if source_ip is not None:
            self._values["source_ip"] = source_ip

    @builtins.property
    def host_header(self) -> typing.Optional["LbListenerRuleConditionHostHeader"]:
        '''host_header block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#host_header LbListenerRule#host_header}
        '''
        result = self._values.get("host_header")
        return typing.cast(typing.Optional["LbListenerRuleConditionHostHeader"], result)

    @builtins.property
    def http_header(self) -> typing.Optional["LbListenerRuleConditionHttpHeader"]:
        '''http_header block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#http_header LbListenerRule#http_header}
        '''
        result = self._values.get("http_header")
        return typing.cast(typing.Optional["LbListenerRuleConditionHttpHeader"], result)

    @builtins.property
    def http_request_method(
        self,
    ) -> typing.Optional["LbListenerRuleConditionHttpRequestMethod"]:
        '''http_request_method block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#http_request_method LbListenerRule#http_request_method}
        '''
        result = self._values.get("http_request_method")
        return typing.cast(typing.Optional["LbListenerRuleConditionHttpRequestMethod"], result)

    @builtins.property
    def path_pattern(self) -> typing.Optional["LbListenerRuleConditionPathPattern"]:
        '''path_pattern block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#path_pattern LbListenerRule#path_pattern}
        '''
        result = self._values.get("path_pattern")
        return typing.cast(typing.Optional["LbListenerRuleConditionPathPattern"], result)

    @builtins.property
    def query_string(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LbListenerRuleConditionQueryString"]]]:
        '''query_string block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#query_string LbListenerRule#query_string}
        '''
        result = self._values.get("query_string")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LbListenerRuleConditionQueryString"]]], result)

    @builtins.property
    def source_ip(self) -> typing.Optional["LbListenerRuleConditionSourceIp"]:
        '''source_ip block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#source_ip LbListenerRule#source_ip}
        '''
        result = self._values.get("source_ip")
        return typing.cast(typing.Optional["LbListenerRuleConditionSourceIp"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LbListenerRuleCondition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lbListenerRule.LbListenerRuleConditionHostHeader",
    jsii_struct_bases=[],
    name_mapping={"values": "values"},
)
class LbListenerRuleConditionHostHeader:
    def __init__(self, *, values: typing.Sequence[builtins.str]) -> None:
        '''
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#values LbListenerRule#values}.
        '''
        if __debug__:
            def stub(*, values: typing.Sequence[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "values": values,
        }

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#values LbListenerRule#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LbListenerRuleConditionHostHeader(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LbListenerRuleConditionHostHeaderOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lbListenerRule.LbListenerRuleConditionHostHeaderOutputReference",
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
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LbListenerRuleConditionHostHeader]:
        return typing.cast(typing.Optional[LbListenerRuleConditionHostHeader], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LbListenerRuleConditionHostHeader],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[LbListenerRuleConditionHostHeader]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lbListenerRule.LbListenerRuleConditionHttpHeader",
    jsii_struct_bases=[],
    name_mapping={"http_header_name": "httpHeaderName", "values": "values"},
)
class LbListenerRuleConditionHttpHeader:
    def __init__(
        self,
        *,
        http_header_name: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param http_header_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#http_header_name LbListenerRule#http_header_name}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#values LbListenerRule#values}.
        '''
        if __debug__:
            def stub(
                *,
                http_header_name: builtins.str,
                values: typing.Sequence[builtins.str],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument http_header_name", value=http_header_name, expected_type=type_hints["http_header_name"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "http_header_name": http_header_name,
            "values": values,
        }

    @builtins.property
    def http_header_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#http_header_name LbListenerRule#http_header_name}.'''
        result = self._values.get("http_header_name")
        assert result is not None, "Required property 'http_header_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#values LbListenerRule#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LbListenerRuleConditionHttpHeader(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LbListenerRuleConditionHttpHeaderOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lbListenerRule.LbListenerRuleConditionHttpHeaderOutputReference",
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
    @jsii.member(jsii_name="httpHeaderNameInput")
    def http_header_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "httpHeaderNameInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="httpHeaderName")
    def http_header_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "httpHeaderName"))

    @http_header_name.setter
    def http_header_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpHeaderName", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LbListenerRuleConditionHttpHeader]:
        return typing.cast(typing.Optional[LbListenerRuleConditionHttpHeader], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LbListenerRuleConditionHttpHeader],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[LbListenerRuleConditionHttpHeader]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lbListenerRule.LbListenerRuleConditionHttpRequestMethod",
    jsii_struct_bases=[],
    name_mapping={"values": "values"},
)
class LbListenerRuleConditionHttpRequestMethod:
    def __init__(self, *, values: typing.Sequence[builtins.str]) -> None:
        '''
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#values LbListenerRule#values}.
        '''
        if __debug__:
            def stub(*, values: typing.Sequence[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "values": values,
        }

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#values LbListenerRule#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LbListenerRuleConditionHttpRequestMethod(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LbListenerRuleConditionHttpRequestMethodOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lbListenerRule.LbListenerRuleConditionHttpRequestMethodOutputReference",
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
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LbListenerRuleConditionHttpRequestMethod]:
        return typing.cast(typing.Optional[LbListenerRuleConditionHttpRequestMethod], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LbListenerRuleConditionHttpRequestMethod],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[LbListenerRuleConditionHttpRequestMethod],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LbListenerRuleConditionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lbListenerRule.LbListenerRuleConditionList",
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
    def get(self, index: jsii.Number) -> "LbListenerRuleConditionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LbListenerRuleConditionOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LbListenerRuleCondition]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LbListenerRuleCondition]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LbListenerRuleCondition]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LbListenerRuleCondition]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LbListenerRuleConditionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lbListenerRule.LbListenerRuleConditionOutputReference",
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

    @jsii.member(jsii_name="putHostHeader")
    def put_host_header(self, *, values: typing.Sequence[builtins.str]) -> None:
        '''
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#values LbListenerRule#values}.
        '''
        value = LbListenerRuleConditionHostHeader(values=values)

        return typing.cast(None, jsii.invoke(self, "putHostHeader", [value]))

    @jsii.member(jsii_name="putHttpHeader")
    def put_http_header(
        self,
        *,
        http_header_name: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param http_header_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#http_header_name LbListenerRule#http_header_name}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#values LbListenerRule#values}.
        '''
        value = LbListenerRuleConditionHttpHeader(
            http_header_name=http_header_name, values=values
        )

        return typing.cast(None, jsii.invoke(self, "putHttpHeader", [value]))

    @jsii.member(jsii_name="putHttpRequestMethod")
    def put_http_request_method(self, *, values: typing.Sequence[builtins.str]) -> None:
        '''
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#values LbListenerRule#values}.
        '''
        value = LbListenerRuleConditionHttpRequestMethod(values=values)

        return typing.cast(None, jsii.invoke(self, "putHttpRequestMethod", [value]))

    @jsii.member(jsii_name="putPathPattern")
    def put_path_pattern(self, *, values: typing.Sequence[builtins.str]) -> None:
        '''
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#values LbListenerRule#values}.
        '''
        value = LbListenerRuleConditionPathPattern(values=values)

        return typing.cast(None, jsii.invoke(self, "putPathPattern", [value]))

    @jsii.member(jsii_name="putQueryString")
    def put_query_string(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LbListenerRuleConditionQueryString", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LbListenerRuleConditionQueryString, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putQueryString", [value]))

    @jsii.member(jsii_name="putSourceIp")
    def put_source_ip(self, *, values: typing.Sequence[builtins.str]) -> None:
        '''
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#values LbListenerRule#values}.
        '''
        value = LbListenerRuleConditionSourceIp(values=values)

        return typing.cast(None, jsii.invoke(self, "putSourceIp", [value]))

    @jsii.member(jsii_name="resetHostHeader")
    def reset_host_header(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostHeader", []))

    @jsii.member(jsii_name="resetHttpHeader")
    def reset_http_header(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpHeader", []))

    @jsii.member(jsii_name="resetHttpRequestMethod")
    def reset_http_request_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpRequestMethod", []))

    @jsii.member(jsii_name="resetPathPattern")
    def reset_path_pattern(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPathPattern", []))

    @jsii.member(jsii_name="resetQueryString")
    def reset_query_string(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryString", []))

    @jsii.member(jsii_name="resetSourceIp")
    def reset_source_ip(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceIp", []))

    @builtins.property
    @jsii.member(jsii_name="hostHeader")
    def host_header(self) -> LbListenerRuleConditionHostHeaderOutputReference:
        return typing.cast(LbListenerRuleConditionHostHeaderOutputReference, jsii.get(self, "hostHeader"))

    @builtins.property
    @jsii.member(jsii_name="httpHeader")
    def http_header(self) -> LbListenerRuleConditionHttpHeaderOutputReference:
        return typing.cast(LbListenerRuleConditionHttpHeaderOutputReference, jsii.get(self, "httpHeader"))

    @builtins.property
    @jsii.member(jsii_name="httpRequestMethod")
    def http_request_method(
        self,
    ) -> LbListenerRuleConditionHttpRequestMethodOutputReference:
        return typing.cast(LbListenerRuleConditionHttpRequestMethodOutputReference, jsii.get(self, "httpRequestMethod"))

    @builtins.property
    @jsii.member(jsii_name="pathPattern")
    def path_pattern(self) -> "LbListenerRuleConditionPathPatternOutputReference":
        return typing.cast("LbListenerRuleConditionPathPatternOutputReference", jsii.get(self, "pathPattern"))

    @builtins.property
    @jsii.member(jsii_name="queryString")
    def query_string(self) -> "LbListenerRuleConditionQueryStringList":
        return typing.cast("LbListenerRuleConditionQueryStringList", jsii.get(self, "queryString"))

    @builtins.property
    @jsii.member(jsii_name="sourceIp")
    def source_ip(self) -> "LbListenerRuleConditionSourceIpOutputReference":
        return typing.cast("LbListenerRuleConditionSourceIpOutputReference", jsii.get(self, "sourceIp"))

    @builtins.property
    @jsii.member(jsii_name="hostHeaderInput")
    def host_header_input(self) -> typing.Optional[LbListenerRuleConditionHostHeader]:
        return typing.cast(typing.Optional[LbListenerRuleConditionHostHeader], jsii.get(self, "hostHeaderInput"))

    @builtins.property
    @jsii.member(jsii_name="httpHeaderInput")
    def http_header_input(self) -> typing.Optional[LbListenerRuleConditionHttpHeader]:
        return typing.cast(typing.Optional[LbListenerRuleConditionHttpHeader], jsii.get(self, "httpHeaderInput"))

    @builtins.property
    @jsii.member(jsii_name="httpRequestMethodInput")
    def http_request_method_input(
        self,
    ) -> typing.Optional[LbListenerRuleConditionHttpRequestMethod]:
        return typing.cast(typing.Optional[LbListenerRuleConditionHttpRequestMethod], jsii.get(self, "httpRequestMethodInput"))

    @builtins.property
    @jsii.member(jsii_name="pathPatternInput")
    def path_pattern_input(
        self,
    ) -> typing.Optional["LbListenerRuleConditionPathPattern"]:
        return typing.cast(typing.Optional["LbListenerRuleConditionPathPattern"], jsii.get(self, "pathPatternInput"))

    @builtins.property
    @jsii.member(jsii_name="queryStringInput")
    def query_string_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LbListenerRuleConditionQueryString"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LbListenerRuleConditionQueryString"]]], jsii.get(self, "queryStringInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceIpInput")
    def source_ip_input(self) -> typing.Optional["LbListenerRuleConditionSourceIp"]:
        return typing.cast(typing.Optional["LbListenerRuleConditionSourceIp"], jsii.get(self, "sourceIpInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LbListenerRuleCondition, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LbListenerRuleCondition, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LbListenerRuleCondition, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[LbListenerRuleCondition, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lbListenerRule.LbListenerRuleConditionPathPattern",
    jsii_struct_bases=[],
    name_mapping={"values": "values"},
)
class LbListenerRuleConditionPathPattern:
    def __init__(self, *, values: typing.Sequence[builtins.str]) -> None:
        '''
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#values LbListenerRule#values}.
        '''
        if __debug__:
            def stub(*, values: typing.Sequence[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "values": values,
        }

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#values LbListenerRule#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LbListenerRuleConditionPathPattern(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LbListenerRuleConditionPathPatternOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lbListenerRule.LbListenerRuleConditionPathPatternOutputReference",
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
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LbListenerRuleConditionPathPattern]:
        return typing.cast(typing.Optional[LbListenerRuleConditionPathPattern], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LbListenerRuleConditionPathPattern],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[LbListenerRuleConditionPathPattern],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lbListenerRule.LbListenerRuleConditionQueryString",
    jsii_struct_bases=[],
    name_mapping={"value": "value", "key": "key"},
)
class LbListenerRuleConditionQueryString:
    def __init__(
        self,
        *,
        value: builtins.str,
        key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#value LbListenerRule#value}.
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#key LbListenerRule#key}.
        '''
        if __debug__:
            def stub(
                *,
                value: builtins.str,
                key: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
        self._values: typing.Dict[str, typing.Any] = {
            "value": value,
        }
        if key is not None:
            self._values["key"] = key

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#value LbListenerRule#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#key LbListenerRule#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LbListenerRuleConditionQueryString(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LbListenerRuleConditionQueryStringList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lbListenerRule.LbListenerRuleConditionQueryStringList",
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
    ) -> "LbListenerRuleConditionQueryStringOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LbListenerRuleConditionQueryStringOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LbListenerRuleConditionQueryString]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LbListenerRuleConditionQueryString]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LbListenerRuleConditionQueryString]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LbListenerRuleConditionQueryString]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LbListenerRuleConditionQueryStringOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lbListenerRule.LbListenerRuleConditionQueryStringOutputReference",
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

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LbListenerRuleConditionQueryString, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LbListenerRuleConditionQueryString, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LbListenerRuleConditionQueryString, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[LbListenerRuleConditionQueryString, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lbListenerRule.LbListenerRuleConditionSourceIp",
    jsii_struct_bases=[],
    name_mapping={"values": "values"},
)
class LbListenerRuleConditionSourceIp:
    def __init__(self, *, values: typing.Sequence[builtins.str]) -> None:
        '''
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#values LbListenerRule#values}.
        '''
        if __debug__:
            def stub(*, values: typing.Sequence[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "values": values,
        }

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#values LbListenerRule#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LbListenerRuleConditionSourceIp(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LbListenerRuleConditionSourceIpOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lbListenerRule.LbListenerRuleConditionSourceIpOutputReference",
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
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LbListenerRuleConditionSourceIp]:
        return typing.cast(typing.Optional[LbListenerRuleConditionSourceIp], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LbListenerRuleConditionSourceIp],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[LbListenerRuleConditionSourceIp]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lbListenerRule.LbListenerRuleConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "action": "action",
        "condition": "condition",
        "listener_arn": "listenerArn",
        "id": "id",
        "priority": "priority",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class LbListenerRuleConfig(cdktf.TerraformMetaArguments):
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
        action: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LbListenerRuleAction, typing.Dict[str, typing.Any]]]],
        condition: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LbListenerRuleCondition, typing.Dict[str, typing.Any]]]],
        listener_arn: builtins.str,
        id: typing.Optional[builtins.str] = None,
        priority: typing.Optional[jsii.Number] = None,
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
        :param action: action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#action LbListenerRule#action}
        :param condition: condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#condition LbListenerRule#condition}
        :param listener_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#listener_arn LbListenerRule#listener_arn}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#id LbListenerRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#priority LbListenerRule#priority}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#tags LbListenerRule#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#tags_all LbListenerRule#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
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
                action: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LbListenerRuleAction, typing.Dict[str, typing.Any]]]],
                condition: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LbListenerRuleCondition, typing.Dict[str, typing.Any]]]],
                listener_arn: builtins.str,
                id: typing.Optional[builtins.str] = None,
                priority: typing.Optional[jsii.Number] = None,
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
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument condition", value=condition, expected_type=type_hints["condition"])
            check_type(argname="argument listener_arn", value=listener_arn, expected_type=type_hints["listener_arn"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[str, typing.Any] = {
            "action": action,
            "condition": condition,
            "listener_arn": listener_arn,
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
        if id is not None:
            self._values["id"] = id
        if priority is not None:
            self._values["priority"] = priority
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
    def action(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List[LbListenerRuleAction]]:
        '''action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#action LbListenerRule#action}
        '''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List[LbListenerRuleAction]], result)

    @builtins.property
    def condition(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List[LbListenerRuleCondition]]:
        '''condition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#condition LbListenerRule#condition}
        '''
        result = self._values.get("condition")
        assert result is not None, "Required property 'condition' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List[LbListenerRuleCondition]], result)

    @builtins.property
    def listener_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#listener_arn LbListenerRule#listener_arn}.'''
        result = self._values.get("listener_arn")
        assert result is not None, "Required property 'listener_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#id LbListenerRule#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def priority(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#priority LbListenerRule#priority}.'''
        result = self._values.get("priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#tags LbListenerRule#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lb_listener_rule#tags_all LbListenerRule#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LbListenerRuleConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "LbListenerRule",
    "LbListenerRuleAction",
    "LbListenerRuleActionAuthenticateCognito",
    "LbListenerRuleActionAuthenticateCognitoOutputReference",
    "LbListenerRuleActionAuthenticateOidc",
    "LbListenerRuleActionAuthenticateOidcOutputReference",
    "LbListenerRuleActionFixedResponse",
    "LbListenerRuleActionFixedResponseOutputReference",
    "LbListenerRuleActionForward",
    "LbListenerRuleActionForwardOutputReference",
    "LbListenerRuleActionForwardStickiness",
    "LbListenerRuleActionForwardStickinessOutputReference",
    "LbListenerRuleActionForwardTargetGroup",
    "LbListenerRuleActionForwardTargetGroupList",
    "LbListenerRuleActionForwardTargetGroupOutputReference",
    "LbListenerRuleActionList",
    "LbListenerRuleActionOutputReference",
    "LbListenerRuleActionRedirect",
    "LbListenerRuleActionRedirectOutputReference",
    "LbListenerRuleCondition",
    "LbListenerRuleConditionHostHeader",
    "LbListenerRuleConditionHostHeaderOutputReference",
    "LbListenerRuleConditionHttpHeader",
    "LbListenerRuleConditionHttpHeaderOutputReference",
    "LbListenerRuleConditionHttpRequestMethod",
    "LbListenerRuleConditionHttpRequestMethodOutputReference",
    "LbListenerRuleConditionList",
    "LbListenerRuleConditionOutputReference",
    "LbListenerRuleConditionPathPattern",
    "LbListenerRuleConditionPathPatternOutputReference",
    "LbListenerRuleConditionQueryString",
    "LbListenerRuleConditionQueryStringList",
    "LbListenerRuleConditionQueryStringOutputReference",
    "LbListenerRuleConditionSourceIp",
    "LbListenerRuleConditionSourceIpOutputReference",
    "LbListenerRuleConfig",
]

publication.publish()
