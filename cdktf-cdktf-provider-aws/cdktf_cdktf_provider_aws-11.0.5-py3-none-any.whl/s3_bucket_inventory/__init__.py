'''
# `aws_s3_bucket_inventory`

Refer to the Terraform Registory for docs: [`aws_s3_bucket_inventory`](https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory).
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


class S3BucketInventory(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.s3BucketInventory.S3BucketInventory",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory aws_s3_bucket_inventory}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        bucket: builtins.str,
        destination: typing.Union["S3BucketInventoryDestination", typing.Dict[str, typing.Any]],
        included_object_versions: builtins.str,
        name: builtins.str,
        schedule: typing.Union["S3BucketInventorySchedule", typing.Dict[str, typing.Any]],
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        filter: typing.Optional[typing.Union["S3BucketInventoryFilter", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        optional_fields: typing.Optional[typing.Sequence[builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory aws_s3_bucket_inventory} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#bucket S3BucketInventory#bucket}.
        :param destination: destination block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#destination S3BucketInventory#destination}
        :param included_object_versions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#included_object_versions S3BucketInventory#included_object_versions}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#name S3BucketInventory#name}.
        :param schedule: schedule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#schedule S3BucketInventory#schedule}
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#enabled S3BucketInventory#enabled}.
        :param filter: filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#filter S3BucketInventory#filter}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#id S3BucketInventory#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param optional_fields: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#optional_fields S3BucketInventory#optional_fields}.
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
                destination: typing.Union[S3BucketInventoryDestination, typing.Dict[str, typing.Any]],
                included_object_versions: builtins.str,
                name: builtins.str,
                schedule: typing.Union[S3BucketInventorySchedule, typing.Dict[str, typing.Any]],
                enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                filter: typing.Optional[typing.Union[S3BucketInventoryFilter, typing.Dict[str, typing.Any]]] = None,
                id: typing.Optional[builtins.str] = None,
                optional_fields: typing.Optional[typing.Sequence[builtins.str]] = None,
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
        config = S3BucketInventoryConfig(
            bucket=bucket,
            destination=destination,
            included_object_versions=included_object_versions,
            name=name,
            schedule=schedule,
            enabled=enabled,
            filter=filter,
            id=id,
            optional_fields=optional_fields,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putDestination")
    def put_destination(
        self,
        *,
        bucket: typing.Union["S3BucketInventoryDestinationBucket", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param bucket: bucket block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#bucket S3BucketInventory#bucket}
        '''
        value = S3BucketInventoryDestination(bucket=bucket)

        return typing.cast(None, jsii.invoke(self, "putDestination", [value]))

    @jsii.member(jsii_name="putFilter")
    def put_filter(self, *, prefix: typing.Optional[builtins.str] = None) -> None:
        '''
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#prefix S3BucketInventory#prefix}.
        '''
        value = S3BucketInventoryFilter(prefix=prefix)

        return typing.cast(None, jsii.invoke(self, "putFilter", [value]))

    @jsii.member(jsii_name="putSchedule")
    def put_schedule(self, *, frequency: builtins.str) -> None:
        '''
        :param frequency: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#frequency S3BucketInventory#frequency}.
        '''
        value = S3BucketInventorySchedule(frequency=frequency)

        return typing.cast(None, jsii.invoke(self, "putSchedule", [value]))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetFilter")
    def reset_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilter", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetOptionalFields")
    def reset_optional_fields(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOptionalFields", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="destination")
    def destination(self) -> "S3BucketInventoryDestinationOutputReference":
        return typing.cast("S3BucketInventoryDestinationOutputReference", jsii.get(self, "destination"))

    @builtins.property
    @jsii.member(jsii_name="filter")
    def filter(self) -> "S3BucketInventoryFilterOutputReference":
        return typing.cast("S3BucketInventoryFilterOutputReference", jsii.get(self, "filter"))

    @builtins.property
    @jsii.member(jsii_name="schedule")
    def schedule(self) -> "S3BucketInventoryScheduleOutputReference":
        return typing.cast("S3BucketInventoryScheduleOutputReference", jsii.get(self, "schedule"))

    @builtins.property
    @jsii.member(jsii_name="bucketInput")
    def bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationInput")
    def destination_input(self) -> typing.Optional["S3BucketInventoryDestination"]:
        return typing.cast(typing.Optional["S3BucketInventoryDestination"], jsii.get(self, "destinationInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="filterInput")
    def filter_input(self) -> typing.Optional["S3BucketInventoryFilter"]:
        return typing.cast(typing.Optional["S3BucketInventoryFilter"], jsii.get(self, "filterInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="includedObjectVersionsInput")
    def included_object_versions_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "includedObjectVersionsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="optionalFieldsInput")
    def optional_fields_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "optionalFieldsInput"))

    @builtins.property
    @jsii.member(jsii_name="scheduleInput")
    def schedule_input(self) -> typing.Optional["S3BucketInventorySchedule"]:
        return typing.cast(typing.Optional["S3BucketInventorySchedule"], jsii.get(self, "scheduleInput"))

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
    @jsii.member(jsii_name="includedObjectVersions")
    def included_object_versions(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "includedObjectVersions"))

    @included_object_versions.setter
    def included_object_versions(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includedObjectVersions", value)

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
    @jsii.member(jsii_name="optionalFields")
    def optional_fields(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "optionalFields"))

    @optional_fields.setter
    def optional_fields(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "optionalFields", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.s3BucketInventory.S3BucketInventoryConfig",
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
        "destination": "destination",
        "included_object_versions": "includedObjectVersions",
        "name": "name",
        "schedule": "schedule",
        "enabled": "enabled",
        "filter": "filter",
        "id": "id",
        "optional_fields": "optionalFields",
    },
)
class S3BucketInventoryConfig(cdktf.TerraformMetaArguments):
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
        destination: typing.Union["S3BucketInventoryDestination", typing.Dict[str, typing.Any]],
        included_object_versions: builtins.str,
        name: builtins.str,
        schedule: typing.Union["S3BucketInventorySchedule", typing.Dict[str, typing.Any]],
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        filter: typing.Optional[typing.Union["S3BucketInventoryFilter", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        optional_fields: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#bucket S3BucketInventory#bucket}.
        :param destination: destination block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#destination S3BucketInventory#destination}
        :param included_object_versions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#included_object_versions S3BucketInventory#included_object_versions}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#name S3BucketInventory#name}.
        :param schedule: schedule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#schedule S3BucketInventory#schedule}
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#enabled S3BucketInventory#enabled}.
        :param filter: filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#filter S3BucketInventory#filter}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#id S3BucketInventory#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param optional_fields: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#optional_fields S3BucketInventory#optional_fields}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(destination, dict):
            destination = S3BucketInventoryDestination(**destination)
        if isinstance(schedule, dict):
            schedule = S3BucketInventorySchedule(**schedule)
        if isinstance(filter, dict):
            filter = S3BucketInventoryFilter(**filter)
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
                destination: typing.Union[S3BucketInventoryDestination, typing.Dict[str, typing.Any]],
                included_object_versions: builtins.str,
                name: builtins.str,
                schedule: typing.Union[S3BucketInventorySchedule, typing.Dict[str, typing.Any]],
                enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                filter: typing.Optional[typing.Union[S3BucketInventoryFilter, typing.Dict[str, typing.Any]]] = None,
                id: typing.Optional[builtins.str] = None,
                optional_fields: typing.Optional[typing.Sequence[builtins.str]] = None,
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
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
            check_type(argname="argument included_object_versions", value=included_object_versions, expected_type=type_hints["included_object_versions"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument schedule", value=schedule, expected_type=type_hints["schedule"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument filter", value=filter, expected_type=type_hints["filter"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument optional_fields", value=optional_fields, expected_type=type_hints["optional_fields"])
        self._values: typing.Dict[str, typing.Any] = {
            "bucket": bucket,
            "destination": destination,
            "included_object_versions": included_object_versions,
            "name": name,
            "schedule": schedule,
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
        if enabled is not None:
            self._values["enabled"] = enabled
        if filter is not None:
            self._values["filter"] = filter
        if id is not None:
            self._values["id"] = id
        if optional_fields is not None:
            self._values["optional_fields"] = optional_fields

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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#bucket S3BucketInventory#bucket}.'''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def destination(self) -> "S3BucketInventoryDestination":
        '''destination block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#destination S3BucketInventory#destination}
        '''
        result = self._values.get("destination")
        assert result is not None, "Required property 'destination' is missing"
        return typing.cast("S3BucketInventoryDestination", result)

    @builtins.property
    def included_object_versions(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#included_object_versions S3BucketInventory#included_object_versions}.'''
        result = self._values.get("included_object_versions")
        assert result is not None, "Required property 'included_object_versions' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#name S3BucketInventory#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def schedule(self) -> "S3BucketInventorySchedule":
        '''schedule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#schedule S3BucketInventory#schedule}
        '''
        result = self._values.get("schedule")
        assert result is not None, "Required property 'schedule' is missing"
        return typing.cast("S3BucketInventorySchedule", result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#enabled S3BucketInventory#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def filter(self) -> typing.Optional["S3BucketInventoryFilter"]:
        '''filter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#filter S3BucketInventory#filter}
        '''
        result = self._values.get("filter")
        return typing.cast(typing.Optional["S3BucketInventoryFilter"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#id S3BucketInventory#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def optional_fields(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#optional_fields S3BucketInventory#optional_fields}.'''
        result = self._values.get("optional_fields")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketInventoryConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.s3BucketInventory.S3BucketInventoryDestination",
    jsii_struct_bases=[],
    name_mapping={"bucket": "bucket"},
)
class S3BucketInventoryDestination:
    def __init__(
        self,
        *,
        bucket: typing.Union["S3BucketInventoryDestinationBucket", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param bucket: bucket block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#bucket S3BucketInventory#bucket}
        '''
        if isinstance(bucket, dict):
            bucket = S3BucketInventoryDestinationBucket(**bucket)
        if __debug__:
            def stub(
                *,
                bucket: typing.Union[S3BucketInventoryDestinationBucket, typing.Dict[str, typing.Any]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
        self._values: typing.Dict[str, typing.Any] = {
            "bucket": bucket,
        }

    @builtins.property
    def bucket(self) -> "S3BucketInventoryDestinationBucket":
        '''bucket block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#bucket S3BucketInventory#bucket}
        '''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast("S3BucketInventoryDestinationBucket", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketInventoryDestination(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.s3BucketInventory.S3BucketInventoryDestinationBucket",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_arn": "bucketArn",
        "format": "format",
        "account_id": "accountId",
        "encryption": "encryption",
        "prefix": "prefix",
    },
)
class S3BucketInventoryDestinationBucket:
    def __init__(
        self,
        *,
        bucket_arn: builtins.str,
        format: builtins.str,
        account_id: typing.Optional[builtins.str] = None,
        encryption: typing.Optional[typing.Union["S3BucketInventoryDestinationBucketEncryption", typing.Dict[str, typing.Any]]] = None,
        prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#bucket_arn S3BucketInventory#bucket_arn}.
        :param format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#format S3BucketInventory#format}.
        :param account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#account_id S3BucketInventory#account_id}.
        :param encryption: encryption block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#encryption S3BucketInventory#encryption}
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#prefix S3BucketInventory#prefix}.
        '''
        if isinstance(encryption, dict):
            encryption = S3BucketInventoryDestinationBucketEncryption(**encryption)
        if __debug__:
            def stub(
                *,
                bucket_arn: builtins.str,
                format: builtins.str,
                account_id: typing.Optional[builtins.str] = None,
                encryption: typing.Optional[typing.Union[S3BucketInventoryDestinationBucketEncryption, typing.Dict[str, typing.Any]]] = None,
                prefix: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument bucket_arn", value=bucket_arn, expected_type=type_hints["bucket_arn"])
            check_type(argname="argument format", value=format, expected_type=type_hints["format"])
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument encryption", value=encryption, expected_type=type_hints["encryption"])
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
        self._values: typing.Dict[str, typing.Any] = {
            "bucket_arn": bucket_arn,
            "format": format,
        }
        if account_id is not None:
            self._values["account_id"] = account_id
        if encryption is not None:
            self._values["encryption"] = encryption
        if prefix is not None:
            self._values["prefix"] = prefix

    @builtins.property
    def bucket_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#bucket_arn S3BucketInventory#bucket_arn}.'''
        result = self._values.get("bucket_arn")
        assert result is not None, "Required property 'bucket_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def format(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#format S3BucketInventory#format}.'''
        result = self._values.get("format")
        assert result is not None, "Required property 'format' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def account_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#account_id S3BucketInventory#account_id}.'''
        result = self._values.get("account_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encryption(
        self,
    ) -> typing.Optional["S3BucketInventoryDestinationBucketEncryption"]:
        '''encryption block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#encryption S3BucketInventory#encryption}
        '''
        result = self._values.get("encryption")
        return typing.cast(typing.Optional["S3BucketInventoryDestinationBucketEncryption"], result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#prefix S3BucketInventory#prefix}.'''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketInventoryDestinationBucket(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.s3BucketInventory.S3BucketInventoryDestinationBucketEncryption",
    jsii_struct_bases=[],
    name_mapping={"sse_kms": "sseKms", "sse_s3": "sseS3"},
)
class S3BucketInventoryDestinationBucketEncryption:
    def __init__(
        self,
        *,
        sse_kms: typing.Optional[typing.Union["S3BucketInventoryDestinationBucketEncryptionSseKms", typing.Dict[str, typing.Any]]] = None,
        sse_s3: typing.Optional[typing.Union["S3BucketInventoryDestinationBucketEncryptionSseS3", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param sse_kms: sse_kms block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#sse_kms S3BucketInventory#sse_kms}
        :param sse_s3: sse_s3 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#sse_s3 S3BucketInventory#sse_s3}
        '''
        if isinstance(sse_kms, dict):
            sse_kms = S3BucketInventoryDestinationBucketEncryptionSseKms(**sse_kms)
        if isinstance(sse_s3, dict):
            sse_s3 = S3BucketInventoryDestinationBucketEncryptionSseS3(**sse_s3)
        if __debug__:
            def stub(
                *,
                sse_kms: typing.Optional[typing.Union[S3BucketInventoryDestinationBucketEncryptionSseKms, typing.Dict[str, typing.Any]]] = None,
                sse_s3: typing.Optional[typing.Union[S3BucketInventoryDestinationBucketEncryptionSseS3, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument sse_kms", value=sse_kms, expected_type=type_hints["sse_kms"])
            check_type(argname="argument sse_s3", value=sse_s3, expected_type=type_hints["sse_s3"])
        self._values: typing.Dict[str, typing.Any] = {}
        if sse_kms is not None:
            self._values["sse_kms"] = sse_kms
        if sse_s3 is not None:
            self._values["sse_s3"] = sse_s3

    @builtins.property
    def sse_kms(
        self,
    ) -> typing.Optional["S3BucketInventoryDestinationBucketEncryptionSseKms"]:
        '''sse_kms block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#sse_kms S3BucketInventory#sse_kms}
        '''
        result = self._values.get("sse_kms")
        return typing.cast(typing.Optional["S3BucketInventoryDestinationBucketEncryptionSseKms"], result)

    @builtins.property
    def sse_s3(
        self,
    ) -> typing.Optional["S3BucketInventoryDestinationBucketEncryptionSseS3"]:
        '''sse_s3 block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#sse_s3 S3BucketInventory#sse_s3}
        '''
        result = self._values.get("sse_s3")
        return typing.cast(typing.Optional["S3BucketInventoryDestinationBucketEncryptionSseS3"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketInventoryDestinationBucketEncryption(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketInventoryDestinationBucketEncryptionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.s3BucketInventory.S3BucketInventoryDestinationBucketEncryptionOutputReference",
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

    @jsii.member(jsii_name="putSseKms")
    def put_sse_kms(self, *, key_id: builtins.str) -> None:
        '''
        :param key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#key_id S3BucketInventory#key_id}.
        '''
        value = S3BucketInventoryDestinationBucketEncryptionSseKms(key_id=key_id)

        return typing.cast(None, jsii.invoke(self, "putSseKms", [value]))

    @jsii.member(jsii_name="putSseS3")
    def put_sse_s3(self) -> None:
        value = S3BucketInventoryDestinationBucketEncryptionSseS3()

        return typing.cast(None, jsii.invoke(self, "putSseS3", [value]))

    @jsii.member(jsii_name="resetSseKms")
    def reset_sse_kms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSseKms", []))

    @jsii.member(jsii_name="resetSseS3")
    def reset_sse_s3(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSseS3", []))

    @builtins.property
    @jsii.member(jsii_name="sseKms")
    def sse_kms(
        self,
    ) -> "S3BucketInventoryDestinationBucketEncryptionSseKmsOutputReference":
        return typing.cast("S3BucketInventoryDestinationBucketEncryptionSseKmsOutputReference", jsii.get(self, "sseKms"))

    @builtins.property
    @jsii.member(jsii_name="sseS3")
    def sse_s3(
        self,
    ) -> "S3BucketInventoryDestinationBucketEncryptionSseS3OutputReference":
        return typing.cast("S3BucketInventoryDestinationBucketEncryptionSseS3OutputReference", jsii.get(self, "sseS3"))

    @builtins.property
    @jsii.member(jsii_name="sseKmsInput")
    def sse_kms_input(
        self,
    ) -> typing.Optional["S3BucketInventoryDestinationBucketEncryptionSseKms"]:
        return typing.cast(typing.Optional["S3BucketInventoryDestinationBucketEncryptionSseKms"], jsii.get(self, "sseKmsInput"))

    @builtins.property
    @jsii.member(jsii_name="sseS3Input")
    def sse_s3_input(
        self,
    ) -> typing.Optional["S3BucketInventoryDestinationBucketEncryptionSseS3"]:
        return typing.cast(typing.Optional["S3BucketInventoryDestinationBucketEncryptionSseS3"], jsii.get(self, "sseS3Input"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3BucketInventoryDestinationBucketEncryption]:
        return typing.cast(typing.Optional[S3BucketInventoryDestinationBucketEncryption], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketInventoryDestinationBucketEncryption],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[S3BucketInventoryDestinationBucketEncryption],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.s3BucketInventory.S3BucketInventoryDestinationBucketEncryptionSseKms",
    jsii_struct_bases=[],
    name_mapping={"key_id": "keyId"},
)
class S3BucketInventoryDestinationBucketEncryptionSseKms:
    def __init__(self, *, key_id: builtins.str) -> None:
        '''
        :param key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#key_id S3BucketInventory#key_id}.
        '''
        if __debug__:
            def stub(*, key_id: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument key_id", value=key_id, expected_type=type_hints["key_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "key_id": key_id,
        }

    @builtins.property
    def key_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#key_id S3BucketInventory#key_id}.'''
        result = self._values.get("key_id")
        assert result is not None, "Required property 'key_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketInventoryDestinationBucketEncryptionSseKms(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketInventoryDestinationBucketEncryptionSseKmsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.s3BucketInventory.S3BucketInventoryDestinationBucketEncryptionSseKmsOutputReference",
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
    @jsii.member(jsii_name="keyIdInput")
    def key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="keyId")
    def key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyId"))

    @key_id.setter
    def key_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3BucketInventoryDestinationBucketEncryptionSseKms]:
        return typing.cast(typing.Optional[S3BucketInventoryDestinationBucketEncryptionSseKms], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketInventoryDestinationBucketEncryptionSseKms],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[S3BucketInventoryDestinationBucketEncryptionSseKms],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.s3BucketInventory.S3BucketInventoryDestinationBucketEncryptionSseS3",
    jsii_struct_bases=[],
    name_mapping={},
)
class S3BucketInventoryDestinationBucketEncryptionSseS3:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketInventoryDestinationBucketEncryptionSseS3(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketInventoryDestinationBucketEncryptionSseS3OutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.s3BucketInventory.S3BucketInventoryDestinationBucketEncryptionSseS3OutputReference",
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
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3BucketInventoryDestinationBucketEncryptionSseS3]:
        return typing.cast(typing.Optional[S3BucketInventoryDestinationBucketEncryptionSseS3], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketInventoryDestinationBucketEncryptionSseS3],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[S3BucketInventoryDestinationBucketEncryptionSseS3],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class S3BucketInventoryDestinationBucketOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.s3BucketInventory.S3BucketInventoryDestinationBucketOutputReference",
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

    @jsii.member(jsii_name="putEncryption")
    def put_encryption(
        self,
        *,
        sse_kms: typing.Optional[typing.Union[S3BucketInventoryDestinationBucketEncryptionSseKms, typing.Dict[str, typing.Any]]] = None,
        sse_s3: typing.Optional[typing.Union[S3BucketInventoryDestinationBucketEncryptionSseS3, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param sse_kms: sse_kms block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#sse_kms S3BucketInventory#sse_kms}
        :param sse_s3: sse_s3 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#sse_s3 S3BucketInventory#sse_s3}
        '''
        value = S3BucketInventoryDestinationBucketEncryption(
            sse_kms=sse_kms, sse_s3=sse_s3
        )

        return typing.cast(None, jsii.invoke(self, "putEncryption", [value]))

    @jsii.member(jsii_name="resetAccountId")
    def reset_account_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccountId", []))

    @jsii.member(jsii_name="resetEncryption")
    def reset_encryption(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncryption", []))

    @jsii.member(jsii_name="resetPrefix")
    def reset_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefix", []))

    @builtins.property
    @jsii.member(jsii_name="encryption")
    def encryption(self) -> S3BucketInventoryDestinationBucketEncryptionOutputReference:
        return typing.cast(S3BucketInventoryDestinationBucketEncryptionOutputReference, jsii.get(self, "encryption"))

    @builtins.property
    @jsii.member(jsii_name="accountIdInput")
    def account_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketArnInput")
    def bucket_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketArnInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptionInput")
    def encryption_input(
        self,
    ) -> typing.Optional[S3BucketInventoryDestinationBucketEncryption]:
        return typing.cast(typing.Optional[S3BucketInventoryDestinationBucketEncryption], jsii.get(self, "encryptionInput"))

    @builtins.property
    @jsii.member(jsii_name="formatInput")
    def format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "formatInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixInput")
    def prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixInput"))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value)

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
    def internal_value(self) -> typing.Optional[S3BucketInventoryDestinationBucket]:
        return typing.cast(typing.Optional[S3BucketInventoryDestinationBucket], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketInventoryDestinationBucket],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[S3BucketInventoryDestinationBucket],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class S3BucketInventoryDestinationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.s3BucketInventory.S3BucketInventoryDestinationOutputReference",
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

    @jsii.member(jsii_name="putBucket")
    def put_bucket(
        self,
        *,
        bucket_arn: builtins.str,
        format: builtins.str,
        account_id: typing.Optional[builtins.str] = None,
        encryption: typing.Optional[typing.Union[S3BucketInventoryDestinationBucketEncryption, typing.Dict[str, typing.Any]]] = None,
        prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#bucket_arn S3BucketInventory#bucket_arn}.
        :param format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#format S3BucketInventory#format}.
        :param account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#account_id S3BucketInventory#account_id}.
        :param encryption: encryption block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#encryption S3BucketInventory#encryption}
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#prefix S3BucketInventory#prefix}.
        '''
        value = S3BucketInventoryDestinationBucket(
            bucket_arn=bucket_arn,
            format=format,
            account_id=account_id,
            encryption=encryption,
            prefix=prefix,
        )

        return typing.cast(None, jsii.invoke(self, "putBucket", [value]))

    @builtins.property
    @jsii.member(jsii_name="bucket")
    def bucket(self) -> S3BucketInventoryDestinationBucketOutputReference:
        return typing.cast(S3BucketInventoryDestinationBucketOutputReference, jsii.get(self, "bucket"))

    @builtins.property
    @jsii.member(jsii_name="bucketInput")
    def bucket_input(self) -> typing.Optional[S3BucketInventoryDestinationBucket]:
        return typing.cast(typing.Optional[S3BucketInventoryDestinationBucket], jsii.get(self, "bucketInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[S3BucketInventoryDestination]:
        return typing.cast(typing.Optional[S3BucketInventoryDestination], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketInventoryDestination],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[S3BucketInventoryDestination]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.s3BucketInventory.S3BucketInventoryFilter",
    jsii_struct_bases=[],
    name_mapping={"prefix": "prefix"},
)
class S3BucketInventoryFilter:
    def __init__(self, *, prefix: typing.Optional[builtins.str] = None) -> None:
        '''
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#prefix S3BucketInventory#prefix}.
        '''
        if __debug__:
            def stub(*, prefix: typing.Optional[builtins.str] = None) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
        self._values: typing.Dict[str, typing.Any] = {}
        if prefix is not None:
            self._values["prefix"] = prefix

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#prefix S3BucketInventory#prefix}.'''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketInventoryFilter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketInventoryFilterOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.s3BucketInventory.S3BucketInventoryFilterOutputReference",
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

    @builtins.property
    @jsii.member(jsii_name="prefixInput")
    def prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixInput"))

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
    def internal_value(self) -> typing.Optional[S3BucketInventoryFilter]:
        return typing.cast(typing.Optional[S3BucketInventoryFilter], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[S3BucketInventoryFilter]) -> None:
        if __debug__:
            def stub(value: typing.Optional[S3BucketInventoryFilter]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.s3BucketInventory.S3BucketInventorySchedule",
    jsii_struct_bases=[],
    name_mapping={"frequency": "frequency"},
)
class S3BucketInventorySchedule:
    def __init__(self, *, frequency: builtins.str) -> None:
        '''
        :param frequency: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#frequency S3BucketInventory#frequency}.
        '''
        if __debug__:
            def stub(*, frequency: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument frequency", value=frequency, expected_type=type_hints["frequency"])
        self._values: typing.Dict[str, typing.Any] = {
            "frequency": frequency,
        }

    @builtins.property
    def frequency(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3_bucket_inventory#frequency S3BucketInventory#frequency}.'''
        result = self._values.get("frequency")
        assert result is not None, "Required property 'frequency' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketInventorySchedule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketInventoryScheduleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.s3BucketInventory.S3BucketInventoryScheduleOutputReference",
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
    @jsii.member(jsii_name="frequencyInput")
    def frequency_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "frequencyInput"))

    @builtins.property
    @jsii.member(jsii_name="frequency")
    def frequency(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "frequency"))

    @frequency.setter
    def frequency(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "frequency", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[S3BucketInventorySchedule]:
        return typing.cast(typing.Optional[S3BucketInventorySchedule], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[S3BucketInventorySchedule]) -> None:
        if __debug__:
            def stub(value: typing.Optional[S3BucketInventorySchedule]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "S3BucketInventory",
    "S3BucketInventoryConfig",
    "S3BucketInventoryDestination",
    "S3BucketInventoryDestinationBucket",
    "S3BucketInventoryDestinationBucketEncryption",
    "S3BucketInventoryDestinationBucketEncryptionOutputReference",
    "S3BucketInventoryDestinationBucketEncryptionSseKms",
    "S3BucketInventoryDestinationBucketEncryptionSseKmsOutputReference",
    "S3BucketInventoryDestinationBucketEncryptionSseS3",
    "S3BucketInventoryDestinationBucketEncryptionSseS3OutputReference",
    "S3BucketInventoryDestinationBucketOutputReference",
    "S3BucketInventoryDestinationOutputReference",
    "S3BucketInventoryFilter",
    "S3BucketInventoryFilterOutputReference",
    "S3BucketInventorySchedule",
    "S3BucketInventoryScheduleOutputReference",
]

publication.publish()
