'''
# `aws_codebuild_project`

Refer to the Terraform Registory for docs: [`aws_codebuild_project`](https://www.terraform.io/docs/providers/aws/r/codebuild_project).
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


class CodebuildProject(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.codebuildProject.CodebuildProject",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project aws_codebuild_project}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        artifacts: typing.Union["CodebuildProjectArtifacts", typing.Dict[str, typing.Any]],
        environment: typing.Union["CodebuildProjectEnvironment", typing.Dict[str, typing.Any]],
        name: builtins.str,
        service_role: builtins.str,
        source: typing.Union["CodebuildProjectSource", typing.Dict[str, typing.Any]],
        badge_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        build_batch_config: typing.Optional[typing.Union["CodebuildProjectBuildBatchConfig", typing.Dict[str, typing.Any]]] = None,
        build_timeout: typing.Optional[jsii.Number] = None,
        cache: typing.Optional[typing.Union["CodebuildProjectCache", typing.Dict[str, typing.Any]]] = None,
        concurrent_build_limit: typing.Optional[jsii.Number] = None,
        description: typing.Optional[builtins.str] = None,
        encryption_key: typing.Optional[builtins.str] = None,
        file_system_locations: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CodebuildProjectFileSystemLocations", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        logs_config: typing.Optional[typing.Union["CodebuildProjectLogsConfig", typing.Dict[str, typing.Any]]] = None,
        project_visibility: typing.Optional[builtins.str] = None,
        queued_timeout: typing.Optional[jsii.Number] = None,
        resource_access_role: typing.Optional[builtins.str] = None,
        secondary_artifacts: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CodebuildProjectSecondaryArtifacts", typing.Dict[str, typing.Any]]]]] = None,
        secondary_sources: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CodebuildProjectSecondarySources", typing.Dict[str, typing.Any]]]]] = None,
        secondary_source_version: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CodebuildProjectSecondarySourceVersion", typing.Dict[str, typing.Any]]]]] = None,
        source_version: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        vpc_config: typing.Optional[typing.Union["CodebuildProjectVpcConfig", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project aws_codebuild_project} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param artifacts: artifacts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#artifacts CodebuildProject#artifacts}
        :param environment: environment block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#environment CodebuildProject#environment}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#name CodebuildProject#name}.
        :param service_role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#service_role CodebuildProject#service_role}.
        :param source: source block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#source CodebuildProject#source}
        :param badge_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#badge_enabled CodebuildProject#badge_enabled}.
        :param build_batch_config: build_batch_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#build_batch_config CodebuildProject#build_batch_config}
        :param build_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#build_timeout CodebuildProject#build_timeout}.
        :param cache: cache block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#cache CodebuildProject#cache}
        :param concurrent_build_limit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#concurrent_build_limit CodebuildProject#concurrent_build_limit}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#description CodebuildProject#description}.
        :param encryption_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#encryption_key CodebuildProject#encryption_key}.
        :param file_system_locations: file_system_locations block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#file_system_locations CodebuildProject#file_system_locations}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#id CodebuildProject#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param logs_config: logs_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#logs_config CodebuildProject#logs_config}
        :param project_visibility: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#project_visibility CodebuildProject#project_visibility}.
        :param queued_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#queued_timeout CodebuildProject#queued_timeout}.
        :param resource_access_role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#resource_access_role CodebuildProject#resource_access_role}.
        :param secondary_artifacts: secondary_artifacts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#secondary_artifacts CodebuildProject#secondary_artifacts}
        :param secondary_sources: secondary_sources block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#secondary_sources CodebuildProject#secondary_sources}
        :param secondary_source_version: secondary_source_version block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#secondary_source_version CodebuildProject#secondary_source_version}
        :param source_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#source_version CodebuildProject#source_version}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#tags CodebuildProject#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#tags_all CodebuildProject#tags_all}.
        :param vpc_config: vpc_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#vpc_config CodebuildProject#vpc_config}
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
                artifacts: typing.Union[CodebuildProjectArtifacts, typing.Dict[str, typing.Any]],
                environment: typing.Union[CodebuildProjectEnvironment, typing.Dict[str, typing.Any]],
                name: builtins.str,
                service_role: builtins.str,
                source: typing.Union[CodebuildProjectSource, typing.Dict[str, typing.Any]],
                badge_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                build_batch_config: typing.Optional[typing.Union[CodebuildProjectBuildBatchConfig, typing.Dict[str, typing.Any]]] = None,
                build_timeout: typing.Optional[jsii.Number] = None,
                cache: typing.Optional[typing.Union[CodebuildProjectCache, typing.Dict[str, typing.Any]]] = None,
                concurrent_build_limit: typing.Optional[jsii.Number] = None,
                description: typing.Optional[builtins.str] = None,
                encryption_key: typing.Optional[builtins.str] = None,
                file_system_locations: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CodebuildProjectFileSystemLocations, typing.Dict[str, typing.Any]]]]] = None,
                id: typing.Optional[builtins.str] = None,
                logs_config: typing.Optional[typing.Union[CodebuildProjectLogsConfig, typing.Dict[str, typing.Any]]] = None,
                project_visibility: typing.Optional[builtins.str] = None,
                queued_timeout: typing.Optional[jsii.Number] = None,
                resource_access_role: typing.Optional[builtins.str] = None,
                secondary_artifacts: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CodebuildProjectSecondaryArtifacts, typing.Dict[str, typing.Any]]]]] = None,
                secondary_sources: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CodebuildProjectSecondarySources, typing.Dict[str, typing.Any]]]]] = None,
                secondary_source_version: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CodebuildProjectSecondarySourceVersion, typing.Dict[str, typing.Any]]]]] = None,
                source_version: typing.Optional[builtins.str] = None,
                tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                vpc_config: typing.Optional[typing.Union[CodebuildProjectVpcConfig, typing.Dict[str, typing.Any]]] = None,
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
        config = CodebuildProjectConfig(
            artifacts=artifacts,
            environment=environment,
            name=name,
            service_role=service_role,
            source=source,
            badge_enabled=badge_enabled,
            build_batch_config=build_batch_config,
            build_timeout=build_timeout,
            cache=cache,
            concurrent_build_limit=concurrent_build_limit,
            description=description,
            encryption_key=encryption_key,
            file_system_locations=file_system_locations,
            id=id,
            logs_config=logs_config,
            project_visibility=project_visibility,
            queued_timeout=queued_timeout,
            resource_access_role=resource_access_role,
            secondary_artifacts=secondary_artifacts,
            secondary_sources=secondary_sources,
            secondary_source_version=secondary_source_version,
            source_version=source_version,
            tags=tags,
            tags_all=tags_all,
            vpc_config=vpc_config,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putArtifacts")
    def put_artifacts(
        self,
        *,
        type: builtins.str,
        artifact_identifier: typing.Optional[builtins.str] = None,
        bucket_owner_access: typing.Optional[builtins.str] = None,
        encryption_disabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        location: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        namespace_type: typing.Optional[builtins.str] = None,
        override_artifact_name: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        packaging: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#type CodebuildProject#type}.
        :param artifact_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#artifact_identifier CodebuildProject#artifact_identifier}.
        :param bucket_owner_access: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#bucket_owner_access CodebuildProject#bucket_owner_access}.
        :param encryption_disabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#encryption_disabled CodebuildProject#encryption_disabled}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#location CodebuildProject#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#name CodebuildProject#name}.
        :param namespace_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#namespace_type CodebuildProject#namespace_type}.
        :param override_artifact_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#override_artifact_name CodebuildProject#override_artifact_name}.
        :param packaging: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#packaging CodebuildProject#packaging}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#path CodebuildProject#path}.
        '''
        value = CodebuildProjectArtifacts(
            type=type,
            artifact_identifier=artifact_identifier,
            bucket_owner_access=bucket_owner_access,
            encryption_disabled=encryption_disabled,
            location=location,
            name=name,
            namespace_type=namespace_type,
            override_artifact_name=override_artifact_name,
            packaging=packaging,
            path=path,
        )

        return typing.cast(None, jsii.invoke(self, "putArtifacts", [value]))

    @jsii.member(jsii_name="putBuildBatchConfig")
    def put_build_batch_config(
        self,
        *,
        service_role: builtins.str,
        combine_artifacts: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        restrictions: typing.Optional[typing.Union["CodebuildProjectBuildBatchConfigRestrictions", typing.Dict[str, typing.Any]]] = None,
        timeout_in_mins: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param service_role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#service_role CodebuildProject#service_role}.
        :param combine_artifacts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#combine_artifacts CodebuildProject#combine_artifacts}.
        :param restrictions: restrictions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#restrictions CodebuildProject#restrictions}
        :param timeout_in_mins: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#timeout_in_mins CodebuildProject#timeout_in_mins}.
        '''
        value = CodebuildProjectBuildBatchConfig(
            service_role=service_role,
            combine_artifacts=combine_artifacts,
            restrictions=restrictions,
            timeout_in_mins=timeout_in_mins,
        )

        return typing.cast(None, jsii.invoke(self, "putBuildBatchConfig", [value]))

    @jsii.member(jsii_name="putCache")
    def put_cache(
        self,
        *,
        location: typing.Optional[builtins.str] = None,
        modes: typing.Optional[typing.Sequence[builtins.str]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#location CodebuildProject#location}.
        :param modes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#modes CodebuildProject#modes}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#type CodebuildProject#type}.
        '''
        value = CodebuildProjectCache(location=location, modes=modes, type=type)

        return typing.cast(None, jsii.invoke(self, "putCache", [value]))

    @jsii.member(jsii_name="putEnvironment")
    def put_environment(
        self,
        *,
        compute_type: builtins.str,
        image: builtins.str,
        type: builtins.str,
        certificate: typing.Optional[builtins.str] = None,
        environment_variable: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CodebuildProjectEnvironmentEnvironmentVariable", typing.Dict[str, typing.Any]]]]] = None,
        image_pull_credentials_type: typing.Optional[builtins.str] = None,
        privileged_mode: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        registry_credential: typing.Optional[typing.Union["CodebuildProjectEnvironmentRegistryCredential", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param compute_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#compute_type CodebuildProject#compute_type}.
        :param image: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#image CodebuildProject#image}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#type CodebuildProject#type}.
        :param certificate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#certificate CodebuildProject#certificate}.
        :param environment_variable: environment_variable block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#environment_variable CodebuildProject#environment_variable}
        :param image_pull_credentials_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#image_pull_credentials_type CodebuildProject#image_pull_credentials_type}.
        :param privileged_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#privileged_mode CodebuildProject#privileged_mode}.
        :param registry_credential: registry_credential block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#registry_credential CodebuildProject#registry_credential}
        '''
        value = CodebuildProjectEnvironment(
            compute_type=compute_type,
            image=image,
            type=type,
            certificate=certificate,
            environment_variable=environment_variable,
            image_pull_credentials_type=image_pull_credentials_type,
            privileged_mode=privileged_mode,
            registry_credential=registry_credential,
        )

        return typing.cast(None, jsii.invoke(self, "putEnvironment", [value]))

    @jsii.member(jsii_name="putFileSystemLocations")
    def put_file_system_locations(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CodebuildProjectFileSystemLocations", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CodebuildProjectFileSystemLocations, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putFileSystemLocations", [value]))

    @jsii.member(jsii_name="putLogsConfig")
    def put_logs_config(
        self,
        *,
        cloudwatch_logs: typing.Optional[typing.Union["CodebuildProjectLogsConfigCloudwatchLogs", typing.Dict[str, typing.Any]]] = None,
        s3_logs: typing.Optional[typing.Union["CodebuildProjectLogsConfigS3Logs", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param cloudwatch_logs: cloudwatch_logs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#cloudwatch_logs CodebuildProject#cloudwatch_logs}
        :param s3_logs: s3_logs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#s3_logs CodebuildProject#s3_logs}
        '''
        value = CodebuildProjectLogsConfig(
            cloudwatch_logs=cloudwatch_logs, s3_logs=s3_logs
        )

        return typing.cast(None, jsii.invoke(self, "putLogsConfig", [value]))

    @jsii.member(jsii_name="putSecondaryArtifacts")
    def put_secondary_artifacts(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CodebuildProjectSecondaryArtifacts", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CodebuildProjectSecondaryArtifacts, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSecondaryArtifacts", [value]))

    @jsii.member(jsii_name="putSecondarySources")
    def put_secondary_sources(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CodebuildProjectSecondarySources", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CodebuildProjectSecondarySources, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSecondarySources", [value]))

    @jsii.member(jsii_name="putSecondarySourceVersion")
    def put_secondary_source_version(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CodebuildProjectSecondarySourceVersion", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CodebuildProjectSecondarySourceVersion, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSecondarySourceVersion", [value]))

    @jsii.member(jsii_name="putSource")
    def put_source(
        self,
        *,
        type: builtins.str,
        auth: typing.Optional[typing.Union["CodebuildProjectSourceAuth", typing.Dict[str, typing.Any]]] = None,
        buildspec: typing.Optional[builtins.str] = None,
        build_status_config: typing.Optional[typing.Union["CodebuildProjectSourceBuildStatusConfig", typing.Dict[str, typing.Any]]] = None,
        git_clone_depth: typing.Optional[jsii.Number] = None,
        git_submodules_config: typing.Optional[typing.Union["CodebuildProjectSourceGitSubmodulesConfig", typing.Dict[str, typing.Any]]] = None,
        insecure_ssl: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        location: typing.Optional[builtins.str] = None,
        report_build_status: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#type CodebuildProject#type}.
        :param auth: auth block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#auth CodebuildProject#auth}
        :param buildspec: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#buildspec CodebuildProject#buildspec}.
        :param build_status_config: build_status_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#build_status_config CodebuildProject#build_status_config}
        :param git_clone_depth: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#git_clone_depth CodebuildProject#git_clone_depth}.
        :param git_submodules_config: git_submodules_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#git_submodules_config CodebuildProject#git_submodules_config}
        :param insecure_ssl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#insecure_ssl CodebuildProject#insecure_ssl}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#location CodebuildProject#location}.
        :param report_build_status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#report_build_status CodebuildProject#report_build_status}.
        '''
        value = CodebuildProjectSource(
            type=type,
            auth=auth,
            buildspec=buildspec,
            build_status_config=build_status_config,
            git_clone_depth=git_clone_depth,
            git_submodules_config=git_submodules_config,
            insecure_ssl=insecure_ssl,
            location=location,
            report_build_status=report_build_status,
        )

        return typing.cast(None, jsii.invoke(self, "putSource", [value]))

    @jsii.member(jsii_name="putVpcConfig")
    def put_vpc_config(
        self,
        *,
        security_group_ids: typing.Sequence[builtins.str],
        subnets: typing.Sequence[builtins.str],
        vpc_id: builtins.str,
    ) -> None:
        '''
        :param security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#security_group_ids CodebuildProject#security_group_ids}.
        :param subnets: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#subnets CodebuildProject#subnets}.
        :param vpc_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#vpc_id CodebuildProject#vpc_id}.
        '''
        value = CodebuildProjectVpcConfig(
            security_group_ids=security_group_ids, subnets=subnets, vpc_id=vpc_id
        )

        return typing.cast(None, jsii.invoke(self, "putVpcConfig", [value]))

    @jsii.member(jsii_name="resetBadgeEnabled")
    def reset_badge_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBadgeEnabled", []))

    @jsii.member(jsii_name="resetBuildBatchConfig")
    def reset_build_batch_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBuildBatchConfig", []))

    @jsii.member(jsii_name="resetBuildTimeout")
    def reset_build_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBuildTimeout", []))

    @jsii.member(jsii_name="resetCache")
    def reset_cache(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCache", []))

    @jsii.member(jsii_name="resetConcurrentBuildLimit")
    def reset_concurrent_build_limit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConcurrentBuildLimit", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetEncryptionKey")
    def reset_encryption_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncryptionKey", []))

    @jsii.member(jsii_name="resetFileSystemLocations")
    def reset_file_system_locations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFileSystemLocations", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLogsConfig")
    def reset_logs_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogsConfig", []))

    @jsii.member(jsii_name="resetProjectVisibility")
    def reset_project_visibility(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProjectVisibility", []))

    @jsii.member(jsii_name="resetQueuedTimeout")
    def reset_queued_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueuedTimeout", []))

    @jsii.member(jsii_name="resetResourceAccessRole")
    def reset_resource_access_role(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceAccessRole", []))

    @jsii.member(jsii_name="resetSecondaryArtifacts")
    def reset_secondary_artifacts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecondaryArtifacts", []))

    @jsii.member(jsii_name="resetSecondarySources")
    def reset_secondary_sources(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecondarySources", []))

    @jsii.member(jsii_name="resetSecondarySourceVersion")
    def reset_secondary_source_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecondarySourceVersion", []))

    @jsii.member(jsii_name="resetSourceVersion")
    def reset_source_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceVersion", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetVpcConfig")
    def reset_vpc_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVpcConfig", []))

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
    @jsii.member(jsii_name="artifacts")
    def artifacts(self) -> "CodebuildProjectArtifactsOutputReference":
        return typing.cast("CodebuildProjectArtifactsOutputReference", jsii.get(self, "artifacts"))

    @builtins.property
    @jsii.member(jsii_name="badgeUrl")
    def badge_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "badgeUrl"))

    @builtins.property
    @jsii.member(jsii_name="buildBatchConfig")
    def build_batch_config(self) -> "CodebuildProjectBuildBatchConfigOutputReference":
        return typing.cast("CodebuildProjectBuildBatchConfigOutputReference", jsii.get(self, "buildBatchConfig"))

    @builtins.property
    @jsii.member(jsii_name="cache")
    def cache(self) -> "CodebuildProjectCacheOutputReference":
        return typing.cast("CodebuildProjectCacheOutputReference", jsii.get(self, "cache"))

    @builtins.property
    @jsii.member(jsii_name="environment")
    def environment(self) -> "CodebuildProjectEnvironmentOutputReference":
        return typing.cast("CodebuildProjectEnvironmentOutputReference", jsii.get(self, "environment"))

    @builtins.property
    @jsii.member(jsii_name="fileSystemLocations")
    def file_system_locations(self) -> "CodebuildProjectFileSystemLocationsList":
        return typing.cast("CodebuildProjectFileSystemLocationsList", jsii.get(self, "fileSystemLocations"))

    @builtins.property
    @jsii.member(jsii_name="logsConfig")
    def logs_config(self) -> "CodebuildProjectLogsConfigOutputReference":
        return typing.cast("CodebuildProjectLogsConfigOutputReference", jsii.get(self, "logsConfig"))

    @builtins.property
    @jsii.member(jsii_name="publicProjectAlias")
    def public_project_alias(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicProjectAlias"))

    @builtins.property
    @jsii.member(jsii_name="secondaryArtifacts")
    def secondary_artifacts(self) -> "CodebuildProjectSecondaryArtifactsList":
        return typing.cast("CodebuildProjectSecondaryArtifactsList", jsii.get(self, "secondaryArtifacts"))

    @builtins.property
    @jsii.member(jsii_name="secondarySources")
    def secondary_sources(self) -> "CodebuildProjectSecondarySourcesList":
        return typing.cast("CodebuildProjectSecondarySourcesList", jsii.get(self, "secondarySources"))

    @builtins.property
    @jsii.member(jsii_name="secondarySourceVersion")
    def secondary_source_version(self) -> "CodebuildProjectSecondarySourceVersionList":
        return typing.cast("CodebuildProjectSecondarySourceVersionList", jsii.get(self, "secondarySourceVersion"))

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> "CodebuildProjectSourceOutputReference":
        return typing.cast("CodebuildProjectSourceOutputReference", jsii.get(self, "source"))

    @builtins.property
    @jsii.member(jsii_name="vpcConfig")
    def vpc_config(self) -> "CodebuildProjectVpcConfigOutputReference":
        return typing.cast("CodebuildProjectVpcConfigOutputReference", jsii.get(self, "vpcConfig"))

    @builtins.property
    @jsii.member(jsii_name="artifactsInput")
    def artifacts_input(self) -> typing.Optional["CodebuildProjectArtifacts"]:
        return typing.cast(typing.Optional["CodebuildProjectArtifacts"], jsii.get(self, "artifactsInput"))

    @builtins.property
    @jsii.member(jsii_name="badgeEnabledInput")
    def badge_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "badgeEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="buildBatchConfigInput")
    def build_batch_config_input(
        self,
    ) -> typing.Optional["CodebuildProjectBuildBatchConfig"]:
        return typing.cast(typing.Optional["CodebuildProjectBuildBatchConfig"], jsii.get(self, "buildBatchConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="buildTimeoutInput")
    def build_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "buildTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="cacheInput")
    def cache_input(self) -> typing.Optional["CodebuildProjectCache"]:
        return typing.cast(typing.Optional["CodebuildProjectCache"], jsii.get(self, "cacheInput"))

    @builtins.property
    @jsii.member(jsii_name="concurrentBuildLimitInput")
    def concurrent_build_limit_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "concurrentBuildLimitInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptionKeyInput")
    def encryption_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "encryptionKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="environmentInput")
    def environment_input(self) -> typing.Optional["CodebuildProjectEnvironment"]:
        return typing.cast(typing.Optional["CodebuildProjectEnvironment"], jsii.get(self, "environmentInput"))

    @builtins.property
    @jsii.member(jsii_name="fileSystemLocationsInput")
    def file_system_locations_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CodebuildProjectFileSystemLocations"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CodebuildProjectFileSystemLocations"]]], jsii.get(self, "fileSystemLocationsInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="logsConfigInput")
    def logs_config_input(self) -> typing.Optional["CodebuildProjectLogsConfig"]:
        return typing.cast(typing.Optional["CodebuildProjectLogsConfig"], jsii.get(self, "logsConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="projectVisibilityInput")
    def project_visibility_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectVisibilityInput"))

    @builtins.property
    @jsii.member(jsii_name="queuedTimeoutInput")
    def queued_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "queuedTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceAccessRoleInput")
    def resource_access_role_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceAccessRoleInput"))

    @builtins.property
    @jsii.member(jsii_name="secondaryArtifactsInput")
    def secondary_artifacts_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CodebuildProjectSecondaryArtifacts"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CodebuildProjectSecondaryArtifacts"]]], jsii.get(self, "secondaryArtifactsInput"))

    @builtins.property
    @jsii.member(jsii_name="secondarySourcesInput")
    def secondary_sources_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CodebuildProjectSecondarySources"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CodebuildProjectSecondarySources"]]], jsii.get(self, "secondarySourcesInput"))

    @builtins.property
    @jsii.member(jsii_name="secondarySourceVersionInput")
    def secondary_source_version_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CodebuildProjectSecondarySourceVersion"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CodebuildProjectSecondarySourceVersion"]]], jsii.get(self, "secondarySourceVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceRoleInput")
    def service_role_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceRoleInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceInput")
    def source_input(self) -> typing.Optional["CodebuildProjectSource"]:
        return typing.cast(typing.Optional["CodebuildProjectSource"], jsii.get(self, "sourceInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceVersionInput")
    def source_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceVersionInput"))

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
    @jsii.member(jsii_name="vpcConfigInput")
    def vpc_config_input(self) -> typing.Optional["CodebuildProjectVpcConfig"]:
        return typing.cast(typing.Optional["CodebuildProjectVpcConfig"], jsii.get(self, "vpcConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="badgeEnabled")
    def badge_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "badgeEnabled"))

    @badge_enabled.setter
    def badge_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "badgeEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="buildTimeout")
    def build_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "buildTimeout"))

    @build_timeout.setter
    def build_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "buildTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="concurrentBuildLimit")
    def concurrent_build_limit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "concurrentBuildLimit"))

    @concurrent_build_limit.setter
    def concurrent_build_limit(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "concurrentBuildLimit", value)

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
    @jsii.member(jsii_name="encryptionKey")
    def encryption_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "encryptionKey"))

    @encryption_key.setter
    def encryption_key(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionKey", value)

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
    @jsii.member(jsii_name="projectVisibility")
    def project_visibility(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "projectVisibility"))

    @project_visibility.setter
    def project_visibility(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectVisibility", value)

    @builtins.property
    @jsii.member(jsii_name="queuedTimeout")
    def queued_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "queuedTimeout"))

    @queued_timeout.setter
    def queued_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queuedTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="resourceAccessRole")
    def resource_access_role(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceAccessRole"))

    @resource_access_role.setter
    def resource_access_role(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceAccessRole", value)

    @builtins.property
    @jsii.member(jsii_name="serviceRole")
    def service_role(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceRole"))

    @service_role.setter
    def service_role(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceRole", value)

    @builtins.property
    @jsii.member(jsii_name="sourceVersion")
    def source_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceVersion"))

    @source_version.setter
    def source_version(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceVersion", value)

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
    jsii_type="@cdktf/provider-aws.codebuildProject.CodebuildProjectArtifacts",
    jsii_struct_bases=[],
    name_mapping={
        "type": "type",
        "artifact_identifier": "artifactIdentifier",
        "bucket_owner_access": "bucketOwnerAccess",
        "encryption_disabled": "encryptionDisabled",
        "location": "location",
        "name": "name",
        "namespace_type": "namespaceType",
        "override_artifact_name": "overrideArtifactName",
        "packaging": "packaging",
        "path": "path",
    },
)
class CodebuildProjectArtifacts:
    def __init__(
        self,
        *,
        type: builtins.str,
        artifact_identifier: typing.Optional[builtins.str] = None,
        bucket_owner_access: typing.Optional[builtins.str] = None,
        encryption_disabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        location: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        namespace_type: typing.Optional[builtins.str] = None,
        override_artifact_name: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        packaging: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#type CodebuildProject#type}.
        :param artifact_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#artifact_identifier CodebuildProject#artifact_identifier}.
        :param bucket_owner_access: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#bucket_owner_access CodebuildProject#bucket_owner_access}.
        :param encryption_disabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#encryption_disabled CodebuildProject#encryption_disabled}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#location CodebuildProject#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#name CodebuildProject#name}.
        :param namespace_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#namespace_type CodebuildProject#namespace_type}.
        :param override_artifact_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#override_artifact_name CodebuildProject#override_artifact_name}.
        :param packaging: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#packaging CodebuildProject#packaging}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#path CodebuildProject#path}.
        '''
        if __debug__:
            def stub(
                *,
                type: builtins.str,
                artifact_identifier: typing.Optional[builtins.str] = None,
                bucket_owner_access: typing.Optional[builtins.str] = None,
                encryption_disabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                location: typing.Optional[builtins.str] = None,
                name: typing.Optional[builtins.str] = None,
                namespace_type: typing.Optional[builtins.str] = None,
                override_artifact_name: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                packaging: typing.Optional[builtins.str] = None,
                path: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument artifact_identifier", value=artifact_identifier, expected_type=type_hints["artifact_identifier"])
            check_type(argname="argument bucket_owner_access", value=bucket_owner_access, expected_type=type_hints["bucket_owner_access"])
            check_type(argname="argument encryption_disabled", value=encryption_disabled, expected_type=type_hints["encryption_disabled"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument namespace_type", value=namespace_type, expected_type=type_hints["namespace_type"])
            check_type(argname="argument override_artifact_name", value=override_artifact_name, expected_type=type_hints["override_artifact_name"])
            check_type(argname="argument packaging", value=packaging, expected_type=type_hints["packaging"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if artifact_identifier is not None:
            self._values["artifact_identifier"] = artifact_identifier
        if bucket_owner_access is not None:
            self._values["bucket_owner_access"] = bucket_owner_access
        if encryption_disabled is not None:
            self._values["encryption_disabled"] = encryption_disabled
        if location is not None:
            self._values["location"] = location
        if name is not None:
            self._values["name"] = name
        if namespace_type is not None:
            self._values["namespace_type"] = namespace_type
        if override_artifact_name is not None:
            self._values["override_artifact_name"] = override_artifact_name
        if packaging is not None:
            self._values["packaging"] = packaging
        if path is not None:
            self._values["path"] = path

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#type CodebuildProject#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def artifact_identifier(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#artifact_identifier CodebuildProject#artifact_identifier}.'''
        result = self._values.get("artifact_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bucket_owner_access(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#bucket_owner_access CodebuildProject#bucket_owner_access}.'''
        result = self._values.get("bucket_owner_access")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encryption_disabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#encryption_disabled CodebuildProject#encryption_disabled}.'''
        result = self._values.get("encryption_disabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def location(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#location CodebuildProject#location}.'''
        result = self._values.get("location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#name CodebuildProject#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#namespace_type CodebuildProject#namespace_type}.'''
        result = self._values.get("namespace_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def override_artifact_name(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#override_artifact_name CodebuildProject#override_artifact_name}.'''
        result = self._values.get("override_artifact_name")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def packaging(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#packaging CodebuildProject#packaging}.'''
        result = self._values.get("packaging")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#path CodebuildProject#path}.'''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodebuildProjectArtifacts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodebuildProjectArtifactsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.codebuildProject.CodebuildProjectArtifactsOutputReference",
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

    @jsii.member(jsii_name="resetArtifactIdentifier")
    def reset_artifact_identifier(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArtifactIdentifier", []))

    @jsii.member(jsii_name="resetBucketOwnerAccess")
    def reset_bucket_owner_access(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketOwnerAccess", []))

    @jsii.member(jsii_name="resetEncryptionDisabled")
    def reset_encryption_disabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncryptionDisabled", []))

    @jsii.member(jsii_name="resetLocation")
    def reset_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocation", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNamespaceType")
    def reset_namespace_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespaceType", []))

    @jsii.member(jsii_name="resetOverrideArtifactName")
    def reset_override_artifact_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOverrideArtifactName", []))

    @jsii.member(jsii_name="resetPackaging")
    def reset_packaging(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPackaging", []))

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @builtins.property
    @jsii.member(jsii_name="artifactIdentifierInput")
    def artifact_identifier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "artifactIdentifierInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketOwnerAccessInput")
    def bucket_owner_access_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketOwnerAccessInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptionDisabledInput")
    def encryption_disabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "encryptionDisabledInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceTypeInput")
    def namespace_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="overrideArtifactNameInput")
    def override_artifact_name_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "overrideArtifactNameInput"))

    @builtins.property
    @jsii.member(jsii_name="packagingInput")
    def packaging_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "packagingInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="artifactIdentifier")
    def artifact_identifier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "artifactIdentifier"))

    @artifact_identifier.setter
    def artifact_identifier(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "artifactIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="bucketOwnerAccess")
    def bucket_owner_access(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketOwnerAccess"))

    @bucket_owner_access.setter
    def bucket_owner_access(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketOwnerAccess", value)

    @builtins.property
    @jsii.member(jsii_name="encryptionDisabled")
    def encryption_disabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "encryptionDisabled"))

    @encryption_disabled.setter
    def encryption_disabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionDisabled", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

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
    @jsii.member(jsii_name="namespaceType")
    def namespace_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespaceType"))

    @namespace_type.setter
    def namespace_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespaceType", value)

    @builtins.property
    @jsii.member(jsii_name="overrideArtifactName")
    def override_artifact_name(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "overrideArtifactName"))

    @override_artifact_name.setter
    def override_artifact_name(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "overrideArtifactName", value)

    @builtins.property
    @jsii.member(jsii_name="packaging")
    def packaging(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "packaging"))

    @packaging.setter
    def packaging(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "packaging", value)

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

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CodebuildProjectArtifacts]:
        return typing.cast(typing.Optional[CodebuildProjectArtifacts], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[CodebuildProjectArtifacts]) -> None:
        if __debug__:
            def stub(value: typing.Optional[CodebuildProjectArtifacts]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.codebuildProject.CodebuildProjectBuildBatchConfig",
    jsii_struct_bases=[],
    name_mapping={
        "service_role": "serviceRole",
        "combine_artifacts": "combineArtifacts",
        "restrictions": "restrictions",
        "timeout_in_mins": "timeoutInMins",
    },
)
class CodebuildProjectBuildBatchConfig:
    def __init__(
        self,
        *,
        service_role: builtins.str,
        combine_artifacts: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        restrictions: typing.Optional[typing.Union["CodebuildProjectBuildBatchConfigRestrictions", typing.Dict[str, typing.Any]]] = None,
        timeout_in_mins: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param service_role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#service_role CodebuildProject#service_role}.
        :param combine_artifacts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#combine_artifacts CodebuildProject#combine_artifacts}.
        :param restrictions: restrictions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#restrictions CodebuildProject#restrictions}
        :param timeout_in_mins: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#timeout_in_mins CodebuildProject#timeout_in_mins}.
        '''
        if isinstance(restrictions, dict):
            restrictions = CodebuildProjectBuildBatchConfigRestrictions(**restrictions)
        if __debug__:
            def stub(
                *,
                service_role: builtins.str,
                combine_artifacts: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                restrictions: typing.Optional[typing.Union[CodebuildProjectBuildBatchConfigRestrictions, typing.Dict[str, typing.Any]]] = None,
                timeout_in_mins: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument service_role", value=service_role, expected_type=type_hints["service_role"])
            check_type(argname="argument combine_artifacts", value=combine_artifacts, expected_type=type_hints["combine_artifacts"])
            check_type(argname="argument restrictions", value=restrictions, expected_type=type_hints["restrictions"])
            check_type(argname="argument timeout_in_mins", value=timeout_in_mins, expected_type=type_hints["timeout_in_mins"])
        self._values: typing.Dict[str, typing.Any] = {
            "service_role": service_role,
        }
        if combine_artifacts is not None:
            self._values["combine_artifacts"] = combine_artifacts
        if restrictions is not None:
            self._values["restrictions"] = restrictions
        if timeout_in_mins is not None:
            self._values["timeout_in_mins"] = timeout_in_mins

    @builtins.property
    def service_role(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#service_role CodebuildProject#service_role}.'''
        result = self._values.get("service_role")
        assert result is not None, "Required property 'service_role' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def combine_artifacts(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#combine_artifacts CodebuildProject#combine_artifacts}.'''
        result = self._values.get("combine_artifacts")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def restrictions(
        self,
    ) -> typing.Optional["CodebuildProjectBuildBatchConfigRestrictions"]:
        '''restrictions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#restrictions CodebuildProject#restrictions}
        '''
        result = self._values.get("restrictions")
        return typing.cast(typing.Optional["CodebuildProjectBuildBatchConfigRestrictions"], result)

    @builtins.property
    def timeout_in_mins(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#timeout_in_mins CodebuildProject#timeout_in_mins}.'''
        result = self._values.get("timeout_in_mins")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodebuildProjectBuildBatchConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodebuildProjectBuildBatchConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.codebuildProject.CodebuildProjectBuildBatchConfigOutputReference",
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

    @jsii.member(jsii_name="putRestrictions")
    def put_restrictions(
        self,
        *,
        compute_types_allowed: typing.Optional[typing.Sequence[builtins.str]] = None,
        maximum_builds_allowed: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param compute_types_allowed: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#compute_types_allowed CodebuildProject#compute_types_allowed}.
        :param maximum_builds_allowed: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#maximum_builds_allowed CodebuildProject#maximum_builds_allowed}.
        '''
        value = CodebuildProjectBuildBatchConfigRestrictions(
            compute_types_allowed=compute_types_allowed,
            maximum_builds_allowed=maximum_builds_allowed,
        )

        return typing.cast(None, jsii.invoke(self, "putRestrictions", [value]))

    @jsii.member(jsii_name="resetCombineArtifacts")
    def reset_combine_artifacts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCombineArtifacts", []))

    @jsii.member(jsii_name="resetRestrictions")
    def reset_restrictions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRestrictions", []))

    @jsii.member(jsii_name="resetTimeoutInMins")
    def reset_timeout_in_mins(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeoutInMins", []))

    @builtins.property
    @jsii.member(jsii_name="restrictions")
    def restrictions(
        self,
    ) -> "CodebuildProjectBuildBatchConfigRestrictionsOutputReference":
        return typing.cast("CodebuildProjectBuildBatchConfigRestrictionsOutputReference", jsii.get(self, "restrictions"))

    @builtins.property
    @jsii.member(jsii_name="combineArtifactsInput")
    def combine_artifacts_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "combineArtifactsInput"))

    @builtins.property
    @jsii.member(jsii_name="restrictionsInput")
    def restrictions_input(
        self,
    ) -> typing.Optional["CodebuildProjectBuildBatchConfigRestrictions"]:
        return typing.cast(typing.Optional["CodebuildProjectBuildBatchConfigRestrictions"], jsii.get(self, "restrictionsInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceRoleInput")
    def service_role_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceRoleInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutInMinsInput")
    def timeout_in_mins_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timeoutInMinsInput"))

    @builtins.property
    @jsii.member(jsii_name="combineArtifacts")
    def combine_artifacts(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "combineArtifacts"))

    @combine_artifacts.setter
    def combine_artifacts(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "combineArtifacts", value)

    @builtins.property
    @jsii.member(jsii_name="serviceRole")
    def service_role(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceRole"))

    @service_role.setter
    def service_role(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceRole", value)

    @builtins.property
    @jsii.member(jsii_name="timeoutInMins")
    def timeout_in_mins(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "timeoutInMins"))

    @timeout_in_mins.setter
    def timeout_in_mins(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeoutInMins", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CodebuildProjectBuildBatchConfig]:
        return typing.cast(typing.Optional[CodebuildProjectBuildBatchConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CodebuildProjectBuildBatchConfig],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[CodebuildProjectBuildBatchConfig]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.codebuildProject.CodebuildProjectBuildBatchConfigRestrictions",
    jsii_struct_bases=[],
    name_mapping={
        "compute_types_allowed": "computeTypesAllowed",
        "maximum_builds_allowed": "maximumBuildsAllowed",
    },
)
class CodebuildProjectBuildBatchConfigRestrictions:
    def __init__(
        self,
        *,
        compute_types_allowed: typing.Optional[typing.Sequence[builtins.str]] = None,
        maximum_builds_allowed: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param compute_types_allowed: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#compute_types_allowed CodebuildProject#compute_types_allowed}.
        :param maximum_builds_allowed: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#maximum_builds_allowed CodebuildProject#maximum_builds_allowed}.
        '''
        if __debug__:
            def stub(
                *,
                compute_types_allowed: typing.Optional[typing.Sequence[builtins.str]] = None,
                maximum_builds_allowed: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument compute_types_allowed", value=compute_types_allowed, expected_type=type_hints["compute_types_allowed"])
            check_type(argname="argument maximum_builds_allowed", value=maximum_builds_allowed, expected_type=type_hints["maximum_builds_allowed"])
        self._values: typing.Dict[str, typing.Any] = {}
        if compute_types_allowed is not None:
            self._values["compute_types_allowed"] = compute_types_allowed
        if maximum_builds_allowed is not None:
            self._values["maximum_builds_allowed"] = maximum_builds_allowed

    @builtins.property
    def compute_types_allowed(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#compute_types_allowed CodebuildProject#compute_types_allowed}.'''
        result = self._values.get("compute_types_allowed")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def maximum_builds_allowed(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#maximum_builds_allowed CodebuildProject#maximum_builds_allowed}.'''
        result = self._values.get("maximum_builds_allowed")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodebuildProjectBuildBatchConfigRestrictions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodebuildProjectBuildBatchConfigRestrictionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.codebuildProject.CodebuildProjectBuildBatchConfigRestrictionsOutputReference",
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

    @jsii.member(jsii_name="resetComputeTypesAllowed")
    def reset_compute_types_allowed(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComputeTypesAllowed", []))

    @jsii.member(jsii_name="resetMaximumBuildsAllowed")
    def reset_maximum_builds_allowed(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaximumBuildsAllowed", []))

    @builtins.property
    @jsii.member(jsii_name="computeTypesAllowedInput")
    def compute_types_allowed_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "computeTypesAllowedInput"))

    @builtins.property
    @jsii.member(jsii_name="maximumBuildsAllowedInput")
    def maximum_builds_allowed_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maximumBuildsAllowedInput"))

    @builtins.property
    @jsii.member(jsii_name="computeTypesAllowed")
    def compute_types_allowed(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "computeTypesAllowed"))

    @compute_types_allowed.setter
    def compute_types_allowed(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "computeTypesAllowed", value)

    @builtins.property
    @jsii.member(jsii_name="maximumBuildsAllowed")
    def maximum_builds_allowed(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maximumBuildsAllowed"))

    @maximum_builds_allowed.setter
    def maximum_builds_allowed(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maximumBuildsAllowed", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CodebuildProjectBuildBatchConfigRestrictions]:
        return typing.cast(typing.Optional[CodebuildProjectBuildBatchConfigRestrictions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CodebuildProjectBuildBatchConfigRestrictions],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CodebuildProjectBuildBatchConfigRestrictions],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.codebuildProject.CodebuildProjectCache",
    jsii_struct_bases=[],
    name_mapping={"location": "location", "modes": "modes", "type": "type"},
)
class CodebuildProjectCache:
    def __init__(
        self,
        *,
        location: typing.Optional[builtins.str] = None,
        modes: typing.Optional[typing.Sequence[builtins.str]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#location CodebuildProject#location}.
        :param modes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#modes CodebuildProject#modes}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#type CodebuildProject#type}.
        '''
        if __debug__:
            def stub(
                *,
                location: typing.Optional[builtins.str] = None,
                modes: typing.Optional[typing.Sequence[builtins.str]] = None,
                type: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument modes", value=modes, expected_type=type_hints["modes"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if location is not None:
            self._values["location"] = location
        if modes is not None:
            self._values["modes"] = modes
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def location(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#location CodebuildProject#location}.'''
        result = self._values.get("location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def modes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#modes CodebuildProject#modes}.'''
        result = self._values.get("modes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#type CodebuildProject#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodebuildProjectCache(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodebuildProjectCacheOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.codebuildProject.CodebuildProjectCacheOutputReference",
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

    @jsii.member(jsii_name="resetLocation")
    def reset_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocation", []))

    @jsii.member(jsii_name="resetModes")
    def reset_modes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetModes", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="modesInput")
    def modes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "modesInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="modes")
    def modes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "modes"))

    @modes.setter
    def modes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "modes", value)

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

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CodebuildProjectCache]:
        return typing.cast(typing.Optional[CodebuildProjectCache], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[CodebuildProjectCache]) -> None:
        if __debug__:
            def stub(value: typing.Optional[CodebuildProjectCache]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.codebuildProject.CodebuildProjectConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "artifacts": "artifacts",
        "environment": "environment",
        "name": "name",
        "service_role": "serviceRole",
        "source": "source",
        "badge_enabled": "badgeEnabled",
        "build_batch_config": "buildBatchConfig",
        "build_timeout": "buildTimeout",
        "cache": "cache",
        "concurrent_build_limit": "concurrentBuildLimit",
        "description": "description",
        "encryption_key": "encryptionKey",
        "file_system_locations": "fileSystemLocations",
        "id": "id",
        "logs_config": "logsConfig",
        "project_visibility": "projectVisibility",
        "queued_timeout": "queuedTimeout",
        "resource_access_role": "resourceAccessRole",
        "secondary_artifacts": "secondaryArtifacts",
        "secondary_sources": "secondarySources",
        "secondary_source_version": "secondarySourceVersion",
        "source_version": "sourceVersion",
        "tags": "tags",
        "tags_all": "tagsAll",
        "vpc_config": "vpcConfig",
    },
)
class CodebuildProjectConfig(cdktf.TerraformMetaArguments):
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
        artifacts: typing.Union[CodebuildProjectArtifacts, typing.Dict[str, typing.Any]],
        environment: typing.Union["CodebuildProjectEnvironment", typing.Dict[str, typing.Any]],
        name: builtins.str,
        service_role: builtins.str,
        source: typing.Union["CodebuildProjectSource", typing.Dict[str, typing.Any]],
        badge_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        build_batch_config: typing.Optional[typing.Union[CodebuildProjectBuildBatchConfig, typing.Dict[str, typing.Any]]] = None,
        build_timeout: typing.Optional[jsii.Number] = None,
        cache: typing.Optional[typing.Union[CodebuildProjectCache, typing.Dict[str, typing.Any]]] = None,
        concurrent_build_limit: typing.Optional[jsii.Number] = None,
        description: typing.Optional[builtins.str] = None,
        encryption_key: typing.Optional[builtins.str] = None,
        file_system_locations: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CodebuildProjectFileSystemLocations", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        logs_config: typing.Optional[typing.Union["CodebuildProjectLogsConfig", typing.Dict[str, typing.Any]]] = None,
        project_visibility: typing.Optional[builtins.str] = None,
        queued_timeout: typing.Optional[jsii.Number] = None,
        resource_access_role: typing.Optional[builtins.str] = None,
        secondary_artifacts: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CodebuildProjectSecondaryArtifacts", typing.Dict[str, typing.Any]]]]] = None,
        secondary_sources: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CodebuildProjectSecondarySources", typing.Dict[str, typing.Any]]]]] = None,
        secondary_source_version: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CodebuildProjectSecondarySourceVersion", typing.Dict[str, typing.Any]]]]] = None,
        source_version: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        vpc_config: typing.Optional[typing.Union["CodebuildProjectVpcConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param artifacts: artifacts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#artifacts CodebuildProject#artifacts}
        :param environment: environment block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#environment CodebuildProject#environment}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#name CodebuildProject#name}.
        :param service_role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#service_role CodebuildProject#service_role}.
        :param source: source block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#source CodebuildProject#source}
        :param badge_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#badge_enabled CodebuildProject#badge_enabled}.
        :param build_batch_config: build_batch_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#build_batch_config CodebuildProject#build_batch_config}
        :param build_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#build_timeout CodebuildProject#build_timeout}.
        :param cache: cache block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#cache CodebuildProject#cache}
        :param concurrent_build_limit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#concurrent_build_limit CodebuildProject#concurrent_build_limit}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#description CodebuildProject#description}.
        :param encryption_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#encryption_key CodebuildProject#encryption_key}.
        :param file_system_locations: file_system_locations block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#file_system_locations CodebuildProject#file_system_locations}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#id CodebuildProject#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param logs_config: logs_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#logs_config CodebuildProject#logs_config}
        :param project_visibility: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#project_visibility CodebuildProject#project_visibility}.
        :param queued_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#queued_timeout CodebuildProject#queued_timeout}.
        :param resource_access_role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#resource_access_role CodebuildProject#resource_access_role}.
        :param secondary_artifacts: secondary_artifacts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#secondary_artifacts CodebuildProject#secondary_artifacts}
        :param secondary_sources: secondary_sources block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#secondary_sources CodebuildProject#secondary_sources}
        :param secondary_source_version: secondary_source_version block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#secondary_source_version CodebuildProject#secondary_source_version}
        :param source_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#source_version CodebuildProject#source_version}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#tags CodebuildProject#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#tags_all CodebuildProject#tags_all}.
        :param vpc_config: vpc_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#vpc_config CodebuildProject#vpc_config}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(artifacts, dict):
            artifacts = CodebuildProjectArtifacts(**artifacts)
        if isinstance(environment, dict):
            environment = CodebuildProjectEnvironment(**environment)
        if isinstance(source, dict):
            source = CodebuildProjectSource(**source)
        if isinstance(build_batch_config, dict):
            build_batch_config = CodebuildProjectBuildBatchConfig(**build_batch_config)
        if isinstance(cache, dict):
            cache = CodebuildProjectCache(**cache)
        if isinstance(logs_config, dict):
            logs_config = CodebuildProjectLogsConfig(**logs_config)
        if isinstance(vpc_config, dict):
            vpc_config = CodebuildProjectVpcConfig(**vpc_config)
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
                artifacts: typing.Union[CodebuildProjectArtifacts, typing.Dict[str, typing.Any]],
                environment: typing.Union[CodebuildProjectEnvironment, typing.Dict[str, typing.Any]],
                name: builtins.str,
                service_role: builtins.str,
                source: typing.Union[CodebuildProjectSource, typing.Dict[str, typing.Any]],
                badge_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                build_batch_config: typing.Optional[typing.Union[CodebuildProjectBuildBatchConfig, typing.Dict[str, typing.Any]]] = None,
                build_timeout: typing.Optional[jsii.Number] = None,
                cache: typing.Optional[typing.Union[CodebuildProjectCache, typing.Dict[str, typing.Any]]] = None,
                concurrent_build_limit: typing.Optional[jsii.Number] = None,
                description: typing.Optional[builtins.str] = None,
                encryption_key: typing.Optional[builtins.str] = None,
                file_system_locations: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CodebuildProjectFileSystemLocations, typing.Dict[str, typing.Any]]]]] = None,
                id: typing.Optional[builtins.str] = None,
                logs_config: typing.Optional[typing.Union[CodebuildProjectLogsConfig, typing.Dict[str, typing.Any]]] = None,
                project_visibility: typing.Optional[builtins.str] = None,
                queued_timeout: typing.Optional[jsii.Number] = None,
                resource_access_role: typing.Optional[builtins.str] = None,
                secondary_artifacts: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CodebuildProjectSecondaryArtifacts, typing.Dict[str, typing.Any]]]]] = None,
                secondary_sources: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CodebuildProjectSecondarySources, typing.Dict[str, typing.Any]]]]] = None,
                secondary_source_version: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CodebuildProjectSecondarySourceVersion, typing.Dict[str, typing.Any]]]]] = None,
                source_version: typing.Optional[builtins.str] = None,
                tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                vpc_config: typing.Optional[typing.Union[CodebuildProjectVpcConfig, typing.Dict[str, typing.Any]]] = None,
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
            check_type(argname="argument artifacts", value=artifacts, expected_type=type_hints["artifacts"])
            check_type(argname="argument environment", value=environment, expected_type=type_hints["environment"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument service_role", value=service_role, expected_type=type_hints["service_role"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument badge_enabled", value=badge_enabled, expected_type=type_hints["badge_enabled"])
            check_type(argname="argument build_batch_config", value=build_batch_config, expected_type=type_hints["build_batch_config"])
            check_type(argname="argument build_timeout", value=build_timeout, expected_type=type_hints["build_timeout"])
            check_type(argname="argument cache", value=cache, expected_type=type_hints["cache"])
            check_type(argname="argument concurrent_build_limit", value=concurrent_build_limit, expected_type=type_hints["concurrent_build_limit"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument encryption_key", value=encryption_key, expected_type=type_hints["encryption_key"])
            check_type(argname="argument file_system_locations", value=file_system_locations, expected_type=type_hints["file_system_locations"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument logs_config", value=logs_config, expected_type=type_hints["logs_config"])
            check_type(argname="argument project_visibility", value=project_visibility, expected_type=type_hints["project_visibility"])
            check_type(argname="argument queued_timeout", value=queued_timeout, expected_type=type_hints["queued_timeout"])
            check_type(argname="argument resource_access_role", value=resource_access_role, expected_type=type_hints["resource_access_role"])
            check_type(argname="argument secondary_artifacts", value=secondary_artifacts, expected_type=type_hints["secondary_artifacts"])
            check_type(argname="argument secondary_sources", value=secondary_sources, expected_type=type_hints["secondary_sources"])
            check_type(argname="argument secondary_source_version", value=secondary_source_version, expected_type=type_hints["secondary_source_version"])
            check_type(argname="argument source_version", value=source_version, expected_type=type_hints["source_version"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument vpc_config", value=vpc_config, expected_type=type_hints["vpc_config"])
        self._values: typing.Dict[str, typing.Any] = {
            "artifacts": artifacts,
            "environment": environment,
            "name": name,
            "service_role": service_role,
            "source": source,
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
        if badge_enabled is not None:
            self._values["badge_enabled"] = badge_enabled
        if build_batch_config is not None:
            self._values["build_batch_config"] = build_batch_config
        if build_timeout is not None:
            self._values["build_timeout"] = build_timeout
        if cache is not None:
            self._values["cache"] = cache
        if concurrent_build_limit is not None:
            self._values["concurrent_build_limit"] = concurrent_build_limit
        if description is not None:
            self._values["description"] = description
        if encryption_key is not None:
            self._values["encryption_key"] = encryption_key
        if file_system_locations is not None:
            self._values["file_system_locations"] = file_system_locations
        if id is not None:
            self._values["id"] = id
        if logs_config is not None:
            self._values["logs_config"] = logs_config
        if project_visibility is not None:
            self._values["project_visibility"] = project_visibility
        if queued_timeout is not None:
            self._values["queued_timeout"] = queued_timeout
        if resource_access_role is not None:
            self._values["resource_access_role"] = resource_access_role
        if secondary_artifacts is not None:
            self._values["secondary_artifacts"] = secondary_artifacts
        if secondary_sources is not None:
            self._values["secondary_sources"] = secondary_sources
        if secondary_source_version is not None:
            self._values["secondary_source_version"] = secondary_source_version
        if source_version is not None:
            self._values["source_version"] = source_version
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if vpc_config is not None:
            self._values["vpc_config"] = vpc_config

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
    def artifacts(self) -> CodebuildProjectArtifacts:
        '''artifacts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#artifacts CodebuildProject#artifacts}
        '''
        result = self._values.get("artifacts")
        assert result is not None, "Required property 'artifacts' is missing"
        return typing.cast(CodebuildProjectArtifacts, result)

    @builtins.property
    def environment(self) -> "CodebuildProjectEnvironment":
        '''environment block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#environment CodebuildProject#environment}
        '''
        result = self._values.get("environment")
        assert result is not None, "Required property 'environment' is missing"
        return typing.cast("CodebuildProjectEnvironment", result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#name CodebuildProject#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_role(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#service_role CodebuildProject#service_role}.'''
        result = self._values.get("service_role")
        assert result is not None, "Required property 'service_role' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source(self) -> "CodebuildProjectSource":
        '''source block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#source CodebuildProject#source}
        '''
        result = self._values.get("source")
        assert result is not None, "Required property 'source' is missing"
        return typing.cast("CodebuildProjectSource", result)

    @builtins.property
    def badge_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#badge_enabled CodebuildProject#badge_enabled}.'''
        result = self._values.get("badge_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def build_batch_config(self) -> typing.Optional[CodebuildProjectBuildBatchConfig]:
        '''build_batch_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#build_batch_config CodebuildProject#build_batch_config}
        '''
        result = self._values.get("build_batch_config")
        return typing.cast(typing.Optional[CodebuildProjectBuildBatchConfig], result)

    @builtins.property
    def build_timeout(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#build_timeout CodebuildProject#build_timeout}.'''
        result = self._values.get("build_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def cache(self) -> typing.Optional[CodebuildProjectCache]:
        '''cache block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#cache CodebuildProject#cache}
        '''
        result = self._values.get("cache")
        return typing.cast(typing.Optional[CodebuildProjectCache], result)

    @builtins.property
    def concurrent_build_limit(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#concurrent_build_limit CodebuildProject#concurrent_build_limit}.'''
        result = self._values.get("concurrent_build_limit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#description CodebuildProject#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encryption_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#encryption_key CodebuildProject#encryption_key}.'''
        result = self._values.get("encryption_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def file_system_locations(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CodebuildProjectFileSystemLocations"]]]:
        '''file_system_locations block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#file_system_locations CodebuildProject#file_system_locations}
        '''
        result = self._values.get("file_system_locations")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CodebuildProjectFileSystemLocations"]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#id CodebuildProject#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def logs_config(self) -> typing.Optional["CodebuildProjectLogsConfig"]:
        '''logs_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#logs_config CodebuildProject#logs_config}
        '''
        result = self._values.get("logs_config")
        return typing.cast(typing.Optional["CodebuildProjectLogsConfig"], result)

    @builtins.property
    def project_visibility(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#project_visibility CodebuildProject#project_visibility}.'''
        result = self._values.get("project_visibility")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def queued_timeout(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#queued_timeout CodebuildProject#queued_timeout}.'''
        result = self._values.get("queued_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def resource_access_role(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#resource_access_role CodebuildProject#resource_access_role}.'''
        result = self._values.get("resource_access_role")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def secondary_artifacts(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CodebuildProjectSecondaryArtifacts"]]]:
        '''secondary_artifacts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#secondary_artifacts CodebuildProject#secondary_artifacts}
        '''
        result = self._values.get("secondary_artifacts")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CodebuildProjectSecondaryArtifacts"]]], result)

    @builtins.property
    def secondary_sources(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CodebuildProjectSecondarySources"]]]:
        '''secondary_sources block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#secondary_sources CodebuildProject#secondary_sources}
        '''
        result = self._values.get("secondary_sources")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CodebuildProjectSecondarySources"]]], result)

    @builtins.property
    def secondary_source_version(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CodebuildProjectSecondarySourceVersion"]]]:
        '''secondary_source_version block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#secondary_source_version CodebuildProject#secondary_source_version}
        '''
        result = self._values.get("secondary_source_version")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CodebuildProjectSecondarySourceVersion"]]], result)

    @builtins.property
    def source_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#source_version CodebuildProject#source_version}.'''
        result = self._values.get("source_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#tags CodebuildProject#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#tags_all CodebuildProject#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def vpc_config(self) -> typing.Optional["CodebuildProjectVpcConfig"]:
        '''vpc_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#vpc_config CodebuildProject#vpc_config}
        '''
        result = self._values.get("vpc_config")
        return typing.cast(typing.Optional["CodebuildProjectVpcConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodebuildProjectConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.codebuildProject.CodebuildProjectEnvironment",
    jsii_struct_bases=[],
    name_mapping={
        "compute_type": "computeType",
        "image": "image",
        "type": "type",
        "certificate": "certificate",
        "environment_variable": "environmentVariable",
        "image_pull_credentials_type": "imagePullCredentialsType",
        "privileged_mode": "privilegedMode",
        "registry_credential": "registryCredential",
    },
)
class CodebuildProjectEnvironment:
    def __init__(
        self,
        *,
        compute_type: builtins.str,
        image: builtins.str,
        type: builtins.str,
        certificate: typing.Optional[builtins.str] = None,
        environment_variable: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CodebuildProjectEnvironmentEnvironmentVariable", typing.Dict[str, typing.Any]]]]] = None,
        image_pull_credentials_type: typing.Optional[builtins.str] = None,
        privileged_mode: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        registry_credential: typing.Optional[typing.Union["CodebuildProjectEnvironmentRegistryCredential", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param compute_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#compute_type CodebuildProject#compute_type}.
        :param image: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#image CodebuildProject#image}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#type CodebuildProject#type}.
        :param certificate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#certificate CodebuildProject#certificate}.
        :param environment_variable: environment_variable block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#environment_variable CodebuildProject#environment_variable}
        :param image_pull_credentials_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#image_pull_credentials_type CodebuildProject#image_pull_credentials_type}.
        :param privileged_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#privileged_mode CodebuildProject#privileged_mode}.
        :param registry_credential: registry_credential block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#registry_credential CodebuildProject#registry_credential}
        '''
        if isinstance(registry_credential, dict):
            registry_credential = CodebuildProjectEnvironmentRegistryCredential(**registry_credential)
        if __debug__:
            def stub(
                *,
                compute_type: builtins.str,
                image: builtins.str,
                type: builtins.str,
                certificate: typing.Optional[builtins.str] = None,
                environment_variable: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CodebuildProjectEnvironmentEnvironmentVariable, typing.Dict[str, typing.Any]]]]] = None,
                image_pull_credentials_type: typing.Optional[builtins.str] = None,
                privileged_mode: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                registry_credential: typing.Optional[typing.Union[CodebuildProjectEnvironmentRegistryCredential, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument compute_type", value=compute_type, expected_type=type_hints["compute_type"])
            check_type(argname="argument image", value=image, expected_type=type_hints["image"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument certificate", value=certificate, expected_type=type_hints["certificate"])
            check_type(argname="argument environment_variable", value=environment_variable, expected_type=type_hints["environment_variable"])
            check_type(argname="argument image_pull_credentials_type", value=image_pull_credentials_type, expected_type=type_hints["image_pull_credentials_type"])
            check_type(argname="argument privileged_mode", value=privileged_mode, expected_type=type_hints["privileged_mode"])
            check_type(argname="argument registry_credential", value=registry_credential, expected_type=type_hints["registry_credential"])
        self._values: typing.Dict[str, typing.Any] = {
            "compute_type": compute_type,
            "image": image,
            "type": type,
        }
        if certificate is not None:
            self._values["certificate"] = certificate
        if environment_variable is not None:
            self._values["environment_variable"] = environment_variable
        if image_pull_credentials_type is not None:
            self._values["image_pull_credentials_type"] = image_pull_credentials_type
        if privileged_mode is not None:
            self._values["privileged_mode"] = privileged_mode
        if registry_credential is not None:
            self._values["registry_credential"] = registry_credential

    @builtins.property
    def compute_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#compute_type CodebuildProject#compute_type}.'''
        result = self._values.get("compute_type")
        assert result is not None, "Required property 'compute_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def image(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#image CodebuildProject#image}.'''
        result = self._values.get("image")
        assert result is not None, "Required property 'image' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#type CodebuildProject#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def certificate(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#certificate CodebuildProject#certificate}.'''
        result = self._values.get("certificate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def environment_variable(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CodebuildProjectEnvironmentEnvironmentVariable"]]]:
        '''environment_variable block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#environment_variable CodebuildProject#environment_variable}
        '''
        result = self._values.get("environment_variable")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CodebuildProjectEnvironmentEnvironmentVariable"]]], result)

    @builtins.property
    def image_pull_credentials_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#image_pull_credentials_type CodebuildProject#image_pull_credentials_type}.'''
        result = self._values.get("image_pull_credentials_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def privileged_mode(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#privileged_mode CodebuildProject#privileged_mode}.'''
        result = self._values.get("privileged_mode")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def registry_credential(
        self,
    ) -> typing.Optional["CodebuildProjectEnvironmentRegistryCredential"]:
        '''registry_credential block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#registry_credential CodebuildProject#registry_credential}
        '''
        result = self._values.get("registry_credential")
        return typing.cast(typing.Optional["CodebuildProjectEnvironmentRegistryCredential"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodebuildProjectEnvironment(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.codebuildProject.CodebuildProjectEnvironmentEnvironmentVariable",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "value": "value", "type": "type"},
)
class CodebuildProjectEnvironmentEnvironmentVariable:
    def __init__(
        self,
        *,
        name: builtins.str,
        value: builtins.str,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#name CodebuildProject#name}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#value CodebuildProject#value}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#type CodebuildProject#type}.
        '''
        if __debug__:
            def stub(
                *,
                name: builtins.str,
                value: builtins.str,
                type: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "value": value,
        }
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#name CodebuildProject#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#value CodebuildProject#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#type CodebuildProject#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodebuildProjectEnvironmentEnvironmentVariable(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodebuildProjectEnvironmentEnvironmentVariableList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.codebuildProject.CodebuildProjectEnvironmentEnvironmentVariableList",
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
    ) -> "CodebuildProjectEnvironmentEnvironmentVariableOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CodebuildProjectEnvironmentEnvironmentVariableOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CodebuildProjectEnvironmentEnvironmentVariable]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CodebuildProjectEnvironmentEnvironmentVariable]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CodebuildProjectEnvironmentEnvironmentVariable]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CodebuildProjectEnvironmentEnvironmentVariable]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CodebuildProjectEnvironmentEnvironmentVariableOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.codebuildProject.CodebuildProjectEnvironmentEnvironmentVariableOutputReference",
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

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

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

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CodebuildProjectEnvironmentEnvironmentVariable, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CodebuildProjectEnvironmentEnvironmentVariable, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CodebuildProjectEnvironmentEnvironmentVariable, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[CodebuildProjectEnvironmentEnvironmentVariable, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CodebuildProjectEnvironmentOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.codebuildProject.CodebuildProjectEnvironmentOutputReference",
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

    @jsii.member(jsii_name="putEnvironmentVariable")
    def put_environment_variable(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CodebuildProjectEnvironmentEnvironmentVariable, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CodebuildProjectEnvironmentEnvironmentVariable, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEnvironmentVariable", [value]))

    @jsii.member(jsii_name="putRegistryCredential")
    def put_registry_credential(
        self,
        *,
        credential: builtins.str,
        credential_provider: builtins.str,
    ) -> None:
        '''
        :param credential: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#credential CodebuildProject#credential}.
        :param credential_provider: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#credential_provider CodebuildProject#credential_provider}.
        '''
        value = CodebuildProjectEnvironmentRegistryCredential(
            credential=credential, credential_provider=credential_provider
        )

        return typing.cast(None, jsii.invoke(self, "putRegistryCredential", [value]))

    @jsii.member(jsii_name="resetCertificate")
    def reset_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificate", []))

    @jsii.member(jsii_name="resetEnvironmentVariable")
    def reset_environment_variable(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnvironmentVariable", []))

    @jsii.member(jsii_name="resetImagePullCredentialsType")
    def reset_image_pull_credentials_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImagePullCredentialsType", []))

    @jsii.member(jsii_name="resetPrivilegedMode")
    def reset_privileged_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivilegedMode", []))

    @jsii.member(jsii_name="resetRegistryCredential")
    def reset_registry_credential(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegistryCredential", []))

    @builtins.property
    @jsii.member(jsii_name="environmentVariable")
    def environment_variable(
        self,
    ) -> CodebuildProjectEnvironmentEnvironmentVariableList:
        return typing.cast(CodebuildProjectEnvironmentEnvironmentVariableList, jsii.get(self, "environmentVariable"))

    @builtins.property
    @jsii.member(jsii_name="registryCredential")
    def registry_credential(
        self,
    ) -> "CodebuildProjectEnvironmentRegistryCredentialOutputReference":
        return typing.cast("CodebuildProjectEnvironmentRegistryCredentialOutputReference", jsii.get(self, "registryCredential"))

    @builtins.property
    @jsii.member(jsii_name="certificateInput")
    def certificate_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateInput"))

    @builtins.property
    @jsii.member(jsii_name="computeTypeInput")
    def compute_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "computeTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="environmentVariableInput")
    def environment_variable_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CodebuildProjectEnvironmentEnvironmentVariable]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CodebuildProjectEnvironmentEnvironmentVariable]]], jsii.get(self, "environmentVariableInput"))

    @builtins.property
    @jsii.member(jsii_name="imageInput")
    def image_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageInput"))

    @builtins.property
    @jsii.member(jsii_name="imagePullCredentialsTypeInput")
    def image_pull_credentials_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imagePullCredentialsTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="privilegedModeInput")
    def privileged_mode_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "privilegedModeInput"))

    @builtins.property
    @jsii.member(jsii_name="registryCredentialInput")
    def registry_credential_input(
        self,
    ) -> typing.Optional["CodebuildProjectEnvironmentRegistryCredential"]:
        return typing.cast(typing.Optional["CodebuildProjectEnvironmentRegistryCredential"], jsii.get(self, "registryCredentialInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="certificate")
    def certificate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificate"))

    @certificate.setter
    def certificate(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificate", value)

    @builtins.property
    @jsii.member(jsii_name="computeType")
    def compute_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "computeType"))

    @compute_type.setter
    def compute_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "computeType", value)

    @builtins.property
    @jsii.member(jsii_name="image")
    def image(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "image"))

    @image.setter
    def image(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "image", value)

    @builtins.property
    @jsii.member(jsii_name="imagePullCredentialsType")
    def image_pull_credentials_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "imagePullCredentialsType"))

    @image_pull_credentials_type.setter
    def image_pull_credentials_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imagePullCredentialsType", value)

    @builtins.property
    @jsii.member(jsii_name="privilegedMode")
    def privileged_mode(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "privilegedMode"))

    @privileged_mode.setter
    def privileged_mode(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privilegedMode", value)

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

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CodebuildProjectEnvironment]:
        return typing.cast(typing.Optional[CodebuildProjectEnvironment], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CodebuildProjectEnvironment],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[CodebuildProjectEnvironment]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.codebuildProject.CodebuildProjectEnvironmentRegistryCredential",
    jsii_struct_bases=[],
    name_mapping={
        "credential": "credential",
        "credential_provider": "credentialProvider",
    },
)
class CodebuildProjectEnvironmentRegistryCredential:
    def __init__(
        self,
        *,
        credential: builtins.str,
        credential_provider: builtins.str,
    ) -> None:
        '''
        :param credential: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#credential CodebuildProject#credential}.
        :param credential_provider: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#credential_provider CodebuildProject#credential_provider}.
        '''
        if __debug__:
            def stub(
                *,
                credential: builtins.str,
                credential_provider: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument credential", value=credential, expected_type=type_hints["credential"])
            check_type(argname="argument credential_provider", value=credential_provider, expected_type=type_hints["credential_provider"])
        self._values: typing.Dict[str, typing.Any] = {
            "credential": credential,
            "credential_provider": credential_provider,
        }

    @builtins.property
    def credential(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#credential CodebuildProject#credential}.'''
        result = self._values.get("credential")
        assert result is not None, "Required property 'credential' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def credential_provider(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#credential_provider CodebuildProject#credential_provider}.'''
        result = self._values.get("credential_provider")
        assert result is not None, "Required property 'credential_provider' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodebuildProjectEnvironmentRegistryCredential(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodebuildProjectEnvironmentRegistryCredentialOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.codebuildProject.CodebuildProjectEnvironmentRegistryCredentialOutputReference",
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
    @jsii.member(jsii_name="credentialInput")
    def credential_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "credentialInput"))

    @builtins.property
    @jsii.member(jsii_name="credentialProviderInput")
    def credential_provider_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "credentialProviderInput"))

    @builtins.property
    @jsii.member(jsii_name="credential")
    def credential(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "credential"))

    @credential.setter
    def credential(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "credential", value)

    @builtins.property
    @jsii.member(jsii_name="credentialProvider")
    def credential_provider(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "credentialProvider"))

    @credential_provider.setter
    def credential_provider(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "credentialProvider", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CodebuildProjectEnvironmentRegistryCredential]:
        return typing.cast(typing.Optional[CodebuildProjectEnvironmentRegistryCredential], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CodebuildProjectEnvironmentRegistryCredential],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CodebuildProjectEnvironmentRegistryCredential],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.codebuildProject.CodebuildProjectFileSystemLocations",
    jsii_struct_bases=[],
    name_mapping={
        "identifier": "identifier",
        "location": "location",
        "mount_options": "mountOptions",
        "mount_point": "mountPoint",
        "type": "type",
    },
)
class CodebuildProjectFileSystemLocations:
    def __init__(
        self,
        *,
        identifier: typing.Optional[builtins.str] = None,
        location: typing.Optional[builtins.str] = None,
        mount_options: typing.Optional[builtins.str] = None,
        mount_point: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#identifier CodebuildProject#identifier}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#location CodebuildProject#location}.
        :param mount_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#mount_options CodebuildProject#mount_options}.
        :param mount_point: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#mount_point CodebuildProject#mount_point}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#type CodebuildProject#type}.
        '''
        if __debug__:
            def stub(
                *,
                identifier: typing.Optional[builtins.str] = None,
                location: typing.Optional[builtins.str] = None,
                mount_options: typing.Optional[builtins.str] = None,
                mount_point: typing.Optional[builtins.str] = None,
                type: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument identifier", value=identifier, expected_type=type_hints["identifier"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument mount_options", value=mount_options, expected_type=type_hints["mount_options"])
            check_type(argname="argument mount_point", value=mount_point, expected_type=type_hints["mount_point"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if identifier is not None:
            self._values["identifier"] = identifier
        if location is not None:
            self._values["location"] = location
        if mount_options is not None:
            self._values["mount_options"] = mount_options
        if mount_point is not None:
            self._values["mount_point"] = mount_point
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def identifier(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#identifier CodebuildProject#identifier}.'''
        result = self._values.get("identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def location(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#location CodebuildProject#location}.'''
        result = self._values.get("location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mount_options(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#mount_options CodebuildProject#mount_options}.'''
        result = self._values.get("mount_options")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mount_point(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#mount_point CodebuildProject#mount_point}.'''
        result = self._values.get("mount_point")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#type CodebuildProject#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodebuildProjectFileSystemLocations(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodebuildProjectFileSystemLocationsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.codebuildProject.CodebuildProjectFileSystemLocationsList",
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
    ) -> "CodebuildProjectFileSystemLocationsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CodebuildProjectFileSystemLocationsOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CodebuildProjectFileSystemLocations]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CodebuildProjectFileSystemLocations]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CodebuildProjectFileSystemLocations]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CodebuildProjectFileSystemLocations]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CodebuildProjectFileSystemLocationsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.codebuildProject.CodebuildProjectFileSystemLocationsOutputReference",
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

    @jsii.member(jsii_name="resetIdentifier")
    def reset_identifier(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentifier", []))

    @jsii.member(jsii_name="resetLocation")
    def reset_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocation", []))

    @jsii.member(jsii_name="resetMountOptions")
    def reset_mount_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMountOptions", []))

    @jsii.member(jsii_name="resetMountPoint")
    def reset_mount_point(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMountPoint", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="identifierInput")
    def identifier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identifierInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="mountOptionsInput")
    def mount_options_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mountOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="mountPointInput")
    def mount_point_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mountPointInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="identifier")
    def identifier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identifier"))

    @identifier.setter
    def identifier(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identifier", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="mountOptions")
    def mount_options(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mountOptions"))

    @mount_options.setter
    def mount_options(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mountOptions", value)

    @builtins.property
    @jsii.member(jsii_name="mountPoint")
    def mount_point(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mountPoint"))

    @mount_point.setter
    def mount_point(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mountPoint", value)

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

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CodebuildProjectFileSystemLocations, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CodebuildProjectFileSystemLocations, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CodebuildProjectFileSystemLocations, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[CodebuildProjectFileSystemLocations, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.codebuildProject.CodebuildProjectLogsConfig",
    jsii_struct_bases=[],
    name_mapping={"cloudwatch_logs": "cloudwatchLogs", "s3_logs": "s3Logs"},
)
class CodebuildProjectLogsConfig:
    def __init__(
        self,
        *,
        cloudwatch_logs: typing.Optional[typing.Union["CodebuildProjectLogsConfigCloudwatchLogs", typing.Dict[str, typing.Any]]] = None,
        s3_logs: typing.Optional[typing.Union["CodebuildProjectLogsConfigS3Logs", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param cloudwatch_logs: cloudwatch_logs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#cloudwatch_logs CodebuildProject#cloudwatch_logs}
        :param s3_logs: s3_logs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#s3_logs CodebuildProject#s3_logs}
        '''
        if isinstance(cloudwatch_logs, dict):
            cloudwatch_logs = CodebuildProjectLogsConfigCloudwatchLogs(**cloudwatch_logs)
        if isinstance(s3_logs, dict):
            s3_logs = CodebuildProjectLogsConfigS3Logs(**s3_logs)
        if __debug__:
            def stub(
                *,
                cloudwatch_logs: typing.Optional[typing.Union[CodebuildProjectLogsConfigCloudwatchLogs, typing.Dict[str, typing.Any]]] = None,
                s3_logs: typing.Optional[typing.Union[CodebuildProjectLogsConfigS3Logs, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument cloudwatch_logs", value=cloudwatch_logs, expected_type=type_hints["cloudwatch_logs"])
            check_type(argname="argument s3_logs", value=s3_logs, expected_type=type_hints["s3_logs"])
        self._values: typing.Dict[str, typing.Any] = {}
        if cloudwatch_logs is not None:
            self._values["cloudwatch_logs"] = cloudwatch_logs
        if s3_logs is not None:
            self._values["s3_logs"] = s3_logs

    @builtins.property
    def cloudwatch_logs(
        self,
    ) -> typing.Optional["CodebuildProjectLogsConfigCloudwatchLogs"]:
        '''cloudwatch_logs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#cloudwatch_logs CodebuildProject#cloudwatch_logs}
        '''
        result = self._values.get("cloudwatch_logs")
        return typing.cast(typing.Optional["CodebuildProjectLogsConfigCloudwatchLogs"], result)

    @builtins.property
    def s3_logs(self) -> typing.Optional["CodebuildProjectLogsConfigS3Logs"]:
        '''s3_logs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#s3_logs CodebuildProject#s3_logs}
        '''
        result = self._values.get("s3_logs")
        return typing.cast(typing.Optional["CodebuildProjectLogsConfigS3Logs"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodebuildProjectLogsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.codebuildProject.CodebuildProjectLogsConfigCloudwatchLogs",
    jsii_struct_bases=[],
    name_mapping={
        "group_name": "groupName",
        "status": "status",
        "stream_name": "streamName",
    },
)
class CodebuildProjectLogsConfigCloudwatchLogs:
    def __init__(
        self,
        *,
        group_name: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
        stream_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#group_name CodebuildProject#group_name}.
        :param status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#status CodebuildProject#status}.
        :param stream_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#stream_name CodebuildProject#stream_name}.
        '''
        if __debug__:
            def stub(
                *,
                group_name: typing.Optional[builtins.str] = None,
                status: typing.Optional[builtins.str] = None,
                stream_name: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument group_name", value=group_name, expected_type=type_hints["group_name"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument stream_name", value=stream_name, expected_type=type_hints["stream_name"])
        self._values: typing.Dict[str, typing.Any] = {}
        if group_name is not None:
            self._values["group_name"] = group_name
        if status is not None:
            self._values["status"] = status
        if stream_name is not None:
            self._values["stream_name"] = stream_name

    @builtins.property
    def group_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#group_name CodebuildProject#group_name}.'''
        result = self._values.get("group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#status CodebuildProject#status}.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def stream_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#stream_name CodebuildProject#stream_name}.'''
        result = self._values.get("stream_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodebuildProjectLogsConfigCloudwatchLogs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodebuildProjectLogsConfigCloudwatchLogsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.codebuildProject.CodebuildProjectLogsConfigCloudwatchLogsOutputReference",
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

    @jsii.member(jsii_name="resetGroupName")
    def reset_group_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupName", []))

    @jsii.member(jsii_name="resetStatus")
    def reset_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatus", []))

    @jsii.member(jsii_name="resetStreamName")
    def reset_stream_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStreamName", []))

    @builtins.property
    @jsii.member(jsii_name="groupNameInput")
    def group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="statusInput")
    def status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusInput"))

    @builtins.property
    @jsii.member(jsii_name="streamNameInput")
    def stream_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "streamNameInput"))

    @builtins.property
    @jsii.member(jsii_name="groupName")
    def group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "groupName"))

    @group_name.setter
    def group_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupName", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @status.setter
    def status(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @builtins.property
    @jsii.member(jsii_name="streamName")
    def stream_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "streamName"))

    @stream_name.setter
    def stream_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "streamName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CodebuildProjectLogsConfigCloudwatchLogs]:
        return typing.cast(typing.Optional[CodebuildProjectLogsConfigCloudwatchLogs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CodebuildProjectLogsConfigCloudwatchLogs],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CodebuildProjectLogsConfigCloudwatchLogs],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CodebuildProjectLogsConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.codebuildProject.CodebuildProjectLogsConfigOutputReference",
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

    @jsii.member(jsii_name="putCloudwatchLogs")
    def put_cloudwatch_logs(
        self,
        *,
        group_name: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
        stream_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#group_name CodebuildProject#group_name}.
        :param status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#status CodebuildProject#status}.
        :param stream_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#stream_name CodebuildProject#stream_name}.
        '''
        value = CodebuildProjectLogsConfigCloudwatchLogs(
            group_name=group_name, status=status, stream_name=stream_name
        )

        return typing.cast(None, jsii.invoke(self, "putCloudwatchLogs", [value]))

    @jsii.member(jsii_name="putS3Logs")
    def put_s3_logs(
        self,
        *,
        bucket_owner_access: typing.Optional[builtins.str] = None,
        encryption_disabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        location: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_owner_access: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#bucket_owner_access CodebuildProject#bucket_owner_access}.
        :param encryption_disabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#encryption_disabled CodebuildProject#encryption_disabled}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#location CodebuildProject#location}.
        :param status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#status CodebuildProject#status}.
        '''
        value = CodebuildProjectLogsConfigS3Logs(
            bucket_owner_access=bucket_owner_access,
            encryption_disabled=encryption_disabled,
            location=location,
            status=status,
        )

        return typing.cast(None, jsii.invoke(self, "putS3Logs", [value]))

    @jsii.member(jsii_name="resetCloudwatchLogs")
    def reset_cloudwatch_logs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudwatchLogs", []))

    @jsii.member(jsii_name="resetS3Logs")
    def reset_s3_logs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3Logs", []))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLogs")
    def cloudwatch_logs(
        self,
    ) -> CodebuildProjectLogsConfigCloudwatchLogsOutputReference:
        return typing.cast(CodebuildProjectLogsConfigCloudwatchLogsOutputReference, jsii.get(self, "cloudwatchLogs"))

    @builtins.property
    @jsii.member(jsii_name="s3Logs")
    def s3_logs(self) -> "CodebuildProjectLogsConfigS3LogsOutputReference":
        return typing.cast("CodebuildProjectLogsConfigS3LogsOutputReference", jsii.get(self, "s3Logs"))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLogsInput")
    def cloudwatch_logs_input(
        self,
    ) -> typing.Optional[CodebuildProjectLogsConfigCloudwatchLogs]:
        return typing.cast(typing.Optional[CodebuildProjectLogsConfigCloudwatchLogs], jsii.get(self, "cloudwatchLogsInput"))

    @builtins.property
    @jsii.member(jsii_name="s3LogsInput")
    def s3_logs_input(self) -> typing.Optional["CodebuildProjectLogsConfigS3Logs"]:
        return typing.cast(typing.Optional["CodebuildProjectLogsConfigS3Logs"], jsii.get(self, "s3LogsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CodebuildProjectLogsConfig]:
        return typing.cast(typing.Optional[CodebuildProjectLogsConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CodebuildProjectLogsConfig],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[CodebuildProjectLogsConfig]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.codebuildProject.CodebuildProjectLogsConfigS3Logs",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_owner_access": "bucketOwnerAccess",
        "encryption_disabled": "encryptionDisabled",
        "location": "location",
        "status": "status",
    },
)
class CodebuildProjectLogsConfigS3Logs:
    def __init__(
        self,
        *,
        bucket_owner_access: typing.Optional[builtins.str] = None,
        encryption_disabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        location: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_owner_access: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#bucket_owner_access CodebuildProject#bucket_owner_access}.
        :param encryption_disabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#encryption_disabled CodebuildProject#encryption_disabled}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#location CodebuildProject#location}.
        :param status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#status CodebuildProject#status}.
        '''
        if __debug__:
            def stub(
                *,
                bucket_owner_access: typing.Optional[builtins.str] = None,
                encryption_disabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                location: typing.Optional[builtins.str] = None,
                status: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument bucket_owner_access", value=bucket_owner_access, expected_type=type_hints["bucket_owner_access"])
            check_type(argname="argument encryption_disabled", value=encryption_disabled, expected_type=type_hints["encryption_disabled"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
        self._values: typing.Dict[str, typing.Any] = {}
        if bucket_owner_access is not None:
            self._values["bucket_owner_access"] = bucket_owner_access
        if encryption_disabled is not None:
            self._values["encryption_disabled"] = encryption_disabled
        if location is not None:
            self._values["location"] = location
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def bucket_owner_access(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#bucket_owner_access CodebuildProject#bucket_owner_access}.'''
        result = self._values.get("bucket_owner_access")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encryption_disabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#encryption_disabled CodebuildProject#encryption_disabled}.'''
        result = self._values.get("encryption_disabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def location(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#location CodebuildProject#location}.'''
        result = self._values.get("location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#status CodebuildProject#status}.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodebuildProjectLogsConfigS3Logs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodebuildProjectLogsConfigS3LogsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.codebuildProject.CodebuildProjectLogsConfigS3LogsOutputReference",
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

    @jsii.member(jsii_name="resetBucketOwnerAccess")
    def reset_bucket_owner_access(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketOwnerAccess", []))

    @jsii.member(jsii_name="resetEncryptionDisabled")
    def reset_encryption_disabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncryptionDisabled", []))

    @jsii.member(jsii_name="resetLocation")
    def reset_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocation", []))

    @jsii.member(jsii_name="resetStatus")
    def reset_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatus", []))

    @builtins.property
    @jsii.member(jsii_name="bucketOwnerAccessInput")
    def bucket_owner_access_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketOwnerAccessInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptionDisabledInput")
    def encryption_disabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "encryptionDisabledInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="statusInput")
    def status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketOwnerAccess")
    def bucket_owner_access(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketOwnerAccess"))

    @bucket_owner_access.setter
    def bucket_owner_access(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketOwnerAccess", value)

    @builtins.property
    @jsii.member(jsii_name="encryptionDisabled")
    def encryption_disabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "encryptionDisabled"))

    @encryption_disabled.setter
    def encryption_disabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionDisabled", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @status.setter
    def status(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CodebuildProjectLogsConfigS3Logs]:
        return typing.cast(typing.Optional[CodebuildProjectLogsConfigS3Logs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CodebuildProjectLogsConfigS3Logs],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[CodebuildProjectLogsConfigS3Logs]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.codebuildProject.CodebuildProjectSecondaryArtifacts",
    jsii_struct_bases=[],
    name_mapping={
        "artifact_identifier": "artifactIdentifier",
        "type": "type",
        "bucket_owner_access": "bucketOwnerAccess",
        "encryption_disabled": "encryptionDisabled",
        "location": "location",
        "name": "name",
        "namespace_type": "namespaceType",
        "override_artifact_name": "overrideArtifactName",
        "packaging": "packaging",
        "path": "path",
    },
)
class CodebuildProjectSecondaryArtifacts:
    def __init__(
        self,
        *,
        artifact_identifier: builtins.str,
        type: builtins.str,
        bucket_owner_access: typing.Optional[builtins.str] = None,
        encryption_disabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        location: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        namespace_type: typing.Optional[builtins.str] = None,
        override_artifact_name: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        packaging: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param artifact_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#artifact_identifier CodebuildProject#artifact_identifier}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#type CodebuildProject#type}.
        :param bucket_owner_access: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#bucket_owner_access CodebuildProject#bucket_owner_access}.
        :param encryption_disabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#encryption_disabled CodebuildProject#encryption_disabled}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#location CodebuildProject#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#name CodebuildProject#name}.
        :param namespace_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#namespace_type CodebuildProject#namespace_type}.
        :param override_artifact_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#override_artifact_name CodebuildProject#override_artifact_name}.
        :param packaging: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#packaging CodebuildProject#packaging}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#path CodebuildProject#path}.
        '''
        if __debug__:
            def stub(
                *,
                artifact_identifier: builtins.str,
                type: builtins.str,
                bucket_owner_access: typing.Optional[builtins.str] = None,
                encryption_disabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                location: typing.Optional[builtins.str] = None,
                name: typing.Optional[builtins.str] = None,
                namespace_type: typing.Optional[builtins.str] = None,
                override_artifact_name: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                packaging: typing.Optional[builtins.str] = None,
                path: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument artifact_identifier", value=artifact_identifier, expected_type=type_hints["artifact_identifier"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument bucket_owner_access", value=bucket_owner_access, expected_type=type_hints["bucket_owner_access"])
            check_type(argname="argument encryption_disabled", value=encryption_disabled, expected_type=type_hints["encryption_disabled"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument namespace_type", value=namespace_type, expected_type=type_hints["namespace_type"])
            check_type(argname="argument override_artifact_name", value=override_artifact_name, expected_type=type_hints["override_artifact_name"])
            check_type(argname="argument packaging", value=packaging, expected_type=type_hints["packaging"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        self._values: typing.Dict[str, typing.Any] = {
            "artifact_identifier": artifact_identifier,
            "type": type,
        }
        if bucket_owner_access is not None:
            self._values["bucket_owner_access"] = bucket_owner_access
        if encryption_disabled is not None:
            self._values["encryption_disabled"] = encryption_disabled
        if location is not None:
            self._values["location"] = location
        if name is not None:
            self._values["name"] = name
        if namespace_type is not None:
            self._values["namespace_type"] = namespace_type
        if override_artifact_name is not None:
            self._values["override_artifact_name"] = override_artifact_name
        if packaging is not None:
            self._values["packaging"] = packaging
        if path is not None:
            self._values["path"] = path

    @builtins.property
    def artifact_identifier(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#artifact_identifier CodebuildProject#artifact_identifier}.'''
        result = self._values.get("artifact_identifier")
        assert result is not None, "Required property 'artifact_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#type CodebuildProject#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bucket_owner_access(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#bucket_owner_access CodebuildProject#bucket_owner_access}.'''
        result = self._values.get("bucket_owner_access")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encryption_disabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#encryption_disabled CodebuildProject#encryption_disabled}.'''
        result = self._values.get("encryption_disabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def location(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#location CodebuildProject#location}.'''
        result = self._values.get("location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#name CodebuildProject#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#namespace_type CodebuildProject#namespace_type}.'''
        result = self._values.get("namespace_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def override_artifact_name(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#override_artifact_name CodebuildProject#override_artifact_name}.'''
        result = self._values.get("override_artifact_name")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def packaging(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#packaging CodebuildProject#packaging}.'''
        result = self._values.get("packaging")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#path CodebuildProject#path}.'''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodebuildProjectSecondaryArtifacts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodebuildProjectSecondaryArtifactsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.codebuildProject.CodebuildProjectSecondaryArtifactsList",
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
    ) -> "CodebuildProjectSecondaryArtifactsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CodebuildProjectSecondaryArtifactsOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CodebuildProjectSecondaryArtifacts]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CodebuildProjectSecondaryArtifacts]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CodebuildProjectSecondaryArtifacts]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CodebuildProjectSecondaryArtifacts]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CodebuildProjectSecondaryArtifactsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.codebuildProject.CodebuildProjectSecondaryArtifactsOutputReference",
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

    @jsii.member(jsii_name="resetBucketOwnerAccess")
    def reset_bucket_owner_access(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketOwnerAccess", []))

    @jsii.member(jsii_name="resetEncryptionDisabled")
    def reset_encryption_disabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncryptionDisabled", []))

    @jsii.member(jsii_name="resetLocation")
    def reset_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocation", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNamespaceType")
    def reset_namespace_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespaceType", []))

    @jsii.member(jsii_name="resetOverrideArtifactName")
    def reset_override_artifact_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOverrideArtifactName", []))

    @jsii.member(jsii_name="resetPackaging")
    def reset_packaging(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPackaging", []))

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @builtins.property
    @jsii.member(jsii_name="artifactIdentifierInput")
    def artifact_identifier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "artifactIdentifierInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketOwnerAccessInput")
    def bucket_owner_access_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketOwnerAccessInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptionDisabledInput")
    def encryption_disabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "encryptionDisabledInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceTypeInput")
    def namespace_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="overrideArtifactNameInput")
    def override_artifact_name_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "overrideArtifactNameInput"))

    @builtins.property
    @jsii.member(jsii_name="packagingInput")
    def packaging_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "packagingInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="artifactIdentifier")
    def artifact_identifier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "artifactIdentifier"))

    @artifact_identifier.setter
    def artifact_identifier(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "artifactIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="bucketOwnerAccess")
    def bucket_owner_access(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketOwnerAccess"))

    @bucket_owner_access.setter
    def bucket_owner_access(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketOwnerAccess", value)

    @builtins.property
    @jsii.member(jsii_name="encryptionDisabled")
    def encryption_disabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "encryptionDisabled"))

    @encryption_disabled.setter
    def encryption_disabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionDisabled", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

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
    @jsii.member(jsii_name="namespaceType")
    def namespace_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespaceType"))

    @namespace_type.setter
    def namespace_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespaceType", value)

    @builtins.property
    @jsii.member(jsii_name="overrideArtifactName")
    def override_artifact_name(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "overrideArtifactName"))

    @override_artifact_name.setter
    def override_artifact_name(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "overrideArtifactName", value)

    @builtins.property
    @jsii.member(jsii_name="packaging")
    def packaging(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "packaging"))

    @packaging.setter
    def packaging(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "packaging", value)

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

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CodebuildProjectSecondaryArtifacts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CodebuildProjectSecondaryArtifacts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CodebuildProjectSecondaryArtifacts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[CodebuildProjectSecondaryArtifacts, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.codebuildProject.CodebuildProjectSecondarySourceVersion",
    jsii_struct_bases=[],
    name_mapping={
        "source_identifier": "sourceIdentifier",
        "source_version": "sourceVersion",
    },
)
class CodebuildProjectSecondarySourceVersion:
    def __init__(
        self,
        *,
        source_identifier: builtins.str,
        source_version: builtins.str,
    ) -> None:
        '''
        :param source_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#source_identifier CodebuildProject#source_identifier}.
        :param source_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#source_version CodebuildProject#source_version}.
        '''
        if __debug__:
            def stub(
                *,
                source_identifier: builtins.str,
                source_version: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument source_identifier", value=source_identifier, expected_type=type_hints["source_identifier"])
            check_type(argname="argument source_version", value=source_version, expected_type=type_hints["source_version"])
        self._values: typing.Dict[str, typing.Any] = {
            "source_identifier": source_identifier,
            "source_version": source_version,
        }

    @builtins.property
    def source_identifier(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#source_identifier CodebuildProject#source_identifier}.'''
        result = self._values.get("source_identifier")
        assert result is not None, "Required property 'source_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_version(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#source_version CodebuildProject#source_version}.'''
        result = self._values.get("source_version")
        assert result is not None, "Required property 'source_version' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodebuildProjectSecondarySourceVersion(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodebuildProjectSecondarySourceVersionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.codebuildProject.CodebuildProjectSecondarySourceVersionList",
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
    ) -> "CodebuildProjectSecondarySourceVersionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CodebuildProjectSecondarySourceVersionOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CodebuildProjectSecondarySourceVersion]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CodebuildProjectSecondarySourceVersion]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CodebuildProjectSecondarySourceVersion]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CodebuildProjectSecondarySourceVersion]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CodebuildProjectSecondarySourceVersionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.codebuildProject.CodebuildProjectSecondarySourceVersionOutputReference",
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
    @jsii.member(jsii_name="sourceIdentifierInput")
    def source_identifier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceIdentifierInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceVersionInput")
    def source_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceIdentifier")
    def source_identifier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceIdentifier"))

    @source_identifier.setter
    def source_identifier(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="sourceVersion")
    def source_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceVersion"))

    @source_version.setter
    def source_version(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceVersion", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CodebuildProjectSecondarySourceVersion, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CodebuildProjectSecondarySourceVersion, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CodebuildProjectSecondarySourceVersion, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[CodebuildProjectSecondarySourceVersion, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.codebuildProject.CodebuildProjectSecondarySources",
    jsii_struct_bases=[],
    name_mapping={
        "source_identifier": "sourceIdentifier",
        "type": "type",
        "auth": "auth",
        "buildspec": "buildspec",
        "build_status_config": "buildStatusConfig",
        "git_clone_depth": "gitCloneDepth",
        "git_submodules_config": "gitSubmodulesConfig",
        "insecure_ssl": "insecureSsl",
        "location": "location",
        "report_build_status": "reportBuildStatus",
    },
)
class CodebuildProjectSecondarySources:
    def __init__(
        self,
        *,
        source_identifier: builtins.str,
        type: builtins.str,
        auth: typing.Optional[typing.Union["CodebuildProjectSecondarySourcesAuth", typing.Dict[str, typing.Any]]] = None,
        buildspec: typing.Optional[builtins.str] = None,
        build_status_config: typing.Optional[typing.Union["CodebuildProjectSecondarySourcesBuildStatusConfig", typing.Dict[str, typing.Any]]] = None,
        git_clone_depth: typing.Optional[jsii.Number] = None,
        git_submodules_config: typing.Optional[typing.Union["CodebuildProjectSecondarySourcesGitSubmodulesConfig", typing.Dict[str, typing.Any]]] = None,
        insecure_ssl: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        location: typing.Optional[builtins.str] = None,
        report_build_status: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param source_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#source_identifier CodebuildProject#source_identifier}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#type CodebuildProject#type}.
        :param auth: auth block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#auth CodebuildProject#auth}
        :param buildspec: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#buildspec CodebuildProject#buildspec}.
        :param build_status_config: build_status_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#build_status_config CodebuildProject#build_status_config}
        :param git_clone_depth: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#git_clone_depth CodebuildProject#git_clone_depth}.
        :param git_submodules_config: git_submodules_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#git_submodules_config CodebuildProject#git_submodules_config}
        :param insecure_ssl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#insecure_ssl CodebuildProject#insecure_ssl}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#location CodebuildProject#location}.
        :param report_build_status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#report_build_status CodebuildProject#report_build_status}.
        '''
        if isinstance(auth, dict):
            auth = CodebuildProjectSecondarySourcesAuth(**auth)
        if isinstance(build_status_config, dict):
            build_status_config = CodebuildProjectSecondarySourcesBuildStatusConfig(**build_status_config)
        if isinstance(git_submodules_config, dict):
            git_submodules_config = CodebuildProjectSecondarySourcesGitSubmodulesConfig(**git_submodules_config)
        if __debug__:
            def stub(
                *,
                source_identifier: builtins.str,
                type: builtins.str,
                auth: typing.Optional[typing.Union[CodebuildProjectSecondarySourcesAuth, typing.Dict[str, typing.Any]]] = None,
                buildspec: typing.Optional[builtins.str] = None,
                build_status_config: typing.Optional[typing.Union[CodebuildProjectSecondarySourcesBuildStatusConfig, typing.Dict[str, typing.Any]]] = None,
                git_clone_depth: typing.Optional[jsii.Number] = None,
                git_submodules_config: typing.Optional[typing.Union[CodebuildProjectSecondarySourcesGitSubmodulesConfig, typing.Dict[str, typing.Any]]] = None,
                insecure_ssl: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                location: typing.Optional[builtins.str] = None,
                report_build_status: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument source_identifier", value=source_identifier, expected_type=type_hints["source_identifier"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument auth", value=auth, expected_type=type_hints["auth"])
            check_type(argname="argument buildspec", value=buildspec, expected_type=type_hints["buildspec"])
            check_type(argname="argument build_status_config", value=build_status_config, expected_type=type_hints["build_status_config"])
            check_type(argname="argument git_clone_depth", value=git_clone_depth, expected_type=type_hints["git_clone_depth"])
            check_type(argname="argument git_submodules_config", value=git_submodules_config, expected_type=type_hints["git_submodules_config"])
            check_type(argname="argument insecure_ssl", value=insecure_ssl, expected_type=type_hints["insecure_ssl"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument report_build_status", value=report_build_status, expected_type=type_hints["report_build_status"])
        self._values: typing.Dict[str, typing.Any] = {
            "source_identifier": source_identifier,
            "type": type,
        }
        if auth is not None:
            self._values["auth"] = auth
        if buildspec is not None:
            self._values["buildspec"] = buildspec
        if build_status_config is not None:
            self._values["build_status_config"] = build_status_config
        if git_clone_depth is not None:
            self._values["git_clone_depth"] = git_clone_depth
        if git_submodules_config is not None:
            self._values["git_submodules_config"] = git_submodules_config
        if insecure_ssl is not None:
            self._values["insecure_ssl"] = insecure_ssl
        if location is not None:
            self._values["location"] = location
        if report_build_status is not None:
            self._values["report_build_status"] = report_build_status

    @builtins.property
    def source_identifier(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#source_identifier CodebuildProject#source_identifier}.'''
        result = self._values.get("source_identifier")
        assert result is not None, "Required property 'source_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#type CodebuildProject#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def auth(self) -> typing.Optional["CodebuildProjectSecondarySourcesAuth"]:
        '''auth block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#auth CodebuildProject#auth}
        '''
        result = self._values.get("auth")
        return typing.cast(typing.Optional["CodebuildProjectSecondarySourcesAuth"], result)

    @builtins.property
    def buildspec(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#buildspec CodebuildProject#buildspec}.'''
        result = self._values.get("buildspec")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def build_status_config(
        self,
    ) -> typing.Optional["CodebuildProjectSecondarySourcesBuildStatusConfig"]:
        '''build_status_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#build_status_config CodebuildProject#build_status_config}
        '''
        result = self._values.get("build_status_config")
        return typing.cast(typing.Optional["CodebuildProjectSecondarySourcesBuildStatusConfig"], result)

    @builtins.property
    def git_clone_depth(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#git_clone_depth CodebuildProject#git_clone_depth}.'''
        result = self._values.get("git_clone_depth")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def git_submodules_config(
        self,
    ) -> typing.Optional["CodebuildProjectSecondarySourcesGitSubmodulesConfig"]:
        '''git_submodules_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#git_submodules_config CodebuildProject#git_submodules_config}
        '''
        result = self._values.get("git_submodules_config")
        return typing.cast(typing.Optional["CodebuildProjectSecondarySourcesGitSubmodulesConfig"], result)

    @builtins.property
    def insecure_ssl(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#insecure_ssl CodebuildProject#insecure_ssl}.'''
        result = self._values.get("insecure_ssl")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def location(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#location CodebuildProject#location}.'''
        result = self._values.get("location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def report_build_status(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#report_build_status CodebuildProject#report_build_status}.'''
        result = self._values.get("report_build_status")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodebuildProjectSecondarySources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.codebuildProject.CodebuildProjectSecondarySourcesAuth",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "resource": "resource"},
)
class CodebuildProjectSecondarySourcesAuth:
    def __init__(
        self,
        *,
        type: builtins.str,
        resource: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#type CodebuildProject#type}.
        :param resource: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#resource CodebuildProject#resource}.
        '''
        if __debug__:
            def stub(
                *,
                type: builtins.str,
                resource: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if resource is not None:
            self._values["resource"] = resource

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#type CodebuildProject#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#resource CodebuildProject#resource}.'''
        result = self._values.get("resource")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodebuildProjectSecondarySourcesAuth(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodebuildProjectSecondarySourcesAuthOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.codebuildProject.CodebuildProjectSecondarySourcesAuthOutputReference",
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

    @jsii.member(jsii_name="resetResource")
    def reset_resource(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResource", []))

    @builtins.property
    @jsii.member(jsii_name="resourceInput")
    def resource_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="resource")
    def resource(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resource"))

    @resource.setter
    def resource(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resource", value)

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

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CodebuildProjectSecondarySourcesAuth]:
        return typing.cast(typing.Optional[CodebuildProjectSecondarySourcesAuth], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CodebuildProjectSecondarySourcesAuth],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CodebuildProjectSecondarySourcesAuth],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.codebuildProject.CodebuildProjectSecondarySourcesBuildStatusConfig",
    jsii_struct_bases=[],
    name_mapping={"context": "context", "target_url": "targetUrl"},
)
class CodebuildProjectSecondarySourcesBuildStatusConfig:
    def __init__(
        self,
        *,
        context: typing.Optional[builtins.str] = None,
        target_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param context: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#context CodebuildProject#context}.
        :param target_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#target_url CodebuildProject#target_url}.
        '''
        if __debug__:
            def stub(
                *,
                context: typing.Optional[builtins.str] = None,
                target_url: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument context", value=context, expected_type=type_hints["context"])
            check_type(argname="argument target_url", value=target_url, expected_type=type_hints["target_url"])
        self._values: typing.Dict[str, typing.Any] = {}
        if context is not None:
            self._values["context"] = context
        if target_url is not None:
            self._values["target_url"] = target_url

    @builtins.property
    def context(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#context CodebuildProject#context}.'''
        result = self._values.get("context")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#target_url CodebuildProject#target_url}.'''
        result = self._values.get("target_url")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodebuildProjectSecondarySourcesBuildStatusConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodebuildProjectSecondarySourcesBuildStatusConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.codebuildProject.CodebuildProjectSecondarySourcesBuildStatusConfigOutputReference",
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

    @jsii.member(jsii_name="resetContext")
    def reset_context(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContext", []))

    @jsii.member(jsii_name="resetTargetUrl")
    def reset_target_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetUrl", []))

    @builtins.property
    @jsii.member(jsii_name="contextInput")
    def context_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contextInput"))

    @builtins.property
    @jsii.member(jsii_name="targetUrlInput")
    def target_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="context")
    def context(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "context"))

    @context.setter
    def context(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "context", value)

    @builtins.property
    @jsii.member(jsii_name="targetUrl")
    def target_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetUrl"))

    @target_url.setter
    def target_url(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetUrl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CodebuildProjectSecondarySourcesBuildStatusConfig]:
        return typing.cast(typing.Optional[CodebuildProjectSecondarySourcesBuildStatusConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CodebuildProjectSecondarySourcesBuildStatusConfig],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CodebuildProjectSecondarySourcesBuildStatusConfig],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.codebuildProject.CodebuildProjectSecondarySourcesGitSubmodulesConfig",
    jsii_struct_bases=[],
    name_mapping={"fetch_submodules": "fetchSubmodules"},
)
class CodebuildProjectSecondarySourcesGitSubmodulesConfig:
    def __init__(
        self,
        *,
        fetch_submodules: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param fetch_submodules: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#fetch_submodules CodebuildProject#fetch_submodules}.
        '''
        if __debug__:
            def stub(
                *,
                fetch_submodules: typing.Union[builtins.bool, cdktf.IResolvable],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument fetch_submodules", value=fetch_submodules, expected_type=type_hints["fetch_submodules"])
        self._values: typing.Dict[str, typing.Any] = {
            "fetch_submodules": fetch_submodules,
        }

    @builtins.property
    def fetch_submodules(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#fetch_submodules CodebuildProject#fetch_submodules}.'''
        result = self._values.get("fetch_submodules")
        assert result is not None, "Required property 'fetch_submodules' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodebuildProjectSecondarySourcesGitSubmodulesConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodebuildProjectSecondarySourcesGitSubmodulesConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.codebuildProject.CodebuildProjectSecondarySourcesGitSubmodulesConfigOutputReference",
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
    @jsii.member(jsii_name="fetchSubmodulesInput")
    def fetch_submodules_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "fetchSubmodulesInput"))

    @builtins.property
    @jsii.member(jsii_name="fetchSubmodules")
    def fetch_submodules(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "fetchSubmodules"))

    @fetch_submodules.setter
    def fetch_submodules(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fetchSubmodules", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CodebuildProjectSecondarySourcesGitSubmodulesConfig]:
        return typing.cast(typing.Optional[CodebuildProjectSecondarySourcesGitSubmodulesConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CodebuildProjectSecondarySourcesGitSubmodulesConfig],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CodebuildProjectSecondarySourcesGitSubmodulesConfig],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CodebuildProjectSecondarySourcesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.codebuildProject.CodebuildProjectSecondarySourcesList",
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
    ) -> "CodebuildProjectSecondarySourcesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CodebuildProjectSecondarySourcesOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CodebuildProjectSecondarySources]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CodebuildProjectSecondarySources]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CodebuildProjectSecondarySources]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CodebuildProjectSecondarySources]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CodebuildProjectSecondarySourcesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.codebuildProject.CodebuildProjectSecondarySourcesOutputReference",
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

    @jsii.member(jsii_name="putAuth")
    def put_auth(
        self,
        *,
        type: builtins.str,
        resource: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#type CodebuildProject#type}.
        :param resource: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#resource CodebuildProject#resource}.
        '''
        value = CodebuildProjectSecondarySourcesAuth(type=type, resource=resource)

        return typing.cast(None, jsii.invoke(self, "putAuth", [value]))

    @jsii.member(jsii_name="putBuildStatusConfig")
    def put_build_status_config(
        self,
        *,
        context: typing.Optional[builtins.str] = None,
        target_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param context: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#context CodebuildProject#context}.
        :param target_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#target_url CodebuildProject#target_url}.
        '''
        value = CodebuildProjectSecondarySourcesBuildStatusConfig(
            context=context, target_url=target_url
        )

        return typing.cast(None, jsii.invoke(self, "putBuildStatusConfig", [value]))

    @jsii.member(jsii_name="putGitSubmodulesConfig")
    def put_git_submodules_config(
        self,
        *,
        fetch_submodules: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param fetch_submodules: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#fetch_submodules CodebuildProject#fetch_submodules}.
        '''
        value = CodebuildProjectSecondarySourcesGitSubmodulesConfig(
            fetch_submodules=fetch_submodules
        )

        return typing.cast(None, jsii.invoke(self, "putGitSubmodulesConfig", [value]))

    @jsii.member(jsii_name="resetAuth")
    def reset_auth(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuth", []))

    @jsii.member(jsii_name="resetBuildspec")
    def reset_buildspec(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBuildspec", []))

    @jsii.member(jsii_name="resetBuildStatusConfig")
    def reset_build_status_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBuildStatusConfig", []))

    @jsii.member(jsii_name="resetGitCloneDepth")
    def reset_git_clone_depth(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGitCloneDepth", []))

    @jsii.member(jsii_name="resetGitSubmodulesConfig")
    def reset_git_submodules_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGitSubmodulesConfig", []))

    @jsii.member(jsii_name="resetInsecureSsl")
    def reset_insecure_ssl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInsecureSsl", []))

    @jsii.member(jsii_name="resetLocation")
    def reset_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocation", []))

    @jsii.member(jsii_name="resetReportBuildStatus")
    def reset_report_build_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReportBuildStatus", []))

    @builtins.property
    @jsii.member(jsii_name="auth")
    def auth(self) -> CodebuildProjectSecondarySourcesAuthOutputReference:
        return typing.cast(CodebuildProjectSecondarySourcesAuthOutputReference, jsii.get(self, "auth"))

    @builtins.property
    @jsii.member(jsii_name="buildStatusConfig")
    def build_status_config(
        self,
    ) -> CodebuildProjectSecondarySourcesBuildStatusConfigOutputReference:
        return typing.cast(CodebuildProjectSecondarySourcesBuildStatusConfigOutputReference, jsii.get(self, "buildStatusConfig"))

    @builtins.property
    @jsii.member(jsii_name="gitSubmodulesConfig")
    def git_submodules_config(
        self,
    ) -> CodebuildProjectSecondarySourcesGitSubmodulesConfigOutputReference:
        return typing.cast(CodebuildProjectSecondarySourcesGitSubmodulesConfigOutputReference, jsii.get(self, "gitSubmodulesConfig"))

    @builtins.property
    @jsii.member(jsii_name="authInput")
    def auth_input(self) -> typing.Optional[CodebuildProjectSecondarySourcesAuth]:
        return typing.cast(typing.Optional[CodebuildProjectSecondarySourcesAuth], jsii.get(self, "authInput"))

    @builtins.property
    @jsii.member(jsii_name="buildspecInput")
    def buildspec_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "buildspecInput"))

    @builtins.property
    @jsii.member(jsii_name="buildStatusConfigInput")
    def build_status_config_input(
        self,
    ) -> typing.Optional[CodebuildProjectSecondarySourcesBuildStatusConfig]:
        return typing.cast(typing.Optional[CodebuildProjectSecondarySourcesBuildStatusConfig], jsii.get(self, "buildStatusConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="gitCloneDepthInput")
    def git_clone_depth_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "gitCloneDepthInput"))

    @builtins.property
    @jsii.member(jsii_name="gitSubmodulesConfigInput")
    def git_submodules_config_input(
        self,
    ) -> typing.Optional[CodebuildProjectSecondarySourcesGitSubmodulesConfig]:
        return typing.cast(typing.Optional[CodebuildProjectSecondarySourcesGitSubmodulesConfig], jsii.get(self, "gitSubmodulesConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="insecureSslInput")
    def insecure_ssl_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "insecureSslInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="reportBuildStatusInput")
    def report_build_status_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "reportBuildStatusInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceIdentifierInput")
    def source_identifier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceIdentifierInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="buildspec")
    def buildspec(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "buildspec"))

    @buildspec.setter
    def buildspec(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "buildspec", value)

    @builtins.property
    @jsii.member(jsii_name="gitCloneDepth")
    def git_clone_depth(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "gitCloneDepth"))

    @git_clone_depth.setter
    def git_clone_depth(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gitCloneDepth", value)

    @builtins.property
    @jsii.member(jsii_name="insecureSsl")
    def insecure_ssl(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "insecureSsl"))

    @insecure_ssl.setter
    def insecure_ssl(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "insecureSsl", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="reportBuildStatus")
    def report_build_status(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "reportBuildStatus"))

    @report_build_status.setter
    def report_build_status(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "reportBuildStatus", value)

    @builtins.property
    @jsii.member(jsii_name="sourceIdentifier")
    def source_identifier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceIdentifier"))

    @source_identifier.setter
    def source_identifier(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceIdentifier", value)

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

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CodebuildProjectSecondarySources, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CodebuildProjectSecondarySources, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CodebuildProjectSecondarySources, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[CodebuildProjectSecondarySources, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.codebuildProject.CodebuildProjectSource",
    jsii_struct_bases=[],
    name_mapping={
        "type": "type",
        "auth": "auth",
        "buildspec": "buildspec",
        "build_status_config": "buildStatusConfig",
        "git_clone_depth": "gitCloneDepth",
        "git_submodules_config": "gitSubmodulesConfig",
        "insecure_ssl": "insecureSsl",
        "location": "location",
        "report_build_status": "reportBuildStatus",
    },
)
class CodebuildProjectSource:
    def __init__(
        self,
        *,
        type: builtins.str,
        auth: typing.Optional[typing.Union["CodebuildProjectSourceAuth", typing.Dict[str, typing.Any]]] = None,
        buildspec: typing.Optional[builtins.str] = None,
        build_status_config: typing.Optional[typing.Union["CodebuildProjectSourceBuildStatusConfig", typing.Dict[str, typing.Any]]] = None,
        git_clone_depth: typing.Optional[jsii.Number] = None,
        git_submodules_config: typing.Optional[typing.Union["CodebuildProjectSourceGitSubmodulesConfig", typing.Dict[str, typing.Any]]] = None,
        insecure_ssl: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        location: typing.Optional[builtins.str] = None,
        report_build_status: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#type CodebuildProject#type}.
        :param auth: auth block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#auth CodebuildProject#auth}
        :param buildspec: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#buildspec CodebuildProject#buildspec}.
        :param build_status_config: build_status_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#build_status_config CodebuildProject#build_status_config}
        :param git_clone_depth: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#git_clone_depth CodebuildProject#git_clone_depth}.
        :param git_submodules_config: git_submodules_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#git_submodules_config CodebuildProject#git_submodules_config}
        :param insecure_ssl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#insecure_ssl CodebuildProject#insecure_ssl}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#location CodebuildProject#location}.
        :param report_build_status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#report_build_status CodebuildProject#report_build_status}.
        '''
        if isinstance(auth, dict):
            auth = CodebuildProjectSourceAuth(**auth)
        if isinstance(build_status_config, dict):
            build_status_config = CodebuildProjectSourceBuildStatusConfig(**build_status_config)
        if isinstance(git_submodules_config, dict):
            git_submodules_config = CodebuildProjectSourceGitSubmodulesConfig(**git_submodules_config)
        if __debug__:
            def stub(
                *,
                type: builtins.str,
                auth: typing.Optional[typing.Union[CodebuildProjectSourceAuth, typing.Dict[str, typing.Any]]] = None,
                buildspec: typing.Optional[builtins.str] = None,
                build_status_config: typing.Optional[typing.Union[CodebuildProjectSourceBuildStatusConfig, typing.Dict[str, typing.Any]]] = None,
                git_clone_depth: typing.Optional[jsii.Number] = None,
                git_submodules_config: typing.Optional[typing.Union[CodebuildProjectSourceGitSubmodulesConfig, typing.Dict[str, typing.Any]]] = None,
                insecure_ssl: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                location: typing.Optional[builtins.str] = None,
                report_build_status: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument auth", value=auth, expected_type=type_hints["auth"])
            check_type(argname="argument buildspec", value=buildspec, expected_type=type_hints["buildspec"])
            check_type(argname="argument build_status_config", value=build_status_config, expected_type=type_hints["build_status_config"])
            check_type(argname="argument git_clone_depth", value=git_clone_depth, expected_type=type_hints["git_clone_depth"])
            check_type(argname="argument git_submodules_config", value=git_submodules_config, expected_type=type_hints["git_submodules_config"])
            check_type(argname="argument insecure_ssl", value=insecure_ssl, expected_type=type_hints["insecure_ssl"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument report_build_status", value=report_build_status, expected_type=type_hints["report_build_status"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if auth is not None:
            self._values["auth"] = auth
        if buildspec is not None:
            self._values["buildspec"] = buildspec
        if build_status_config is not None:
            self._values["build_status_config"] = build_status_config
        if git_clone_depth is not None:
            self._values["git_clone_depth"] = git_clone_depth
        if git_submodules_config is not None:
            self._values["git_submodules_config"] = git_submodules_config
        if insecure_ssl is not None:
            self._values["insecure_ssl"] = insecure_ssl
        if location is not None:
            self._values["location"] = location
        if report_build_status is not None:
            self._values["report_build_status"] = report_build_status

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#type CodebuildProject#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def auth(self) -> typing.Optional["CodebuildProjectSourceAuth"]:
        '''auth block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#auth CodebuildProject#auth}
        '''
        result = self._values.get("auth")
        return typing.cast(typing.Optional["CodebuildProjectSourceAuth"], result)

    @builtins.property
    def buildspec(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#buildspec CodebuildProject#buildspec}.'''
        result = self._values.get("buildspec")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def build_status_config(
        self,
    ) -> typing.Optional["CodebuildProjectSourceBuildStatusConfig"]:
        '''build_status_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#build_status_config CodebuildProject#build_status_config}
        '''
        result = self._values.get("build_status_config")
        return typing.cast(typing.Optional["CodebuildProjectSourceBuildStatusConfig"], result)

    @builtins.property
    def git_clone_depth(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#git_clone_depth CodebuildProject#git_clone_depth}.'''
        result = self._values.get("git_clone_depth")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def git_submodules_config(
        self,
    ) -> typing.Optional["CodebuildProjectSourceGitSubmodulesConfig"]:
        '''git_submodules_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#git_submodules_config CodebuildProject#git_submodules_config}
        '''
        result = self._values.get("git_submodules_config")
        return typing.cast(typing.Optional["CodebuildProjectSourceGitSubmodulesConfig"], result)

    @builtins.property
    def insecure_ssl(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#insecure_ssl CodebuildProject#insecure_ssl}.'''
        result = self._values.get("insecure_ssl")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def location(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#location CodebuildProject#location}.'''
        result = self._values.get("location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def report_build_status(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#report_build_status CodebuildProject#report_build_status}.'''
        result = self._values.get("report_build_status")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodebuildProjectSource(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.codebuildProject.CodebuildProjectSourceAuth",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "resource": "resource"},
)
class CodebuildProjectSourceAuth:
    def __init__(
        self,
        *,
        type: builtins.str,
        resource: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#type CodebuildProject#type}.
        :param resource: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#resource CodebuildProject#resource}.
        '''
        if __debug__:
            def stub(
                *,
                type: builtins.str,
                resource: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if resource is not None:
            self._values["resource"] = resource

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#type CodebuildProject#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#resource CodebuildProject#resource}.'''
        result = self._values.get("resource")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodebuildProjectSourceAuth(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodebuildProjectSourceAuthOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.codebuildProject.CodebuildProjectSourceAuthOutputReference",
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

    @jsii.member(jsii_name="resetResource")
    def reset_resource(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResource", []))

    @builtins.property
    @jsii.member(jsii_name="resourceInput")
    def resource_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="resource")
    def resource(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resource"))

    @resource.setter
    def resource(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resource", value)

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

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CodebuildProjectSourceAuth]:
        return typing.cast(typing.Optional[CodebuildProjectSourceAuth], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CodebuildProjectSourceAuth],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[CodebuildProjectSourceAuth]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.codebuildProject.CodebuildProjectSourceBuildStatusConfig",
    jsii_struct_bases=[],
    name_mapping={"context": "context", "target_url": "targetUrl"},
)
class CodebuildProjectSourceBuildStatusConfig:
    def __init__(
        self,
        *,
        context: typing.Optional[builtins.str] = None,
        target_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param context: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#context CodebuildProject#context}.
        :param target_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#target_url CodebuildProject#target_url}.
        '''
        if __debug__:
            def stub(
                *,
                context: typing.Optional[builtins.str] = None,
                target_url: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument context", value=context, expected_type=type_hints["context"])
            check_type(argname="argument target_url", value=target_url, expected_type=type_hints["target_url"])
        self._values: typing.Dict[str, typing.Any] = {}
        if context is not None:
            self._values["context"] = context
        if target_url is not None:
            self._values["target_url"] = target_url

    @builtins.property
    def context(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#context CodebuildProject#context}.'''
        result = self._values.get("context")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#target_url CodebuildProject#target_url}.'''
        result = self._values.get("target_url")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodebuildProjectSourceBuildStatusConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodebuildProjectSourceBuildStatusConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.codebuildProject.CodebuildProjectSourceBuildStatusConfigOutputReference",
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

    @jsii.member(jsii_name="resetContext")
    def reset_context(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContext", []))

    @jsii.member(jsii_name="resetTargetUrl")
    def reset_target_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetUrl", []))

    @builtins.property
    @jsii.member(jsii_name="contextInput")
    def context_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contextInput"))

    @builtins.property
    @jsii.member(jsii_name="targetUrlInput")
    def target_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="context")
    def context(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "context"))

    @context.setter
    def context(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "context", value)

    @builtins.property
    @jsii.member(jsii_name="targetUrl")
    def target_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetUrl"))

    @target_url.setter
    def target_url(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetUrl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CodebuildProjectSourceBuildStatusConfig]:
        return typing.cast(typing.Optional[CodebuildProjectSourceBuildStatusConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CodebuildProjectSourceBuildStatusConfig],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CodebuildProjectSourceBuildStatusConfig],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.codebuildProject.CodebuildProjectSourceGitSubmodulesConfig",
    jsii_struct_bases=[],
    name_mapping={"fetch_submodules": "fetchSubmodules"},
)
class CodebuildProjectSourceGitSubmodulesConfig:
    def __init__(
        self,
        *,
        fetch_submodules: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param fetch_submodules: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#fetch_submodules CodebuildProject#fetch_submodules}.
        '''
        if __debug__:
            def stub(
                *,
                fetch_submodules: typing.Union[builtins.bool, cdktf.IResolvable],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument fetch_submodules", value=fetch_submodules, expected_type=type_hints["fetch_submodules"])
        self._values: typing.Dict[str, typing.Any] = {
            "fetch_submodules": fetch_submodules,
        }

    @builtins.property
    def fetch_submodules(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#fetch_submodules CodebuildProject#fetch_submodules}.'''
        result = self._values.get("fetch_submodules")
        assert result is not None, "Required property 'fetch_submodules' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodebuildProjectSourceGitSubmodulesConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodebuildProjectSourceGitSubmodulesConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.codebuildProject.CodebuildProjectSourceGitSubmodulesConfigOutputReference",
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
    @jsii.member(jsii_name="fetchSubmodulesInput")
    def fetch_submodules_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "fetchSubmodulesInput"))

    @builtins.property
    @jsii.member(jsii_name="fetchSubmodules")
    def fetch_submodules(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "fetchSubmodules"))

    @fetch_submodules.setter
    def fetch_submodules(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fetchSubmodules", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CodebuildProjectSourceGitSubmodulesConfig]:
        return typing.cast(typing.Optional[CodebuildProjectSourceGitSubmodulesConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CodebuildProjectSourceGitSubmodulesConfig],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CodebuildProjectSourceGitSubmodulesConfig],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CodebuildProjectSourceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.codebuildProject.CodebuildProjectSourceOutputReference",
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

    @jsii.member(jsii_name="putAuth")
    def put_auth(
        self,
        *,
        type: builtins.str,
        resource: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#type CodebuildProject#type}.
        :param resource: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#resource CodebuildProject#resource}.
        '''
        value = CodebuildProjectSourceAuth(type=type, resource=resource)

        return typing.cast(None, jsii.invoke(self, "putAuth", [value]))

    @jsii.member(jsii_name="putBuildStatusConfig")
    def put_build_status_config(
        self,
        *,
        context: typing.Optional[builtins.str] = None,
        target_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param context: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#context CodebuildProject#context}.
        :param target_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#target_url CodebuildProject#target_url}.
        '''
        value = CodebuildProjectSourceBuildStatusConfig(
            context=context, target_url=target_url
        )

        return typing.cast(None, jsii.invoke(self, "putBuildStatusConfig", [value]))

    @jsii.member(jsii_name="putGitSubmodulesConfig")
    def put_git_submodules_config(
        self,
        *,
        fetch_submodules: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param fetch_submodules: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#fetch_submodules CodebuildProject#fetch_submodules}.
        '''
        value = CodebuildProjectSourceGitSubmodulesConfig(
            fetch_submodules=fetch_submodules
        )

        return typing.cast(None, jsii.invoke(self, "putGitSubmodulesConfig", [value]))

    @jsii.member(jsii_name="resetAuth")
    def reset_auth(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuth", []))

    @jsii.member(jsii_name="resetBuildspec")
    def reset_buildspec(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBuildspec", []))

    @jsii.member(jsii_name="resetBuildStatusConfig")
    def reset_build_status_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBuildStatusConfig", []))

    @jsii.member(jsii_name="resetGitCloneDepth")
    def reset_git_clone_depth(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGitCloneDepth", []))

    @jsii.member(jsii_name="resetGitSubmodulesConfig")
    def reset_git_submodules_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGitSubmodulesConfig", []))

    @jsii.member(jsii_name="resetInsecureSsl")
    def reset_insecure_ssl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInsecureSsl", []))

    @jsii.member(jsii_name="resetLocation")
    def reset_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocation", []))

    @jsii.member(jsii_name="resetReportBuildStatus")
    def reset_report_build_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReportBuildStatus", []))

    @builtins.property
    @jsii.member(jsii_name="auth")
    def auth(self) -> CodebuildProjectSourceAuthOutputReference:
        return typing.cast(CodebuildProjectSourceAuthOutputReference, jsii.get(self, "auth"))

    @builtins.property
    @jsii.member(jsii_name="buildStatusConfig")
    def build_status_config(
        self,
    ) -> CodebuildProjectSourceBuildStatusConfigOutputReference:
        return typing.cast(CodebuildProjectSourceBuildStatusConfigOutputReference, jsii.get(self, "buildStatusConfig"))

    @builtins.property
    @jsii.member(jsii_name="gitSubmodulesConfig")
    def git_submodules_config(
        self,
    ) -> CodebuildProjectSourceGitSubmodulesConfigOutputReference:
        return typing.cast(CodebuildProjectSourceGitSubmodulesConfigOutputReference, jsii.get(self, "gitSubmodulesConfig"))

    @builtins.property
    @jsii.member(jsii_name="authInput")
    def auth_input(self) -> typing.Optional[CodebuildProjectSourceAuth]:
        return typing.cast(typing.Optional[CodebuildProjectSourceAuth], jsii.get(self, "authInput"))

    @builtins.property
    @jsii.member(jsii_name="buildspecInput")
    def buildspec_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "buildspecInput"))

    @builtins.property
    @jsii.member(jsii_name="buildStatusConfigInput")
    def build_status_config_input(
        self,
    ) -> typing.Optional[CodebuildProjectSourceBuildStatusConfig]:
        return typing.cast(typing.Optional[CodebuildProjectSourceBuildStatusConfig], jsii.get(self, "buildStatusConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="gitCloneDepthInput")
    def git_clone_depth_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "gitCloneDepthInput"))

    @builtins.property
    @jsii.member(jsii_name="gitSubmodulesConfigInput")
    def git_submodules_config_input(
        self,
    ) -> typing.Optional[CodebuildProjectSourceGitSubmodulesConfig]:
        return typing.cast(typing.Optional[CodebuildProjectSourceGitSubmodulesConfig], jsii.get(self, "gitSubmodulesConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="insecureSslInput")
    def insecure_ssl_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "insecureSslInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="reportBuildStatusInput")
    def report_build_status_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "reportBuildStatusInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="buildspec")
    def buildspec(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "buildspec"))

    @buildspec.setter
    def buildspec(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "buildspec", value)

    @builtins.property
    @jsii.member(jsii_name="gitCloneDepth")
    def git_clone_depth(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "gitCloneDepth"))

    @git_clone_depth.setter
    def git_clone_depth(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gitCloneDepth", value)

    @builtins.property
    @jsii.member(jsii_name="insecureSsl")
    def insecure_ssl(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "insecureSsl"))

    @insecure_ssl.setter
    def insecure_ssl(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "insecureSsl", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="reportBuildStatus")
    def report_build_status(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "reportBuildStatus"))

    @report_build_status.setter
    def report_build_status(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "reportBuildStatus", value)

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

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CodebuildProjectSource]:
        return typing.cast(typing.Optional[CodebuildProjectSource], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[CodebuildProjectSource]) -> None:
        if __debug__:
            def stub(value: typing.Optional[CodebuildProjectSource]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.codebuildProject.CodebuildProjectVpcConfig",
    jsii_struct_bases=[],
    name_mapping={
        "security_group_ids": "securityGroupIds",
        "subnets": "subnets",
        "vpc_id": "vpcId",
    },
)
class CodebuildProjectVpcConfig:
    def __init__(
        self,
        *,
        security_group_ids: typing.Sequence[builtins.str],
        subnets: typing.Sequence[builtins.str],
        vpc_id: builtins.str,
    ) -> None:
        '''
        :param security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#security_group_ids CodebuildProject#security_group_ids}.
        :param subnets: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#subnets CodebuildProject#subnets}.
        :param vpc_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#vpc_id CodebuildProject#vpc_id}.
        '''
        if __debug__:
            def stub(
                *,
                security_group_ids: typing.Sequence[builtins.str],
                subnets: typing.Sequence[builtins.str],
                vpc_id: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
            check_type(argname="argument subnets", value=subnets, expected_type=type_hints["subnets"])
            check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "security_group_ids": security_group_ids,
            "subnets": subnets,
            "vpc_id": vpc_id,
        }

    @builtins.property
    def security_group_ids(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#security_group_ids CodebuildProject#security_group_ids}.'''
        result = self._values.get("security_group_ids")
        assert result is not None, "Required property 'security_group_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def subnets(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#subnets CodebuildProject#subnets}.'''
        result = self._values.get("subnets")
        assert result is not None, "Required property 'subnets' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def vpc_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codebuild_project#vpc_id CodebuildProject#vpc_id}.'''
        result = self._values.get("vpc_id")
        assert result is not None, "Required property 'vpc_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodebuildProjectVpcConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodebuildProjectVpcConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.codebuildProject.CodebuildProjectVpcConfigOutputReference",
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
    @jsii.member(jsii_name="securityGroupIdsInput")
    def security_group_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetsInput")
    def subnets_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "subnetsInput"))

    @builtins.property
    @jsii.member(jsii_name="vpcIdInput")
    def vpc_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vpcIdInput"))

    @builtins.property
    @jsii.member(jsii_name="securityGroupIds")
    def security_group_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityGroupIds"))

    @security_group_ids.setter
    def security_group_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroupIds", value)

    @builtins.property
    @jsii.member(jsii_name="subnets")
    def subnets(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnets"))

    @subnets.setter
    def subnets(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnets", value)

    @builtins.property
    @jsii.member(jsii_name="vpcId")
    def vpc_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpcId"))

    @vpc_id.setter
    def vpc_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CodebuildProjectVpcConfig]:
        return typing.cast(typing.Optional[CodebuildProjectVpcConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[CodebuildProjectVpcConfig]) -> None:
        if __debug__:
            def stub(value: typing.Optional[CodebuildProjectVpcConfig]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "CodebuildProject",
    "CodebuildProjectArtifacts",
    "CodebuildProjectArtifactsOutputReference",
    "CodebuildProjectBuildBatchConfig",
    "CodebuildProjectBuildBatchConfigOutputReference",
    "CodebuildProjectBuildBatchConfigRestrictions",
    "CodebuildProjectBuildBatchConfigRestrictionsOutputReference",
    "CodebuildProjectCache",
    "CodebuildProjectCacheOutputReference",
    "CodebuildProjectConfig",
    "CodebuildProjectEnvironment",
    "CodebuildProjectEnvironmentEnvironmentVariable",
    "CodebuildProjectEnvironmentEnvironmentVariableList",
    "CodebuildProjectEnvironmentEnvironmentVariableOutputReference",
    "CodebuildProjectEnvironmentOutputReference",
    "CodebuildProjectEnvironmentRegistryCredential",
    "CodebuildProjectEnvironmentRegistryCredentialOutputReference",
    "CodebuildProjectFileSystemLocations",
    "CodebuildProjectFileSystemLocationsList",
    "CodebuildProjectFileSystemLocationsOutputReference",
    "CodebuildProjectLogsConfig",
    "CodebuildProjectLogsConfigCloudwatchLogs",
    "CodebuildProjectLogsConfigCloudwatchLogsOutputReference",
    "CodebuildProjectLogsConfigOutputReference",
    "CodebuildProjectLogsConfigS3Logs",
    "CodebuildProjectLogsConfigS3LogsOutputReference",
    "CodebuildProjectSecondaryArtifacts",
    "CodebuildProjectSecondaryArtifactsList",
    "CodebuildProjectSecondaryArtifactsOutputReference",
    "CodebuildProjectSecondarySourceVersion",
    "CodebuildProjectSecondarySourceVersionList",
    "CodebuildProjectSecondarySourceVersionOutputReference",
    "CodebuildProjectSecondarySources",
    "CodebuildProjectSecondarySourcesAuth",
    "CodebuildProjectSecondarySourcesAuthOutputReference",
    "CodebuildProjectSecondarySourcesBuildStatusConfig",
    "CodebuildProjectSecondarySourcesBuildStatusConfigOutputReference",
    "CodebuildProjectSecondarySourcesGitSubmodulesConfig",
    "CodebuildProjectSecondarySourcesGitSubmodulesConfigOutputReference",
    "CodebuildProjectSecondarySourcesList",
    "CodebuildProjectSecondarySourcesOutputReference",
    "CodebuildProjectSource",
    "CodebuildProjectSourceAuth",
    "CodebuildProjectSourceAuthOutputReference",
    "CodebuildProjectSourceBuildStatusConfig",
    "CodebuildProjectSourceBuildStatusConfigOutputReference",
    "CodebuildProjectSourceGitSubmodulesConfig",
    "CodebuildProjectSourceGitSubmodulesConfigOutputReference",
    "CodebuildProjectSourceOutputReference",
    "CodebuildProjectVpcConfig",
    "CodebuildProjectVpcConfigOutputReference",
]

publication.publish()
