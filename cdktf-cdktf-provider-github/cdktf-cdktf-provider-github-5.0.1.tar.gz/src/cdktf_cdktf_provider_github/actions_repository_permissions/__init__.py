'''
# `github_actions_repository_permissions`

Refer to the Terraform Registory for docs: [`github_actions_repository_permissions`](https://www.terraform.io/docs/providers/github/r/actions_repository_permissions).
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


class ActionsRepositoryPermissions(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-github.actionsRepositoryPermissions.ActionsRepositoryPermissions",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/github/r/actions_repository_permissions github_actions_repository_permissions}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        repository: builtins.str,
        allowed_actions: typing.Optional[builtins.str] = None,
        allowed_actions_config: typing.Optional[typing.Union["ActionsRepositoryPermissionsAllowedActionsConfig", typing.Dict[str, typing.Any]]] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/github/r/actions_repository_permissions github_actions_repository_permissions} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param repository: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/actions_repository_permissions#repository ActionsRepositoryPermissions#repository}.
        :param allowed_actions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/actions_repository_permissions#allowed_actions ActionsRepositoryPermissions#allowed_actions}.
        :param allowed_actions_config: allowed_actions_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/actions_repository_permissions#allowed_actions_config ActionsRepositoryPermissions#allowed_actions_config}
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/actions_repository_permissions#enabled ActionsRepositoryPermissions#enabled}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/actions_repository_permissions#id ActionsRepositoryPermissions#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
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
                repository: builtins.str,
                allowed_actions: typing.Optional[builtins.str] = None,
                allowed_actions_config: typing.Optional[typing.Union[ActionsRepositoryPermissionsAllowedActionsConfig, typing.Dict[str, typing.Any]]] = None,
                enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                id: typing.Optional[builtins.str] = None,
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
        config = ActionsRepositoryPermissionsConfig(
            repository=repository,
            allowed_actions=allowed_actions,
            allowed_actions_config=allowed_actions_config,
            enabled=enabled,
            id=id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAllowedActionsConfig")
    def put_allowed_actions_config(
        self,
        *,
        github_owned_allowed: typing.Union[builtins.bool, cdktf.IResolvable],
        patterns_allowed: typing.Optional[typing.Sequence[builtins.str]] = None,
        verified_allowed: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param github_owned_allowed: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/actions_repository_permissions#github_owned_allowed ActionsRepositoryPermissions#github_owned_allowed}.
        :param patterns_allowed: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/actions_repository_permissions#patterns_allowed ActionsRepositoryPermissions#patterns_allowed}.
        :param verified_allowed: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/actions_repository_permissions#verified_allowed ActionsRepositoryPermissions#verified_allowed}.
        '''
        value = ActionsRepositoryPermissionsAllowedActionsConfig(
            github_owned_allowed=github_owned_allowed,
            patterns_allowed=patterns_allowed,
            verified_allowed=verified_allowed,
        )

        return typing.cast(None, jsii.invoke(self, "putAllowedActionsConfig", [value]))

    @jsii.member(jsii_name="resetAllowedActions")
    def reset_allowed_actions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedActions", []))

    @jsii.member(jsii_name="resetAllowedActionsConfig")
    def reset_allowed_actions_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedActionsConfig", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="allowedActionsConfig")
    def allowed_actions_config(
        self,
    ) -> "ActionsRepositoryPermissionsAllowedActionsConfigOutputReference":
        return typing.cast("ActionsRepositoryPermissionsAllowedActionsConfigOutputReference", jsii.get(self, "allowedActionsConfig"))

    @builtins.property
    @jsii.member(jsii_name="allowedActionsConfigInput")
    def allowed_actions_config_input(
        self,
    ) -> typing.Optional["ActionsRepositoryPermissionsAllowedActionsConfig"]:
        return typing.cast(typing.Optional["ActionsRepositoryPermissionsAllowedActionsConfig"], jsii.get(self, "allowedActionsConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedActionsInput")
    def allowed_actions_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "allowedActionsInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="repositoryInput")
    def repository_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "repositoryInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedActions")
    def allowed_actions(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "allowedActions"))

    @allowed_actions.setter
    def allowed_actions(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedActions", value)

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
    @jsii.member(jsii_name="repository")
    def repository(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "repository"))

    @repository.setter
    def repository(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repository", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-github.actionsRepositoryPermissions.ActionsRepositoryPermissionsAllowedActionsConfig",
    jsii_struct_bases=[],
    name_mapping={
        "github_owned_allowed": "githubOwnedAllowed",
        "patterns_allowed": "patternsAllowed",
        "verified_allowed": "verifiedAllowed",
    },
)
class ActionsRepositoryPermissionsAllowedActionsConfig:
    def __init__(
        self,
        *,
        github_owned_allowed: typing.Union[builtins.bool, cdktf.IResolvable],
        patterns_allowed: typing.Optional[typing.Sequence[builtins.str]] = None,
        verified_allowed: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param github_owned_allowed: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/actions_repository_permissions#github_owned_allowed ActionsRepositoryPermissions#github_owned_allowed}.
        :param patterns_allowed: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/actions_repository_permissions#patterns_allowed ActionsRepositoryPermissions#patterns_allowed}.
        :param verified_allowed: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/actions_repository_permissions#verified_allowed ActionsRepositoryPermissions#verified_allowed}.
        '''
        if __debug__:
            def stub(
                *,
                github_owned_allowed: typing.Union[builtins.bool, cdktf.IResolvable],
                patterns_allowed: typing.Optional[typing.Sequence[builtins.str]] = None,
                verified_allowed: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument github_owned_allowed", value=github_owned_allowed, expected_type=type_hints["github_owned_allowed"])
            check_type(argname="argument patterns_allowed", value=patterns_allowed, expected_type=type_hints["patterns_allowed"])
            check_type(argname="argument verified_allowed", value=verified_allowed, expected_type=type_hints["verified_allowed"])
        self._values: typing.Dict[str, typing.Any] = {
            "github_owned_allowed": github_owned_allowed,
        }
        if patterns_allowed is not None:
            self._values["patterns_allowed"] = patterns_allowed
        if verified_allowed is not None:
            self._values["verified_allowed"] = verified_allowed

    @builtins.property
    def github_owned_allowed(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/actions_repository_permissions#github_owned_allowed ActionsRepositoryPermissions#github_owned_allowed}.'''
        result = self._values.get("github_owned_allowed")
        assert result is not None, "Required property 'github_owned_allowed' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def patterns_allowed(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/actions_repository_permissions#patterns_allowed ActionsRepositoryPermissions#patterns_allowed}.'''
        result = self._values.get("patterns_allowed")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def verified_allowed(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/actions_repository_permissions#verified_allowed ActionsRepositoryPermissions#verified_allowed}.'''
        result = self._values.get("verified_allowed")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ActionsRepositoryPermissionsAllowedActionsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ActionsRepositoryPermissionsAllowedActionsConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-github.actionsRepositoryPermissions.ActionsRepositoryPermissionsAllowedActionsConfigOutputReference",
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

    @jsii.member(jsii_name="resetPatternsAllowed")
    def reset_patterns_allowed(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPatternsAllowed", []))

    @jsii.member(jsii_name="resetVerifiedAllowed")
    def reset_verified_allowed(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVerifiedAllowed", []))

    @builtins.property
    @jsii.member(jsii_name="githubOwnedAllowedInput")
    def github_owned_allowed_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "githubOwnedAllowedInput"))

    @builtins.property
    @jsii.member(jsii_name="patternsAllowedInput")
    def patterns_allowed_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "patternsAllowedInput"))

    @builtins.property
    @jsii.member(jsii_name="verifiedAllowedInput")
    def verified_allowed_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "verifiedAllowedInput"))

    @builtins.property
    @jsii.member(jsii_name="githubOwnedAllowed")
    def github_owned_allowed(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "githubOwnedAllowed"))

    @github_owned_allowed.setter
    def github_owned_allowed(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "githubOwnedAllowed", value)

    @builtins.property
    @jsii.member(jsii_name="patternsAllowed")
    def patterns_allowed(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "patternsAllowed"))

    @patterns_allowed.setter
    def patterns_allowed(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "patternsAllowed", value)

    @builtins.property
    @jsii.member(jsii_name="verifiedAllowed")
    def verified_allowed(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "verifiedAllowed"))

    @verified_allowed.setter
    def verified_allowed(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "verifiedAllowed", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ActionsRepositoryPermissionsAllowedActionsConfig]:
        return typing.cast(typing.Optional[ActionsRepositoryPermissionsAllowedActionsConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ActionsRepositoryPermissionsAllowedActionsConfig],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[ActionsRepositoryPermissionsAllowedActionsConfig],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-github.actionsRepositoryPermissions.ActionsRepositoryPermissionsConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "repository": "repository",
        "allowed_actions": "allowedActions",
        "allowed_actions_config": "allowedActionsConfig",
        "enabled": "enabled",
        "id": "id",
    },
)
class ActionsRepositoryPermissionsConfig(cdktf.TerraformMetaArguments):
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
        repository: builtins.str,
        allowed_actions: typing.Optional[builtins.str] = None,
        allowed_actions_config: typing.Optional[typing.Union[ActionsRepositoryPermissionsAllowedActionsConfig, typing.Dict[str, typing.Any]]] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param repository: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/actions_repository_permissions#repository ActionsRepositoryPermissions#repository}.
        :param allowed_actions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/actions_repository_permissions#allowed_actions ActionsRepositoryPermissions#allowed_actions}.
        :param allowed_actions_config: allowed_actions_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/actions_repository_permissions#allowed_actions_config ActionsRepositoryPermissions#allowed_actions_config}
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/actions_repository_permissions#enabled ActionsRepositoryPermissions#enabled}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/actions_repository_permissions#id ActionsRepositoryPermissions#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(allowed_actions_config, dict):
            allowed_actions_config = ActionsRepositoryPermissionsAllowedActionsConfig(**allowed_actions_config)
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
                repository: builtins.str,
                allowed_actions: typing.Optional[builtins.str] = None,
                allowed_actions_config: typing.Optional[typing.Union[ActionsRepositoryPermissionsAllowedActionsConfig, typing.Dict[str, typing.Any]]] = None,
                enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                id: typing.Optional[builtins.str] = None,
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
            check_type(argname="argument repository", value=repository, expected_type=type_hints["repository"])
            check_type(argname="argument allowed_actions", value=allowed_actions, expected_type=type_hints["allowed_actions"])
            check_type(argname="argument allowed_actions_config", value=allowed_actions_config, expected_type=type_hints["allowed_actions_config"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[str, typing.Any] = {
            "repository": repository,
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
        if allowed_actions is not None:
            self._values["allowed_actions"] = allowed_actions
        if allowed_actions_config is not None:
            self._values["allowed_actions_config"] = allowed_actions_config
        if enabled is not None:
            self._values["enabled"] = enabled
        if id is not None:
            self._values["id"] = id

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
    def repository(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/actions_repository_permissions#repository ActionsRepositoryPermissions#repository}.'''
        result = self._values.get("repository")
        assert result is not None, "Required property 'repository' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allowed_actions(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/actions_repository_permissions#allowed_actions ActionsRepositoryPermissions#allowed_actions}.'''
        result = self._values.get("allowed_actions")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def allowed_actions_config(
        self,
    ) -> typing.Optional[ActionsRepositoryPermissionsAllowedActionsConfig]:
        '''allowed_actions_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/actions_repository_permissions#allowed_actions_config ActionsRepositoryPermissions#allowed_actions_config}
        '''
        result = self._values.get("allowed_actions_config")
        return typing.cast(typing.Optional[ActionsRepositoryPermissionsAllowedActionsConfig], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/actions_repository_permissions#enabled ActionsRepositoryPermissions#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/actions_repository_permissions#id ActionsRepositoryPermissions#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ActionsRepositoryPermissionsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ActionsRepositoryPermissions",
    "ActionsRepositoryPermissionsAllowedActionsConfig",
    "ActionsRepositoryPermissionsAllowedActionsConfigOutputReference",
    "ActionsRepositoryPermissionsConfig",
]

publication.publish()
