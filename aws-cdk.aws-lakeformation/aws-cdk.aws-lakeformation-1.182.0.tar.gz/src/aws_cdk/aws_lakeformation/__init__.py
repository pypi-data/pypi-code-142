'''
# AWS::LakeFormation Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_lakeformation as lakeformation
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for LakeFormation construct libraries](https://constructs.dev/search?q=lakeformation)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::LakeFormation resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_LakeFormation.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::LakeFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_LakeFormation.html).

(Read the [CDK Contributing Guide](https://github.com/aws/aws-cdk/blob/master/CONTRIBUTING.md) and submit an RFC if you are interested in contributing to this construct library.)

<!--END CFNONLY DISCLAIMER-->
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

from ._jsii import *

import aws_cdk.core


@jsii.implements(aws_cdk.core.IInspectable)
class CfnDataCellsFilter(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-lakeformation.CfnDataCellsFilter",
):
    '''A CloudFormation ``AWS::LakeFormation::DataCellsFilter``.

    A structure that represents a data cell filter with column-level, row-level, and/or cell-level security. Data cell filters belong to a specific table in a Data Catalog . During a stack operation, AWS CloudFormation calls the AWS Lake Formation ``CreateDataCellsFilter`` API operation to create a ``DataCellsFilter`` resource, and calls the ``DeleteDataCellsFilter`` API operation to delete it.

    :cloudformationResource: AWS::LakeFormation::DataCellsFilter
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datacellsfilter.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_lakeformation as lakeformation
        
        # all_rows_wildcard: Any
        
        cfn_data_cells_filter = lakeformation.CfnDataCellsFilter(self, "MyCfnDataCellsFilter",
            database_name="databaseName",
            name="name",
            table_catalog_id="tableCatalogId",
            table_name="tableName",
        
            # the properties below are optional
            column_names=["columnNames"],
            column_wildcard=lakeformation.CfnDataCellsFilter.ColumnWildcardProperty(
                excluded_column_names=["excludedColumnNames"]
            ),
            row_filter=lakeformation.CfnDataCellsFilter.RowFilterProperty(
                all_rows_wildcard=all_rows_wildcard,
                filter_expression="filterExpression"
            )
        )
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        database_name: builtins.str,
        name: builtins.str,
        table_catalog_id: builtins.str,
        table_name: builtins.str,
        column_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        column_wildcard: typing.Optional[typing.Union[typing.Union["CfnDataCellsFilter.ColumnWildcardProperty", typing.Dict[str, typing.Any]], aws_cdk.core.IResolvable]] = None,
        row_filter: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union["CfnDataCellsFilter.RowFilterProperty", typing.Dict[str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::LakeFormation::DataCellsFilter``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param database_name: UTF-8 string, not less than 1 or more than 255 bytes long, matching the `single-line string pattern <https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api-aws-lake-formation-api-common.html#aws-glue-api-regex-oneLine>`_ . A database in the Data Catalog .
        :param name: UTF-8 string, not less than 1 or more than 255 bytes long, matching the `single-line string pattern <https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api-aws-lake-formation-api-common.html#aws-glue-api-regex-oneLine>`_ . The name given by the user to the data filter cell.
        :param table_catalog_id: Catalog id string, not less than 1 or more than 255 bytes long, matching the `single-line string pattern <https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api-aws-lake-formation-api-common.html#aws-glue-api-regex-oneLine>`_ . The ID of the catalog to which the table belongs.
        :param table_name: UTF-8 string, not less than 1 or more than 255 bytes long, matching the `single-line string pattern <https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api-aws-lake-formation-api-common.html#aws-glue-api-regex-oneLine>`_ . A table in the database.
        :param column_names: An array of UTF-8 strings. A list of column names.
        :param column_wildcard: A wildcard with exclusions. You must specify either a ``ColumnNames`` list or the ``ColumnWildCard`` .
        :param row_filter: A PartiQL predicate.
        '''
        if __debug__:
            def stub(
                scope: aws_cdk.core.Construct,
                id: builtins.str,
                *,
                database_name: builtins.str,
                name: builtins.str,
                table_catalog_id: builtins.str,
                table_name: builtins.str,
                column_names: typing.Optional[typing.Sequence[builtins.str]] = None,
                column_wildcard: typing.Optional[typing.Union[typing.Union[CfnDataCellsFilter.ColumnWildcardProperty, typing.Dict[str, typing.Any]], aws_cdk.core.IResolvable]] = None,
                row_filter: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnDataCellsFilter.RowFilterProperty, typing.Dict[str, typing.Any]]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDataCellsFilterProps(
            database_name=database_name,
            name=name,
            table_catalog_id=table_catalog_id,
            table_name=table_name,
            column_names=column_names,
            column_wildcard=column_wildcard,
            row_filter=row_filter,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            def stub(inspector: aws_cdk.core.TreeInspector) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            def stub(props: typing.Mapping[builtins.str, typing.Any]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="databaseName")
    def database_name(self) -> builtins.str:
        '''UTF-8 string, not less than 1 or more than 255 bytes long, matching the `single-line string pattern <https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api-aws-lake-formation-api-common.html#aws-glue-api-regex-oneLine>`_ .

        A database in the Data Catalog .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datacellsfilter.html#cfn-lakeformation-datacellsfilter-databasename
        '''
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
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''UTF-8 string, not less than 1 or more than 255 bytes long, matching the `single-line string pattern <https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api-aws-lake-formation-api-common.html#aws-glue-api-regex-oneLine>`_ .

        The name given by the user to the data filter cell.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datacellsfilter.html#cfn-lakeformation-datacellsfilter-name
        '''
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
    @jsii.member(jsii_name="tableCatalogId")
    def table_catalog_id(self) -> builtins.str:
        '''Catalog id string, not less than 1 or more than 255 bytes long, matching the `single-line string pattern <https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api-aws-lake-formation-api-common.html#aws-glue-api-regex-oneLine>`_ .

        The ID of the catalog to which the table belongs.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datacellsfilter.html#cfn-lakeformation-datacellsfilter-tablecatalogid
        '''
        return typing.cast(builtins.str, jsii.get(self, "tableCatalogId"))

    @table_catalog_id.setter
    def table_catalog_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tableCatalogId", value)

    @builtins.property
    @jsii.member(jsii_name="tableName")
    def table_name(self) -> builtins.str:
        '''UTF-8 string, not less than 1 or more than 255 bytes long, matching the `single-line string pattern <https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api-aws-lake-formation-api-common.html#aws-glue-api-regex-oneLine>`_ .

        A table in the database.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datacellsfilter.html#cfn-lakeformation-datacellsfilter-tablename
        '''
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
    @jsii.member(jsii_name="columnNames")
    def column_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of UTF-8 strings.

        A list of column names.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datacellsfilter.html#cfn-lakeformation-datacellsfilter-columnnames
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "columnNames"))

    @column_names.setter
    def column_names(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            def stub(value: typing.Optional[typing.List[builtins.str]]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "columnNames", value)

    @builtins.property
    @jsii.member(jsii_name="columnWildcard")
    def column_wildcard(
        self,
    ) -> typing.Optional[typing.Union["CfnDataCellsFilter.ColumnWildcardProperty", aws_cdk.core.IResolvable]]:
        '''A wildcard with exclusions.

        You must specify either a ``ColumnNames`` list or the ``ColumnWildCard`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datacellsfilter.html#cfn-lakeformation-datacellsfilter-columnwildcard
        '''
        return typing.cast(typing.Optional[typing.Union["CfnDataCellsFilter.ColumnWildcardProperty", aws_cdk.core.IResolvable]], jsii.get(self, "columnWildcard"))

    @column_wildcard.setter
    def column_wildcard(
        self,
        value: typing.Optional[typing.Union["CfnDataCellsFilter.ColumnWildcardProperty", aws_cdk.core.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[CfnDataCellsFilter.ColumnWildcardProperty, aws_cdk.core.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "columnWildcard", value)

    @builtins.property
    @jsii.member(jsii_name="rowFilter")
    def row_filter(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataCellsFilter.RowFilterProperty"]]:
        '''A PartiQL predicate.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datacellsfilter.html#cfn-lakeformation-datacellsfilter-rowfilter
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataCellsFilter.RowFilterProperty"]], jsii.get(self, "rowFilter"))

    @row_filter.setter
    def row_filter(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataCellsFilter.RowFilterProperty"]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDataCellsFilter.RowFilterProperty]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rowFilter", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-lakeformation.CfnDataCellsFilter.ColumnWildcardProperty",
        jsii_struct_bases=[],
        name_mapping={"excluded_column_names": "excludedColumnNames"},
    )
    class ColumnWildcardProperty:
        def __init__(
            self,
            *,
            excluded_column_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''A wildcard object, consisting of an optional list of excluded column names or indexes.

            :param excluded_column_names: Excludes column names. Any column with this name will be excluded.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-datacellsfilter-columnwildcard.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_lakeformation as lakeformation
                
                column_wildcard_property = lakeformation.CfnDataCellsFilter.ColumnWildcardProperty(
                    excluded_column_names=["excludedColumnNames"]
                )
            '''
            if __debug__:
                def stub(
                    *,
                    excluded_column_names: typing.Optional[typing.Sequence[builtins.str]] = None,
                ) -> None:
                    ...
                type_hints = typing.get_type_hints(stub)
                check_type(argname="argument excluded_column_names", value=excluded_column_names, expected_type=type_hints["excluded_column_names"])
            self._values: typing.Dict[str, typing.Any] = {}
            if excluded_column_names is not None:
                self._values["excluded_column_names"] = excluded_column_names

        @builtins.property
        def excluded_column_names(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Excludes column names.

            Any column with this name will be excluded.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-datacellsfilter-columnwildcard.html#cfn-lakeformation-datacellsfilter-columnwildcard-excludedcolumnnames
            '''
            result = self._values.get("excluded_column_names")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ColumnWildcardProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-lakeformation.CfnDataCellsFilter.RowFilterProperty",
        jsii_struct_bases=[],
        name_mapping={
            "all_rows_wildcard": "allRowsWildcard",
            "filter_expression": "filterExpression",
        },
    )
    class RowFilterProperty:
        def __init__(
            self,
            *,
            all_rows_wildcard: typing.Any = None,
            filter_expression: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A PartiQL predicate.

            :param all_rows_wildcard: A wildcard for all rows.
            :param filter_expression: A filter expression.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-datacellsfilter-rowfilter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_lakeformation as lakeformation
                
                # all_rows_wildcard: Any
                
                row_filter_property = lakeformation.CfnDataCellsFilter.RowFilterProperty(
                    all_rows_wildcard=all_rows_wildcard,
                    filter_expression="filterExpression"
                )
            '''
            if __debug__:
                def stub(
                    *,
                    all_rows_wildcard: typing.Any = None,
                    filter_expression: typing.Optional[builtins.str] = None,
                ) -> None:
                    ...
                type_hints = typing.get_type_hints(stub)
                check_type(argname="argument all_rows_wildcard", value=all_rows_wildcard, expected_type=type_hints["all_rows_wildcard"])
                check_type(argname="argument filter_expression", value=filter_expression, expected_type=type_hints["filter_expression"])
            self._values: typing.Dict[str, typing.Any] = {}
            if all_rows_wildcard is not None:
                self._values["all_rows_wildcard"] = all_rows_wildcard
            if filter_expression is not None:
                self._values["filter_expression"] = filter_expression

        @builtins.property
        def all_rows_wildcard(self) -> typing.Any:
            '''A wildcard for all rows.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-datacellsfilter-rowfilter.html#cfn-lakeformation-datacellsfilter-rowfilter-allrowswildcard
            '''
            result = self._values.get("all_rows_wildcard")
            return typing.cast(typing.Any, result)

        @builtins.property
        def filter_expression(self) -> typing.Optional[builtins.str]:
            '''A filter expression.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-datacellsfilter-rowfilter.html#cfn-lakeformation-datacellsfilter-rowfilter-filterexpression
            '''
            result = self._values.get("filter_expression")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RowFilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-lakeformation.CfnDataCellsFilterProps",
    jsii_struct_bases=[],
    name_mapping={
        "database_name": "databaseName",
        "name": "name",
        "table_catalog_id": "tableCatalogId",
        "table_name": "tableName",
        "column_names": "columnNames",
        "column_wildcard": "columnWildcard",
        "row_filter": "rowFilter",
    },
)
class CfnDataCellsFilterProps:
    def __init__(
        self,
        *,
        database_name: builtins.str,
        name: builtins.str,
        table_catalog_id: builtins.str,
        table_name: builtins.str,
        column_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        column_wildcard: typing.Optional[typing.Union[typing.Union[CfnDataCellsFilter.ColumnWildcardProperty, typing.Dict[str, typing.Any]], aws_cdk.core.IResolvable]] = None,
        row_filter: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnDataCellsFilter.RowFilterProperty, typing.Dict[str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDataCellsFilter``.

        :param database_name: UTF-8 string, not less than 1 or more than 255 bytes long, matching the `single-line string pattern <https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api-aws-lake-formation-api-common.html#aws-glue-api-regex-oneLine>`_ . A database in the Data Catalog .
        :param name: UTF-8 string, not less than 1 or more than 255 bytes long, matching the `single-line string pattern <https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api-aws-lake-formation-api-common.html#aws-glue-api-regex-oneLine>`_ . The name given by the user to the data filter cell.
        :param table_catalog_id: Catalog id string, not less than 1 or more than 255 bytes long, matching the `single-line string pattern <https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api-aws-lake-formation-api-common.html#aws-glue-api-regex-oneLine>`_ . The ID of the catalog to which the table belongs.
        :param table_name: UTF-8 string, not less than 1 or more than 255 bytes long, matching the `single-line string pattern <https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api-aws-lake-formation-api-common.html#aws-glue-api-regex-oneLine>`_ . A table in the database.
        :param column_names: An array of UTF-8 strings. A list of column names.
        :param column_wildcard: A wildcard with exclusions. You must specify either a ``ColumnNames`` list or the ``ColumnWildCard`` .
        :param row_filter: A PartiQL predicate.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datacellsfilter.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_lakeformation as lakeformation
            
            # all_rows_wildcard: Any
            
            cfn_data_cells_filter_props = lakeformation.CfnDataCellsFilterProps(
                database_name="databaseName",
                name="name",
                table_catalog_id="tableCatalogId",
                table_name="tableName",
            
                # the properties below are optional
                column_names=["columnNames"],
                column_wildcard=lakeformation.CfnDataCellsFilter.ColumnWildcardProperty(
                    excluded_column_names=["excludedColumnNames"]
                ),
                row_filter=lakeformation.CfnDataCellsFilter.RowFilterProperty(
                    all_rows_wildcard=all_rows_wildcard,
                    filter_expression="filterExpression"
                )
            )
        '''
        if __debug__:
            def stub(
                *,
                database_name: builtins.str,
                name: builtins.str,
                table_catalog_id: builtins.str,
                table_name: builtins.str,
                column_names: typing.Optional[typing.Sequence[builtins.str]] = None,
                column_wildcard: typing.Optional[typing.Union[typing.Union[CfnDataCellsFilter.ColumnWildcardProperty, typing.Dict[str, typing.Any]], aws_cdk.core.IResolvable]] = None,
                row_filter: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnDataCellsFilter.RowFilterProperty, typing.Dict[str, typing.Any]]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument table_catalog_id", value=table_catalog_id, expected_type=type_hints["table_catalog_id"])
            check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
            check_type(argname="argument column_names", value=column_names, expected_type=type_hints["column_names"])
            check_type(argname="argument column_wildcard", value=column_wildcard, expected_type=type_hints["column_wildcard"])
            check_type(argname="argument row_filter", value=row_filter, expected_type=type_hints["row_filter"])
        self._values: typing.Dict[str, typing.Any] = {
            "database_name": database_name,
            "name": name,
            "table_catalog_id": table_catalog_id,
            "table_name": table_name,
        }
        if column_names is not None:
            self._values["column_names"] = column_names
        if column_wildcard is not None:
            self._values["column_wildcard"] = column_wildcard
        if row_filter is not None:
            self._values["row_filter"] = row_filter

    @builtins.property
    def database_name(self) -> builtins.str:
        '''UTF-8 string, not less than 1 or more than 255 bytes long, matching the `single-line string pattern <https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api-aws-lake-formation-api-common.html#aws-glue-api-regex-oneLine>`_ .

        A database in the Data Catalog .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datacellsfilter.html#cfn-lakeformation-datacellsfilter-databasename
        '''
        result = self._values.get("database_name")
        assert result is not None, "Required property 'database_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''UTF-8 string, not less than 1 or more than 255 bytes long, matching the `single-line string pattern <https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api-aws-lake-formation-api-common.html#aws-glue-api-regex-oneLine>`_ .

        The name given by the user to the data filter cell.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datacellsfilter.html#cfn-lakeformation-datacellsfilter-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def table_catalog_id(self) -> builtins.str:
        '''Catalog id string, not less than 1 or more than 255 bytes long, matching the `single-line string pattern <https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api-aws-lake-formation-api-common.html#aws-glue-api-regex-oneLine>`_ .

        The ID of the catalog to which the table belongs.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datacellsfilter.html#cfn-lakeformation-datacellsfilter-tablecatalogid
        '''
        result = self._values.get("table_catalog_id")
        assert result is not None, "Required property 'table_catalog_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def table_name(self) -> builtins.str:
        '''UTF-8 string, not less than 1 or more than 255 bytes long, matching the `single-line string pattern <https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api-aws-lake-formation-api-common.html#aws-glue-api-regex-oneLine>`_ .

        A table in the database.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datacellsfilter.html#cfn-lakeformation-datacellsfilter-tablename
        '''
        result = self._values.get("table_name")
        assert result is not None, "Required property 'table_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def column_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of UTF-8 strings.

        A list of column names.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datacellsfilter.html#cfn-lakeformation-datacellsfilter-columnnames
        '''
        result = self._values.get("column_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def column_wildcard(
        self,
    ) -> typing.Optional[typing.Union[CfnDataCellsFilter.ColumnWildcardProperty, aws_cdk.core.IResolvable]]:
        '''A wildcard with exclusions.

        You must specify either a ``ColumnNames`` list or the ``ColumnWildCard`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datacellsfilter.html#cfn-lakeformation-datacellsfilter-columnwildcard
        '''
        result = self._values.get("column_wildcard")
        return typing.cast(typing.Optional[typing.Union[CfnDataCellsFilter.ColumnWildcardProperty, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def row_filter(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDataCellsFilter.RowFilterProperty]]:
        '''A PartiQL predicate.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datacellsfilter.html#cfn-lakeformation-datacellsfilter-rowfilter
        '''
        result = self._values.get("row_filter")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDataCellsFilter.RowFilterProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDataCellsFilterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnDataLakeSettings(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-lakeformation.CfnDataLakeSettings",
):
    '''A CloudFormation ``AWS::LakeFormation::DataLakeSettings``.

    The ``AWS::LakeFormation::DataLakeSettings`` resource is an AWS Lake Formation resource type that manages the data lake settings for your account. Note that the CloudFormation template only supports updating the ``Admins`` list. It does not support updating the `CreateDatabaseDefaultPermissions <https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api-aws-lake-formation-api-settings.html#aws-lake-formation-api-aws-lake-formation-api-settings-DataLakeSettings>`_ or `CreateTableDefaultPermissions <https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api-aws-lake-formation-api-settings.html#aws-lake-formation-api-aws-lake-formation-api-settings-DataLakeSettings>`_ . Those permissions can only be edited in the DataLakeSettings resource via the API.

    :cloudformationResource: AWS::LakeFormation::DataLakeSettings
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datalakesettings.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_lakeformation as lakeformation
        
        cfn_data_lake_settings = lakeformation.CfnDataLakeSettings(self, "MyCfnDataLakeSettings",
            admins=[lakeformation.CfnDataLakeSettings.DataLakePrincipalProperty(
                data_lake_principal_identifier="dataLakePrincipalIdentifier"
            )],
            trusted_resource_owners=["trustedResourceOwners"]
        )
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        admins: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, typing.Union["CfnDataLakeSettings.DataLakePrincipalProperty", typing.Dict[str, typing.Any]]]]]] = None,
        trusted_resource_owners: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Create a new ``AWS::LakeFormation::DataLakeSettings``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param admins: A list of AWS Lake Formation principals.
        :param trusted_resource_owners: An array of UTF-8 strings. A list of the resource-owning account IDs that the caller's account can use to share their user access details (user ARNs). The user ARNs can be logged in the resource owner's CloudTrail log. You may want to specify this property when you are in a high-trust boundary, such as the same team or company.
        '''
        if __debug__:
            def stub(
                scope: aws_cdk.core.Construct,
                id: builtins.str,
                *,
                admins: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnDataLakeSettings.DataLakePrincipalProperty, typing.Dict[str, typing.Any]]]]]] = None,
                trusted_resource_owners: typing.Optional[typing.Sequence[builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDataLakeSettingsProps(
            admins=admins, trusted_resource_owners=trusted_resource_owners
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            def stub(inspector: aws_cdk.core.TreeInspector) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            def stub(props: typing.Mapping[builtins.str, typing.Any]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="admins")
    def admins(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDataLakeSettings.DataLakePrincipalProperty"]]]]:
        '''A list of AWS Lake Formation principals.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datalakesettings.html#cfn-lakeformation-datalakesettings-admins
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDataLakeSettings.DataLakePrincipalProperty"]]]], jsii.get(self, "admins"))

    @admins.setter
    def admins(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDataLakeSettings.DataLakePrincipalProperty"]]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnDataLakeSettings.DataLakePrincipalProperty]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "admins", value)

    @builtins.property
    @jsii.member(jsii_name="trustedResourceOwners")
    def trusted_resource_owners(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of UTF-8 strings.

        A list of the resource-owning account IDs that the caller's account can use to share their user access details (user ARNs). The user ARNs can be logged in the resource owner's CloudTrail log. You may want to specify this property when you are in a high-trust boundary, such as the same team or company.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datalakesettings.html#cfn-lakeformation-datalakesettings-trustedresourceowners
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "trustedResourceOwners"))

    @trusted_resource_owners.setter
    def trusted_resource_owners(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[typing.List[builtins.str]]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "trustedResourceOwners", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-lakeformation.CfnDataLakeSettings.DataLakePrincipalProperty",
        jsii_struct_bases=[],
        name_mapping={"data_lake_principal_identifier": "dataLakePrincipalIdentifier"},
    )
    class DataLakePrincipalProperty:
        def __init__(
            self,
            *,
            data_lake_principal_identifier: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The Lake Formation principal.

            :param data_lake_principal_identifier: An identifier for the Lake Formation principal.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-datalakesettings-datalakeprincipal.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_lakeformation as lakeformation
                
                data_lake_principal_property = lakeformation.CfnDataLakeSettings.DataLakePrincipalProperty(
                    data_lake_principal_identifier="dataLakePrincipalIdentifier"
                )
            '''
            if __debug__:
                def stub(
                    *,
                    data_lake_principal_identifier: typing.Optional[builtins.str] = None,
                ) -> None:
                    ...
                type_hints = typing.get_type_hints(stub)
                check_type(argname="argument data_lake_principal_identifier", value=data_lake_principal_identifier, expected_type=type_hints["data_lake_principal_identifier"])
            self._values: typing.Dict[str, typing.Any] = {}
            if data_lake_principal_identifier is not None:
                self._values["data_lake_principal_identifier"] = data_lake_principal_identifier

        @builtins.property
        def data_lake_principal_identifier(self) -> typing.Optional[builtins.str]:
            '''An identifier for the Lake Formation principal.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-datalakesettings-datalakeprincipal.html#cfn-lakeformation-datalakesettings-datalakeprincipal-datalakeprincipalidentifier
            '''
            result = self._values.get("data_lake_principal_identifier")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataLakePrincipalProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-lakeformation.CfnDataLakeSettingsProps",
    jsii_struct_bases=[],
    name_mapping={
        "admins": "admins",
        "trusted_resource_owners": "trustedResourceOwners",
    },
)
class CfnDataLakeSettingsProps:
    def __init__(
        self,
        *,
        admins: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnDataLakeSettings.DataLakePrincipalProperty, typing.Dict[str, typing.Any]]]]]] = None,
        trusted_resource_owners: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDataLakeSettings``.

        :param admins: A list of AWS Lake Formation principals.
        :param trusted_resource_owners: An array of UTF-8 strings. A list of the resource-owning account IDs that the caller's account can use to share their user access details (user ARNs). The user ARNs can be logged in the resource owner's CloudTrail log. You may want to specify this property when you are in a high-trust boundary, such as the same team or company.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datalakesettings.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_lakeformation as lakeformation
            
            cfn_data_lake_settings_props = lakeformation.CfnDataLakeSettingsProps(
                admins=[lakeformation.CfnDataLakeSettings.DataLakePrincipalProperty(
                    data_lake_principal_identifier="dataLakePrincipalIdentifier"
                )],
                trusted_resource_owners=["trustedResourceOwners"]
            )
        '''
        if __debug__:
            def stub(
                *,
                admins: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnDataLakeSettings.DataLakePrincipalProperty, typing.Dict[str, typing.Any]]]]]] = None,
                trusted_resource_owners: typing.Optional[typing.Sequence[builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument admins", value=admins, expected_type=type_hints["admins"])
            check_type(argname="argument trusted_resource_owners", value=trusted_resource_owners, expected_type=type_hints["trusted_resource_owners"])
        self._values: typing.Dict[str, typing.Any] = {}
        if admins is not None:
            self._values["admins"] = admins
        if trusted_resource_owners is not None:
            self._values["trusted_resource_owners"] = trusted_resource_owners

    @builtins.property
    def admins(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnDataLakeSettings.DataLakePrincipalProperty]]]]:
        '''A list of AWS Lake Formation principals.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datalakesettings.html#cfn-lakeformation-datalakesettings-admins
        '''
        result = self._values.get("admins")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnDataLakeSettings.DataLakePrincipalProperty]]]], result)

    @builtins.property
    def trusted_resource_owners(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of UTF-8 strings.

        A list of the resource-owning account IDs that the caller's account can use to share their user access details (user ARNs). The user ARNs can be logged in the resource owner's CloudTrail log. You may want to specify this property when you are in a high-trust boundary, such as the same team or company.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datalakesettings.html#cfn-lakeformation-datalakesettings-trustedresourceowners
        '''
        result = self._values.get("trusted_resource_owners")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDataLakeSettingsProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnPermissions(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-lakeformation.CfnPermissions",
):
    '''A CloudFormation ``AWS::LakeFormation::Permissions``.

    The ``AWS::LakeFormation::Permissions`` resource represents the permissions that a principal has on an AWS Glue Data Catalog resource (such as AWS Glue database or AWS Glue tables). When you upload a permissions stack, the permissions are granted to the principal and when you remove the stack, the permissions are revoked from the principal. If you remove a stack, and the principal does not have the permissions referenced in the stack then AWS Lake Formation will throw an error because you can’t call revoke on non-existing permissions. To successfully remove the stack, you’ll need to regrant those permissions and then remove the stack.
    .. epigraph::

       New versions of AWS Lake Formation permission resources are now available. For more information, see: `AWS:LakeFormation::PrincipalPermissions <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-principalpermissions.html>`_

    :cloudformationResource: AWS::LakeFormation::Permissions
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-permissions.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_lakeformation as lakeformation
        
        cfn_permissions = lakeformation.CfnPermissions(self, "MyCfnPermissions",
            data_lake_principal=lakeformation.CfnPermissions.DataLakePrincipalProperty(
                data_lake_principal_identifier="dataLakePrincipalIdentifier"
            ),
            resource=lakeformation.CfnPermissions.ResourceProperty(
                database_resource=lakeformation.CfnPermissions.DatabaseResourceProperty(
                    catalog_id="catalogId",
                    name="name"
                ),
                data_location_resource=lakeformation.CfnPermissions.DataLocationResourceProperty(
                    catalog_id="catalogId",
                    s3_resource="s3Resource"
                ),
                table_resource=lakeformation.CfnPermissions.TableResourceProperty(
                    catalog_id="catalogId",
                    database_name="databaseName",
                    name="name",
                    table_wildcard=lakeformation.CfnPermissions.TableWildcardProperty()
                ),
                table_with_columns_resource=lakeformation.CfnPermissions.TableWithColumnsResourceProperty(
                    catalog_id="catalogId",
                    column_names=["columnNames"],
                    column_wildcard=lakeformation.CfnPermissions.ColumnWildcardProperty(
                        excluded_column_names=["excludedColumnNames"]
                    ),
                    database_name="databaseName",
                    name="name"
                )
            ),
        
            # the properties below are optional
            permissions=["permissions"],
            permissions_with_grant_option=["permissionsWithGrantOption"]
        )
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        data_lake_principal: typing.Union[aws_cdk.core.IResolvable, typing.Union["CfnPermissions.DataLakePrincipalProperty", typing.Dict[str, typing.Any]]],
        resource: typing.Union[aws_cdk.core.IResolvable, typing.Union["CfnPermissions.ResourceProperty", typing.Dict[str, typing.Any]]],
        permissions: typing.Optional[typing.Sequence[builtins.str]] = None,
        permissions_with_grant_option: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Create a new ``AWS::LakeFormation::Permissions``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param data_lake_principal: The AWS Lake Formation principal.
        :param resource: A structure for the resource.
        :param permissions: The permissions granted or revoked.
        :param permissions_with_grant_option: Indicates the ability to grant permissions (as a subset of permissions granted).
        '''
        if __debug__:
            def stub(
                scope: aws_cdk.core.Construct,
                id: builtins.str,
                *,
                data_lake_principal: typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnPermissions.DataLakePrincipalProperty, typing.Dict[str, typing.Any]]],
                resource: typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnPermissions.ResourceProperty, typing.Dict[str, typing.Any]]],
                permissions: typing.Optional[typing.Sequence[builtins.str]] = None,
                permissions_with_grant_option: typing.Optional[typing.Sequence[builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPermissionsProps(
            data_lake_principal=data_lake_principal,
            resource=resource,
            permissions=permissions,
            permissions_with_grant_option=permissions_with_grant_option,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            def stub(inspector: aws_cdk.core.TreeInspector) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            def stub(props: typing.Mapping[builtins.str, typing.Any]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="dataLakePrincipal")
    def data_lake_principal(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnPermissions.DataLakePrincipalProperty"]:
        '''The AWS Lake Formation principal.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-permissions.html#cfn-lakeformation-permissions-datalakeprincipal
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnPermissions.DataLakePrincipalProperty"], jsii.get(self, "dataLakePrincipal"))

    @data_lake_principal.setter
    def data_lake_principal(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnPermissions.DataLakePrincipalProperty"],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Union[aws_cdk.core.IResolvable, CfnPermissions.DataLakePrincipalProperty],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataLakePrincipal", value)

    @builtins.property
    @jsii.member(jsii_name="resource")
    def resource(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnPermissions.ResourceProperty"]:
        '''A structure for the resource.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-permissions.html#cfn-lakeformation-permissions-resource
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnPermissions.ResourceProperty"], jsii.get(self, "resource"))

    @resource.setter
    def resource(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnPermissions.ResourceProperty"],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Union[aws_cdk.core.IResolvable, CfnPermissions.ResourceProperty],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resource", value)

    @builtins.property
    @jsii.member(jsii_name="permissions")
    def permissions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The permissions granted or revoked.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-permissions.html#cfn-lakeformation-permissions-permissions
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "permissions"))

    @permissions.setter
    def permissions(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            def stub(value: typing.Optional[typing.List[builtins.str]]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "permissions", value)

    @builtins.property
    @jsii.member(jsii_name="permissionsWithGrantOption")
    def permissions_with_grant_option(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Indicates the ability to grant permissions (as a subset of permissions granted).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-permissions.html#cfn-lakeformation-permissions-permissionswithgrantoption
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "permissionsWithGrantOption"))

    @permissions_with_grant_option.setter
    def permissions_with_grant_option(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[typing.List[builtins.str]]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "permissionsWithGrantOption", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-lakeformation.CfnPermissions.ColumnWildcardProperty",
        jsii_struct_bases=[],
        name_mapping={"excluded_column_names": "excludedColumnNames"},
    )
    class ColumnWildcardProperty:
        def __init__(
            self,
            *,
            excluded_column_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''A wildcard object, consisting of an optional list of excluded column names or indexes.

            :param excluded_column_names: Excludes column names. Any column with this name will be excluded.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-columnwildcard.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_lakeformation as lakeformation
                
                column_wildcard_property = lakeformation.CfnPermissions.ColumnWildcardProperty(
                    excluded_column_names=["excludedColumnNames"]
                )
            '''
            if __debug__:
                def stub(
                    *,
                    excluded_column_names: typing.Optional[typing.Sequence[builtins.str]] = None,
                ) -> None:
                    ...
                type_hints = typing.get_type_hints(stub)
                check_type(argname="argument excluded_column_names", value=excluded_column_names, expected_type=type_hints["excluded_column_names"])
            self._values: typing.Dict[str, typing.Any] = {}
            if excluded_column_names is not None:
                self._values["excluded_column_names"] = excluded_column_names

        @builtins.property
        def excluded_column_names(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Excludes column names.

            Any column with this name will be excluded.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-columnwildcard.html#cfn-lakeformation-permissions-columnwildcard-excludedcolumnnames
            '''
            result = self._values.get("excluded_column_names")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ColumnWildcardProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-lakeformation.CfnPermissions.DataLakePrincipalProperty",
        jsii_struct_bases=[],
        name_mapping={"data_lake_principal_identifier": "dataLakePrincipalIdentifier"},
    )
    class DataLakePrincipalProperty:
        def __init__(
            self,
            *,
            data_lake_principal_identifier: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The Lake Formation principal.

            :param data_lake_principal_identifier: An identifier for the Lake Formation principal.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-datalakeprincipal.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_lakeformation as lakeformation
                
                data_lake_principal_property = lakeformation.CfnPermissions.DataLakePrincipalProperty(
                    data_lake_principal_identifier="dataLakePrincipalIdentifier"
                )
            '''
            if __debug__:
                def stub(
                    *,
                    data_lake_principal_identifier: typing.Optional[builtins.str] = None,
                ) -> None:
                    ...
                type_hints = typing.get_type_hints(stub)
                check_type(argname="argument data_lake_principal_identifier", value=data_lake_principal_identifier, expected_type=type_hints["data_lake_principal_identifier"])
            self._values: typing.Dict[str, typing.Any] = {}
            if data_lake_principal_identifier is not None:
                self._values["data_lake_principal_identifier"] = data_lake_principal_identifier

        @builtins.property
        def data_lake_principal_identifier(self) -> typing.Optional[builtins.str]:
            '''An identifier for the Lake Formation principal.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-datalakeprincipal.html#cfn-lakeformation-permissions-datalakeprincipal-datalakeprincipalidentifier
            '''
            result = self._values.get("data_lake_principal_identifier")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataLakePrincipalProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-lakeformation.CfnPermissions.DataLocationResourceProperty",
        jsii_struct_bases=[],
        name_mapping={"catalog_id": "catalogId", "s3_resource": "s3Resource"},
    )
    class DataLocationResourceProperty:
        def __init__(
            self,
            *,
            catalog_id: typing.Optional[builtins.str] = None,
            s3_resource: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A structure for a data location object where permissions are granted or revoked.

            :param catalog_id: The identifier for the Data Catalog . By default, it is the account ID of the caller.
            :param s3_resource: The Amazon Resource Name (ARN) that uniquely identifies the data location resource.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-datalocationresource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_lakeformation as lakeformation
                
                data_location_resource_property = lakeformation.CfnPermissions.DataLocationResourceProperty(
                    catalog_id="catalogId",
                    s3_resource="s3Resource"
                )
            '''
            if __debug__:
                def stub(
                    *,
                    catalog_id: typing.Optional[builtins.str] = None,
                    s3_resource: typing.Optional[builtins.str] = None,
                ) -> None:
                    ...
                type_hints = typing.get_type_hints(stub)
                check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
                check_type(argname="argument s3_resource", value=s3_resource, expected_type=type_hints["s3_resource"])
            self._values: typing.Dict[str, typing.Any] = {}
            if catalog_id is not None:
                self._values["catalog_id"] = catalog_id
            if s3_resource is not None:
                self._values["s3_resource"] = s3_resource

        @builtins.property
        def catalog_id(self) -> typing.Optional[builtins.str]:
            '''The identifier for the Data Catalog .

            By default, it is the account ID of the caller.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-datalocationresource.html#cfn-lakeformation-permissions-datalocationresource-catalogid
            '''
            result = self._values.get("catalog_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3_resource(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) that uniquely identifies the data location resource.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-datalocationresource.html#cfn-lakeformation-permissions-datalocationresource-s3resource
            '''
            result = self._values.get("s3_resource")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataLocationResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-lakeformation.CfnPermissions.DatabaseResourceProperty",
        jsii_struct_bases=[],
        name_mapping={"catalog_id": "catalogId", "name": "name"},
    )
    class DatabaseResourceProperty:
        def __init__(
            self,
            *,
            catalog_id: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A structure for the database object.

            :param catalog_id: The identifier for the Data Catalog . By default, it is the account ID of the caller.
            :param name: The name of the database resource. Unique to the Data Catalog.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-databaseresource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_lakeformation as lakeformation
                
                database_resource_property = lakeformation.CfnPermissions.DatabaseResourceProperty(
                    catalog_id="catalogId",
                    name="name"
                )
            '''
            if __debug__:
                def stub(
                    *,
                    catalog_id: typing.Optional[builtins.str] = None,
                    name: typing.Optional[builtins.str] = None,
                ) -> None:
                    ...
                type_hints = typing.get_type_hints(stub)
                check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[str, typing.Any] = {}
            if catalog_id is not None:
                self._values["catalog_id"] = catalog_id
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def catalog_id(self) -> typing.Optional[builtins.str]:
            '''The identifier for the Data Catalog .

            By default, it is the account ID of the caller.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-databaseresource.html#cfn-lakeformation-permissions-databaseresource-catalogid
            '''
            result = self._values.get("catalog_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the database resource.

            Unique to the Data Catalog.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-databaseresource.html#cfn-lakeformation-permissions-databaseresource-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DatabaseResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-lakeformation.CfnPermissions.ResourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "database_resource": "databaseResource",
            "data_location_resource": "dataLocationResource",
            "table_resource": "tableResource",
            "table_with_columns_resource": "tableWithColumnsResource",
        },
    )
    class ResourceProperty:
        def __init__(
            self,
            *,
            database_resource: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union["CfnPermissions.DatabaseResourceProperty", typing.Dict[str, typing.Any]]]] = None,
            data_location_resource: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union["CfnPermissions.DataLocationResourceProperty", typing.Dict[str, typing.Any]]]] = None,
            table_resource: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union["CfnPermissions.TableResourceProperty", typing.Dict[str, typing.Any]]]] = None,
            table_with_columns_resource: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union["CfnPermissions.TableWithColumnsResourceProperty", typing.Dict[str, typing.Any]]]] = None,
        ) -> None:
            '''A structure for the resource.

            :param database_resource: A structure for the database object.
            :param data_location_resource: A structure for a data location object where permissions are granted or revoked.
            :param table_resource: A structure for the table object. A table is a metadata definition that represents your data. You can Grant and Revoke table privileges to a principal.
            :param table_with_columns_resource: A structure for a table with columns object. This object is only used when granting a SELECT permission.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-resource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_lakeformation as lakeformation
                
                resource_property = lakeformation.CfnPermissions.ResourceProperty(
                    database_resource=lakeformation.CfnPermissions.DatabaseResourceProperty(
                        catalog_id="catalogId",
                        name="name"
                    ),
                    data_location_resource=lakeformation.CfnPermissions.DataLocationResourceProperty(
                        catalog_id="catalogId",
                        s3_resource="s3Resource"
                    ),
                    table_resource=lakeformation.CfnPermissions.TableResourceProperty(
                        catalog_id="catalogId",
                        database_name="databaseName",
                        name="name",
                        table_wildcard=lakeformation.CfnPermissions.TableWildcardProperty()
                    ),
                    table_with_columns_resource=lakeformation.CfnPermissions.TableWithColumnsResourceProperty(
                        catalog_id="catalogId",
                        column_names=["columnNames"],
                        column_wildcard=lakeformation.CfnPermissions.ColumnWildcardProperty(
                            excluded_column_names=["excludedColumnNames"]
                        ),
                        database_name="databaseName",
                        name="name"
                    )
                )
            '''
            if __debug__:
                def stub(
                    *,
                    database_resource: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnPermissions.DatabaseResourceProperty, typing.Dict[str, typing.Any]]]] = None,
                    data_location_resource: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnPermissions.DataLocationResourceProperty, typing.Dict[str, typing.Any]]]] = None,
                    table_resource: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnPermissions.TableResourceProperty, typing.Dict[str, typing.Any]]]] = None,
                    table_with_columns_resource: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnPermissions.TableWithColumnsResourceProperty, typing.Dict[str, typing.Any]]]] = None,
                ) -> None:
                    ...
                type_hints = typing.get_type_hints(stub)
                check_type(argname="argument database_resource", value=database_resource, expected_type=type_hints["database_resource"])
                check_type(argname="argument data_location_resource", value=data_location_resource, expected_type=type_hints["data_location_resource"])
                check_type(argname="argument table_resource", value=table_resource, expected_type=type_hints["table_resource"])
                check_type(argname="argument table_with_columns_resource", value=table_with_columns_resource, expected_type=type_hints["table_with_columns_resource"])
            self._values: typing.Dict[str, typing.Any] = {}
            if database_resource is not None:
                self._values["database_resource"] = database_resource
            if data_location_resource is not None:
                self._values["data_location_resource"] = data_location_resource
            if table_resource is not None:
                self._values["table_resource"] = table_resource
            if table_with_columns_resource is not None:
                self._values["table_with_columns_resource"] = table_with_columns_resource

        @builtins.property
        def database_resource(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPermissions.DatabaseResourceProperty"]]:
            '''A structure for the database object.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-resource.html#cfn-lakeformation-permissions-resource-databaseresource
            '''
            result = self._values.get("database_resource")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPermissions.DatabaseResourceProperty"]], result)

        @builtins.property
        def data_location_resource(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPermissions.DataLocationResourceProperty"]]:
            '''A structure for a data location object where permissions are granted or revoked.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-resource.html#cfn-lakeformation-permissions-resource-datalocationresource
            '''
            result = self._values.get("data_location_resource")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPermissions.DataLocationResourceProperty"]], result)

        @builtins.property
        def table_resource(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPermissions.TableResourceProperty"]]:
            '''A structure for the table object.

            A table is a metadata definition that represents your data. You can Grant and Revoke table privileges to a principal.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-resource.html#cfn-lakeformation-permissions-resource-tableresource
            '''
            result = self._values.get("table_resource")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPermissions.TableResourceProperty"]], result)

        @builtins.property
        def table_with_columns_resource(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPermissions.TableWithColumnsResourceProperty"]]:
            '''A structure for a table with columns object.

            This object is only used when granting a SELECT permission.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-resource.html#cfn-lakeformation-permissions-resource-tablewithcolumnsresource
            '''
            result = self._values.get("table_with_columns_resource")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPermissions.TableWithColumnsResourceProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-lakeformation.CfnPermissions.TableResourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "catalog_id": "catalogId",
            "database_name": "databaseName",
            "name": "name",
            "table_wildcard": "tableWildcard",
        },
    )
    class TableResourceProperty:
        def __init__(
            self,
            *,
            catalog_id: typing.Optional[builtins.str] = None,
            database_name: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
            table_wildcard: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union["CfnPermissions.TableWildcardProperty", typing.Dict[str, typing.Any]]]] = None,
        ) -> None:
            '''A structure for the table object.

            A table is a metadata definition that represents your data. You can Grant and Revoke table privileges to a principal.

            :param catalog_id: The identifier for the Data Catalog . By default, it is the account ID of the caller.
            :param database_name: The name of the database for the table. Unique to a Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database privileges to a principal.
            :param name: The name of the table.
            :param table_wildcard: An empty object representing all tables under a database. If this field is specified instead of the ``Name`` field, all tables under ``DatabaseName`` will have permission changes applied.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tableresource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_lakeformation as lakeformation
                
                table_resource_property = lakeformation.CfnPermissions.TableResourceProperty(
                    catalog_id="catalogId",
                    database_name="databaseName",
                    name="name",
                    table_wildcard=lakeformation.CfnPermissions.TableWildcardProperty()
                )
            '''
            if __debug__:
                def stub(
                    *,
                    catalog_id: typing.Optional[builtins.str] = None,
                    database_name: typing.Optional[builtins.str] = None,
                    name: typing.Optional[builtins.str] = None,
                    table_wildcard: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnPermissions.TableWildcardProperty, typing.Dict[str, typing.Any]]]] = None,
                ) -> None:
                    ...
                type_hints = typing.get_type_hints(stub)
                check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
                check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument table_wildcard", value=table_wildcard, expected_type=type_hints["table_wildcard"])
            self._values: typing.Dict[str, typing.Any] = {}
            if catalog_id is not None:
                self._values["catalog_id"] = catalog_id
            if database_name is not None:
                self._values["database_name"] = database_name
            if name is not None:
                self._values["name"] = name
            if table_wildcard is not None:
                self._values["table_wildcard"] = table_wildcard

        @builtins.property
        def catalog_id(self) -> typing.Optional[builtins.str]:
            '''The identifier for the Data Catalog .

            By default, it is the account ID of the caller.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tableresource.html#cfn-lakeformation-permissions-tableresource-catalogid
            '''
            result = self._values.get("catalog_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def database_name(self) -> typing.Optional[builtins.str]:
            '''The name of the database for the table.

            Unique to a Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database privileges to a principal.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tableresource.html#cfn-lakeformation-permissions-tableresource-databasename
            '''
            result = self._values.get("database_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the table.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tableresource.html#cfn-lakeformation-permissions-tableresource-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def table_wildcard(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPermissions.TableWildcardProperty"]]:
            '''An empty object representing all tables under a database.

            If this field is specified instead of the ``Name`` field, all tables under ``DatabaseName`` will have permission changes applied.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tableresource.html#cfn-lakeformation-permissions-tableresource-tablewildcard
            '''
            result = self._values.get("table_wildcard")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPermissions.TableWildcardProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TableResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-lakeformation.CfnPermissions.TableWildcardProperty",
        jsii_struct_bases=[],
        name_mapping={},
    )
    class TableWildcardProperty:
        def __init__(self) -> None:
            '''A wildcard object representing every table under a database.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewildcard.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_lakeformation as lakeformation
                
                table_wildcard_property = lakeformation.CfnPermissions.TableWildcardProperty()
            '''
            self._values: typing.Dict[str, typing.Any] = {}

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TableWildcardProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-lakeformation.CfnPermissions.TableWithColumnsResourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "catalog_id": "catalogId",
            "column_names": "columnNames",
            "column_wildcard": "columnWildcard",
            "database_name": "databaseName",
            "name": "name",
        },
    )
    class TableWithColumnsResourceProperty:
        def __init__(
            self,
            *,
            catalog_id: typing.Optional[builtins.str] = None,
            column_names: typing.Optional[typing.Sequence[builtins.str]] = None,
            column_wildcard: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union["CfnPermissions.ColumnWildcardProperty", typing.Dict[str, typing.Any]]]] = None,
            database_name: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A structure for a table with columns object. This object is only used when granting a SELECT permission.

            This object must take a value for at least one of ``ColumnsNames`` , ``ColumnsIndexes`` , or ``ColumnsWildcard`` .

            :param catalog_id: The identifier for the Data Catalog . By default, it is the account ID of the caller.
            :param column_names: The list of column names for the table. At least one of ``ColumnNames`` or ``ColumnWildcard`` is required.
            :param column_wildcard: A wildcard specified by a ``ColumnWildcard`` object. At least one of ``ColumnNames`` or ``ColumnWildcard`` is required.
            :param database_name: The name of the database for the table with columns resource. Unique to the Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database privileges to a principal.
            :param name: The name of the table resource. A table is a metadata definition that represents your data. You can Grant and Revoke table privileges to a principal.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewithcolumnsresource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_lakeformation as lakeformation
                
                table_with_columns_resource_property = lakeformation.CfnPermissions.TableWithColumnsResourceProperty(
                    catalog_id="catalogId",
                    column_names=["columnNames"],
                    column_wildcard=lakeformation.CfnPermissions.ColumnWildcardProperty(
                        excluded_column_names=["excludedColumnNames"]
                    ),
                    database_name="databaseName",
                    name="name"
                )
            '''
            if __debug__:
                def stub(
                    *,
                    catalog_id: typing.Optional[builtins.str] = None,
                    column_names: typing.Optional[typing.Sequence[builtins.str]] = None,
                    column_wildcard: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnPermissions.ColumnWildcardProperty, typing.Dict[str, typing.Any]]]] = None,
                    database_name: typing.Optional[builtins.str] = None,
                    name: typing.Optional[builtins.str] = None,
                ) -> None:
                    ...
                type_hints = typing.get_type_hints(stub)
                check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
                check_type(argname="argument column_names", value=column_names, expected_type=type_hints["column_names"])
                check_type(argname="argument column_wildcard", value=column_wildcard, expected_type=type_hints["column_wildcard"])
                check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[str, typing.Any] = {}
            if catalog_id is not None:
                self._values["catalog_id"] = catalog_id
            if column_names is not None:
                self._values["column_names"] = column_names
            if column_wildcard is not None:
                self._values["column_wildcard"] = column_wildcard
            if database_name is not None:
                self._values["database_name"] = database_name
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def catalog_id(self) -> typing.Optional[builtins.str]:
            '''The identifier for the Data Catalog .

            By default, it is the account ID of the caller.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewithcolumnsresource.html#cfn-lakeformation-permissions-tablewithcolumnsresource-catalogid
            '''
            result = self._values.get("catalog_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def column_names(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The list of column names for the table.

            At least one of ``ColumnNames`` or ``ColumnWildcard`` is required.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewithcolumnsresource.html#cfn-lakeformation-permissions-tablewithcolumnsresource-columnnames
            '''
            result = self._values.get("column_names")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def column_wildcard(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPermissions.ColumnWildcardProperty"]]:
            '''A wildcard specified by a ``ColumnWildcard`` object.

            At least one of ``ColumnNames`` or ``ColumnWildcard`` is required.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewithcolumnsresource.html#cfn-lakeformation-permissions-tablewithcolumnsresource-columnwildcard
            '''
            result = self._values.get("column_wildcard")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPermissions.ColumnWildcardProperty"]], result)

        @builtins.property
        def database_name(self) -> typing.Optional[builtins.str]:
            '''The name of the database for the table with columns resource.

            Unique to the Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database privileges to a principal.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewithcolumnsresource.html#cfn-lakeformation-permissions-tablewithcolumnsresource-databasename
            '''
            result = self._values.get("database_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the table resource.

            A table is a metadata definition that represents your data. You can Grant and Revoke table privileges to a principal.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewithcolumnsresource.html#cfn-lakeformation-permissions-tablewithcolumnsresource-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TableWithColumnsResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-lakeformation.CfnPermissionsProps",
    jsii_struct_bases=[],
    name_mapping={
        "data_lake_principal": "dataLakePrincipal",
        "resource": "resource",
        "permissions": "permissions",
        "permissions_with_grant_option": "permissionsWithGrantOption",
    },
)
class CfnPermissionsProps:
    def __init__(
        self,
        *,
        data_lake_principal: typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnPermissions.DataLakePrincipalProperty, typing.Dict[str, typing.Any]]],
        resource: typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnPermissions.ResourceProperty, typing.Dict[str, typing.Any]]],
        permissions: typing.Optional[typing.Sequence[builtins.str]] = None,
        permissions_with_grant_option: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnPermissions``.

        :param data_lake_principal: The AWS Lake Formation principal.
        :param resource: A structure for the resource.
        :param permissions: The permissions granted or revoked.
        :param permissions_with_grant_option: Indicates the ability to grant permissions (as a subset of permissions granted).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-permissions.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_lakeformation as lakeformation
            
            cfn_permissions_props = lakeformation.CfnPermissionsProps(
                data_lake_principal=lakeformation.CfnPermissions.DataLakePrincipalProperty(
                    data_lake_principal_identifier="dataLakePrincipalIdentifier"
                ),
                resource=lakeformation.CfnPermissions.ResourceProperty(
                    database_resource=lakeformation.CfnPermissions.DatabaseResourceProperty(
                        catalog_id="catalogId",
                        name="name"
                    ),
                    data_location_resource=lakeformation.CfnPermissions.DataLocationResourceProperty(
                        catalog_id="catalogId",
                        s3_resource="s3Resource"
                    ),
                    table_resource=lakeformation.CfnPermissions.TableResourceProperty(
                        catalog_id="catalogId",
                        database_name="databaseName",
                        name="name",
                        table_wildcard=lakeformation.CfnPermissions.TableWildcardProperty()
                    ),
                    table_with_columns_resource=lakeformation.CfnPermissions.TableWithColumnsResourceProperty(
                        catalog_id="catalogId",
                        column_names=["columnNames"],
                        column_wildcard=lakeformation.CfnPermissions.ColumnWildcardProperty(
                            excluded_column_names=["excludedColumnNames"]
                        ),
                        database_name="databaseName",
                        name="name"
                    )
                ),
            
                # the properties below are optional
                permissions=["permissions"],
                permissions_with_grant_option=["permissionsWithGrantOption"]
            )
        '''
        if __debug__:
            def stub(
                *,
                data_lake_principal: typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnPermissions.DataLakePrincipalProperty, typing.Dict[str, typing.Any]]],
                resource: typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnPermissions.ResourceProperty, typing.Dict[str, typing.Any]]],
                permissions: typing.Optional[typing.Sequence[builtins.str]] = None,
                permissions_with_grant_option: typing.Optional[typing.Sequence[builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument data_lake_principal", value=data_lake_principal, expected_type=type_hints["data_lake_principal"])
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
            check_type(argname="argument permissions", value=permissions, expected_type=type_hints["permissions"])
            check_type(argname="argument permissions_with_grant_option", value=permissions_with_grant_option, expected_type=type_hints["permissions_with_grant_option"])
        self._values: typing.Dict[str, typing.Any] = {
            "data_lake_principal": data_lake_principal,
            "resource": resource,
        }
        if permissions is not None:
            self._values["permissions"] = permissions
        if permissions_with_grant_option is not None:
            self._values["permissions_with_grant_option"] = permissions_with_grant_option

    @builtins.property
    def data_lake_principal(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnPermissions.DataLakePrincipalProperty]:
        '''The AWS Lake Formation principal.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-permissions.html#cfn-lakeformation-permissions-datalakeprincipal
        '''
        result = self._values.get("data_lake_principal")
        assert result is not None, "Required property 'data_lake_principal' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnPermissions.DataLakePrincipalProperty], result)

    @builtins.property
    def resource(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnPermissions.ResourceProperty]:
        '''A structure for the resource.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-permissions.html#cfn-lakeformation-permissions-resource
        '''
        result = self._values.get("resource")
        assert result is not None, "Required property 'resource' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnPermissions.ResourceProperty], result)

    @builtins.property
    def permissions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The permissions granted or revoked.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-permissions.html#cfn-lakeformation-permissions-permissions
        '''
        result = self._values.get("permissions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def permissions_with_grant_option(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Indicates the ability to grant permissions (as a subset of permissions granted).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-permissions.html#cfn-lakeformation-permissions-permissionswithgrantoption
        '''
        result = self._values.get("permissions_with_grant_option")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPermissionsProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnPrincipalPermissions(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-lakeformation.CfnPrincipalPermissions",
):
    '''A CloudFormation ``AWS::LakeFormation::PrincipalPermissions``.

    The ``AWS::LakeFormation::PrincipalPermissions`` resource represents the permissions that a principal has on a Data Catalog resource (such as AWS Glue databases or AWS Glue tables). When you create a ``PrincipalPermissions`` resource, the permissions are granted via the AWS Lake Formation ``GrantPermissions`` API operation. When you delete a ``PrincipalPermissions`` resource, the permissions on principal-resource pair are revoked via the AWS Lake Formation ``RevokePermissions`` API operation.

    :cloudformationResource: AWS::LakeFormation::PrincipalPermissions
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-principalpermissions.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_lakeformation as lakeformation
        
        # catalog: Any
        # table_wildcard: Any
        
        cfn_principal_permissions = lakeformation.CfnPrincipalPermissions(self, "MyCfnPrincipalPermissions",
            permissions=["permissions"],
            permissions_with_grant_option=["permissionsWithGrantOption"],
            principal=lakeformation.CfnPrincipalPermissions.DataLakePrincipalProperty(
                data_lake_principal_identifier="dataLakePrincipalIdentifier"
            ),
            resource=lakeformation.CfnPrincipalPermissions.ResourceProperty(
                catalog=catalog,
                database=lakeformation.CfnPrincipalPermissions.DatabaseResourceProperty(
                    catalog_id="catalogId",
                    name="name"
                ),
                data_cells_filter=lakeformation.CfnPrincipalPermissions.DataCellsFilterResourceProperty(
                    database_name="databaseName",
                    name="name",
                    table_catalog_id="tableCatalogId",
                    table_name="tableName"
                ),
                data_location=lakeformation.CfnPrincipalPermissions.DataLocationResourceProperty(
                    catalog_id="catalogId",
                    resource_arn="resourceArn"
                ),
                lf_tag=lakeformation.CfnPrincipalPermissions.LFTagKeyResourceProperty(
                    catalog_id="catalogId",
                    tag_key="tagKey",
                    tag_values=["tagValues"]
                ),
                lf_tag_policy=lakeformation.CfnPrincipalPermissions.LFTagPolicyResourceProperty(
                    catalog_id="catalogId",
                    expression=[lakeformation.CfnPrincipalPermissions.LFTagProperty(
                        tag_key="tagKey",
                        tag_values=["tagValues"]
                    )],
                    resource_type="resourceType"
                ),
                table=lakeformation.CfnPrincipalPermissions.TableResourceProperty(
                    catalog_id="catalogId",
                    database_name="databaseName",
        
                    # the properties below are optional
                    name="name",
                    table_wildcard=table_wildcard
                ),
                table_with_columns=lakeformation.CfnPrincipalPermissions.TableWithColumnsResourceProperty(
                    catalog_id="catalogId",
                    database_name="databaseName",
                    name="name",
        
                    # the properties below are optional
                    column_names=["columnNames"],
                    column_wildcard=lakeformation.CfnPrincipalPermissions.ColumnWildcardProperty(
                        excluded_column_names=["excludedColumnNames"]
                    )
                )
            ),
        
            # the properties below are optional
            catalog="catalog"
        )
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        permissions: typing.Sequence[builtins.str],
        permissions_with_grant_option: typing.Sequence[builtins.str],
        principal: typing.Union[aws_cdk.core.IResolvable, typing.Union["CfnPrincipalPermissions.DataLakePrincipalProperty", typing.Dict[str, typing.Any]]],
        resource: typing.Union[aws_cdk.core.IResolvable, typing.Union["CfnPrincipalPermissions.ResourceProperty", typing.Dict[str, typing.Any]]],
        catalog: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::LakeFormation::PrincipalPermissions``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param permissions: The permissions granted or revoked.
        :param permissions_with_grant_option: Indicates the ability to grant permissions (as a subset of permissions granted).
        :param principal: The principal to be granted a permission.
        :param resource: The resource to be granted or revoked permissions.
        :param catalog: The identifier for the Data Catalog . By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment.
        '''
        if __debug__:
            def stub(
                scope: aws_cdk.core.Construct,
                id: builtins.str,
                *,
                permissions: typing.Sequence[builtins.str],
                permissions_with_grant_option: typing.Sequence[builtins.str],
                principal: typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnPrincipalPermissions.DataLakePrincipalProperty, typing.Dict[str, typing.Any]]],
                resource: typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnPrincipalPermissions.ResourceProperty, typing.Dict[str, typing.Any]]],
                catalog: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPrincipalPermissionsProps(
            permissions=permissions,
            permissions_with_grant_option=permissions_with_grant_option,
            principal=principal,
            resource=resource,
            catalog=catalog,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            def stub(inspector: aws_cdk.core.TreeInspector) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            def stub(props: typing.Mapping[builtins.str, typing.Any]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrPrincipalIdentifier")
    def attr_principal_identifier(self) -> builtins.str:
        '''Json encoding of the input principal.

        For example: ``{"DataLakePrincipalIdentifier":"arn:aws:iam::123456789012:role/ExampleRole"}``

        :cloudformationAttribute: PrincipalIdentifier
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPrincipalIdentifier"))

    @builtins.property
    @jsii.member(jsii_name="attrResourceIdentifier")
    def attr_resource_identifier(self) -> builtins.str:
        '''Json encoding of the input resource.

        For example: ``{"Catalog":null,"Database":null,"Table":null,"TableWithColumns":null,"DataLocation":null,"DataCellsFilter":{"TableCatalogId":"123456789012","DatabaseName":"ExampleDatabase","TableName":"ExampleTable","Name":"ExampleFilter"},"LFTag":null,"LFTagPolicy":null}``

        :cloudformationAttribute: ResourceIdentifier
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrResourceIdentifier"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="permissions")
    def permissions(self) -> typing.List[builtins.str]:
        '''The permissions granted or revoked.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-principalpermissions.html#cfn-lakeformation-principalpermissions-permissions
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "permissions"))

    @permissions.setter
    def permissions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "permissions", value)

    @builtins.property
    @jsii.member(jsii_name="permissionsWithGrantOption")
    def permissions_with_grant_option(self) -> typing.List[builtins.str]:
        '''Indicates the ability to grant permissions (as a subset of permissions granted).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-principalpermissions.html#cfn-lakeformation-principalpermissions-permissionswithgrantoption
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "permissionsWithGrantOption"))

    @permissions_with_grant_option.setter
    def permissions_with_grant_option(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "permissionsWithGrantOption", value)

    @builtins.property
    @jsii.member(jsii_name="principal")
    def principal(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnPrincipalPermissions.DataLakePrincipalProperty"]:
        '''The principal to be granted a permission.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-principalpermissions.html#cfn-lakeformation-principalpermissions-principal
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnPrincipalPermissions.DataLakePrincipalProperty"], jsii.get(self, "principal"))

    @principal.setter
    def principal(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnPrincipalPermissions.DataLakePrincipalProperty"],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Union[aws_cdk.core.IResolvable, CfnPrincipalPermissions.DataLakePrincipalProperty],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "principal", value)

    @builtins.property
    @jsii.member(jsii_name="resource")
    def resource(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnPrincipalPermissions.ResourceProperty"]:
        '''The resource to be granted or revoked permissions.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-principalpermissions.html#cfn-lakeformation-principalpermissions-resource
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnPrincipalPermissions.ResourceProperty"], jsii.get(self, "resource"))

    @resource.setter
    def resource(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnPrincipalPermissions.ResourceProperty"],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Union[aws_cdk.core.IResolvable, CfnPrincipalPermissions.ResourceProperty],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resource", value)

    @builtins.property
    @jsii.member(jsii_name="catalog")
    def catalog(self) -> typing.Optional[builtins.str]:
        '''The identifier for the Data Catalog .

        By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-principalpermissions.html#cfn-lakeformation-principalpermissions-catalog
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "catalog"))

    @catalog.setter
    def catalog(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.Optional[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "catalog", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-lakeformation.CfnPrincipalPermissions.ColumnWildcardProperty",
        jsii_struct_bases=[],
        name_mapping={"excluded_column_names": "excludedColumnNames"},
    )
    class ColumnWildcardProperty:
        def __init__(
            self,
            *,
            excluded_column_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''A wildcard object, consisting of an optional list of excluded column names or indexes.

            :param excluded_column_names: Excludes column names. Any column with this name will be excluded.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-columnwildcard.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_lakeformation as lakeformation
                
                column_wildcard_property = lakeformation.CfnPrincipalPermissions.ColumnWildcardProperty(
                    excluded_column_names=["excludedColumnNames"]
                )
            '''
            if __debug__:
                def stub(
                    *,
                    excluded_column_names: typing.Optional[typing.Sequence[builtins.str]] = None,
                ) -> None:
                    ...
                type_hints = typing.get_type_hints(stub)
                check_type(argname="argument excluded_column_names", value=excluded_column_names, expected_type=type_hints["excluded_column_names"])
            self._values: typing.Dict[str, typing.Any] = {}
            if excluded_column_names is not None:
                self._values["excluded_column_names"] = excluded_column_names

        @builtins.property
        def excluded_column_names(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Excludes column names.

            Any column with this name will be excluded.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-columnwildcard.html#cfn-lakeformation-principalpermissions-columnwildcard-excludedcolumnnames
            '''
            result = self._values.get("excluded_column_names")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ColumnWildcardProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-lakeformation.CfnPrincipalPermissions.DataCellsFilterResourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "database_name": "databaseName",
            "name": "name",
            "table_catalog_id": "tableCatalogId",
            "table_name": "tableName",
        },
    )
    class DataCellsFilterResourceProperty:
        def __init__(
            self,
            *,
            database_name: builtins.str,
            name: builtins.str,
            table_catalog_id: builtins.str,
            table_name: builtins.str,
        ) -> None:
            '''A structure that describes certain columns on certain rows.

            :param database_name: A database in the Data Catalog .
            :param name: The name given by the user to the data filter cell.
            :param table_catalog_id: The ID of the catalog to which the table belongs.
            :param table_name: The name of the table.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-datacellsfilterresource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_lakeformation as lakeformation
                
                data_cells_filter_resource_property = lakeformation.CfnPrincipalPermissions.DataCellsFilterResourceProperty(
                    database_name="databaseName",
                    name="name",
                    table_catalog_id="tableCatalogId",
                    table_name="tableName"
                )
            '''
            if __debug__:
                def stub(
                    *,
                    database_name: builtins.str,
                    name: builtins.str,
                    table_catalog_id: builtins.str,
                    table_name: builtins.str,
                ) -> None:
                    ...
                type_hints = typing.get_type_hints(stub)
                check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument table_catalog_id", value=table_catalog_id, expected_type=type_hints["table_catalog_id"])
                check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
            self._values: typing.Dict[str, typing.Any] = {
                "database_name": database_name,
                "name": name,
                "table_catalog_id": table_catalog_id,
                "table_name": table_name,
            }

        @builtins.property
        def database_name(self) -> builtins.str:
            '''A database in the Data Catalog .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-datacellsfilterresource.html#cfn-lakeformation-principalpermissions-datacellsfilterresource-databasename
            '''
            result = self._values.get("database_name")
            assert result is not None, "Required property 'database_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> builtins.str:
            '''The name given by the user to the data filter cell.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-datacellsfilterresource.html#cfn-lakeformation-principalpermissions-datacellsfilterresource-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def table_catalog_id(self) -> builtins.str:
            '''The ID of the catalog to which the table belongs.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-datacellsfilterresource.html#cfn-lakeformation-principalpermissions-datacellsfilterresource-tablecatalogid
            '''
            result = self._values.get("table_catalog_id")
            assert result is not None, "Required property 'table_catalog_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def table_name(self) -> builtins.str:
            '''The name of the table.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-datacellsfilterresource.html#cfn-lakeformation-principalpermissions-datacellsfilterresource-tablename
            '''
            result = self._values.get("table_name")
            assert result is not None, "Required property 'table_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataCellsFilterResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-lakeformation.CfnPrincipalPermissions.DataLakePrincipalProperty",
        jsii_struct_bases=[],
        name_mapping={"data_lake_principal_identifier": "dataLakePrincipalIdentifier"},
    )
    class DataLakePrincipalProperty:
        def __init__(
            self,
            *,
            data_lake_principal_identifier: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The AWS Lake Formation principal.

            :param data_lake_principal_identifier: An identifier for the AWS Lake Formation principal.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-datalakeprincipal.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_lakeformation as lakeformation
                
                data_lake_principal_property = lakeformation.CfnPrincipalPermissions.DataLakePrincipalProperty(
                    data_lake_principal_identifier="dataLakePrincipalIdentifier"
                )
            '''
            if __debug__:
                def stub(
                    *,
                    data_lake_principal_identifier: typing.Optional[builtins.str] = None,
                ) -> None:
                    ...
                type_hints = typing.get_type_hints(stub)
                check_type(argname="argument data_lake_principal_identifier", value=data_lake_principal_identifier, expected_type=type_hints["data_lake_principal_identifier"])
            self._values: typing.Dict[str, typing.Any] = {}
            if data_lake_principal_identifier is not None:
                self._values["data_lake_principal_identifier"] = data_lake_principal_identifier

        @builtins.property
        def data_lake_principal_identifier(self) -> typing.Optional[builtins.str]:
            '''An identifier for the AWS Lake Formation principal.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-datalakeprincipal.html#cfn-lakeformation-principalpermissions-datalakeprincipal-datalakeprincipalidentifier
            '''
            result = self._values.get("data_lake_principal_identifier")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataLakePrincipalProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-lakeformation.CfnPrincipalPermissions.DataLocationResourceProperty",
        jsii_struct_bases=[],
        name_mapping={"catalog_id": "catalogId", "resource_arn": "resourceArn"},
    )
    class DataLocationResourceProperty:
        def __init__(
            self,
            *,
            catalog_id: builtins.str,
            resource_arn: builtins.str,
        ) -> None:
            '''A structure for a data location object where permissions are granted or revoked.

            :param catalog_id: The identifier for the Data Catalog where the location is registered with AWS Lake Formation .
            :param resource_arn: The Amazon Resource Name (ARN) that uniquely identifies the data location resource.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-datalocationresource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_lakeformation as lakeformation
                
                data_location_resource_property = lakeformation.CfnPrincipalPermissions.DataLocationResourceProperty(
                    catalog_id="catalogId",
                    resource_arn="resourceArn"
                )
            '''
            if __debug__:
                def stub(
                    *,
                    catalog_id: builtins.str,
                    resource_arn: builtins.str,
                ) -> None:
                    ...
                type_hints = typing.get_type_hints(stub)
                check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
                check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
            self._values: typing.Dict[str, typing.Any] = {
                "catalog_id": catalog_id,
                "resource_arn": resource_arn,
            }

        @builtins.property
        def catalog_id(self) -> builtins.str:
            '''The identifier for the Data Catalog where the location is registered with AWS Lake Formation .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-datalocationresource.html#cfn-lakeformation-principalpermissions-datalocationresource-catalogid
            '''
            result = self._values.get("catalog_id")
            assert result is not None, "Required property 'catalog_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def resource_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) that uniquely identifies the data location resource.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-datalocationresource.html#cfn-lakeformation-principalpermissions-datalocationresource-resourcearn
            '''
            result = self._values.get("resource_arn")
            assert result is not None, "Required property 'resource_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataLocationResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-lakeformation.CfnPrincipalPermissions.DatabaseResourceProperty",
        jsii_struct_bases=[],
        name_mapping={"catalog_id": "catalogId", "name": "name"},
    )
    class DatabaseResourceProperty:
        def __init__(self, *, catalog_id: builtins.str, name: builtins.str) -> None:
            '''A structure for the database object.

            :param catalog_id: The identifier for the Data Catalog. By default, it is the account ID of the caller.
            :param name: The name of the database resource. Unique to the Data Catalog.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-databaseresource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_lakeformation as lakeformation
                
                database_resource_property = lakeformation.CfnPrincipalPermissions.DatabaseResourceProperty(
                    catalog_id="catalogId",
                    name="name"
                )
            '''
            if __debug__:
                def stub(*, catalog_id: builtins.str, name: builtins.str) -> None:
                    ...
                type_hints = typing.get_type_hints(stub)
                check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[str, typing.Any] = {
                "catalog_id": catalog_id,
                "name": name,
            }

        @builtins.property
        def catalog_id(self) -> builtins.str:
            '''The identifier for the Data Catalog.

            By default, it is the account ID of the caller.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-databaseresource.html#cfn-lakeformation-principalpermissions-databaseresource-catalogid
            '''
            result = self._values.get("catalog_id")
            assert result is not None, "Required property 'catalog_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the database resource.

            Unique to the Data Catalog.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-databaseresource.html#cfn-lakeformation-principalpermissions-databaseresource-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DatabaseResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-lakeformation.CfnPrincipalPermissions.LFTagKeyResourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "catalog_id": "catalogId",
            "tag_key": "tagKey",
            "tag_values": "tagValues",
        },
    )
    class LFTagKeyResourceProperty:
        def __init__(
            self,
            *,
            catalog_id: builtins.str,
            tag_key: builtins.str,
            tag_values: typing.Sequence[builtins.str],
        ) -> None:
            '''A structure containing an LF-tag key and values for a resource.

            :param catalog_id: The identifier for the Data Catalog where the location is registered with Data Catalog .
            :param tag_key: The key-name for the LF-tag.
            :param tag_values: A list of possible values for the corresponding ``TagKey`` of an LF-tag key-value pair.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-lftagkeyresource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_lakeformation as lakeformation
                
                l_fTag_key_resource_property = lakeformation.CfnPrincipalPermissions.LFTagKeyResourceProperty(
                    catalog_id="catalogId",
                    tag_key="tagKey",
                    tag_values=["tagValues"]
                )
            '''
            if __debug__:
                def stub(
                    *,
                    catalog_id: builtins.str,
                    tag_key: builtins.str,
                    tag_values: typing.Sequence[builtins.str],
                ) -> None:
                    ...
                type_hints = typing.get_type_hints(stub)
                check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
                check_type(argname="argument tag_key", value=tag_key, expected_type=type_hints["tag_key"])
                check_type(argname="argument tag_values", value=tag_values, expected_type=type_hints["tag_values"])
            self._values: typing.Dict[str, typing.Any] = {
                "catalog_id": catalog_id,
                "tag_key": tag_key,
                "tag_values": tag_values,
            }

        @builtins.property
        def catalog_id(self) -> builtins.str:
            '''The identifier for the Data Catalog where the location is registered with Data Catalog .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-lftagkeyresource.html#cfn-lakeformation-principalpermissions-lftagkeyresource-catalogid
            '''
            result = self._values.get("catalog_id")
            assert result is not None, "Required property 'catalog_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def tag_key(self) -> builtins.str:
            '''The key-name for the LF-tag.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-lftagkeyresource.html#cfn-lakeformation-principalpermissions-lftagkeyresource-tagkey
            '''
            result = self._values.get("tag_key")
            assert result is not None, "Required property 'tag_key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def tag_values(self) -> typing.List[builtins.str]:
            '''A list of possible values for the corresponding ``TagKey`` of an LF-tag key-value pair.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-lftagkeyresource.html#cfn-lakeformation-principalpermissions-lftagkeyresource-tagvalues
            '''
            result = self._values.get("tag_values")
            assert result is not None, "Required property 'tag_values' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LFTagKeyResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-lakeformation.CfnPrincipalPermissions.LFTagPolicyResourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "catalog_id": "catalogId",
            "expression": "expression",
            "resource_type": "resourceType",
        },
    )
    class LFTagPolicyResourceProperty:
        def __init__(
            self,
            *,
            catalog_id: builtins.str,
            expression: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, typing.Union["CfnPrincipalPermissions.LFTagProperty", typing.Dict[str, typing.Any]]]]],
            resource_type: builtins.str,
        ) -> None:
            '''A list of LF-tag conditions that define a resource's LF-tag policy.

            A structure that allows an admin to grant user permissions on certain conditions. For example, granting a role access to all columns that do not have the LF-tag 'PII' in tables that have the LF-tag 'Prod'.

            :param catalog_id: The identifier for the Data Catalog . The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your AWS Lake Formation environment.
            :param expression: A list of LF-tag conditions that apply to the resource's LF-tag policy.
            :param resource_type: The resource type for which the LF-tag policy applies.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-lftagpolicyresource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_lakeformation as lakeformation
                
                l_fTag_policy_resource_property = lakeformation.CfnPrincipalPermissions.LFTagPolicyResourceProperty(
                    catalog_id="catalogId",
                    expression=[lakeformation.CfnPrincipalPermissions.LFTagProperty(
                        tag_key="tagKey",
                        tag_values=["tagValues"]
                    )],
                    resource_type="resourceType"
                )
            '''
            if __debug__:
                def stub(
                    *,
                    catalog_id: builtins.str,
                    expression: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnPrincipalPermissions.LFTagProperty, typing.Dict[str, typing.Any]]]]],
                    resource_type: builtins.str,
                ) -> None:
                    ...
                type_hints = typing.get_type_hints(stub)
                check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
                check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
                check_type(argname="argument resource_type", value=resource_type, expected_type=type_hints["resource_type"])
            self._values: typing.Dict[str, typing.Any] = {
                "catalog_id": catalog_id,
                "expression": expression,
                "resource_type": resource_type,
            }

        @builtins.property
        def catalog_id(self) -> builtins.str:
            '''The identifier for the Data Catalog .

            The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your AWS Lake Formation environment.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-lftagpolicyresource.html#cfn-lakeformation-principalpermissions-lftagpolicyresource-catalogid
            '''
            result = self._values.get("catalog_id")
            assert result is not None, "Required property 'catalog_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def expression(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnPrincipalPermissions.LFTagProperty"]]]:
            '''A list of LF-tag conditions that apply to the resource's LF-tag policy.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-lftagpolicyresource.html#cfn-lakeformation-principalpermissions-lftagpolicyresource-expression
            '''
            result = self._values.get("expression")
            assert result is not None, "Required property 'expression' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnPrincipalPermissions.LFTagProperty"]]], result)

        @builtins.property
        def resource_type(self) -> builtins.str:
            '''The resource type for which the LF-tag policy applies.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-lftagpolicyresource.html#cfn-lakeformation-principalpermissions-lftagpolicyresource-resourcetype
            '''
            result = self._values.get("resource_type")
            assert result is not None, "Required property 'resource_type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LFTagPolicyResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-lakeformation.CfnPrincipalPermissions.LFTagProperty",
        jsii_struct_bases=[],
        name_mapping={"tag_key": "tagKey", "tag_values": "tagValues"},
    )
    class LFTagProperty:
        def __init__(
            self,
            *,
            tag_key: typing.Optional[builtins.str] = None,
            tag_values: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''The LF-tag key and values attached to a resource.

            :param tag_key: The key-name for the LF-tag.
            :param tag_values: A list of possible values of the corresponding ``TagKey`` of an LF-tag key-value pair.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-lftag.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_lakeformation as lakeformation
                
                l_fTag_property = lakeformation.CfnPrincipalPermissions.LFTagProperty(
                    tag_key="tagKey",
                    tag_values=["tagValues"]
                )
            '''
            if __debug__:
                def stub(
                    *,
                    tag_key: typing.Optional[builtins.str] = None,
                    tag_values: typing.Optional[typing.Sequence[builtins.str]] = None,
                ) -> None:
                    ...
                type_hints = typing.get_type_hints(stub)
                check_type(argname="argument tag_key", value=tag_key, expected_type=type_hints["tag_key"])
                check_type(argname="argument tag_values", value=tag_values, expected_type=type_hints["tag_values"])
            self._values: typing.Dict[str, typing.Any] = {}
            if tag_key is not None:
                self._values["tag_key"] = tag_key
            if tag_values is not None:
                self._values["tag_values"] = tag_values

        @builtins.property
        def tag_key(self) -> typing.Optional[builtins.str]:
            '''The key-name for the LF-tag.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-lftag.html#cfn-lakeformation-principalpermissions-lftag-tagkey
            '''
            result = self._values.get("tag_key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def tag_values(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of possible values of the corresponding ``TagKey`` of an LF-tag key-value pair.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-lftag.html#cfn-lakeformation-principalpermissions-lftag-tagvalues
            '''
            result = self._values.get("tag_values")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LFTagProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-lakeformation.CfnPrincipalPermissions.ResourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "catalog": "catalog",
            "database": "database",
            "data_cells_filter": "dataCellsFilter",
            "data_location": "dataLocation",
            "lf_tag": "lfTag",
            "lf_tag_policy": "lfTagPolicy",
            "table": "table",
            "table_with_columns": "tableWithColumns",
        },
    )
    class ResourceProperty:
        def __init__(
            self,
            *,
            catalog: typing.Any = None,
            database: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union["CfnPrincipalPermissions.DatabaseResourceProperty", typing.Dict[str, typing.Any]]]] = None,
            data_cells_filter: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union["CfnPrincipalPermissions.DataCellsFilterResourceProperty", typing.Dict[str, typing.Any]]]] = None,
            data_location: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union["CfnPrincipalPermissions.DataLocationResourceProperty", typing.Dict[str, typing.Any]]]] = None,
            lf_tag: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union["CfnPrincipalPermissions.LFTagKeyResourceProperty", typing.Dict[str, typing.Any]]]] = None,
            lf_tag_policy: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union["CfnPrincipalPermissions.LFTagPolicyResourceProperty", typing.Dict[str, typing.Any]]]] = None,
            table: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union["CfnPrincipalPermissions.TableResourceProperty", typing.Dict[str, typing.Any]]]] = None,
            table_with_columns: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union["CfnPrincipalPermissions.TableWithColumnsResourceProperty", typing.Dict[str, typing.Any]]]] = None,
        ) -> None:
            '''A structure for the resource.

            :param catalog: The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your AWS Lake Formation environment.
            :param database: The database for the resource. Unique to the Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database permissions to a principal.
            :param data_cells_filter: A data cell filter.
            :param data_location: The location of an Amazon S3 path where permissions are granted or revoked.
            :param lf_tag: The LF-tag key and values attached to a resource.
            :param lf_tag_policy: A list of LF-tag conditions that define a resource's LF-tag policy.
            :param table: The table for the resource. A table is a metadata definition that represents your data. You can Grant and Revoke table privileges to a principal.
            :param table_with_columns: The table with columns for the resource. A principal with permissions to this resource can select metadata from the columns of a table in the Data Catalog and the underlying data in Amazon S3.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-resource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_lakeformation as lakeformation
                
                # catalog: Any
                # table_wildcard: Any
                
                resource_property = lakeformation.CfnPrincipalPermissions.ResourceProperty(
                    catalog=catalog,
                    database=lakeformation.CfnPrincipalPermissions.DatabaseResourceProperty(
                        catalog_id="catalogId",
                        name="name"
                    ),
                    data_cells_filter=lakeformation.CfnPrincipalPermissions.DataCellsFilterResourceProperty(
                        database_name="databaseName",
                        name="name",
                        table_catalog_id="tableCatalogId",
                        table_name="tableName"
                    ),
                    data_location=lakeformation.CfnPrincipalPermissions.DataLocationResourceProperty(
                        catalog_id="catalogId",
                        resource_arn="resourceArn"
                    ),
                    lf_tag=lakeformation.CfnPrincipalPermissions.LFTagKeyResourceProperty(
                        catalog_id="catalogId",
                        tag_key="tagKey",
                        tag_values=["tagValues"]
                    ),
                    lf_tag_policy=lakeformation.CfnPrincipalPermissions.LFTagPolicyResourceProperty(
                        catalog_id="catalogId",
                        expression=[lakeformation.CfnPrincipalPermissions.LFTagProperty(
                            tag_key="tagKey",
                            tag_values=["tagValues"]
                        )],
                        resource_type="resourceType"
                    ),
                    table=lakeformation.CfnPrincipalPermissions.TableResourceProperty(
                        catalog_id="catalogId",
                        database_name="databaseName",
                
                        # the properties below are optional
                        name="name",
                        table_wildcard=table_wildcard
                    ),
                    table_with_columns=lakeformation.CfnPrincipalPermissions.TableWithColumnsResourceProperty(
                        catalog_id="catalogId",
                        database_name="databaseName",
                        name="name",
                
                        # the properties below are optional
                        column_names=["columnNames"],
                        column_wildcard=lakeformation.CfnPrincipalPermissions.ColumnWildcardProperty(
                            excluded_column_names=["excludedColumnNames"]
                        )
                    )
                )
            '''
            if __debug__:
                def stub(
                    *,
                    catalog: typing.Any = None,
                    database: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnPrincipalPermissions.DatabaseResourceProperty, typing.Dict[str, typing.Any]]]] = None,
                    data_cells_filter: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnPrincipalPermissions.DataCellsFilterResourceProperty, typing.Dict[str, typing.Any]]]] = None,
                    data_location: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnPrincipalPermissions.DataLocationResourceProperty, typing.Dict[str, typing.Any]]]] = None,
                    lf_tag: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnPrincipalPermissions.LFTagKeyResourceProperty, typing.Dict[str, typing.Any]]]] = None,
                    lf_tag_policy: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnPrincipalPermissions.LFTagPolicyResourceProperty, typing.Dict[str, typing.Any]]]] = None,
                    table: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnPrincipalPermissions.TableResourceProperty, typing.Dict[str, typing.Any]]]] = None,
                    table_with_columns: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnPrincipalPermissions.TableWithColumnsResourceProperty, typing.Dict[str, typing.Any]]]] = None,
                ) -> None:
                    ...
                type_hints = typing.get_type_hints(stub)
                check_type(argname="argument catalog", value=catalog, expected_type=type_hints["catalog"])
                check_type(argname="argument database", value=database, expected_type=type_hints["database"])
                check_type(argname="argument data_cells_filter", value=data_cells_filter, expected_type=type_hints["data_cells_filter"])
                check_type(argname="argument data_location", value=data_location, expected_type=type_hints["data_location"])
                check_type(argname="argument lf_tag", value=lf_tag, expected_type=type_hints["lf_tag"])
                check_type(argname="argument lf_tag_policy", value=lf_tag_policy, expected_type=type_hints["lf_tag_policy"])
                check_type(argname="argument table", value=table, expected_type=type_hints["table"])
                check_type(argname="argument table_with_columns", value=table_with_columns, expected_type=type_hints["table_with_columns"])
            self._values: typing.Dict[str, typing.Any] = {}
            if catalog is not None:
                self._values["catalog"] = catalog
            if database is not None:
                self._values["database"] = database
            if data_cells_filter is not None:
                self._values["data_cells_filter"] = data_cells_filter
            if data_location is not None:
                self._values["data_location"] = data_location
            if lf_tag is not None:
                self._values["lf_tag"] = lf_tag
            if lf_tag_policy is not None:
                self._values["lf_tag_policy"] = lf_tag_policy
            if table is not None:
                self._values["table"] = table
            if table_with_columns is not None:
                self._values["table_with_columns"] = table_with_columns

        @builtins.property
        def catalog(self) -> typing.Any:
            '''The identifier for the Data Catalog.

            By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your AWS Lake Formation environment.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-resource.html#cfn-lakeformation-principalpermissions-resource-catalog
            '''
            result = self._values.get("catalog")
            return typing.cast(typing.Any, result)

        @builtins.property
        def database(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPrincipalPermissions.DatabaseResourceProperty"]]:
            '''The database for the resource.

            Unique to the Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database permissions to a principal.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-resource.html#cfn-lakeformation-principalpermissions-resource-database
            '''
            result = self._values.get("database")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPrincipalPermissions.DatabaseResourceProperty"]], result)

        @builtins.property
        def data_cells_filter(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPrincipalPermissions.DataCellsFilterResourceProperty"]]:
            '''A data cell filter.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-resource.html#cfn-lakeformation-principalpermissions-resource-datacellsfilter
            '''
            result = self._values.get("data_cells_filter")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPrincipalPermissions.DataCellsFilterResourceProperty"]], result)

        @builtins.property
        def data_location(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPrincipalPermissions.DataLocationResourceProperty"]]:
            '''The location of an Amazon S3 path where permissions are granted or revoked.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-resource.html#cfn-lakeformation-principalpermissions-resource-datalocation
            '''
            result = self._values.get("data_location")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPrincipalPermissions.DataLocationResourceProperty"]], result)

        @builtins.property
        def lf_tag(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPrincipalPermissions.LFTagKeyResourceProperty"]]:
            '''The LF-tag key and values attached to a resource.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-resource.html#cfn-lakeformation-principalpermissions-resource-lftag
            '''
            result = self._values.get("lf_tag")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPrincipalPermissions.LFTagKeyResourceProperty"]], result)

        @builtins.property
        def lf_tag_policy(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPrincipalPermissions.LFTagPolicyResourceProperty"]]:
            '''A list of LF-tag conditions that define a resource's LF-tag policy.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-resource.html#cfn-lakeformation-principalpermissions-resource-lftagpolicy
            '''
            result = self._values.get("lf_tag_policy")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPrincipalPermissions.LFTagPolicyResourceProperty"]], result)

        @builtins.property
        def table(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPrincipalPermissions.TableResourceProperty"]]:
            '''The table for the resource.

            A table is a metadata definition that represents your data. You can Grant and Revoke table privileges to a principal.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-resource.html#cfn-lakeformation-principalpermissions-resource-table
            '''
            result = self._values.get("table")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPrincipalPermissions.TableResourceProperty"]], result)

        @builtins.property
        def table_with_columns(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPrincipalPermissions.TableWithColumnsResourceProperty"]]:
            '''The table with columns for the resource.

            A principal with permissions to this resource can select metadata from the columns of a table in the Data Catalog and the underlying data in Amazon S3.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-resource.html#cfn-lakeformation-principalpermissions-resource-tablewithcolumns
            '''
            result = self._values.get("table_with_columns")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPrincipalPermissions.TableWithColumnsResourceProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-lakeformation.CfnPrincipalPermissions.TableResourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "catalog_id": "catalogId",
            "database_name": "databaseName",
            "name": "name",
            "table_wildcard": "tableWildcard",
        },
    )
    class TableResourceProperty:
        def __init__(
            self,
            *,
            catalog_id: builtins.str,
            database_name: builtins.str,
            name: typing.Optional[builtins.str] = None,
            table_wildcard: typing.Any = None,
        ) -> None:
            '''A structure for the table object.

            A table is a metadata definition that represents your data. You can Grant and Revoke table privileges to a principal.

            :param catalog_id: ``CfnPrincipalPermissions.TableResourceProperty.CatalogId``.
            :param database_name: The name of the database for the table. Unique to a Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database privileges to a principal.
            :param name: The name of the table.
            :param table_wildcard: A wildcard object representing every table under a database. At least one of ``TableResource$Name`` or ``TableResource$TableWildcard`` is required.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-tableresource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_lakeformation as lakeformation
                
                # table_wildcard: Any
                
                table_resource_property = lakeformation.CfnPrincipalPermissions.TableResourceProperty(
                    catalog_id="catalogId",
                    database_name="databaseName",
                
                    # the properties below are optional
                    name="name",
                    table_wildcard=table_wildcard
                )
            '''
            if __debug__:
                def stub(
                    *,
                    catalog_id: builtins.str,
                    database_name: builtins.str,
                    name: typing.Optional[builtins.str] = None,
                    table_wildcard: typing.Any = None,
                ) -> None:
                    ...
                type_hints = typing.get_type_hints(stub)
                check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
                check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument table_wildcard", value=table_wildcard, expected_type=type_hints["table_wildcard"])
            self._values: typing.Dict[str, typing.Any] = {
                "catalog_id": catalog_id,
                "database_name": database_name,
            }
            if name is not None:
                self._values["name"] = name
            if table_wildcard is not None:
                self._values["table_wildcard"] = table_wildcard

        @builtins.property
        def catalog_id(self) -> builtins.str:
            '''``CfnPrincipalPermissions.TableResourceProperty.CatalogId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-tableresource.html#cfn-lakeformation-principalpermissions-tableresource-catalogid
            '''
            result = self._values.get("catalog_id")
            assert result is not None, "Required property 'catalog_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def database_name(self) -> builtins.str:
            '''The name of the database for the table.

            Unique to a Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database privileges to a principal.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-tableresource.html#cfn-lakeformation-principalpermissions-tableresource-databasename
            '''
            result = self._values.get("database_name")
            assert result is not None, "Required property 'database_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the table.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-tableresource.html#cfn-lakeformation-principalpermissions-tableresource-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def table_wildcard(self) -> typing.Any:
            '''A wildcard object representing every table under a database.

            At least one of ``TableResource$Name`` or ``TableResource$TableWildcard`` is required.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-tableresource.html#cfn-lakeformation-principalpermissions-tableresource-tablewildcard
            '''
            result = self._values.get("table_wildcard")
            return typing.cast(typing.Any, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TableResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-lakeformation.CfnPrincipalPermissions.TableWithColumnsResourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "catalog_id": "catalogId",
            "database_name": "databaseName",
            "name": "name",
            "column_names": "columnNames",
            "column_wildcard": "columnWildcard",
        },
    )
    class TableWithColumnsResourceProperty:
        def __init__(
            self,
            *,
            catalog_id: builtins.str,
            database_name: builtins.str,
            name: builtins.str,
            column_names: typing.Optional[typing.Sequence[builtins.str]] = None,
            column_wildcard: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union["CfnPrincipalPermissions.ColumnWildcardProperty", typing.Dict[str, typing.Any]]]] = None,
        ) -> None:
            '''A structure for a table with columns object. This object is only used when granting a SELECT permission.

            This object must take a value for at least one of ``ColumnsNames`` , ``ColumnsIndexes`` , or ``ColumnsWildcard`` .

            :param catalog_id: The identifier for the Data Catalog where the location is registered with AWS Lake Formation .
            :param database_name: The name of the database for the table with columns resource. Unique to the Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database privileges to a principal.
            :param name: The name of the table resource. A table is a metadata definition that represents your data. You can Grant and Revoke table privileges to a principal.
            :param column_names: The list of column names for the table. At least one of ``ColumnNames`` or ``ColumnWildcard`` is required.
            :param column_wildcard: A wildcard specified by a ``ColumnWildcard`` object. At least one of ``ColumnNames`` or ``ColumnWildcard`` is required.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-tablewithcolumnsresource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_lakeformation as lakeformation
                
                table_with_columns_resource_property = lakeformation.CfnPrincipalPermissions.TableWithColumnsResourceProperty(
                    catalog_id="catalogId",
                    database_name="databaseName",
                    name="name",
                
                    # the properties below are optional
                    column_names=["columnNames"],
                    column_wildcard=lakeformation.CfnPrincipalPermissions.ColumnWildcardProperty(
                        excluded_column_names=["excludedColumnNames"]
                    )
                )
            '''
            if __debug__:
                def stub(
                    *,
                    catalog_id: builtins.str,
                    database_name: builtins.str,
                    name: builtins.str,
                    column_names: typing.Optional[typing.Sequence[builtins.str]] = None,
                    column_wildcard: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnPrincipalPermissions.ColumnWildcardProperty, typing.Dict[str, typing.Any]]]] = None,
                ) -> None:
                    ...
                type_hints = typing.get_type_hints(stub)
                check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
                check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument column_names", value=column_names, expected_type=type_hints["column_names"])
                check_type(argname="argument column_wildcard", value=column_wildcard, expected_type=type_hints["column_wildcard"])
            self._values: typing.Dict[str, typing.Any] = {
                "catalog_id": catalog_id,
                "database_name": database_name,
                "name": name,
            }
            if column_names is not None:
                self._values["column_names"] = column_names
            if column_wildcard is not None:
                self._values["column_wildcard"] = column_wildcard

        @builtins.property
        def catalog_id(self) -> builtins.str:
            '''The identifier for the Data Catalog where the location is registered with AWS Lake Formation .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-tablewithcolumnsresource.html#cfn-lakeformation-principalpermissions-tablewithcolumnsresource-catalogid
            '''
            result = self._values.get("catalog_id")
            assert result is not None, "Required property 'catalog_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def database_name(self) -> builtins.str:
            '''The name of the database for the table with columns resource.

            Unique to the Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database privileges to a principal.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-tablewithcolumnsresource.html#cfn-lakeformation-principalpermissions-tablewithcolumnsresource-databasename
            '''
            result = self._values.get("database_name")
            assert result is not None, "Required property 'database_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the table resource.

            A table is a metadata definition that represents your data. You can Grant and Revoke table privileges to a principal.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-tablewithcolumnsresource.html#cfn-lakeformation-principalpermissions-tablewithcolumnsresource-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def column_names(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The list of column names for the table.

            At least one of ``ColumnNames`` or ``ColumnWildcard`` is required.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-tablewithcolumnsresource.html#cfn-lakeformation-principalpermissions-tablewithcolumnsresource-columnnames
            '''
            result = self._values.get("column_names")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def column_wildcard(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPrincipalPermissions.ColumnWildcardProperty"]]:
            '''A wildcard specified by a ``ColumnWildcard`` object.

            At least one of ``ColumnNames`` or ``ColumnWildcard`` is required.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-tablewithcolumnsresource.html#cfn-lakeformation-principalpermissions-tablewithcolumnsresource-columnwildcard
            '''
            result = self._values.get("column_wildcard")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPrincipalPermissions.ColumnWildcardProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TableWithColumnsResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-lakeformation.CfnPrincipalPermissionsProps",
    jsii_struct_bases=[],
    name_mapping={
        "permissions": "permissions",
        "permissions_with_grant_option": "permissionsWithGrantOption",
        "principal": "principal",
        "resource": "resource",
        "catalog": "catalog",
    },
)
class CfnPrincipalPermissionsProps:
    def __init__(
        self,
        *,
        permissions: typing.Sequence[builtins.str],
        permissions_with_grant_option: typing.Sequence[builtins.str],
        principal: typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnPrincipalPermissions.DataLakePrincipalProperty, typing.Dict[str, typing.Any]]],
        resource: typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnPrincipalPermissions.ResourceProperty, typing.Dict[str, typing.Any]]],
        catalog: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnPrincipalPermissions``.

        :param permissions: The permissions granted or revoked.
        :param permissions_with_grant_option: Indicates the ability to grant permissions (as a subset of permissions granted).
        :param principal: The principal to be granted a permission.
        :param resource: The resource to be granted or revoked permissions.
        :param catalog: The identifier for the Data Catalog . By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-principalpermissions.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_lakeformation as lakeformation
            
            # catalog: Any
            # table_wildcard: Any
            
            cfn_principal_permissions_props = lakeformation.CfnPrincipalPermissionsProps(
                permissions=["permissions"],
                permissions_with_grant_option=["permissionsWithGrantOption"],
                principal=lakeformation.CfnPrincipalPermissions.DataLakePrincipalProperty(
                    data_lake_principal_identifier="dataLakePrincipalIdentifier"
                ),
                resource=lakeformation.CfnPrincipalPermissions.ResourceProperty(
                    catalog=catalog,
                    database=lakeformation.CfnPrincipalPermissions.DatabaseResourceProperty(
                        catalog_id="catalogId",
                        name="name"
                    ),
                    data_cells_filter=lakeformation.CfnPrincipalPermissions.DataCellsFilterResourceProperty(
                        database_name="databaseName",
                        name="name",
                        table_catalog_id="tableCatalogId",
                        table_name="tableName"
                    ),
                    data_location=lakeformation.CfnPrincipalPermissions.DataLocationResourceProperty(
                        catalog_id="catalogId",
                        resource_arn="resourceArn"
                    ),
                    lf_tag=lakeformation.CfnPrincipalPermissions.LFTagKeyResourceProperty(
                        catalog_id="catalogId",
                        tag_key="tagKey",
                        tag_values=["tagValues"]
                    ),
                    lf_tag_policy=lakeformation.CfnPrincipalPermissions.LFTagPolicyResourceProperty(
                        catalog_id="catalogId",
                        expression=[lakeformation.CfnPrincipalPermissions.LFTagProperty(
                            tag_key="tagKey",
                            tag_values=["tagValues"]
                        )],
                        resource_type="resourceType"
                    ),
                    table=lakeformation.CfnPrincipalPermissions.TableResourceProperty(
                        catalog_id="catalogId",
                        database_name="databaseName",
            
                        # the properties below are optional
                        name="name",
                        table_wildcard=table_wildcard
                    ),
                    table_with_columns=lakeformation.CfnPrincipalPermissions.TableWithColumnsResourceProperty(
                        catalog_id="catalogId",
                        database_name="databaseName",
                        name="name",
            
                        # the properties below are optional
                        column_names=["columnNames"],
                        column_wildcard=lakeformation.CfnPrincipalPermissions.ColumnWildcardProperty(
                            excluded_column_names=["excludedColumnNames"]
                        )
                    )
                ),
            
                # the properties below are optional
                catalog="catalog"
            )
        '''
        if __debug__:
            def stub(
                *,
                permissions: typing.Sequence[builtins.str],
                permissions_with_grant_option: typing.Sequence[builtins.str],
                principal: typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnPrincipalPermissions.DataLakePrincipalProperty, typing.Dict[str, typing.Any]]],
                resource: typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnPrincipalPermissions.ResourceProperty, typing.Dict[str, typing.Any]]],
                catalog: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument permissions", value=permissions, expected_type=type_hints["permissions"])
            check_type(argname="argument permissions_with_grant_option", value=permissions_with_grant_option, expected_type=type_hints["permissions_with_grant_option"])
            check_type(argname="argument principal", value=principal, expected_type=type_hints["principal"])
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
            check_type(argname="argument catalog", value=catalog, expected_type=type_hints["catalog"])
        self._values: typing.Dict[str, typing.Any] = {
            "permissions": permissions,
            "permissions_with_grant_option": permissions_with_grant_option,
            "principal": principal,
            "resource": resource,
        }
        if catalog is not None:
            self._values["catalog"] = catalog

    @builtins.property
    def permissions(self) -> typing.List[builtins.str]:
        '''The permissions granted or revoked.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-principalpermissions.html#cfn-lakeformation-principalpermissions-permissions
        '''
        result = self._values.get("permissions")
        assert result is not None, "Required property 'permissions' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def permissions_with_grant_option(self) -> typing.List[builtins.str]:
        '''Indicates the ability to grant permissions (as a subset of permissions granted).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-principalpermissions.html#cfn-lakeformation-principalpermissions-permissionswithgrantoption
        '''
        result = self._values.get("permissions_with_grant_option")
        assert result is not None, "Required property 'permissions_with_grant_option' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def principal(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnPrincipalPermissions.DataLakePrincipalProperty]:
        '''The principal to be granted a permission.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-principalpermissions.html#cfn-lakeformation-principalpermissions-principal
        '''
        result = self._values.get("principal")
        assert result is not None, "Required property 'principal' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnPrincipalPermissions.DataLakePrincipalProperty], result)

    @builtins.property
    def resource(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnPrincipalPermissions.ResourceProperty]:
        '''The resource to be granted or revoked permissions.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-principalpermissions.html#cfn-lakeformation-principalpermissions-resource
        '''
        result = self._values.get("resource")
        assert result is not None, "Required property 'resource' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnPrincipalPermissions.ResourceProperty], result)

    @builtins.property
    def catalog(self) -> typing.Optional[builtins.str]:
        '''The identifier for the Data Catalog .

        By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-principalpermissions.html#cfn-lakeformation-principalpermissions-catalog
        '''
        result = self._values.get("catalog")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPrincipalPermissionsProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnResource(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-lakeformation.CfnResource",
):
    '''A CloudFormation ``AWS::LakeFormation::Resource``.

    The ``AWS::LakeFormation::Resource`` represents the data (  buckets and folders) that is being registered with AWS Lake Formation . During a stack operation, AWS CloudFormation calls the AWS Lake Formation ```RegisterResource`` <https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api-credential-vending.html#aws-lake-formation-api-credential-vending-RegisterResource>`_ API operation to register the resource. To remove a ``Resource`` type, AWS CloudFormation calls the AWS Lake Formation ```DeregisterResource`` <https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api-credential-vending.html#aws-lake-formation-api-credential-vending-DeregisterResource>`_ API operation.

    :cloudformationResource: AWS::LakeFormation::Resource
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-resource.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_lakeformation as lakeformation
        
        cfn_resource = lakeformation.CfnResource(self, "MyCfnResource",
            resource_arn="resourceArn",
            use_service_linked_role=False,
        
            # the properties below are optional
            role_arn="roleArn"
        )
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        resource_arn: builtins.str,
        use_service_linked_role: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
        role_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::LakeFormation::Resource``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param resource_arn: The Amazon Resource Name (ARN) of the resource.
        :param use_service_linked_role: Designates a trusted caller, an IAM principal, by registering this caller with the Data Catalog .
        :param role_arn: The IAM role that registered a resource.
        '''
        if __debug__:
            def stub(
                scope: aws_cdk.core.Construct,
                id: builtins.str,
                *,
                resource_arn: builtins.str,
                use_service_linked_role: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
                role_arn: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnResourceProps(
            resource_arn=resource_arn,
            use_service_linked_role=use_service_linked_role,
            role_arn=role_arn,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            def stub(inspector: aws_cdk.core.TreeInspector) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            def stub(props: typing.Mapping[builtins.str, typing.Any]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="resourceArn")
    def resource_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the resource.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-resource.html#cfn-lakeformation-resource-resourcearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "resourceArn"))

    @resource_arn.setter
    def resource_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceArn", value)

    @builtins.property
    @jsii.member(jsii_name="useServiceLinkedRole")
    def use_service_linked_role(
        self,
    ) -> typing.Union[builtins.bool, aws_cdk.core.IResolvable]:
        '''Designates a trusted caller, an IAM principal, by registering this caller with the Data Catalog .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-resource.html#cfn-lakeformation-resource-useservicelinkedrole
        '''
        return typing.cast(typing.Union[builtins.bool, aws_cdk.core.IResolvable], jsii.get(self, "useServiceLinkedRole"))

    @use_service_linked_role.setter
    def use_service_linked_role(
        self,
        value: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useServiceLinkedRole", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''The IAM role that registered a resource.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-resource.html#cfn-lakeformation-resource-rolearn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.Optional[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-lakeformation.CfnResourceProps",
    jsii_struct_bases=[],
    name_mapping={
        "resource_arn": "resourceArn",
        "use_service_linked_role": "useServiceLinkedRole",
        "role_arn": "roleArn",
    },
)
class CfnResourceProps:
    def __init__(
        self,
        *,
        resource_arn: builtins.str,
        use_service_linked_role: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
        role_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnResource``.

        :param resource_arn: The Amazon Resource Name (ARN) of the resource.
        :param use_service_linked_role: Designates a trusted caller, an IAM principal, by registering this caller with the Data Catalog .
        :param role_arn: The IAM role that registered a resource.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-resource.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_lakeformation as lakeformation
            
            cfn_resource_props = lakeformation.CfnResourceProps(
                resource_arn="resourceArn",
                use_service_linked_role=False,
            
                # the properties below are optional
                role_arn="roleArn"
            )
        '''
        if __debug__:
            def stub(
                *,
                resource_arn: builtins.str,
                use_service_linked_role: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
                role_arn: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
            check_type(argname="argument use_service_linked_role", value=use_service_linked_role, expected_type=type_hints["use_service_linked_role"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
        self._values: typing.Dict[str, typing.Any] = {
            "resource_arn": resource_arn,
            "use_service_linked_role": use_service_linked_role,
        }
        if role_arn is not None:
            self._values["role_arn"] = role_arn

    @builtins.property
    def resource_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the resource.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-resource.html#cfn-lakeformation-resource-resourcearn
        '''
        result = self._values.get("resource_arn")
        assert result is not None, "Required property 'resource_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def use_service_linked_role(
        self,
    ) -> typing.Union[builtins.bool, aws_cdk.core.IResolvable]:
        '''Designates a trusted caller, an IAM principal, by registering this caller with the Data Catalog .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-resource.html#cfn-lakeformation-resource-useservicelinkedrole
        '''
        result = self._values.get("use_service_linked_role")
        assert result is not None, "Required property 'use_service_linked_role' is missing"
        return typing.cast(typing.Union[builtins.bool, aws_cdk.core.IResolvable], result)

    @builtins.property
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''The IAM role that registered a resource.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-resource.html#cfn-lakeformation-resource-rolearn
        '''
        result = self._values.get("role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnTag(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-lakeformation.CfnTag",
):
    '''A CloudFormation ``AWS::LakeFormation::Tag``.

    The ``AWS::LakeFormation::Tag`` resource represents an LF-tag, which consists of a key and one or more possible values for the key. During a stack operation, AWS CloudFormation calls the AWS Lake Formation ``CreateLFTag`` API to create a tag, and ``UpdateLFTag`` API to update a tag resource, and a ``DeleteLFTag`` to delete it.

    :cloudformationResource: AWS::LakeFormation::Tag
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-tag.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_lakeformation as lakeformation
        
        cfn_tag = lakeformation.CfnTag(self, "MyCfnTag",
            tag_key="tagKey",
            tag_values=["tagValues"],
        
            # the properties below are optional
            catalog_id="catalogId"
        )
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        tag_key: builtins.str,
        tag_values: typing.Sequence[builtins.str],
        catalog_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::LakeFormation::Tag``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param tag_key: UTF-8 string, not less than 1 or more than 255 bytes long, matching the `single-line string pattern <https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api-aws-lake-formation-api-common.html#aws-glue-api-regex-oneLine>`_ . The key-name for the LF-tag.
        :param tag_values: An array of UTF-8 strings, not less than 1 or more than 50 strings. A list of possible values of the corresponding ``TagKey`` of an LF-tag key-value pair.
        :param catalog_id: Catalog id string, not less than 1 or more than 255 bytes long, matching the `single-line string pattern <https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api-aws-lake-formation-api-common.html#aws-glue-api-regex-oneLine>`_ . The identifier for the Data Catalog . By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your AWS Lake Formation environment.
        '''
        if __debug__:
            def stub(
                scope: aws_cdk.core.Construct,
                id: builtins.str,
                *,
                tag_key: builtins.str,
                tag_values: typing.Sequence[builtins.str],
                catalog_id: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnTagProps(
            tag_key=tag_key, tag_values=tag_values, catalog_id=catalog_id
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            def stub(inspector: aws_cdk.core.TreeInspector) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            def stub(props: typing.Mapping[builtins.str, typing.Any]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tagKey")
    def tag_key(self) -> builtins.str:
        '''UTF-8 string, not less than 1 or more than 255 bytes long, matching the `single-line string pattern <https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api-aws-lake-formation-api-common.html#aws-glue-api-regex-oneLine>`_ .

        The key-name for the LF-tag.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-tag.html#cfn-lakeformation-tag-tagkey
        '''
        return typing.cast(builtins.str, jsii.get(self, "tagKey"))

    @tag_key.setter
    def tag_key(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagKey", value)

    @builtins.property
    @jsii.member(jsii_name="tagValues")
    def tag_values(self) -> typing.List[builtins.str]:
        '''An array of UTF-8 strings, not less than 1 or more than 50 strings.

        A list of possible values of the corresponding ``TagKey`` of an LF-tag key-value pair.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-tag.html#cfn-lakeformation-tag-tagvalues
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tagValues"))

    @tag_values.setter
    def tag_values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagValues", value)

    @builtins.property
    @jsii.member(jsii_name="catalogId")
    def catalog_id(self) -> typing.Optional[builtins.str]:
        '''Catalog id string, not less than 1 or more than 255 bytes long, matching the `single-line string pattern <https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api-aws-lake-formation-api-common.html#aws-glue-api-regex-oneLine>`_ .

        The identifier for the Data Catalog . By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your AWS Lake Formation environment.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-tag.html#cfn-lakeformation-tag-catalogid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "catalogId"))

    @catalog_id.setter
    def catalog_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.Optional[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "catalogId", value)


@jsii.implements(aws_cdk.core.IInspectable)
class CfnTagAssociation(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-lakeformation.CfnTagAssociation",
):
    '''A CloudFormation ``AWS::LakeFormation::TagAssociation``.

    The ``AWS::LakeFormation::TagAssociation`` resource represents an assignment of an LF-tag to a Data Catalog resource (database, table, or column). During a stack operation, CloudFormation calls AWS Lake Formation ``AddLFTagsToResource`` API to create a ``TagAssociation`` resource and calls the ``RemoveLFTagsToResource`` API to delete it.

    :cloudformationResource: AWS::LakeFormation::TagAssociation
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-tagassociation.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_lakeformation as lakeformation
        
        # catalog: Any
        # table_wildcard: Any
        
        cfn_tag_association = lakeformation.CfnTagAssociation(self, "MyCfnTagAssociation",
            lf_tags=[lakeformation.CfnTagAssociation.LFTagPairProperty(
                catalog_id="catalogId",
                tag_key="tagKey",
                tag_values=["tagValues"]
            )],
            resource=lakeformation.CfnTagAssociation.ResourceProperty(
                catalog=catalog,
                database=lakeformation.CfnTagAssociation.DatabaseResourceProperty(
                    catalog_id="catalogId",
                    name="name"
                ),
                table=lakeformation.CfnTagAssociation.TableResourceProperty(
                    catalog_id="catalogId",
                    database_name="databaseName",
        
                    # the properties below are optional
                    name="name",
                    table_wildcard=table_wildcard
                ),
                table_with_columns=lakeformation.CfnTagAssociation.TableWithColumnsResourceProperty(
                    catalog_id="catalogId",
                    column_names=["columnNames"],
                    database_name="databaseName",
                    name="name"
                )
            )
        )
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        lf_tags: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, typing.Union["CfnTagAssociation.LFTagPairProperty", typing.Dict[str, typing.Any]]]]],
        resource: typing.Union[aws_cdk.core.IResolvable, typing.Union["CfnTagAssociation.ResourceProperty", typing.Dict[str, typing.Any]]],
    ) -> None:
        '''Create a new ``AWS::LakeFormation::TagAssociation``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param lf_tags: A structure containing an LF-tag key-value pair.
        :param resource: UTF-8 string (valid values: ``DATABASE | TABLE`` ). The resource for which the LF-tag policy applies.
        '''
        if __debug__:
            def stub(
                scope: aws_cdk.core.Construct,
                id: builtins.str,
                *,
                lf_tags: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnTagAssociation.LFTagPairProperty, typing.Dict[str, typing.Any]]]]],
                resource: typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnTagAssociation.ResourceProperty, typing.Dict[str, typing.Any]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnTagAssociationProps(lf_tags=lf_tags, resource=resource)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            def stub(inspector: aws_cdk.core.TreeInspector) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            def stub(props: typing.Mapping[builtins.str, typing.Any]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrResourceIdentifier")
    def attr_resource_identifier(self) -> builtins.str:
        '''Json encoding of the input resource.

        **Examples** - Database: ``{"Catalog":null,"Database":{"CatalogId":"123456789012","Name":"ExampleDbName"},"Table":null,"TableWithColumns":null}``

        - Table: ``{"Catalog":null,"Database":null,"Table":{"CatalogId":"123456789012","DatabaseName":"ExampleDbName","Name":"ExampleTableName","TableWildcard":null},"TableWithColumns":null}``
        - Columns: ``{"Catalog":null,"Database":null,"Table":null,"TableWithColumns":{"CatalogId":"123456789012","DatabaseName":"ExampleDbName","Name":"ExampleTableName","ColumnNames":["ExampleColName1","ExampleColName2"]}}``

        :cloudformationAttribute: ResourceIdentifier
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrResourceIdentifier"))

    @builtins.property
    @jsii.member(jsii_name="attrTagsIdentifier")
    def attr_tags_identifier(self) -> builtins.str:
        '''Json encoding of the input LFTags list.

        For example: ``[{"CatalogId":null,"TagKey":"tagKey1","TagValues":null},{"CatalogId":null,"TagKey":"tagKey2","TagValues":null}]``

        :cloudformationAttribute: TagsIdentifier
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTagsIdentifier"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="lfTags")
    def lf_tags(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnTagAssociation.LFTagPairProperty"]]]:
        '''A structure containing an LF-tag key-value pair.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-tagassociation.html#cfn-lakeformation-tagassociation-lftags
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnTagAssociation.LFTagPairProperty"]]], jsii.get(self, "lfTags"))

    @lf_tags.setter
    def lf_tags(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnTagAssociation.LFTagPairProperty"]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnTagAssociation.LFTagPairProperty]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lfTags", value)

    @builtins.property
    @jsii.member(jsii_name="resource")
    def resource(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnTagAssociation.ResourceProperty"]:
        '''UTF-8 string (valid values: ``DATABASE | TABLE`` ).

        The resource for which the LF-tag policy applies.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-tagassociation.html#cfn-lakeformation-tagassociation-resource
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnTagAssociation.ResourceProperty"], jsii.get(self, "resource"))

    @resource.setter
    def resource(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnTagAssociation.ResourceProperty"],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Union[aws_cdk.core.IResolvable, CfnTagAssociation.ResourceProperty],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resource", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-lakeformation.CfnTagAssociation.DatabaseResourceProperty",
        jsii_struct_bases=[],
        name_mapping={"catalog_id": "catalogId", "name": "name"},
    )
    class DatabaseResourceProperty:
        def __init__(self, *, catalog_id: builtins.str, name: builtins.str) -> None:
            '''A structure for the database object.

            :param catalog_id: The identifier for the Data Catalog . By default, it should be the account ID of the caller.
            :param name: The name of the database resource. Unique to the Data Catalog.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-databaseresource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_lakeformation as lakeformation
                
                database_resource_property = lakeformation.CfnTagAssociation.DatabaseResourceProperty(
                    catalog_id="catalogId",
                    name="name"
                )
            '''
            if __debug__:
                def stub(*, catalog_id: builtins.str, name: builtins.str) -> None:
                    ...
                type_hints = typing.get_type_hints(stub)
                check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[str, typing.Any] = {
                "catalog_id": catalog_id,
                "name": name,
            }

        @builtins.property
        def catalog_id(self) -> builtins.str:
            '''The identifier for the Data Catalog .

            By default, it should be the account ID of the caller.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-databaseresource.html#cfn-lakeformation-tagassociation-databaseresource-catalogid
            '''
            result = self._values.get("catalog_id")
            assert result is not None, "Required property 'catalog_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the database resource.

            Unique to the Data Catalog.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-databaseresource.html#cfn-lakeformation-tagassociation-databaseresource-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DatabaseResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-lakeformation.CfnTagAssociation.LFTagPairProperty",
        jsii_struct_bases=[],
        name_mapping={
            "catalog_id": "catalogId",
            "tag_key": "tagKey",
            "tag_values": "tagValues",
        },
    )
    class LFTagPairProperty:
        def __init__(
            self,
            *,
            catalog_id: builtins.str,
            tag_key: builtins.str,
            tag_values: typing.Sequence[builtins.str],
        ) -> None:
            '''A structure containing the catalog ID, tag key, and tag values of an LF-tag key-value pair.

            :param catalog_id: The identifier for the Data Catalog . By default, it is the account ID of the caller.
            :param tag_key: The key-name for the LF-tag.
            :param tag_values: A list of possible values of the corresponding ``TagKey`` of an LF-tag key-value pair.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-lftagpair.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_lakeformation as lakeformation
                
                l_fTag_pair_property = lakeformation.CfnTagAssociation.LFTagPairProperty(
                    catalog_id="catalogId",
                    tag_key="tagKey",
                    tag_values=["tagValues"]
                )
            '''
            if __debug__:
                def stub(
                    *,
                    catalog_id: builtins.str,
                    tag_key: builtins.str,
                    tag_values: typing.Sequence[builtins.str],
                ) -> None:
                    ...
                type_hints = typing.get_type_hints(stub)
                check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
                check_type(argname="argument tag_key", value=tag_key, expected_type=type_hints["tag_key"])
                check_type(argname="argument tag_values", value=tag_values, expected_type=type_hints["tag_values"])
            self._values: typing.Dict[str, typing.Any] = {
                "catalog_id": catalog_id,
                "tag_key": tag_key,
                "tag_values": tag_values,
            }

        @builtins.property
        def catalog_id(self) -> builtins.str:
            '''The identifier for the Data Catalog .

            By default, it is the account ID of the caller.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-lftagpair.html#cfn-lakeformation-tagassociation-lftagpair-catalogid
            '''
            result = self._values.get("catalog_id")
            assert result is not None, "Required property 'catalog_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def tag_key(self) -> builtins.str:
            '''The key-name for the LF-tag.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-lftagpair.html#cfn-lakeformation-tagassociation-lftagpair-tagkey
            '''
            result = self._values.get("tag_key")
            assert result is not None, "Required property 'tag_key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def tag_values(self) -> typing.List[builtins.str]:
            '''A list of possible values of the corresponding ``TagKey`` of an LF-tag key-value pair.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-lftagpair.html#cfn-lakeformation-tagassociation-lftagpair-tagvalues
            '''
            result = self._values.get("tag_values")
            assert result is not None, "Required property 'tag_values' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LFTagPairProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-lakeformation.CfnTagAssociation.ResourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "catalog": "catalog",
            "database": "database",
            "table": "table",
            "table_with_columns": "tableWithColumns",
        },
    )
    class ResourceProperty:
        def __init__(
            self,
            *,
            catalog: typing.Any = None,
            database: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union["CfnTagAssociation.DatabaseResourceProperty", typing.Dict[str, typing.Any]]]] = None,
            table: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union["CfnTagAssociation.TableResourceProperty", typing.Dict[str, typing.Any]]]] = None,
            table_with_columns: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union["CfnTagAssociation.TableWithColumnsResourceProperty", typing.Dict[str, typing.Any]]]] = None,
        ) -> None:
            '''A structure for the resource.

            :param catalog: The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your AWS Lake Formation environment.
            :param database: The database for the resource. Unique to the Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database permissions to a principal.
            :param table: The table for the resource. A table is a metadata definition that represents your data. You can Grant and Revoke table privileges to a principal.
            :param table_with_columns: The table with columns for the resource. A principal with permissions to this resource can select metadata from the columns of a table in the Data Catalog and the underlying data in Amazon S3.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-resource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_lakeformation as lakeformation
                
                # catalog: Any
                # table_wildcard: Any
                
                resource_property = lakeformation.CfnTagAssociation.ResourceProperty(
                    catalog=catalog,
                    database=lakeformation.CfnTagAssociation.DatabaseResourceProperty(
                        catalog_id="catalogId",
                        name="name"
                    ),
                    table=lakeformation.CfnTagAssociation.TableResourceProperty(
                        catalog_id="catalogId",
                        database_name="databaseName",
                
                        # the properties below are optional
                        name="name",
                        table_wildcard=table_wildcard
                    ),
                    table_with_columns=lakeformation.CfnTagAssociation.TableWithColumnsResourceProperty(
                        catalog_id="catalogId",
                        column_names=["columnNames"],
                        database_name="databaseName",
                        name="name"
                    )
                )
            '''
            if __debug__:
                def stub(
                    *,
                    catalog: typing.Any = None,
                    database: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnTagAssociation.DatabaseResourceProperty, typing.Dict[str, typing.Any]]]] = None,
                    table: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnTagAssociation.TableResourceProperty, typing.Dict[str, typing.Any]]]] = None,
                    table_with_columns: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnTagAssociation.TableWithColumnsResourceProperty, typing.Dict[str, typing.Any]]]] = None,
                ) -> None:
                    ...
                type_hints = typing.get_type_hints(stub)
                check_type(argname="argument catalog", value=catalog, expected_type=type_hints["catalog"])
                check_type(argname="argument database", value=database, expected_type=type_hints["database"])
                check_type(argname="argument table", value=table, expected_type=type_hints["table"])
                check_type(argname="argument table_with_columns", value=table_with_columns, expected_type=type_hints["table_with_columns"])
            self._values: typing.Dict[str, typing.Any] = {}
            if catalog is not None:
                self._values["catalog"] = catalog
            if database is not None:
                self._values["database"] = database
            if table is not None:
                self._values["table"] = table
            if table_with_columns is not None:
                self._values["table_with_columns"] = table_with_columns

        @builtins.property
        def catalog(self) -> typing.Any:
            '''The identifier for the Data Catalog.

            By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your AWS Lake Formation environment.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-resource.html#cfn-lakeformation-tagassociation-resource-catalog
            '''
            result = self._values.get("catalog")
            return typing.cast(typing.Any, result)

        @builtins.property
        def database(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTagAssociation.DatabaseResourceProperty"]]:
            '''The database for the resource.

            Unique to the Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database permissions to a principal.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-resource.html#cfn-lakeformation-tagassociation-resource-database
            '''
            result = self._values.get("database")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTagAssociation.DatabaseResourceProperty"]], result)

        @builtins.property
        def table(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTagAssociation.TableResourceProperty"]]:
            '''The table for the resource.

            A table is a metadata definition that represents your data. You can Grant and Revoke table privileges to a principal.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-resource.html#cfn-lakeformation-tagassociation-resource-table
            '''
            result = self._values.get("table")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTagAssociation.TableResourceProperty"]], result)

        @builtins.property
        def table_with_columns(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTagAssociation.TableWithColumnsResourceProperty"]]:
            '''The table with columns for the resource.

            A principal with permissions to this resource can select metadata from the columns of a table in the Data Catalog and the underlying data in Amazon S3.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-resource.html#cfn-lakeformation-tagassociation-resource-tablewithcolumns
            '''
            result = self._values.get("table_with_columns")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTagAssociation.TableWithColumnsResourceProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-lakeformation.CfnTagAssociation.TableResourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "catalog_id": "catalogId",
            "database_name": "databaseName",
            "name": "name",
            "table_wildcard": "tableWildcard",
        },
    )
    class TableResourceProperty:
        def __init__(
            self,
            *,
            catalog_id: builtins.str,
            database_name: builtins.str,
            name: typing.Optional[builtins.str] = None,
            table_wildcard: typing.Any = None,
        ) -> None:
            '''A structure for the table object.

            A table is a metadata definition that represents your data. You can Grant and Revoke table privileges to a principal.

            :param catalog_id: The identifier for the Data Catalog . By default, it is the account ID of the caller.
            :param database_name: The name of the database for the table. Unique to a Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database privileges to a principal.
            :param name: The name of the table.
            :param table_wildcard: A wildcard object representing every table under a database. At least one of ``TableResource$Name`` or ``TableResource$TableWildcard`` is required.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-tableresource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_lakeformation as lakeformation
                
                # table_wildcard: Any
                
                table_resource_property = lakeformation.CfnTagAssociation.TableResourceProperty(
                    catalog_id="catalogId",
                    database_name="databaseName",
                
                    # the properties below are optional
                    name="name",
                    table_wildcard=table_wildcard
                )
            '''
            if __debug__:
                def stub(
                    *,
                    catalog_id: builtins.str,
                    database_name: builtins.str,
                    name: typing.Optional[builtins.str] = None,
                    table_wildcard: typing.Any = None,
                ) -> None:
                    ...
                type_hints = typing.get_type_hints(stub)
                check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
                check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument table_wildcard", value=table_wildcard, expected_type=type_hints["table_wildcard"])
            self._values: typing.Dict[str, typing.Any] = {
                "catalog_id": catalog_id,
                "database_name": database_name,
            }
            if name is not None:
                self._values["name"] = name
            if table_wildcard is not None:
                self._values["table_wildcard"] = table_wildcard

        @builtins.property
        def catalog_id(self) -> builtins.str:
            '''The identifier for the Data Catalog .

            By default, it is the account ID of the caller.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-tableresource.html#cfn-lakeformation-tagassociation-tableresource-catalogid
            '''
            result = self._values.get("catalog_id")
            assert result is not None, "Required property 'catalog_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def database_name(self) -> builtins.str:
            '''The name of the database for the table.

            Unique to a Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database privileges to a principal.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-tableresource.html#cfn-lakeformation-tagassociation-tableresource-databasename
            '''
            result = self._values.get("database_name")
            assert result is not None, "Required property 'database_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the table.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-tableresource.html#cfn-lakeformation-tagassociation-tableresource-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def table_wildcard(self) -> typing.Any:
            '''A wildcard object representing every table under a database.

            At least one of ``TableResource$Name`` or ``TableResource$TableWildcard`` is required.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-tableresource.html#cfn-lakeformation-tagassociation-tableresource-tablewildcard
            '''
            result = self._values.get("table_wildcard")
            return typing.cast(typing.Any, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TableResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-lakeformation.CfnTagAssociation.TableWithColumnsResourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "catalog_id": "catalogId",
            "column_names": "columnNames",
            "database_name": "databaseName",
            "name": "name",
        },
    )
    class TableWithColumnsResourceProperty:
        def __init__(
            self,
            *,
            catalog_id: builtins.str,
            column_names: typing.Sequence[builtins.str],
            database_name: builtins.str,
            name: builtins.str,
        ) -> None:
            '''A structure for a table with columns object. This object is only used when granting a SELECT permission.

            This object must take a value for at least one of ``ColumnsNames`` , ``ColumnsIndexes`` , or ``ColumnsWildcard`` .

            :param catalog_id: A wildcard object representing every table under a database. At least one of TableResource$Name or TableResource$TableWildcard is required.
            :param column_names: The list of column names for the table. At least one of ``ColumnNames`` or ``ColumnWildcard`` is required.
            :param database_name: The name of the database for the table with columns resource. Unique to the Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database privileges to a principal.
            :param name: The name of the table resource. A table is a metadata definition that represents your data. You can Grant and Revoke table privileges to a principal.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-tablewithcolumnsresource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_lakeformation as lakeformation
                
                table_with_columns_resource_property = lakeformation.CfnTagAssociation.TableWithColumnsResourceProperty(
                    catalog_id="catalogId",
                    column_names=["columnNames"],
                    database_name="databaseName",
                    name="name"
                )
            '''
            if __debug__:
                def stub(
                    *,
                    catalog_id: builtins.str,
                    column_names: typing.Sequence[builtins.str],
                    database_name: builtins.str,
                    name: builtins.str,
                ) -> None:
                    ...
                type_hints = typing.get_type_hints(stub)
                check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
                check_type(argname="argument column_names", value=column_names, expected_type=type_hints["column_names"])
                check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[str, typing.Any] = {
                "catalog_id": catalog_id,
                "column_names": column_names,
                "database_name": database_name,
                "name": name,
            }

        @builtins.property
        def catalog_id(self) -> builtins.str:
            '''A wildcard object representing every table under a database.

            At least one of TableResource$Name or TableResource$TableWildcard is required.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-tablewithcolumnsresource.html#cfn-lakeformation-tagassociation-tablewithcolumnsresource-catalogid
            '''
            result = self._values.get("catalog_id")
            assert result is not None, "Required property 'catalog_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def column_names(self) -> typing.List[builtins.str]:
            '''The list of column names for the table.

            At least one of ``ColumnNames`` or ``ColumnWildcard`` is required.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-tablewithcolumnsresource.html#cfn-lakeformation-tagassociation-tablewithcolumnsresource-columnnames
            '''
            result = self._values.get("column_names")
            assert result is not None, "Required property 'column_names' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def database_name(self) -> builtins.str:
            '''The name of the database for the table with columns resource.

            Unique to the Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database privileges to a principal.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-tablewithcolumnsresource.html#cfn-lakeformation-tagassociation-tablewithcolumnsresource-databasename
            '''
            result = self._values.get("database_name")
            assert result is not None, "Required property 'database_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the table resource.

            A table is a metadata definition that represents your data. You can Grant and Revoke table privileges to a principal.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-tablewithcolumnsresource.html#cfn-lakeformation-tagassociation-tablewithcolumnsresource-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TableWithColumnsResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-lakeformation.CfnTagAssociationProps",
    jsii_struct_bases=[],
    name_mapping={"lf_tags": "lfTags", "resource": "resource"},
)
class CfnTagAssociationProps:
    def __init__(
        self,
        *,
        lf_tags: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnTagAssociation.LFTagPairProperty, typing.Dict[str, typing.Any]]]]],
        resource: typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnTagAssociation.ResourceProperty, typing.Dict[str, typing.Any]]],
    ) -> None:
        '''Properties for defining a ``CfnTagAssociation``.

        :param lf_tags: A structure containing an LF-tag key-value pair.
        :param resource: UTF-8 string (valid values: ``DATABASE | TABLE`` ). The resource for which the LF-tag policy applies.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-tagassociation.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_lakeformation as lakeformation
            
            # catalog: Any
            # table_wildcard: Any
            
            cfn_tag_association_props = lakeformation.CfnTagAssociationProps(
                lf_tags=[lakeformation.CfnTagAssociation.LFTagPairProperty(
                    catalog_id="catalogId",
                    tag_key="tagKey",
                    tag_values=["tagValues"]
                )],
                resource=lakeformation.CfnTagAssociation.ResourceProperty(
                    catalog=catalog,
                    database=lakeformation.CfnTagAssociation.DatabaseResourceProperty(
                        catalog_id="catalogId",
                        name="name"
                    ),
                    table=lakeformation.CfnTagAssociation.TableResourceProperty(
                        catalog_id="catalogId",
                        database_name="databaseName",
            
                        # the properties below are optional
                        name="name",
                        table_wildcard=table_wildcard
                    ),
                    table_with_columns=lakeformation.CfnTagAssociation.TableWithColumnsResourceProperty(
                        catalog_id="catalogId",
                        column_names=["columnNames"],
                        database_name="databaseName",
                        name="name"
                    )
                )
            )
        '''
        if __debug__:
            def stub(
                *,
                lf_tags: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnTagAssociation.LFTagPairProperty, typing.Dict[str, typing.Any]]]]],
                resource: typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnTagAssociation.ResourceProperty, typing.Dict[str, typing.Any]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument lf_tags", value=lf_tags, expected_type=type_hints["lf_tags"])
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        self._values: typing.Dict[str, typing.Any] = {
            "lf_tags": lf_tags,
            "resource": resource,
        }

    @builtins.property
    def lf_tags(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnTagAssociation.LFTagPairProperty]]]:
        '''A structure containing an LF-tag key-value pair.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-tagassociation.html#cfn-lakeformation-tagassociation-lftags
        '''
        result = self._values.get("lf_tags")
        assert result is not None, "Required property 'lf_tags' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnTagAssociation.LFTagPairProperty]]], result)

    @builtins.property
    def resource(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnTagAssociation.ResourceProperty]:
        '''UTF-8 string (valid values: ``DATABASE | TABLE`` ).

        The resource for which the LF-tag policy applies.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-tagassociation.html#cfn-lakeformation-tagassociation-resource
        '''
        result = self._values.get("resource")
        assert result is not None, "Required property 'resource' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnTagAssociation.ResourceProperty], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTagAssociationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-lakeformation.CfnTagProps",
    jsii_struct_bases=[],
    name_mapping={
        "tag_key": "tagKey",
        "tag_values": "tagValues",
        "catalog_id": "catalogId",
    },
)
class CfnTagProps:
    def __init__(
        self,
        *,
        tag_key: builtins.str,
        tag_values: typing.Sequence[builtins.str],
        catalog_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnTag``.

        :param tag_key: UTF-8 string, not less than 1 or more than 255 bytes long, matching the `single-line string pattern <https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api-aws-lake-formation-api-common.html#aws-glue-api-regex-oneLine>`_ . The key-name for the LF-tag.
        :param tag_values: An array of UTF-8 strings, not less than 1 or more than 50 strings. A list of possible values of the corresponding ``TagKey`` of an LF-tag key-value pair.
        :param catalog_id: Catalog id string, not less than 1 or more than 255 bytes long, matching the `single-line string pattern <https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api-aws-lake-formation-api-common.html#aws-glue-api-regex-oneLine>`_ . The identifier for the Data Catalog . By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your AWS Lake Formation environment.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-tag.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_lakeformation as lakeformation
            
            cfn_tag_props = lakeformation.CfnTagProps(
                tag_key="tagKey",
                tag_values=["tagValues"],
            
                # the properties below are optional
                catalog_id="catalogId"
            )
        '''
        if __debug__:
            def stub(
                *,
                tag_key: builtins.str,
                tag_values: typing.Sequence[builtins.str],
                catalog_id: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument tag_key", value=tag_key, expected_type=type_hints["tag_key"])
            check_type(argname="argument tag_values", value=tag_values, expected_type=type_hints["tag_values"])
            check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "tag_key": tag_key,
            "tag_values": tag_values,
        }
        if catalog_id is not None:
            self._values["catalog_id"] = catalog_id

    @builtins.property
    def tag_key(self) -> builtins.str:
        '''UTF-8 string, not less than 1 or more than 255 bytes long, matching the `single-line string pattern <https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api-aws-lake-formation-api-common.html#aws-glue-api-regex-oneLine>`_ .

        The key-name for the LF-tag.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-tag.html#cfn-lakeformation-tag-tagkey
        '''
        result = self._values.get("tag_key")
        assert result is not None, "Required property 'tag_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tag_values(self) -> typing.List[builtins.str]:
        '''An array of UTF-8 strings, not less than 1 or more than 50 strings.

        A list of possible values of the corresponding ``TagKey`` of an LF-tag key-value pair.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-tag.html#cfn-lakeformation-tag-tagvalues
        '''
        result = self._values.get("tag_values")
        assert result is not None, "Required property 'tag_values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def catalog_id(self) -> typing.Optional[builtins.str]:
        '''Catalog id string, not less than 1 or more than 255 bytes long, matching the `single-line string pattern <https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api-aws-lake-formation-api-common.html#aws-glue-api-regex-oneLine>`_ .

        The identifier for the Data Catalog . By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your AWS Lake Formation environment.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-tag.html#cfn-lakeformation-tag-catalogid
        '''
        result = self._values.get("catalog_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTagProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnDataCellsFilter",
    "CfnDataCellsFilterProps",
    "CfnDataLakeSettings",
    "CfnDataLakeSettingsProps",
    "CfnPermissions",
    "CfnPermissionsProps",
    "CfnPrincipalPermissions",
    "CfnPrincipalPermissionsProps",
    "CfnResource",
    "CfnResourceProps",
    "CfnTag",
    "CfnTagAssociation",
    "CfnTagAssociationProps",
    "CfnTagProps",
]

publication.publish()
