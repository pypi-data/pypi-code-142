'''
# `aws_apigatewayv2_route`

Refer to the Terraform Registory for docs: [`aws_apigatewayv2_route`](https://www.terraform.io/docs/providers/aws/r/apigatewayv2_route).
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


class Apigatewayv2Route(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.apigatewayv2Route.Apigatewayv2Route",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_route aws_apigatewayv2_route}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        api_id: builtins.str,
        route_key: builtins.str,
        api_key_required: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        authorization_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
        authorization_type: typing.Optional[builtins.str] = None,
        authorizer_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        model_selection_expression: typing.Optional[builtins.str] = None,
        operation_name: typing.Optional[builtins.str] = None,
        request_models: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        request_parameter: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["Apigatewayv2RouteRequestParameter", typing.Dict[str, typing.Any]]]]] = None,
        route_response_selection_expression: typing.Optional[builtins.str] = None,
        target: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_route aws_apigatewayv2_route} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param api_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_route#api_id Apigatewayv2Route#api_id}.
        :param route_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_route#route_key Apigatewayv2Route#route_key}.
        :param api_key_required: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_route#api_key_required Apigatewayv2Route#api_key_required}.
        :param authorization_scopes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_route#authorization_scopes Apigatewayv2Route#authorization_scopes}.
        :param authorization_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_route#authorization_type Apigatewayv2Route#authorization_type}.
        :param authorizer_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_route#authorizer_id Apigatewayv2Route#authorizer_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_route#id Apigatewayv2Route#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param model_selection_expression: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_route#model_selection_expression Apigatewayv2Route#model_selection_expression}.
        :param operation_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_route#operation_name Apigatewayv2Route#operation_name}.
        :param request_models: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_route#request_models Apigatewayv2Route#request_models}.
        :param request_parameter: request_parameter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_route#request_parameter Apigatewayv2Route#request_parameter}
        :param route_response_selection_expression: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_route#route_response_selection_expression Apigatewayv2Route#route_response_selection_expression}.
        :param target: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_route#target Apigatewayv2Route#target}.
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
                api_id: builtins.str,
                route_key: builtins.str,
                api_key_required: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                authorization_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
                authorization_type: typing.Optional[builtins.str] = None,
                authorizer_id: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                model_selection_expression: typing.Optional[builtins.str] = None,
                operation_name: typing.Optional[builtins.str] = None,
                request_models: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                request_parameter: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[Apigatewayv2RouteRequestParameter, typing.Dict[str, typing.Any]]]]] = None,
                route_response_selection_expression: typing.Optional[builtins.str] = None,
                target: typing.Optional[builtins.str] = None,
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
        config = Apigatewayv2RouteConfig(
            api_id=api_id,
            route_key=route_key,
            api_key_required=api_key_required,
            authorization_scopes=authorization_scopes,
            authorization_type=authorization_type,
            authorizer_id=authorizer_id,
            id=id,
            model_selection_expression=model_selection_expression,
            operation_name=operation_name,
            request_models=request_models,
            request_parameter=request_parameter,
            route_response_selection_expression=route_response_selection_expression,
            target=target,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putRequestParameter")
    def put_request_parameter(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["Apigatewayv2RouteRequestParameter", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[Apigatewayv2RouteRequestParameter, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRequestParameter", [value]))

    @jsii.member(jsii_name="resetApiKeyRequired")
    def reset_api_key_required(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApiKeyRequired", []))

    @jsii.member(jsii_name="resetAuthorizationScopes")
    def reset_authorization_scopes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthorizationScopes", []))

    @jsii.member(jsii_name="resetAuthorizationType")
    def reset_authorization_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthorizationType", []))

    @jsii.member(jsii_name="resetAuthorizerId")
    def reset_authorizer_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthorizerId", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetModelSelectionExpression")
    def reset_model_selection_expression(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetModelSelectionExpression", []))

    @jsii.member(jsii_name="resetOperationName")
    def reset_operation_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOperationName", []))

    @jsii.member(jsii_name="resetRequestModels")
    def reset_request_models(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestModels", []))

    @jsii.member(jsii_name="resetRequestParameter")
    def reset_request_parameter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestParameter", []))

    @jsii.member(jsii_name="resetRouteResponseSelectionExpression")
    def reset_route_response_selection_expression(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRouteResponseSelectionExpression", []))

    @jsii.member(jsii_name="resetTarget")
    def reset_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTarget", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="requestParameter")
    def request_parameter(self) -> "Apigatewayv2RouteRequestParameterList":
        return typing.cast("Apigatewayv2RouteRequestParameterList", jsii.get(self, "requestParameter"))

    @builtins.property
    @jsii.member(jsii_name="apiIdInput")
    def api_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiIdInput"))

    @builtins.property
    @jsii.member(jsii_name="apiKeyRequiredInput")
    def api_key_required_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "apiKeyRequiredInput"))

    @builtins.property
    @jsii.member(jsii_name="authorizationScopesInput")
    def authorization_scopes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "authorizationScopesInput"))

    @builtins.property
    @jsii.member(jsii_name="authorizationTypeInput")
    def authorization_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authorizationTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="authorizerIdInput")
    def authorizer_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authorizerIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="modelSelectionExpressionInput")
    def model_selection_expression_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modelSelectionExpressionInput"))

    @builtins.property
    @jsii.member(jsii_name="operationNameInput")
    def operation_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operationNameInput"))

    @builtins.property
    @jsii.member(jsii_name="requestModelsInput")
    def request_models_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "requestModelsInput"))

    @builtins.property
    @jsii.member(jsii_name="requestParameterInput")
    def request_parameter_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["Apigatewayv2RouteRequestParameter"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["Apigatewayv2RouteRequestParameter"]]], jsii.get(self, "requestParameterInput"))

    @builtins.property
    @jsii.member(jsii_name="routeKeyInput")
    def route_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "routeKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="routeResponseSelectionExpressionInput")
    def route_response_selection_expression_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "routeResponseSelectionExpressionInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiId"))

    @api_id.setter
    def api_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiId", value)

    @builtins.property
    @jsii.member(jsii_name="apiKeyRequired")
    def api_key_required(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "apiKeyRequired"))

    @api_key_required.setter
    def api_key_required(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiKeyRequired", value)

    @builtins.property
    @jsii.member(jsii_name="authorizationScopes")
    def authorization_scopes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "authorizationScopes"))

    @authorization_scopes.setter
    def authorization_scopes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorizationScopes", value)

    @builtins.property
    @jsii.member(jsii_name="authorizationType")
    def authorization_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authorizationType"))

    @authorization_type.setter
    def authorization_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorizationType", value)

    @builtins.property
    @jsii.member(jsii_name="authorizerId")
    def authorizer_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authorizerId"))

    @authorizer_id.setter
    def authorizer_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorizerId", value)

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
    @jsii.member(jsii_name="modelSelectionExpression")
    def model_selection_expression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "modelSelectionExpression"))

    @model_selection_expression.setter
    def model_selection_expression(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "modelSelectionExpression", value)

    @builtins.property
    @jsii.member(jsii_name="operationName")
    def operation_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operationName"))

    @operation_name.setter
    def operation_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operationName", value)

    @builtins.property
    @jsii.member(jsii_name="requestModels")
    def request_models(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "requestModels"))

    @request_models.setter
    def request_models(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.Mapping[builtins.str, builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestModels", value)

    @builtins.property
    @jsii.member(jsii_name="routeKey")
    def route_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "routeKey"))

    @route_key.setter
    def route_key(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "routeKey", value)

    @builtins.property
    @jsii.member(jsii_name="routeResponseSelectionExpression")
    def route_response_selection_expression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "routeResponseSelectionExpression"))

    @route_response_selection_expression.setter
    def route_response_selection_expression(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "routeResponseSelectionExpression", value)

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "target"))

    @target.setter
    def target(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.apigatewayv2Route.Apigatewayv2RouteConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "api_id": "apiId",
        "route_key": "routeKey",
        "api_key_required": "apiKeyRequired",
        "authorization_scopes": "authorizationScopes",
        "authorization_type": "authorizationType",
        "authorizer_id": "authorizerId",
        "id": "id",
        "model_selection_expression": "modelSelectionExpression",
        "operation_name": "operationName",
        "request_models": "requestModels",
        "request_parameter": "requestParameter",
        "route_response_selection_expression": "routeResponseSelectionExpression",
        "target": "target",
    },
)
class Apigatewayv2RouteConfig(cdktf.TerraformMetaArguments):
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
        api_id: builtins.str,
        route_key: builtins.str,
        api_key_required: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        authorization_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
        authorization_type: typing.Optional[builtins.str] = None,
        authorizer_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        model_selection_expression: typing.Optional[builtins.str] = None,
        operation_name: typing.Optional[builtins.str] = None,
        request_models: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        request_parameter: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["Apigatewayv2RouteRequestParameter", typing.Dict[str, typing.Any]]]]] = None,
        route_response_selection_expression: typing.Optional[builtins.str] = None,
        target: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param api_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_route#api_id Apigatewayv2Route#api_id}.
        :param route_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_route#route_key Apigatewayv2Route#route_key}.
        :param api_key_required: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_route#api_key_required Apigatewayv2Route#api_key_required}.
        :param authorization_scopes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_route#authorization_scopes Apigatewayv2Route#authorization_scopes}.
        :param authorization_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_route#authorization_type Apigatewayv2Route#authorization_type}.
        :param authorizer_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_route#authorizer_id Apigatewayv2Route#authorizer_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_route#id Apigatewayv2Route#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param model_selection_expression: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_route#model_selection_expression Apigatewayv2Route#model_selection_expression}.
        :param operation_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_route#operation_name Apigatewayv2Route#operation_name}.
        :param request_models: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_route#request_models Apigatewayv2Route#request_models}.
        :param request_parameter: request_parameter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_route#request_parameter Apigatewayv2Route#request_parameter}
        :param route_response_selection_expression: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_route#route_response_selection_expression Apigatewayv2Route#route_response_selection_expression}.
        :param target: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_route#target Apigatewayv2Route#target}.
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
                api_id: builtins.str,
                route_key: builtins.str,
                api_key_required: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                authorization_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
                authorization_type: typing.Optional[builtins.str] = None,
                authorizer_id: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                model_selection_expression: typing.Optional[builtins.str] = None,
                operation_name: typing.Optional[builtins.str] = None,
                request_models: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                request_parameter: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[Apigatewayv2RouteRequestParameter, typing.Dict[str, typing.Any]]]]] = None,
                route_response_selection_expression: typing.Optional[builtins.str] = None,
                target: typing.Optional[builtins.str] = None,
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
            check_type(argname="argument api_id", value=api_id, expected_type=type_hints["api_id"])
            check_type(argname="argument route_key", value=route_key, expected_type=type_hints["route_key"])
            check_type(argname="argument api_key_required", value=api_key_required, expected_type=type_hints["api_key_required"])
            check_type(argname="argument authorization_scopes", value=authorization_scopes, expected_type=type_hints["authorization_scopes"])
            check_type(argname="argument authorization_type", value=authorization_type, expected_type=type_hints["authorization_type"])
            check_type(argname="argument authorizer_id", value=authorizer_id, expected_type=type_hints["authorizer_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument model_selection_expression", value=model_selection_expression, expected_type=type_hints["model_selection_expression"])
            check_type(argname="argument operation_name", value=operation_name, expected_type=type_hints["operation_name"])
            check_type(argname="argument request_models", value=request_models, expected_type=type_hints["request_models"])
            check_type(argname="argument request_parameter", value=request_parameter, expected_type=type_hints["request_parameter"])
            check_type(argname="argument route_response_selection_expression", value=route_response_selection_expression, expected_type=type_hints["route_response_selection_expression"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
        self._values: typing.Dict[str, typing.Any] = {
            "api_id": api_id,
            "route_key": route_key,
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
        if api_key_required is not None:
            self._values["api_key_required"] = api_key_required
        if authorization_scopes is not None:
            self._values["authorization_scopes"] = authorization_scopes
        if authorization_type is not None:
            self._values["authorization_type"] = authorization_type
        if authorizer_id is not None:
            self._values["authorizer_id"] = authorizer_id
        if id is not None:
            self._values["id"] = id
        if model_selection_expression is not None:
            self._values["model_selection_expression"] = model_selection_expression
        if operation_name is not None:
            self._values["operation_name"] = operation_name
        if request_models is not None:
            self._values["request_models"] = request_models
        if request_parameter is not None:
            self._values["request_parameter"] = request_parameter
        if route_response_selection_expression is not None:
            self._values["route_response_selection_expression"] = route_response_selection_expression
        if target is not None:
            self._values["target"] = target

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
    def api_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_route#api_id Apigatewayv2Route#api_id}.'''
        result = self._values.get("api_id")
        assert result is not None, "Required property 'api_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def route_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_route#route_key Apigatewayv2Route#route_key}.'''
        result = self._values.get("route_key")
        assert result is not None, "Required property 'route_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def api_key_required(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_route#api_key_required Apigatewayv2Route#api_key_required}.'''
        result = self._values.get("api_key_required")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def authorization_scopes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_route#authorization_scopes Apigatewayv2Route#authorization_scopes}.'''
        result = self._values.get("authorization_scopes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def authorization_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_route#authorization_type Apigatewayv2Route#authorization_type}.'''
        result = self._values.get("authorization_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def authorizer_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_route#authorizer_id Apigatewayv2Route#authorizer_id}.'''
        result = self._values.get("authorizer_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_route#id Apigatewayv2Route#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def model_selection_expression(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_route#model_selection_expression Apigatewayv2Route#model_selection_expression}.'''
        result = self._values.get("model_selection_expression")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def operation_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_route#operation_name Apigatewayv2Route#operation_name}.'''
        result = self._values.get("operation_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_models(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_route#request_models Apigatewayv2Route#request_models}.'''
        result = self._values.get("request_models")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def request_parameter(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["Apigatewayv2RouteRequestParameter"]]]:
        '''request_parameter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_route#request_parameter Apigatewayv2Route#request_parameter}
        '''
        result = self._values.get("request_parameter")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["Apigatewayv2RouteRequestParameter"]]], result)

    @builtins.property
    def route_response_selection_expression(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_route#route_response_selection_expression Apigatewayv2Route#route_response_selection_expression}.'''
        result = self._values.get("route_response_selection_expression")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_route#target Apigatewayv2Route#target}.'''
        result = self._values.get("target")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Apigatewayv2RouteConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.apigatewayv2Route.Apigatewayv2RouteRequestParameter",
    jsii_struct_bases=[],
    name_mapping={
        "request_parameter_key": "requestParameterKey",
        "required": "required",
    },
)
class Apigatewayv2RouteRequestParameter:
    def __init__(
        self,
        *,
        request_parameter_key: builtins.str,
        required: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param request_parameter_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_route#request_parameter_key Apigatewayv2Route#request_parameter_key}.
        :param required: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_route#required Apigatewayv2Route#required}.
        '''
        if __debug__:
            def stub(
                *,
                request_parameter_key: builtins.str,
                required: typing.Union[builtins.bool, cdktf.IResolvable],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument request_parameter_key", value=request_parameter_key, expected_type=type_hints["request_parameter_key"])
            check_type(argname="argument required", value=required, expected_type=type_hints["required"])
        self._values: typing.Dict[str, typing.Any] = {
            "request_parameter_key": request_parameter_key,
            "required": required,
        }

    @builtins.property
    def request_parameter_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_route#request_parameter_key Apigatewayv2Route#request_parameter_key}.'''
        result = self._values.get("request_parameter_key")
        assert result is not None, "Required property 'request_parameter_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def required(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_route#required Apigatewayv2Route#required}.'''
        result = self._values.get("required")
        assert result is not None, "Required property 'required' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Apigatewayv2RouteRequestParameter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Apigatewayv2RouteRequestParameterList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.apigatewayv2Route.Apigatewayv2RouteRequestParameterList",
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
    ) -> "Apigatewayv2RouteRequestParameterOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Apigatewayv2RouteRequestParameterOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Apigatewayv2RouteRequestParameter]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Apigatewayv2RouteRequestParameter]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Apigatewayv2RouteRequestParameter]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Apigatewayv2RouteRequestParameter]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Apigatewayv2RouteRequestParameterOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.apigatewayv2Route.Apigatewayv2RouteRequestParameterOutputReference",
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
    @jsii.member(jsii_name="requestParameterKeyInput")
    def request_parameter_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "requestParameterKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="requiredInput")
    def required_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "requiredInput"))

    @builtins.property
    @jsii.member(jsii_name="requestParameterKey")
    def request_parameter_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "requestParameterKey"))

    @request_parameter_key.setter
    def request_parameter_key(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestParameterKey", value)

    @builtins.property
    @jsii.member(jsii_name="required")
    def required(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "required"))

    @required.setter
    def required(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "required", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[Apigatewayv2RouteRequestParameter, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[Apigatewayv2RouteRequestParameter, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[Apigatewayv2RouteRequestParameter, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[Apigatewayv2RouteRequestParameter, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Apigatewayv2Route",
    "Apigatewayv2RouteConfig",
    "Apigatewayv2RouteRequestParameter",
    "Apigatewayv2RouteRequestParameterList",
    "Apigatewayv2RouteRequestParameterOutputReference",
]

publication.publish()
