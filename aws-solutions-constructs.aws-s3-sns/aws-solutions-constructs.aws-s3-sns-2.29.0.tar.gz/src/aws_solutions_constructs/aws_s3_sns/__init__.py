'''
# aws-s3-sns module

<!--BEGIN STABILITY BANNER-->---


![Stability: Experimental](https://img.shields.io/badge/stability-Experimental-important.svg?style=for-the-badge)

> All classes are under active development and subject to non-backward compatible changes or removal in any
> future version. These are not subject to the [Semantic Versioning](https://semver.org/) model.
> This means that while you may use them, you may need to update your source code when upgrading to a newer version of this package.

---
<!--END STABILITY BANNER-->

| **Reference Documentation**:| <span style="font-weight: normal">https://docs.aws.amazon.com/solutions/latest/constructs/</span>|
|:-------------|:-------------|

<div style="height:8px"></div>

| **Language**     | **Package**        |
|:-------------|-----------------|
|![Python Logo](https://docs.aws.amazon.com/cdk/api/latest/img/python32.png) Python|`aws_solutions_constructs.aws_s3_sns`|
|![Typescript Logo](https://docs.aws.amazon.com/cdk/api/latest/img/typescript32.png) Typescript|`@aws-solutions-constructs/aws-s3-sns`|
|![Java Logo](https://docs.aws.amazon.com/cdk/api/latest/img/java32.png) Java|`software.amazon.awsconstructs.services.s3sns`|

## Overview

This AWS Solutions Construct implements an Amazon S3 Bucket that is configured to send S3 event messages to an Amazon SNS topic.

Here is a minimal deployable pattern definition:

Typescript

```python
import { Construct } from 'constructs';
import { Stack, StackProps } from 'aws-cdk-lib';
import { S3ToSns } from "@aws-solutions-constructs/aws-s3-sns";

new S3ToSns(this, 'S3ToSNSPattern', {});
```

Python

```python
from aws_solutions_constructs.aws_s3_sns import S3ToSns
from aws_cdk import Stack
from constructs import Construct

S3ToSns(self, 'S3ToSNSPattern')
```

Java

```java
import software.constructs.Construct;

import software.amazon.awscdk.Stack;
import software.amazon.awscdk.StackProps;
import software.amazon.awsconstructs.services.s3sns.*;

new S3ToSns(this, "S3ToSNSPattern", new S3ToSnsProps.Builder()
        .build());
```

## Pattern Construct Props

| **Name**     | **Type**        | **Description** |
|:-------------|:----------------|-----------------|
|existingBucketObj?|[`s3.Bucket`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.Bucket.html)|Existing instance of S3 Bucket object. If this is provided, then also providing bucketProps is an error. |
|bucketProps?|[`s3.BucketProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.BucketProps.html)|Optional user provided props to override the default props for the S3 Bucket.|
|s3EventTypes?|[`s3.EventType[]`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.EventType.html)|The S3 event types that will trigger the notification. Defaults to s3.EventType.OBJECT_CREATED.|
|s3EventFilters?|[`s3.NotificationKeyFilter[]`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.NotificationKeyFilter.html)|S3 object key filter rules to determine which objects trigger this event. If not specified no filter rules will be applied.|
|loggingBucketProps?|[`s3.BucketProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.BucketProps.html)|Optional user provided props to override the default props for the S3 Logging Bucket.|
|logS3AccessLogs?|`boolean`|Whether to turn on Access Logging for the S3 bucket. Creates an S3 bucket with associated storage costs for the logs. Enabling Access Logging is a best practice. default - true|
|existingTopicObj?|[`sns.Topic`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_sns.Topic.html)|An optional, existing SNS topic to be used instead of the default topic. Providing both this and `topicProps` will cause an error. If the SNS Topic is encrypted with a Customer-Managed KMS Key, the key must be specified in the `existingTopicEncryptionKey` property.|
|existingTopicEncryptionKey?|[`kms.Key`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_kms.Key.html)|If an existing topic is provided in the `existingTopicObj` property, and that topic is encrypted with a Customer-Managed KMS key, this property also needs to be set with same key.|
|topicProps?|[`sns.TopicProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_sns.TopicProps.html)|Optional user provided props to override the default props for the SNS topic.|
|enableEncryptionWithCustomerManagedKey?|`boolean`|If no key is provided, this flag determines whether the topic is encrypted with a new CMK or an AWS managed key. This flag is ignored if any of the following are defined: topicProps.encryptionMasterKey, encryptionKey or encryptionKeyProps.|
|encryptionKey?|[`kms.Key`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_kms.Key.html)|An optional, imported encryption key to encrypt the SNS Topic with.|
|encryptionKeyProps?|[`kms.KeyProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_kms.Key.html#construct-props)|Optional user provided properties to override the default properties for the KMS encryption key used to encrypt the SNS Topic with.|

## Pattern Properties

| **Name**     | **Type**        | **Description** |
|:-------------|:----------------|-----------------|
|snsTopic|[`sns.Topic`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_sns.Topic.html)|Returns an instance of the SNS Topic created by the pattern.|
|encryptionKey?|[`kms.Key`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_kms.Key.html)|Returns an instance of the kms.Key associated with the SNS Topic|
|s3Bucket?|[`s3.Bucket`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.Bucket.html)|Returns an instance of the s3.Bucket created by the construct|
|s3LoggingBucket?|[`s3.Bucket`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.Bucket.html)|Returns an instance of s3.Bucket created by the construct as the logging bucket for the primary bucket.|
|s3BucketInterface|[`s3.IBucket`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.IBucket.html)|Returns an instance of s3.IBucket created by the construct.|

## Default settings

Out of the box implementation of the Construct without any override will set the following defaults:

### Amazon S3 Bucket

* Configure Access logging for the S3 Bucket
* Enable server-side encryption for S3 Bucket using an AWS managed KMS Key
* Enforce encryption of data in transit
* Turn on the versioning for the S3 Bucket
* Don't allow public access for the S3 Bucket
* Retain the S3 Bucket when deleting the CloudFormation stack
* Applies Lifecycle rule to move noncurrent object versions to Glacier storage after 90 days

### Amazon SNS Topic

* Configure least privilege SNS Topic access policy to allow the S3 Bucket to publish messages to it
* Enable server-side encryption for the SNS Topic using an AWS managed KMS Key
* Enforce encryption of data in transit

## Architecture

![Architecture Diagram](architecture.png)

---


© Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.
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

import aws_cdk.aws_kms
import aws_cdk.aws_s3
import aws_cdk.aws_sns
import constructs


class S3ToSns(
    constructs.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-solutions-constructs/aws-s3-sns.S3ToSns",
):
    '''
    :summary: The S3ToSns class.
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        bucket_props: typing.Optional[typing.Union[aws_cdk.aws_s3.BucketProps, typing.Dict[str, typing.Any]]] = None,
        enable_encryption_with_customer_managed_key: typing.Optional[builtins.bool] = None,
        encryption_key: typing.Optional[aws_cdk.aws_kms.Key] = None,
        encryption_key_props: typing.Optional[typing.Union[aws_cdk.aws_kms.KeyProps, typing.Dict[str, typing.Any]]] = None,
        existing_bucket_obj: typing.Optional[aws_cdk.aws_s3.Bucket] = None,
        existing_topic_encryption_key: typing.Optional[aws_cdk.aws_kms.Key] = None,
        existing_topic_obj: typing.Optional[aws_cdk.aws_sns.Topic] = None,
        logging_bucket_props: typing.Optional[typing.Union[aws_cdk.aws_s3.BucketProps, typing.Dict[str, typing.Any]]] = None,
        log_s3_access_logs: typing.Optional[builtins.bool] = None,
        s3_event_filters: typing.Optional[typing.Sequence[typing.Union[aws_cdk.aws_s3.NotificationKeyFilter, typing.Dict[str, typing.Any]]]] = None,
        s3_event_types: typing.Optional[typing.Sequence[aws_cdk.aws_s3.EventType]] = None,
        topic_props: typing.Optional[typing.Union[aws_cdk.aws_sns.TopicProps, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param scope: - represents the scope for all the resources.
        :param id: - this is a a scope-unique id.
        :param bucket_props: Optional user provided props to override the default props for the S3 Bucket. Default: - Default props are used
        :param enable_encryption_with_customer_managed_key: If no key is provided, this flag determines whether the topic is encrypted with a new CMK or an AWS managed key. This flag is ignored if any of the following are defined: topicProps.masterKey, encryptionKey or encryptionKeyProps. Default: - False if topicProps.masterKey, encryptionKey, and encryptionKeyProps are all undefined.
        :param encryption_key: An optional, imported encryption key to encrypt the SNS Topic with. Default: - None
        :param encryption_key_props: Optional user provided properties to override the default properties for the KMS encryption key used to encrypt the SNS Topic with. Default: - None
        :param existing_bucket_obj: Existing instance of S3 Bucket object, providing both this and ``bucketProps`` will cause an error. Default: - None
        :param existing_topic_encryption_key: If an existing topic is provided in the ``existingTopicObj`` property, and that topic is encrypted with a Customer-Managed KMS key, this property also needs to be set with same key. Default: - None
        :param existing_topic_obj: An optional, existing SNS topic to be used instead of the default topic. Providing both this and ``topicProps`` will cause an error. If the SNS Topic is encrypted with a Customer-Managed KMS Key, the key must be specified in the ``existingTopicEncryptionKey`` property. Default: - Default props are used
        :param logging_bucket_props: Optional user provided props to override the default props for the S3 Logging Bucket. Default: - Default props are used
        :param log_s3_access_logs: Whether to turn on Access Logs for the S3 bucket with the associated storage costs. Enabling Access Logging is a best practice. Default: - true
        :param s3_event_filters: S3 object key filter rules to determine which objects trigger this event. Default: - If not specified no filter rules will be applied.
        :param s3_event_types: The S3 event types that will trigger the notification. Default: - If not specified the s3.EventType.OBJECT_CREATED event will trigger the notification.
        :param topic_props: Optional user provided properties. Default: - Default props are used

        :access: public
        :since: 0.8.0
        :summary: Constructs a new instance of the S3ToSns class.
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                id: builtins.str,
                *,
                bucket_props: typing.Optional[typing.Union[aws_cdk.aws_s3.BucketProps, typing.Dict[str, typing.Any]]] = None,
                enable_encryption_with_customer_managed_key: typing.Optional[builtins.bool] = None,
                encryption_key: typing.Optional[aws_cdk.aws_kms.Key] = None,
                encryption_key_props: typing.Optional[typing.Union[aws_cdk.aws_kms.KeyProps, typing.Dict[str, typing.Any]]] = None,
                existing_bucket_obj: typing.Optional[aws_cdk.aws_s3.Bucket] = None,
                existing_topic_encryption_key: typing.Optional[aws_cdk.aws_kms.Key] = None,
                existing_topic_obj: typing.Optional[aws_cdk.aws_sns.Topic] = None,
                logging_bucket_props: typing.Optional[typing.Union[aws_cdk.aws_s3.BucketProps, typing.Dict[str, typing.Any]]] = None,
                log_s3_access_logs: typing.Optional[builtins.bool] = None,
                s3_event_filters: typing.Optional[typing.Sequence[typing.Union[aws_cdk.aws_s3.NotificationKeyFilter, typing.Dict[str, typing.Any]]]] = None,
                s3_event_types: typing.Optional[typing.Sequence[aws_cdk.aws_s3.EventType]] = None,
                topic_props: typing.Optional[typing.Union[aws_cdk.aws_sns.TopicProps, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = S3ToSnsProps(
            bucket_props=bucket_props,
            enable_encryption_with_customer_managed_key=enable_encryption_with_customer_managed_key,
            encryption_key=encryption_key,
            encryption_key_props=encryption_key_props,
            existing_bucket_obj=existing_bucket_obj,
            existing_topic_encryption_key=existing_topic_encryption_key,
            existing_topic_obj=existing_topic_obj,
            logging_bucket_props=logging_bucket_props,
            log_s3_access_logs=log_s3_access_logs,
            s3_event_filters=s3_event_filters,
            s3_event_types=s3_event_types,
            topic_props=topic_props,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="s3BucketInterface")
    def s3_bucket_interface(self) -> aws_cdk.aws_s3.IBucket:
        return typing.cast(aws_cdk.aws_s3.IBucket, jsii.get(self, "s3BucketInterface"))

    @builtins.property
    @jsii.member(jsii_name="snsTopic")
    def sns_topic(self) -> aws_cdk.aws_sns.Topic:
        return typing.cast(aws_cdk.aws_sns.Topic, jsii.get(self, "snsTopic"))

    @builtins.property
    @jsii.member(jsii_name="encryptionKey")
    def encryption_key(self) -> typing.Optional[aws_cdk.aws_kms.IKey]:
        return typing.cast(typing.Optional[aws_cdk.aws_kms.IKey], jsii.get(self, "encryptionKey"))

    @builtins.property
    @jsii.member(jsii_name="s3Bucket")
    def s3_bucket(self) -> typing.Optional[aws_cdk.aws_s3.Bucket]:
        return typing.cast(typing.Optional[aws_cdk.aws_s3.Bucket], jsii.get(self, "s3Bucket"))

    @builtins.property
    @jsii.member(jsii_name="s3LoggingBucket")
    def s3_logging_bucket(self) -> typing.Optional[aws_cdk.aws_s3.Bucket]:
        return typing.cast(typing.Optional[aws_cdk.aws_s3.Bucket], jsii.get(self, "s3LoggingBucket"))


@jsii.data_type(
    jsii_type="@aws-solutions-constructs/aws-s3-sns.S3ToSnsProps",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_props": "bucketProps",
        "enable_encryption_with_customer_managed_key": "enableEncryptionWithCustomerManagedKey",
        "encryption_key": "encryptionKey",
        "encryption_key_props": "encryptionKeyProps",
        "existing_bucket_obj": "existingBucketObj",
        "existing_topic_encryption_key": "existingTopicEncryptionKey",
        "existing_topic_obj": "existingTopicObj",
        "logging_bucket_props": "loggingBucketProps",
        "log_s3_access_logs": "logS3AccessLogs",
        "s3_event_filters": "s3EventFilters",
        "s3_event_types": "s3EventTypes",
        "topic_props": "topicProps",
    },
)
class S3ToSnsProps:
    def __init__(
        self,
        *,
        bucket_props: typing.Optional[typing.Union[aws_cdk.aws_s3.BucketProps, typing.Dict[str, typing.Any]]] = None,
        enable_encryption_with_customer_managed_key: typing.Optional[builtins.bool] = None,
        encryption_key: typing.Optional[aws_cdk.aws_kms.Key] = None,
        encryption_key_props: typing.Optional[typing.Union[aws_cdk.aws_kms.KeyProps, typing.Dict[str, typing.Any]]] = None,
        existing_bucket_obj: typing.Optional[aws_cdk.aws_s3.Bucket] = None,
        existing_topic_encryption_key: typing.Optional[aws_cdk.aws_kms.Key] = None,
        existing_topic_obj: typing.Optional[aws_cdk.aws_sns.Topic] = None,
        logging_bucket_props: typing.Optional[typing.Union[aws_cdk.aws_s3.BucketProps, typing.Dict[str, typing.Any]]] = None,
        log_s3_access_logs: typing.Optional[builtins.bool] = None,
        s3_event_filters: typing.Optional[typing.Sequence[typing.Union[aws_cdk.aws_s3.NotificationKeyFilter, typing.Dict[str, typing.Any]]]] = None,
        s3_event_types: typing.Optional[typing.Sequence[aws_cdk.aws_s3.EventType]] = None,
        topic_props: typing.Optional[typing.Union[aws_cdk.aws_sns.TopicProps, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param bucket_props: Optional user provided props to override the default props for the S3 Bucket. Default: - Default props are used
        :param enable_encryption_with_customer_managed_key: If no key is provided, this flag determines whether the topic is encrypted with a new CMK or an AWS managed key. This flag is ignored if any of the following are defined: topicProps.masterKey, encryptionKey or encryptionKeyProps. Default: - False if topicProps.masterKey, encryptionKey, and encryptionKeyProps are all undefined.
        :param encryption_key: An optional, imported encryption key to encrypt the SNS Topic with. Default: - None
        :param encryption_key_props: Optional user provided properties to override the default properties for the KMS encryption key used to encrypt the SNS Topic with. Default: - None
        :param existing_bucket_obj: Existing instance of S3 Bucket object, providing both this and ``bucketProps`` will cause an error. Default: - None
        :param existing_topic_encryption_key: If an existing topic is provided in the ``existingTopicObj`` property, and that topic is encrypted with a Customer-Managed KMS key, this property also needs to be set with same key. Default: - None
        :param existing_topic_obj: An optional, existing SNS topic to be used instead of the default topic. Providing both this and ``topicProps`` will cause an error. If the SNS Topic is encrypted with a Customer-Managed KMS Key, the key must be specified in the ``existingTopicEncryptionKey`` property. Default: - Default props are used
        :param logging_bucket_props: Optional user provided props to override the default props for the S3 Logging Bucket. Default: - Default props are used
        :param log_s3_access_logs: Whether to turn on Access Logs for the S3 bucket with the associated storage costs. Enabling Access Logging is a best practice. Default: - true
        :param s3_event_filters: S3 object key filter rules to determine which objects trigger this event. Default: - If not specified no filter rules will be applied.
        :param s3_event_types: The S3 event types that will trigger the notification. Default: - If not specified the s3.EventType.OBJECT_CREATED event will trigger the notification.
        :param topic_props: Optional user provided properties. Default: - Default props are used

        :summary: The properties for the S3ToSns class.
        '''
        if isinstance(bucket_props, dict):
            bucket_props = aws_cdk.aws_s3.BucketProps(**bucket_props)
        if isinstance(encryption_key_props, dict):
            encryption_key_props = aws_cdk.aws_kms.KeyProps(**encryption_key_props)
        if isinstance(logging_bucket_props, dict):
            logging_bucket_props = aws_cdk.aws_s3.BucketProps(**logging_bucket_props)
        if isinstance(topic_props, dict):
            topic_props = aws_cdk.aws_sns.TopicProps(**topic_props)
        if __debug__:
            def stub(
                *,
                bucket_props: typing.Optional[typing.Union[aws_cdk.aws_s3.BucketProps, typing.Dict[str, typing.Any]]] = None,
                enable_encryption_with_customer_managed_key: typing.Optional[builtins.bool] = None,
                encryption_key: typing.Optional[aws_cdk.aws_kms.Key] = None,
                encryption_key_props: typing.Optional[typing.Union[aws_cdk.aws_kms.KeyProps, typing.Dict[str, typing.Any]]] = None,
                existing_bucket_obj: typing.Optional[aws_cdk.aws_s3.Bucket] = None,
                existing_topic_encryption_key: typing.Optional[aws_cdk.aws_kms.Key] = None,
                existing_topic_obj: typing.Optional[aws_cdk.aws_sns.Topic] = None,
                logging_bucket_props: typing.Optional[typing.Union[aws_cdk.aws_s3.BucketProps, typing.Dict[str, typing.Any]]] = None,
                log_s3_access_logs: typing.Optional[builtins.bool] = None,
                s3_event_filters: typing.Optional[typing.Sequence[typing.Union[aws_cdk.aws_s3.NotificationKeyFilter, typing.Dict[str, typing.Any]]]] = None,
                s3_event_types: typing.Optional[typing.Sequence[aws_cdk.aws_s3.EventType]] = None,
                topic_props: typing.Optional[typing.Union[aws_cdk.aws_sns.TopicProps, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument bucket_props", value=bucket_props, expected_type=type_hints["bucket_props"])
            check_type(argname="argument enable_encryption_with_customer_managed_key", value=enable_encryption_with_customer_managed_key, expected_type=type_hints["enable_encryption_with_customer_managed_key"])
            check_type(argname="argument encryption_key", value=encryption_key, expected_type=type_hints["encryption_key"])
            check_type(argname="argument encryption_key_props", value=encryption_key_props, expected_type=type_hints["encryption_key_props"])
            check_type(argname="argument existing_bucket_obj", value=existing_bucket_obj, expected_type=type_hints["existing_bucket_obj"])
            check_type(argname="argument existing_topic_encryption_key", value=existing_topic_encryption_key, expected_type=type_hints["existing_topic_encryption_key"])
            check_type(argname="argument existing_topic_obj", value=existing_topic_obj, expected_type=type_hints["existing_topic_obj"])
            check_type(argname="argument logging_bucket_props", value=logging_bucket_props, expected_type=type_hints["logging_bucket_props"])
            check_type(argname="argument log_s3_access_logs", value=log_s3_access_logs, expected_type=type_hints["log_s3_access_logs"])
            check_type(argname="argument s3_event_filters", value=s3_event_filters, expected_type=type_hints["s3_event_filters"])
            check_type(argname="argument s3_event_types", value=s3_event_types, expected_type=type_hints["s3_event_types"])
            check_type(argname="argument topic_props", value=topic_props, expected_type=type_hints["topic_props"])
        self._values: typing.Dict[str, typing.Any] = {}
        if bucket_props is not None:
            self._values["bucket_props"] = bucket_props
        if enable_encryption_with_customer_managed_key is not None:
            self._values["enable_encryption_with_customer_managed_key"] = enable_encryption_with_customer_managed_key
        if encryption_key is not None:
            self._values["encryption_key"] = encryption_key
        if encryption_key_props is not None:
            self._values["encryption_key_props"] = encryption_key_props
        if existing_bucket_obj is not None:
            self._values["existing_bucket_obj"] = existing_bucket_obj
        if existing_topic_encryption_key is not None:
            self._values["existing_topic_encryption_key"] = existing_topic_encryption_key
        if existing_topic_obj is not None:
            self._values["existing_topic_obj"] = existing_topic_obj
        if logging_bucket_props is not None:
            self._values["logging_bucket_props"] = logging_bucket_props
        if log_s3_access_logs is not None:
            self._values["log_s3_access_logs"] = log_s3_access_logs
        if s3_event_filters is not None:
            self._values["s3_event_filters"] = s3_event_filters
        if s3_event_types is not None:
            self._values["s3_event_types"] = s3_event_types
        if topic_props is not None:
            self._values["topic_props"] = topic_props

    @builtins.property
    def bucket_props(self) -> typing.Optional[aws_cdk.aws_s3.BucketProps]:
        '''Optional user provided props to override the default props for the S3 Bucket.

        :default: - Default props are used
        '''
        result = self._values.get("bucket_props")
        return typing.cast(typing.Optional[aws_cdk.aws_s3.BucketProps], result)

    @builtins.property
    def enable_encryption_with_customer_managed_key(
        self,
    ) -> typing.Optional[builtins.bool]:
        '''If no key is provided, this flag determines whether the topic is encrypted with a new CMK or an AWS managed key.

        This flag is ignored if any of the following are defined: topicProps.masterKey, encryptionKey or encryptionKeyProps.

        :default: - False if topicProps.masterKey, encryptionKey, and encryptionKeyProps are all undefined.
        '''
        result = self._values.get("enable_encryption_with_customer_managed_key")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def encryption_key(self) -> typing.Optional[aws_cdk.aws_kms.Key]:
        '''An optional, imported encryption key to encrypt the SNS Topic with.

        :default: - None
        '''
        result = self._values.get("encryption_key")
        return typing.cast(typing.Optional[aws_cdk.aws_kms.Key], result)

    @builtins.property
    def encryption_key_props(self) -> typing.Optional[aws_cdk.aws_kms.KeyProps]:
        '''Optional user provided properties to override the default properties for the KMS encryption key used to encrypt the SNS Topic with.

        :default: - None
        '''
        result = self._values.get("encryption_key_props")
        return typing.cast(typing.Optional[aws_cdk.aws_kms.KeyProps], result)

    @builtins.property
    def existing_bucket_obj(self) -> typing.Optional[aws_cdk.aws_s3.Bucket]:
        '''Existing instance of S3 Bucket object, providing both this and ``bucketProps`` will cause an error.

        :default: - None
        '''
        result = self._values.get("existing_bucket_obj")
        return typing.cast(typing.Optional[aws_cdk.aws_s3.Bucket], result)

    @builtins.property
    def existing_topic_encryption_key(self) -> typing.Optional[aws_cdk.aws_kms.Key]:
        '''If an existing topic is provided in the ``existingTopicObj`` property, and that topic is encrypted with a Customer-Managed KMS key, this property also needs to be set with same key.

        :default: - None
        '''
        result = self._values.get("existing_topic_encryption_key")
        return typing.cast(typing.Optional[aws_cdk.aws_kms.Key], result)

    @builtins.property
    def existing_topic_obj(self) -> typing.Optional[aws_cdk.aws_sns.Topic]:
        '''An optional, existing SNS topic to be used instead of the default topic.

        Providing both this and ``topicProps`` will cause an error.
        If the SNS Topic is encrypted with a Customer-Managed KMS Key, the key must be specified in the ``existingTopicEncryptionKey`` property.

        :default: - Default props are used
        '''
        result = self._values.get("existing_topic_obj")
        return typing.cast(typing.Optional[aws_cdk.aws_sns.Topic], result)

    @builtins.property
    def logging_bucket_props(self) -> typing.Optional[aws_cdk.aws_s3.BucketProps]:
        '''Optional user provided props to override the default props for the S3 Logging Bucket.

        :default: - Default props are used
        '''
        result = self._values.get("logging_bucket_props")
        return typing.cast(typing.Optional[aws_cdk.aws_s3.BucketProps], result)

    @builtins.property
    def log_s3_access_logs(self) -> typing.Optional[builtins.bool]:
        '''Whether to turn on Access Logs for the S3 bucket with the associated storage costs.

        Enabling Access Logging is a best practice.

        :default: - true
        '''
        result = self._values.get("log_s3_access_logs")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def s3_event_filters(
        self,
    ) -> typing.Optional[typing.List[aws_cdk.aws_s3.NotificationKeyFilter]]:
        '''S3 object key filter rules to determine which objects trigger this event.

        :default: - If not specified no filter rules will be applied.
        '''
        result = self._values.get("s3_event_filters")
        return typing.cast(typing.Optional[typing.List[aws_cdk.aws_s3.NotificationKeyFilter]], result)

    @builtins.property
    def s3_event_types(self) -> typing.Optional[typing.List[aws_cdk.aws_s3.EventType]]:
        '''The S3 event types that will trigger the notification.

        :default: - If not specified the s3.EventType.OBJECT_CREATED event will trigger the notification.
        '''
        result = self._values.get("s3_event_types")
        return typing.cast(typing.Optional[typing.List[aws_cdk.aws_s3.EventType]], result)

    @builtins.property
    def topic_props(self) -> typing.Optional[aws_cdk.aws_sns.TopicProps]:
        '''Optional user provided properties.

        :default: - Default props are used
        '''
        result = self._values.get("topic_props")
        return typing.cast(typing.Optional[aws_cdk.aws_sns.TopicProps], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3ToSnsProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "S3ToSns",
    "S3ToSnsProps",
]

publication.publish()
