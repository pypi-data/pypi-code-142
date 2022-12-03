'''
# `aws_appsync_datasource`

Refer to the Terraform Registory for docs: [`aws_appsync_datasource`](https://www.terraform.io/docs/providers/aws/r/appsync_datasource).
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


class AppsyncDatasource(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appsyncDatasource.AppsyncDatasource",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource aws_appsync_datasource}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        api_id: builtins.str,
        name: builtins.str,
        type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        dynamodb_config: typing.Optional[typing.Union["AppsyncDatasourceDynamodbConfig", typing.Dict[str, typing.Any]]] = None,
        elasticsearch_config: typing.Optional[typing.Union["AppsyncDatasourceElasticsearchConfig", typing.Dict[str, typing.Any]]] = None,
        http_config: typing.Optional[typing.Union["AppsyncDatasourceHttpConfig", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        lambda_config: typing.Optional[typing.Union["AppsyncDatasourceLambdaConfig", typing.Dict[str, typing.Any]]] = None,
        relational_database_config: typing.Optional[typing.Union["AppsyncDatasourceRelationalDatabaseConfig", typing.Dict[str, typing.Any]]] = None,
        service_role_arn: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource aws_appsync_datasource} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param api_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#api_id AppsyncDatasource#api_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#name AppsyncDatasource#name}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#type AppsyncDatasource#type}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#description AppsyncDatasource#description}.
        :param dynamodb_config: dynamodb_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#dynamodb_config AppsyncDatasource#dynamodb_config}
        :param elasticsearch_config: elasticsearch_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#elasticsearch_config AppsyncDatasource#elasticsearch_config}
        :param http_config: http_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#http_config AppsyncDatasource#http_config}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#id AppsyncDatasource#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param lambda_config: lambda_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#lambda_config AppsyncDatasource#lambda_config}
        :param relational_database_config: relational_database_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#relational_database_config AppsyncDatasource#relational_database_config}
        :param service_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#service_role_arn AppsyncDatasource#service_role_arn}.
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
                name: builtins.str,
                type: builtins.str,
                description: typing.Optional[builtins.str] = None,
                dynamodb_config: typing.Optional[typing.Union[AppsyncDatasourceDynamodbConfig, typing.Dict[str, typing.Any]]] = None,
                elasticsearch_config: typing.Optional[typing.Union[AppsyncDatasourceElasticsearchConfig, typing.Dict[str, typing.Any]]] = None,
                http_config: typing.Optional[typing.Union[AppsyncDatasourceHttpConfig, typing.Dict[str, typing.Any]]] = None,
                id: typing.Optional[builtins.str] = None,
                lambda_config: typing.Optional[typing.Union[AppsyncDatasourceLambdaConfig, typing.Dict[str, typing.Any]]] = None,
                relational_database_config: typing.Optional[typing.Union[AppsyncDatasourceRelationalDatabaseConfig, typing.Dict[str, typing.Any]]] = None,
                service_role_arn: typing.Optional[builtins.str] = None,
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
        config = AppsyncDatasourceConfig(
            api_id=api_id,
            name=name,
            type=type,
            description=description,
            dynamodb_config=dynamodb_config,
            elasticsearch_config=elasticsearch_config,
            http_config=http_config,
            id=id,
            lambda_config=lambda_config,
            relational_database_config=relational_database_config,
            service_role_arn=service_role_arn,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putDynamodbConfig")
    def put_dynamodb_config(
        self,
        *,
        table_name: builtins.str,
        delta_sync_config: typing.Optional[typing.Union["AppsyncDatasourceDynamodbConfigDeltaSyncConfig", typing.Dict[str, typing.Any]]] = None,
        region: typing.Optional[builtins.str] = None,
        use_caller_credentials: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        versioned: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param table_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#table_name AppsyncDatasource#table_name}.
        :param delta_sync_config: delta_sync_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#delta_sync_config AppsyncDatasource#delta_sync_config}
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#region AppsyncDatasource#region}.
        :param use_caller_credentials: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#use_caller_credentials AppsyncDatasource#use_caller_credentials}.
        :param versioned: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#versioned AppsyncDatasource#versioned}.
        '''
        value = AppsyncDatasourceDynamodbConfig(
            table_name=table_name,
            delta_sync_config=delta_sync_config,
            region=region,
            use_caller_credentials=use_caller_credentials,
            versioned=versioned,
        )

        return typing.cast(None, jsii.invoke(self, "putDynamodbConfig", [value]))

    @jsii.member(jsii_name="putElasticsearchConfig")
    def put_elasticsearch_config(
        self,
        *,
        endpoint: builtins.str,
        region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#endpoint AppsyncDatasource#endpoint}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#region AppsyncDatasource#region}.
        '''
        value = AppsyncDatasourceElasticsearchConfig(endpoint=endpoint, region=region)

        return typing.cast(None, jsii.invoke(self, "putElasticsearchConfig", [value]))

    @jsii.member(jsii_name="putHttpConfig")
    def put_http_config(
        self,
        *,
        endpoint: builtins.str,
        authorization_config: typing.Optional[typing.Union["AppsyncDatasourceHttpConfigAuthorizationConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#endpoint AppsyncDatasource#endpoint}.
        :param authorization_config: authorization_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#authorization_config AppsyncDatasource#authorization_config}
        '''
        value = AppsyncDatasourceHttpConfig(
            endpoint=endpoint, authorization_config=authorization_config
        )

        return typing.cast(None, jsii.invoke(self, "putHttpConfig", [value]))

    @jsii.member(jsii_name="putLambdaConfig")
    def put_lambda_config(self, *, function_arn: builtins.str) -> None:
        '''
        :param function_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#function_arn AppsyncDatasource#function_arn}.
        '''
        value = AppsyncDatasourceLambdaConfig(function_arn=function_arn)

        return typing.cast(None, jsii.invoke(self, "putLambdaConfig", [value]))

    @jsii.member(jsii_name="putRelationalDatabaseConfig")
    def put_relational_database_config(
        self,
        *,
        http_endpoint_config: typing.Optional[typing.Union["AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfig", typing.Dict[str, typing.Any]]] = None,
        source_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param http_endpoint_config: http_endpoint_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#http_endpoint_config AppsyncDatasource#http_endpoint_config}
        :param source_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#source_type AppsyncDatasource#source_type}.
        '''
        value = AppsyncDatasourceRelationalDatabaseConfig(
            http_endpoint_config=http_endpoint_config, source_type=source_type
        )

        return typing.cast(None, jsii.invoke(self, "putRelationalDatabaseConfig", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDynamodbConfig")
    def reset_dynamodb_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDynamodbConfig", []))

    @jsii.member(jsii_name="resetElasticsearchConfig")
    def reset_elasticsearch_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetElasticsearchConfig", []))

    @jsii.member(jsii_name="resetHttpConfig")
    def reset_http_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpConfig", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLambdaConfig")
    def reset_lambda_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLambdaConfig", []))

    @jsii.member(jsii_name="resetRelationalDatabaseConfig")
    def reset_relational_database_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRelationalDatabaseConfig", []))

    @jsii.member(jsii_name="resetServiceRoleArn")
    def reset_service_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceRoleArn", []))

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
    @jsii.member(jsii_name="dynamodbConfig")
    def dynamodb_config(self) -> "AppsyncDatasourceDynamodbConfigOutputReference":
        return typing.cast("AppsyncDatasourceDynamodbConfigOutputReference", jsii.get(self, "dynamodbConfig"))

    @builtins.property
    @jsii.member(jsii_name="elasticsearchConfig")
    def elasticsearch_config(
        self,
    ) -> "AppsyncDatasourceElasticsearchConfigOutputReference":
        return typing.cast("AppsyncDatasourceElasticsearchConfigOutputReference", jsii.get(self, "elasticsearchConfig"))

    @builtins.property
    @jsii.member(jsii_name="httpConfig")
    def http_config(self) -> "AppsyncDatasourceHttpConfigOutputReference":
        return typing.cast("AppsyncDatasourceHttpConfigOutputReference", jsii.get(self, "httpConfig"))

    @builtins.property
    @jsii.member(jsii_name="lambdaConfig")
    def lambda_config(self) -> "AppsyncDatasourceLambdaConfigOutputReference":
        return typing.cast("AppsyncDatasourceLambdaConfigOutputReference", jsii.get(self, "lambdaConfig"))

    @builtins.property
    @jsii.member(jsii_name="relationalDatabaseConfig")
    def relational_database_config(
        self,
    ) -> "AppsyncDatasourceRelationalDatabaseConfigOutputReference":
        return typing.cast("AppsyncDatasourceRelationalDatabaseConfigOutputReference", jsii.get(self, "relationalDatabaseConfig"))

    @builtins.property
    @jsii.member(jsii_name="apiIdInput")
    def api_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiIdInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="dynamodbConfigInput")
    def dynamodb_config_input(
        self,
    ) -> typing.Optional["AppsyncDatasourceDynamodbConfig"]:
        return typing.cast(typing.Optional["AppsyncDatasourceDynamodbConfig"], jsii.get(self, "dynamodbConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="elasticsearchConfigInput")
    def elasticsearch_config_input(
        self,
    ) -> typing.Optional["AppsyncDatasourceElasticsearchConfig"]:
        return typing.cast(typing.Optional["AppsyncDatasourceElasticsearchConfig"], jsii.get(self, "elasticsearchConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="httpConfigInput")
    def http_config_input(self) -> typing.Optional["AppsyncDatasourceHttpConfig"]:
        return typing.cast(typing.Optional["AppsyncDatasourceHttpConfig"], jsii.get(self, "httpConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="lambdaConfigInput")
    def lambda_config_input(self) -> typing.Optional["AppsyncDatasourceLambdaConfig"]:
        return typing.cast(typing.Optional["AppsyncDatasourceLambdaConfig"], jsii.get(self, "lambdaConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="relationalDatabaseConfigInput")
    def relational_database_config_input(
        self,
    ) -> typing.Optional["AppsyncDatasourceRelationalDatabaseConfig"]:
        return typing.cast(typing.Optional["AppsyncDatasourceRelationalDatabaseConfig"], jsii.get(self, "relationalDatabaseConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceRoleArnInput")
    def service_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

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
    @jsii.member(jsii_name="serviceRoleArn")
    def service_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceRoleArn"))

    @service_role_arn.setter
    def service_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceRoleArn", value)

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


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appsyncDatasource.AppsyncDatasourceConfig",
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
        "name": "name",
        "type": "type",
        "description": "description",
        "dynamodb_config": "dynamodbConfig",
        "elasticsearch_config": "elasticsearchConfig",
        "http_config": "httpConfig",
        "id": "id",
        "lambda_config": "lambdaConfig",
        "relational_database_config": "relationalDatabaseConfig",
        "service_role_arn": "serviceRoleArn",
    },
)
class AppsyncDatasourceConfig(cdktf.TerraformMetaArguments):
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
        name: builtins.str,
        type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        dynamodb_config: typing.Optional[typing.Union["AppsyncDatasourceDynamodbConfig", typing.Dict[str, typing.Any]]] = None,
        elasticsearch_config: typing.Optional[typing.Union["AppsyncDatasourceElasticsearchConfig", typing.Dict[str, typing.Any]]] = None,
        http_config: typing.Optional[typing.Union["AppsyncDatasourceHttpConfig", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        lambda_config: typing.Optional[typing.Union["AppsyncDatasourceLambdaConfig", typing.Dict[str, typing.Any]]] = None,
        relational_database_config: typing.Optional[typing.Union["AppsyncDatasourceRelationalDatabaseConfig", typing.Dict[str, typing.Any]]] = None,
        service_role_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param api_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#api_id AppsyncDatasource#api_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#name AppsyncDatasource#name}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#type AppsyncDatasource#type}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#description AppsyncDatasource#description}.
        :param dynamodb_config: dynamodb_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#dynamodb_config AppsyncDatasource#dynamodb_config}
        :param elasticsearch_config: elasticsearch_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#elasticsearch_config AppsyncDatasource#elasticsearch_config}
        :param http_config: http_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#http_config AppsyncDatasource#http_config}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#id AppsyncDatasource#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param lambda_config: lambda_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#lambda_config AppsyncDatasource#lambda_config}
        :param relational_database_config: relational_database_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#relational_database_config AppsyncDatasource#relational_database_config}
        :param service_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#service_role_arn AppsyncDatasource#service_role_arn}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(dynamodb_config, dict):
            dynamodb_config = AppsyncDatasourceDynamodbConfig(**dynamodb_config)
        if isinstance(elasticsearch_config, dict):
            elasticsearch_config = AppsyncDatasourceElasticsearchConfig(**elasticsearch_config)
        if isinstance(http_config, dict):
            http_config = AppsyncDatasourceHttpConfig(**http_config)
        if isinstance(lambda_config, dict):
            lambda_config = AppsyncDatasourceLambdaConfig(**lambda_config)
        if isinstance(relational_database_config, dict):
            relational_database_config = AppsyncDatasourceRelationalDatabaseConfig(**relational_database_config)
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
                name: builtins.str,
                type: builtins.str,
                description: typing.Optional[builtins.str] = None,
                dynamodb_config: typing.Optional[typing.Union[AppsyncDatasourceDynamodbConfig, typing.Dict[str, typing.Any]]] = None,
                elasticsearch_config: typing.Optional[typing.Union[AppsyncDatasourceElasticsearchConfig, typing.Dict[str, typing.Any]]] = None,
                http_config: typing.Optional[typing.Union[AppsyncDatasourceHttpConfig, typing.Dict[str, typing.Any]]] = None,
                id: typing.Optional[builtins.str] = None,
                lambda_config: typing.Optional[typing.Union[AppsyncDatasourceLambdaConfig, typing.Dict[str, typing.Any]]] = None,
                relational_database_config: typing.Optional[typing.Union[AppsyncDatasourceRelationalDatabaseConfig, typing.Dict[str, typing.Any]]] = None,
                service_role_arn: typing.Optional[builtins.str] = None,
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
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument dynamodb_config", value=dynamodb_config, expected_type=type_hints["dynamodb_config"])
            check_type(argname="argument elasticsearch_config", value=elasticsearch_config, expected_type=type_hints["elasticsearch_config"])
            check_type(argname="argument http_config", value=http_config, expected_type=type_hints["http_config"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument lambda_config", value=lambda_config, expected_type=type_hints["lambda_config"])
            check_type(argname="argument relational_database_config", value=relational_database_config, expected_type=type_hints["relational_database_config"])
            check_type(argname="argument service_role_arn", value=service_role_arn, expected_type=type_hints["service_role_arn"])
        self._values: typing.Dict[str, typing.Any] = {
            "api_id": api_id,
            "name": name,
            "type": type,
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
        if dynamodb_config is not None:
            self._values["dynamodb_config"] = dynamodb_config
        if elasticsearch_config is not None:
            self._values["elasticsearch_config"] = elasticsearch_config
        if http_config is not None:
            self._values["http_config"] = http_config
        if id is not None:
            self._values["id"] = id
        if lambda_config is not None:
            self._values["lambda_config"] = lambda_config
        if relational_database_config is not None:
            self._values["relational_database_config"] = relational_database_config
        if service_role_arn is not None:
            self._values["service_role_arn"] = service_role_arn

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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#api_id AppsyncDatasource#api_id}.'''
        result = self._values.get("api_id")
        assert result is not None, "Required property 'api_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#name AppsyncDatasource#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#type AppsyncDatasource#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#description AppsyncDatasource#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dynamodb_config(self) -> typing.Optional["AppsyncDatasourceDynamodbConfig"]:
        '''dynamodb_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#dynamodb_config AppsyncDatasource#dynamodb_config}
        '''
        result = self._values.get("dynamodb_config")
        return typing.cast(typing.Optional["AppsyncDatasourceDynamodbConfig"], result)

    @builtins.property
    def elasticsearch_config(
        self,
    ) -> typing.Optional["AppsyncDatasourceElasticsearchConfig"]:
        '''elasticsearch_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#elasticsearch_config AppsyncDatasource#elasticsearch_config}
        '''
        result = self._values.get("elasticsearch_config")
        return typing.cast(typing.Optional["AppsyncDatasourceElasticsearchConfig"], result)

    @builtins.property
    def http_config(self) -> typing.Optional["AppsyncDatasourceHttpConfig"]:
        '''http_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#http_config AppsyncDatasource#http_config}
        '''
        result = self._values.get("http_config")
        return typing.cast(typing.Optional["AppsyncDatasourceHttpConfig"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#id AppsyncDatasource#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lambda_config(self) -> typing.Optional["AppsyncDatasourceLambdaConfig"]:
        '''lambda_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#lambda_config AppsyncDatasource#lambda_config}
        '''
        result = self._values.get("lambda_config")
        return typing.cast(typing.Optional["AppsyncDatasourceLambdaConfig"], result)

    @builtins.property
    def relational_database_config(
        self,
    ) -> typing.Optional["AppsyncDatasourceRelationalDatabaseConfig"]:
        '''relational_database_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#relational_database_config AppsyncDatasource#relational_database_config}
        '''
        result = self._values.get("relational_database_config")
        return typing.cast(typing.Optional["AppsyncDatasourceRelationalDatabaseConfig"], result)

    @builtins.property
    def service_role_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#service_role_arn AppsyncDatasource#service_role_arn}.'''
        result = self._values.get("service_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncDatasourceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appsyncDatasource.AppsyncDatasourceDynamodbConfig",
    jsii_struct_bases=[],
    name_mapping={
        "table_name": "tableName",
        "delta_sync_config": "deltaSyncConfig",
        "region": "region",
        "use_caller_credentials": "useCallerCredentials",
        "versioned": "versioned",
    },
)
class AppsyncDatasourceDynamodbConfig:
    def __init__(
        self,
        *,
        table_name: builtins.str,
        delta_sync_config: typing.Optional[typing.Union["AppsyncDatasourceDynamodbConfigDeltaSyncConfig", typing.Dict[str, typing.Any]]] = None,
        region: typing.Optional[builtins.str] = None,
        use_caller_credentials: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        versioned: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param table_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#table_name AppsyncDatasource#table_name}.
        :param delta_sync_config: delta_sync_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#delta_sync_config AppsyncDatasource#delta_sync_config}
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#region AppsyncDatasource#region}.
        :param use_caller_credentials: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#use_caller_credentials AppsyncDatasource#use_caller_credentials}.
        :param versioned: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#versioned AppsyncDatasource#versioned}.
        '''
        if isinstance(delta_sync_config, dict):
            delta_sync_config = AppsyncDatasourceDynamodbConfigDeltaSyncConfig(**delta_sync_config)
        if __debug__:
            def stub(
                *,
                table_name: builtins.str,
                delta_sync_config: typing.Optional[typing.Union[AppsyncDatasourceDynamodbConfigDeltaSyncConfig, typing.Dict[str, typing.Any]]] = None,
                region: typing.Optional[builtins.str] = None,
                use_caller_credentials: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                versioned: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
            check_type(argname="argument delta_sync_config", value=delta_sync_config, expected_type=type_hints["delta_sync_config"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument use_caller_credentials", value=use_caller_credentials, expected_type=type_hints["use_caller_credentials"])
            check_type(argname="argument versioned", value=versioned, expected_type=type_hints["versioned"])
        self._values: typing.Dict[str, typing.Any] = {
            "table_name": table_name,
        }
        if delta_sync_config is not None:
            self._values["delta_sync_config"] = delta_sync_config
        if region is not None:
            self._values["region"] = region
        if use_caller_credentials is not None:
            self._values["use_caller_credentials"] = use_caller_credentials
        if versioned is not None:
            self._values["versioned"] = versioned

    @builtins.property
    def table_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#table_name AppsyncDatasource#table_name}.'''
        result = self._values.get("table_name")
        assert result is not None, "Required property 'table_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def delta_sync_config(
        self,
    ) -> typing.Optional["AppsyncDatasourceDynamodbConfigDeltaSyncConfig"]:
        '''delta_sync_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#delta_sync_config AppsyncDatasource#delta_sync_config}
        '''
        result = self._values.get("delta_sync_config")
        return typing.cast(typing.Optional["AppsyncDatasourceDynamodbConfigDeltaSyncConfig"], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#region AppsyncDatasource#region}.'''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def use_caller_credentials(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#use_caller_credentials AppsyncDatasource#use_caller_credentials}.'''
        result = self._values.get("use_caller_credentials")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def versioned(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#versioned AppsyncDatasource#versioned}.'''
        result = self._values.get("versioned")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncDatasourceDynamodbConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appsyncDatasource.AppsyncDatasourceDynamodbConfigDeltaSyncConfig",
    jsii_struct_bases=[],
    name_mapping={
        "delta_sync_table_name": "deltaSyncTableName",
        "base_table_ttl": "baseTableTtl",
        "delta_sync_table_ttl": "deltaSyncTableTtl",
    },
)
class AppsyncDatasourceDynamodbConfigDeltaSyncConfig:
    def __init__(
        self,
        *,
        delta_sync_table_name: builtins.str,
        base_table_ttl: typing.Optional[jsii.Number] = None,
        delta_sync_table_ttl: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param delta_sync_table_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#delta_sync_table_name AppsyncDatasource#delta_sync_table_name}.
        :param base_table_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#base_table_ttl AppsyncDatasource#base_table_ttl}.
        :param delta_sync_table_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#delta_sync_table_ttl AppsyncDatasource#delta_sync_table_ttl}.
        '''
        if __debug__:
            def stub(
                *,
                delta_sync_table_name: builtins.str,
                base_table_ttl: typing.Optional[jsii.Number] = None,
                delta_sync_table_ttl: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument delta_sync_table_name", value=delta_sync_table_name, expected_type=type_hints["delta_sync_table_name"])
            check_type(argname="argument base_table_ttl", value=base_table_ttl, expected_type=type_hints["base_table_ttl"])
            check_type(argname="argument delta_sync_table_ttl", value=delta_sync_table_ttl, expected_type=type_hints["delta_sync_table_ttl"])
        self._values: typing.Dict[str, typing.Any] = {
            "delta_sync_table_name": delta_sync_table_name,
        }
        if base_table_ttl is not None:
            self._values["base_table_ttl"] = base_table_ttl
        if delta_sync_table_ttl is not None:
            self._values["delta_sync_table_ttl"] = delta_sync_table_ttl

    @builtins.property
    def delta_sync_table_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#delta_sync_table_name AppsyncDatasource#delta_sync_table_name}.'''
        result = self._values.get("delta_sync_table_name")
        assert result is not None, "Required property 'delta_sync_table_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def base_table_ttl(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#base_table_ttl AppsyncDatasource#base_table_ttl}.'''
        result = self._values.get("base_table_ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def delta_sync_table_ttl(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#delta_sync_table_ttl AppsyncDatasource#delta_sync_table_ttl}.'''
        result = self._values.get("delta_sync_table_ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncDatasourceDynamodbConfigDeltaSyncConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppsyncDatasourceDynamodbConfigDeltaSyncConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appsyncDatasource.AppsyncDatasourceDynamodbConfigDeltaSyncConfigOutputReference",
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

    @jsii.member(jsii_name="resetBaseTableTtl")
    def reset_base_table_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBaseTableTtl", []))

    @jsii.member(jsii_name="resetDeltaSyncTableTtl")
    def reset_delta_sync_table_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeltaSyncTableTtl", []))

    @builtins.property
    @jsii.member(jsii_name="baseTableTtlInput")
    def base_table_ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "baseTableTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="deltaSyncTableNameInput")
    def delta_sync_table_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deltaSyncTableNameInput"))

    @builtins.property
    @jsii.member(jsii_name="deltaSyncTableTtlInput")
    def delta_sync_table_ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "deltaSyncTableTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="baseTableTtl")
    def base_table_ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "baseTableTtl"))

    @base_table_ttl.setter
    def base_table_ttl(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "baseTableTtl", value)

    @builtins.property
    @jsii.member(jsii_name="deltaSyncTableName")
    def delta_sync_table_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deltaSyncTableName"))

    @delta_sync_table_name.setter
    def delta_sync_table_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deltaSyncTableName", value)

    @builtins.property
    @jsii.member(jsii_name="deltaSyncTableTtl")
    def delta_sync_table_ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "deltaSyncTableTtl"))

    @delta_sync_table_ttl.setter
    def delta_sync_table_ttl(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deltaSyncTableTtl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppsyncDatasourceDynamodbConfigDeltaSyncConfig]:
        return typing.cast(typing.Optional[AppsyncDatasourceDynamodbConfigDeltaSyncConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppsyncDatasourceDynamodbConfigDeltaSyncConfig],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppsyncDatasourceDynamodbConfigDeltaSyncConfig],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppsyncDatasourceDynamodbConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appsyncDatasource.AppsyncDatasourceDynamodbConfigOutputReference",
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

    @jsii.member(jsii_name="putDeltaSyncConfig")
    def put_delta_sync_config(
        self,
        *,
        delta_sync_table_name: builtins.str,
        base_table_ttl: typing.Optional[jsii.Number] = None,
        delta_sync_table_ttl: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param delta_sync_table_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#delta_sync_table_name AppsyncDatasource#delta_sync_table_name}.
        :param base_table_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#base_table_ttl AppsyncDatasource#base_table_ttl}.
        :param delta_sync_table_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#delta_sync_table_ttl AppsyncDatasource#delta_sync_table_ttl}.
        '''
        value = AppsyncDatasourceDynamodbConfigDeltaSyncConfig(
            delta_sync_table_name=delta_sync_table_name,
            base_table_ttl=base_table_ttl,
            delta_sync_table_ttl=delta_sync_table_ttl,
        )

        return typing.cast(None, jsii.invoke(self, "putDeltaSyncConfig", [value]))

    @jsii.member(jsii_name="resetDeltaSyncConfig")
    def reset_delta_sync_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeltaSyncConfig", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @jsii.member(jsii_name="resetUseCallerCredentials")
    def reset_use_caller_credentials(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseCallerCredentials", []))

    @jsii.member(jsii_name="resetVersioned")
    def reset_versioned(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersioned", []))

    @builtins.property
    @jsii.member(jsii_name="deltaSyncConfig")
    def delta_sync_config(
        self,
    ) -> AppsyncDatasourceDynamodbConfigDeltaSyncConfigOutputReference:
        return typing.cast(AppsyncDatasourceDynamodbConfigDeltaSyncConfigOutputReference, jsii.get(self, "deltaSyncConfig"))

    @builtins.property
    @jsii.member(jsii_name="deltaSyncConfigInput")
    def delta_sync_config_input(
        self,
    ) -> typing.Optional[AppsyncDatasourceDynamodbConfigDeltaSyncConfig]:
        return typing.cast(typing.Optional[AppsyncDatasourceDynamodbConfigDeltaSyncConfig], jsii.get(self, "deltaSyncConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="tableNameInput")
    def table_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tableNameInput"))

    @builtins.property
    @jsii.member(jsii_name="useCallerCredentialsInput")
    def use_caller_credentials_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "useCallerCredentialsInput"))

    @builtins.property
    @jsii.member(jsii_name="versionedInput")
    def versioned_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "versionedInput"))

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

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
    @jsii.member(jsii_name="useCallerCredentials")
    def use_caller_credentials(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "useCallerCredentials"))

    @use_caller_credentials.setter
    def use_caller_credentials(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useCallerCredentials", value)

    @builtins.property
    @jsii.member(jsii_name="versioned")
    def versioned(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "versioned"))

    @versioned.setter
    def versioned(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "versioned", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppsyncDatasourceDynamodbConfig]:
        return typing.cast(typing.Optional[AppsyncDatasourceDynamodbConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppsyncDatasourceDynamodbConfig],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[AppsyncDatasourceDynamodbConfig]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appsyncDatasource.AppsyncDatasourceElasticsearchConfig",
    jsii_struct_bases=[],
    name_mapping={"endpoint": "endpoint", "region": "region"},
)
class AppsyncDatasourceElasticsearchConfig:
    def __init__(
        self,
        *,
        endpoint: builtins.str,
        region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#endpoint AppsyncDatasource#endpoint}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#region AppsyncDatasource#region}.
        '''
        if __debug__:
            def stub(
                *,
                endpoint: builtins.str,
                region: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
        self._values: typing.Dict[str, typing.Any] = {
            "endpoint": endpoint,
        }
        if region is not None:
            self._values["region"] = region

    @builtins.property
    def endpoint(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#endpoint AppsyncDatasource#endpoint}.'''
        result = self._values.get("endpoint")
        assert result is not None, "Required property 'endpoint' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#region AppsyncDatasource#region}.'''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncDatasourceElasticsearchConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppsyncDatasourceElasticsearchConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appsyncDatasource.AppsyncDatasourceElasticsearchConfigOutputReference",
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

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @builtins.property
    @jsii.member(jsii_name="endpointInput")
    def endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="endpoint")
    def endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpoint"))

    @endpoint.setter
    def endpoint(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpoint", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppsyncDatasourceElasticsearchConfig]:
        return typing.cast(typing.Optional[AppsyncDatasourceElasticsearchConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppsyncDatasourceElasticsearchConfig],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppsyncDatasourceElasticsearchConfig],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appsyncDatasource.AppsyncDatasourceHttpConfig",
    jsii_struct_bases=[],
    name_mapping={
        "endpoint": "endpoint",
        "authorization_config": "authorizationConfig",
    },
)
class AppsyncDatasourceHttpConfig:
    def __init__(
        self,
        *,
        endpoint: builtins.str,
        authorization_config: typing.Optional[typing.Union["AppsyncDatasourceHttpConfigAuthorizationConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#endpoint AppsyncDatasource#endpoint}.
        :param authorization_config: authorization_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#authorization_config AppsyncDatasource#authorization_config}
        '''
        if isinstance(authorization_config, dict):
            authorization_config = AppsyncDatasourceHttpConfigAuthorizationConfig(**authorization_config)
        if __debug__:
            def stub(
                *,
                endpoint: builtins.str,
                authorization_config: typing.Optional[typing.Union[AppsyncDatasourceHttpConfigAuthorizationConfig, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
            check_type(argname="argument authorization_config", value=authorization_config, expected_type=type_hints["authorization_config"])
        self._values: typing.Dict[str, typing.Any] = {
            "endpoint": endpoint,
        }
        if authorization_config is not None:
            self._values["authorization_config"] = authorization_config

    @builtins.property
    def endpoint(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#endpoint AppsyncDatasource#endpoint}.'''
        result = self._values.get("endpoint")
        assert result is not None, "Required property 'endpoint' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def authorization_config(
        self,
    ) -> typing.Optional["AppsyncDatasourceHttpConfigAuthorizationConfig"]:
        '''authorization_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#authorization_config AppsyncDatasource#authorization_config}
        '''
        result = self._values.get("authorization_config")
        return typing.cast(typing.Optional["AppsyncDatasourceHttpConfigAuthorizationConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncDatasourceHttpConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appsyncDatasource.AppsyncDatasourceHttpConfigAuthorizationConfig",
    jsii_struct_bases=[],
    name_mapping={
        "authorization_type": "authorizationType",
        "aws_iam_config": "awsIamConfig",
    },
)
class AppsyncDatasourceHttpConfigAuthorizationConfig:
    def __init__(
        self,
        *,
        authorization_type: typing.Optional[builtins.str] = None,
        aws_iam_config: typing.Optional[typing.Union["AppsyncDatasourceHttpConfigAuthorizationConfigAwsIamConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param authorization_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#authorization_type AppsyncDatasource#authorization_type}.
        :param aws_iam_config: aws_iam_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#aws_iam_config AppsyncDatasource#aws_iam_config}
        '''
        if isinstance(aws_iam_config, dict):
            aws_iam_config = AppsyncDatasourceHttpConfigAuthorizationConfigAwsIamConfig(**aws_iam_config)
        if __debug__:
            def stub(
                *,
                authorization_type: typing.Optional[builtins.str] = None,
                aws_iam_config: typing.Optional[typing.Union[AppsyncDatasourceHttpConfigAuthorizationConfigAwsIamConfig, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument authorization_type", value=authorization_type, expected_type=type_hints["authorization_type"])
            check_type(argname="argument aws_iam_config", value=aws_iam_config, expected_type=type_hints["aws_iam_config"])
        self._values: typing.Dict[str, typing.Any] = {}
        if authorization_type is not None:
            self._values["authorization_type"] = authorization_type
        if aws_iam_config is not None:
            self._values["aws_iam_config"] = aws_iam_config

    @builtins.property
    def authorization_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#authorization_type AppsyncDatasource#authorization_type}.'''
        result = self._values.get("authorization_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def aws_iam_config(
        self,
    ) -> typing.Optional["AppsyncDatasourceHttpConfigAuthorizationConfigAwsIamConfig"]:
        '''aws_iam_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#aws_iam_config AppsyncDatasource#aws_iam_config}
        '''
        result = self._values.get("aws_iam_config")
        return typing.cast(typing.Optional["AppsyncDatasourceHttpConfigAuthorizationConfigAwsIamConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncDatasourceHttpConfigAuthorizationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appsyncDatasource.AppsyncDatasourceHttpConfigAuthorizationConfigAwsIamConfig",
    jsii_struct_bases=[],
    name_mapping={
        "signing_region": "signingRegion",
        "signing_service_name": "signingServiceName",
    },
)
class AppsyncDatasourceHttpConfigAuthorizationConfigAwsIamConfig:
    def __init__(
        self,
        *,
        signing_region: typing.Optional[builtins.str] = None,
        signing_service_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param signing_region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#signing_region AppsyncDatasource#signing_region}.
        :param signing_service_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#signing_service_name AppsyncDatasource#signing_service_name}.
        '''
        if __debug__:
            def stub(
                *,
                signing_region: typing.Optional[builtins.str] = None,
                signing_service_name: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument signing_region", value=signing_region, expected_type=type_hints["signing_region"])
            check_type(argname="argument signing_service_name", value=signing_service_name, expected_type=type_hints["signing_service_name"])
        self._values: typing.Dict[str, typing.Any] = {}
        if signing_region is not None:
            self._values["signing_region"] = signing_region
        if signing_service_name is not None:
            self._values["signing_service_name"] = signing_service_name

    @builtins.property
    def signing_region(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#signing_region AppsyncDatasource#signing_region}.'''
        result = self._values.get("signing_region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def signing_service_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#signing_service_name AppsyncDatasource#signing_service_name}.'''
        result = self._values.get("signing_service_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncDatasourceHttpConfigAuthorizationConfigAwsIamConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppsyncDatasourceHttpConfigAuthorizationConfigAwsIamConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appsyncDatasource.AppsyncDatasourceHttpConfigAuthorizationConfigAwsIamConfigOutputReference",
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

    @jsii.member(jsii_name="resetSigningRegion")
    def reset_signing_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSigningRegion", []))

    @jsii.member(jsii_name="resetSigningServiceName")
    def reset_signing_service_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSigningServiceName", []))

    @builtins.property
    @jsii.member(jsii_name="signingRegionInput")
    def signing_region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "signingRegionInput"))

    @builtins.property
    @jsii.member(jsii_name="signingServiceNameInput")
    def signing_service_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "signingServiceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="signingRegion")
    def signing_region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "signingRegion"))

    @signing_region.setter
    def signing_region(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "signingRegion", value)

    @builtins.property
    @jsii.member(jsii_name="signingServiceName")
    def signing_service_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "signingServiceName"))

    @signing_service_name.setter
    def signing_service_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "signingServiceName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppsyncDatasourceHttpConfigAuthorizationConfigAwsIamConfig]:
        return typing.cast(typing.Optional[AppsyncDatasourceHttpConfigAuthorizationConfigAwsIamConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppsyncDatasourceHttpConfigAuthorizationConfigAwsIamConfig],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppsyncDatasourceHttpConfigAuthorizationConfigAwsIamConfig],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppsyncDatasourceHttpConfigAuthorizationConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appsyncDatasource.AppsyncDatasourceHttpConfigAuthorizationConfigOutputReference",
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

    @jsii.member(jsii_name="putAwsIamConfig")
    def put_aws_iam_config(
        self,
        *,
        signing_region: typing.Optional[builtins.str] = None,
        signing_service_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param signing_region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#signing_region AppsyncDatasource#signing_region}.
        :param signing_service_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#signing_service_name AppsyncDatasource#signing_service_name}.
        '''
        value = AppsyncDatasourceHttpConfigAuthorizationConfigAwsIamConfig(
            signing_region=signing_region, signing_service_name=signing_service_name
        )

        return typing.cast(None, jsii.invoke(self, "putAwsIamConfig", [value]))

    @jsii.member(jsii_name="resetAuthorizationType")
    def reset_authorization_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthorizationType", []))

    @jsii.member(jsii_name="resetAwsIamConfig")
    def reset_aws_iam_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsIamConfig", []))

    @builtins.property
    @jsii.member(jsii_name="awsIamConfig")
    def aws_iam_config(
        self,
    ) -> AppsyncDatasourceHttpConfigAuthorizationConfigAwsIamConfigOutputReference:
        return typing.cast(AppsyncDatasourceHttpConfigAuthorizationConfigAwsIamConfigOutputReference, jsii.get(self, "awsIamConfig"))

    @builtins.property
    @jsii.member(jsii_name="authorizationTypeInput")
    def authorization_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authorizationTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="awsIamConfigInput")
    def aws_iam_config_input(
        self,
    ) -> typing.Optional[AppsyncDatasourceHttpConfigAuthorizationConfigAwsIamConfig]:
        return typing.cast(typing.Optional[AppsyncDatasourceHttpConfigAuthorizationConfigAwsIamConfig], jsii.get(self, "awsIamConfigInput"))

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
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppsyncDatasourceHttpConfigAuthorizationConfig]:
        return typing.cast(typing.Optional[AppsyncDatasourceHttpConfigAuthorizationConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppsyncDatasourceHttpConfigAuthorizationConfig],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppsyncDatasourceHttpConfigAuthorizationConfig],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppsyncDatasourceHttpConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appsyncDatasource.AppsyncDatasourceHttpConfigOutputReference",
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

    @jsii.member(jsii_name="putAuthorizationConfig")
    def put_authorization_config(
        self,
        *,
        authorization_type: typing.Optional[builtins.str] = None,
        aws_iam_config: typing.Optional[typing.Union[AppsyncDatasourceHttpConfigAuthorizationConfigAwsIamConfig, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param authorization_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#authorization_type AppsyncDatasource#authorization_type}.
        :param aws_iam_config: aws_iam_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#aws_iam_config AppsyncDatasource#aws_iam_config}
        '''
        value = AppsyncDatasourceHttpConfigAuthorizationConfig(
            authorization_type=authorization_type, aws_iam_config=aws_iam_config
        )

        return typing.cast(None, jsii.invoke(self, "putAuthorizationConfig", [value]))

    @jsii.member(jsii_name="resetAuthorizationConfig")
    def reset_authorization_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthorizationConfig", []))

    @builtins.property
    @jsii.member(jsii_name="authorizationConfig")
    def authorization_config(
        self,
    ) -> AppsyncDatasourceHttpConfigAuthorizationConfigOutputReference:
        return typing.cast(AppsyncDatasourceHttpConfigAuthorizationConfigOutputReference, jsii.get(self, "authorizationConfig"))

    @builtins.property
    @jsii.member(jsii_name="authorizationConfigInput")
    def authorization_config_input(
        self,
    ) -> typing.Optional[AppsyncDatasourceHttpConfigAuthorizationConfig]:
        return typing.cast(typing.Optional[AppsyncDatasourceHttpConfigAuthorizationConfig], jsii.get(self, "authorizationConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointInput")
    def endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointInput"))

    @builtins.property
    @jsii.member(jsii_name="endpoint")
    def endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpoint"))

    @endpoint.setter
    def endpoint(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpoint", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppsyncDatasourceHttpConfig]:
        return typing.cast(typing.Optional[AppsyncDatasourceHttpConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppsyncDatasourceHttpConfig],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[AppsyncDatasourceHttpConfig]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appsyncDatasource.AppsyncDatasourceLambdaConfig",
    jsii_struct_bases=[],
    name_mapping={"function_arn": "functionArn"},
)
class AppsyncDatasourceLambdaConfig:
    def __init__(self, *, function_arn: builtins.str) -> None:
        '''
        :param function_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#function_arn AppsyncDatasource#function_arn}.
        '''
        if __debug__:
            def stub(*, function_arn: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument function_arn", value=function_arn, expected_type=type_hints["function_arn"])
        self._values: typing.Dict[str, typing.Any] = {
            "function_arn": function_arn,
        }

    @builtins.property
    def function_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#function_arn AppsyncDatasource#function_arn}.'''
        result = self._values.get("function_arn")
        assert result is not None, "Required property 'function_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncDatasourceLambdaConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppsyncDatasourceLambdaConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appsyncDatasource.AppsyncDatasourceLambdaConfigOutputReference",
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
    @jsii.member(jsii_name="functionArnInput")
    def function_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "functionArnInput"))

    @builtins.property
    @jsii.member(jsii_name="functionArn")
    def function_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "functionArn"))

    @function_arn.setter
    def function_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "functionArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppsyncDatasourceLambdaConfig]:
        return typing.cast(typing.Optional[AppsyncDatasourceLambdaConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppsyncDatasourceLambdaConfig],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[AppsyncDatasourceLambdaConfig]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appsyncDatasource.AppsyncDatasourceRelationalDatabaseConfig",
    jsii_struct_bases=[],
    name_mapping={
        "http_endpoint_config": "httpEndpointConfig",
        "source_type": "sourceType",
    },
)
class AppsyncDatasourceRelationalDatabaseConfig:
    def __init__(
        self,
        *,
        http_endpoint_config: typing.Optional[typing.Union["AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfig", typing.Dict[str, typing.Any]]] = None,
        source_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param http_endpoint_config: http_endpoint_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#http_endpoint_config AppsyncDatasource#http_endpoint_config}
        :param source_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#source_type AppsyncDatasource#source_type}.
        '''
        if isinstance(http_endpoint_config, dict):
            http_endpoint_config = AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfig(**http_endpoint_config)
        if __debug__:
            def stub(
                *,
                http_endpoint_config: typing.Optional[typing.Union[AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfig, typing.Dict[str, typing.Any]]] = None,
                source_type: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument http_endpoint_config", value=http_endpoint_config, expected_type=type_hints["http_endpoint_config"])
            check_type(argname="argument source_type", value=source_type, expected_type=type_hints["source_type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if http_endpoint_config is not None:
            self._values["http_endpoint_config"] = http_endpoint_config
        if source_type is not None:
            self._values["source_type"] = source_type

    @builtins.property
    def http_endpoint_config(
        self,
    ) -> typing.Optional["AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfig"]:
        '''http_endpoint_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#http_endpoint_config AppsyncDatasource#http_endpoint_config}
        '''
        result = self._values.get("http_endpoint_config")
        return typing.cast(typing.Optional["AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfig"], result)

    @builtins.property
    def source_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#source_type AppsyncDatasource#source_type}.'''
        result = self._values.get("source_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncDatasourceRelationalDatabaseConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appsyncDatasource.AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfig",
    jsii_struct_bases=[],
    name_mapping={
        "aws_secret_store_arn": "awsSecretStoreArn",
        "db_cluster_identifier": "dbClusterIdentifier",
        "database_name": "databaseName",
        "region": "region",
        "schema": "schema",
    },
)
class AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfig:
    def __init__(
        self,
        *,
        aws_secret_store_arn: builtins.str,
        db_cluster_identifier: builtins.str,
        database_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        schema: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_secret_store_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#aws_secret_store_arn AppsyncDatasource#aws_secret_store_arn}.
        :param db_cluster_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#db_cluster_identifier AppsyncDatasource#db_cluster_identifier}.
        :param database_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#database_name AppsyncDatasource#database_name}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#region AppsyncDatasource#region}.
        :param schema: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#schema AppsyncDatasource#schema}.
        '''
        if __debug__:
            def stub(
                *,
                aws_secret_store_arn: builtins.str,
                db_cluster_identifier: builtins.str,
                database_name: typing.Optional[builtins.str] = None,
                region: typing.Optional[builtins.str] = None,
                schema: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument aws_secret_store_arn", value=aws_secret_store_arn, expected_type=type_hints["aws_secret_store_arn"])
            check_type(argname="argument db_cluster_identifier", value=db_cluster_identifier, expected_type=type_hints["db_cluster_identifier"])
            check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument schema", value=schema, expected_type=type_hints["schema"])
        self._values: typing.Dict[str, typing.Any] = {
            "aws_secret_store_arn": aws_secret_store_arn,
            "db_cluster_identifier": db_cluster_identifier,
        }
        if database_name is not None:
            self._values["database_name"] = database_name
        if region is not None:
            self._values["region"] = region
        if schema is not None:
            self._values["schema"] = schema

    @builtins.property
    def aws_secret_store_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#aws_secret_store_arn AppsyncDatasource#aws_secret_store_arn}.'''
        result = self._values.get("aws_secret_store_arn")
        assert result is not None, "Required property 'aws_secret_store_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def db_cluster_identifier(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#db_cluster_identifier AppsyncDatasource#db_cluster_identifier}.'''
        result = self._values.get("db_cluster_identifier")
        assert result is not None, "Required property 'db_cluster_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def database_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#database_name AppsyncDatasource#database_name}.'''
        result = self._values.get("database_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#region AppsyncDatasource#region}.'''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def schema(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#schema AppsyncDatasource#schema}.'''
        result = self._values.get("schema")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appsyncDatasource.AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfigOutputReference",
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

    @jsii.member(jsii_name="resetDatabaseName")
    def reset_database_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatabaseName", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @jsii.member(jsii_name="resetSchema")
    def reset_schema(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchema", []))

    @builtins.property
    @jsii.member(jsii_name="awsSecretStoreArnInput")
    def aws_secret_store_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "awsSecretStoreArnInput"))

    @builtins.property
    @jsii.member(jsii_name="databaseNameInput")
    def database_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseNameInput"))

    @builtins.property
    @jsii.member(jsii_name="dbClusterIdentifierInput")
    def db_cluster_identifier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dbClusterIdentifierInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="schemaInput")
    def schema_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schemaInput"))

    @builtins.property
    @jsii.member(jsii_name="awsSecretStoreArn")
    def aws_secret_store_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "awsSecretStoreArn"))

    @aws_secret_store_arn.setter
    def aws_secret_store_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsSecretStoreArn", value)

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
    @jsii.member(jsii_name="dbClusterIdentifier")
    def db_cluster_identifier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dbClusterIdentifier"))

    @db_cluster_identifier.setter
    def db_cluster_identifier(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dbClusterIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="schema")
    def schema(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schema"))

    @schema.setter
    def schema(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schema", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfig]:
        return typing.cast(typing.Optional[AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfig],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfig],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppsyncDatasourceRelationalDatabaseConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appsyncDatasource.AppsyncDatasourceRelationalDatabaseConfigOutputReference",
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

    @jsii.member(jsii_name="putHttpEndpointConfig")
    def put_http_endpoint_config(
        self,
        *,
        aws_secret_store_arn: builtins.str,
        db_cluster_identifier: builtins.str,
        database_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        schema: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_secret_store_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#aws_secret_store_arn AppsyncDatasource#aws_secret_store_arn}.
        :param db_cluster_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#db_cluster_identifier AppsyncDatasource#db_cluster_identifier}.
        :param database_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#database_name AppsyncDatasource#database_name}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#region AppsyncDatasource#region}.
        :param schema: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appsync_datasource#schema AppsyncDatasource#schema}.
        '''
        value = AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfig(
            aws_secret_store_arn=aws_secret_store_arn,
            db_cluster_identifier=db_cluster_identifier,
            database_name=database_name,
            region=region,
            schema=schema,
        )

        return typing.cast(None, jsii.invoke(self, "putHttpEndpointConfig", [value]))

    @jsii.member(jsii_name="resetHttpEndpointConfig")
    def reset_http_endpoint_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpEndpointConfig", []))

    @jsii.member(jsii_name="resetSourceType")
    def reset_source_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceType", []))

    @builtins.property
    @jsii.member(jsii_name="httpEndpointConfig")
    def http_endpoint_config(
        self,
    ) -> AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfigOutputReference:
        return typing.cast(AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfigOutputReference, jsii.get(self, "httpEndpointConfig"))

    @builtins.property
    @jsii.member(jsii_name="httpEndpointConfigInput")
    def http_endpoint_config_input(
        self,
    ) -> typing.Optional[AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfig]:
        return typing.cast(typing.Optional[AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfig], jsii.get(self, "httpEndpointConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceTypeInput")
    def source_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceType")
    def source_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceType"))

    @source_type.setter
    def source_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppsyncDatasourceRelationalDatabaseConfig]:
        return typing.cast(typing.Optional[AppsyncDatasourceRelationalDatabaseConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppsyncDatasourceRelationalDatabaseConfig],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppsyncDatasourceRelationalDatabaseConfig],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "AppsyncDatasource",
    "AppsyncDatasourceConfig",
    "AppsyncDatasourceDynamodbConfig",
    "AppsyncDatasourceDynamodbConfigDeltaSyncConfig",
    "AppsyncDatasourceDynamodbConfigDeltaSyncConfigOutputReference",
    "AppsyncDatasourceDynamodbConfigOutputReference",
    "AppsyncDatasourceElasticsearchConfig",
    "AppsyncDatasourceElasticsearchConfigOutputReference",
    "AppsyncDatasourceHttpConfig",
    "AppsyncDatasourceHttpConfigAuthorizationConfig",
    "AppsyncDatasourceHttpConfigAuthorizationConfigAwsIamConfig",
    "AppsyncDatasourceHttpConfigAuthorizationConfigAwsIamConfigOutputReference",
    "AppsyncDatasourceHttpConfigAuthorizationConfigOutputReference",
    "AppsyncDatasourceHttpConfigOutputReference",
    "AppsyncDatasourceLambdaConfig",
    "AppsyncDatasourceLambdaConfigOutputReference",
    "AppsyncDatasourceRelationalDatabaseConfig",
    "AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfig",
    "AppsyncDatasourceRelationalDatabaseConfigHttpEndpointConfigOutputReference",
    "AppsyncDatasourceRelationalDatabaseConfigOutputReference",
]

publication.publish()
