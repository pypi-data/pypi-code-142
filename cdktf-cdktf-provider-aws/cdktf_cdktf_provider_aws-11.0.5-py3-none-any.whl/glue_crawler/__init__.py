'''
# `aws_glue_crawler`

Refer to the Terraform Registory for docs: [`aws_glue_crawler`](https://www.terraform.io/docs/providers/aws/r/glue_crawler).
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


class GlueCrawler(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.glueCrawler.GlueCrawler",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler aws_glue_crawler}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        database_name: builtins.str,
        name: builtins.str,
        role: builtins.str,
        catalog_target: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GlueCrawlerCatalogTarget", typing.Dict[str, typing.Any]]]]] = None,
        classifiers: typing.Optional[typing.Sequence[builtins.str]] = None,
        configuration: typing.Optional[builtins.str] = None,
        delta_target: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GlueCrawlerDeltaTarget", typing.Dict[str, typing.Any]]]]] = None,
        description: typing.Optional[builtins.str] = None,
        dynamodb_target: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GlueCrawlerDynamodbTarget", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        jdbc_target: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GlueCrawlerJdbcTarget", typing.Dict[str, typing.Any]]]]] = None,
        lineage_configuration: typing.Optional[typing.Union["GlueCrawlerLineageConfiguration", typing.Dict[str, typing.Any]]] = None,
        mongodb_target: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GlueCrawlerMongodbTarget", typing.Dict[str, typing.Any]]]]] = None,
        recrawl_policy: typing.Optional[typing.Union["GlueCrawlerRecrawlPolicy", typing.Dict[str, typing.Any]]] = None,
        s3_target: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GlueCrawlerS3Target", typing.Dict[str, typing.Any]]]]] = None,
        schedule: typing.Optional[builtins.str] = None,
        schema_change_policy: typing.Optional[typing.Union["GlueCrawlerSchemaChangePolicy", typing.Dict[str, typing.Any]]] = None,
        security_configuration: typing.Optional[builtins.str] = None,
        table_prefix: typing.Optional[builtins.str] = None,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler aws_glue_crawler} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param database_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#database_name GlueCrawler#database_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#name GlueCrawler#name}.
        :param role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#role GlueCrawler#role}.
        :param catalog_target: catalog_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#catalog_target GlueCrawler#catalog_target}
        :param classifiers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#classifiers GlueCrawler#classifiers}.
        :param configuration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#configuration GlueCrawler#configuration}.
        :param delta_target: delta_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#delta_target GlueCrawler#delta_target}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#description GlueCrawler#description}.
        :param dynamodb_target: dynamodb_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#dynamodb_target GlueCrawler#dynamodb_target}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#id GlueCrawler#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param jdbc_target: jdbc_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#jdbc_target GlueCrawler#jdbc_target}
        :param lineage_configuration: lineage_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#lineage_configuration GlueCrawler#lineage_configuration}
        :param mongodb_target: mongodb_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#mongodb_target GlueCrawler#mongodb_target}
        :param recrawl_policy: recrawl_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#recrawl_policy GlueCrawler#recrawl_policy}
        :param s3_target: s3_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#s3_target GlueCrawler#s3_target}
        :param schedule: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#schedule GlueCrawler#schedule}.
        :param schema_change_policy: schema_change_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#schema_change_policy GlueCrawler#schema_change_policy}
        :param security_configuration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#security_configuration GlueCrawler#security_configuration}.
        :param table_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#table_prefix GlueCrawler#table_prefix}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#tags GlueCrawler#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#tags_all GlueCrawler#tags_all}.
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
                database_name: builtins.str,
                name: builtins.str,
                role: builtins.str,
                catalog_target: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GlueCrawlerCatalogTarget, typing.Dict[str, typing.Any]]]]] = None,
                classifiers: typing.Optional[typing.Sequence[builtins.str]] = None,
                configuration: typing.Optional[builtins.str] = None,
                delta_target: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GlueCrawlerDeltaTarget, typing.Dict[str, typing.Any]]]]] = None,
                description: typing.Optional[builtins.str] = None,
                dynamodb_target: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GlueCrawlerDynamodbTarget, typing.Dict[str, typing.Any]]]]] = None,
                id: typing.Optional[builtins.str] = None,
                jdbc_target: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GlueCrawlerJdbcTarget, typing.Dict[str, typing.Any]]]]] = None,
                lineage_configuration: typing.Optional[typing.Union[GlueCrawlerLineageConfiguration, typing.Dict[str, typing.Any]]] = None,
                mongodb_target: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GlueCrawlerMongodbTarget, typing.Dict[str, typing.Any]]]]] = None,
                recrawl_policy: typing.Optional[typing.Union[GlueCrawlerRecrawlPolicy, typing.Dict[str, typing.Any]]] = None,
                s3_target: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GlueCrawlerS3Target, typing.Dict[str, typing.Any]]]]] = None,
                schedule: typing.Optional[builtins.str] = None,
                schema_change_policy: typing.Optional[typing.Union[GlueCrawlerSchemaChangePolicy, typing.Dict[str, typing.Any]]] = None,
                security_configuration: typing.Optional[builtins.str] = None,
                table_prefix: typing.Optional[builtins.str] = None,
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
        config = GlueCrawlerConfig(
            database_name=database_name,
            name=name,
            role=role,
            catalog_target=catalog_target,
            classifiers=classifiers,
            configuration=configuration,
            delta_target=delta_target,
            description=description,
            dynamodb_target=dynamodb_target,
            id=id,
            jdbc_target=jdbc_target,
            lineage_configuration=lineage_configuration,
            mongodb_target=mongodb_target,
            recrawl_policy=recrawl_policy,
            s3_target=s3_target,
            schedule=schedule,
            schema_change_policy=schema_change_policy,
            security_configuration=security_configuration,
            table_prefix=table_prefix,
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

    @jsii.member(jsii_name="putCatalogTarget")
    def put_catalog_target(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GlueCrawlerCatalogTarget", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GlueCrawlerCatalogTarget, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCatalogTarget", [value]))

    @jsii.member(jsii_name="putDeltaTarget")
    def put_delta_target(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GlueCrawlerDeltaTarget", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GlueCrawlerDeltaTarget, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDeltaTarget", [value]))

    @jsii.member(jsii_name="putDynamodbTarget")
    def put_dynamodb_target(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GlueCrawlerDynamodbTarget", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GlueCrawlerDynamodbTarget, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDynamodbTarget", [value]))

    @jsii.member(jsii_name="putJdbcTarget")
    def put_jdbc_target(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GlueCrawlerJdbcTarget", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GlueCrawlerJdbcTarget, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putJdbcTarget", [value]))

    @jsii.member(jsii_name="putLineageConfiguration")
    def put_lineage_configuration(
        self,
        *,
        crawler_lineage_settings: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param crawler_lineage_settings: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#crawler_lineage_settings GlueCrawler#crawler_lineage_settings}.
        '''
        value = GlueCrawlerLineageConfiguration(
            crawler_lineage_settings=crawler_lineage_settings
        )

        return typing.cast(None, jsii.invoke(self, "putLineageConfiguration", [value]))

    @jsii.member(jsii_name="putMongodbTarget")
    def put_mongodb_target(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GlueCrawlerMongodbTarget", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GlueCrawlerMongodbTarget, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMongodbTarget", [value]))

    @jsii.member(jsii_name="putRecrawlPolicy")
    def put_recrawl_policy(
        self,
        *,
        recrawl_behavior: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param recrawl_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#recrawl_behavior GlueCrawler#recrawl_behavior}.
        '''
        value = GlueCrawlerRecrawlPolicy(recrawl_behavior=recrawl_behavior)

        return typing.cast(None, jsii.invoke(self, "putRecrawlPolicy", [value]))

    @jsii.member(jsii_name="putS3Target")
    def put_s3_target(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GlueCrawlerS3Target", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GlueCrawlerS3Target, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putS3Target", [value]))

    @jsii.member(jsii_name="putSchemaChangePolicy")
    def put_schema_change_policy(
        self,
        *,
        delete_behavior: typing.Optional[builtins.str] = None,
        update_behavior: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param delete_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#delete_behavior GlueCrawler#delete_behavior}.
        :param update_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#update_behavior GlueCrawler#update_behavior}.
        '''
        value = GlueCrawlerSchemaChangePolicy(
            delete_behavior=delete_behavior, update_behavior=update_behavior
        )

        return typing.cast(None, jsii.invoke(self, "putSchemaChangePolicy", [value]))

    @jsii.member(jsii_name="resetCatalogTarget")
    def reset_catalog_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCatalogTarget", []))

    @jsii.member(jsii_name="resetClassifiers")
    def reset_classifiers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClassifiers", []))

    @jsii.member(jsii_name="resetConfiguration")
    def reset_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfiguration", []))

    @jsii.member(jsii_name="resetDeltaTarget")
    def reset_delta_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeltaTarget", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDynamodbTarget")
    def reset_dynamodb_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDynamodbTarget", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetJdbcTarget")
    def reset_jdbc_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJdbcTarget", []))

    @jsii.member(jsii_name="resetLineageConfiguration")
    def reset_lineage_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLineageConfiguration", []))

    @jsii.member(jsii_name="resetMongodbTarget")
    def reset_mongodb_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMongodbTarget", []))

    @jsii.member(jsii_name="resetRecrawlPolicy")
    def reset_recrawl_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRecrawlPolicy", []))

    @jsii.member(jsii_name="resetS3Target")
    def reset_s3_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3Target", []))

    @jsii.member(jsii_name="resetSchedule")
    def reset_schedule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchedule", []))

    @jsii.member(jsii_name="resetSchemaChangePolicy")
    def reset_schema_change_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchemaChangePolicy", []))

    @jsii.member(jsii_name="resetSecurityConfiguration")
    def reset_security_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurityConfiguration", []))

    @jsii.member(jsii_name="resetTablePrefix")
    def reset_table_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTablePrefix", []))

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
    @jsii.member(jsii_name="catalogTarget")
    def catalog_target(self) -> "GlueCrawlerCatalogTargetList":
        return typing.cast("GlueCrawlerCatalogTargetList", jsii.get(self, "catalogTarget"))

    @builtins.property
    @jsii.member(jsii_name="deltaTarget")
    def delta_target(self) -> "GlueCrawlerDeltaTargetList":
        return typing.cast("GlueCrawlerDeltaTargetList", jsii.get(self, "deltaTarget"))

    @builtins.property
    @jsii.member(jsii_name="dynamodbTarget")
    def dynamodb_target(self) -> "GlueCrawlerDynamodbTargetList":
        return typing.cast("GlueCrawlerDynamodbTargetList", jsii.get(self, "dynamodbTarget"))

    @builtins.property
    @jsii.member(jsii_name="jdbcTarget")
    def jdbc_target(self) -> "GlueCrawlerJdbcTargetList":
        return typing.cast("GlueCrawlerJdbcTargetList", jsii.get(self, "jdbcTarget"))

    @builtins.property
    @jsii.member(jsii_name="lineageConfiguration")
    def lineage_configuration(self) -> "GlueCrawlerLineageConfigurationOutputReference":
        return typing.cast("GlueCrawlerLineageConfigurationOutputReference", jsii.get(self, "lineageConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="mongodbTarget")
    def mongodb_target(self) -> "GlueCrawlerMongodbTargetList":
        return typing.cast("GlueCrawlerMongodbTargetList", jsii.get(self, "mongodbTarget"))

    @builtins.property
    @jsii.member(jsii_name="recrawlPolicy")
    def recrawl_policy(self) -> "GlueCrawlerRecrawlPolicyOutputReference":
        return typing.cast("GlueCrawlerRecrawlPolicyOutputReference", jsii.get(self, "recrawlPolicy"))

    @builtins.property
    @jsii.member(jsii_name="s3Target")
    def s3_target(self) -> "GlueCrawlerS3TargetList":
        return typing.cast("GlueCrawlerS3TargetList", jsii.get(self, "s3Target"))

    @builtins.property
    @jsii.member(jsii_name="schemaChangePolicy")
    def schema_change_policy(self) -> "GlueCrawlerSchemaChangePolicyOutputReference":
        return typing.cast("GlueCrawlerSchemaChangePolicyOutputReference", jsii.get(self, "schemaChangePolicy"))

    @builtins.property
    @jsii.member(jsii_name="catalogTargetInput")
    def catalog_target_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GlueCrawlerCatalogTarget"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GlueCrawlerCatalogTarget"]]], jsii.get(self, "catalogTargetInput"))

    @builtins.property
    @jsii.member(jsii_name="classifiersInput")
    def classifiers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "classifiersInput"))

    @builtins.property
    @jsii.member(jsii_name="configurationInput")
    def configuration_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "configurationInput"))

    @builtins.property
    @jsii.member(jsii_name="databaseNameInput")
    def database_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseNameInput"))

    @builtins.property
    @jsii.member(jsii_name="deltaTargetInput")
    def delta_target_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GlueCrawlerDeltaTarget"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GlueCrawlerDeltaTarget"]]], jsii.get(self, "deltaTargetInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="dynamodbTargetInput")
    def dynamodb_target_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GlueCrawlerDynamodbTarget"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GlueCrawlerDynamodbTarget"]]], jsii.get(self, "dynamodbTargetInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="jdbcTargetInput")
    def jdbc_target_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GlueCrawlerJdbcTarget"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GlueCrawlerJdbcTarget"]]], jsii.get(self, "jdbcTargetInput"))

    @builtins.property
    @jsii.member(jsii_name="lineageConfigurationInput")
    def lineage_configuration_input(
        self,
    ) -> typing.Optional["GlueCrawlerLineageConfiguration"]:
        return typing.cast(typing.Optional["GlueCrawlerLineageConfiguration"], jsii.get(self, "lineageConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="mongodbTargetInput")
    def mongodb_target_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GlueCrawlerMongodbTarget"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GlueCrawlerMongodbTarget"]]], jsii.get(self, "mongodbTargetInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="recrawlPolicyInput")
    def recrawl_policy_input(self) -> typing.Optional["GlueCrawlerRecrawlPolicy"]:
        return typing.cast(typing.Optional["GlueCrawlerRecrawlPolicy"], jsii.get(self, "recrawlPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="roleInput")
    def role_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleInput"))

    @builtins.property
    @jsii.member(jsii_name="s3TargetInput")
    def s3_target_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GlueCrawlerS3Target"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GlueCrawlerS3Target"]]], jsii.get(self, "s3TargetInput"))

    @builtins.property
    @jsii.member(jsii_name="scheduleInput")
    def schedule_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scheduleInput"))

    @builtins.property
    @jsii.member(jsii_name="schemaChangePolicyInput")
    def schema_change_policy_input(
        self,
    ) -> typing.Optional["GlueCrawlerSchemaChangePolicy"]:
        return typing.cast(typing.Optional["GlueCrawlerSchemaChangePolicy"], jsii.get(self, "schemaChangePolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="securityConfigurationInput")
    def security_configuration_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "securityConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="tablePrefixInput")
    def table_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tablePrefixInput"))

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
    @jsii.member(jsii_name="classifiers")
    def classifiers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "classifiers"))

    @classifiers.setter
    def classifiers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "classifiers", value)

    @builtins.property
    @jsii.member(jsii_name="configuration")
    def configuration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "configuration"))

    @configuration.setter
    def configuration(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configuration", value)

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
    @jsii.member(jsii_name="role")
    def role(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "role"))

    @role.setter
    def role(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "role", value)

    @builtins.property
    @jsii.member(jsii_name="schedule")
    def schedule(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schedule"))

    @schedule.setter
    def schedule(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schedule", value)

    @builtins.property
    @jsii.member(jsii_name="securityConfiguration")
    def security_configuration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "securityConfiguration"))

    @security_configuration.setter
    def security_configuration(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="tablePrefix")
    def table_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tablePrefix"))

    @table_prefix.setter
    def table_prefix(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tablePrefix", value)

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
    jsii_type="@cdktf/provider-aws.glueCrawler.GlueCrawlerCatalogTarget",
    jsii_struct_bases=[],
    name_mapping={"database_name": "databaseName", "tables": "tables"},
)
class GlueCrawlerCatalogTarget:
    def __init__(
        self,
        *,
        database_name: builtins.str,
        tables: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param database_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#database_name GlueCrawler#database_name}.
        :param tables: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#tables GlueCrawler#tables}.
        '''
        if __debug__:
            def stub(
                *,
                database_name: builtins.str,
                tables: typing.Sequence[builtins.str],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
            check_type(argname="argument tables", value=tables, expected_type=type_hints["tables"])
        self._values: typing.Dict[str, typing.Any] = {
            "database_name": database_name,
            "tables": tables,
        }

    @builtins.property
    def database_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#database_name GlueCrawler#database_name}.'''
        result = self._values.get("database_name")
        assert result is not None, "Required property 'database_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tables(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#tables GlueCrawler#tables}.'''
        result = self._values.get("tables")
        assert result is not None, "Required property 'tables' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GlueCrawlerCatalogTarget(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GlueCrawlerCatalogTargetList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.glueCrawler.GlueCrawlerCatalogTargetList",
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
    def get(self, index: jsii.Number) -> "GlueCrawlerCatalogTargetOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GlueCrawlerCatalogTargetOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GlueCrawlerCatalogTarget]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GlueCrawlerCatalogTarget]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GlueCrawlerCatalogTarget]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GlueCrawlerCatalogTarget]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GlueCrawlerCatalogTargetOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.glueCrawler.GlueCrawlerCatalogTargetOutputReference",
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
    @jsii.member(jsii_name="databaseNameInput")
    def database_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseNameInput"))

    @builtins.property
    @jsii.member(jsii_name="tablesInput")
    def tables_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tablesInput"))

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
    @jsii.member(jsii_name="tables")
    def tables(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tables"))

    @tables.setter
    def tables(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tables", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GlueCrawlerCatalogTarget, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GlueCrawlerCatalogTarget, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GlueCrawlerCatalogTarget, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[GlueCrawlerCatalogTarget, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.glueCrawler.GlueCrawlerConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "database_name": "databaseName",
        "name": "name",
        "role": "role",
        "catalog_target": "catalogTarget",
        "classifiers": "classifiers",
        "configuration": "configuration",
        "delta_target": "deltaTarget",
        "description": "description",
        "dynamodb_target": "dynamodbTarget",
        "id": "id",
        "jdbc_target": "jdbcTarget",
        "lineage_configuration": "lineageConfiguration",
        "mongodb_target": "mongodbTarget",
        "recrawl_policy": "recrawlPolicy",
        "s3_target": "s3Target",
        "schedule": "schedule",
        "schema_change_policy": "schemaChangePolicy",
        "security_configuration": "securityConfiguration",
        "table_prefix": "tablePrefix",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class GlueCrawlerConfig(cdktf.TerraformMetaArguments):
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
        database_name: builtins.str,
        name: builtins.str,
        role: builtins.str,
        catalog_target: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GlueCrawlerCatalogTarget, typing.Dict[str, typing.Any]]]]] = None,
        classifiers: typing.Optional[typing.Sequence[builtins.str]] = None,
        configuration: typing.Optional[builtins.str] = None,
        delta_target: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GlueCrawlerDeltaTarget", typing.Dict[str, typing.Any]]]]] = None,
        description: typing.Optional[builtins.str] = None,
        dynamodb_target: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GlueCrawlerDynamodbTarget", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        jdbc_target: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GlueCrawlerJdbcTarget", typing.Dict[str, typing.Any]]]]] = None,
        lineage_configuration: typing.Optional[typing.Union["GlueCrawlerLineageConfiguration", typing.Dict[str, typing.Any]]] = None,
        mongodb_target: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GlueCrawlerMongodbTarget", typing.Dict[str, typing.Any]]]]] = None,
        recrawl_policy: typing.Optional[typing.Union["GlueCrawlerRecrawlPolicy", typing.Dict[str, typing.Any]]] = None,
        s3_target: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GlueCrawlerS3Target", typing.Dict[str, typing.Any]]]]] = None,
        schedule: typing.Optional[builtins.str] = None,
        schema_change_policy: typing.Optional[typing.Union["GlueCrawlerSchemaChangePolicy", typing.Dict[str, typing.Any]]] = None,
        security_configuration: typing.Optional[builtins.str] = None,
        table_prefix: typing.Optional[builtins.str] = None,
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
        :param database_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#database_name GlueCrawler#database_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#name GlueCrawler#name}.
        :param role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#role GlueCrawler#role}.
        :param catalog_target: catalog_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#catalog_target GlueCrawler#catalog_target}
        :param classifiers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#classifiers GlueCrawler#classifiers}.
        :param configuration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#configuration GlueCrawler#configuration}.
        :param delta_target: delta_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#delta_target GlueCrawler#delta_target}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#description GlueCrawler#description}.
        :param dynamodb_target: dynamodb_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#dynamodb_target GlueCrawler#dynamodb_target}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#id GlueCrawler#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param jdbc_target: jdbc_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#jdbc_target GlueCrawler#jdbc_target}
        :param lineage_configuration: lineage_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#lineage_configuration GlueCrawler#lineage_configuration}
        :param mongodb_target: mongodb_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#mongodb_target GlueCrawler#mongodb_target}
        :param recrawl_policy: recrawl_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#recrawl_policy GlueCrawler#recrawl_policy}
        :param s3_target: s3_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#s3_target GlueCrawler#s3_target}
        :param schedule: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#schedule GlueCrawler#schedule}.
        :param schema_change_policy: schema_change_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#schema_change_policy GlueCrawler#schema_change_policy}
        :param security_configuration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#security_configuration GlueCrawler#security_configuration}.
        :param table_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#table_prefix GlueCrawler#table_prefix}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#tags GlueCrawler#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#tags_all GlueCrawler#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(lineage_configuration, dict):
            lineage_configuration = GlueCrawlerLineageConfiguration(**lineage_configuration)
        if isinstance(recrawl_policy, dict):
            recrawl_policy = GlueCrawlerRecrawlPolicy(**recrawl_policy)
        if isinstance(schema_change_policy, dict):
            schema_change_policy = GlueCrawlerSchemaChangePolicy(**schema_change_policy)
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
                database_name: builtins.str,
                name: builtins.str,
                role: builtins.str,
                catalog_target: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GlueCrawlerCatalogTarget, typing.Dict[str, typing.Any]]]]] = None,
                classifiers: typing.Optional[typing.Sequence[builtins.str]] = None,
                configuration: typing.Optional[builtins.str] = None,
                delta_target: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GlueCrawlerDeltaTarget, typing.Dict[str, typing.Any]]]]] = None,
                description: typing.Optional[builtins.str] = None,
                dynamodb_target: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GlueCrawlerDynamodbTarget, typing.Dict[str, typing.Any]]]]] = None,
                id: typing.Optional[builtins.str] = None,
                jdbc_target: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GlueCrawlerJdbcTarget, typing.Dict[str, typing.Any]]]]] = None,
                lineage_configuration: typing.Optional[typing.Union[GlueCrawlerLineageConfiguration, typing.Dict[str, typing.Any]]] = None,
                mongodb_target: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GlueCrawlerMongodbTarget, typing.Dict[str, typing.Any]]]]] = None,
                recrawl_policy: typing.Optional[typing.Union[GlueCrawlerRecrawlPolicy, typing.Dict[str, typing.Any]]] = None,
                s3_target: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GlueCrawlerS3Target, typing.Dict[str, typing.Any]]]]] = None,
                schedule: typing.Optional[builtins.str] = None,
                schema_change_policy: typing.Optional[typing.Union[GlueCrawlerSchemaChangePolicy, typing.Dict[str, typing.Any]]] = None,
                security_configuration: typing.Optional[builtins.str] = None,
                table_prefix: typing.Optional[builtins.str] = None,
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
            check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument catalog_target", value=catalog_target, expected_type=type_hints["catalog_target"])
            check_type(argname="argument classifiers", value=classifiers, expected_type=type_hints["classifiers"])
            check_type(argname="argument configuration", value=configuration, expected_type=type_hints["configuration"])
            check_type(argname="argument delta_target", value=delta_target, expected_type=type_hints["delta_target"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument dynamodb_target", value=dynamodb_target, expected_type=type_hints["dynamodb_target"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument jdbc_target", value=jdbc_target, expected_type=type_hints["jdbc_target"])
            check_type(argname="argument lineage_configuration", value=lineage_configuration, expected_type=type_hints["lineage_configuration"])
            check_type(argname="argument mongodb_target", value=mongodb_target, expected_type=type_hints["mongodb_target"])
            check_type(argname="argument recrawl_policy", value=recrawl_policy, expected_type=type_hints["recrawl_policy"])
            check_type(argname="argument s3_target", value=s3_target, expected_type=type_hints["s3_target"])
            check_type(argname="argument schedule", value=schedule, expected_type=type_hints["schedule"])
            check_type(argname="argument schema_change_policy", value=schema_change_policy, expected_type=type_hints["schema_change_policy"])
            check_type(argname="argument security_configuration", value=security_configuration, expected_type=type_hints["security_configuration"])
            check_type(argname="argument table_prefix", value=table_prefix, expected_type=type_hints["table_prefix"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[str, typing.Any] = {
            "database_name": database_name,
            "name": name,
            "role": role,
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
        if catalog_target is not None:
            self._values["catalog_target"] = catalog_target
        if classifiers is not None:
            self._values["classifiers"] = classifiers
        if configuration is not None:
            self._values["configuration"] = configuration
        if delta_target is not None:
            self._values["delta_target"] = delta_target
        if description is not None:
            self._values["description"] = description
        if dynamodb_target is not None:
            self._values["dynamodb_target"] = dynamodb_target
        if id is not None:
            self._values["id"] = id
        if jdbc_target is not None:
            self._values["jdbc_target"] = jdbc_target
        if lineage_configuration is not None:
            self._values["lineage_configuration"] = lineage_configuration
        if mongodb_target is not None:
            self._values["mongodb_target"] = mongodb_target
        if recrawl_policy is not None:
            self._values["recrawl_policy"] = recrawl_policy
        if s3_target is not None:
            self._values["s3_target"] = s3_target
        if schedule is not None:
            self._values["schedule"] = schedule
        if schema_change_policy is not None:
            self._values["schema_change_policy"] = schema_change_policy
        if security_configuration is not None:
            self._values["security_configuration"] = security_configuration
        if table_prefix is not None:
            self._values["table_prefix"] = table_prefix
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
    def database_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#database_name GlueCrawler#database_name}.'''
        result = self._values.get("database_name")
        assert result is not None, "Required property 'database_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#name GlueCrawler#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#role GlueCrawler#role}.'''
        result = self._values.get("role")
        assert result is not None, "Required property 'role' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def catalog_target(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GlueCrawlerCatalogTarget]]]:
        '''catalog_target block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#catalog_target GlueCrawler#catalog_target}
        '''
        result = self._values.get("catalog_target")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GlueCrawlerCatalogTarget]]], result)

    @builtins.property
    def classifiers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#classifiers GlueCrawler#classifiers}.'''
        result = self._values.get("classifiers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def configuration(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#configuration GlueCrawler#configuration}.'''
        result = self._values.get("configuration")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delta_target(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GlueCrawlerDeltaTarget"]]]:
        '''delta_target block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#delta_target GlueCrawler#delta_target}
        '''
        result = self._values.get("delta_target")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GlueCrawlerDeltaTarget"]]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#description GlueCrawler#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dynamodb_target(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GlueCrawlerDynamodbTarget"]]]:
        '''dynamodb_target block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#dynamodb_target GlueCrawler#dynamodb_target}
        '''
        result = self._values.get("dynamodb_target")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GlueCrawlerDynamodbTarget"]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#id GlueCrawler#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def jdbc_target(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GlueCrawlerJdbcTarget"]]]:
        '''jdbc_target block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#jdbc_target GlueCrawler#jdbc_target}
        '''
        result = self._values.get("jdbc_target")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GlueCrawlerJdbcTarget"]]], result)

    @builtins.property
    def lineage_configuration(
        self,
    ) -> typing.Optional["GlueCrawlerLineageConfiguration"]:
        '''lineage_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#lineage_configuration GlueCrawler#lineage_configuration}
        '''
        result = self._values.get("lineage_configuration")
        return typing.cast(typing.Optional["GlueCrawlerLineageConfiguration"], result)

    @builtins.property
    def mongodb_target(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GlueCrawlerMongodbTarget"]]]:
        '''mongodb_target block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#mongodb_target GlueCrawler#mongodb_target}
        '''
        result = self._values.get("mongodb_target")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GlueCrawlerMongodbTarget"]]], result)

    @builtins.property
    def recrawl_policy(self) -> typing.Optional["GlueCrawlerRecrawlPolicy"]:
        '''recrawl_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#recrawl_policy GlueCrawler#recrawl_policy}
        '''
        result = self._values.get("recrawl_policy")
        return typing.cast(typing.Optional["GlueCrawlerRecrawlPolicy"], result)

    @builtins.property
    def s3_target(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GlueCrawlerS3Target"]]]:
        '''s3_target block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#s3_target GlueCrawler#s3_target}
        '''
        result = self._values.get("s3_target")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GlueCrawlerS3Target"]]], result)

    @builtins.property
    def schedule(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#schedule GlueCrawler#schedule}.'''
        result = self._values.get("schedule")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def schema_change_policy(self) -> typing.Optional["GlueCrawlerSchemaChangePolicy"]:
        '''schema_change_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#schema_change_policy GlueCrawler#schema_change_policy}
        '''
        result = self._values.get("schema_change_policy")
        return typing.cast(typing.Optional["GlueCrawlerSchemaChangePolicy"], result)

    @builtins.property
    def security_configuration(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#security_configuration GlueCrawler#security_configuration}.'''
        result = self._values.get("security_configuration")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def table_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#table_prefix GlueCrawler#table_prefix}.'''
        result = self._values.get("table_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#tags GlueCrawler#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#tags_all GlueCrawler#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GlueCrawlerConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.glueCrawler.GlueCrawlerDeltaTarget",
    jsii_struct_bases=[],
    name_mapping={
        "connection_name": "connectionName",
        "delta_tables": "deltaTables",
        "write_manifest": "writeManifest",
    },
)
class GlueCrawlerDeltaTarget:
    def __init__(
        self,
        *,
        connection_name: builtins.str,
        delta_tables: typing.Sequence[builtins.str],
        write_manifest: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param connection_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#connection_name GlueCrawler#connection_name}.
        :param delta_tables: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#delta_tables GlueCrawler#delta_tables}.
        :param write_manifest: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#write_manifest GlueCrawler#write_manifest}.
        '''
        if __debug__:
            def stub(
                *,
                connection_name: builtins.str,
                delta_tables: typing.Sequence[builtins.str],
                write_manifest: typing.Union[builtins.bool, cdktf.IResolvable],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument connection_name", value=connection_name, expected_type=type_hints["connection_name"])
            check_type(argname="argument delta_tables", value=delta_tables, expected_type=type_hints["delta_tables"])
            check_type(argname="argument write_manifest", value=write_manifest, expected_type=type_hints["write_manifest"])
        self._values: typing.Dict[str, typing.Any] = {
            "connection_name": connection_name,
            "delta_tables": delta_tables,
            "write_manifest": write_manifest,
        }

    @builtins.property
    def connection_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#connection_name GlueCrawler#connection_name}.'''
        result = self._values.get("connection_name")
        assert result is not None, "Required property 'connection_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def delta_tables(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#delta_tables GlueCrawler#delta_tables}.'''
        result = self._values.get("delta_tables")
        assert result is not None, "Required property 'delta_tables' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def write_manifest(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#write_manifest GlueCrawler#write_manifest}.'''
        result = self._values.get("write_manifest")
        assert result is not None, "Required property 'write_manifest' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GlueCrawlerDeltaTarget(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GlueCrawlerDeltaTargetList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.glueCrawler.GlueCrawlerDeltaTargetList",
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
    def get(self, index: jsii.Number) -> "GlueCrawlerDeltaTargetOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GlueCrawlerDeltaTargetOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GlueCrawlerDeltaTarget]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GlueCrawlerDeltaTarget]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GlueCrawlerDeltaTarget]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GlueCrawlerDeltaTarget]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GlueCrawlerDeltaTargetOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.glueCrawler.GlueCrawlerDeltaTargetOutputReference",
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
    @jsii.member(jsii_name="connectionNameInput")
    def connection_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectionNameInput"))

    @builtins.property
    @jsii.member(jsii_name="deltaTablesInput")
    def delta_tables_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "deltaTablesInput"))

    @builtins.property
    @jsii.member(jsii_name="writeManifestInput")
    def write_manifest_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "writeManifestInput"))

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
    @jsii.member(jsii_name="deltaTables")
    def delta_tables(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "deltaTables"))

    @delta_tables.setter
    def delta_tables(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deltaTables", value)

    @builtins.property
    @jsii.member(jsii_name="writeManifest")
    def write_manifest(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "writeManifest"))

    @write_manifest.setter
    def write_manifest(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "writeManifest", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GlueCrawlerDeltaTarget, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GlueCrawlerDeltaTarget, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GlueCrawlerDeltaTarget, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[GlueCrawlerDeltaTarget, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.glueCrawler.GlueCrawlerDynamodbTarget",
    jsii_struct_bases=[],
    name_mapping={"path": "path", "scan_all": "scanAll", "scan_rate": "scanRate"},
)
class GlueCrawlerDynamodbTarget:
    def __init__(
        self,
        *,
        path: builtins.str,
        scan_all: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        scan_rate: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#path GlueCrawler#path}.
        :param scan_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#scan_all GlueCrawler#scan_all}.
        :param scan_rate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#scan_rate GlueCrawler#scan_rate}.
        '''
        if __debug__:
            def stub(
                *,
                path: builtins.str,
                scan_all: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                scan_rate: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument scan_all", value=scan_all, expected_type=type_hints["scan_all"])
            check_type(argname="argument scan_rate", value=scan_rate, expected_type=type_hints["scan_rate"])
        self._values: typing.Dict[str, typing.Any] = {
            "path": path,
        }
        if scan_all is not None:
            self._values["scan_all"] = scan_all
        if scan_rate is not None:
            self._values["scan_rate"] = scan_rate

    @builtins.property
    def path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#path GlueCrawler#path}.'''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def scan_all(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#scan_all GlueCrawler#scan_all}.'''
        result = self._values.get("scan_all")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def scan_rate(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#scan_rate GlueCrawler#scan_rate}.'''
        result = self._values.get("scan_rate")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GlueCrawlerDynamodbTarget(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GlueCrawlerDynamodbTargetList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.glueCrawler.GlueCrawlerDynamodbTargetList",
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
    def get(self, index: jsii.Number) -> "GlueCrawlerDynamodbTargetOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GlueCrawlerDynamodbTargetOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GlueCrawlerDynamodbTarget]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GlueCrawlerDynamodbTarget]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GlueCrawlerDynamodbTarget]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GlueCrawlerDynamodbTarget]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GlueCrawlerDynamodbTargetOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.glueCrawler.GlueCrawlerDynamodbTargetOutputReference",
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

    @jsii.member(jsii_name="resetScanAll")
    def reset_scan_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScanAll", []))

    @jsii.member(jsii_name="resetScanRate")
    def reset_scan_rate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScanRate", []))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="scanAllInput")
    def scan_all_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "scanAllInput"))

    @builtins.property
    @jsii.member(jsii_name="scanRateInput")
    def scan_rate_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "scanRateInput"))

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="scanAll")
    def scan_all(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "scanAll"))

    @scan_all.setter
    def scan_all(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scanAll", value)

    @builtins.property
    @jsii.member(jsii_name="scanRate")
    def scan_rate(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "scanRate"))

    @scan_rate.setter
    def scan_rate(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scanRate", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GlueCrawlerDynamodbTarget, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GlueCrawlerDynamodbTarget, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GlueCrawlerDynamodbTarget, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[GlueCrawlerDynamodbTarget, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.glueCrawler.GlueCrawlerJdbcTarget",
    jsii_struct_bases=[],
    name_mapping={
        "connection_name": "connectionName",
        "path": "path",
        "exclusions": "exclusions",
    },
)
class GlueCrawlerJdbcTarget:
    def __init__(
        self,
        *,
        connection_name: builtins.str,
        path: builtins.str,
        exclusions: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param connection_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#connection_name GlueCrawler#connection_name}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#path GlueCrawler#path}.
        :param exclusions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#exclusions GlueCrawler#exclusions}.
        '''
        if __debug__:
            def stub(
                *,
                connection_name: builtins.str,
                path: builtins.str,
                exclusions: typing.Optional[typing.Sequence[builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument connection_name", value=connection_name, expected_type=type_hints["connection_name"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument exclusions", value=exclusions, expected_type=type_hints["exclusions"])
        self._values: typing.Dict[str, typing.Any] = {
            "connection_name": connection_name,
            "path": path,
        }
        if exclusions is not None:
            self._values["exclusions"] = exclusions

    @builtins.property
    def connection_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#connection_name GlueCrawler#connection_name}.'''
        result = self._values.get("connection_name")
        assert result is not None, "Required property 'connection_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#path GlueCrawler#path}.'''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def exclusions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#exclusions GlueCrawler#exclusions}.'''
        result = self._values.get("exclusions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GlueCrawlerJdbcTarget(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GlueCrawlerJdbcTargetList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.glueCrawler.GlueCrawlerJdbcTargetList",
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
    def get(self, index: jsii.Number) -> "GlueCrawlerJdbcTargetOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GlueCrawlerJdbcTargetOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GlueCrawlerJdbcTarget]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GlueCrawlerJdbcTarget]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GlueCrawlerJdbcTarget]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GlueCrawlerJdbcTarget]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GlueCrawlerJdbcTargetOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.glueCrawler.GlueCrawlerJdbcTargetOutputReference",
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

    @jsii.member(jsii_name="resetExclusions")
    def reset_exclusions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExclusions", []))

    @builtins.property
    @jsii.member(jsii_name="connectionNameInput")
    def connection_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectionNameInput"))

    @builtins.property
    @jsii.member(jsii_name="exclusionsInput")
    def exclusions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "exclusionsInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

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
    @jsii.member(jsii_name="exclusions")
    def exclusions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "exclusions"))

    @exclusions.setter
    def exclusions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exclusions", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GlueCrawlerJdbcTarget, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GlueCrawlerJdbcTarget, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GlueCrawlerJdbcTarget, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[GlueCrawlerJdbcTarget, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.glueCrawler.GlueCrawlerLineageConfiguration",
    jsii_struct_bases=[],
    name_mapping={"crawler_lineage_settings": "crawlerLineageSettings"},
)
class GlueCrawlerLineageConfiguration:
    def __init__(
        self,
        *,
        crawler_lineage_settings: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param crawler_lineage_settings: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#crawler_lineage_settings GlueCrawler#crawler_lineage_settings}.
        '''
        if __debug__:
            def stub(
                *,
                crawler_lineage_settings: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument crawler_lineage_settings", value=crawler_lineage_settings, expected_type=type_hints["crawler_lineage_settings"])
        self._values: typing.Dict[str, typing.Any] = {}
        if crawler_lineage_settings is not None:
            self._values["crawler_lineage_settings"] = crawler_lineage_settings

    @builtins.property
    def crawler_lineage_settings(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#crawler_lineage_settings GlueCrawler#crawler_lineage_settings}.'''
        result = self._values.get("crawler_lineage_settings")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GlueCrawlerLineageConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GlueCrawlerLineageConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.glueCrawler.GlueCrawlerLineageConfigurationOutputReference",
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

    @jsii.member(jsii_name="resetCrawlerLineageSettings")
    def reset_crawler_lineage_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCrawlerLineageSettings", []))

    @builtins.property
    @jsii.member(jsii_name="crawlerLineageSettingsInput")
    def crawler_lineage_settings_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "crawlerLineageSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="crawlerLineageSettings")
    def crawler_lineage_settings(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "crawlerLineageSettings"))

    @crawler_lineage_settings.setter
    def crawler_lineage_settings(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "crawlerLineageSettings", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GlueCrawlerLineageConfiguration]:
        return typing.cast(typing.Optional[GlueCrawlerLineageConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GlueCrawlerLineageConfiguration],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[GlueCrawlerLineageConfiguration]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.glueCrawler.GlueCrawlerMongodbTarget",
    jsii_struct_bases=[],
    name_mapping={
        "connection_name": "connectionName",
        "path": "path",
        "scan_all": "scanAll",
    },
)
class GlueCrawlerMongodbTarget:
    def __init__(
        self,
        *,
        connection_name: builtins.str,
        path: builtins.str,
        scan_all: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param connection_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#connection_name GlueCrawler#connection_name}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#path GlueCrawler#path}.
        :param scan_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#scan_all GlueCrawler#scan_all}.
        '''
        if __debug__:
            def stub(
                *,
                connection_name: builtins.str,
                path: builtins.str,
                scan_all: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument connection_name", value=connection_name, expected_type=type_hints["connection_name"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument scan_all", value=scan_all, expected_type=type_hints["scan_all"])
        self._values: typing.Dict[str, typing.Any] = {
            "connection_name": connection_name,
            "path": path,
        }
        if scan_all is not None:
            self._values["scan_all"] = scan_all

    @builtins.property
    def connection_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#connection_name GlueCrawler#connection_name}.'''
        result = self._values.get("connection_name")
        assert result is not None, "Required property 'connection_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#path GlueCrawler#path}.'''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def scan_all(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#scan_all GlueCrawler#scan_all}.'''
        result = self._values.get("scan_all")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GlueCrawlerMongodbTarget(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GlueCrawlerMongodbTargetList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.glueCrawler.GlueCrawlerMongodbTargetList",
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
    def get(self, index: jsii.Number) -> "GlueCrawlerMongodbTargetOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GlueCrawlerMongodbTargetOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GlueCrawlerMongodbTarget]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GlueCrawlerMongodbTarget]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GlueCrawlerMongodbTarget]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GlueCrawlerMongodbTarget]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GlueCrawlerMongodbTargetOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.glueCrawler.GlueCrawlerMongodbTargetOutputReference",
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

    @jsii.member(jsii_name="resetScanAll")
    def reset_scan_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScanAll", []))

    @builtins.property
    @jsii.member(jsii_name="connectionNameInput")
    def connection_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectionNameInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="scanAllInput")
    def scan_all_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "scanAllInput"))

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
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="scanAll")
    def scan_all(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "scanAll"))

    @scan_all.setter
    def scan_all(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scanAll", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GlueCrawlerMongodbTarget, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GlueCrawlerMongodbTarget, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GlueCrawlerMongodbTarget, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[GlueCrawlerMongodbTarget, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.glueCrawler.GlueCrawlerRecrawlPolicy",
    jsii_struct_bases=[],
    name_mapping={"recrawl_behavior": "recrawlBehavior"},
)
class GlueCrawlerRecrawlPolicy:
    def __init__(
        self,
        *,
        recrawl_behavior: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param recrawl_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#recrawl_behavior GlueCrawler#recrawl_behavior}.
        '''
        if __debug__:
            def stub(*, recrawl_behavior: typing.Optional[builtins.str] = None) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument recrawl_behavior", value=recrawl_behavior, expected_type=type_hints["recrawl_behavior"])
        self._values: typing.Dict[str, typing.Any] = {}
        if recrawl_behavior is not None:
            self._values["recrawl_behavior"] = recrawl_behavior

    @builtins.property
    def recrawl_behavior(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#recrawl_behavior GlueCrawler#recrawl_behavior}.'''
        result = self._values.get("recrawl_behavior")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GlueCrawlerRecrawlPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GlueCrawlerRecrawlPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.glueCrawler.GlueCrawlerRecrawlPolicyOutputReference",
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

    @jsii.member(jsii_name="resetRecrawlBehavior")
    def reset_recrawl_behavior(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRecrawlBehavior", []))

    @builtins.property
    @jsii.member(jsii_name="recrawlBehaviorInput")
    def recrawl_behavior_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "recrawlBehaviorInput"))

    @builtins.property
    @jsii.member(jsii_name="recrawlBehavior")
    def recrawl_behavior(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "recrawlBehavior"))

    @recrawl_behavior.setter
    def recrawl_behavior(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recrawlBehavior", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GlueCrawlerRecrawlPolicy]:
        return typing.cast(typing.Optional[GlueCrawlerRecrawlPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[GlueCrawlerRecrawlPolicy]) -> None:
        if __debug__:
            def stub(value: typing.Optional[GlueCrawlerRecrawlPolicy]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.glueCrawler.GlueCrawlerS3Target",
    jsii_struct_bases=[],
    name_mapping={
        "path": "path",
        "connection_name": "connectionName",
        "dlq_event_queue_arn": "dlqEventQueueArn",
        "event_queue_arn": "eventQueueArn",
        "exclusions": "exclusions",
        "sample_size": "sampleSize",
    },
)
class GlueCrawlerS3Target:
    def __init__(
        self,
        *,
        path: builtins.str,
        connection_name: typing.Optional[builtins.str] = None,
        dlq_event_queue_arn: typing.Optional[builtins.str] = None,
        event_queue_arn: typing.Optional[builtins.str] = None,
        exclusions: typing.Optional[typing.Sequence[builtins.str]] = None,
        sample_size: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#path GlueCrawler#path}.
        :param connection_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#connection_name GlueCrawler#connection_name}.
        :param dlq_event_queue_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#dlq_event_queue_arn GlueCrawler#dlq_event_queue_arn}.
        :param event_queue_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#event_queue_arn GlueCrawler#event_queue_arn}.
        :param exclusions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#exclusions GlueCrawler#exclusions}.
        :param sample_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#sample_size GlueCrawler#sample_size}.
        '''
        if __debug__:
            def stub(
                *,
                path: builtins.str,
                connection_name: typing.Optional[builtins.str] = None,
                dlq_event_queue_arn: typing.Optional[builtins.str] = None,
                event_queue_arn: typing.Optional[builtins.str] = None,
                exclusions: typing.Optional[typing.Sequence[builtins.str]] = None,
                sample_size: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument connection_name", value=connection_name, expected_type=type_hints["connection_name"])
            check_type(argname="argument dlq_event_queue_arn", value=dlq_event_queue_arn, expected_type=type_hints["dlq_event_queue_arn"])
            check_type(argname="argument event_queue_arn", value=event_queue_arn, expected_type=type_hints["event_queue_arn"])
            check_type(argname="argument exclusions", value=exclusions, expected_type=type_hints["exclusions"])
            check_type(argname="argument sample_size", value=sample_size, expected_type=type_hints["sample_size"])
        self._values: typing.Dict[str, typing.Any] = {
            "path": path,
        }
        if connection_name is not None:
            self._values["connection_name"] = connection_name
        if dlq_event_queue_arn is not None:
            self._values["dlq_event_queue_arn"] = dlq_event_queue_arn
        if event_queue_arn is not None:
            self._values["event_queue_arn"] = event_queue_arn
        if exclusions is not None:
            self._values["exclusions"] = exclusions
        if sample_size is not None:
            self._values["sample_size"] = sample_size

    @builtins.property
    def path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#path GlueCrawler#path}.'''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def connection_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#connection_name GlueCrawler#connection_name}.'''
        result = self._values.get("connection_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dlq_event_queue_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#dlq_event_queue_arn GlueCrawler#dlq_event_queue_arn}.'''
        result = self._values.get("dlq_event_queue_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def event_queue_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#event_queue_arn GlueCrawler#event_queue_arn}.'''
        result = self._values.get("event_queue_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def exclusions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#exclusions GlueCrawler#exclusions}.'''
        result = self._values.get("exclusions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def sample_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#sample_size GlueCrawler#sample_size}.'''
        result = self._values.get("sample_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GlueCrawlerS3Target(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GlueCrawlerS3TargetList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.glueCrawler.GlueCrawlerS3TargetList",
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
    def get(self, index: jsii.Number) -> "GlueCrawlerS3TargetOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GlueCrawlerS3TargetOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GlueCrawlerS3Target]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GlueCrawlerS3Target]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GlueCrawlerS3Target]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GlueCrawlerS3Target]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GlueCrawlerS3TargetOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.glueCrawler.GlueCrawlerS3TargetOutputReference",
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

    @jsii.member(jsii_name="resetConnectionName")
    def reset_connection_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectionName", []))

    @jsii.member(jsii_name="resetDlqEventQueueArn")
    def reset_dlq_event_queue_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDlqEventQueueArn", []))

    @jsii.member(jsii_name="resetEventQueueArn")
    def reset_event_queue_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEventQueueArn", []))

    @jsii.member(jsii_name="resetExclusions")
    def reset_exclusions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExclusions", []))

    @jsii.member(jsii_name="resetSampleSize")
    def reset_sample_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSampleSize", []))

    @builtins.property
    @jsii.member(jsii_name="connectionNameInput")
    def connection_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectionNameInput"))

    @builtins.property
    @jsii.member(jsii_name="dlqEventQueueArnInput")
    def dlq_event_queue_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dlqEventQueueArnInput"))

    @builtins.property
    @jsii.member(jsii_name="eventQueueArnInput")
    def event_queue_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "eventQueueArnInput"))

    @builtins.property
    @jsii.member(jsii_name="exclusionsInput")
    def exclusions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "exclusionsInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="sampleSizeInput")
    def sample_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sampleSizeInput"))

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
    @jsii.member(jsii_name="dlqEventQueueArn")
    def dlq_event_queue_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dlqEventQueueArn"))

    @dlq_event_queue_arn.setter
    def dlq_event_queue_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dlqEventQueueArn", value)

    @builtins.property
    @jsii.member(jsii_name="eventQueueArn")
    def event_queue_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "eventQueueArn"))

    @event_queue_arn.setter
    def event_queue_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventQueueArn", value)

    @builtins.property
    @jsii.member(jsii_name="exclusions")
    def exclusions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "exclusions"))

    @exclusions.setter
    def exclusions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exclusions", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="sampleSize")
    def sample_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sampleSize"))

    @sample_size.setter
    def sample_size(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sampleSize", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GlueCrawlerS3Target, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GlueCrawlerS3Target, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GlueCrawlerS3Target, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[GlueCrawlerS3Target, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.glueCrawler.GlueCrawlerSchemaChangePolicy",
    jsii_struct_bases=[],
    name_mapping={
        "delete_behavior": "deleteBehavior",
        "update_behavior": "updateBehavior",
    },
)
class GlueCrawlerSchemaChangePolicy:
    def __init__(
        self,
        *,
        delete_behavior: typing.Optional[builtins.str] = None,
        update_behavior: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param delete_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#delete_behavior GlueCrawler#delete_behavior}.
        :param update_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#update_behavior GlueCrawler#update_behavior}.
        '''
        if __debug__:
            def stub(
                *,
                delete_behavior: typing.Optional[builtins.str] = None,
                update_behavior: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument delete_behavior", value=delete_behavior, expected_type=type_hints["delete_behavior"])
            check_type(argname="argument update_behavior", value=update_behavior, expected_type=type_hints["update_behavior"])
        self._values: typing.Dict[str, typing.Any] = {}
        if delete_behavior is not None:
            self._values["delete_behavior"] = delete_behavior
        if update_behavior is not None:
            self._values["update_behavior"] = update_behavior

    @builtins.property
    def delete_behavior(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#delete_behavior GlueCrawler#delete_behavior}.'''
        result = self._values.get("delete_behavior")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update_behavior(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_crawler#update_behavior GlueCrawler#update_behavior}.'''
        result = self._values.get("update_behavior")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GlueCrawlerSchemaChangePolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GlueCrawlerSchemaChangePolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.glueCrawler.GlueCrawlerSchemaChangePolicyOutputReference",
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

    @jsii.member(jsii_name="resetDeleteBehavior")
    def reset_delete_behavior(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeleteBehavior", []))

    @jsii.member(jsii_name="resetUpdateBehavior")
    def reset_update_behavior(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdateBehavior", []))

    @builtins.property
    @jsii.member(jsii_name="deleteBehaviorInput")
    def delete_behavior_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteBehaviorInput"))

    @builtins.property
    @jsii.member(jsii_name="updateBehaviorInput")
    def update_behavior_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "updateBehaviorInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteBehavior")
    def delete_behavior(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deleteBehavior"))

    @delete_behavior.setter
    def delete_behavior(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deleteBehavior", value)

    @builtins.property
    @jsii.member(jsii_name="updateBehavior")
    def update_behavior(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "updateBehavior"))

    @update_behavior.setter
    def update_behavior(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "updateBehavior", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GlueCrawlerSchemaChangePolicy]:
        return typing.cast(typing.Optional[GlueCrawlerSchemaChangePolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GlueCrawlerSchemaChangePolicy],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[GlueCrawlerSchemaChangePolicy]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GlueCrawler",
    "GlueCrawlerCatalogTarget",
    "GlueCrawlerCatalogTargetList",
    "GlueCrawlerCatalogTargetOutputReference",
    "GlueCrawlerConfig",
    "GlueCrawlerDeltaTarget",
    "GlueCrawlerDeltaTargetList",
    "GlueCrawlerDeltaTargetOutputReference",
    "GlueCrawlerDynamodbTarget",
    "GlueCrawlerDynamodbTargetList",
    "GlueCrawlerDynamodbTargetOutputReference",
    "GlueCrawlerJdbcTarget",
    "GlueCrawlerJdbcTargetList",
    "GlueCrawlerJdbcTargetOutputReference",
    "GlueCrawlerLineageConfiguration",
    "GlueCrawlerLineageConfigurationOutputReference",
    "GlueCrawlerMongodbTarget",
    "GlueCrawlerMongodbTargetList",
    "GlueCrawlerMongodbTargetOutputReference",
    "GlueCrawlerRecrawlPolicy",
    "GlueCrawlerRecrawlPolicyOutputReference",
    "GlueCrawlerS3Target",
    "GlueCrawlerS3TargetList",
    "GlueCrawlerS3TargetOutputReference",
    "GlueCrawlerSchemaChangePolicy",
    "GlueCrawlerSchemaChangePolicyOutputReference",
]

publication.publish()
