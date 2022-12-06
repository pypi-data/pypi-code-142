'''
# `google_network_services_edge_cache_origin`

Refer to the Terraform Registory for docs: [`google_network_services_edge_cache_origin`](https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin).
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

import cdktf as _cdktf_9a9027ec
import constructs as _constructs_77d1e7e8


class NetworkServicesEdgeCacheOrigin(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.networkServicesEdgeCacheOrigin.NetworkServicesEdgeCacheOrigin",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin google_network_services_edge_cache_origin}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        origin_address: builtins.str,
        aws_v4_authentication: typing.Optional[typing.Union["NetworkServicesEdgeCacheOriginAwsV4Authentication", typing.Dict[builtins.str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        failover_origin: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        max_attempts: typing.Optional[jsii.Number] = None,
        port: typing.Optional[jsii.Number] = None,
        project: typing.Optional[builtins.str] = None,
        protocol: typing.Optional[builtins.str] = None,
        retry_conditions: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeout: typing.Optional[typing.Union["NetworkServicesEdgeCacheOriginTimeout", typing.Dict[builtins.str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["NetworkServicesEdgeCacheOriginTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin google_network_services_edge_cache_origin} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Name of the resource; provided by the client when the resource is created. The name must be 1-64 characters long, and match the regular expression [a-zA-Z][a-zA-Z0-9_-]* which means the first character must be a letter, and all following characters must be a dash, underscore, letter or digit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#name NetworkServicesEdgeCacheOrigin#name}
        :param origin_address: A fully qualified domain name (FQDN) or IP address reachable over the public Internet, or the address of a Google Cloud Storage bucket. This address will be used as the origin for cache requests - e.g. FQDN: media-backend.example.com, IPv4: 35.218.1.1, IPv6: 2607:f8b0:4012:809::200e, Cloud Storage: gs://bucketname When providing an FQDN (hostname), it must be publicly resolvable (e.g. via Google public DNS) and IP addresses must be publicly routable. It must not contain a protocol (e.g., https://) and it must not contain any slashes. If a Cloud Storage bucket is provided, it must be in the canonical "gs://bucketname" format. Other forms, such as "storage.googleapis.com", will be rejected. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#origin_address NetworkServicesEdgeCacheOrigin#origin_address}
        :param aws_v4_authentication: aws_v4_authentication block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#aws_v4_authentication NetworkServicesEdgeCacheOrigin#aws_v4_authentication}
        :param description: A human-readable description of the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#description NetworkServicesEdgeCacheOrigin#description}
        :param failover_origin: The Origin resource to try when the current origin cannot be reached. After maxAttempts is reached, the configured failoverOrigin will be used to fulfil the request. The value of timeout.maxAttemptsTimeout dictates the timeout across all origins. A reference to a Topic resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#failover_origin NetworkServicesEdgeCacheOrigin#failover_origin}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#id NetworkServicesEdgeCacheOrigin#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: Set of label tags associated with the EdgeCache resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#labels NetworkServicesEdgeCacheOrigin#labels}
        :param max_attempts: The maximum number of attempts to cache fill from this origin. Another attempt is made when a cache fill fails with one of the retryConditions. Once maxAttempts to this origin have failed the failoverOrigin will be used, if one is specified. That failoverOrigin may specify its own maxAttempts, retryConditions and failoverOrigin to control its own cache fill failures. The total number of allowed attempts to cache fill across this and failover origins is limited to four. The total time allowed for cache fill attempts across this and failover origins can be controlled with maxAttemptsTimeout. The last valid, non-retried response from all origins will be returned to the client. If no origin returns a valid response, an HTTP 502 will be returned to the client. Defaults to 1. Must be a value greater than 0 and less than 4. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#max_attempts NetworkServicesEdgeCacheOrigin#max_attempts}
        :param port: The port to connect to the origin on. Defaults to port 443 for HTTP2 and HTTPS protocols, and port 80 for HTTP. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#port NetworkServicesEdgeCacheOrigin#port}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#project NetworkServicesEdgeCacheOrigin#project}.
        :param protocol: The protocol to use to connect to the configured origin. Defaults to HTTP2, and it is strongly recommended that users use HTTP2 for both security & performance. When using HTTP2 or HTTPS as the protocol, a valid, publicly-signed, unexpired TLS (SSL) certificate must be presented by the origin server. Possible values: ["HTTP2", "HTTPS", "HTTP"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#protocol NetworkServicesEdgeCacheOrigin#protocol}
        :param retry_conditions: Specifies one or more retry conditions for the configured origin. If the failure mode during a connection attempt to the origin matches the configured retryCondition(s), the origin request will be retried up to maxAttempts times. The failoverOrigin, if configured, will then be used to satisfy the request. The default retryCondition is "CONNECT_FAILURE". retryConditions apply to this origin, and not subsequent failoverOrigin(s), which may specify their own retryConditions and maxAttempts. Valid values are: - CONNECT_FAILURE: Retry on failures connecting to origins, for example due to connection timeouts. - HTTP_5XX: Retry if the origin responds with any 5xx response code, or if the origin does not respond at all, example: disconnects, reset, read timeout, connection failure, and refused streams. - GATEWAY_ERROR: Similar to 5xx, but only applies to response codes 502, 503 or 504. - RETRIABLE_4XX: Retry for retriable 4xx response codes, which include HTTP 409 (Conflict) and HTTP 429 (Too Many Requests) - NOT_FOUND: Retry if the origin returns a HTTP 404 (Not Found). This can be useful when generating video content, and the segment is not available yet. - FORBIDDEN: Retry if the origin returns a HTTP 403 (Forbidden). Possible values: ["CONNECT_FAILURE", "HTTP_5XX", "GATEWAY_ERROR", "RETRIABLE_4XX", "NOT_FOUND", "FORBIDDEN"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#retry_conditions NetworkServicesEdgeCacheOrigin#retry_conditions}
        :param timeout: timeout block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#timeout NetworkServicesEdgeCacheOrigin#timeout}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#timeouts NetworkServicesEdgeCacheOrigin#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1c21df93d1996318f9c957070740c8d72e22c37e5bff3072eb29fb680a72cb2)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = NetworkServicesEdgeCacheOriginConfig(
            name=name,
            origin_address=origin_address,
            aws_v4_authentication=aws_v4_authentication,
            description=description,
            failover_origin=failover_origin,
            id=id,
            labels=labels,
            max_attempts=max_attempts,
            port=port,
            project=project,
            protocol=protocol,
            retry_conditions=retry_conditions,
            timeout=timeout,
            timeouts=timeouts,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAwsV4Authentication")
    def put_aws_v4_authentication(
        self,
        *,
        access_key_id: builtins.str,
        origin_region: builtins.str,
        secret_access_key_version: builtins.str,
    ) -> None:
        '''
        :param access_key_id: The access key ID your origin uses to identify the key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#access_key_id NetworkServicesEdgeCacheOrigin#access_key_id}
        :param origin_region: The name of the AWS region that your origin is in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#origin_region NetworkServicesEdgeCacheOrigin#origin_region}
        :param secret_access_key_version: The Secret Manager secret version of the secret access key used by your origin. This is the resource name of the secret version in the format 'projects/*/secrets/*/versions/*' where the '*' values are replaced by the project, secret, and version you require. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#secret_access_key_version NetworkServicesEdgeCacheOrigin#secret_access_key_version}
        '''
        value = NetworkServicesEdgeCacheOriginAwsV4Authentication(
            access_key_id=access_key_id,
            origin_region=origin_region,
            secret_access_key_version=secret_access_key_version,
        )

        return typing.cast(None, jsii.invoke(self, "putAwsV4Authentication", [value]))

    @jsii.member(jsii_name="putTimeout")
    def put_timeout(
        self,
        *,
        connect_timeout: typing.Optional[builtins.str] = None,
        max_attempts_timeout: typing.Optional[builtins.str] = None,
        read_timeout: typing.Optional[builtins.str] = None,
        response_timeout: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connect_timeout: The maximum duration to wait for a single origin connection to be established, including DNS lookup, TLS handshake and TCP/QUIC connection establishment. Defaults to 5 seconds. The timeout must be a value between 1s and 15s. The connectTimeout capped by the deadline set by the request's maxAttemptsTimeout. The last connection attempt may have a smaller connectTimeout in order to adhere to the overall maxAttemptsTimeout. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#connect_timeout NetworkServicesEdgeCacheOrigin#connect_timeout}
        :param max_attempts_timeout: The maximum time across all connection attempts to the origin, including failover origins, before returning an error to the client. A HTTP 504 will be returned if the timeout is reached before a response is returned. Defaults to 15 seconds. The timeout must be a value between 1s and 30s. If a failoverOrigin is specified, the maxAttemptsTimeout of the first configured origin sets the deadline for all connection attempts across all failoverOrigins. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#max_attempts_timeout NetworkServicesEdgeCacheOrigin#max_attempts_timeout}
        :param read_timeout: The maximum duration to wait between reads of a single HTTP connection/stream. Defaults to 15 seconds. The timeout must be a value between 1s and 30s. The readTimeout is capped by the responseTimeout. All reads of the HTTP connection/stream must be completed by the deadline set by the responseTimeout. If the response headers have already been written to the connection, the response will be truncated and logged. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#read_timeout NetworkServicesEdgeCacheOrigin#read_timeout}
        :param response_timeout: The maximum duration to wait for the last byte of a response to arrive when reading from the HTTP connection/stream. Defaults to 30 seconds. The timeout must be a value between 1s and 120s. The responseTimeout starts after the connection has been established. This also applies to HTTP Chunked Transfer Encoding responses, and/or when an open-ended Range request is made to the origin. Origins that take longer to write additional bytes to the response than the configured responseTimeout will result in an error being returned to the client. If the response headers have already been written to the connection, the response will be truncated and logged. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#response_timeout NetworkServicesEdgeCacheOrigin#response_timeout}
        '''
        value = NetworkServicesEdgeCacheOriginTimeout(
            connect_timeout=connect_timeout,
            max_attempts_timeout=max_attempts_timeout,
            read_timeout=read_timeout,
            response_timeout=response_timeout,
        )

        return typing.cast(None, jsii.invoke(self, "putTimeout", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#create NetworkServicesEdgeCacheOrigin#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#delete NetworkServicesEdgeCacheOrigin#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#update NetworkServicesEdgeCacheOrigin#update}.
        '''
        value = NetworkServicesEdgeCacheOriginTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAwsV4Authentication")
    def reset_aws_v4_authentication(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsV4Authentication", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetFailoverOrigin")
    def reset_failover_origin(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFailoverOrigin", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetMaxAttempts")
    def reset_max_attempts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxAttempts", []))

    @jsii.member(jsii_name="resetPort")
    def reset_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPort", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetProtocol")
    def reset_protocol(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProtocol", []))

    @jsii.member(jsii_name="resetRetryConditions")
    def reset_retry_conditions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetryConditions", []))

    @jsii.member(jsii_name="resetTimeout")
    def reset_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeout", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="awsV4Authentication")
    def aws_v4_authentication(
        self,
    ) -> "NetworkServicesEdgeCacheOriginAwsV4AuthenticationOutputReference":
        return typing.cast("NetworkServicesEdgeCacheOriginAwsV4AuthenticationOutputReference", jsii.get(self, "awsV4Authentication"))

    @builtins.property
    @jsii.member(jsii_name="timeout")
    def timeout(self) -> "NetworkServicesEdgeCacheOriginTimeoutOutputReference":
        return typing.cast("NetworkServicesEdgeCacheOriginTimeoutOutputReference", jsii.get(self, "timeout"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "NetworkServicesEdgeCacheOriginTimeoutsOutputReference":
        return typing.cast("NetworkServicesEdgeCacheOriginTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="awsV4AuthenticationInput")
    def aws_v4_authentication_input(
        self,
    ) -> typing.Optional["NetworkServicesEdgeCacheOriginAwsV4Authentication"]:
        return typing.cast(typing.Optional["NetworkServicesEdgeCacheOriginAwsV4Authentication"], jsii.get(self, "awsV4AuthenticationInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="failoverOriginInput")
    def failover_origin_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "failoverOriginInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="maxAttemptsInput")
    def max_attempts_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxAttemptsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="originAddressInput")
    def origin_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "originAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="retryConditionsInput")
    def retry_conditions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "retryConditionsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutInput")
    def timeout_input(self) -> typing.Optional["NetworkServicesEdgeCacheOriginTimeout"]:
        return typing.cast(typing.Optional["NetworkServicesEdgeCacheOriginTimeout"], jsii.get(self, "timeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["NetworkServicesEdgeCacheOriginTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["NetworkServicesEdgeCacheOriginTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16e06de5d4511b597377b3704165fe68f5061fa218cccc1fb02c78010c20bf3d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="failoverOrigin")
    def failover_origin(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "failoverOrigin"))

    @failover_origin.setter
    def failover_origin(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9bed1df947dd4291ac8d920c17d244da333aaa0d36e1cd8e7fe3d8f7e2c2e443)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "failoverOrigin", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57018818f7b0afffe196d835a8c51a510d6b467bbcacea6d00c751113523eabb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0283f28f9e9bc54b93c31c6b3ec148410010935ab9e8d028e90813f452c84eac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="maxAttempts")
    def max_attempts(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxAttempts"))

    @max_attempts.setter
    def max_attempts(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ad6d4a66a9d05fab3c121584245b9c9f96fa5994855897ff30712f56c79364c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxAttempts", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed9fada3a5871a695333a3deadef144f6f9fff05eadb9bd6de1f45bfea3c42f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="originAddress")
    def origin_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "originAddress"))

    @origin_address.setter
    def origin_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23fb04baf13d9e0a5b80c4e50b72113920ec1e68b117ebac295889879b98f31a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "originAddress", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c62b94ae140109467add0660268aebaa3f483b49534e665c01fa0682bac8272a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b1d456352eea565e3617e50b7f26ff00fc89c44a4967c2b1ca8771063e722bf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d22aadbd696b95d5f31e42cd11056a698b7c1a2be7aa5d482a4c3c389e5aa4ba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="retryConditions")
    def retry_conditions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "retryConditions"))

    @retry_conditions.setter
    def retry_conditions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__137537043a957722109451292d236f6c95d403fc6d78efe856a78937f37eb7f0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retryConditions", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google.networkServicesEdgeCacheOrigin.NetworkServicesEdgeCacheOriginAwsV4Authentication",
    jsii_struct_bases=[],
    name_mapping={
        "access_key_id": "accessKeyId",
        "origin_region": "originRegion",
        "secret_access_key_version": "secretAccessKeyVersion",
    },
)
class NetworkServicesEdgeCacheOriginAwsV4Authentication:
    def __init__(
        self,
        *,
        access_key_id: builtins.str,
        origin_region: builtins.str,
        secret_access_key_version: builtins.str,
    ) -> None:
        '''
        :param access_key_id: The access key ID your origin uses to identify the key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#access_key_id NetworkServicesEdgeCacheOrigin#access_key_id}
        :param origin_region: The name of the AWS region that your origin is in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#origin_region NetworkServicesEdgeCacheOrigin#origin_region}
        :param secret_access_key_version: The Secret Manager secret version of the secret access key used by your origin. This is the resource name of the secret version in the format 'projects/*/secrets/*/versions/*' where the '*' values are replaced by the project, secret, and version you require. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#secret_access_key_version NetworkServicesEdgeCacheOrigin#secret_access_key_version}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66e5dec465d5b7635b95bef1883417915cba4c6b65ca53f5dab11b22ce9f43dc)
            check_type(argname="argument access_key_id", value=access_key_id, expected_type=type_hints["access_key_id"])
            check_type(argname="argument origin_region", value=origin_region, expected_type=type_hints["origin_region"])
            check_type(argname="argument secret_access_key_version", value=secret_access_key_version, expected_type=type_hints["secret_access_key_version"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "access_key_id": access_key_id,
            "origin_region": origin_region,
            "secret_access_key_version": secret_access_key_version,
        }

    @builtins.property
    def access_key_id(self) -> builtins.str:
        '''The access key ID your origin uses to identify the key.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#access_key_id NetworkServicesEdgeCacheOrigin#access_key_id}
        '''
        result = self._values.get("access_key_id")
        assert result is not None, "Required property 'access_key_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def origin_region(self) -> builtins.str:
        '''The name of the AWS region that your origin is in.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#origin_region NetworkServicesEdgeCacheOrigin#origin_region}
        '''
        result = self._values.get("origin_region")
        assert result is not None, "Required property 'origin_region' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def secret_access_key_version(self) -> builtins.str:
        '''The Secret Manager secret version of the secret access key used by your origin.

        This is the resource name of the secret version in the format 'projects/*/secrets/*/versions/*' where the '*' values are replaced by the project, secret, and version you require.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#secret_access_key_version NetworkServicesEdgeCacheOrigin#secret_access_key_version}
        '''
        result = self._values.get("secret_access_key_version")
        assert result is not None, "Required property 'secret_access_key_version' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkServicesEdgeCacheOriginAwsV4Authentication(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class NetworkServicesEdgeCacheOriginAwsV4AuthenticationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.networkServicesEdgeCacheOrigin.NetworkServicesEdgeCacheOriginAwsV4AuthenticationOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7df46e97393357f5d549387189e1c1e2601aef30432c247cee4b4ef8afc51d5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="accessKeyIdInput")
    def access_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="originRegionInput")
    def origin_region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "originRegionInput"))

    @builtins.property
    @jsii.member(jsii_name="secretAccessKeyVersionInput")
    def secret_access_key_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretAccessKeyVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="accessKeyId")
    def access_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessKeyId"))

    @access_key_id.setter
    def access_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e13308eaf0c2d1b431afc017b8b117cefa10371ff0948b3aba53fa557c6249d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="originRegion")
    def origin_region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "originRegion"))

    @origin_region.setter
    def origin_region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0de7c6e7fa5cc74b17059bbb124a783198213a80fbb46b2342c097bb221cea16)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "originRegion", value)

    @builtins.property
    @jsii.member(jsii_name="secretAccessKeyVersion")
    def secret_access_key_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretAccessKeyVersion"))

    @secret_access_key_version.setter
    def secret_access_key_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dbc1b5db3b3356a02bc8a4105ebaf2857f11014ee5add98a59ecf142604dc1c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretAccessKeyVersion", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[NetworkServicesEdgeCacheOriginAwsV4Authentication]:
        return typing.cast(typing.Optional[NetworkServicesEdgeCacheOriginAwsV4Authentication], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[NetworkServicesEdgeCacheOriginAwsV4Authentication],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2bc3c1ceaa95f0faa9de888c1318870524750a47e45003ce11b381cbe049bc87)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google.networkServicesEdgeCacheOrigin.NetworkServicesEdgeCacheOriginConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "name": "name",
        "origin_address": "originAddress",
        "aws_v4_authentication": "awsV4Authentication",
        "description": "description",
        "failover_origin": "failoverOrigin",
        "id": "id",
        "labels": "labels",
        "max_attempts": "maxAttempts",
        "port": "port",
        "project": "project",
        "protocol": "protocol",
        "retry_conditions": "retryConditions",
        "timeout": "timeout",
        "timeouts": "timeouts",
    },
)
class NetworkServicesEdgeCacheOriginConfig(_cdktf_9a9027ec.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
        name: builtins.str,
        origin_address: builtins.str,
        aws_v4_authentication: typing.Optional[typing.Union[NetworkServicesEdgeCacheOriginAwsV4Authentication, typing.Dict[builtins.str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        failover_origin: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        max_attempts: typing.Optional[jsii.Number] = None,
        port: typing.Optional[jsii.Number] = None,
        project: typing.Optional[builtins.str] = None,
        protocol: typing.Optional[builtins.str] = None,
        retry_conditions: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeout: typing.Optional[typing.Union["NetworkServicesEdgeCacheOriginTimeout", typing.Dict[builtins.str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["NetworkServicesEdgeCacheOriginTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Name of the resource; provided by the client when the resource is created. The name must be 1-64 characters long, and match the regular expression [a-zA-Z][a-zA-Z0-9_-]* which means the first character must be a letter, and all following characters must be a dash, underscore, letter or digit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#name NetworkServicesEdgeCacheOrigin#name}
        :param origin_address: A fully qualified domain name (FQDN) or IP address reachable over the public Internet, or the address of a Google Cloud Storage bucket. This address will be used as the origin for cache requests - e.g. FQDN: media-backend.example.com, IPv4: 35.218.1.1, IPv6: 2607:f8b0:4012:809::200e, Cloud Storage: gs://bucketname When providing an FQDN (hostname), it must be publicly resolvable (e.g. via Google public DNS) and IP addresses must be publicly routable. It must not contain a protocol (e.g., https://) and it must not contain any slashes. If a Cloud Storage bucket is provided, it must be in the canonical "gs://bucketname" format. Other forms, such as "storage.googleapis.com", will be rejected. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#origin_address NetworkServicesEdgeCacheOrigin#origin_address}
        :param aws_v4_authentication: aws_v4_authentication block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#aws_v4_authentication NetworkServicesEdgeCacheOrigin#aws_v4_authentication}
        :param description: A human-readable description of the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#description NetworkServicesEdgeCacheOrigin#description}
        :param failover_origin: The Origin resource to try when the current origin cannot be reached. After maxAttempts is reached, the configured failoverOrigin will be used to fulfil the request. The value of timeout.maxAttemptsTimeout dictates the timeout across all origins. A reference to a Topic resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#failover_origin NetworkServicesEdgeCacheOrigin#failover_origin}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#id NetworkServicesEdgeCacheOrigin#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: Set of label tags associated with the EdgeCache resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#labels NetworkServicesEdgeCacheOrigin#labels}
        :param max_attempts: The maximum number of attempts to cache fill from this origin. Another attempt is made when a cache fill fails with one of the retryConditions. Once maxAttempts to this origin have failed the failoverOrigin will be used, if one is specified. That failoverOrigin may specify its own maxAttempts, retryConditions and failoverOrigin to control its own cache fill failures. The total number of allowed attempts to cache fill across this and failover origins is limited to four. The total time allowed for cache fill attempts across this and failover origins can be controlled with maxAttemptsTimeout. The last valid, non-retried response from all origins will be returned to the client. If no origin returns a valid response, an HTTP 502 will be returned to the client. Defaults to 1. Must be a value greater than 0 and less than 4. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#max_attempts NetworkServicesEdgeCacheOrigin#max_attempts}
        :param port: The port to connect to the origin on. Defaults to port 443 for HTTP2 and HTTPS protocols, and port 80 for HTTP. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#port NetworkServicesEdgeCacheOrigin#port}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#project NetworkServicesEdgeCacheOrigin#project}.
        :param protocol: The protocol to use to connect to the configured origin. Defaults to HTTP2, and it is strongly recommended that users use HTTP2 for both security & performance. When using HTTP2 or HTTPS as the protocol, a valid, publicly-signed, unexpired TLS (SSL) certificate must be presented by the origin server. Possible values: ["HTTP2", "HTTPS", "HTTP"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#protocol NetworkServicesEdgeCacheOrigin#protocol}
        :param retry_conditions: Specifies one or more retry conditions for the configured origin. If the failure mode during a connection attempt to the origin matches the configured retryCondition(s), the origin request will be retried up to maxAttempts times. The failoverOrigin, if configured, will then be used to satisfy the request. The default retryCondition is "CONNECT_FAILURE". retryConditions apply to this origin, and not subsequent failoverOrigin(s), which may specify their own retryConditions and maxAttempts. Valid values are: - CONNECT_FAILURE: Retry on failures connecting to origins, for example due to connection timeouts. - HTTP_5XX: Retry if the origin responds with any 5xx response code, or if the origin does not respond at all, example: disconnects, reset, read timeout, connection failure, and refused streams. - GATEWAY_ERROR: Similar to 5xx, but only applies to response codes 502, 503 or 504. - RETRIABLE_4XX: Retry for retriable 4xx response codes, which include HTTP 409 (Conflict) and HTTP 429 (Too Many Requests) - NOT_FOUND: Retry if the origin returns a HTTP 404 (Not Found). This can be useful when generating video content, and the segment is not available yet. - FORBIDDEN: Retry if the origin returns a HTTP 403 (Forbidden). Possible values: ["CONNECT_FAILURE", "HTTP_5XX", "GATEWAY_ERROR", "RETRIABLE_4XX", "NOT_FOUND", "FORBIDDEN"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#retry_conditions NetworkServicesEdgeCacheOrigin#retry_conditions}
        :param timeout: timeout block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#timeout NetworkServicesEdgeCacheOrigin#timeout}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#timeouts NetworkServicesEdgeCacheOrigin#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(aws_v4_authentication, dict):
            aws_v4_authentication = NetworkServicesEdgeCacheOriginAwsV4Authentication(**aws_v4_authentication)
        if isinstance(timeout, dict):
            timeout = NetworkServicesEdgeCacheOriginTimeout(**timeout)
        if isinstance(timeouts, dict):
            timeouts = NetworkServicesEdgeCacheOriginTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8dcb37a20d2a8ad5c4e32b9ddaab86c1be8a7fe650e95e7e38db09255ea5c30c)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument origin_address", value=origin_address, expected_type=type_hints["origin_address"])
            check_type(argname="argument aws_v4_authentication", value=aws_v4_authentication, expected_type=type_hints["aws_v4_authentication"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument failover_origin", value=failover_origin, expected_type=type_hints["failover_origin"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument max_attempts", value=max_attempts, expected_type=type_hints["max_attempts"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument retry_conditions", value=retry_conditions, expected_type=type_hints["retry_conditions"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "origin_address": origin_address,
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
        if aws_v4_authentication is not None:
            self._values["aws_v4_authentication"] = aws_v4_authentication
        if description is not None:
            self._values["description"] = description
        if failover_origin is not None:
            self._values["failover_origin"] = failover_origin
        if id is not None:
            self._values["id"] = id
        if labels is not None:
            self._values["labels"] = labels
        if max_attempts is not None:
            self._values["max_attempts"] = max_attempts
        if port is not None:
            self._values["port"] = port
        if project is not None:
            self._values["project"] = project
        if protocol is not None:
            self._values["protocol"] = protocol
        if retry_conditions is not None:
            self._values["retry_conditions"] = retry_conditions
        if timeout is not None:
            self._values["timeout"] = timeout
        if timeouts is not None:
            self._values["timeouts"] = timeouts

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, _cdktf_9a9027ec.WinrmProvisionerConnection]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, _cdktf_9a9027ec.WinrmProvisionerConnection]], result)

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(
        self,
    ) -> typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[_cdktf_9a9027ec.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[_cdktf_9a9027ec.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[typing.List[typing.Union[_cdktf_9a9027ec.FileProvisioner, _cdktf_9a9027ec.LocalExecProvisioner, _cdktf_9a9027ec.RemoteExecProvisioner]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provisioners")
        return typing.cast(typing.Optional[typing.List[typing.Union[_cdktf_9a9027ec.FileProvisioner, _cdktf_9a9027ec.LocalExecProvisioner, _cdktf_9a9027ec.RemoteExecProvisioner]]], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the resource;

        provided by the client when the resource is created.
        The name must be 1-64 characters long, and match the regular expression [a-zA-Z][a-zA-Z0-9_-]* which means the first character must be a letter,
        and all following characters must be a dash, underscore, letter or digit.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#name NetworkServicesEdgeCacheOrigin#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def origin_address(self) -> builtins.str:
        '''A fully qualified domain name (FQDN) or IP address reachable over the public Internet, or the address of a Google Cloud Storage bucket.

        This address will be used as the origin for cache requests - e.g. FQDN: media-backend.example.com, IPv4: 35.218.1.1, IPv6: 2607:f8b0:4012:809::200e, Cloud Storage: gs://bucketname

        When providing an FQDN (hostname), it must be publicly resolvable (e.g. via Google public DNS) and IP addresses must be publicly routable.  It must not contain a protocol (e.g., https://) and it must not contain any slashes.
        If a Cloud Storage bucket is provided, it must be in the canonical "gs://bucketname" format. Other forms, such as "storage.googleapis.com", will be rejected.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#origin_address NetworkServicesEdgeCacheOrigin#origin_address}
        '''
        result = self._values.get("origin_address")
        assert result is not None, "Required property 'origin_address' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def aws_v4_authentication(
        self,
    ) -> typing.Optional[NetworkServicesEdgeCacheOriginAwsV4Authentication]:
        '''aws_v4_authentication block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#aws_v4_authentication NetworkServicesEdgeCacheOrigin#aws_v4_authentication}
        '''
        result = self._values.get("aws_v4_authentication")
        return typing.cast(typing.Optional[NetworkServicesEdgeCacheOriginAwsV4Authentication], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A human-readable description of the resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#description NetworkServicesEdgeCacheOrigin#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def failover_origin(self) -> typing.Optional[builtins.str]:
        '''The Origin resource to try when the current origin cannot be reached.

        After maxAttempts is reached, the configured failoverOrigin will be used to fulfil the request.

        The value of timeout.maxAttemptsTimeout dictates the timeout across all origins.
        A reference to a Topic resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#failover_origin NetworkServicesEdgeCacheOrigin#failover_origin}
        '''
        result = self._values.get("failover_origin")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#id NetworkServicesEdgeCacheOrigin#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Set of label tags associated with the EdgeCache resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#labels NetworkServicesEdgeCacheOrigin#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def max_attempts(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of attempts to cache fill from this origin.

        Another attempt is made when a cache fill fails with one of the retryConditions.

        Once maxAttempts to this origin have failed the failoverOrigin will be used, if one is specified. That failoverOrigin may specify its own maxAttempts,
        retryConditions and failoverOrigin to control its own cache fill failures.

        The total number of allowed attempts to cache fill across this and failover origins is limited to four.
        The total time allowed for cache fill attempts across this and failover origins can be controlled with maxAttemptsTimeout.

        The last valid, non-retried response from all origins will be returned to the client.
        If no origin returns a valid response, an HTTP 502 will be returned to the client.

        Defaults to 1. Must be a value greater than 0 and less than 4.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#max_attempts NetworkServicesEdgeCacheOrigin#max_attempts}
        '''
        result = self._values.get("max_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''The port to connect to the origin on.

        Defaults to port 443 for HTTP2 and HTTPS protocols, and port 80 for HTTP.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#port NetworkServicesEdgeCacheOrigin#port}
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#project NetworkServicesEdgeCacheOrigin#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def protocol(self) -> typing.Optional[builtins.str]:
        '''The protocol to use to connect to the configured origin.

        Defaults to HTTP2, and it is strongly recommended that users use HTTP2 for both security & performance.

        When using HTTP2 or HTTPS as the protocol, a valid, publicly-signed, unexpired TLS (SSL) certificate must be presented by the origin server. Possible values: ["HTTP2", "HTTPS", "HTTP"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#protocol NetworkServicesEdgeCacheOrigin#protocol}
        '''
        result = self._values.get("protocol")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def retry_conditions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies one or more retry conditions for the configured origin.

        If the failure mode during a connection attempt to the origin matches the configured retryCondition(s),
        the origin request will be retried up to maxAttempts times. The failoverOrigin, if configured, will then be used to satisfy the request.

        The default retryCondition is "CONNECT_FAILURE".

        retryConditions apply to this origin, and not subsequent failoverOrigin(s),
        which may specify their own retryConditions and maxAttempts.

        Valid values are:

        - CONNECT_FAILURE: Retry on failures connecting to origins, for example due to connection timeouts.
        - HTTP_5XX: Retry if the origin responds with any 5xx response code, or if the origin does not respond at all, example: disconnects, reset, read timeout, connection failure, and refused streams.
        - GATEWAY_ERROR: Similar to 5xx, but only applies to response codes 502, 503 or 504.
        - RETRIABLE_4XX: Retry for retriable 4xx response codes, which include HTTP 409 (Conflict) and HTTP 429 (Too Many Requests)
        - NOT_FOUND: Retry if the origin returns a HTTP 404 (Not Found). This can be useful when generating video content, and the segment is not available yet.
        - FORBIDDEN: Retry if the origin returns a HTTP 403 (Forbidden). Possible values: ["CONNECT_FAILURE", "HTTP_5XX", "GATEWAY_ERROR", "RETRIABLE_4XX", "NOT_FOUND", "FORBIDDEN"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#retry_conditions NetworkServicesEdgeCacheOrigin#retry_conditions}
        '''
        result = self._values.get("retry_conditions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def timeout(self) -> typing.Optional["NetworkServicesEdgeCacheOriginTimeout"]:
        '''timeout block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#timeout NetworkServicesEdgeCacheOrigin#timeout}
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional["NetworkServicesEdgeCacheOriginTimeout"], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["NetworkServicesEdgeCacheOriginTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#timeouts NetworkServicesEdgeCacheOrigin#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["NetworkServicesEdgeCacheOriginTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkServicesEdgeCacheOriginConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google.networkServicesEdgeCacheOrigin.NetworkServicesEdgeCacheOriginTimeout",
    jsii_struct_bases=[],
    name_mapping={
        "connect_timeout": "connectTimeout",
        "max_attempts_timeout": "maxAttemptsTimeout",
        "read_timeout": "readTimeout",
        "response_timeout": "responseTimeout",
    },
)
class NetworkServicesEdgeCacheOriginTimeout:
    def __init__(
        self,
        *,
        connect_timeout: typing.Optional[builtins.str] = None,
        max_attempts_timeout: typing.Optional[builtins.str] = None,
        read_timeout: typing.Optional[builtins.str] = None,
        response_timeout: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connect_timeout: The maximum duration to wait for a single origin connection to be established, including DNS lookup, TLS handshake and TCP/QUIC connection establishment. Defaults to 5 seconds. The timeout must be a value between 1s and 15s. The connectTimeout capped by the deadline set by the request's maxAttemptsTimeout. The last connection attempt may have a smaller connectTimeout in order to adhere to the overall maxAttemptsTimeout. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#connect_timeout NetworkServicesEdgeCacheOrigin#connect_timeout}
        :param max_attempts_timeout: The maximum time across all connection attempts to the origin, including failover origins, before returning an error to the client. A HTTP 504 will be returned if the timeout is reached before a response is returned. Defaults to 15 seconds. The timeout must be a value between 1s and 30s. If a failoverOrigin is specified, the maxAttemptsTimeout of the first configured origin sets the deadline for all connection attempts across all failoverOrigins. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#max_attempts_timeout NetworkServicesEdgeCacheOrigin#max_attempts_timeout}
        :param read_timeout: The maximum duration to wait between reads of a single HTTP connection/stream. Defaults to 15 seconds. The timeout must be a value between 1s and 30s. The readTimeout is capped by the responseTimeout. All reads of the HTTP connection/stream must be completed by the deadline set by the responseTimeout. If the response headers have already been written to the connection, the response will be truncated and logged. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#read_timeout NetworkServicesEdgeCacheOrigin#read_timeout}
        :param response_timeout: The maximum duration to wait for the last byte of a response to arrive when reading from the HTTP connection/stream. Defaults to 30 seconds. The timeout must be a value between 1s and 120s. The responseTimeout starts after the connection has been established. This also applies to HTTP Chunked Transfer Encoding responses, and/or when an open-ended Range request is made to the origin. Origins that take longer to write additional bytes to the response than the configured responseTimeout will result in an error being returned to the client. If the response headers have already been written to the connection, the response will be truncated and logged. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#response_timeout NetworkServicesEdgeCacheOrigin#response_timeout}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87e8085f0f540c26a6d6478e628a51dd6039cd1193b8968b27bf1ee6546a2416)
            check_type(argname="argument connect_timeout", value=connect_timeout, expected_type=type_hints["connect_timeout"])
            check_type(argname="argument max_attempts_timeout", value=max_attempts_timeout, expected_type=type_hints["max_attempts_timeout"])
            check_type(argname="argument read_timeout", value=read_timeout, expected_type=type_hints["read_timeout"])
            check_type(argname="argument response_timeout", value=response_timeout, expected_type=type_hints["response_timeout"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if connect_timeout is not None:
            self._values["connect_timeout"] = connect_timeout
        if max_attempts_timeout is not None:
            self._values["max_attempts_timeout"] = max_attempts_timeout
        if read_timeout is not None:
            self._values["read_timeout"] = read_timeout
        if response_timeout is not None:
            self._values["response_timeout"] = response_timeout

    @builtins.property
    def connect_timeout(self) -> typing.Optional[builtins.str]:
        '''The maximum duration to wait for a single origin connection to be established, including DNS lookup, TLS handshake and TCP/QUIC connection establishment.

        Defaults to 5 seconds. The timeout must be a value between 1s and 15s.

        The connectTimeout capped by the deadline set by the request's maxAttemptsTimeout.  The last connection attempt may have a smaller connectTimeout in order to adhere to the overall maxAttemptsTimeout.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#connect_timeout NetworkServicesEdgeCacheOrigin#connect_timeout}
        '''
        result = self._values.get("connect_timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_attempts_timeout(self) -> typing.Optional[builtins.str]:
        '''The maximum time across all connection attempts to the origin, including failover origins, before returning an error to the client.

        A HTTP 504 will be returned if the timeout is reached before a response is returned.

        Defaults to 15 seconds. The timeout must be a value between 1s and 30s.

        If a failoverOrigin is specified, the maxAttemptsTimeout of the first configured origin sets the deadline for all connection attempts across all failoverOrigins.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#max_attempts_timeout NetworkServicesEdgeCacheOrigin#max_attempts_timeout}
        '''
        result = self._values.get("max_attempts_timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read_timeout(self) -> typing.Optional[builtins.str]:
        '''The maximum duration to wait between reads of a single HTTP connection/stream.

        Defaults to 15 seconds.  The timeout must be a value between 1s and 30s.

        The readTimeout is capped by the responseTimeout.  All reads of the HTTP connection/stream must be completed by the deadline set by the responseTimeout.

        If the response headers have already been written to the connection, the response will be truncated and logged.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#read_timeout NetworkServicesEdgeCacheOrigin#read_timeout}
        '''
        result = self._values.get("read_timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def response_timeout(self) -> typing.Optional[builtins.str]:
        '''The maximum duration to wait for the last byte of a response to arrive when reading from the HTTP connection/stream.

        Defaults to 30 seconds. The timeout must be a value between 1s and 120s.

        The responseTimeout starts after the connection has been established.

        This also applies to HTTP Chunked Transfer Encoding responses, and/or when an open-ended Range request is made to the origin. Origins that take longer to write additional bytes to the response than the configured responseTimeout will result in an error being returned to the client.

        If the response headers have already been written to the connection, the response will be truncated and logged.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#response_timeout NetworkServicesEdgeCacheOrigin#response_timeout}
        '''
        result = self._values.get("response_timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkServicesEdgeCacheOriginTimeout(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class NetworkServicesEdgeCacheOriginTimeoutOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.networkServicesEdgeCacheOrigin.NetworkServicesEdgeCacheOriginTimeoutOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a93469c1f5102e842415c30010ae3830e3e0232f2e64bdc6a718418f645ba951)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetConnectTimeout")
    def reset_connect_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectTimeout", []))

    @jsii.member(jsii_name="resetMaxAttemptsTimeout")
    def reset_max_attempts_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxAttemptsTimeout", []))

    @jsii.member(jsii_name="resetReadTimeout")
    def reset_read_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadTimeout", []))

    @jsii.member(jsii_name="resetResponseTimeout")
    def reset_response_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResponseTimeout", []))

    @builtins.property
    @jsii.member(jsii_name="connectTimeoutInput")
    def connect_timeout_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="maxAttemptsTimeoutInput")
    def max_attempts_timeout_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxAttemptsTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="readTimeoutInput")
    def read_timeout_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "readTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="responseTimeoutInput")
    def response_timeout_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "responseTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="connectTimeout")
    def connect_timeout(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectTimeout"))

    @connect_timeout.setter
    def connect_timeout(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42f9b1ca47700c1923a17cea1159b5a774b83a307fe5cfb52be6059d7b6672a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="maxAttemptsTimeout")
    def max_attempts_timeout(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maxAttemptsTimeout"))

    @max_attempts_timeout.setter
    def max_attempts_timeout(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d080edf18cfb051fb64ef435466dc4208303dd701f22675116db8dda763db54f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxAttemptsTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="readTimeout")
    def read_timeout(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "readTimeout"))

    @read_timeout.setter
    def read_timeout(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e81b4afb74cb177142b84e004ecad625d1a8820162c5ac9a3a227fd905fe5148)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="responseTimeout")
    def response_timeout(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "responseTimeout"))

    @response_timeout.setter
    def response_timeout(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc54da3751259c20044434da499f369fc836c5e1e062382372ae9ff2dd364903)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "responseTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[NetworkServicesEdgeCacheOriginTimeout]:
        return typing.cast(typing.Optional[NetworkServicesEdgeCacheOriginTimeout], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[NetworkServicesEdgeCacheOriginTimeout],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__accdefea2feb68dfd48bf58c7de1ff4ab766047bad40e7dc6f1ddb9c52d31839)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google.networkServicesEdgeCacheOrigin.NetworkServicesEdgeCacheOriginTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class NetworkServicesEdgeCacheOriginTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#create NetworkServicesEdgeCacheOrigin#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#delete NetworkServicesEdgeCacheOrigin#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#update NetworkServicesEdgeCacheOrigin#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48290cbe5d8d7bb5e130b0ee838e2e5e5f2bbd0e3c5fcc00c118deaa4c128bef)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#create NetworkServicesEdgeCacheOrigin#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#delete NetworkServicesEdgeCacheOrigin#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google/r/network_services_edge_cache_origin#update NetworkServicesEdgeCacheOrigin#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkServicesEdgeCacheOriginTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class NetworkServicesEdgeCacheOriginTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google.networkServicesEdgeCacheOrigin.NetworkServicesEdgeCacheOriginTimeoutsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68d030eb456d40ae00e9264aa84cf010c0702327d48eeb3983fc76f3bf986d18)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @jsii.member(jsii_name="resetUpdate")
    def reset_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="updateInput")
    def update_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "updateInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91d06d40a306e38f336fa5e90378ccab47a1187e9be4c3f1f676c16d0be2a94e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f9e7912fe33ecb192bda4b6beebcd3c045a5f6e320d01e68d1f0686764c2b98)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0256e91321e29295953d4f1d4448bc08ecd286933fbdf4b825dd93799c5d973e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[NetworkServicesEdgeCacheOriginTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[NetworkServicesEdgeCacheOriginTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[NetworkServicesEdgeCacheOriginTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be178a4410c910600d40f1129dfc841e6e28ef1bdeac5328b1f347e0d0ea57c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "NetworkServicesEdgeCacheOrigin",
    "NetworkServicesEdgeCacheOriginAwsV4Authentication",
    "NetworkServicesEdgeCacheOriginAwsV4AuthenticationOutputReference",
    "NetworkServicesEdgeCacheOriginConfig",
    "NetworkServicesEdgeCacheOriginTimeout",
    "NetworkServicesEdgeCacheOriginTimeoutOutputReference",
    "NetworkServicesEdgeCacheOriginTimeouts",
    "NetworkServicesEdgeCacheOriginTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__c1c21df93d1996318f9c957070740c8d72e22c37e5bff3072eb29fb680a72cb2(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    origin_address: builtins.str,
    aws_v4_authentication: typing.Optional[typing.Union[NetworkServicesEdgeCacheOriginAwsV4Authentication, typing.Dict[builtins.str, typing.Any]]] = None,
    description: typing.Optional[builtins.str] = None,
    failover_origin: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    max_attempts: typing.Optional[jsii.Number] = None,
    port: typing.Optional[jsii.Number] = None,
    project: typing.Optional[builtins.str] = None,
    protocol: typing.Optional[builtins.str] = None,
    retry_conditions: typing.Optional[typing.Sequence[builtins.str]] = None,
    timeout: typing.Optional[typing.Union[NetworkServicesEdgeCacheOriginTimeout, typing.Dict[builtins.str, typing.Any]]] = None,
    timeouts: typing.Optional[typing.Union[NetworkServicesEdgeCacheOriginTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16e06de5d4511b597377b3704165fe68f5061fa218cccc1fb02c78010c20bf3d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9bed1df947dd4291ac8d920c17d244da333aaa0d36e1cd8e7fe3d8f7e2c2e443(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57018818f7b0afffe196d835a8c51a510d6b467bbcacea6d00c751113523eabb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0283f28f9e9bc54b93c31c6b3ec148410010935ab9e8d028e90813f452c84eac(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ad6d4a66a9d05fab3c121584245b9c9f96fa5994855897ff30712f56c79364c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed9fada3a5871a695333a3deadef144f6f9fff05eadb9bd6de1f45bfea3c42f1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23fb04baf13d9e0a5b80c4e50b72113920ec1e68b117ebac295889879b98f31a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c62b94ae140109467add0660268aebaa3f483b49534e665c01fa0682bac8272a(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b1d456352eea565e3617e50b7f26ff00fc89c44a4967c2b1ca8771063e722bf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d22aadbd696b95d5f31e42cd11056a698b7c1a2be7aa5d482a4c3c389e5aa4ba(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__137537043a957722109451292d236f6c95d403fc6d78efe856a78937f37eb7f0(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66e5dec465d5b7635b95bef1883417915cba4c6b65ca53f5dab11b22ce9f43dc(
    *,
    access_key_id: builtins.str,
    origin_region: builtins.str,
    secret_access_key_version: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7df46e97393357f5d549387189e1c1e2601aef30432c247cee4b4ef8afc51d5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e13308eaf0c2d1b431afc017b8b117cefa10371ff0948b3aba53fa557c6249d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0de7c6e7fa5cc74b17059bbb124a783198213a80fbb46b2342c097bb221cea16(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dbc1b5db3b3356a02bc8a4105ebaf2857f11014ee5add98a59ecf142604dc1c2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bc3c1ceaa95f0faa9de888c1318870524750a47e45003ce11b381cbe049bc87(
    value: typing.Optional[NetworkServicesEdgeCacheOriginAwsV4Authentication],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8dcb37a20d2a8ad5c4e32b9ddaab86c1be8a7fe650e95e7e38db09255ea5c30c(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    origin_address: builtins.str,
    aws_v4_authentication: typing.Optional[typing.Union[NetworkServicesEdgeCacheOriginAwsV4Authentication, typing.Dict[builtins.str, typing.Any]]] = None,
    description: typing.Optional[builtins.str] = None,
    failover_origin: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    max_attempts: typing.Optional[jsii.Number] = None,
    port: typing.Optional[jsii.Number] = None,
    project: typing.Optional[builtins.str] = None,
    protocol: typing.Optional[builtins.str] = None,
    retry_conditions: typing.Optional[typing.Sequence[builtins.str]] = None,
    timeout: typing.Optional[typing.Union[NetworkServicesEdgeCacheOriginTimeout, typing.Dict[builtins.str, typing.Any]]] = None,
    timeouts: typing.Optional[typing.Union[NetworkServicesEdgeCacheOriginTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87e8085f0f540c26a6d6478e628a51dd6039cd1193b8968b27bf1ee6546a2416(
    *,
    connect_timeout: typing.Optional[builtins.str] = None,
    max_attempts_timeout: typing.Optional[builtins.str] = None,
    read_timeout: typing.Optional[builtins.str] = None,
    response_timeout: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a93469c1f5102e842415c30010ae3830e3e0232f2e64bdc6a718418f645ba951(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42f9b1ca47700c1923a17cea1159b5a774b83a307fe5cfb52be6059d7b6672a8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d080edf18cfb051fb64ef435466dc4208303dd701f22675116db8dda763db54f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e81b4afb74cb177142b84e004ecad625d1a8820162c5ac9a3a227fd905fe5148(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc54da3751259c20044434da499f369fc836c5e1e062382372ae9ff2dd364903(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__accdefea2feb68dfd48bf58c7de1ff4ab766047bad40e7dc6f1ddb9c52d31839(
    value: typing.Optional[NetworkServicesEdgeCacheOriginTimeout],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48290cbe5d8d7bb5e130b0ee838e2e5e5f2bbd0e3c5fcc00c118deaa4c128bef(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68d030eb456d40ae00e9264aa84cf010c0702327d48eeb3983fc76f3bf986d18(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91d06d40a306e38f336fa5e90378ccab47a1187e9be4c3f1f676c16d0be2a94e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f9e7912fe33ecb192bda4b6beebcd3c045a5f6e320d01e68d1f0686764c2b98(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0256e91321e29295953d4f1d4448bc08ecd286933fbdf4b825dd93799c5d973e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be178a4410c910600d40f1129dfc841e6e28ef1bdeac5328b1f347e0d0ea57c9(
    value: typing.Optional[typing.Union[NetworkServicesEdgeCacheOriginTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
