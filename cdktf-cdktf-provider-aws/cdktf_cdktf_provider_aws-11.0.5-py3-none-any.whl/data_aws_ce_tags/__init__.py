'''
# `data_aws_ce_tags`

Refer to the Terraform Registory for docs: [`data_aws_ce_tags`](https://www.terraform.io/docs/providers/aws/d/ce_tags).
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


class DataAwsCeTags(
    cdktf.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dataAwsCeTags.DataAwsCeTags",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/d/ce_tags aws_ce_tags}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        time_period: typing.Union["DataAwsCeTagsTimePeriod", typing.Dict[str, typing.Any]],
        filter: typing.Optional[typing.Union["DataAwsCeTagsFilter", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        search_string: typing.Optional[builtins.str] = None,
        sort_by: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataAwsCeTagsSortBy", typing.Dict[str, typing.Any]]]]] = None,
        tag_key: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/d/ce_tags aws_ce_tags} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param time_period: time_period block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#time_period DataAwsCeTags#time_period}
        :param filter: filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#filter DataAwsCeTags#filter}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#id DataAwsCeTags#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param search_string: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#search_string DataAwsCeTags#search_string}.
        :param sort_by: sort_by block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#sort_by DataAwsCeTags#sort_by}
        :param tag_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#tag_key DataAwsCeTags#tag_key}.
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
                time_period: typing.Union[DataAwsCeTagsTimePeriod, typing.Dict[str, typing.Any]],
                filter: typing.Optional[typing.Union[DataAwsCeTagsFilter, typing.Dict[str, typing.Any]]] = None,
                id: typing.Optional[builtins.str] = None,
                search_string: typing.Optional[builtins.str] = None,
                sort_by: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[DataAwsCeTagsSortBy, typing.Dict[str, typing.Any]]]]] = None,
                tag_key: typing.Optional[builtins.str] = None,
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
        config = DataAwsCeTagsConfig(
            time_period=time_period,
            filter=filter,
            id=id,
            search_string=search_string,
            sort_by=sort_by,
            tag_key=tag_key,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putFilter")
    def put_filter(
        self,
        *,
        and_: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataAwsCeTagsFilterAnd", typing.Dict[str, typing.Any]]]]] = None,
        cost_category: typing.Optional[typing.Union["DataAwsCeTagsFilterCostCategory", typing.Dict[str, typing.Any]]] = None,
        dimension: typing.Optional[typing.Union["DataAwsCeTagsFilterDimension", typing.Dict[str, typing.Any]]] = None,
        not_: typing.Optional[typing.Union["DataAwsCeTagsFilterNot", typing.Dict[str, typing.Any]]] = None,
        or_: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataAwsCeTagsFilterOr", typing.Dict[str, typing.Any]]]]] = None,
        tags: typing.Optional[typing.Union["DataAwsCeTagsFilterTags", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param and_: and block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#and DataAwsCeTags#and}
        :param cost_category: cost_category block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#cost_category DataAwsCeTags#cost_category}
        :param dimension: dimension block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#dimension DataAwsCeTags#dimension}
        :param not_: not block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#not DataAwsCeTags#not}
        :param or_: or block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#or DataAwsCeTags#or}
        :param tags: tags block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#tags DataAwsCeTags#tags}
        '''
        value = DataAwsCeTagsFilter(
            and_=and_,
            cost_category=cost_category,
            dimension=dimension,
            not_=not_,
            or_=or_,
            tags=tags,
        )

        return typing.cast(None, jsii.invoke(self, "putFilter", [value]))

    @jsii.member(jsii_name="putSortBy")
    def put_sort_by(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataAwsCeTagsSortBy", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[DataAwsCeTagsSortBy, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSortBy", [value]))

    @jsii.member(jsii_name="putTimePeriod")
    def put_time_period(self, *, end: builtins.str, start: builtins.str) -> None:
        '''
        :param end: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#end DataAwsCeTags#end}.
        :param start: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#start DataAwsCeTags#start}.
        '''
        value = DataAwsCeTagsTimePeriod(end=end, start=start)

        return typing.cast(None, jsii.invoke(self, "putTimePeriod", [value]))

    @jsii.member(jsii_name="resetFilter")
    def reset_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilter", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetSearchString")
    def reset_search_string(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSearchString", []))

    @jsii.member(jsii_name="resetSortBy")
    def reset_sort_by(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSortBy", []))

    @jsii.member(jsii_name="resetTagKey")
    def reset_tag_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagKey", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="filter")
    def filter(self) -> "DataAwsCeTagsFilterOutputReference":
        return typing.cast("DataAwsCeTagsFilterOutputReference", jsii.get(self, "filter"))

    @builtins.property
    @jsii.member(jsii_name="sortBy")
    def sort_by(self) -> "DataAwsCeTagsSortByList":
        return typing.cast("DataAwsCeTagsSortByList", jsii.get(self, "sortBy"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="timePeriod")
    def time_period(self) -> "DataAwsCeTagsTimePeriodOutputReference":
        return typing.cast("DataAwsCeTagsTimePeriodOutputReference", jsii.get(self, "timePeriod"))

    @builtins.property
    @jsii.member(jsii_name="filterInput")
    def filter_input(self) -> typing.Optional["DataAwsCeTagsFilter"]:
        return typing.cast(typing.Optional["DataAwsCeTagsFilter"], jsii.get(self, "filterInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="searchStringInput")
    def search_string_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "searchStringInput"))

    @builtins.property
    @jsii.member(jsii_name="sortByInput")
    def sort_by_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataAwsCeTagsSortBy"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataAwsCeTagsSortBy"]]], jsii.get(self, "sortByInput"))

    @builtins.property
    @jsii.member(jsii_name="tagKeyInput")
    def tag_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tagKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="timePeriodInput")
    def time_period_input(self) -> typing.Optional["DataAwsCeTagsTimePeriod"]:
        return typing.cast(typing.Optional["DataAwsCeTagsTimePeriod"], jsii.get(self, "timePeriodInput"))

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
    @jsii.member(jsii_name="searchString")
    def search_string(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "searchString"))

    @search_string.setter
    def search_string(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "searchString", value)

    @builtins.property
    @jsii.member(jsii_name="tagKey")
    def tag_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tagKey"))

    @tag_key.setter
    def tag_key(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagKey", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.dataAwsCeTags.DataAwsCeTagsConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "time_period": "timePeriod",
        "filter": "filter",
        "id": "id",
        "search_string": "searchString",
        "sort_by": "sortBy",
        "tag_key": "tagKey",
    },
)
class DataAwsCeTagsConfig(cdktf.TerraformMetaArguments):
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
        time_period: typing.Union["DataAwsCeTagsTimePeriod", typing.Dict[str, typing.Any]],
        filter: typing.Optional[typing.Union["DataAwsCeTagsFilter", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        search_string: typing.Optional[builtins.str] = None,
        sort_by: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataAwsCeTagsSortBy", typing.Dict[str, typing.Any]]]]] = None,
        tag_key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param time_period: time_period block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#time_period DataAwsCeTags#time_period}
        :param filter: filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#filter DataAwsCeTags#filter}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#id DataAwsCeTags#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param search_string: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#search_string DataAwsCeTags#search_string}.
        :param sort_by: sort_by block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#sort_by DataAwsCeTags#sort_by}
        :param tag_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#tag_key DataAwsCeTags#tag_key}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(time_period, dict):
            time_period = DataAwsCeTagsTimePeriod(**time_period)
        if isinstance(filter, dict):
            filter = DataAwsCeTagsFilter(**filter)
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
                time_period: typing.Union[DataAwsCeTagsTimePeriod, typing.Dict[str, typing.Any]],
                filter: typing.Optional[typing.Union[DataAwsCeTagsFilter, typing.Dict[str, typing.Any]]] = None,
                id: typing.Optional[builtins.str] = None,
                search_string: typing.Optional[builtins.str] = None,
                sort_by: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[DataAwsCeTagsSortBy, typing.Dict[str, typing.Any]]]]] = None,
                tag_key: typing.Optional[builtins.str] = None,
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
            check_type(argname="argument time_period", value=time_period, expected_type=type_hints["time_period"])
            check_type(argname="argument filter", value=filter, expected_type=type_hints["filter"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument search_string", value=search_string, expected_type=type_hints["search_string"])
            check_type(argname="argument sort_by", value=sort_by, expected_type=type_hints["sort_by"])
            check_type(argname="argument tag_key", value=tag_key, expected_type=type_hints["tag_key"])
        self._values: typing.Dict[str, typing.Any] = {
            "time_period": time_period,
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
        if filter is not None:
            self._values["filter"] = filter
        if id is not None:
            self._values["id"] = id
        if search_string is not None:
            self._values["search_string"] = search_string
        if sort_by is not None:
            self._values["sort_by"] = sort_by
        if tag_key is not None:
            self._values["tag_key"] = tag_key

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
    def time_period(self) -> "DataAwsCeTagsTimePeriod":
        '''time_period block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#time_period DataAwsCeTags#time_period}
        '''
        result = self._values.get("time_period")
        assert result is not None, "Required property 'time_period' is missing"
        return typing.cast("DataAwsCeTagsTimePeriod", result)

    @builtins.property
    def filter(self) -> typing.Optional["DataAwsCeTagsFilter"]:
        '''filter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#filter DataAwsCeTags#filter}
        '''
        result = self._values.get("filter")
        return typing.cast(typing.Optional["DataAwsCeTagsFilter"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#id DataAwsCeTags#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def search_string(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#search_string DataAwsCeTags#search_string}.'''
        result = self._values.get("search_string")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sort_by(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataAwsCeTagsSortBy"]]]:
        '''sort_by block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#sort_by DataAwsCeTags#sort_by}
        '''
        result = self._values.get("sort_by")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataAwsCeTagsSortBy"]]], result)

    @builtins.property
    def tag_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#tag_key DataAwsCeTags#tag_key}.'''
        result = self._values.get("tag_key")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsCeTagsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.dataAwsCeTags.DataAwsCeTagsFilter",
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
class DataAwsCeTagsFilter:
    def __init__(
        self,
        *,
        and_: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataAwsCeTagsFilterAnd", typing.Dict[str, typing.Any]]]]] = None,
        cost_category: typing.Optional[typing.Union["DataAwsCeTagsFilterCostCategory", typing.Dict[str, typing.Any]]] = None,
        dimension: typing.Optional[typing.Union["DataAwsCeTagsFilterDimension", typing.Dict[str, typing.Any]]] = None,
        not_: typing.Optional[typing.Union["DataAwsCeTagsFilterNot", typing.Dict[str, typing.Any]]] = None,
        or_: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataAwsCeTagsFilterOr", typing.Dict[str, typing.Any]]]]] = None,
        tags: typing.Optional[typing.Union["DataAwsCeTagsFilterTags", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param and_: and block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#and DataAwsCeTags#and}
        :param cost_category: cost_category block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#cost_category DataAwsCeTags#cost_category}
        :param dimension: dimension block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#dimension DataAwsCeTags#dimension}
        :param not_: not block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#not DataAwsCeTags#not}
        :param or_: or block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#or DataAwsCeTags#or}
        :param tags: tags block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#tags DataAwsCeTags#tags}
        '''
        if isinstance(cost_category, dict):
            cost_category = DataAwsCeTagsFilterCostCategory(**cost_category)
        if isinstance(dimension, dict):
            dimension = DataAwsCeTagsFilterDimension(**dimension)
        if isinstance(not_, dict):
            not_ = DataAwsCeTagsFilterNot(**not_)
        if isinstance(tags, dict):
            tags = DataAwsCeTagsFilterTags(**tags)
        if __debug__:
            def stub(
                *,
                and_: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[DataAwsCeTagsFilterAnd, typing.Dict[str, typing.Any]]]]] = None,
                cost_category: typing.Optional[typing.Union[DataAwsCeTagsFilterCostCategory, typing.Dict[str, typing.Any]]] = None,
                dimension: typing.Optional[typing.Union[DataAwsCeTagsFilterDimension, typing.Dict[str, typing.Any]]] = None,
                not_: typing.Optional[typing.Union[DataAwsCeTagsFilterNot, typing.Dict[str, typing.Any]]] = None,
                or_: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[DataAwsCeTagsFilterOr, typing.Dict[str, typing.Any]]]]] = None,
                tags: typing.Optional[typing.Union[DataAwsCeTagsFilterTags, typing.Dict[str, typing.Any]]] = None,
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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataAwsCeTagsFilterAnd"]]]:
        '''and block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#and DataAwsCeTags#and}
        '''
        result = self._values.get("and_")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataAwsCeTagsFilterAnd"]]], result)

    @builtins.property
    def cost_category(self) -> typing.Optional["DataAwsCeTagsFilterCostCategory"]:
        '''cost_category block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#cost_category DataAwsCeTags#cost_category}
        '''
        result = self._values.get("cost_category")
        return typing.cast(typing.Optional["DataAwsCeTagsFilterCostCategory"], result)

    @builtins.property
    def dimension(self) -> typing.Optional["DataAwsCeTagsFilterDimension"]:
        '''dimension block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#dimension DataAwsCeTags#dimension}
        '''
        result = self._values.get("dimension")
        return typing.cast(typing.Optional["DataAwsCeTagsFilterDimension"], result)

    @builtins.property
    def not_(self) -> typing.Optional["DataAwsCeTagsFilterNot"]:
        '''not block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#not DataAwsCeTags#not}
        '''
        result = self._values.get("not_")
        return typing.cast(typing.Optional["DataAwsCeTagsFilterNot"], result)

    @builtins.property
    def or_(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataAwsCeTagsFilterOr"]]]:
        '''or block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#or DataAwsCeTags#or}
        '''
        result = self._values.get("or_")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataAwsCeTagsFilterOr"]]], result)

    @builtins.property
    def tags(self) -> typing.Optional["DataAwsCeTagsFilterTags"]:
        '''tags block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#tags DataAwsCeTags#tags}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional["DataAwsCeTagsFilterTags"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsCeTagsFilter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.dataAwsCeTags.DataAwsCeTagsFilterAnd",
    jsii_struct_bases=[],
    name_mapping={
        "cost_category": "costCategory",
        "dimension": "dimension",
        "tags": "tags",
    },
)
class DataAwsCeTagsFilterAnd:
    def __init__(
        self,
        *,
        cost_category: typing.Optional[typing.Union["DataAwsCeTagsFilterAndCostCategory", typing.Dict[str, typing.Any]]] = None,
        dimension: typing.Optional[typing.Union["DataAwsCeTagsFilterAndDimension", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Union["DataAwsCeTagsFilterAndTags", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param cost_category: cost_category block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#cost_category DataAwsCeTags#cost_category}
        :param dimension: dimension block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#dimension DataAwsCeTags#dimension}
        :param tags: tags block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#tags DataAwsCeTags#tags}
        '''
        if isinstance(cost_category, dict):
            cost_category = DataAwsCeTagsFilterAndCostCategory(**cost_category)
        if isinstance(dimension, dict):
            dimension = DataAwsCeTagsFilterAndDimension(**dimension)
        if isinstance(tags, dict):
            tags = DataAwsCeTagsFilterAndTags(**tags)
        if __debug__:
            def stub(
                *,
                cost_category: typing.Optional[typing.Union[DataAwsCeTagsFilterAndCostCategory, typing.Dict[str, typing.Any]]] = None,
                dimension: typing.Optional[typing.Union[DataAwsCeTagsFilterAndDimension, typing.Dict[str, typing.Any]]] = None,
                tags: typing.Optional[typing.Union[DataAwsCeTagsFilterAndTags, typing.Dict[str, typing.Any]]] = None,
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
    def cost_category(self) -> typing.Optional["DataAwsCeTagsFilterAndCostCategory"]:
        '''cost_category block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#cost_category DataAwsCeTags#cost_category}
        '''
        result = self._values.get("cost_category")
        return typing.cast(typing.Optional["DataAwsCeTagsFilterAndCostCategory"], result)

    @builtins.property
    def dimension(self) -> typing.Optional["DataAwsCeTagsFilterAndDimension"]:
        '''dimension block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#dimension DataAwsCeTags#dimension}
        '''
        result = self._values.get("dimension")
        return typing.cast(typing.Optional["DataAwsCeTagsFilterAndDimension"], result)

    @builtins.property
    def tags(self) -> typing.Optional["DataAwsCeTagsFilterAndTags"]:
        '''tags block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#tags DataAwsCeTags#tags}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional["DataAwsCeTagsFilterAndTags"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsCeTagsFilterAnd(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.dataAwsCeTags.DataAwsCeTagsFilterAndCostCategory",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "match_options": "matchOptions", "values": "values"},
)
class DataAwsCeTagsFilterAndCostCategory:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.'''
        result = self._values.get("match_options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsCeTagsFilterAndCostCategory(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsCeTagsFilterAndCostCategoryOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dataAwsCeTags.DataAwsCeTagsFilterAndCostCategoryOutputReference",
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
    def internal_value(self) -> typing.Optional[DataAwsCeTagsFilterAndCostCategory]:
        return typing.cast(typing.Optional[DataAwsCeTagsFilterAndCostCategory], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAwsCeTagsFilterAndCostCategory],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[DataAwsCeTagsFilterAndCostCategory],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.dataAwsCeTags.DataAwsCeTagsFilterAndDimension",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "match_options": "matchOptions", "values": "values"},
)
class DataAwsCeTagsFilterAndDimension:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.'''
        result = self._values.get("match_options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsCeTagsFilterAndDimension(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsCeTagsFilterAndDimensionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dataAwsCeTags.DataAwsCeTagsFilterAndDimensionOutputReference",
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
    def internal_value(self) -> typing.Optional[DataAwsCeTagsFilterAndDimension]:
        return typing.cast(typing.Optional[DataAwsCeTagsFilterAndDimension], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAwsCeTagsFilterAndDimension],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[DataAwsCeTagsFilterAndDimension]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAwsCeTagsFilterAndList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dataAwsCeTags.DataAwsCeTagsFilterAndList",
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
    def get(self, index: jsii.Number) -> "DataAwsCeTagsFilterAndOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAwsCeTagsFilterAndOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataAwsCeTagsFilterAnd]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataAwsCeTagsFilterAnd]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataAwsCeTagsFilterAnd]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataAwsCeTagsFilterAnd]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAwsCeTagsFilterAndOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dataAwsCeTags.DataAwsCeTagsFilterAndOutputReference",
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
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.
        '''
        value = DataAwsCeTagsFilterAndCostCategory(
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
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.
        '''
        value = DataAwsCeTagsFilterAndDimension(
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
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.
        '''
        value = DataAwsCeTagsFilterAndTags(
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
    def cost_category(self) -> DataAwsCeTagsFilterAndCostCategoryOutputReference:
        return typing.cast(DataAwsCeTagsFilterAndCostCategoryOutputReference, jsii.get(self, "costCategory"))

    @builtins.property
    @jsii.member(jsii_name="dimension")
    def dimension(self) -> DataAwsCeTagsFilterAndDimensionOutputReference:
        return typing.cast(DataAwsCeTagsFilterAndDimensionOutputReference, jsii.get(self, "dimension"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> "DataAwsCeTagsFilterAndTagsOutputReference":
        return typing.cast("DataAwsCeTagsFilterAndTagsOutputReference", jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="costCategoryInput")
    def cost_category_input(
        self,
    ) -> typing.Optional[DataAwsCeTagsFilterAndCostCategory]:
        return typing.cast(typing.Optional[DataAwsCeTagsFilterAndCostCategory], jsii.get(self, "costCategoryInput"))

    @builtins.property
    @jsii.member(jsii_name="dimensionInput")
    def dimension_input(self) -> typing.Optional[DataAwsCeTagsFilterAndDimension]:
        return typing.cast(typing.Optional[DataAwsCeTagsFilterAndDimension], jsii.get(self, "dimensionInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional["DataAwsCeTagsFilterAndTags"]:
        return typing.cast(typing.Optional["DataAwsCeTagsFilterAndTags"], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataAwsCeTagsFilterAnd, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataAwsCeTagsFilterAnd, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataAwsCeTagsFilterAnd, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[DataAwsCeTagsFilterAnd, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.dataAwsCeTags.DataAwsCeTagsFilterAndTags",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "match_options": "matchOptions", "values": "values"},
)
class DataAwsCeTagsFilterAndTags:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.'''
        result = self._values.get("match_options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsCeTagsFilterAndTags(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsCeTagsFilterAndTagsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dataAwsCeTags.DataAwsCeTagsFilterAndTagsOutputReference",
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
    def internal_value(self) -> typing.Optional[DataAwsCeTagsFilterAndTags]:
        return typing.cast(typing.Optional[DataAwsCeTagsFilterAndTags], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAwsCeTagsFilterAndTags],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[DataAwsCeTagsFilterAndTags]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.dataAwsCeTags.DataAwsCeTagsFilterCostCategory",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "match_options": "matchOptions", "values": "values"},
)
class DataAwsCeTagsFilterCostCategory:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.'''
        result = self._values.get("match_options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsCeTagsFilterCostCategory(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsCeTagsFilterCostCategoryOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dataAwsCeTags.DataAwsCeTagsFilterCostCategoryOutputReference",
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
    def internal_value(self) -> typing.Optional[DataAwsCeTagsFilterCostCategory]:
        return typing.cast(typing.Optional[DataAwsCeTagsFilterCostCategory], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAwsCeTagsFilterCostCategory],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[DataAwsCeTagsFilterCostCategory]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.dataAwsCeTags.DataAwsCeTagsFilterDimension",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "match_options": "matchOptions", "values": "values"},
)
class DataAwsCeTagsFilterDimension:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.'''
        result = self._values.get("match_options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsCeTagsFilterDimension(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsCeTagsFilterDimensionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dataAwsCeTags.DataAwsCeTagsFilterDimensionOutputReference",
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
    def internal_value(self) -> typing.Optional[DataAwsCeTagsFilterDimension]:
        return typing.cast(typing.Optional[DataAwsCeTagsFilterDimension], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAwsCeTagsFilterDimension],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[DataAwsCeTagsFilterDimension]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.dataAwsCeTags.DataAwsCeTagsFilterNot",
    jsii_struct_bases=[],
    name_mapping={
        "cost_category": "costCategory",
        "dimension": "dimension",
        "tags": "tags",
    },
)
class DataAwsCeTagsFilterNot:
    def __init__(
        self,
        *,
        cost_category: typing.Optional[typing.Union["DataAwsCeTagsFilterNotCostCategory", typing.Dict[str, typing.Any]]] = None,
        dimension: typing.Optional[typing.Union["DataAwsCeTagsFilterNotDimension", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Union["DataAwsCeTagsFilterNotTags", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param cost_category: cost_category block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#cost_category DataAwsCeTags#cost_category}
        :param dimension: dimension block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#dimension DataAwsCeTags#dimension}
        :param tags: tags block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#tags DataAwsCeTags#tags}
        '''
        if isinstance(cost_category, dict):
            cost_category = DataAwsCeTagsFilterNotCostCategory(**cost_category)
        if isinstance(dimension, dict):
            dimension = DataAwsCeTagsFilterNotDimension(**dimension)
        if isinstance(tags, dict):
            tags = DataAwsCeTagsFilterNotTags(**tags)
        if __debug__:
            def stub(
                *,
                cost_category: typing.Optional[typing.Union[DataAwsCeTagsFilterNotCostCategory, typing.Dict[str, typing.Any]]] = None,
                dimension: typing.Optional[typing.Union[DataAwsCeTagsFilterNotDimension, typing.Dict[str, typing.Any]]] = None,
                tags: typing.Optional[typing.Union[DataAwsCeTagsFilterNotTags, typing.Dict[str, typing.Any]]] = None,
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
    def cost_category(self) -> typing.Optional["DataAwsCeTagsFilterNotCostCategory"]:
        '''cost_category block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#cost_category DataAwsCeTags#cost_category}
        '''
        result = self._values.get("cost_category")
        return typing.cast(typing.Optional["DataAwsCeTagsFilterNotCostCategory"], result)

    @builtins.property
    def dimension(self) -> typing.Optional["DataAwsCeTagsFilterNotDimension"]:
        '''dimension block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#dimension DataAwsCeTags#dimension}
        '''
        result = self._values.get("dimension")
        return typing.cast(typing.Optional["DataAwsCeTagsFilterNotDimension"], result)

    @builtins.property
    def tags(self) -> typing.Optional["DataAwsCeTagsFilterNotTags"]:
        '''tags block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#tags DataAwsCeTags#tags}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional["DataAwsCeTagsFilterNotTags"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsCeTagsFilterNot(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.dataAwsCeTags.DataAwsCeTagsFilterNotCostCategory",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "match_options": "matchOptions", "values": "values"},
)
class DataAwsCeTagsFilterNotCostCategory:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.'''
        result = self._values.get("match_options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsCeTagsFilterNotCostCategory(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsCeTagsFilterNotCostCategoryOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dataAwsCeTags.DataAwsCeTagsFilterNotCostCategoryOutputReference",
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
    def internal_value(self) -> typing.Optional[DataAwsCeTagsFilterNotCostCategory]:
        return typing.cast(typing.Optional[DataAwsCeTagsFilterNotCostCategory], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAwsCeTagsFilterNotCostCategory],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[DataAwsCeTagsFilterNotCostCategory],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.dataAwsCeTags.DataAwsCeTagsFilterNotDimension",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "match_options": "matchOptions", "values": "values"},
)
class DataAwsCeTagsFilterNotDimension:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.'''
        result = self._values.get("match_options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsCeTagsFilterNotDimension(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsCeTagsFilterNotDimensionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dataAwsCeTags.DataAwsCeTagsFilterNotDimensionOutputReference",
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
    def internal_value(self) -> typing.Optional[DataAwsCeTagsFilterNotDimension]:
        return typing.cast(typing.Optional[DataAwsCeTagsFilterNotDimension], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAwsCeTagsFilterNotDimension],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[DataAwsCeTagsFilterNotDimension]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAwsCeTagsFilterNotOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dataAwsCeTags.DataAwsCeTagsFilterNotOutputReference",
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
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.
        '''
        value = DataAwsCeTagsFilterNotCostCategory(
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
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.
        '''
        value = DataAwsCeTagsFilterNotDimension(
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
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.
        '''
        value = DataAwsCeTagsFilterNotTags(
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
    def cost_category(self) -> DataAwsCeTagsFilterNotCostCategoryOutputReference:
        return typing.cast(DataAwsCeTagsFilterNotCostCategoryOutputReference, jsii.get(self, "costCategory"))

    @builtins.property
    @jsii.member(jsii_name="dimension")
    def dimension(self) -> DataAwsCeTagsFilterNotDimensionOutputReference:
        return typing.cast(DataAwsCeTagsFilterNotDimensionOutputReference, jsii.get(self, "dimension"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> "DataAwsCeTagsFilterNotTagsOutputReference":
        return typing.cast("DataAwsCeTagsFilterNotTagsOutputReference", jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="costCategoryInput")
    def cost_category_input(
        self,
    ) -> typing.Optional[DataAwsCeTagsFilterNotCostCategory]:
        return typing.cast(typing.Optional[DataAwsCeTagsFilterNotCostCategory], jsii.get(self, "costCategoryInput"))

    @builtins.property
    @jsii.member(jsii_name="dimensionInput")
    def dimension_input(self) -> typing.Optional[DataAwsCeTagsFilterNotDimension]:
        return typing.cast(typing.Optional[DataAwsCeTagsFilterNotDimension], jsii.get(self, "dimensionInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional["DataAwsCeTagsFilterNotTags"]:
        return typing.cast(typing.Optional["DataAwsCeTagsFilterNotTags"], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataAwsCeTagsFilterNot]:
        return typing.cast(typing.Optional[DataAwsCeTagsFilterNot], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[DataAwsCeTagsFilterNot]) -> None:
        if __debug__:
            def stub(value: typing.Optional[DataAwsCeTagsFilterNot]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.dataAwsCeTags.DataAwsCeTagsFilterNotTags",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "match_options": "matchOptions", "values": "values"},
)
class DataAwsCeTagsFilterNotTags:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.'''
        result = self._values.get("match_options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsCeTagsFilterNotTags(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsCeTagsFilterNotTagsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dataAwsCeTags.DataAwsCeTagsFilterNotTagsOutputReference",
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
    def internal_value(self) -> typing.Optional[DataAwsCeTagsFilterNotTags]:
        return typing.cast(typing.Optional[DataAwsCeTagsFilterNotTags], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAwsCeTagsFilterNotTags],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[DataAwsCeTagsFilterNotTags]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.dataAwsCeTags.DataAwsCeTagsFilterOr",
    jsii_struct_bases=[],
    name_mapping={
        "cost_category": "costCategory",
        "dimension": "dimension",
        "tags": "tags",
    },
)
class DataAwsCeTagsFilterOr:
    def __init__(
        self,
        *,
        cost_category: typing.Optional[typing.Union["DataAwsCeTagsFilterOrCostCategory", typing.Dict[str, typing.Any]]] = None,
        dimension: typing.Optional[typing.Union["DataAwsCeTagsFilterOrDimension", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Union["DataAwsCeTagsFilterOrTags", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param cost_category: cost_category block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#cost_category DataAwsCeTags#cost_category}
        :param dimension: dimension block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#dimension DataAwsCeTags#dimension}
        :param tags: tags block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#tags DataAwsCeTags#tags}
        '''
        if isinstance(cost_category, dict):
            cost_category = DataAwsCeTagsFilterOrCostCategory(**cost_category)
        if isinstance(dimension, dict):
            dimension = DataAwsCeTagsFilterOrDimension(**dimension)
        if isinstance(tags, dict):
            tags = DataAwsCeTagsFilterOrTags(**tags)
        if __debug__:
            def stub(
                *,
                cost_category: typing.Optional[typing.Union[DataAwsCeTagsFilterOrCostCategory, typing.Dict[str, typing.Any]]] = None,
                dimension: typing.Optional[typing.Union[DataAwsCeTagsFilterOrDimension, typing.Dict[str, typing.Any]]] = None,
                tags: typing.Optional[typing.Union[DataAwsCeTagsFilterOrTags, typing.Dict[str, typing.Any]]] = None,
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
    def cost_category(self) -> typing.Optional["DataAwsCeTagsFilterOrCostCategory"]:
        '''cost_category block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#cost_category DataAwsCeTags#cost_category}
        '''
        result = self._values.get("cost_category")
        return typing.cast(typing.Optional["DataAwsCeTagsFilterOrCostCategory"], result)

    @builtins.property
    def dimension(self) -> typing.Optional["DataAwsCeTagsFilterOrDimension"]:
        '''dimension block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#dimension DataAwsCeTags#dimension}
        '''
        result = self._values.get("dimension")
        return typing.cast(typing.Optional["DataAwsCeTagsFilterOrDimension"], result)

    @builtins.property
    def tags(self) -> typing.Optional["DataAwsCeTagsFilterOrTags"]:
        '''tags block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#tags DataAwsCeTags#tags}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional["DataAwsCeTagsFilterOrTags"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsCeTagsFilterOr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.dataAwsCeTags.DataAwsCeTagsFilterOrCostCategory",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "match_options": "matchOptions", "values": "values"},
)
class DataAwsCeTagsFilterOrCostCategory:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.'''
        result = self._values.get("match_options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsCeTagsFilterOrCostCategory(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsCeTagsFilterOrCostCategoryOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dataAwsCeTags.DataAwsCeTagsFilterOrCostCategoryOutputReference",
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
    def internal_value(self) -> typing.Optional[DataAwsCeTagsFilterOrCostCategory]:
        return typing.cast(typing.Optional[DataAwsCeTagsFilterOrCostCategory], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAwsCeTagsFilterOrCostCategory],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[DataAwsCeTagsFilterOrCostCategory]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.dataAwsCeTags.DataAwsCeTagsFilterOrDimension",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "match_options": "matchOptions", "values": "values"},
)
class DataAwsCeTagsFilterOrDimension:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.'''
        result = self._values.get("match_options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsCeTagsFilterOrDimension(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsCeTagsFilterOrDimensionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dataAwsCeTags.DataAwsCeTagsFilterOrDimensionOutputReference",
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
    def internal_value(self) -> typing.Optional[DataAwsCeTagsFilterOrDimension]:
        return typing.cast(typing.Optional[DataAwsCeTagsFilterOrDimension], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAwsCeTagsFilterOrDimension],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[DataAwsCeTagsFilterOrDimension]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAwsCeTagsFilterOrList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dataAwsCeTags.DataAwsCeTagsFilterOrList",
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
    def get(self, index: jsii.Number) -> "DataAwsCeTagsFilterOrOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAwsCeTagsFilterOrOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataAwsCeTagsFilterOr]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataAwsCeTagsFilterOr]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataAwsCeTagsFilterOr]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataAwsCeTagsFilterOr]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAwsCeTagsFilterOrOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dataAwsCeTags.DataAwsCeTagsFilterOrOutputReference",
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
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.
        '''
        value = DataAwsCeTagsFilterOrCostCategory(
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
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.
        '''
        value = DataAwsCeTagsFilterOrDimension(
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
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.
        '''
        value = DataAwsCeTagsFilterOrTags(
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
    def cost_category(self) -> DataAwsCeTagsFilterOrCostCategoryOutputReference:
        return typing.cast(DataAwsCeTagsFilterOrCostCategoryOutputReference, jsii.get(self, "costCategory"))

    @builtins.property
    @jsii.member(jsii_name="dimension")
    def dimension(self) -> DataAwsCeTagsFilterOrDimensionOutputReference:
        return typing.cast(DataAwsCeTagsFilterOrDimensionOutputReference, jsii.get(self, "dimension"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> "DataAwsCeTagsFilterOrTagsOutputReference":
        return typing.cast("DataAwsCeTagsFilterOrTagsOutputReference", jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="costCategoryInput")
    def cost_category_input(self) -> typing.Optional[DataAwsCeTagsFilterOrCostCategory]:
        return typing.cast(typing.Optional[DataAwsCeTagsFilterOrCostCategory], jsii.get(self, "costCategoryInput"))

    @builtins.property
    @jsii.member(jsii_name="dimensionInput")
    def dimension_input(self) -> typing.Optional[DataAwsCeTagsFilterOrDimension]:
        return typing.cast(typing.Optional[DataAwsCeTagsFilterOrDimension], jsii.get(self, "dimensionInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional["DataAwsCeTagsFilterOrTags"]:
        return typing.cast(typing.Optional["DataAwsCeTagsFilterOrTags"], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataAwsCeTagsFilterOr, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataAwsCeTagsFilterOr, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataAwsCeTagsFilterOr, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[DataAwsCeTagsFilterOr, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.dataAwsCeTags.DataAwsCeTagsFilterOrTags",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "match_options": "matchOptions", "values": "values"},
)
class DataAwsCeTagsFilterOrTags:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.'''
        result = self._values.get("match_options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsCeTagsFilterOrTags(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsCeTagsFilterOrTagsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dataAwsCeTags.DataAwsCeTagsFilterOrTagsOutputReference",
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
    def internal_value(self) -> typing.Optional[DataAwsCeTagsFilterOrTags]:
        return typing.cast(typing.Optional[DataAwsCeTagsFilterOrTags], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[DataAwsCeTagsFilterOrTags]) -> None:
        if __debug__:
            def stub(value: typing.Optional[DataAwsCeTagsFilterOrTags]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAwsCeTagsFilterOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dataAwsCeTags.DataAwsCeTagsFilterOutputReference",
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
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[DataAwsCeTagsFilterAnd, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[DataAwsCeTagsFilterAnd, typing.Dict[str, typing.Any]]]],
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
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.
        '''
        value = DataAwsCeTagsFilterCostCategory(
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
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.
        '''
        value = DataAwsCeTagsFilterDimension(
            key=key, match_options=match_options, values=values
        )

        return typing.cast(None, jsii.invoke(self, "putDimension", [value]))

    @jsii.member(jsii_name="putNot")
    def put_not(
        self,
        *,
        cost_category: typing.Optional[typing.Union[DataAwsCeTagsFilterNotCostCategory, typing.Dict[str, typing.Any]]] = None,
        dimension: typing.Optional[typing.Union[DataAwsCeTagsFilterNotDimension, typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Union[DataAwsCeTagsFilterNotTags, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param cost_category: cost_category block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#cost_category DataAwsCeTags#cost_category}
        :param dimension: dimension block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#dimension DataAwsCeTags#dimension}
        :param tags: tags block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#tags DataAwsCeTags#tags}
        '''
        value = DataAwsCeTagsFilterNot(
            cost_category=cost_category, dimension=dimension, tags=tags
        )

        return typing.cast(None, jsii.invoke(self, "putNot", [value]))

    @jsii.member(jsii_name="putOr")
    def put_or(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[DataAwsCeTagsFilterOr, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[DataAwsCeTagsFilterOr, typing.Dict[str, typing.Any]]]],
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
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.
        '''
        value = DataAwsCeTagsFilterTags(
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
    def and_(self) -> DataAwsCeTagsFilterAndList:
        return typing.cast(DataAwsCeTagsFilterAndList, jsii.get(self, "and"))

    @builtins.property
    @jsii.member(jsii_name="costCategory")
    def cost_category(self) -> DataAwsCeTagsFilterCostCategoryOutputReference:
        return typing.cast(DataAwsCeTagsFilterCostCategoryOutputReference, jsii.get(self, "costCategory"))

    @builtins.property
    @jsii.member(jsii_name="dimension")
    def dimension(self) -> DataAwsCeTagsFilterDimensionOutputReference:
        return typing.cast(DataAwsCeTagsFilterDimensionOutputReference, jsii.get(self, "dimension"))

    @builtins.property
    @jsii.member(jsii_name="not")
    def not_(self) -> DataAwsCeTagsFilterNotOutputReference:
        return typing.cast(DataAwsCeTagsFilterNotOutputReference, jsii.get(self, "not"))

    @builtins.property
    @jsii.member(jsii_name="or")
    def or_(self) -> DataAwsCeTagsFilterOrList:
        return typing.cast(DataAwsCeTagsFilterOrList, jsii.get(self, "or"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> "DataAwsCeTagsFilterTagsOutputReference":
        return typing.cast("DataAwsCeTagsFilterTagsOutputReference", jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="andInput")
    def and_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataAwsCeTagsFilterAnd]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataAwsCeTagsFilterAnd]]], jsii.get(self, "andInput"))

    @builtins.property
    @jsii.member(jsii_name="costCategoryInput")
    def cost_category_input(self) -> typing.Optional[DataAwsCeTagsFilterCostCategory]:
        return typing.cast(typing.Optional[DataAwsCeTagsFilterCostCategory], jsii.get(self, "costCategoryInput"))

    @builtins.property
    @jsii.member(jsii_name="dimensionInput")
    def dimension_input(self) -> typing.Optional[DataAwsCeTagsFilterDimension]:
        return typing.cast(typing.Optional[DataAwsCeTagsFilterDimension], jsii.get(self, "dimensionInput"))

    @builtins.property
    @jsii.member(jsii_name="notInput")
    def not_input(self) -> typing.Optional[DataAwsCeTagsFilterNot]:
        return typing.cast(typing.Optional[DataAwsCeTagsFilterNot], jsii.get(self, "notInput"))

    @builtins.property
    @jsii.member(jsii_name="orInput")
    def or_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataAwsCeTagsFilterOr]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataAwsCeTagsFilterOr]]], jsii.get(self, "orInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional["DataAwsCeTagsFilterTags"]:
        return typing.cast(typing.Optional["DataAwsCeTagsFilterTags"], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataAwsCeTagsFilter]:
        return typing.cast(typing.Optional[DataAwsCeTagsFilter], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[DataAwsCeTagsFilter]) -> None:
        if __debug__:
            def stub(value: typing.Optional[DataAwsCeTagsFilter]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.dataAwsCeTags.DataAwsCeTagsFilterTags",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "match_options": "matchOptions", "values": "values"},
)
class DataAwsCeTagsFilterTags:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        match_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.
        :param match_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#match_options DataAwsCeTags#match_options}.'''
        result = self._values.get("match_options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#values DataAwsCeTags#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsCeTagsFilterTags(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsCeTagsFilterTagsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dataAwsCeTags.DataAwsCeTagsFilterTagsOutputReference",
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
    def internal_value(self) -> typing.Optional[DataAwsCeTagsFilterTags]:
        return typing.cast(typing.Optional[DataAwsCeTagsFilterTags], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[DataAwsCeTagsFilterTags]) -> None:
        if __debug__:
            def stub(value: typing.Optional[DataAwsCeTagsFilterTags]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.dataAwsCeTags.DataAwsCeTagsSortBy",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "sort_order": "sortOrder"},
)
class DataAwsCeTagsSortBy:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        sort_order: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.
        :param sort_order: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#sort_order DataAwsCeTags#sort_order}.
        '''
        if __debug__:
            def stub(
                *,
                key: typing.Optional[builtins.str] = None,
                sort_order: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument sort_order", value=sort_order, expected_type=type_hints["sort_order"])
        self._values: typing.Dict[str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if sort_order is not None:
            self._values["sort_order"] = sort_order

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#key DataAwsCeTags#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sort_order(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#sort_order DataAwsCeTags#sort_order}.'''
        result = self._values.get("sort_order")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsCeTagsSortBy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsCeTagsSortByList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dataAwsCeTags.DataAwsCeTagsSortByList",
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
    def get(self, index: jsii.Number) -> "DataAwsCeTagsSortByOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAwsCeTagsSortByOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataAwsCeTagsSortBy]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataAwsCeTagsSortBy]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataAwsCeTagsSortBy]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataAwsCeTagsSortBy]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAwsCeTagsSortByOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dataAwsCeTags.DataAwsCeTagsSortByOutputReference",
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

    @jsii.member(jsii_name="resetSortOrder")
    def reset_sort_order(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSortOrder", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="sortOrderInput")
    def sort_order_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sortOrderInput"))

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
    @jsii.member(jsii_name="sortOrder")
    def sort_order(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sortOrder"))

    @sort_order.setter
    def sort_order(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sortOrder", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataAwsCeTagsSortBy, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataAwsCeTagsSortBy, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataAwsCeTagsSortBy, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[DataAwsCeTagsSortBy, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.dataAwsCeTags.DataAwsCeTagsTimePeriod",
    jsii_struct_bases=[],
    name_mapping={"end": "end", "start": "start"},
)
class DataAwsCeTagsTimePeriod:
    def __init__(self, *, end: builtins.str, start: builtins.str) -> None:
        '''
        :param end: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#end DataAwsCeTags#end}.
        :param start: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#start DataAwsCeTags#start}.
        '''
        if __debug__:
            def stub(*, end: builtins.str, start: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument end", value=end, expected_type=type_hints["end"])
            check_type(argname="argument start", value=start, expected_type=type_hints["start"])
        self._values: typing.Dict[str, typing.Any] = {
            "end": end,
            "start": start,
        }

    @builtins.property
    def end(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#end DataAwsCeTags#end}.'''
        result = self._values.get("end")
        assert result is not None, "Required property 'end' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def start(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/ce_tags#start DataAwsCeTags#start}.'''
        result = self._values.get("start")
        assert result is not None, "Required property 'start' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsCeTagsTimePeriod(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsCeTagsTimePeriodOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dataAwsCeTags.DataAwsCeTagsTimePeriodOutputReference",
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
    @jsii.member(jsii_name="endInput")
    def end_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endInput"))

    @builtins.property
    @jsii.member(jsii_name="startInput")
    def start_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "startInput"))

    @builtins.property
    @jsii.member(jsii_name="end")
    def end(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "end"))

    @end.setter
    def end(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "end", value)

    @builtins.property
    @jsii.member(jsii_name="start")
    def start(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "start"))

    @start.setter
    def start(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "start", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataAwsCeTagsTimePeriod]:
        return typing.cast(typing.Optional[DataAwsCeTagsTimePeriod], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[DataAwsCeTagsTimePeriod]) -> None:
        if __debug__:
            def stub(value: typing.Optional[DataAwsCeTagsTimePeriod]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DataAwsCeTags",
    "DataAwsCeTagsConfig",
    "DataAwsCeTagsFilter",
    "DataAwsCeTagsFilterAnd",
    "DataAwsCeTagsFilterAndCostCategory",
    "DataAwsCeTagsFilterAndCostCategoryOutputReference",
    "DataAwsCeTagsFilterAndDimension",
    "DataAwsCeTagsFilterAndDimensionOutputReference",
    "DataAwsCeTagsFilterAndList",
    "DataAwsCeTagsFilterAndOutputReference",
    "DataAwsCeTagsFilterAndTags",
    "DataAwsCeTagsFilterAndTagsOutputReference",
    "DataAwsCeTagsFilterCostCategory",
    "DataAwsCeTagsFilterCostCategoryOutputReference",
    "DataAwsCeTagsFilterDimension",
    "DataAwsCeTagsFilterDimensionOutputReference",
    "DataAwsCeTagsFilterNot",
    "DataAwsCeTagsFilterNotCostCategory",
    "DataAwsCeTagsFilterNotCostCategoryOutputReference",
    "DataAwsCeTagsFilterNotDimension",
    "DataAwsCeTagsFilterNotDimensionOutputReference",
    "DataAwsCeTagsFilterNotOutputReference",
    "DataAwsCeTagsFilterNotTags",
    "DataAwsCeTagsFilterNotTagsOutputReference",
    "DataAwsCeTagsFilterOr",
    "DataAwsCeTagsFilterOrCostCategory",
    "DataAwsCeTagsFilterOrCostCategoryOutputReference",
    "DataAwsCeTagsFilterOrDimension",
    "DataAwsCeTagsFilterOrDimensionOutputReference",
    "DataAwsCeTagsFilterOrList",
    "DataAwsCeTagsFilterOrOutputReference",
    "DataAwsCeTagsFilterOrTags",
    "DataAwsCeTagsFilterOrTagsOutputReference",
    "DataAwsCeTagsFilterOutputReference",
    "DataAwsCeTagsFilterTags",
    "DataAwsCeTagsFilterTagsOutputReference",
    "DataAwsCeTagsSortBy",
    "DataAwsCeTagsSortByList",
    "DataAwsCeTagsSortByOutputReference",
    "DataAwsCeTagsTimePeriod",
    "DataAwsCeTagsTimePeriodOutputReference",
]

publication.publish()
