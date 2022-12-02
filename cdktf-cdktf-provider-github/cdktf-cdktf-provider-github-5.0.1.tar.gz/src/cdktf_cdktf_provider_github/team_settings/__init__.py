'''
# `github_team_settings`

Refer to the Terraform Registory for docs: [`github_team_settings`](https://www.terraform.io/docs/providers/github/r/team_settings).
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


class TeamSettings(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-github.teamSettings.TeamSettings",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/github/r/team_settings github_team_settings}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        team_id: builtins.str,
        id: typing.Optional[builtins.str] = None,
        review_request_delegation: typing.Optional[typing.Union["TeamSettingsReviewRequestDelegation", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/github/r/team_settings github_team_settings} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param team_id: ID or slug of team. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/team_settings#team_id TeamSettings#team_id}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/team_settings#id TeamSettings#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param review_request_delegation: review_request_delegation block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/team_settings#review_request_delegation TeamSettings#review_request_delegation}
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
                team_id: builtins.str,
                id: typing.Optional[builtins.str] = None,
                review_request_delegation: typing.Optional[typing.Union[TeamSettingsReviewRequestDelegation, typing.Dict[str, typing.Any]]] = None,
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
        config = TeamSettingsConfig(
            team_id=team_id,
            id=id,
            review_request_delegation=review_request_delegation,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putReviewRequestDelegation")
    def put_review_request_delegation(
        self,
        *,
        algorithm: typing.Optional[builtins.str] = None,
        member_count: typing.Optional[jsii.Number] = None,
        notify: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param algorithm: Algorithm to use when determining team members to be assigned to a pull request. Allowed values are ROUND_ROBIN and LOAD_BALANCE Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/team_settings#algorithm TeamSettings#algorithm}
        :param member_count: The number of reviewers to be assigned to a pull request from this team. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/team_settings#member_count TeamSettings#member_count}
        :param notify: Notify the entire team when a pull request is assigned to a member of the team. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/team_settings#notify TeamSettings#notify}
        '''
        value = TeamSettingsReviewRequestDelegation(
            algorithm=algorithm, member_count=member_count, notify=notify
        )

        return typing.cast(None, jsii.invoke(self, "putReviewRequestDelegation", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetReviewRequestDelegation")
    def reset_review_request_delegation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReviewRequestDelegation", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="reviewRequestDelegation")
    def review_request_delegation(
        self,
    ) -> "TeamSettingsReviewRequestDelegationOutputReference":
        return typing.cast("TeamSettingsReviewRequestDelegationOutputReference", jsii.get(self, "reviewRequestDelegation"))

    @builtins.property
    @jsii.member(jsii_name="teamSlug")
    def team_slug(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "teamSlug"))

    @builtins.property
    @jsii.member(jsii_name="teamUid")
    def team_uid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "teamUid"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="reviewRequestDelegationInput")
    def review_request_delegation_input(
        self,
    ) -> typing.Optional["TeamSettingsReviewRequestDelegation"]:
        return typing.cast(typing.Optional["TeamSettingsReviewRequestDelegation"], jsii.get(self, "reviewRequestDelegationInput"))

    @builtins.property
    @jsii.member(jsii_name="teamIdInput")
    def team_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "teamIdInput"))

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
    @jsii.member(jsii_name="teamId")
    def team_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "teamId"))

    @team_id.setter
    def team_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "teamId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-github.teamSettings.TeamSettingsConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "team_id": "teamId",
        "id": "id",
        "review_request_delegation": "reviewRequestDelegation",
    },
)
class TeamSettingsConfig(cdktf.TerraformMetaArguments):
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
        team_id: builtins.str,
        id: typing.Optional[builtins.str] = None,
        review_request_delegation: typing.Optional[typing.Union["TeamSettingsReviewRequestDelegation", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param team_id: ID or slug of team. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/team_settings#team_id TeamSettings#team_id}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/team_settings#id TeamSettings#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param review_request_delegation: review_request_delegation block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/team_settings#review_request_delegation TeamSettings#review_request_delegation}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(review_request_delegation, dict):
            review_request_delegation = TeamSettingsReviewRequestDelegation(**review_request_delegation)
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
                team_id: builtins.str,
                id: typing.Optional[builtins.str] = None,
                review_request_delegation: typing.Optional[typing.Union[TeamSettingsReviewRequestDelegation, typing.Dict[str, typing.Any]]] = None,
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
            check_type(argname="argument team_id", value=team_id, expected_type=type_hints["team_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument review_request_delegation", value=review_request_delegation, expected_type=type_hints["review_request_delegation"])
        self._values: typing.Dict[str, typing.Any] = {
            "team_id": team_id,
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
        if review_request_delegation is not None:
            self._values["review_request_delegation"] = review_request_delegation

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
    def team_id(self) -> builtins.str:
        '''ID or slug of team.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/team_settings#team_id TeamSettings#team_id}
        '''
        result = self._values.get("team_id")
        assert result is not None, "Required property 'team_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/team_settings#id TeamSettings#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def review_request_delegation(
        self,
    ) -> typing.Optional["TeamSettingsReviewRequestDelegation"]:
        '''review_request_delegation block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/team_settings#review_request_delegation TeamSettings#review_request_delegation}
        '''
        result = self._values.get("review_request_delegation")
        return typing.cast(typing.Optional["TeamSettingsReviewRequestDelegation"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TeamSettingsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-github.teamSettings.TeamSettingsReviewRequestDelegation",
    jsii_struct_bases=[],
    name_mapping={
        "algorithm": "algorithm",
        "member_count": "memberCount",
        "notify": "notify",
    },
)
class TeamSettingsReviewRequestDelegation:
    def __init__(
        self,
        *,
        algorithm: typing.Optional[builtins.str] = None,
        member_count: typing.Optional[jsii.Number] = None,
        notify: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param algorithm: Algorithm to use when determining team members to be assigned to a pull request. Allowed values are ROUND_ROBIN and LOAD_BALANCE Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/team_settings#algorithm TeamSettings#algorithm}
        :param member_count: The number of reviewers to be assigned to a pull request from this team. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/team_settings#member_count TeamSettings#member_count}
        :param notify: Notify the entire team when a pull request is assigned to a member of the team. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/team_settings#notify TeamSettings#notify}
        '''
        if __debug__:
            def stub(
                *,
                algorithm: typing.Optional[builtins.str] = None,
                member_count: typing.Optional[jsii.Number] = None,
                notify: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument algorithm", value=algorithm, expected_type=type_hints["algorithm"])
            check_type(argname="argument member_count", value=member_count, expected_type=type_hints["member_count"])
            check_type(argname="argument notify", value=notify, expected_type=type_hints["notify"])
        self._values: typing.Dict[str, typing.Any] = {}
        if algorithm is not None:
            self._values["algorithm"] = algorithm
        if member_count is not None:
            self._values["member_count"] = member_count
        if notify is not None:
            self._values["notify"] = notify

    @builtins.property
    def algorithm(self) -> typing.Optional[builtins.str]:
        '''Algorithm to use when determining team members to be assigned to a pull request.

        Allowed values are ROUND_ROBIN and LOAD_BALANCE

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/team_settings#algorithm TeamSettings#algorithm}
        '''
        result = self._values.get("algorithm")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def member_count(self) -> typing.Optional[jsii.Number]:
        '''The number of reviewers to be assigned to a pull request from this team.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/team_settings#member_count TeamSettings#member_count}
        '''
        result = self._values.get("member_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def notify(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Notify the entire team when a pull request is assigned to a member of the team.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/team_settings#notify TeamSettings#notify}
        '''
        result = self._values.get("notify")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TeamSettingsReviewRequestDelegation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TeamSettingsReviewRequestDelegationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-github.teamSettings.TeamSettingsReviewRequestDelegationOutputReference",
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

    @jsii.member(jsii_name="resetAlgorithm")
    def reset_algorithm(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlgorithm", []))

    @jsii.member(jsii_name="resetMemberCount")
    def reset_member_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMemberCount", []))

    @jsii.member(jsii_name="resetNotify")
    def reset_notify(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotify", []))

    @builtins.property
    @jsii.member(jsii_name="algorithmInput")
    def algorithm_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "algorithmInput"))

    @builtins.property
    @jsii.member(jsii_name="memberCountInput")
    def member_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "memberCountInput"))

    @builtins.property
    @jsii.member(jsii_name="notifyInput")
    def notify_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "notifyInput"))

    @builtins.property
    @jsii.member(jsii_name="algorithm")
    def algorithm(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "algorithm"))

    @algorithm.setter
    def algorithm(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "algorithm", value)

    @builtins.property
    @jsii.member(jsii_name="memberCount")
    def member_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "memberCount"))

    @member_count.setter
    def member_count(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memberCount", value)

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
    def internal_value(self) -> typing.Optional[TeamSettingsReviewRequestDelegation]:
        return typing.cast(typing.Optional[TeamSettingsReviewRequestDelegation], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[TeamSettingsReviewRequestDelegation],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[TeamSettingsReviewRequestDelegation],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "TeamSettings",
    "TeamSettingsConfig",
    "TeamSettingsReviewRequestDelegation",
    "TeamSettingsReviewRequestDelegationOutputReference",
]

publication.publish()
