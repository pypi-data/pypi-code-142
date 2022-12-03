'''
# `aws_s3_bucket_analytics_configuration`

Refer to the Terraform Registory for docs: [`aws_s3_bucket_analytics_configuration`](https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration).
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


class S3BucketAnalyticsConfiguration(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.s3BucketAnalyticsConfiguration.S3BucketAnalyticsConfiguration",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration aws_s3_bucket_analytics_configuration}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        bucket: builtins.str,
        name: builtins.str,
        filter: typing.Optional[typing.Union["S3BucketAnalyticsConfigurationFilter", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        storage_class_analysis: typing.Optional[typing.Union["S3BucketAnalyticsConfigurationStorageClassAnalysis", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration aws_s3_bucket_analytics_configuration} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#bucket S3BucketAnalyticsConfiguration#bucket}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#name S3BucketAnalyticsConfiguration#name}.
        :param filter: filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#filter S3BucketAnalyticsConfiguration#filter}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#id S3BucketAnalyticsConfiguration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param storage_class_analysis: storage_class_analysis block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#storage_class_analysis S3BucketAnalyticsConfiguration#storage_class_analysis}
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
                bucket: builtins.str,
                name: builtins.str,
                filter: typing.Optional[typing.Union[S3BucketAnalyticsConfigurationFilter, typing.Dict[str, typing.Any]]] = None,
                id: typing.Optional[builtins.str] = None,
                storage_class_analysis: typing.Optional[typing.Union[S3BucketAnalyticsConfigurationStorageClassAnalysis, typing.Dict[str, typing.Any]]] = None,
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
        config = S3BucketAnalyticsConfigurationConfig(
            bucket=bucket,
            name=name,
            filter=filter,
            id=id,
            storage_class_analysis=storage_class_analysis,
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
        prefix: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#prefix S3BucketAnalyticsConfiguration#prefix}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#tags S3BucketAnalyticsConfiguration#tags}.
        '''
        value = S3BucketAnalyticsConfigurationFilter(prefix=prefix, tags=tags)

        return typing.cast(None, jsii.invoke(self, "putFilter", [value]))

    @jsii.member(jsii_name="putStorageClassAnalysis")
    def put_storage_class_analysis(
        self,
        *,
        data_export: typing.Union["S3BucketAnalyticsConfigurationStorageClassAnalysisDataExport", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param data_export: data_export block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#data_export S3BucketAnalyticsConfiguration#data_export}
        '''
        value = S3BucketAnalyticsConfigurationStorageClassAnalysis(
            data_export=data_export
        )

        return typing.cast(None, jsii.invoke(self, "putStorageClassAnalysis", [value]))

    @jsii.member(jsii_name="resetFilter")
    def reset_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilter", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetStorageClassAnalysis")
    def reset_storage_class_analysis(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageClassAnalysis", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="filter")
    def filter(self) -> "S3BucketAnalyticsConfigurationFilterOutputReference":
        return typing.cast("S3BucketAnalyticsConfigurationFilterOutputReference", jsii.get(self, "filter"))

    @builtins.property
    @jsii.member(jsii_name="storageClassAnalysis")
    def storage_class_analysis(
        self,
    ) -> "S3BucketAnalyticsConfigurationStorageClassAnalysisOutputReference":
        return typing.cast("S3BucketAnalyticsConfigurationStorageClassAnalysisOutputReference", jsii.get(self, "storageClassAnalysis"))

    @builtins.property
    @jsii.member(jsii_name="bucketInput")
    def bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketInput"))

    @builtins.property
    @jsii.member(jsii_name="filterInput")
    def filter_input(self) -> typing.Optional["S3BucketAnalyticsConfigurationFilter"]:
        return typing.cast(typing.Optional["S3BucketAnalyticsConfigurationFilter"], jsii.get(self, "filterInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="storageClassAnalysisInput")
    def storage_class_analysis_input(
        self,
    ) -> typing.Optional["S3BucketAnalyticsConfigurationStorageClassAnalysis"]:
        return typing.cast(typing.Optional["S3BucketAnalyticsConfigurationStorageClassAnalysis"], jsii.get(self, "storageClassAnalysisInput"))

    @builtins.property
    @jsii.member(jsii_name="bucket")
    def bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucket"))

    @bucket.setter
    def bucket(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucket", value)

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


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.s3BucketAnalyticsConfiguration.S3BucketAnalyticsConfigurationConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "bucket": "bucket",
        "name": "name",
        "filter": "filter",
        "id": "id",
        "storage_class_analysis": "storageClassAnalysis",
    },
)
class S3BucketAnalyticsConfigurationConfig(cdktf.TerraformMetaArguments):
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
        bucket: builtins.str,
        name: builtins.str,
        filter: typing.Optional[typing.Union["S3BucketAnalyticsConfigurationFilter", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        storage_class_analysis: typing.Optional[typing.Union["S3BucketAnalyticsConfigurationStorageClassAnalysis", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#bucket S3BucketAnalyticsConfiguration#bucket}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#name S3BucketAnalyticsConfiguration#name}.
        :param filter: filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#filter S3BucketAnalyticsConfiguration#filter}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#id S3BucketAnalyticsConfiguration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param storage_class_analysis: storage_class_analysis block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#storage_class_analysis S3BucketAnalyticsConfiguration#storage_class_analysis}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(filter, dict):
            filter = S3BucketAnalyticsConfigurationFilter(**filter)
        if isinstance(storage_class_analysis, dict):
            storage_class_analysis = S3BucketAnalyticsConfigurationStorageClassAnalysis(**storage_class_analysis)
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
                bucket: builtins.str,
                name: builtins.str,
                filter: typing.Optional[typing.Union[S3BucketAnalyticsConfigurationFilter, typing.Dict[str, typing.Any]]] = None,
                id: typing.Optional[builtins.str] = None,
                storage_class_analysis: typing.Optional[typing.Union[S3BucketAnalyticsConfigurationStorageClassAnalysis, typing.Dict[str, typing.Any]]] = None,
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
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument filter", value=filter, expected_type=type_hints["filter"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument storage_class_analysis", value=storage_class_analysis, expected_type=type_hints["storage_class_analysis"])
        self._values: typing.Dict[str, typing.Any] = {
            "bucket": bucket,
            "name": name,
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
        if storage_class_analysis is not None:
            self._values["storage_class_analysis"] = storage_class_analysis

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
    def bucket(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#bucket S3BucketAnalyticsConfiguration#bucket}.'''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#name S3BucketAnalyticsConfiguration#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def filter(self) -> typing.Optional["S3BucketAnalyticsConfigurationFilter"]:
        '''filter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#filter S3BucketAnalyticsConfiguration#filter}
        '''
        result = self._values.get("filter")
        return typing.cast(typing.Optional["S3BucketAnalyticsConfigurationFilter"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#id S3BucketAnalyticsConfiguration#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_class_analysis(
        self,
    ) -> typing.Optional["S3BucketAnalyticsConfigurationStorageClassAnalysis"]:
        '''storage_class_analysis block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#storage_class_analysis S3BucketAnalyticsConfiguration#storage_class_analysis}
        '''
        result = self._values.get("storage_class_analysis")
        return typing.cast(typing.Optional["S3BucketAnalyticsConfigurationStorageClassAnalysis"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketAnalyticsConfigurationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.s3BucketAnalyticsConfiguration.S3BucketAnalyticsConfigurationFilter",
    jsii_struct_bases=[],
    name_mapping={"prefix": "prefix", "tags": "tags"},
)
class S3BucketAnalyticsConfigurationFilter:
    def __init__(
        self,
        *,
        prefix: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#prefix S3BucketAnalyticsConfiguration#prefix}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#tags S3BucketAnalyticsConfiguration#tags}.
        '''
        if __debug__:
            def stub(
                *,
                prefix: typing.Optional[builtins.str] = None,
                tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {}
        if prefix is not None:
            self._values["prefix"] = prefix
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#prefix S3BucketAnalyticsConfiguration#prefix}.'''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#tags S3BucketAnalyticsConfiguration#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketAnalyticsConfigurationFilter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketAnalyticsConfigurationFilterOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.s3BucketAnalyticsConfiguration.S3BucketAnalyticsConfigurationFilterOutputReference",
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

    @jsii.member(jsii_name="resetPrefix")
    def reset_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefix", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @builtins.property
    @jsii.member(jsii_name="prefixInput")
    def prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="prefix")
    def prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefix"))

    @prefix.setter
    def prefix(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefix", value)

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
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[S3BucketAnalyticsConfigurationFilter]:
        return typing.cast(typing.Optional[S3BucketAnalyticsConfigurationFilter], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketAnalyticsConfigurationFilter],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[S3BucketAnalyticsConfigurationFilter],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.s3BucketAnalyticsConfiguration.S3BucketAnalyticsConfigurationStorageClassAnalysis",
    jsii_struct_bases=[],
    name_mapping={"data_export": "dataExport"},
)
class S3BucketAnalyticsConfigurationStorageClassAnalysis:
    def __init__(
        self,
        *,
        data_export: typing.Union["S3BucketAnalyticsConfigurationStorageClassAnalysisDataExport", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param data_export: data_export block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#data_export S3BucketAnalyticsConfiguration#data_export}
        '''
        if isinstance(data_export, dict):
            data_export = S3BucketAnalyticsConfigurationStorageClassAnalysisDataExport(**data_export)
        if __debug__:
            def stub(
                *,
                data_export: typing.Union[S3BucketAnalyticsConfigurationStorageClassAnalysisDataExport, typing.Dict[str, typing.Any]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument data_export", value=data_export, expected_type=type_hints["data_export"])
        self._values: typing.Dict[str, typing.Any] = {
            "data_export": data_export,
        }

    @builtins.property
    def data_export(
        self,
    ) -> "S3BucketAnalyticsConfigurationStorageClassAnalysisDataExport":
        '''data_export block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#data_export S3BucketAnalyticsConfiguration#data_export}
        '''
        result = self._values.get("data_export")
        assert result is not None, "Required property 'data_export' is missing"
        return typing.cast("S3BucketAnalyticsConfigurationStorageClassAnalysisDataExport", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketAnalyticsConfigurationStorageClassAnalysis(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.s3BucketAnalyticsConfiguration.S3BucketAnalyticsConfigurationStorageClassAnalysisDataExport",
    jsii_struct_bases=[],
    name_mapping={
        "destination": "destination",
        "output_schema_version": "outputSchemaVersion",
    },
)
class S3BucketAnalyticsConfigurationStorageClassAnalysisDataExport:
    def __init__(
        self,
        *,
        destination: typing.Union["S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestination", typing.Dict[str, typing.Any]],
        output_schema_version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param destination: destination block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#destination S3BucketAnalyticsConfiguration#destination}
        :param output_schema_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#output_schema_version S3BucketAnalyticsConfiguration#output_schema_version}.
        '''
        if isinstance(destination, dict):
            destination = S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestination(**destination)
        if __debug__:
            def stub(
                *,
                destination: typing.Union[S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestination, typing.Dict[str, typing.Any]],
                output_schema_version: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
            check_type(argname="argument output_schema_version", value=output_schema_version, expected_type=type_hints["output_schema_version"])
        self._values: typing.Dict[str, typing.Any] = {
            "destination": destination,
        }
        if output_schema_version is not None:
            self._values["output_schema_version"] = output_schema_version

    @builtins.property
    def destination(
        self,
    ) -> "S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestination":
        '''destination block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#destination S3BucketAnalyticsConfiguration#destination}
        '''
        result = self._values.get("destination")
        assert result is not None, "Required property 'destination' is missing"
        return typing.cast("S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestination", result)

    @builtins.property
    def output_schema_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#output_schema_version S3BucketAnalyticsConfiguration#output_schema_version}.'''
        result = self._values.get("output_schema_version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketAnalyticsConfigurationStorageClassAnalysisDataExport(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.s3BucketAnalyticsConfiguration.S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestination",
    jsii_struct_bases=[],
    name_mapping={"s3_bucket_destination": "s3BucketDestination"},
)
class S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestination:
    def __init__(
        self,
        *,
        s3_bucket_destination: typing.Union["S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestination", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param s3_bucket_destination: s3_bucket_destination block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#s3_bucket_destination S3BucketAnalyticsConfiguration#s3_bucket_destination}
        '''
        if isinstance(s3_bucket_destination, dict):
            s3_bucket_destination = S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestination(**s3_bucket_destination)
        if __debug__:
            def stub(
                *,
                s3_bucket_destination: typing.Union[S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestination, typing.Dict[str, typing.Any]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument s3_bucket_destination", value=s3_bucket_destination, expected_type=type_hints["s3_bucket_destination"])
        self._values: typing.Dict[str, typing.Any] = {
            "s3_bucket_destination": s3_bucket_destination,
        }

    @builtins.property
    def s3_bucket_destination(
        self,
    ) -> "S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestination":
        '''s3_bucket_destination block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#s3_bucket_destination S3BucketAnalyticsConfiguration#s3_bucket_destination}
        '''
        result = self._values.get("s3_bucket_destination")
        assert result is not None, "Required property 's3_bucket_destination' is missing"
        return typing.cast("S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestination", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestination(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestinationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.s3BucketAnalyticsConfiguration.S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestinationOutputReference",
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

    @jsii.member(jsii_name="putS3BucketDestination")
    def put_s3_bucket_destination(
        self,
        *,
        bucket_arn: builtins.str,
        bucket_account_id: typing.Optional[builtins.str] = None,
        format: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#bucket_arn S3BucketAnalyticsConfiguration#bucket_arn}.
        :param bucket_account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#bucket_account_id S3BucketAnalyticsConfiguration#bucket_account_id}.
        :param format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#format S3BucketAnalyticsConfiguration#format}.
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#prefix S3BucketAnalyticsConfiguration#prefix}.
        '''
        value = S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestination(
            bucket_arn=bucket_arn,
            bucket_account_id=bucket_account_id,
            format=format,
            prefix=prefix,
        )

        return typing.cast(None, jsii.invoke(self, "putS3BucketDestination", [value]))

    @builtins.property
    @jsii.member(jsii_name="s3BucketDestination")
    def s3_bucket_destination(
        self,
    ) -> "S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestinationOutputReference":
        return typing.cast("S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestinationOutputReference", jsii.get(self, "s3BucketDestination"))

    @builtins.property
    @jsii.member(jsii_name="s3BucketDestinationInput")
    def s3_bucket_destination_input(
        self,
    ) -> typing.Optional["S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestination"]:
        return typing.cast(typing.Optional["S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestination"], jsii.get(self, "s3BucketDestinationInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestination]:
        return typing.cast(typing.Optional[S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestination], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestination],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestination],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.s3BucketAnalyticsConfiguration.S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestination",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_arn": "bucketArn",
        "bucket_account_id": "bucketAccountId",
        "format": "format",
        "prefix": "prefix",
    },
)
class S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestination:
    def __init__(
        self,
        *,
        bucket_arn: builtins.str,
        bucket_account_id: typing.Optional[builtins.str] = None,
        format: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#bucket_arn S3BucketAnalyticsConfiguration#bucket_arn}.
        :param bucket_account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#bucket_account_id S3BucketAnalyticsConfiguration#bucket_account_id}.
        :param format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#format S3BucketAnalyticsConfiguration#format}.
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#prefix S3BucketAnalyticsConfiguration#prefix}.
        '''
        if __debug__:
            def stub(
                *,
                bucket_arn: builtins.str,
                bucket_account_id: typing.Optional[builtins.str] = None,
                format: typing.Optional[builtins.str] = None,
                prefix: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument bucket_arn", value=bucket_arn, expected_type=type_hints["bucket_arn"])
            check_type(argname="argument bucket_account_id", value=bucket_account_id, expected_type=type_hints["bucket_account_id"])
            check_type(argname="argument format", value=format, expected_type=type_hints["format"])
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
        self._values: typing.Dict[str, typing.Any] = {
            "bucket_arn": bucket_arn,
        }
        if bucket_account_id is not None:
            self._values["bucket_account_id"] = bucket_account_id
        if format is not None:
            self._values["format"] = format
        if prefix is not None:
            self._values["prefix"] = prefix

    @builtins.property
    def bucket_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#bucket_arn S3BucketAnalyticsConfiguration#bucket_arn}.'''
        result = self._values.get("bucket_arn")
        assert result is not None, "Required property 'bucket_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bucket_account_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#bucket_account_id S3BucketAnalyticsConfiguration#bucket_account_id}.'''
        result = self._values.get("bucket_account_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def format(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#format S3BucketAnalyticsConfiguration#format}.'''
        result = self._values.get("format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#prefix S3BucketAnalyticsConfiguration#prefix}.'''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestination(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestinationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.s3BucketAnalyticsConfiguration.S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestinationOutputReference",
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

    @jsii.member(jsii_name="resetBucketAccountId")
    def reset_bucket_account_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketAccountId", []))

    @jsii.member(jsii_name="resetFormat")
    def reset_format(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFormat", []))

    @jsii.member(jsii_name="resetPrefix")
    def reset_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefix", []))

    @builtins.property
    @jsii.member(jsii_name="bucketAccountIdInput")
    def bucket_account_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketAccountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketArnInput")
    def bucket_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketArnInput"))

    @builtins.property
    @jsii.member(jsii_name="formatInput")
    def format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "formatInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixInput")
    def prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketAccountId")
    def bucket_account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketAccountId"))

    @bucket_account_id.setter
    def bucket_account_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketAccountId", value)

    @builtins.property
    @jsii.member(jsii_name="bucketArn")
    def bucket_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketArn"))

    @bucket_arn.setter
    def bucket_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketArn", value)

    @builtins.property
    @jsii.member(jsii_name="format")
    def format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "format"))

    @format.setter
    def format(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "format", value)

    @builtins.property
    @jsii.member(jsii_name="prefix")
    def prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefix"))

    @prefix.setter
    def prefix(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefix", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestination]:
        return typing.cast(typing.Optional[S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestination], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestination],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestination],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.s3BucketAnalyticsConfiguration.S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportOutputReference",
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

    @jsii.member(jsii_name="putDestination")
    def put_destination(
        self,
        *,
        s3_bucket_destination: typing.Union[S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestination, typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param s3_bucket_destination: s3_bucket_destination block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#s3_bucket_destination S3BucketAnalyticsConfiguration#s3_bucket_destination}
        '''
        value = S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestination(
            s3_bucket_destination=s3_bucket_destination
        )

        return typing.cast(None, jsii.invoke(self, "putDestination", [value]))

    @jsii.member(jsii_name="resetOutputSchemaVersion")
    def reset_output_schema_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOutputSchemaVersion", []))

    @builtins.property
    @jsii.member(jsii_name="destination")
    def destination(
        self,
    ) -> S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestinationOutputReference:
        return typing.cast(S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestinationOutputReference, jsii.get(self, "destination"))

    @builtins.property
    @jsii.member(jsii_name="destinationInput")
    def destination_input(
        self,
    ) -> typing.Optional[S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestination]:
        return typing.cast(typing.Optional[S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestination], jsii.get(self, "destinationInput"))

    @builtins.property
    @jsii.member(jsii_name="outputSchemaVersionInput")
    def output_schema_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "outputSchemaVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="outputSchemaVersion")
    def output_schema_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "outputSchemaVersion"))

    @output_schema_version.setter
    def output_schema_version(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outputSchemaVersion", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3BucketAnalyticsConfigurationStorageClassAnalysisDataExport]:
        return typing.cast(typing.Optional[S3BucketAnalyticsConfigurationStorageClassAnalysisDataExport], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketAnalyticsConfigurationStorageClassAnalysisDataExport],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[S3BucketAnalyticsConfigurationStorageClassAnalysisDataExport],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class S3BucketAnalyticsConfigurationStorageClassAnalysisOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.s3BucketAnalyticsConfiguration.S3BucketAnalyticsConfigurationStorageClassAnalysisOutputReference",
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

    @jsii.member(jsii_name="putDataExport")
    def put_data_export(
        self,
        *,
        destination: typing.Union[S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestination, typing.Dict[str, typing.Any]],
        output_schema_version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param destination: destination block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#destination S3BucketAnalyticsConfiguration#destination}
        :param output_schema_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_analytics_configuration#output_schema_version S3BucketAnalyticsConfiguration#output_schema_version}.
        '''
        value = S3BucketAnalyticsConfigurationStorageClassAnalysisDataExport(
            destination=destination, output_schema_version=output_schema_version
        )

        return typing.cast(None, jsii.invoke(self, "putDataExport", [value]))

    @builtins.property
    @jsii.member(jsii_name="dataExport")
    def data_export(
        self,
    ) -> S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportOutputReference:
        return typing.cast(S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportOutputReference, jsii.get(self, "dataExport"))

    @builtins.property
    @jsii.member(jsii_name="dataExportInput")
    def data_export_input(
        self,
    ) -> typing.Optional[S3BucketAnalyticsConfigurationStorageClassAnalysisDataExport]:
        return typing.cast(typing.Optional[S3BucketAnalyticsConfigurationStorageClassAnalysisDataExport], jsii.get(self, "dataExportInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3BucketAnalyticsConfigurationStorageClassAnalysis]:
        return typing.cast(typing.Optional[S3BucketAnalyticsConfigurationStorageClassAnalysis], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketAnalyticsConfigurationStorageClassAnalysis],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[S3BucketAnalyticsConfigurationStorageClassAnalysis],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "S3BucketAnalyticsConfiguration",
    "S3BucketAnalyticsConfigurationConfig",
    "S3BucketAnalyticsConfigurationFilter",
    "S3BucketAnalyticsConfigurationFilterOutputReference",
    "S3BucketAnalyticsConfigurationStorageClassAnalysis",
    "S3BucketAnalyticsConfigurationStorageClassAnalysisDataExport",
    "S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestination",
    "S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestinationOutputReference",
    "S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestination",
    "S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestinationOutputReference",
    "S3BucketAnalyticsConfigurationStorageClassAnalysisDataExportOutputReference",
    "S3BucketAnalyticsConfigurationStorageClassAnalysisOutputReference",
]

publication.publish()
