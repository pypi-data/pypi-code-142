'''
# `aws_iam_account_password_policy`

Refer to the Terraform Registory for docs: [`aws_iam_account_password_policy`](https://www.terraform.io/docs/providers/aws/r/iam_account_password_policy).
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


class IamAccountPasswordPolicy(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.iamAccountPasswordPolicy.IamAccountPasswordPolicy",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/iam_account_password_policy aws_iam_account_password_policy}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        allow_users_to_change_password: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        hard_expiry: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        max_password_age: typing.Optional[jsii.Number] = None,
        minimum_password_length: typing.Optional[jsii.Number] = None,
        password_reuse_prevention: typing.Optional[jsii.Number] = None,
        require_lowercase_characters: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        require_numbers: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        require_symbols: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        require_uppercase_characters: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/iam_account_password_policy aws_iam_account_password_policy} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param allow_users_to_change_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iam_account_password_policy#allow_users_to_change_password IamAccountPasswordPolicy#allow_users_to_change_password}.
        :param hard_expiry: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iam_account_password_policy#hard_expiry IamAccountPasswordPolicy#hard_expiry}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iam_account_password_policy#id IamAccountPasswordPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param max_password_age: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iam_account_password_policy#max_password_age IamAccountPasswordPolicy#max_password_age}.
        :param minimum_password_length: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iam_account_password_policy#minimum_password_length IamAccountPasswordPolicy#minimum_password_length}.
        :param password_reuse_prevention: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iam_account_password_policy#password_reuse_prevention IamAccountPasswordPolicy#password_reuse_prevention}.
        :param require_lowercase_characters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iam_account_password_policy#require_lowercase_characters IamAccountPasswordPolicy#require_lowercase_characters}.
        :param require_numbers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iam_account_password_policy#require_numbers IamAccountPasswordPolicy#require_numbers}.
        :param require_symbols: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iam_account_password_policy#require_symbols IamAccountPasswordPolicy#require_symbols}.
        :param require_uppercase_characters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iam_account_password_policy#require_uppercase_characters IamAccountPasswordPolicy#require_uppercase_characters}.
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
                allow_users_to_change_password: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                hard_expiry: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                id: typing.Optional[builtins.str] = None,
                max_password_age: typing.Optional[jsii.Number] = None,
                minimum_password_length: typing.Optional[jsii.Number] = None,
                password_reuse_prevention: typing.Optional[jsii.Number] = None,
                require_lowercase_characters: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                require_numbers: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                require_symbols: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                require_uppercase_characters: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
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
        config = IamAccountPasswordPolicyConfig(
            allow_users_to_change_password=allow_users_to_change_password,
            hard_expiry=hard_expiry,
            id=id,
            max_password_age=max_password_age,
            minimum_password_length=minimum_password_length,
            password_reuse_prevention=password_reuse_prevention,
            require_lowercase_characters=require_lowercase_characters,
            require_numbers=require_numbers,
            require_symbols=require_symbols,
            require_uppercase_characters=require_uppercase_characters,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetAllowUsersToChangePassword")
    def reset_allow_users_to_change_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowUsersToChangePassword", []))

    @jsii.member(jsii_name="resetHardExpiry")
    def reset_hard_expiry(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHardExpiry", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMaxPasswordAge")
    def reset_max_password_age(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxPasswordAge", []))

    @jsii.member(jsii_name="resetMinimumPasswordLength")
    def reset_minimum_password_length(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinimumPasswordLength", []))

    @jsii.member(jsii_name="resetPasswordReusePrevention")
    def reset_password_reuse_prevention(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPasswordReusePrevention", []))

    @jsii.member(jsii_name="resetRequireLowercaseCharacters")
    def reset_require_lowercase_characters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequireLowercaseCharacters", []))

    @jsii.member(jsii_name="resetRequireNumbers")
    def reset_require_numbers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequireNumbers", []))

    @jsii.member(jsii_name="resetRequireSymbols")
    def reset_require_symbols(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequireSymbols", []))

    @jsii.member(jsii_name="resetRequireUppercaseCharacters")
    def reset_require_uppercase_characters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequireUppercaseCharacters", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="expirePasswords")
    def expire_passwords(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "expirePasswords"))

    @builtins.property
    @jsii.member(jsii_name="allowUsersToChangePasswordInput")
    def allow_users_to_change_password_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowUsersToChangePasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="hardExpiryInput")
    def hard_expiry_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "hardExpiryInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="maxPasswordAgeInput")
    def max_password_age_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxPasswordAgeInput"))

    @builtins.property
    @jsii.member(jsii_name="minimumPasswordLengthInput")
    def minimum_password_length_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minimumPasswordLengthInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordReusePreventionInput")
    def password_reuse_prevention_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "passwordReusePreventionInput"))

    @builtins.property
    @jsii.member(jsii_name="requireLowercaseCharactersInput")
    def require_lowercase_characters_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "requireLowercaseCharactersInput"))

    @builtins.property
    @jsii.member(jsii_name="requireNumbersInput")
    def require_numbers_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "requireNumbersInput"))

    @builtins.property
    @jsii.member(jsii_name="requireSymbolsInput")
    def require_symbols_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "requireSymbolsInput"))

    @builtins.property
    @jsii.member(jsii_name="requireUppercaseCharactersInput")
    def require_uppercase_characters_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "requireUppercaseCharactersInput"))

    @builtins.property
    @jsii.member(jsii_name="allowUsersToChangePassword")
    def allow_users_to_change_password(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowUsersToChangePassword"))

    @allow_users_to_change_password.setter
    def allow_users_to_change_password(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowUsersToChangePassword", value)

    @builtins.property
    @jsii.member(jsii_name="hardExpiry")
    def hard_expiry(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "hardExpiry"))

    @hard_expiry.setter
    def hard_expiry(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hardExpiry", value)

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
    @jsii.member(jsii_name="maxPasswordAge")
    def max_password_age(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxPasswordAge"))

    @max_password_age.setter
    def max_password_age(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxPasswordAge", value)

    @builtins.property
    @jsii.member(jsii_name="minimumPasswordLength")
    def minimum_password_length(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minimumPasswordLength"))

    @minimum_password_length.setter
    def minimum_password_length(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minimumPasswordLength", value)

    @builtins.property
    @jsii.member(jsii_name="passwordReusePrevention")
    def password_reuse_prevention(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "passwordReusePrevention"))

    @password_reuse_prevention.setter
    def password_reuse_prevention(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "passwordReusePrevention", value)

    @builtins.property
    @jsii.member(jsii_name="requireLowercaseCharacters")
    def require_lowercase_characters(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "requireLowercaseCharacters"))

    @require_lowercase_characters.setter
    def require_lowercase_characters(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requireLowercaseCharacters", value)

    @builtins.property
    @jsii.member(jsii_name="requireNumbers")
    def require_numbers(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "requireNumbers"))

    @require_numbers.setter
    def require_numbers(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requireNumbers", value)

    @builtins.property
    @jsii.member(jsii_name="requireSymbols")
    def require_symbols(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "requireSymbols"))

    @require_symbols.setter
    def require_symbols(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requireSymbols", value)

    @builtins.property
    @jsii.member(jsii_name="requireUppercaseCharacters")
    def require_uppercase_characters(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "requireUppercaseCharacters"))

    @require_uppercase_characters.setter
    def require_uppercase_characters(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requireUppercaseCharacters", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.iamAccountPasswordPolicy.IamAccountPasswordPolicyConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "allow_users_to_change_password": "allowUsersToChangePassword",
        "hard_expiry": "hardExpiry",
        "id": "id",
        "max_password_age": "maxPasswordAge",
        "minimum_password_length": "minimumPasswordLength",
        "password_reuse_prevention": "passwordReusePrevention",
        "require_lowercase_characters": "requireLowercaseCharacters",
        "require_numbers": "requireNumbers",
        "require_symbols": "requireSymbols",
        "require_uppercase_characters": "requireUppercaseCharacters",
    },
)
class IamAccountPasswordPolicyConfig(cdktf.TerraformMetaArguments):
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
        allow_users_to_change_password: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        hard_expiry: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        max_password_age: typing.Optional[jsii.Number] = None,
        minimum_password_length: typing.Optional[jsii.Number] = None,
        password_reuse_prevention: typing.Optional[jsii.Number] = None,
        require_lowercase_characters: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        require_numbers: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        require_symbols: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        require_uppercase_characters: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param allow_users_to_change_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iam_account_password_policy#allow_users_to_change_password IamAccountPasswordPolicy#allow_users_to_change_password}.
        :param hard_expiry: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iam_account_password_policy#hard_expiry IamAccountPasswordPolicy#hard_expiry}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iam_account_password_policy#id IamAccountPasswordPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param max_password_age: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iam_account_password_policy#max_password_age IamAccountPasswordPolicy#max_password_age}.
        :param minimum_password_length: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iam_account_password_policy#minimum_password_length IamAccountPasswordPolicy#minimum_password_length}.
        :param password_reuse_prevention: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iam_account_password_policy#password_reuse_prevention IamAccountPasswordPolicy#password_reuse_prevention}.
        :param require_lowercase_characters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iam_account_password_policy#require_lowercase_characters IamAccountPasswordPolicy#require_lowercase_characters}.
        :param require_numbers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iam_account_password_policy#require_numbers IamAccountPasswordPolicy#require_numbers}.
        :param require_symbols: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iam_account_password_policy#require_symbols IamAccountPasswordPolicy#require_symbols}.
        :param require_uppercase_characters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iam_account_password_policy#require_uppercase_characters IamAccountPasswordPolicy#require_uppercase_characters}.
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
                allow_users_to_change_password: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                hard_expiry: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                id: typing.Optional[builtins.str] = None,
                max_password_age: typing.Optional[jsii.Number] = None,
                minimum_password_length: typing.Optional[jsii.Number] = None,
                password_reuse_prevention: typing.Optional[jsii.Number] = None,
                require_lowercase_characters: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                require_numbers: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                require_symbols: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                require_uppercase_characters: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
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
            check_type(argname="argument allow_users_to_change_password", value=allow_users_to_change_password, expected_type=type_hints["allow_users_to_change_password"])
            check_type(argname="argument hard_expiry", value=hard_expiry, expected_type=type_hints["hard_expiry"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument max_password_age", value=max_password_age, expected_type=type_hints["max_password_age"])
            check_type(argname="argument minimum_password_length", value=minimum_password_length, expected_type=type_hints["minimum_password_length"])
            check_type(argname="argument password_reuse_prevention", value=password_reuse_prevention, expected_type=type_hints["password_reuse_prevention"])
            check_type(argname="argument require_lowercase_characters", value=require_lowercase_characters, expected_type=type_hints["require_lowercase_characters"])
            check_type(argname="argument require_numbers", value=require_numbers, expected_type=type_hints["require_numbers"])
            check_type(argname="argument require_symbols", value=require_symbols, expected_type=type_hints["require_symbols"])
            check_type(argname="argument require_uppercase_characters", value=require_uppercase_characters, expected_type=type_hints["require_uppercase_characters"])
        self._values: typing.Dict[str, typing.Any] = {}
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
        if allow_users_to_change_password is not None:
            self._values["allow_users_to_change_password"] = allow_users_to_change_password
        if hard_expiry is not None:
            self._values["hard_expiry"] = hard_expiry
        if id is not None:
            self._values["id"] = id
        if max_password_age is not None:
            self._values["max_password_age"] = max_password_age
        if minimum_password_length is not None:
            self._values["minimum_password_length"] = minimum_password_length
        if password_reuse_prevention is not None:
            self._values["password_reuse_prevention"] = password_reuse_prevention
        if require_lowercase_characters is not None:
            self._values["require_lowercase_characters"] = require_lowercase_characters
        if require_numbers is not None:
            self._values["require_numbers"] = require_numbers
        if require_symbols is not None:
            self._values["require_symbols"] = require_symbols
        if require_uppercase_characters is not None:
            self._values["require_uppercase_characters"] = require_uppercase_characters

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
    def allow_users_to_change_password(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iam_account_password_policy#allow_users_to_change_password IamAccountPasswordPolicy#allow_users_to_change_password}.'''
        result = self._values.get("allow_users_to_change_password")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def hard_expiry(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iam_account_password_policy#hard_expiry IamAccountPasswordPolicy#hard_expiry}.'''
        result = self._values.get("hard_expiry")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iam_account_password_policy#id IamAccountPasswordPolicy#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_password_age(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iam_account_password_policy#max_password_age IamAccountPasswordPolicy#max_password_age}.'''
        result = self._values.get("max_password_age")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def minimum_password_length(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iam_account_password_policy#minimum_password_length IamAccountPasswordPolicy#minimum_password_length}.'''
        result = self._values.get("minimum_password_length")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def password_reuse_prevention(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iam_account_password_policy#password_reuse_prevention IamAccountPasswordPolicy#password_reuse_prevention}.'''
        result = self._values.get("password_reuse_prevention")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def require_lowercase_characters(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iam_account_password_policy#require_lowercase_characters IamAccountPasswordPolicy#require_lowercase_characters}.'''
        result = self._values.get("require_lowercase_characters")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def require_numbers(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iam_account_password_policy#require_numbers IamAccountPasswordPolicy#require_numbers}.'''
        result = self._values.get("require_numbers")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def require_symbols(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iam_account_password_policy#require_symbols IamAccountPasswordPolicy#require_symbols}.'''
        result = self._values.get("require_symbols")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def require_uppercase_characters(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iam_account_password_policy#require_uppercase_characters IamAccountPasswordPolicy#require_uppercase_characters}.'''
        result = self._values.get("require_uppercase_characters")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IamAccountPasswordPolicyConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "IamAccountPasswordPolicy",
    "IamAccountPasswordPolicyConfig",
]

publication.publish()
