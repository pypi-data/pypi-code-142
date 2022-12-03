'''
# `aws_ce_cost_category`

Refer to the Terraform Registory for docs: [`aws_ce_cost_category`](https://www.terraform.io/docs/providers/aws/r/ce_cost_category).
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


class CeCostCategory(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ceCostCategory.CeCostCategory",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category aws_ce_cost_category}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        rule: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CeCostCategoryRule", typing.Dict[str, typing.Any]]]],
        rule_version: builtins.str,
        default_value: typing.Optional[builtins.str] = None,
        effective_start: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        split_charge_rule: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CeCostCategorySplitChargeRule", typing.Dict[str, typing.Any]]]]] = None,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category aws_ce_cost_category} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#name CeCostCategory#name}.
        :param rule: rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#rule CeCostCategory#rule}
        :param rule_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#rule_version CeCostCategory#rule_version}.
        :param default_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#default_value CeCostCategory#default_value}.
        :param effective_start: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#effective_start CeCostCategory#effective_start}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#id CeCostCategory#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param split_charge_rule: split_charge_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#split_charge_rule CeCostCategory#split_charge_rule}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#tags CeCostCategory#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#tags_all CeCostCategory#tags_all}.
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
                name: builtins.str,
                rule: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CeCostCategoryRule, typing.Dict[str, typing.Any]]]],
                rule_version: builtins.str,
                default_value: typing.Optional[builtins.str] = None,
                effective_start: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                split_charge_rule: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CeCostCategorySplitChargeRule, typing.Dict[str, typing.Any]]]]] = None,
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
        config = CeCostCategoryConfig(
            name=name,
            rule=rule,
            rule_version=rule_version,
            default_value=default_value,
            effective_start=effective_start,
            id=id,
            split_charge_rule=split_charge_rule,
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

    @jsii.member(jsii_name="putRule")
    def put_rule(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CeCostCategoryRule", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CeCostCategoryRule, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRule", [value]))

    @jsii.member(jsii_name="putSplitChargeRule")
    def put_split_charge_rule(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CeCostCategorySplitChargeRule", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CeCostCategorySplitChargeRule, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSplitChargeRule", [value]))

    @jsii.member(jsii_name="resetDefaultValue")
    def reset_default_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultValue", []))

    @jsii.member(jsii_name="resetEffectiveStart")
    def reset_effective_start(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEffectiveStart", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetSplitChargeRule")
    def reset_split_charge_rule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSplitChargeRule", []))

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
    @jsii.member(jsii_name="effectiveEnd")
    def effective_end(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "effectiveEnd"))

    @builtins.property
    @jsii.member(jsii_name="rule")
    def rule(self) -> "CeCostCategoryRuleList":
        return typing.cast("CeCostCategoryRuleList", jsii.get(self, "rule"))

    @builtins.property
    @jsii.member(jsii_name="splitChargeRule")
    def split_charge_rule(self) -> "CeCostCategorySplitChargeRuleList":
        return typing.cast("CeCostCategorySplitChargeRuleList", jsii.get(self, "splitChargeRule"))

    @builtins.property
    @jsii.member(jsii_name="defaultValueInput")
    def default_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultValueInput"))

    @builtins.property
    @jsii.member(jsii_name="effectiveStartInput")
    def effective_start_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "effectiveStartInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleInput")
    def rule_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CeCostCategoryRule"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CeCostCategoryRule"]]], jsii.get(self, "ruleInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleVersionInput")
    def rule_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ruleVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="splitChargeRuleInput")
    def split_charge_rule_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CeCostCategorySplitChargeRule"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CeCostCategorySplitChargeRule"]]], jsii.get(self, "splitChargeRuleInput"))

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
    @jsii.member(jsii_name="defaultValue")
    def default_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultValue"))

    @default_value.setter
    def default_value(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultValue", value)

    @builtins.property
    @jsii.member(jsii_name="effectiveStart")
    def effective_start(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "effectiveStart"))

    @effective_start.setter
    def effective_start(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "effectiveStart", value)

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
    @jsii.member(jsii_name="ruleVersion")
    def rule_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ruleVersion"))

    @rule_version.setter
    def rule_version(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleVersion", value)

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
    jsii_type="@cdktf/provider-aws.ceCostCategory.CeCostCategoryConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "name": "name",
        "rule": "rule",
        "rule_version": "ruleVersion",
        "default_value": "defaultValue",
        "effective_start": "effectiveStart",
        "id": "id",
        "split_charge_rule": "splitChargeRule",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class CeCostCategoryConfig(cdktf.TerraformMetaArguments):
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
        name: builtins.str,
        rule: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CeCostCategoryRule", typing.Dict[str, typing.Any]]]],
        rule_version: builtins.str,
        default_value: typing.Optional[builtins.str] = None,
        effective_start: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        split_charge_rule: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CeCostCategorySplitChargeRule", typing.Dict[str, typing.Any]]]]] = None,
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
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#name CeCostCategory#name}.
        :param rule: rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#rule CeCostCategory#rule}
        :param rule_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#rule_version CeCostCategory#rule_version}.
        :param default_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#default_value CeCostCategory#default_value}.
        :param effective_start: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#effective_start CeCostCategory#effective_start}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#id CeCostCategory#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param split_charge_rule: split_charge_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#split_charge_rule CeCostCategory#split_charge_rule}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#tags CeCostCategory#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#tags_all CeCostCategory#tags_all}.
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
                name: builtins.str,
                rule: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CeCostCategoryRule, typing.Dict[str, typing.Any]]]],
                rule_version: builtins.str,
                default_value: typing.Optional[builtins.str] = None,
                effective_start: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                split_charge_rule: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CeCostCategorySplitChargeRule, typing.Dict[str, typing.Any]]]]] = None,
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
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            check_type(argname="argument rule_version", value=rule_version, expected_type=type_hints["rule_version"])
            check_type(argname="argument default_value", value=default_value, expected_type=type_hints["default_value"])
            check_type(argname="argument effective_start", value=effective_start, expected_type=type_hints["effective_start"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument split_charge_rule", value=split_charge_rule, expected_type=type_hints["split_charge_rule"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "rule": rule,
            "rule_version": rule_version,
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
        if default_value is not None:
            self._values["default_value"] = default_value
        if effective_start is not None:
            self._values["effective_start"] = effective_start
        if id is not None:
            self._values["id"] = id
        if split_charge_rule is not None:
            self._values["split_charge_rule"] = split_charge_rule
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
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#name CeCostCategory#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rule(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["CeCostCategoryRule"]]:
        '''rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#rule CeCostCategory#rule}
        '''
        result = self._values.get("rule")
        assert result is not None, "Required property 'rule' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["CeCostCategoryRule"]], result)

    @builtins.property
    def rule_version(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#rule_version CeCostCategory#rule_version}.'''
        result = self._values.get("rule_version")
        assert result is not None, "Required property 'rule_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def default_value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#default_value CeCostCategory#default_value}.'''
        result = self._values.get("default_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def effective_start(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#effective_start CeCostCategory#effective_start}.'''
        result = self._values.get("effective_start")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#id CeCostCategory#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def split_charge_rule(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CeCostCategorySplitChargeRule"]]]:
        '''split_charge_rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#split_charge_rule CeCostCategory#split_charge_rule}
        '''
        result = self._values.get("split_charge_rule")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CeCostCategorySplitChargeRule"]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#tags CeCostCategory#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#tags_all CeCostCategory#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CeCostCategoryConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ceCostCategory.CeCostCategoryRule",
    jsii_struct_bases=[],
    name_mapping={
        "inherited_value": "inheritedValue",
        "rule": "rule",
        "type": "type",
        "value": "value",
    },
)
class CeCostCategoryRule:
    def __init__(
        self,
        *,
        inherited_value: typing.Optional[typing.Union["CeCostCategoryRuleInheritedValue", typing.Dict[str, typing.Any]]] = None,
        rule: typing.Optional[typing.Union["CeCostCategoryRuleRule", typing.Dict[str, typing.Any]]] = None,
        type: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param inherited_value: inherited_value block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#inherited_value CeCostCategory#inherited_value}
        :param rule: rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#rule CeCostCategory#rule}
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#type CeCostCategory#type}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#value CeCostCategory#value}.
        '''
        if isinstance(inherited_value, dict):
            inherited_value = CeCostCategoryRuleInheritedValue(**inherited_value)
        if isinstance(rule, dict):
            rule = CeCostCategoryRuleRule(**rule)
        if __debug__:
            def stub(
                *,
                inherited_value: typing.Optional[typing.Union[CeCostCategoryRuleInheritedValue, typing.Dict[str, typing.Any]]] = None,
                rule: typing.Optional[typing.Union[CeCostCategoryRuleRule, typing.Dict[str, typing.Any]]] = None,
                type: typing.Optional[builtins.str] = None,
                value: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument inherited_value", value=inherited_value, expected_type=type_hints["inherited_value"])
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if inherited_value is not None:
            self._values["inherited_value"] = inherited_value
        if rule is not None:
            self._values["rule"] = rule
        if type is not None:
            self._values["type"] = type
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def inherited_value(self) -> typing.Optional["CeCostCategoryRuleInheritedValue"]:
        '''inherited_value block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#inherited_value CeCostCategory#inherited_value}
        '''
        result = self._values.get("inherited_value")
        return typing.cast(typing.Optional["CeCostCategoryRuleInheritedValue"], result)

    @builtins.property
    def rule(self) -> typing.Optional["CeCostCategoryRuleRule"]:
        '''rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#rule CeCostCategory#rule}
        '''
        result = self._values.get("rule")
        return typing.cast(typing.Optional["CeCostCategoryRuleRule"], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#type CeCostCategory#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#value CeCostCategory#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CeCostCategoryRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ceCostCategory.CeCostCategoryRuleInheritedValue",
    jsii_struct_bases=[],
    name_mapping={"dimension_key": "dimensionKey", "dimension_name": "dimensionName"},
)
class CeCostCategoryRuleInheritedValue:
    def __init__(
        self,
        *,
        dimension_key: typing.Optional[builtins.str] = None,
        dimension_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param dimension_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#dimension_key CeCostCategory#dimension_key}.
        :param dimension_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#dimension_name CeCostCategory#dimension_name}.
        '''
        if __debug__:
            def stub(
                *,
                dimension_key: typing.Optional[builtins.str] = None,
                dimension_name: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument dimension_key", value=dimension_key, expected_type=type_hints["dimension_key"])
            check_type(argname="argument dimension_name", value=dimension_name, expected_type=type_hints["dimension_name"])
        self._values: typing.Dict[str, typing.Any] = {}
        if dimension_key is not None:
            self._values["dimension_key"] = dimension_key
        if dimension_name is not None:
            self._values["dimension_name"] = dimension_name

    @builtins.property
    def dimension_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#dimension_key CeCostCategory#dimension_key}.'''
        result = self._values.get("dimension_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dimension_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#dimension_name CeCostCategory#dimension_name}.'''
        result = self._values.get("dimension_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CeCostCategoryRuleInheritedValue(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CeCostCategoryRuleInheritedValueOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ceCostCategory.CeCostCategoryRuleInheritedValueOutputReference",
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

    @jsii.member(jsii_name="resetDimensionKey")
    def reset_dimension_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDimensionKey", []))

    @jsii.member(jsii_name="resetDimensionName")
    def reset_dimension_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDimensionName", []))

    @builtins.property
    @jsii.member(jsii_name="dimensionKeyInput")
    def dimension_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dimensionKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="dimensionNameInput")
    def dimension_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dimensionNameInput"))

    @builtins.property
    @jsii.member(jsii_name="dimensionKey")
    def dimension_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dimensionKey"))

    @dimension_key.setter
    def dimension_key(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dimensionKey", value)

    @builtins.property
    @jsii.member(jsii_name="dimensionName")
    def dimension_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dimensionName"))

    @dimension_name.setter
    def dimension_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dimensionName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CeCostCategoryRuleInheritedValue]:
        return typing.cast(typing.Optional[CeCostCategoryRuleInheritedValue], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CeCostCategoryRuleInheritedValue],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[CeCostCategoryRuleInheritedValue]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CeCostCategoryRuleList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ceCostCategory.CeCostCategoryRuleList",
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
    def get(self, index: jsii.Number) -> "CeCostCategoryRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CeCostCategoryRuleOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CeCostCategoryRule]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CeCostCategoryRule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CeCostCategoryRule]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CeCostCategoryRule]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CeCostCategoryRuleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ceCostCategory.CeCostCategoryRuleOutputReference",
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

    @jsii.member(jsii_name="putInheritedValue")
    def put_inherited_value(
        self,
        *,
        dimension_key: typing.Optional[builtins.str] = None,
        dimension_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param dimension_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#dimension_key CeCostCategory#dimension_key}.
        :param dimension_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#dimension_name CeCostCategory#dimension_name}.
        '''
        value = CeCostCategoryRuleInheritedValue(
            dimension_key=dimension_key, dimension_name=dimension_name
        )

        return typing.cast(None, jsii.invoke(self, "putInheritedValue", [value]))

    @jsii.member(jsii_name="putRule")
    def put_rule(
        self,
        *,
        and_: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CeCostCategoryRuleRuleAnd", typing.Dict[str, typing.Any]]]]] = None,
        cost_category: typing.Optional[typing.Union["CeCostCategoryRuleRuleCostCategory", typing.Dict[str, typing.Any]]] = None,
        dimension: typing.Optional[typing.Union["CeCostCategoryRuleRuleDimension", typing.Dict[str, typing.Any]]] = None,
        not_: typing.Optional[typing.Union["CeCostCategoryRuleRuleNot", typing.Dict[str, typing.Any]]] = None,
        or_: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CeCostCategoryRuleRuleOr", typing.Dict[str, typing.Any]]]]] = None,
        tags: typing.Optional[typing.Union["CeCostCategoryRuleRuleTags", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param and_: and block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#and CeCostCategory#and}
        :param cost_category: cost_category block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#cost_category CeCostCategory#cost_category}
        :param dimension: dimension block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#dimension CeCostCategory#dimension}
        :param not_: not block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#not CeCostCategory#not}
        :param or_: or block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#or CeCostCategory#or}
        :param tags: tags block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#tags CeCostCategory#tags}
        '''
        value = CeCostCategoryRuleRule(
            and_=and_,
            cost_category=cost_category,
            dimension=dimension,
            not_=not_,
            or_=or_,
            tags=tags,
        )

        return typing.cast(None, jsii.invoke(self, "putRule", [value]))

    @jsii.member(jsii_name="resetInheritedValue")
    def reset_inherited_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInheritedValue", []))

    @jsii.member(jsii_name="resetRule")
    def reset_rule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRule", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="inheritedValue")
    def inherited_value(self) -> CeCostCategoryRuleInheritedValueOutputReference:
        return typing.cast(CeCostCategoryRuleInheritedValueOutputReference, jsii.get(self, "inheritedValue"))

    @builtins.property
    @jsii.member(jsii_name="rule")
    def rule(self) -> "CeCostCategoryRuleRuleOutputReference":
        return typing.cast("CeCostCategoryRuleRuleOutputReference", jsii.get(self, "rule"))

    @builtins.property
    @jsii.member(jsii_name="inheritedValueInput")
    def inherited_value_input(
        self,
    ) -> typing.Optional[CeCostCategoryRuleInheritedValue]:
        return typing.cast(typing.Optional[CeCostCategoryRuleInheritedValue], jsii.get(self, "inheritedValueInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleInput")
    def rule_input(self) -> typing.Optional["CeCostCategoryRuleRule"]:
        return typing.cast(typing.Optional["CeCostCategoryRuleRule"], jsii.get(self, "ruleInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

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
    ) -> typing.Optional[typing.Union[CeCostCategoryRule, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CeCostCategoryRule, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CeCostCategoryRule, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[CeCostCategoryRule, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ceCostCategory.CeCostCategoryRuleRule",
    jsii_struct_bases=[],
    name_mapping={
        "and_": "and",
        "cost_category": "costCategory",
        "dimension": "dimension",
        "not_": "not",
        "or_": "or",
        "tags": "tags",
    },
)
class CeCostCategoryRuleRule:
    def __init__(
        self,
        *,
        and_: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CeCostCategoryRuleRuleAnd", typing.Dict[str, typing.Any]]]]] = None,
        cost_category: typing.Optional[typing.Union["CeCostCategoryRuleRuleCostCategory", typing.Dict[str, typing.Any]]] = None,
        dimension: typing.Optional[typing.Union["CeCostCategoryRuleRuleDimension", typing.Dict[str, typing.Any]]] = None,
        not_: typing.Optional[typing.Union["CeCostCategoryRuleRuleNot", typing.Dict[str, typing.Any]]] = None,
        or_: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CeCostCategoryRuleRuleOr", typing.Dict[str, typing.Any]]]]] = None,
        tags: typing.Optional[typing.Union["CeCostCategoryRuleRuleTags", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param and_: and block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#and CeCostCategory#and}
        :param cost_category: cost_category block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#cost_category CeCostCategory#cost_category}
        :param dimension: dimension block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#dimension CeCostCategory#dimension}
        :param not_: not block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#not CeCostCategory#not}
        :param or_: or block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#or CeCostCategory#or}
        :param tags: tags block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#tags CeCostCategory#tags}
        '''
        if isinstance(cost_category, dict):
            cost_category = CeCostCategoryRuleRuleCostCategory(**cost_category)
        if isinstance(dimension, dict):
            dimension = CeCostCategoryRuleRuleDimension(**dimension)
        if isinstance(not_, dict):
            not_ = CeCostCategoryRuleRuleNot(**not_)
        if isinstance(tags, dict):
            tags = CeCostCategoryRuleRuleTags(**tags)
        if __debug__:
            def stub(
                *,
                and_: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CeCostCategoryRuleRuleAnd, typing.Dict[str, typing.Any]]]]] = None,
                cost_category: typing.Optional[typing.Union[CeCostCategoryRuleRuleCostCategory, typing.Dict[str, typing.Any]]] = None,
                dimension: typing.Optional[typing.Union[CeCostCategoryRuleRuleDimension, typing.Dict[str, typing.Any]]] = None,
                not_: typing.Optional[typing.Union[CeCostCategoryRuleRuleNot, typing.Dict[str, typing.Any]]] = None,
                or_: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CeCostCategoryRuleRuleOr, typing.Dict[str, typing.Any]]]]] = None,
                tags: typing.Optional[typing.Union[CeCostCategoryRuleRuleTags, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument and_", value=and_, expected_type=type_hints["and_"])
            check_type(argname="argument cost_category", value=cost_category, expected_type=type_hints["cost_category"])
            check_type(argname="argument dimension", value=dimension, expected_type=type_hints["dimension"])
            check_type(argname="argument not_", value=not_, expected_type=type_hints["not_"])
            check_type(argname="argument or_", value=or_, expected_type=type_hints["or_"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {}
        if and_ is not None:
            self._values["and_"] = and_
        if cost_category is not None:
            self._values["cost_category"] = cost_category
        if dimension is not None:
            self._values["dimension"] = dimension
        if not_ is not None:
            self._values["not_"] = not_
        if or_ is not None:
            self._values["or_"] = or_
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def and_(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CeCostCategoryRuleRuleAnd"]]]:
        '''and block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#and CeCostCategory#and}
        '''
        result = self._values.get("and_")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CeCostCategoryRuleRuleAnd"]]], result)

    @builtins.property
    def cost_category(self) -> typing.Optional["CeCostCategoryRuleRuleCostCategory"]:
        '''cost_category block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#cost_category CeCostCategory#cost_category}
        '''
        result = self._values.get("cost_category")
        return typing.cast(typing.Optional["CeCostCategoryRuleRuleCostCategory"], result)

    @builtins.property
    def dimension(self) -> typing.Optional["CeCostCategoryRuleRuleDimension"]:
        '''dimension block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#dimension CeCostCategory#dimension}
        '''
        result = self._values.get("dimension")
        return typing.cast(typing.Optional["CeCostCategoryRuleRuleDimension"], result)

    @builtins.property
    def not_(self) -> typing.Optional["CeCostCategoryRuleRuleNot"]:
        '''not block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#not CeCostCategory#not}
        '''
        result = self._values.get("not_")
        return typing.cast(typing.Optional["CeCostCategoryRuleRuleNot"], result)

    @builtins.property
    def or_(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CeCostCategoryRuleRuleOr"]]]:
        '''or block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#or CeCostCategory#or}
        '''
        result = self._values.get("or_")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CeCostCategoryRuleRuleOr"]]], result)

    @builtins.property
    def tags(self) -> typing.Optional["CeCostCategoryRuleRuleTags"]:
        '''tags block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#tags CeCostCategory#tags}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional["CeCostCategoryRuleRuleTags"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CeCostCategoryRuleRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ceCostCategory.CeCostCategoryRuleRuleAnd",
    jsii_struct_bases=[],
    name_mapping={
        "cost_category": "costCategory",
        "dimension": "dimension",
        "tags": "tags",
    },
)
class CeCostCategoryRuleRuleAnd:
    def __init__(
        self,
        *,
        cost_category: typing.Optional[typing.Union["CeCostCategoryRuleRuleAndCostCategory", typing.Dict[str, typing.Any]]] = None,
        dimension: typing.Optional[typing.Union["CeCostCategoryRuleRuleAndDimension", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Union["CeCostCategoryRuleRuleAndTags", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param cost_category: cost_category block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#cost_category CeCostCategory#cost_category}
        :param dimension: dimension block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#dimension CeCostCategory#dimension}
        :param tags: tags block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#tags CeCostCategory#tags}
        '''
        if isinstance(cost_category, dict):
            cost_category = CeCostCategoryRuleRuleAndCostCategory(**cost_category)
        if isinstance(dimension, dict):
            dimension = CeCostCategoryRuleRuleAndDimension(**dimension)
        if isinstance(tags, dict):
            tags = CeCostCategoryRuleRuleAndTags(**tags)
        if __debug__:
            def stub(
                *,
                cost_category: typing.Optional[typing.Union[CeCostCategoryRuleRuleAndCostCategory, typing.Dict[str, typing.Any]]] = None,
                dimension: typing.Optional[typing.Union[CeCostCategoryRuleRuleAndDimension, typing.Dict[str, typing.Any]]] = None,
                tags: typing.Optional[typing.Union[CeCostCategoryRuleRuleAndTags, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument cost_category", value=cost_category, expected_type=type_hints["cost_category"])
            check_type(argname="argument dimension", value=dimension, expected_type=type_hints["dimension"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {}
        if cost_category is not None:
            self._values["cost_category"] = cost_category
        if dimension is not None:
            self._values["dimension"] = dimension
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def cost_category(self) -> typing.Optional["CeCostCategoryRuleRuleAndCostCategory"]:
        '''cost_category block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#cost_category CeCostCategory#cost_category}
        '''
        result = self._values.get("cost_category")
        return typing.cast(typing.Optional["CeCostCategoryRuleRuleAndCostCategory"], result)

    @builtins.property
    def dimension(self) -> typing.Optional["CeCostCategoryRuleRuleAndDimension"]:
        '''dimension block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#dimension CeCostCategory#dimension}
        '''
        result = self._values.get("dimension")
        return typing.cast(typing.Optional["CeCostCategoryRuleRuleAndDimension"], result)

    @builtins.property
    def tags(self) -> typing.Optional["CeCostCategoryRuleRuleAndTags"]:
        '''tags block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#tags CeCostCategory#tags}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional["CeCostCategoryRuleRuleAndTags"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CeCostCategoryRuleRuleAnd(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ceCostCategory.CeCostCategoryRuleRuleAndCostCategory",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "match_options": "matchOptions", "values": "values"},
)
class CeCostCategoryRuleRuleAndCostCategory:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.
        '''
        if __debug__:
            def stub(
                *,
                key: typing.Optional[builtins.str] = None,
                match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
                values: typing.Optional[typing.Sequence[builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument match_options", value=match_options, expected_type=type_hints["match_options"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if match_options is not None:
            self._values["match_options"] = match_options
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.'''
        result = self._values.get("match_options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CeCostCategoryRuleRuleAndCostCategory(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CeCostCategoryRuleRuleAndCostCategoryOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ceCostCategory.CeCostCategoryRuleRuleAndCostCategoryOutputReference",
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

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetMatchOptions")
    def reset_match_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchOptions", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="matchOptionsInput")
    def match_options_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

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
    @jsii.member(jsii_name="matchOptions")
    def match_options(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "matchOptions"))

    @match_options.setter
    def match_options(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchOptions", value)

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
    def internal_value(self) -> typing.Optional[CeCostCategoryRuleRuleAndCostCategory]:
        return typing.cast(typing.Optional[CeCostCategoryRuleRuleAndCostCategory], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CeCostCategoryRuleRuleAndCostCategory],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CeCostCategoryRuleRuleAndCostCategory],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ceCostCategory.CeCostCategoryRuleRuleAndDimension",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "match_options": "matchOptions", "values": "values"},
)
class CeCostCategoryRuleRuleAndDimension:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.
        '''
        if __debug__:
            def stub(
                *,
                key: typing.Optional[builtins.str] = None,
                match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
                values: typing.Optional[typing.Sequence[builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument match_options", value=match_options, expected_type=type_hints["match_options"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if match_options is not None:
            self._values["match_options"] = match_options
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.'''
        result = self._values.get("match_options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CeCostCategoryRuleRuleAndDimension(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CeCostCategoryRuleRuleAndDimensionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ceCostCategory.CeCostCategoryRuleRuleAndDimensionOutputReference",
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

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetMatchOptions")
    def reset_match_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchOptions", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="matchOptionsInput")
    def match_options_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

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
    @jsii.member(jsii_name="matchOptions")
    def match_options(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "matchOptions"))

    @match_options.setter
    def match_options(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchOptions", value)

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
    def internal_value(self) -> typing.Optional[CeCostCategoryRuleRuleAndDimension]:
        return typing.cast(typing.Optional[CeCostCategoryRuleRuleAndDimension], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CeCostCategoryRuleRuleAndDimension],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CeCostCategoryRuleRuleAndDimension],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CeCostCategoryRuleRuleAndList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ceCostCategory.CeCostCategoryRuleRuleAndList",
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
    def get(self, index: jsii.Number) -> "CeCostCategoryRuleRuleAndOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CeCostCategoryRuleRuleAndOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CeCostCategoryRuleRuleAnd]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CeCostCategoryRuleRuleAnd]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CeCostCategoryRuleRuleAnd]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CeCostCategoryRuleRuleAnd]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CeCostCategoryRuleRuleAndOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ceCostCategory.CeCostCategoryRuleRuleAndOutputReference",
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

    @jsii.member(jsii_name="putCostCategory")
    def put_cost_category(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.
        '''
        value = CeCostCategoryRuleRuleAndCostCategory(
            key=key, match_options=match_options, values=values
        )

        return typing.cast(None, jsii.invoke(self, "putCostCategory", [value]))

    @jsii.member(jsii_name="putDimension")
    def put_dimension(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.
        '''
        value = CeCostCategoryRuleRuleAndDimension(
            key=key, match_options=match_options, values=values
        )

        return typing.cast(None, jsii.invoke(self, "putDimension", [value]))

    @jsii.member(jsii_name="putTags")
    def put_tags(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.
        '''
        value = CeCostCategoryRuleRuleAndTags(
            key=key, match_options=match_options, values=values
        )

        return typing.cast(None, jsii.invoke(self, "putTags", [value]))

    @jsii.member(jsii_name="resetCostCategory")
    def reset_cost_category(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCostCategory", []))

    @jsii.member(jsii_name="resetDimension")
    def reset_dimension(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDimension", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @builtins.property
    @jsii.member(jsii_name="costCategory")
    def cost_category(self) -> CeCostCategoryRuleRuleAndCostCategoryOutputReference:
        return typing.cast(CeCostCategoryRuleRuleAndCostCategoryOutputReference, jsii.get(self, "costCategory"))

    @builtins.property
    @jsii.member(jsii_name="dimension")
    def dimension(self) -> CeCostCategoryRuleRuleAndDimensionOutputReference:
        return typing.cast(CeCostCategoryRuleRuleAndDimensionOutputReference, jsii.get(self, "dimension"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> "CeCostCategoryRuleRuleAndTagsOutputReference":
        return typing.cast("CeCostCategoryRuleRuleAndTagsOutputReference", jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="costCategoryInput")
    def cost_category_input(
        self,
    ) -> typing.Optional[CeCostCategoryRuleRuleAndCostCategory]:
        return typing.cast(typing.Optional[CeCostCategoryRuleRuleAndCostCategory], jsii.get(self, "costCategoryInput"))

    @builtins.property
    @jsii.member(jsii_name="dimensionInput")
    def dimension_input(self) -> typing.Optional[CeCostCategoryRuleRuleAndDimension]:
        return typing.cast(typing.Optional[CeCostCategoryRuleRuleAndDimension], jsii.get(self, "dimensionInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional["CeCostCategoryRuleRuleAndTags"]:
        return typing.cast(typing.Optional["CeCostCategoryRuleRuleAndTags"], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CeCostCategoryRuleRuleAnd, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CeCostCategoryRuleRuleAnd, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CeCostCategoryRuleRuleAnd, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[CeCostCategoryRuleRuleAnd, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ceCostCategory.CeCostCategoryRuleRuleAndTags",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "match_options": "matchOptions", "values": "values"},
)
class CeCostCategoryRuleRuleAndTags:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.
        '''
        if __debug__:
            def stub(
                *,
                key: typing.Optional[builtins.str] = None,
                match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
                values: typing.Optional[typing.Sequence[builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument match_options", value=match_options, expected_type=type_hints["match_options"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if match_options is not None:
            self._values["match_options"] = match_options
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.'''
        result = self._values.get("match_options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CeCostCategoryRuleRuleAndTags(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CeCostCategoryRuleRuleAndTagsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ceCostCategory.CeCostCategoryRuleRuleAndTagsOutputReference",
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

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetMatchOptions")
    def reset_match_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchOptions", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="matchOptionsInput")
    def match_options_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

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
    @jsii.member(jsii_name="matchOptions")
    def match_options(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "matchOptions"))

    @match_options.setter
    def match_options(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchOptions", value)

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
    def internal_value(self) -> typing.Optional[CeCostCategoryRuleRuleAndTags]:
        return typing.cast(typing.Optional[CeCostCategoryRuleRuleAndTags], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CeCostCategoryRuleRuleAndTags],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[CeCostCategoryRuleRuleAndTags]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ceCostCategory.CeCostCategoryRuleRuleCostCategory",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "match_options": "matchOptions", "values": "values"},
)
class CeCostCategoryRuleRuleCostCategory:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.
        '''
        if __debug__:
            def stub(
                *,
                key: typing.Optional[builtins.str] = None,
                match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
                values: typing.Optional[typing.Sequence[builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument match_options", value=match_options, expected_type=type_hints["match_options"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if match_options is not None:
            self._values["match_options"] = match_options
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.'''
        result = self._values.get("match_options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CeCostCategoryRuleRuleCostCategory(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CeCostCategoryRuleRuleCostCategoryOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ceCostCategory.CeCostCategoryRuleRuleCostCategoryOutputReference",
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

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetMatchOptions")
    def reset_match_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchOptions", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="matchOptionsInput")
    def match_options_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

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
    @jsii.member(jsii_name="matchOptions")
    def match_options(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "matchOptions"))

    @match_options.setter
    def match_options(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchOptions", value)

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
    def internal_value(self) -> typing.Optional[CeCostCategoryRuleRuleCostCategory]:
        return typing.cast(typing.Optional[CeCostCategoryRuleRuleCostCategory], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CeCostCategoryRuleRuleCostCategory],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CeCostCategoryRuleRuleCostCategory],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ceCostCategory.CeCostCategoryRuleRuleDimension",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "match_options": "matchOptions", "values": "values"},
)
class CeCostCategoryRuleRuleDimension:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.
        '''
        if __debug__:
            def stub(
                *,
                key: typing.Optional[builtins.str] = None,
                match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
                values: typing.Optional[typing.Sequence[builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument match_options", value=match_options, expected_type=type_hints["match_options"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if match_options is not None:
            self._values["match_options"] = match_options
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.'''
        result = self._values.get("match_options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CeCostCategoryRuleRuleDimension(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CeCostCategoryRuleRuleDimensionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ceCostCategory.CeCostCategoryRuleRuleDimensionOutputReference",
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

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetMatchOptions")
    def reset_match_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchOptions", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="matchOptionsInput")
    def match_options_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

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
    @jsii.member(jsii_name="matchOptions")
    def match_options(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "matchOptions"))

    @match_options.setter
    def match_options(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchOptions", value)

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
    def internal_value(self) -> typing.Optional[CeCostCategoryRuleRuleDimension]:
        return typing.cast(typing.Optional[CeCostCategoryRuleRuleDimension], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CeCostCategoryRuleRuleDimension],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[CeCostCategoryRuleRuleDimension]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ceCostCategory.CeCostCategoryRuleRuleNot",
    jsii_struct_bases=[],
    name_mapping={
        "cost_category": "costCategory",
        "dimension": "dimension",
        "tags": "tags",
    },
)
class CeCostCategoryRuleRuleNot:
    def __init__(
        self,
        *,
        cost_category: typing.Optional[typing.Union["CeCostCategoryRuleRuleNotCostCategory", typing.Dict[str, typing.Any]]] = None,
        dimension: typing.Optional[typing.Union["CeCostCategoryRuleRuleNotDimension", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Union["CeCostCategoryRuleRuleNotTags", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param cost_category: cost_category block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#cost_category CeCostCategory#cost_category}
        :param dimension: dimension block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#dimension CeCostCategory#dimension}
        :param tags: tags block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#tags CeCostCategory#tags}
        '''
        if isinstance(cost_category, dict):
            cost_category = CeCostCategoryRuleRuleNotCostCategory(**cost_category)
        if isinstance(dimension, dict):
            dimension = CeCostCategoryRuleRuleNotDimension(**dimension)
        if isinstance(tags, dict):
            tags = CeCostCategoryRuleRuleNotTags(**tags)
        if __debug__:
            def stub(
                *,
                cost_category: typing.Optional[typing.Union[CeCostCategoryRuleRuleNotCostCategory, typing.Dict[str, typing.Any]]] = None,
                dimension: typing.Optional[typing.Union[CeCostCategoryRuleRuleNotDimension, typing.Dict[str, typing.Any]]] = None,
                tags: typing.Optional[typing.Union[CeCostCategoryRuleRuleNotTags, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument cost_category", value=cost_category, expected_type=type_hints["cost_category"])
            check_type(argname="argument dimension", value=dimension, expected_type=type_hints["dimension"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {}
        if cost_category is not None:
            self._values["cost_category"] = cost_category
        if dimension is not None:
            self._values["dimension"] = dimension
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def cost_category(self) -> typing.Optional["CeCostCategoryRuleRuleNotCostCategory"]:
        '''cost_category block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#cost_category CeCostCategory#cost_category}
        '''
        result = self._values.get("cost_category")
        return typing.cast(typing.Optional["CeCostCategoryRuleRuleNotCostCategory"], result)

    @builtins.property
    def dimension(self) -> typing.Optional["CeCostCategoryRuleRuleNotDimension"]:
        '''dimension block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#dimension CeCostCategory#dimension}
        '''
        result = self._values.get("dimension")
        return typing.cast(typing.Optional["CeCostCategoryRuleRuleNotDimension"], result)

    @builtins.property
    def tags(self) -> typing.Optional["CeCostCategoryRuleRuleNotTags"]:
        '''tags block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#tags CeCostCategory#tags}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional["CeCostCategoryRuleRuleNotTags"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CeCostCategoryRuleRuleNot(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ceCostCategory.CeCostCategoryRuleRuleNotCostCategory",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "match_options": "matchOptions", "values": "values"},
)
class CeCostCategoryRuleRuleNotCostCategory:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.
        '''
        if __debug__:
            def stub(
                *,
                key: typing.Optional[builtins.str] = None,
                match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
                values: typing.Optional[typing.Sequence[builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument match_options", value=match_options, expected_type=type_hints["match_options"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if match_options is not None:
            self._values["match_options"] = match_options
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.'''
        result = self._values.get("match_options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CeCostCategoryRuleRuleNotCostCategory(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CeCostCategoryRuleRuleNotCostCategoryOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ceCostCategory.CeCostCategoryRuleRuleNotCostCategoryOutputReference",
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

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetMatchOptions")
    def reset_match_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchOptions", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="matchOptionsInput")
    def match_options_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

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
    @jsii.member(jsii_name="matchOptions")
    def match_options(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "matchOptions"))

    @match_options.setter
    def match_options(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchOptions", value)

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
    def internal_value(self) -> typing.Optional[CeCostCategoryRuleRuleNotCostCategory]:
        return typing.cast(typing.Optional[CeCostCategoryRuleRuleNotCostCategory], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CeCostCategoryRuleRuleNotCostCategory],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CeCostCategoryRuleRuleNotCostCategory],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ceCostCategory.CeCostCategoryRuleRuleNotDimension",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "match_options": "matchOptions", "values": "values"},
)
class CeCostCategoryRuleRuleNotDimension:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.
        '''
        if __debug__:
            def stub(
                *,
                key: typing.Optional[builtins.str] = None,
                match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
                values: typing.Optional[typing.Sequence[builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument match_options", value=match_options, expected_type=type_hints["match_options"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if match_options is not None:
            self._values["match_options"] = match_options
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.'''
        result = self._values.get("match_options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CeCostCategoryRuleRuleNotDimension(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CeCostCategoryRuleRuleNotDimensionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ceCostCategory.CeCostCategoryRuleRuleNotDimensionOutputReference",
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

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetMatchOptions")
    def reset_match_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchOptions", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="matchOptionsInput")
    def match_options_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

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
    @jsii.member(jsii_name="matchOptions")
    def match_options(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "matchOptions"))

    @match_options.setter
    def match_options(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchOptions", value)

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
    def internal_value(self) -> typing.Optional[CeCostCategoryRuleRuleNotDimension]:
        return typing.cast(typing.Optional[CeCostCategoryRuleRuleNotDimension], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CeCostCategoryRuleRuleNotDimension],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CeCostCategoryRuleRuleNotDimension],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CeCostCategoryRuleRuleNotOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ceCostCategory.CeCostCategoryRuleRuleNotOutputReference",
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

    @jsii.member(jsii_name="putCostCategory")
    def put_cost_category(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.
        '''
        value = CeCostCategoryRuleRuleNotCostCategory(
            key=key, match_options=match_options, values=values
        )

        return typing.cast(None, jsii.invoke(self, "putCostCategory", [value]))

    @jsii.member(jsii_name="putDimension")
    def put_dimension(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.
        '''
        value = CeCostCategoryRuleRuleNotDimension(
            key=key, match_options=match_options, values=values
        )

        return typing.cast(None, jsii.invoke(self, "putDimension", [value]))

    @jsii.member(jsii_name="putTags")
    def put_tags(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.
        '''
        value = CeCostCategoryRuleRuleNotTags(
            key=key, match_options=match_options, values=values
        )

        return typing.cast(None, jsii.invoke(self, "putTags", [value]))

    @jsii.member(jsii_name="resetCostCategory")
    def reset_cost_category(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCostCategory", []))

    @jsii.member(jsii_name="resetDimension")
    def reset_dimension(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDimension", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @builtins.property
    @jsii.member(jsii_name="costCategory")
    def cost_category(self) -> CeCostCategoryRuleRuleNotCostCategoryOutputReference:
        return typing.cast(CeCostCategoryRuleRuleNotCostCategoryOutputReference, jsii.get(self, "costCategory"))

    @builtins.property
    @jsii.member(jsii_name="dimension")
    def dimension(self) -> CeCostCategoryRuleRuleNotDimensionOutputReference:
        return typing.cast(CeCostCategoryRuleRuleNotDimensionOutputReference, jsii.get(self, "dimension"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> "CeCostCategoryRuleRuleNotTagsOutputReference":
        return typing.cast("CeCostCategoryRuleRuleNotTagsOutputReference", jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="costCategoryInput")
    def cost_category_input(
        self,
    ) -> typing.Optional[CeCostCategoryRuleRuleNotCostCategory]:
        return typing.cast(typing.Optional[CeCostCategoryRuleRuleNotCostCategory], jsii.get(self, "costCategoryInput"))

    @builtins.property
    @jsii.member(jsii_name="dimensionInput")
    def dimension_input(self) -> typing.Optional[CeCostCategoryRuleRuleNotDimension]:
        return typing.cast(typing.Optional[CeCostCategoryRuleRuleNotDimension], jsii.get(self, "dimensionInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional["CeCostCategoryRuleRuleNotTags"]:
        return typing.cast(typing.Optional["CeCostCategoryRuleRuleNotTags"], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CeCostCategoryRuleRuleNot]:
        return typing.cast(typing.Optional[CeCostCategoryRuleRuleNot], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[CeCostCategoryRuleRuleNot]) -> None:
        if __debug__:
            def stub(value: typing.Optional[CeCostCategoryRuleRuleNot]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ceCostCategory.CeCostCategoryRuleRuleNotTags",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "match_options": "matchOptions", "values": "values"},
)
class CeCostCategoryRuleRuleNotTags:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.
        '''
        if __debug__:
            def stub(
                *,
                key: typing.Optional[builtins.str] = None,
                match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
                values: typing.Optional[typing.Sequence[builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument match_options", value=match_options, expected_type=type_hints["match_options"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if match_options is not None:
            self._values["match_options"] = match_options
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.'''
        result = self._values.get("match_options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CeCostCategoryRuleRuleNotTags(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CeCostCategoryRuleRuleNotTagsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ceCostCategory.CeCostCategoryRuleRuleNotTagsOutputReference",
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

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetMatchOptions")
    def reset_match_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchOptions", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="matchOptionsInput")
    def match_options_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

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
    @jsii.member(jsii_name="matchOptions")
    def match_options(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "matchOptions"))

    @match_options.setter
    def match_options(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchOptions", value)

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
    def internal_value(self) -> typing.Optional[CeCostCategoryRuleRuleNotTags]:
        return typing.cast(typing.Optional[CeCostCategoryRuleRuleNotTags], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CeCostCategoryRuleRuleNotTags],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[CeCostCategoryRuleRuleNotTags]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ceCostCategory.CeCostCategoryRuleRuleOr",
    jsii_struct_bases=[],
    name_mapping={
        "cost_category": "costCategory",
        "dimension": "dimension",
        "tags": "tags",
    },
)
class CeCostCategoryRuleRuleOr:
    def __init__(
        self,
        *,
        cost_category: typing.Optional[typing.Union["CeCostCategoryRuleRuleOrCostCategory", typing.Dict[str, typing.Any]]] = None,
        dimension: typing.Optional[typing.Union["CeCostCategoryRuleRuleOrDimension", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Union["CeCostCategoryRuleRuleOrTags", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param cost_category: cost_category block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#cost_category CeCostCategory#cost_category}
        :param dimension: dimension block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#dimension CeCostCategory#dimension}
        :param tags: tags block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#tags CeCostCategory#tags}
        '''
        if isinstance(cost_category, dict):
            cost_category = CeCostCategoryRuleRuleOrCostCategory(**cost_category)
        if isinstance(dimension, dict):
            dimension = CeCostCategoryRuleRuleOrDimension(**dimension)
        if isinstance(tags, dict):
            tags = CeCostCategoryRuleRuleOrTags(**tags)
        if __debug__:
            def stub(
                *,
                cost_category: typing.Optional[typing.Union[CeCostCategoryRuleRuleOrCostCategory, typing.Dict[str, typing.Any]]] = None,
                dimension: typing.Optional[typing.Union[CeCostCategoryRuleRuleOrDimension, typing.Dict[str, typing.Any]]] = None,
                tags: typing.Optional[typing.Union[CeCostCategoryRuleRuleOrTags, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument cost_category", value=cost_category, expected_type=type_hints["cost_category"])
            check_type(argname="argument dimension", value=dimension, expected_type=type_hints["dimension"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {}
        if cost_category is not None:
            self._values["cost_category"] = cost_category
        if dimension is not None:
            self._values["dimension"] = dimension
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def cost_category(self) -> typing.Optional["CeCostCategoryRuleRuleOrCostCategory"]:
        '''cost_category block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#cost_category CeCostCategory#cost_category}
        '''
        result = self._values.get("cost_category")
        return typing.cast(typing.Optional["CeCostCategoryRuleRuleOrCostCategory"], result)

    @builtins.property
    def dimension(self) -> typing.Optional["CeCostCategoryRuleRuleOrDimension"]:
        '''dimension block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#dimension CeCostCategory#dimension}
        '''
        result = self._values.get("dimension")
        return typing.cast(typing.Optional["CeCostCategoryRuleRuleOrDimension"], result)

    @builtins.property
    def tags(self) -> typing.Optional["CeCostCategoryRuleRuleOrTags"]:
        '''tags block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#tags CeCostCategory#tags}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional["CeCostCategoryRuleRuleOrTags"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CeCostCategoryRuleRuleOr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ceCostCategory.CeCostCategoryRuleRuleOrCostCategory",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "match_options": "matchOptions", "values": "values"},
)
class CeCostCategoryRuleRuleOrCostCategory:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.
        '''
        if __debug__:
            def stub(
                *,
                key: typing.Optional[builtins.str] = None,
                match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
                values: typing.Optional[typing.Sequence[builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument match_options", value=match_options, expected_type=type_hints["match_options"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if match_options is not None:
            self._values["match_options"] = match_options
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.'''
        result = self._values.get("match_options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CeCostCategoryRuleRuleOrCostCategory(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CeCostCategoryRuleRuleOrCostCategoryOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ceCostCategory.CeCostCategoryRuleRuleOrCostCategoryOutputReference",
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

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetMatchOptions")
    def reset_match_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchOptions", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="matchOptionsInput")
    def match_options_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

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
    @jsii.member(jsii_name="matchOptions")
    def match_options(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "matchOptions"))

    @match_options.setter
    def match_options(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchOptions", value)

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
    def internal_value(self) -> typing.Optional[CeCostCategoryRuleRuleOrCostCategory]:
        return typing.cast(typing.Optional[CeCostCategoryRuleRuleOrCostCategory], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CeCostCategoryRuleRuleOrCostCategory],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CeCostCategoryRuleRuleOrCostCategory],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ceCostCategory.CeCostCategoryRuleRuleOrDimension",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "match_options": "matchOptions", "values": "values"},
)
class CeCostCategoryRuleRuleOrDimension:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.
        '''
        if __debug__:
            def stub(
                *,
                key: typing.Optional[builtins.str] = None,
                match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
                values: typing.Optional[typing.Sequence[builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument match_options", value=match_options, expected_type=type_hints["match_options"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if match_options is not None:
            self._values["match_options"] = match_options
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.'''
        result = self._values.get("match_options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CeCostCategoryRuleRuleOrDimension(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CeCostCategoryRuleRuleOrDimensionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ceCostCategory.CeCostCategoryRuleRuleOrDimensionOutputReference",
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

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetMatchOptions")
    def reset_match_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchOptions", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="matchOptionsInput")
    def match_options_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

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
    @jsii.member(jsii_name="matchOptions")
    def match_options(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "matchOptions"))

    @match_options.setter
    def match_options(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchOptions", value)

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
    def internal_value(self) -> typing.Optional[CeCostCategoryRuleRuleOrDimension]:
        return typing.cast(typing.Optional[CeCostCategoryRuleRuleOrDimension], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CeCostCategoryRuleRuleOrDimension],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[CeCostCategoryRuleRuleOrDimension]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CeCostCategoryRuleRuleOrList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ceCostCategory.CeCostCategoryRuleRuleOrList",
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
    def get(self, index: jsii.Number) -> "CeCostCategoryRuleRuleOrOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CeCostCategoryRuleRuleOrOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CeCostCategoryRuleRuleOr]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CeCostCategoryRuleRuleOr]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CeCostCategoryRuleRuleOr]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CeCostCategoryRuleRuleOr]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CeCostCategoryRuleRuleOrOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ceCostCategory.CeCostCategoryRuleRuleOrOutputReference",
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

    @jsii.member(jsii_name="putCostCategory")
    def put_cost_category(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.
        '''
        value = CeCostCategoryRuleRuleOrCostCategory(
            key=key, match_options=match_options, values=values
        )

        return typing.cast(None, jsii.invoke(self, "putCostCategory", [value]))

    @jsii.member(jsii_name="putDimension")
    def put_dimension(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.
        '''
        value = CeCostCategoryRuleRuleOrDimension(
            key=key, match_options=match_options, values=values
        )

        return typing.cast(None, jsii.invoke(self, "putDimension", [value]))

    @jsii.member(jsii_name="putTags")
    def put_tags(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.
        '''
        value = CeCostCategoryRuleRuleOrTags(
            key=key, match_options=match_options, values=values
        )

        return typing.cast(None, jsii.invoke(self, "putTags", [value]))

    @jsii.member(jsii_name="resetCostCategory")
    def reset_cost_category(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCostCategory", []))

    @jsii.member(jsii_name="resetDimension")
    def reset_dimension(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDimension", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @builtins.property
    @jsii.member(jsii_name="costCategory")
    def cost_category(self) -> CeCostCategoryRuleRuleOrCostCategoryOutputReference:
        return typing.cast(CeCostCategoryRuleRuleOrCostCategoryOutputReference, jsii.get(self, "costCategory"))

    @builtins.property
    @jsii.member(jsii_name="dimension")
    def dimension(self) -> CeCostCategoryRuleRuleOrDimensionOutputReference:
        return typing.cast(CeCostCategoryRuleRuleOrDimensionOutputReference, jsii.get(self, "dimension"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> "CeCostCategoryRuleRuleOrTagsOutputReference":
        return typing.cast("CeCostCategoryRuleRuleOrTagsOutputReference", jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="costCategoryInput")
    def cost_category_input(
        self,
    ) -> typing.Optional[CeCostCategoryRuleRuleOrCostCategory]:
        return typing.cast(typing.Optional[CeCostCategoryRuleRuleOrCostCategory], jsii.get(self, "costCategoryInput"))

    @builtins.property
    @jsii.member(jsii_name="dimensionInput")
    def dimension_input(self) -> typing.Optional[CeCostCategoryRuleRuleOrDimension]:
        return typing.cast(typing.Optional[CeCostCategoryRuleRuleOrDimension], jsii.get(self, "dimensionInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional["CeCostCategoryRuleRuleOrTags"]:
        return typing.cast(typing.Optional["CeCostCategoryRuleRuleOrTags"], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CeCostCategoryRuleRuleOr, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CeCostCategoryRuleRuleOr, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CeCostCategoryRuleRuleOr, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[CeCostCategoryRuleRuleOr, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ceCostCategory.CeCostCategoryRuleRuleOrTags",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "match_options": "matchOptions", "values": "values"},
)
class CeCostCategoryRuleRuleOrTags:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.
        '''
        if __debug__:
            def stub(
                *,
                key: typing.Optional[builtins.str] = None,
                match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
                values: typing.Optional[typing.Sequence[builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument match_options", value=match_options, expected_type=type_hints["match_options"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if match_options is not None:
            self._values["match_options"] = match_options
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.'''
        result = self._values.get("match_options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CeCostCategoryRuleRuleOrTags(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CeCostCategoryRuleRuleOrTagsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ceCostCategory.CeCostCategoryRuleRuleOrTagsOutputReference",
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

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetMatchOptions")
    def reset_match_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchOptions", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="matchOptionsInput")
    def match_options_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

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
    @jsii.member(jsii_name="matchOptions")
    def match_options(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "matchOptions"))

    @match_options.setter
    def match_options(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchOptions", value)

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
    def internal_value(self) -> typing.Optional[CeCostCategoryRuleRuleOrTags]:
        return typing.cast(typing.Optional[CeCostCategoryRuleRuleOrTags], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CeCostCategoryRuleRuleOrTags],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[CeCostCategoryRuleRuleOrTags]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CeCostCategoryRuleRuleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ceCostCategory.CeCostCategoryRuleRuleOutputReference",
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

    @jsii.member(jsii_name="putAnd")
    def put_and(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CeCostCategoryRuleRuleAnd, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CeCostCategoryRuleRuleAnd, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAnd", [value]))

    @jsii.member(jsii_name="putCostCategory")
    def put_cost_category(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.
        '''
        value = CeCostCategoryRuleRuleCostCategory(
            key=key, match_options=match_options, values=values
        )

        return typing.cast(None, jsii.invoke(self, "putCostCategory", [value]))

    @jsii.member(jsii_name="putDimension")
    def put_dimension(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.
        '''
        value = CeCostCategoryRuleRuleDimension(
            key=key, match_options=match_options, values=values
        )

        return typing.cast(None, jsii.invoke(self, "putDimension", [value]))

    @jsii.member(jsii_name="putNot")
    def put_not(
        self,
        *,
        cost_category: typing.Optional[typing.Union[CeCostCategoryRuleRuleNotCostCategory, typing.Dict[str, typing.Any]]] = None,
        dimension: typing.Optional[typing.Union[CeCostCategoryRuleRuleNotDimension, typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Union[CeCostCategoryRuleRuleNotTags, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param cost_category: cost_category block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#cost_category CeCostCategory#cost_category}
        :param dimension: dimension block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#dimension CeCostCategory#dimension}
        :param tags: tags block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#tags CeCostCategory#tags}
        '''
        value = CeCostCategoryRuleRuleNot(
            cost_category=cost_category, dimension=dimension, tags=tags
        )

        return typing.cast(None, jsii.invoke(self, "putNot", [value]))

    @jsii.member(jsii_name="putOr")
    def put_or(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CeCostCategoryRuleRuleOr, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CeCostCategoryRuleRuleOr, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putOr", [value]))

    @jsii.member(jsii_name="putTags")
    def put_tags(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.
        '''
        value = CeCostCategoryRuleRuleTags(
            key=key, match_options=match_options, values=values
        )

        return typing.cast(None, jsii.invoke(self, "putTags", [value]))

    @jsii.member(jsii_name="resetAnd")
    def reset_and(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAnd", []))

    @jsii.member(jsii_name="resetCostCategory")
    def reset_cost_category(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCostCategory", []))

    @jsii.member(jsii_name="resetDimension")
    def reset_dimension(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDimension", []))

    @jsii.member(jsii_name="resetNot")
    def reset_not(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNot", []))

    @jsii.member(jsii_name="resetOr")
    def reset_or(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOr", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @builtins.property
    @jsii.member(jsii_name="and")
    def and_(self) -> CeCostCategoryRuleRuleAndList:
        return typing.cast(CeCostCategoryRuleRuleAndList, jsii.get(self, "and"))

    @builtins.property
    @jsii.member(jsii_name="costCategory")
    def cost_category(self) -> CeCostCategoryRuleRuleCostCategoryOutputReference:
        return typing.cast(CeCostCategoryRuleRuleCostCategoryOutputReference, jsii.get(self, "costCategory"))

    @builtins.property
    @jsii.member(jsii_name="dimension")
    def dimension(self) -> CeCostCategoryRuleRuleDimensionOutputReference:
        return typing.cast(CeCostCategoryRuleRuleDimensionOutputReference, jsii.get(self, "dimension"))

    @builtins.property
    @jsii.member(jsii_name="not")
    def not_(self) -> CeCostCategoryRuleRuleNotOutputReference:
        return typing.cast(CeCostCategoryRuleRuleNotOutputReference, jsii.get(self, "not"))

    @builtins.property
    @jsii.member(jsii_name="or")
    def or_(self) -> CeCostCategoryRuleRuleOrList:
        return typing.cast(CeCostCategoryRuleRuleOrList, jsii.get(self, "or"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> "CeCostCategoryRuleRuleTagsOutputReference":
        return typing.cast("CeCostCategoryRuleRuleTagsOutputReference", jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="andInput")
    def and_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CeCostCategoryRuleRuleAnd]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CeCostCategoryRuleRuleAnd]]], jsii.get(self, "andInput"))

    @builtins.property
    @jsii.member(jsii_name="costCategoryInput")
    def cost_category_input(
        self,
    ) -> typing.Optional[CeCostCategoryRuleRuleCostCategory]:
        return typing.cast(typing.Optional[CeCostCategoryRuleRuleCostCategory], jsii.get(self, "costCategoryInput"))

    @builtins.property
    @jsii.member(jsii_name="dimensionInput")
    def dimension_input(self) -> typing.Optional[CeCostCategoryRuleRuleDimension]:
        return typing.cast(typing.Optional[CeCostCategoryRuleRuleDimension], jsii.get(self, "dimensionInput"))

    @builtins.property
    @jsii.member(jsii_name="notInput")
    def not_input(self) -> typing.Optional[CeCostCategoryRuleRuleNot]:
        return typing.cast(typing.Optional[CeCostCategoryRuleRuleNot], jsii.get(self, "notInput"))

    @builtins.property
    @jsii.member(jsii_name="orInput")
    def or_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CeCostCategoryRuleRuleOr]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CeCostCategoryRuleRuleOr]]], jsii.get(self, "orInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional["CeCostCategoryRuleRuleTags"]:
        return typing.cast(typing.Optional["CeCostCategoryRuleRuleTags"], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CeCostCategoryRuleRule]:
        return typing.cast(typing.Optional[CeCostCategoryRuleRule], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[CeCostCategoryRuleRule]) -> None:
        if __debug__:
            def stub(value: typing.Optional[CeCostCategoryRuleRule]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ceCostCategory.CeCostCategoryRuleRuleTags",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "match_options": "matchOptions", "values": "values"},
)
class CeCostCategoryRuleRuleTags:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.
        '''
        if __debug__:
            def stub(
                *,
                key: typing.Optional[builtins.str] = None,
                match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
                values: typing.Optional[typing.Sequence[builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument match_options", value=match_options, expected_type=type_hints["match_options"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if match_options is not None:
            self._values["match_options"] = match_options
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#key CeCostCategory#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#match_options CeCostCategory#match_options}.'''
        result = self._values.get("match_options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CeCostCategoryRuleRuleTags(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CeCostCategoryRuleRuleTagsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ceCostCategory.CeCostCategoryRuleRuleTagsOutputReference",
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

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetMatchOptions")
    def reset_match_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchOptions", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="matchOptionsInput")
    def match_options_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

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
    @jsii.member(jsii_name="matchOptions")
    def match_options(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "matchOptions"))

    @match_options.setter
    def match_options(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchOptions", value)

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
    def internal_value(self) -> typing.Optional[CeCostCategoryRuleRuleTags]:
        return typing.cast(typing.Optional[CeCostCategoryRuleRuleTags], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CeCostCategoryRuleRuleTags],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[CeCostCategoryRuleRuleTags]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ceCostCategory.CeCostCategorySplitChargeRule",
    jsii_struct_bases=[],
    name_mapping={
        "method": "method",
        "source": "source",
        "targets": "targets",
        "parameter": "parameter",
    },
)
class CeCostCategorySplitChargeRule:
    def __init__(
        self,
        *,
        method: builtins.str,
        source: builtins.str,
        targets: typing.Sequence[builtins.str],
        parameter: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CeCostCategorySplitChargeRuleParameter", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param method: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#method CeCostCategory#method}.
        :param source: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#source CeCostCategory#source}.
        :param targets: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#targets CeCostCategory#targets}.
        :param parameter: parameter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#parameter CeCostCategory#parameter}
        '''
        if __debug__:
            def stub(
                *,
                method: builtins.str,
                source: builtins.str,
                targets: typing.Sequence[builtins.str],
                parameter: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CeCostCategorySplitChargeRuleParameter, typing.Dict[str, typing.Any]]]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument method", value=method, expected_type=type_hints["method"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument targets", value=targets, expected_type=type_hints["targets"])
            check_type(argname="argument parameter", value=parameter, expected_type=type_hints["parameter"])
        self._values: typing.Dict[str, typing.Any] = {
            "method": method,
            "source": source,
            "targets": targets,
        }
        if parameter is not None:
            self._values["parameter"] = parameter

    @builtins.property
    def method(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#method CeCostCategory#method}.'''
        result = self._values.get("method")
        assert result is not None, "Required property 'method' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#source CeCostCategory#source}.'''
        result = self._values.get("source")
        assert result is not None, "Required property 'source' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def targets(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#targets CeCostCategory#targets}.'''
        result = self._values.get("targets")
        assert result is not None, "Required property 'targets' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def parameter(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CeCostCategorySplitChargeRuleParameter"]]]:
        '''parameter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#parameter CeCostCategory#parameter}
        '''
        result = self._values.get("parameter")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CeCostCategorySplitChargeRuleParameter"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CeCostCategorySplitChargeRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CeCostCategorySplitChargeRuleList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ceCostCategory.CeCostCategorySplitChargeRuleList",
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
    def get(self, index: jsii.Number) -> "CeCostCategorySplitChargeRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CeCostCategorySplitChargeRuleOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CeCostCategorySplitChargeRule]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CeCostCategorySplitChargeRule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CeCostCategorySplitChargeRule]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CeCostCategorySplitChargeRule]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CeCostCategorySplitChargeRuleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ceCostCategory.CeCostCategorySplitChargeRuleOutputReference",
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

    @jsii.member(jsii_name="putParameter")
    def put_parameter(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CeCostCategorySplitChargeRuleParameter", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CeCostCategorySplitChargeRuleParameter, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putParameter", [value]))

    @jsii.member(jsii_name="resetParameter")
    def reset_parameter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameter", []))

    @builtins.property
    @jsii.member(jsii_name="parameter")
    def parameter(self) -> "CeCostCategorySplitChargeRuleParameterList":
        return typing.cast("CeCostCategorySplitChargeRuleParameterList", jsii.get(self, "parameter"))

    @builtins.property
    @jsii.member(jsii_name="methodInput")
    def method_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "methodInput"))

    @builtins.property
    @jsii.member(jsii_name="parameterInput")
    def parameter_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CeCostCategorySplitChargeRuleParameter"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CeCostCategorySplitChargeRuleParameter"]]], jsii.get(self, "parameterInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceInput")
    def source_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceInput"))

    @builtins.property
    @jsii.member(jsii_name="targetsInput")
    def targets_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "targetsInput"))

    @builtins.property
    @jsii.member(jsii_name="method")
    def method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "method"))

    @method.setter
    def method(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "method", value)

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "source"))

    @source.setter
    def source(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "source", value)

    @builtins.property
    @jsii.member(jsii_name="targets")
    def targets(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "targets"))

    @targets.setter
    def targets(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targets", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CeCostCategorySplitChargeRule, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CeCostCategorySplitChargeRule, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CeCostCategorySplitChargeRule, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[CeCostCategorySplitChargeRule, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ceCostCategory.CeCostCategorySplitChargeRuleParameter",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "values": "values"},
)
class CeCostCategorySplitChargeRuleParameter:
    def __init__(
        self,
        *,
        type: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#type CeCostCategory#type}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.
        '''
        if __debug__:
            def stub(
                *,
                type: typing.Optional[builtins.str] = None,
                values: typing.Optional[typing.Sequence[builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {}
        if type is not None:
            self._values["type"] = type
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#type CeCostCategory#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ce_cost_category#values CeCostCategory#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CeCostCategorySplitChargeRuleParameter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CeCostCategorySplitChargeRuleParameterList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ceCostCategory.CeCostCategorySplitChargeRuleParameterList",
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
    ) -> "CeCostCategorySplitChargeRuleParameterOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CeCostCategorySplitChargeRuleParameterOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CeCostCategorySplitChargeRuleParameter]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CeCostCategorySplitChargeRuleParameter]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CeCostCategorySplitChargeRuleParameter]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CeCostCategorySplitChargeRuleParameter]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CeCostCategorySplitChargeRuleParameterOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ceCostCategory.CeCostCategorySplitChargeRuleParameterOutputReference",
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

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

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
    ) -> typing.Optional[typing.Union[CeCostCategorySplitChargeRuleParameter, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CeCostCategorySplitChargeRuleParameter, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CeCostCategorySplitChargeRuleParameter, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[CeCostCategorySplitChargeRuleParameter, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "CeCostCategory",
    "CeCostCategoryConfig",
    "CeCostCategoryRule",
    "CeCostCategoryRuleInheritedValue",
    "CeCostCategoryRuleInheritedValueOutputReference",
    "CeCostCategoryRuleList",
    "CeCostCategoryRuleOutputReference",
    "CeCostCategoryRuleRule",
    "CeCostCategoryRuleRuleAnd",
    "CeCostCategoryRuleRuleAndCostCategory",
    "CeCostCategoryRuleRuleAndCostCategoryOutputReference",
    "CeCostCategoryRuleRuleAndDimension",
    "CeCostCategoryRuleRuleAndDimensionOutputReference",
    "CeCostCategoryRuleRuleAndList",
    "CeCostCategoryRuleRuleAndOutputReference",
    "CeCostCategoryRuleRuleAndTags",
    "CeCostCategoryRuleRuleAndTagsOutputReference",
    "CeCostCategoryRuleRuleCostCategory",
    "CeCostCategoryRuleRuleCostCategoryOutputReference",
    "CeCostCategoryRuleRuleDimension",
    "CeCostCategoryRuleRuleDimensionOutputReference",
    "CeCostCategoryRuleRuleNot",
    "CeCostCategoryRuleRuleNotCostCategory",
    "CeCostCategoryRuleRuleNotCostCategoryOutputReference",
    "CeCostCategoryRuleRuleNotDimension",
    "CeCostCategoryRuleRuleNotDimensionOutputReference",
    "CeCostCategoryRuleRuleNotOutputReference",
    "CeCostCategoryRuleRuleNotTags",
    "CeCostCategoryRuleRuleNotTagsOutputReference",
    "CeCostCategoryRuleRuleOr",
    "CeCostCategoryRuleRuleOrCostCategory",
    "CeCostCategoryRuleRuleOrCostCategoryOutputReference",
    "CeCostCategoryRuleRuleOrDimension",
    "CeCostCategoryRuleRuleOrDimensionOutputReference",
    "CeCostCategoryRuleRuleOrList",
    "CeCostCategoryRuleRuleOrOutputReference",
    "CeCostCategoryRuleRuleOrTags",
    "CeCostCategoryRuleRuleOrTagsOutputReference",
    "CeCostCategoryRuleRuleOutputReference",
    "CeCostCategoryRuleRuleTags",
    "CeCostCategoryRuleRuleTagsOutputReference",
    "CeCostCategorySplitChargeRule",
    "CeCostCategorySplitChargeRuleList",
    "CeCostCategorySplitChargeRuleOutputReference",
    "CeCostCategorySplitChargeRuleParameter",
    "CeCostCategorySplitChargeRuleParameterList",
    "CeCostCategorySplitChargeRuleParameterOutputReference",
]

publication.publish()
