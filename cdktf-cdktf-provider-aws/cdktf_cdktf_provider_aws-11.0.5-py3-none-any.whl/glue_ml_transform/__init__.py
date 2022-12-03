'''
# `aws_glue_ml_transform`

Refer to the Terraform Registory for docs: [`aws_glue_ml_transform`](https://www.terraform.io/docs/providers/aws/r/glue_ml_transform).
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


class GlueMlTransform(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.glueMlTransform.GlueMlTransform",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/glue_ml_transform aws_glue_ml_transform}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        input_record_tables: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GlueMlTransformInputRecordTables", typing.Dict[str, typing.Any]]]],
        name: builtins.str,
        parameters: typing.Union["GlueMlTransformParameters", typing.Dict[str, typing.Any]],
        role_arn: builtins.str,
        description: typing.Optional[builtins.str] = None,
        glue_version: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        max_capacity: typing.Optional[jsii.Number] = None,
        max_retries: typing.Optional[jsii.Number] = None,
        number_of_workers: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeout: typing.Optional[jsii.Number] = None,
        worker_type: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/glue_ml_transform aws_glue_ml_transform} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param input_record_tables: input_record_tables block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_ml_transform#input_record_tables GlueMlTransform#input_record_tables}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_ml_transform#name GlueMlTransform#name}.
        :param parameters: parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_ml_transform#parameters GlueMlTransform#parameters}
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_ml_transform#role_arn GlueMlTransform#role_arn}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_ml_transform#description GlueMlTransform#description}.
        :param glue_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_ml_transform#glue_version GlueMlTransform#glue_version}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_ml_transform#id GlueMlTransform#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param max_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_ml_transform#max_capacity GlueMlTransform#max_capacity}.
        :param max_retries: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_ml_transform#max_retries GlueMlTransform#max_retries}.
        :param number_of_workers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_ml_transform#number_of_workers GlueMlTransform#number_of_workers}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_ml_transform#tags GlueMlTransform#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_ml_transform#tags_all GlueMlTransform#tags_all}.
        :param timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_ml_transform#timeout GlueMlTransform#timeout}.
        :param worker_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_ml_transform#worker_type GlueMlTransform#worker_type}.
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
                input_record_tables: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GlueMlTransformInputRecordTables, typing.Dict[str, typing.Any]]]],
                name: builtins.str,
                parameters: typing.Union[GlueMlTransformParameters, typing.Dict[str, typing.Any]],
                role_arn: builtins.str,
                description: typing.Optional[builtins.str] = None,
                glue_version: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                max_capacity: typing.Optional[jsii.Number] = None,
                max_retries: typing.Optional[jsii.Number] = None,
                number_of_workers: typing.Optional[jsii.Number] = None,
                tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                timeout: typing.Optional[jsii.Number] = None,
                worker_type: typing.Optional[builtins.str] = None,
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
        config = GlueMlTransformConfig(
            input_record_tables=input_record_tables,
            name=name,
            parameters=parameters,
            role_arn=role_arn,
            description=description,
            glue_version=glue_version,
            id=id,
            max_capacity=max_capacity,
            max_retries=max_retries,
            number_of_workers=number_of_workers,
            tags=tags,
            tags_all=tags_all,
            timeout=timeout,
            worker_type=worker_type,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putInputRecordTables")
    def put_input_record_tables(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GlueMlTransformInputRecordTables", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GlueMlTransformInputRecordTables, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putInputRecordTables", [value]))

    @jsii.member(jsii_name="putParameters")
    def put_parameters(
        self,
        *,
        find_matches_parameters: typing.Union["GlueMlTransformParametersFindMatchesParameters", typing.Dict[str, typing.Any]],
        transform_type: builtins.str,
    ) -> None:
        '''
        :param find_matches_parameters: find_matches_parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_ml_transform#find_matches_parameters GlueMlTransform#find_matches_parameters}
        :param transform_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_ml_transform#transform_type GlueMlTransform#transform_type}.
        '''
        value = GlueMlTransformParameters(
            find_matches_parameters=find_matches_parameters,
            transform_type=transform_type,
        )

        return typing.cast(None, jsii.invoke(self, "putParameters", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetGlueVersion")
    def reset_glue_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGlueVersion", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMaxCapacity")
    def reset_max_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxCapacity", []))

    @jsii.member(jsii_name="resetMaxRetries")
    def reset_max_retries(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxRetries", []))

    @jsii.member(jsii_name="resetNumberOfWorkers")
    def reset_number_of_workers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNumberOfWorkers", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetTimeout")
    def reset_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeout", []))

    @jsii.member(jsii_name="resetWorkerType")
    def reset_worker_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWorkerType", []))

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
    @jsii.member(jsii_name="inputRecordTables")
    def input_record_tables(self) -> "GlueMlTransformInputRecordTablesList":
        return typing.cast("GlueMlTransformInputRecordTablesList", jsii.get(self, "inputRecordTables"))

    @builtins.property
    @jsii.member(jsii_name="labelCount")
    def label_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "labelCount"))

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> "GlueMlTransformParametersOutputReference":
        return typing.cast("GlueMlTransformParametersOutputReference", jsii.get(self, "parameters"))

    @builtins.property
    @jsii.member(jsii_name="schema")
    def schema(self) -> "GlueMlTransformSchemaList":
        return typing.cast("GlueMlTransformSchemaList", jsii.get(self, "schema"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="glueVersionInput")
    def glue_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "glueVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="inputRecordTablesInput")
    def input_record_tables_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GlueMlTransformInputRecordTables"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GlueMlTransformInputRecordTables"]]], jsii.get(self, "inputRecordTablesInput"))

    @builtins.property
    @jsii.member(jsii_name="maxCapacityInput")
    def max_capacity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="maxRetriesInput")
    def max_retries_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxRetriesInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="numberOfWorkersInput")
    def number_of_workers_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "numberOfWorkersInput"))

    @builtins.property
    @jsii.member(jsii_name="parametersInput")
    def parameters_input(self) -> typing.Optional["GlueMlTransformParameters"]:
        return typing.cast(typing.Optional["GlueMlTransformParameters"], jsii.get(self, "parametersInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

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
    @jsii.member(jsii_name="timeoutInput")
    def timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="workerTypeInput")
    def worker_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "workerTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="glueVersion")
    def glue_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "glueVersion"))

    @glue_version.setter
    def glue_version(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "glueVersion", value)

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
    @jsii.member(jsii_name="maxCapacity")
    def max_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxCapacity"))

    @max_capacity.setter
    def max_capacity(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="maxRetries")
    def max_retries(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxRetries"))

    @max_retries.setter
    def max_retries(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxRetries", value)

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
    @jsii.member(jsii_name="numberOfWorkers")
    def number_of_workers(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "numberOfWorkers"))

    @number_of_workers.setter
    def number_of_workers(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numberOfWorkers", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

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

    @builtins.property
    @jsii.member(jsii_name="timeout")
    def timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "timeout"))

    @timeout.setter
    def timeout(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeout", value)

    @builtins.property
    @jsii.member(jsii_name="workerType")
    def worker_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "workerType"))

    @worker_type.setter
    def worker_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workerType", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.glueMlTransform.GlueMlTransformConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "input_record_tables": "inputRecordTables",
        "name": "name",
        "parameters": "parameters",
        "role_arn": "roleArn",
        "description": "description",
        "glue_version": "glueVersion",
        "id": "id",
        "max_capacity": "maxCapacity",
        "max_retries": "maxRetries",
        "number_of_workers": "numberOfWorkers",
        "tags": "tags",
        "tags_all": "tagsAll",
        "timeout": "timeout",
        "worker_type": "workerType",
    },
)
class GlueMlTransformConfig(cdktf.TerraformMetaArguments):
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
        input_record_tables: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GlueMlTransformInputRecordTables", typing.Dict[str, typing.Any]]]],
        name: builtins.str,
        parameters: typing.Union["GlueMlTransformParameters", typing.Dict[str, typing.Any]],
        role_arn: builtins.str,
        description: typing.Optional[builtins.str] = None,
        glue_version: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        max_capacity: typing.Optional[jsii.Number] = None,
        max_retries: typing.Optional[jsii.Number] = None,
        number_of_workers: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeout: typing.Optional[jsii.Number] = None,
        worker_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param input_record_tables: input_record_tables block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_ml_transform#input_record_tables GlueMlTransform#input_record_tables}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_ml_transform#name GlueMlTransform#name}.
        :param parameters: parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_ml_transform#parameters GlueMlTransform#parameters}
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_ml_transform#role_arn GlueMlTransform#role_arn}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_ml_transform#description GlueMlTransform#description}.
        :param glue_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_ml_transform#glue_version GlueMlTransform#glue_version}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_ml_transform#id GlueMlTransform#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param max_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_ml_transform#max_capacity GlueMlTransform#max_capacity}.
        :param max_retries: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_ml_transform#max_retries GlueMlTransform#max_retries}.
        :param number_of_workers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_ml_transform#number_of_workers GlueMlTransform#number_of_workers}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_ml_transform#tags GlueMlTransform#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_ml_transform#tags_all GlueMlTransform#tags_all}.
        :param timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_ml_transform#timeout GlueMlTransform#timeout}.
        :param worker_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_ml_transform#worker_type GlueMlTransform#worker_type}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(parameters, dict):
            parameters = GlueMlTransformParameters(**parameters)
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
                input_record_tables: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GlueMlTransformInputRecordTables, typing.Dict[str, typing.Any]]]],
                name: builtins.str,
                parameters: typing.Union[GlueMlTransformParameters, typing.Dict[str, typing.Any]],
                role_arn: builtins.str,
                description: typing.Optional[builtins.str] = None,
                glue_version: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                max_capacity: typing.Optional[jsii.Number] = None,
                max_retries: typing.Optional[jsii.Number] = None,
                number_of_workers: typing.Optional[jsii.Number] = None,
                tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                timeout: typing.Optional[jsii.Number] = None,
                worker_type: typing.Optional[builtins.str] = None,
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
            check_type(argname="argument input_record_tables", value=input_record_tables, expected_type=type_hints["input_record_tables"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument glue_version", value=glue_version, expected_type=type_hints["glue_version"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument max_capacity", value=max_capacity, expected_type=type_hints["max_capacity"])
            check_type(argname="argument max_retries", value=max_retries, expected_type=type_hints["max_retries"])
            check_type(argname="argument number_of_workers", value=number_of_workers, expected_type=type_hints["number_of_workers"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
            check_type(argname="argument worker_type", value=worker_type, expected_type=type_hints["worker_type"])
        self._values: typing.Dict[str, typing.Any] = {
            "input_record_tables": input_record_tables,
            "name": name,
            "parameters": parameters,
            "role_arn": role_arn,
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
        if description is not None:
            self._values["description"] = description
        if glue_version is not None:
            self._values["glue_version"] = glue_version
        if id is not None:
            self._values["id"] = id
        if max_capacity is not None:
            self._values["max_capacity"] = max_capacity
        if max_retries is not None:
            self._values["max_retries"] = max_retries
        if number_of_workers is not None:
            self._values["number_of_workers"] = number_of_workers
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if timeout is not None:
            self._values["timeout"] = timeout
        if worker_type is not None:
            self._values["worker_type"] = worker_type

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
    def input_record_tables(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["GlueMlTransformInputRecordTables"]]:
        '''input_record_tables block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_ml_transform#input_record_tables GlueMlTransform#input_record_tables}
        '''
        result = self._values.get("input_record_tables")
        assert result is not None, "Required property 'input_record_tables' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["GlueMlTransformInputRecordTables"]], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_ml_transform#name GlueMlTransform#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parameters(self) -> "GlueMlTransformParameters":
        '''parameters block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_ml_transform#parameters GlueMlTransform#parameters}
        '''
        result = self._values.get("parameters")
        assert result is not None, "Required property 'parameters' is missing"
        return typing.cast("GlueMlTransformParameters", result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_ml_transform#role_arn GlueMlTransform#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_ml_transform#description GlueMlTransform#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def glue_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_ml_transform#glue_version GlueMlTransform#glue_version}.'''
        result = self._values.get("glue_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_ml_transform#id GlueMlTransform#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_capacity(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_ml_transform#max_capacity GlueMlTransform#max_capacity}.'''
        result = self._values.get("max_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_retries(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_ml_transform#max_retries GlueMlTransform#max_retries}.'''
        result = self._values.get("max_retries")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def number_of_workers(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_ml_transform#number_of_workers GlueMlTransform#number_of_workers}.'''
        result = self._values.get("number_of_workers")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_ml_transform#tags GlueMlTransform#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_ml_transform#tags_all GlueMlTransform#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeout(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_ml_transform#timeout GlueMlTransform#timeout}.'''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def worker_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_ml_transform#worker_type GlueMlTransform#worker_type}.'''
        result = self._values.get("worker_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GlueMlTransformConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.glueMlTransform.GlueMlTransformInputRecordTables",
    jsii_struct_bases=[],
    name_mapping={
        "database_name": "databaseName",
        "table_name": "tableName",
        "catalog_id": "catalogId",
        "connection_name": "connectionName",
    },
)
class GlueMlTransformInputRecordTables:
    def __init__(
        self,
        *,
        database_name: builtins.str,
        table_name: builtins.str,
        catalog_id: typing.Optional[builtins.str] = None,
        connection_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param database_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_ml_transform#database_name GlueMlTransform#database_name}.
        :param table_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_ml_transform#table_name GlueMlTransform#table_name}.
        :param catalog_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_ml_transform#catalog_id GlueMlTransform#catalog_id}.
        :param connection_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_ml_transform#connection_name GlueMlTransform#connection_name}.
        '''
        if __debug__:
            def stub(
                *,
                database_name: builtins.str,
                table_name: builtins.str,
                catalog_id: typing.Optional[builtins.str] = None,
                connection_name: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
            check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
            check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
            check_type(argname="argument connection_name", value=connection_name, expected_type=type_hints["connection_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "database_name": database_name,
            "table_name": table_name,
        }
        if catalog_id is not None:
            self._values["catalog_id"] = catalog_id
        if connection_name is not None:
            self._values["connection_name"] = connection_name

    @builtins.property
    def database_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_ml_transform#database_name GlueMlTransform#database_name}.'''
        result = self._values.get("database_name")
        assert result is not None, "Required property 'database_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def table_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_ml_transform#table_name GlueMlTransform#table_name}.'''
        result = self._values.get("table_name")
        assert result is not None, "Required property 'table_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def catalog_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_ml_transform#catalog_id GlueMlTransform#catalog_id}.'''
        result = self._values.get("catalog_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def connection_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_ml_transform#connection_name GlueMlTransform#connection_name}.'''
        result = self._values.get("connection_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GlueMlTransformInputRecordTables(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GlueMlTransformInputRecordTablesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.glueMlTransform.GlueMlTransformInputRecordTablesList",
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
    ) -> "GlueMlTransformInputRecordTablesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GlueMlTransformInputRecordTablesOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GlueMlTransformInputRecordTables]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GlueMlTransformInputRecordTables]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GlueMlTransformInputRecordTables]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GlueMlTransformInputRecordTables]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GlueMlTransformInputRecordTablesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.glueMlTransform.GlueMlTransformInputRecordTablesOutputReference",
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

    @jsii.member(jsii_name="resetCatalogId")
    def reset_catalog_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCatalogId", []))

    @jsii.member(jsii_name="resetConnectionName")
    def reset_connection_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectionName", []))

    @builtins.property
    @jsii.member(jsii_name="catalogIdInput")
    def catalog_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "catalogIdInput"))

    @builtins.property
    @jsii.member(jsii_name="connectionNameInput")
    def connection_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectionNameInput"))

    @builtins.property
    @jsii.member(jsii_name="databaseNameInput")
    def database_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseNameInput"))

    @builtins.property
    @jsii.member(jsii_name="tableNameInput")
    def table_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tableNameInput"))

    @builtins.property
    @jsii.member(jsii_name="catalogId")
    def catalog_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "catalogId"))

    @catalog_id.setter
    def catalog_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "catalogId", value)

    @builtins.property
    @jsii.member(jsii_name="connectionName")
    def connection_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectionName"))

    @connection_name.setter
    def connection_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionName", value)

    @builtins.property
    @jsii.member(jsii_name="databaseName")
    def database_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "databaseName"))

    @database_name.setter
    def database_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseName", value)

    @builtins.property
    @jsii.member(jsii_name="tableName")
    def table_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tableName"))

    @table_name.setter
    def table_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tableName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GlueMlTransformInputRecordTables, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GlueMlTransformInputRecordTables, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GlueMlTransformInputRecordTables, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[GlueMlTransformInputRecordTables, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.glueMlTransform.GlueMlTransformParameters",
    jsii_struct_bases=[],
    name_mapping={
        "find_matches_parameters": "findMatchesParameters",
        "transform_type": "transformType",
    },
)
class GlueMlTransformParameters:
    def __init__(
        self,
        *,
        find_matches_parameters: typing.Union["GlueMlTransformParametersFindMatchesParameters", typing.Dict[str, typing.Any]],
        transform_type: builtins.str,
    ) -> None:
        '''
        :param find_matches_parameters: find_matches_parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_ml_transform#find_matches_parameters GlueMlTransform#find_matches_parameters}
        :param transform_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_ml_transform#transform_type GlueMlTransform#transform_type}.
        '''
        if isinstance(find_matches_parameters, dict):
            find_matches_parameters = GlueMlTransformParametersFindMatchesParameters(**find_matches_parameters)
        if __debug__:
            def stub(
                *,
                find_matches_parameters: typing.Union[GlueMlTransformParametersFindMatchesParameters, typing.Dict[str, typing.Any]],
                transform_type: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument find_matches_parameters", value=find_matches_parameters, expected_type=type_hints["find_matches_parameters"])
            check_type(argname="argument transform_type", value=transform_type, expected_type=type_hints["transform_type"])
        self._values: typing.Dict[str, typing.Any] = {
            "find_matches_parameters": find_matches_parameters,
            "transform_type": transform_type,
        }

    @builtins.property
    def find_matches_parameters(
        self,
    ) -> "GlueMlTransformParametersFindMatchesParameters":
        '''find_matches_parameters block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_ml_transform#find_matches_parameters GlueMlTransform#find_matches_parameters}
        '''
        result = self._values.get("find_matches_parameters")
        assert result is not None, "Required property 'find_matches_parameters' is missing"
        return typing.cast("GlueMlTransformParametersFindMatchesParameters", result)

    @builtins.property
    def transform_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_ml_transform#transform_type GlueMlTransform#transform_type}.'''
        result = self._values.get("transform_type")
        assert result is not None, "Required property 'transform_type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GlueMlTransformParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.glueMlTransform.GlueMlTransformParametersFindMatchesParameters",
    jsii_struct_bases=[],
    name_mapping={
        "accuracy_cost_trade_off": "accuracyCostTradeOff",
        "enforce_provided_labels": "enforceProvidedLabels",
        "precision_recall_trade_off": "precisionRecallTradeOff",
        "primary_key_column_name": "primaryKeyColumnName",
    },
)
class GlueMlTransformParametersFindMatchesParameters:
    def __init__(
        self,
        *,
        accuracy_cost_trade_off: typing.Optional[jsii.Number] = None,
        enforce_provided_labels: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        precision_recall_trade_off: typing.Optional[jsii.Number] = None,
        primary_key_column_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param accuracy_cost_trade_off: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_ml_transform#accuracy_cost_trade_off GlueMlTransform#accuracy_cost_trade_off}.
        :param enforce_provided_labels: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_ml_transform#enforce_provided_labels GlueMlTransform#enforce_provided_labels}.
        :param precision_recall_trade_off: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_ml_transform#precision_recall_trade_off GlueMlTransform#precision_recall_trade_off}.
        :param primary_key_column_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_ml_transform#primary_key_column_name GlueMlTransform#primary_key_column_name}.
        '''
        if __debug__:
            def stub(
                *,
                accuracy_cost_trade_off: typing.Optional[jsii.Number] = None,
                enforce_provided_labels: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                precision_recall_trade_off: typing.Optional[jsii.Number] = None,
                primary_key_column_name: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument accuracy_cost_trade_off", value=accuracy_cost_trade_off, expected_type=type_hints["accuracy_cost_trade_off"])
            check_type(argname="argument enforce_provided_labels", value=enforce_provided_labels, expected_type=type_hints["enforce_provided_labels"])
            check_type(argname="argument precision_recall_trade_off", value=precision_recall_trade_off, expected_type=type_hints["precision_recall_trade_off"])
            check_type(argname="argument primary_key_column_name", value=primary_key_column_name, expected_type=type_hints["primary_key_column_name"])
        self._values: typing.Dict[str, typing.Any] = {}
        if accuracy_cost_trade_off is not None:
            self._values["accuracy_cost_trade_off"] = accuracy_cost_trade_off
        if enforce_provided_labels is not None:
            self._values["enforce_provided_labels"] = enforce_provided_labels
        if precision_recall_trade_off is not None:
            self._values["precision_recall_trade_off"] = precision_recall_trade_off
        if primary_key_column_name is not None:
            self._values["primary_key_column_name"] = primary_key_column_name

    @builtins.property
    def accuracy_cost_trade_off(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_ml_transform#accuracy_cost_trade_off GlueMlTransform#accuracy_cost_trade_off}.'''
        result = self._values.get("accuracy_cost_trade_off")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def enforce_provided_labels(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_ml_transform#enforce_provided_labels GlueMlTransform#enforce_provided_labels}.'''
        result = self._values.get("enforce_provided_labels")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def precision_recall_trade_off(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_ml_transform#precision_recall_trade_off GlueMlTransform#precision_recall_trade_off}.'''
        result = self._values.get("precision_recall_trade_off")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def primary_key_column_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_ml_transform#primary_key_column_name GlueMlTransform#primary_key_column_name}.'''
        result = self._values.get("primary_key_column_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GlueMlTransformParametersFindMatchesParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GlueMlTransformParametersFindMatchesParametersOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.glueMlTransform.GlueMlTransformParametersFindMatchesParametersOutputReference",
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

    @jsii.member(jsii_name="resetAccuracyCostTradeOff")
    def reset_accuracy_cost_trade_off(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccuracyCostTradeOff", []))

    @jsii.member(jsii_name="resetEnforceProvidedLabels")
    def reset_enforce_provided_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnforceProvidedLabels", []))

    @jsii.member(jsii_name="resetPrecisionRecallTradeOff")
    def reset_precision_recall_trade_off(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrecisionRecallTradeOff", []))

    @jsii.member(jsii_name="resetPrimaryKeyColumnName")
    def reset_primary_key_column_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrimaryKeyColumnName", []))

    @builtins.property
    @jsii.member(jsii_name="accuracyCostTradeOffInput")
    def accuracy_cost_trade_off_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "accuracyCostTradeOffInput"))

    @builtins.property
    @jsii.member(jsii_name="enforceProvidedLabelsInput")
    def enforce_provided_labels_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enforceProvidedLabelsInput"))

    @builtins.property
    @jsii.member(jsii_name="precisionRecallTradeOffInput")
    def precision_recall_trade_off_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "precisionRecallTradeOffInput"))

    @builtins.property
    @jsii.member(jsii_name="primaryKeyColumnNameInput")
    def primary_key_column_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "primaryKeyColumnNameInput"))

    @builtins.property
    @jsii.member(jsii_name="accuracyCostTradeOff")
    def accuracy_cost_trade_off(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "accuracyCostTradeOff"))

    @accuracy_cost_trade_off.setter
    def accuracy_cost_trade_off(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accuracyCostTradeOff", value)

    @builtins.property
    @jsii.member(jsii_name="enforceProvidedLabels")
    def enforce_provided_labels(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enforceProvidedLabels"))

    @enforce_provided_labels.setter
    def enforce_provided_labels(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enforceProvidedLabels", value)

    @builtins.property
    @jsii.member(jsii_name="precisionRecallTradeOff")
    def precision_recall_trade_off(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "precisionRecallTradeOff"))

    @precision_recall_trade_off.setter
    def precision_recall_trade_off(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "precisionRecallTradeOff", value)

    @builtins.property
    @jsii.member(jsii_name="primaryKeyColumnName")
    def primary_key_column_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "primaryKeyColumnName"))

    @primary_key_column_name.setter
    def primary_key_column_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "primaryKeyColumnName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GlueMlTransformParametersFindMatchesParameters]:
        return typing.cast(typing.Optional[GlueMlTransformParametersFindMatchesParameters], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GlueMlTransformParametersFindMatchesParameters],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[GlueMlTransformParametersFindMatchesParameters],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GlueMlTransformParametersOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.glueMlTransform.GlueMlTransformParametersOutputReference",
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

    @jsii.member(jsii_name="putFindMatchesParameters")
    def put_find_matches_parameters(
        self,
        *,
        accuracy_cost_trade_off: typing.Optional[jsii.Number] = None,
        enforce_provided_labels: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        precision_recall_trade_off: typing.Optional[jsii.Number] = None,
        primary_key_column_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param accuracy_cost_trade_off: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_ml_transform#accuracy_cost_trade_off GlueMlTransform#accuracy_cost_trade_off}.
        :param enforce_provided_labels: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_ml_transform#enforce_provided_labels GlueMlTransform#enforce_provided_labels}.
        :param precision_recall_trade_off: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_ml_transform#precision_recall_trade_off GlueMlTransform#precision_recall_trade_off}.
        :param primary_key_column_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_ml_transform#primary_key_column_name GlueMlTransform#primary_key_column_name}.
        '''
        value = GlueMlTransformParametersFindMatchesParameters(
            accuracy_cost_trade_off=accuracy_cost_trade_off,
            enforce_provided_labels=enforce_provided_labels,
            precision_recall_trade_off=precision_recall_trade_off,
            primary_key_column_name=primary_key_column_name,
        )

        return typing.cast(None, jsii.invoke(self, "putFindMatchesParameters", [value]))

    @builtins.property
    @jsii.member(jsii_name="findMatchesParameters")
    def find_matches_parameters(
        self,
    ) -> GlueMlTransformParametersFindMatchesParametersOutputReference:
        return typing.cast(GlueMlTransformParametersFindMatchesParametersOutputReference, jsii.get(self, "findMatchesParameters"))

    @builtins.property
    @jsii.member(jsii_name="findMatchesParametersInput")
    def find_matches_parameters_input(
        self,
    ) -> typing.Optional[GlueMlTransformParametersFindMatchesParameters]:
        return typing.cast(typing.Optional[GlueMlTransformParametersFindMatchesParameters], jsii.get(self, "findMatchesParametersInput"))

    @builtins.property
    @jsii.member(jsii_name="transformTypeInput")
    def transform_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "transformTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="transformType")
    def transform_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "transformType"))

    @transform_type.setter
    def transform_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "transformType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GlueMlTransformParameters]:
        return typing.cast(typing.Optional[GlueMlTransformParameters], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[GlueMlTransformParameters]) -> None:
        if __debug__:
            def stub(value: typing.Optional[GlueMlTransformParameters]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.glueMlTransform.GlueMlTransformSchema",
    jsii_struct_bases=[],
    name_mapping={},
)
class GlueMlTransformSchema:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GlueMlTransformSchema(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GlueMlTransformSchemaList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.glueMlTransform.GlueMlTransformSchemaList",
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
    def get(self, index: jsii.Number) -> "GlueMlTransformSchemaOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GlueMlTransformSchemaOutputReference", jsii.invoke(self, "get", [index]))

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


class GlueMlTransformSchemaOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.glueMlTransform.GlueMlTransformSchemaOutputReference",
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
    @jsii.member(jsii_name="dataType")
    def data_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataType"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GlueMlTransformSchema]:
        return typing.cast(typing.Optional[GlueMlTransformSchema], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[GlueMlTransformSchema]) -> None:
        if __debug__:
            def stub(value: typing.Optional[GlueMlTransformSchema]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GlueMlTransform",
    "GlueMlTransformConfig",
    "GlueMlTransformInputRecordTables",
    "GlueMlTransformInputRecordTablesList",
    "GlueMlTransformInputRecordTablesOutputReference",
    "GlueMlTransformParameters",
    "GlueMlTransformParametersFindMatchesParameters",
    "GlueMlTransformParametersFindMatchesParametersOutputReference",
    "GlueMlTransformParametersOutputReference",
    "GlueMlTransformSchema",
    "GlueMlTransformSchemaList",
    "GlueMlTransformSchemaOutputReference",
]

publication.publish()
