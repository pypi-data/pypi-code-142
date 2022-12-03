'''
# `aws_opsworks_stack`

Refer to the Terraform Registory for docs: [`aws_opsworks_stack`](https://www.terraform.io/docs/providers/aws/r/opsworks_stack).
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


class OpsworksStack(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.opsworksStack.OpsworksStack",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack aws_opsworks_stack}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        default_instance_profile_arn: builtins.str,
        name: builtins.str,
        region: builtins.str,
        service_role_arn: builtins.str,
        agent_version: typing.Optional[builtins.str] = None,
        berkshelf_version: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        configuration_manager_name: typing.Optional[builtins.str] = None,
        configuration_manager_version: typing.Optional[builtins.str] = None,
        custom_cookbooks_source: typing.Optional[typing.Union["OpsworksStackCustomCookbooksSource", typing.Dict[str, typing.Any]]] = None,
        custom_json: typing.Optional[builtins.str] = None,
        default_availability_zone: typing.Optional[builtins.str] = None,
        default_os: typing.Optional[builtins.str] = None,
        default_root_device_type: typing.Optional[builtins.str] = None,
        default_ssh_key_name: typing.Optional[builtins.str] = None,
        default_subnet_id: typing.Optional[builtins.str] = None,
        hostname_theme: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        manage_berkshelf: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["OpsworksStackTimeouts", typing.Dict[str, typing.Any]]] = None,
        use_custom_cookbooks: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        use_opsworks_security_groups: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        vpc_id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack aws_opsworks_stack} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param default_instance_profile_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#default_instance_profile_arn OpsworksStack#default_instance_profile_arn}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#name OpsworksStack#name}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#region OpsworksStack#region}.
        :param service_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#service_role_arn OpsworksStack#service_role_arn}.
        :param agent_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#agent_version OpsworksStack#agent_version}.
        :param berkshelf_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#berkshelf_version OpsworksStack#berkshelf_version}.
        :param color: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#color OpsworksStack#color}.
        :param configuration_manager_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#configuration_manager_name OpsworksStack#configuration_manager_name}.
        :param configuration_manager_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#configuration_manager_version OpsworksStack#configuration_manager_version}.
        :param custom_cookbooks_source: custom_cookbooks_source block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#custom_cookbooks_source OpsworksStack#custom_cookbooks_source}
        :param custom_json: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#custom_json OpsworksStack#custom_json}.
        :param default_availability_zone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#default_availability_zone OpsworksStack#default_availability_zone}.
        :param default_os: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#default_os OpsworksStack#default_os}.
        :param default_root_device_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#default_root_device_type OpsworksStack#default_root_device_type}.
        :param default_ssh_key_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#default_ssh_key_name OpsworksStack#default_ssh_key_name}.
        :param default_subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#default_subnet_id OpsworksStack#default_subnet_id}.
        :param hostname_theme: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#hostname_theme OpsworksStack#hostname_theme}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#id OpsworksStack#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param manage_berkshelf: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#manage_berkshelf OpsworksStack#manage_berkshelf}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#tags OpsworksStack#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#tags_all OpsworksStack#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#timeouts OpsworksStack#timeouts}
        :param use_custom_cookbooks: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#use_custom_cookbooks OpsworksStack#use_custom_cookbooks}.
        :param use_opsworks_security_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#use_opsworks_security_groups OpsworksStack#use_opsworks_security_groups}.
        :param vpc_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#vpc_id OpsworksStack#vpc_id}.
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
                default_instance_profile_arn: builtins.str,
                name: builtins.str,
                region: builtins.str,
                service_role_arn: builtins.str,
                agent_version: typing.Optional[builtins.str] = None,
                berkshelf_version: typing.Optional[builtins.str] = None,
                color: typing.Optional[builtins.str] = None,
                configuration_manager_name: typing.Optional[builtins.str] = None,
                configuration_manager_version: typing.Optional[builtins.str] = None,
                custom_cookbooks_source: typing.Optional[typing.Union[OpsworksStackCustomCookbooksSource, typing.Dict[str, typing.Any]]] = None,
                custom_json: typing.Optional[builtins.str] = None,
                default_availability_zone: typing.Optional[builtins.str] = None,
                default_os: typing.Optional[builtins.str] = None,
                default_root_device_type: typing.Optional[builtins.str] = None,
                default_ssh_key_name: typing.Optional[builtins.str] = None,
                default_subnet_id: typing.Optional[builtins.str] = None,
                hostname_theme: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                manage_berkshelf: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                timeouts: typing.Optional[typing.Union[OpsworksStackTimeouts, typing.Dict[str, typing.Any]]] = None,
                use_custom_cookbooks: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                use_opsworks_security_groups: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                vpc_id: typing.Optional[builtins.str] = None,
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
        config = OpsworksStackConfig(
            default_instance_profile_arn=default_instance_profile_arn,
            name=name,
            region=region,
            service_role_arn=service_role_arn,
            agent_version=agent_version,
            berkshelf_version=berkshelf_version,
            color=color,
            configuration_manager_name=configuration_manager_name,
            configuration_manager_version=configuration_manager_version,
            custom_cookbooks_source=custom_cookbooks_source,
            custom_json=custom_json,
            default_availability_zone=default_availability_zone,
            default_os=default_os,
            default_root_device_type=default_root_device_type,
            default_ssh_key_name=default_ssh_key_name,
            default_subnet_id=default_subnet_id,
            hostname_theme=hostname_theme,
            id=id,
            manage_berkshelf=manage_berkshelf,
            tags=tags,
            tags_all=tags_all,
            timeouts=timeouts,
            use_custom_cookbooks=use_custom_cookbooks,
            use_opsworks_security_groups=use_opsworks_security_groups,
            vpc_id=vpc_id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putCustomCookbooksSource")
    def put_custom_cookbooks_source(
        self,
        *,
        type: builtins.str,
        url: builtins.str,
        password: typing.Optional[builtins.str] = None,
        revision: typing.Optional[builtins.str] = None,
        ssh_key: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#type OpsworksStack#type}.
        :param url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#url OpsworksStack#url}.
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#password OpsworksStack#password}.
        :param revision: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#revision OpsworksStack#revision}.
        :param ssh_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#ssh_key OpsworksStack#ssh_key}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#username OpsworksStack#username}.
        '''
        value = OpsworksStackCustomCookbooksSource(
            type=type,
            url=url,
            password=password,
            revision=revision,
            ssh_key=ssh_key,
            username=username,
        )

        return typing.cast(None, jsii.invoke(self, "putCustomCookbooksSource", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(self, *, create: typing.Optional[builtins.str] = None) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#create OpsworksStack#create}.
        '''
        value = OpsworksStackTimeouts(create=create)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAgentVersion")
    def reset_agent_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAgentVersion", []))

    @jsii.member(jsii_name="resetBerkshelfVersion")
    def reset_berkshelf_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBerkshelfVersion", []))

    @jsii.member(jsii_name="resetColor")
    def reset_color(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetColor", []))

    @jsii.member(jsii_name="resetConfigurationManagerName")
    def reset_configuration_manager_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfigurationManagerName", []))

    @jsii.member(jsii_name="resetConfigurationManagerVersion")
    def reset_configuration_manager_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfigurationManagerVersion", []))

    @jsii.member(jsii_name="resetCustomCookbooksSource")
    def reset_custom_cookbooks_source(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomCookbooksSource", []))

    @jsii.member(jsii_name="resetCustomJson")
    def reset_custom_json(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomJson", []))

    @jsii.member(jsii_name="resetDefaultAvailabilityZone")
    def reset_default_availability_zone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultAvailabilityZone", []))

    @jsii.member(jsii_name="resetDefaultOs")
    def reset_default_os(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultOs", []))

    @jsii.member(jsii_name="resetDefaultRootDeviceType")
    def reset_default_root_device_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultRootDeviceType", []))

    @jsii.member(jsii_name="resetDefaultSshKeyName")
    def reset_default_ssh_key_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultSshKeyName", []))

    @jsii.member(jsii_name="resetDefaultSubnetId")
    def reset_default_subnet_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultSubnetId", []))

    @jsii.member(jsii_name="resetHostnameTheme")
    def reset_hostname_theme(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostnameTheme", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetManageBerkshelf")
    def reset_manage_berkshelf(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManageBerkshelf", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetUseCustomCookbooks")
    def reset_use_custom_cookbooks(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseCustomCookbooks", []))

    @jsii.member(jsii_name="resetUseOpsworksSecurityGroups")
    def reset_use_opsworks_security_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseOpsworksSecurityGroups", []))

    @jsii.member(jsii_name="resetVpcId")
    def reset_vpc_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVpcId", []))

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
    @jsii.member(jsii_name="customCookbooksSource")
    def custom_cookbooks_source(
        self,
    ) -> "OpsworksStackCustomCookbooksSourceOutputReference":
        return typing.cast("OpsworksStackCustomCookbooksSourceOutputReference", jsii.get(self, "customCookbooksSource"))

    @builtins.property
    @jsii.member(jsii_name="stackEndpoint")
    def stack_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stackEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "OpsworksStackTimeoutsOutputReference":
        return typing.cast("OpsworksStackTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="agentVersionInput")
    def agent_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "agentVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="berkshelfVersionInput")
    def berkshelf_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "berkshelfVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="colorInput")
    def color_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "colorInput"))

    @builtins.property
    @jsii.member(jsii_name="configurationManagerNameInput")
    def configuration_manager_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "configurationManagerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="configurationManagerVersionInput")
    def configuration_manager_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "configurationManagerVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="customCookbooksSourceInput")
    def custom_cookbooks_source_input(
        self,
    ) -> typing.Optional["OpsworksStackCustomCookbooksSource"]:
        return typing.cast(typing.Optional["OpsworksStackCustomCookbooksSource"], jsii.get(self, "customCookbooksSourceInput"))

    @builtins.property
    @jsii.member(jsii_name="customJsonInput")
    def custom_json_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customJsonInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultAvailabilityZoneInput")
    def default_availability_zone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultAvailabilityZoneInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultInstanceProfileArnInput")
    def default_instance_profile_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultInstanceProfileArnInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultOsInput")
    def default_os_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultOsInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultRootDeviceTypeInput")
    def default_root_device_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultRootDeviceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultSshKeyNameInput")
    def default_ssh_key_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultSshKeyNameInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultSubnetIdInput")
    def default_subnet_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultSubnetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="hostnameThemeInput")
    def hostname_theme_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostnameThemeInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="manageBerkshelfInput")
    def manage_berkshelf_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "manageBerkshelfInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceRoleArnInput")
    def service_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceRoleArnInput"))

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
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["OpsworksStackTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["OpsworksStackTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="useCustomCookbooksInput")
    def use_custom_cookbooks_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "useCustomCookbooksInput"))

    @builtins.property
    @jsii.member(jsii_name="useOpsworksSecurityGroupsInput")
    def use_opsworks_security_groups_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "useOpsworksSecurityGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="vpcIdInput")
    def vpc_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vpcIdInput"))

    @builtins.property
    @jsii.member(jsii_name="agentVersion")
    def agent_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "agentVersion"))

    @agent_version.setter
    def agent_version(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "agentVersion", value)

    @builtins.property
    @jsii.member(jsii_name="berkshelfVersion")
    def berkshelf_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "berkshelfVersion"))

    @berkshelf_version.setter
    def berkshelf_version(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "berkshelfVersion", value)

    @builtins.property
    @jsii.member(jsii_name="color")
    def color(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "color"))

    @color.setter
    def color(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "color", value)

    @builtins.property
    @jsii.member(jsii_name="configurationManagerName")
    def configuration_manager_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "configurationManagerName"))

    @configuration_manager_name.setter
    def configuration_manager_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configurationManagerName", value)

    @builtins.property
    @jsii.member(jsii_name="configurationManagerVersion")
    def configuration_manager_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "configurationManagerVersion"))

    @configuration_manager_version.setter
    def configuration_manager_version(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configurationManagerVersion", value)

    @builtins.property
    @jsii.member(jsii_name="customJson")
    def custom_json(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customJson"))

    @custom_json.setter
    def custom_json(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customJson", value)

    @builtins.property
    @jsii.member(jsii_name="defaultAvailabilityZone")
    def default_availability_zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultAvailabilityZone"))

    @default_availability_zone.setter
    def default_availability_zone(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultAvailabilityZone", value)

    @builtins.property
    @jsii.member(jsii_name="defaultInstanceProfileArn")
    def default_instance_profile_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultInstanceProfileArn"))

    @default_instance_profile_arn.setter
    def default_instance_profile_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultInstanceProfileArn", value)

    @builtins.property
    @jsii.member(jsii_name="defaultOs")
    def default_os(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultOs"))

    @default_os.setter
    def default_os(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultOs", value)

    @builtins.property
    @jsii.member(jsii_name="defaultRootDeviceType")
    def default_root_device_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultRootDeviceType"))

    @default_root_device_type.setter
    def default_root_device_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultRootDeviceType", value)

    @builtins.property
    @jsii.member(jsii_name="defaultSshKeyName")
    def default_ssh_key_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultSshKeyName"))

    @default_ssh_key_name.setter
    def default_ssh_key_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultSshKeyName", value)

    @builtins.property
    @jsii.member(jsii_name="defaultSubnetId")
    def default_subnet_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultSubnetId"))

    @default_subnet_id.setter
    def default_subnet_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultSubnetId", value)

    @builtins.property
    @jsii.member(jsii_name="hostnameTheme")
    def hostname_theme(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostnameTheme"))

    @hostname_theme.setter
    def hostname_theme(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostnameTheme", value)

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
    @jsii.member(jsii_name="manageBerkshelf")
    def manage_berkshelf(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "manageBerkshelf"))

    @manage_berkshelf.setter
    def manage_berkshelf(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "manageBerkshelf", value)

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
    @jsii.member(jsii_name="useCustomCookbooks")
    def use_custom_cookbooks(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "useCustomCookbooks"))

    @use_custom_cookbooks.setter
    def use_custom_cookbooks(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useCustomCookbooks", value)

    @builtins.property
    @jsii.member(jsii_name="useOpsworksSecurityGroups")
    def use_opsworks_security_groups(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "useOpsworksSecurityGroups"))

    @use_opsworks_security_groups.setter
    def use_opsworks_security_groups(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useOpsworksSecurityGroups", value)

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


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.opsworksStack.OpsworksStackConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "default_instance_profile_arn": "defaultInstanceProfileArn",
        "name": "name",
        "region": "region",
        "service_role_arn": "serviceRoleArn",
        "agent_version": "agentVersion",
        "berkshelf_version": "berkshelfVersion",
        "color": "color",
        "configuration_manager_name": "configurationManagerName",
        "configuration_manager_version": "configurationManagerVersion",
        "custom_cookbooks_source": "customCookbooksSource",
        "custom_json": "customJson",
        "default_availability_zone": "defaultAvailabilityZone",
        "default_os": "defaultOs",
        "default_root_device_type": "defaultRootDeviceType",
        "default_ssh_key_name": "defaultSshKeyName",
        "default_subnet_id": "defaultSubnetId",
        "hostname_theme": "hostnameTheme",
        "id": "id",
        "manage_berkshelf": "manageBerkshelf",
        "tags": "tags",
        "tags_all": "tagsAll",
        "timeouts": "timeouts",
        "use_custom_cookbooks": "useCustomCookbooks",
        "use_opsworks_security_groups": "useOpsworksSecurityGroups",
        "vpc_id": "vpcId",
    },
)
class OpsworksStackConfig(cdktf.TerraformMetaArguments):
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
        default_instance_profile_arn: builtins.str,
        name: builtins.str,
        region: builtins.str,
        service_role_arn: builtins.str,
        agent_version: typing.Optional[builtins.str] = None,
        berkshelf_version: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        configuration_manager_name: typing.Optional[builtins.str] = None,
        configuration_manager_version: typing.Optional[builtins.str] = None,
        custom_cookbooks_source: typing.Optional[typing.Union["OpsworksStackCustomCookbooksSource", typing.Dict[str, typing.Any]]] = None,
        custom_json: typing.Optional[builtins.str] = None,
        default_availability_zone: typing.Optional[builtins.str] = None,
        default_os: typing.Optional[builtins.str] = None,
        default_root_device_type: typing.Optional[builtins.str] = None,
        default_ssh_key_name: typing.Optional[builtins.str] = None,
        default_subnet_id: typing.Optional[builtins.str] = None,
        hostname_theme: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        manage_berkshelf: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["OpsworksStackTimeouts", typing.Dict[str, typing.Any]]] = None,
        use_custom_cookbooks: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        use_opsworks_security_groups: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        vpc_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param default_instance_profile_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#default_instance_profile_arn OpsworksStack#default_instance_profile_arn}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#name OpsworksStack#name}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#region OpsworksStack#region}.
        :param service_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#service_role_arn OpsworksStack#service_role_arn}.
        :param agent_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#agent_version OpsworksStack#agent_version}.
        :param berkshelf_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#berkshelf_version OpsworksStack#berkshelf_version}.
        :param color: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#color OpsworksStack#color}.
        :param configuration_manager_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#configuration_manager_name OpsworksStack#configuration_manager_name}.
        :param configuration_manager_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#configuration_manager_version OpsworksStack#configuration_manager_version}.
        :param custom_cookbooks_source: custom_cookbooks_source block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#custom_cookbooks_source OpsworksStack#custom_cookbooks_source}
        :param custom_json: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#custom_json OpsworksStack#custom_json}.
        :param default_availability_zone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#default_availability_zone OpsworksStack#default_availability_zone}.
        :param default_os: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#default_os OpsworksStack#default_os}.
        :param default_root_device_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#default_root_device_type OpsworksStack#default_root_device_type}.
        :param default_ssh_key_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#default_ssh_key_name OpsworksStack#default_ssh_key_name}.
        :param default_subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#default_subnet_id OpsworksStack#default_subnet_id}.
        :param hostname_theme: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#hostname_theme OpsworksStack#hostname_theme}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#id OpsworksStack#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param manage_berkshelf: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#manage_berkshelf OpsworksStack#manage_berkshelf}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#tags OpsworksStack#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#tags_all OpsworksStack#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#timeouts OpsworksStack#timeouts}
        :param use_custom_cookbooks: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#use_custom_cookbooks OpsworksStack#use_custom_cookbooks}.
        :param use_opsworks_security_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#use_opsworks_security_groups OpsworksStack#use_opsworks_security_groups}.
        :param vpc_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#vpc_id OpsworksStack#vpc_id}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(custom_cookbooks_source, dict):
            custom_cookbooks_source = OpsworksStackCustomCookbooksSource(**custom_cookbooks_source)
        if isinstance(timeouts, dict):
            timeouts = OpsworksStackTimeouts(**timeouts)
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
                default_instance_profile_arn: builtins.str,
                name: builtins.str,
                region: builtins.str,
                service_role_arn: builtins.str,
                agent_version: typing.Optional[builtins.str] = None,
                berkshelf_version: typing.Optional[builtins.str] = None,
                color: typing.Optional[builtins.str] = None,
                configuration_manager_name: typing.Optional[builtins.str] = None,
                configuration_manager_version: typing.Optional[builtins.str] = None,
                custom_cookbooks_source: typing.Optional[typing.Union[OpsworksStackCustomCookbooksSource, typing.Dict[str, typing.Any]]] = None,
                custom_json: typing.Optional[builtins.str] = None,
                default_availability_zone: typing.Optional[builtins.str] = None,
                default_os: typing.Optional[builtins.str] = None,
                default_root_device_type: typing.Optional[builtins.str] = None,
                default_ssh_key_name: typing.Optional[builtins.str] = None,
                default_subnet_id: typing.Optional[builtins.str] = None,
                hostname_theme: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                manage_berkshelf: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                timeouts: typing.Optional[typing.Union[OpsworksStackTimeouts, typing.Dict[str, typing.Any]]] = None,
                use_custom_cookbooks: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                use_opsworks_security_groups: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                vpc_id: typing.Optional[builtins.str] = None,
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
            check_type(argname="argument default_instance_profile_arn", value=default_instance_profile_arn, expected_type=type_hints["default_instance_profile_arn"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument service_role_arn", value=service_role_arn, expected_type=type_hints["service_role_arn"])
            check_type(argname="argument agent_version", value=agent_version, expected_type=type_hints["agent_version"])
            check_type(argname="argument berkshelf_version", value=berkshelf_version, expected_type=type_hints["berkshelf_version"])
            check_type(argname="argument color", value=color, expected_type=type_hints["color"])
            check_type(argname="argument configuration_manager_name", value=configuration_manager_name, expected_type=type_hints["configuration_manager_name"])
            check_type(argname="argument configuration_manager_version", value=configuration_manager_version, expected_type=type_hints["configuration_manager_version"])
            check_type(argname="argument custom_cookbooks_source", value=custom_cookbooks_source, expected_type=type_hints["custom_cookbooks_source"])
            check_type(argname="argument custom_json", value=custom_json, expected_type=type_hints["custom_json"])
            check_type(argname="argument default_availability_zone", value=default_availability_zone, expected_type=type_hints["default_availability_zone"])
            check_type(argname="argument default_os", value=default_os, expected_type=type_hints["default_os"])
            check_type(argname="argument default_root_device_type", value=default_root_device_type, expected_type=type_hints["default_root_device_type"])
            check_type(argname="argument default_ssh_key_name", value=default_ssh_key_name, expected_type=type_hints["default_ssh_key_name"])
            check_type(argname="argument default_subnet_id", value=default_subnet_id, expected_type=type_hints["default_subnet_id"])
            check_type(argname="argument hostname_theme", value=hostname_theme, expected_type=type_hints["hostname_theme"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument manage_berkshelf", value=manage_berkshelf, expected_type=type_hints["manage_berkshelf"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument use_custom_cookbooks", value=use_custom_cookbooks, expected_type=type_hints["use_custom_cookbooks"])
            check_type(argname="argument use_opsworks_security_groups", value=use_opsworks_security_groups, expected_type=type_hints["use_opsworks_security_groups"])
            check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "default_instance_profile_arn": default_instance_profile_arn,
            "name": name,
            "region": region,
            "service_role_arn": service_role_arn,
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
        if agent_version is not None:
            self._values["agent_version"] = agent_version
        if berkshelf_version is not None:
            self._values["berkshelf_version"] = berkshelf_version
        if color is not None:
            self._values["color"] = color
        if configuration_manager_name is not None:
            self._values["configuration_manager_name"] = configuration_manager_name
        if configuration_manager_version is not None:
            self._values["configuration_manager_version"] = configuration_manager_version
        if custom_cookbooks_source is not None:
            self._values["custom_cookbooks_source"] = custom_cookbooks_source
        if custom_json is not None:
            self._values["custom_json"] = custom_json
        if default_availability_zone is not None:
            self._values["default_availability_zone"] = default_availability_zone
        if default_os is not None:
            self._values["default_os"] = default_os
        if default_root_device_type is not None:
            self._values["default_root_device_type"] = default_root_device_type
        if default_ssh_key_name is not None:
            self._values["default_ssh_key_name"] = default_ssh_key_name
        if default_subnet_id is not None:
            self._values["default_subnet_id"] = default_subnet_id
        if hostname_theme is not None:
            self._values["hostname_theme"] = hostname_theme
        if id is not None:
            self._values["id"] = id
        if manage_berkshelf is not None:
            self._values["manage_berkshelf"] = manage_berkshelf
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if use_custom_cookbooks is not None:
            self._values["use_custom_cookbooks"] = use_custom_cookbooks
        if use_opsworks_security_groups is not None:
            self._values["use_opsworks_security_groups"] = use_opsworks_security_groups
        if vpc_id is not None:
            self._values["vpc_id"] = vpc_id

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
    def default_instance_profile_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#default_instance_profile_arn OpsworksStack#default_instance_profile_arn}.'''
        result = self._values.get("default_instance_profile_arn")
        assert result is not None, "Required property 'default_instance_profile_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#name OpsworksStack#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def region(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#region OpsworksStack#region}.'''
        result = self._values.get("region")
        assert result is not None, "Required property 'region' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#service_role_arn OpsworksStack#service_role_arn}.'''
        result = self._values.get("service_role_arn")
        assert result is not None, "Required property 'service_role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def agent_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#agent_version OpsworksStack#agent_version}.'''
        result = self._values.get("agent_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def berkshelf_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#berkshelf_version OpsworksStack#berkshelf_version}.'''
        result = self._values.get("berkshelf_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def color(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#color OpsworksStack#color}.'''
        result = self._values.get("color")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def configuration_manager_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#configuration_manager_name OpsworksStack#configuration_manager_name}.'''
        result = self._values.get("configuration_manager_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def configuration_manager_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#configuration_manager_version OpsworksStack#configuration_manager_version}.'''
        result = self._values.get("configuration_manager_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_cookbooks_source(
        self,
    ) -> typing.Optional["OpsworksStackCustomCookbooksSource"]:
        '''custom_cookbooks_source block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#custom_cookbooks_source OpsworksStack#custom_cookbooks_source}
        '''
        result = self._values.get("custom_cookbooks_source")
        return typing.cast(typing.Optional["OpsworksStackCustomCookbooksSource"], result)

    @builtins.property
    def custom_json(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#custom_json OpsworksStack#custom_json}.'''
        result = self._values.get("custom_json")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_availability_zone(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#default_availability_zone OpsworksStack#default_availability_zone}.'''
        result = self._values.get("default_availability_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_os(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#default_os OpsworksStack#default_os}.'''
        result = self._values.get("default_os")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_root_device_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#default_root_device_type OpsworksStack#default_root_device_type}.'''
        result = self._values.get("default_root_device_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_ssh_key_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#default_ssh_key_name OpsworksStack#default_ssh_key_name}.'''
        result = self._values.get("default_ssh_key_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_subnet_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#default_subnet_id OpsworksStack#default_subnet_id}.'''
        result = self._values.get("default_subnet_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def hostname_theme(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#hostname_theme OpsworksStack#hostname_theme}.'''
        result = self._values.get("hostname_theme")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#id OpsworksStack#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def manage_berkshelf(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#manage_berkshelf OpsworksStack#manage_berkshelf}.'''
        result = self._values.get("manage_berkshelf")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#tags OpsworksStack#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#tags_all OpsworksStack#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["OpsworksStackTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#timeouts OpsworksStack#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["OpsworksStackTimeouts"], result)

    @builtins.property
    def use_custom_cookbooks(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#use_custom_cookbooks OpsworksStack#use_custom_cookbooks}.'''
        result = self._values.get("use_custom_cookbooks")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def use_opsworks_security_groups(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#use_opsworks_security_groups OpsworksStack#use_opsworks_security_groups}.'''
        result = self._values.get("use_opsworks_security_groups")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def vpc_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#vpc_id OpsworksStack#vpc_id}.'''
        result = self._values.get("vpc_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpsworksStackConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.opsworksStack.OpsworksStackCustomCookbooksSource",
    jsii_struct_bases=[],
    name_mapping={
        "type": "type",
        "url": "url",
        "password": "password",
        "revision": "revision",
        "ssh_key": "sshKey",
        "username": "username",
    },
)
class OpsworksStackCustomCookbooksSource:
    def __init__(
        self,
        *,
        type: builtins.str,
        url: builtins.str,
        password: typing.Optional[builtins.str] = None,
        revision: typing.Optional[builtins.str] = None,
        ssh_key: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#type OpsworksStack#type}.
        :param url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#url OpsworksStack#url}.
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#password OpsworksStack#password}.
        :param revision: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#revision OpsworksStack#revision}.
        :param ssh_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#ssh_key OpsworksStack#ssh_key}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#username OpsworksStack#username}.
        '''
        if __debug__:
            def stub(
                *,
                type: builtins.str,
                url: builtins.str,
                password: typing.Optional[builtins.str] = None,
                revision: typing.Optional[builtins.str] = None,
                ssh_key: typing.Optional[builtins.str] = None,
                username: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument revision", value=revision, expected_type=type_hints["revision"])
            check_type(argname="argument ssh_key", value=ssh_key, expected_type=type_hints["ssh_key"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
            "url": url,
        }
        if password is not None:
            self._values["password"] = password
        if revision is not None:
            self._values["revision"] = revision
        if ssh_key is not None:
            self._values["ssh_key"] = ssh_key
        if username is not None:
            self._values["username"] = username

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#type OpsworksStack#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#url OpsworksStack#url}.'''
        result = self._values.get("url")
        assert result is not None, "Required property 'url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#password OpsworksStack#password}.'''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def revision(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#revision OpsworksStack#revision}.'''
        result = self._values.get("revision")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ssh_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#ssh_key OpsworksStack#ssh_key}.'''
        result = self._values.get("ssh_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#username OpsworksStack#username}.'''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpsworksStackCustomCookbooksSource(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OpsworksStackCustomCookbooksSourceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.opsworksStack.OpsworksStackCustomCookbooksSourceOutputReference",
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

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @jsii.member(jsii_name="resetRevision")
    def reset_revision(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRevision", []))

    @jsii.member(jsii_name="resetSshKey")
    def reset_ssh_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSshKey", []))

    @jsii.member(jsii_name="resetUsername")
    def reset_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsername", []))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="revisionInput")
    def revision_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "revisionInput"))

    @builtins.property
    @jsii.member(jsii_name="sshKeyInput")
    def ssh_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sshKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="urlInput")
    def url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="revision")
    def revision(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "revision"))

    @revision.setter
    def revision(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "revision", value)

    @builtins.property
    @jsii.member(jsii_name="sshKey")
    def ssh_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sshKey"))

    @ssh_key.setter
    def ssh_key(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sshKey", value)

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
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[OpsworksStackCustomCookbooksSource]:
        return typing.cast(typing.Optional[OpsworksStackCustomCookbooksSource], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OpsworksStackCustomCookbooksSource],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[OpsworksStackCustomCookbooksSource],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.opsworksStack.OpsworksStackTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create"},
)
class OpsworksStackTimeouts:
    def __init__(self, *, create: typing.Optional[builtins.str] = None) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#create OpsworksStack#create}.
        '''
        if __debug__:
            def stub(*, create: typing.Optional[builtins.str] = None) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opsworks_stack#create OpsworksStack#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpsworksStackTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OpsworksStackTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.opsworksStack.OpsworksStackTimeoutsOutputReference",
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

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OpsworksStackTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OpsworksStackTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OpsworksStackTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[OpsworksStackTimeouts, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "OpsworksStack",
    "OpsworksStackConfig",
    "OpsworksStackCustomCookbooksSource",
    "OpsworksStackCustomCookbooksSourceOutputReference",
    "OpsworksStackTimeouts",
    "OpsworksStackTimeoutsOutputReference",
]

publication.publish()
