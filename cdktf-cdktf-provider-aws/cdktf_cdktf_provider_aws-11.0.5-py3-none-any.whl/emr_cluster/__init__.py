'''
# `aws_emr_cluster`

Refer to the Terraform Registory for docs: [`aws_emr_cluster`](https://www.terraform.io/docs/providers/aws/r/emr_cluster).
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


class EmrCluster(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.emrCluster.EmrCluster",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster aws_emr_cluster}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        release_label: builtins.str,
        service_role: builtins.str,
        additional_info: typing.Optional[builtins.str] = None,
        applications: typing.Optional[typing.Sequence[builtins.str]] = None,
        autoscaling_role: typing.Optional[builtins.str] = None,
        auto_termination_policy: typing.Optional[typing.Union["EmrClusterAutoTerminationPolicy", typing.Dict[str, typing.Any]]] = None,
        bootstrap_action: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EmrClusterBootstrapAction", typing.Dict[str, typing.Any]]]]] = None,
        configurations: typing.Optional[builtins.str] = None,
        configurations_json: typing.Optional[builtins.str] = None,
        core_instance_fleet: typing.Optional[typing.Union["EmrClusterCoreInstanceFleet", typing.Dict[str, typing.Any]]] = None,
        core_instance_group: typing.Optional[typing.Union["EmrClusterCoreInstanceGroup", typing.Dict[str, typing.Any]]] = None,
        custom_ami_id: typing.Optional[builtins.str] = None,
        ebs_root_volume_size: typing.Optional[jsii.Number] = None,
        ec2_attributes: typing.Optional[typing.Union["EmrClusterEc2Attributes", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        keep_job_flow_alive_when_no_steps: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        kerberos_attributes: typing.Optional[typing.Union["EmrClusterKerberosAttributes", typing.Dict[str, typing.Any]]] = None,
        list_steps_states: typing.Optional[typing.Sequence[builtins.str]] = None,
        log_encryption_kms_key_id: typing.Optional[builtins.str] = None,
        log_uri: typing.Optional[builtins.str] = None,
        master_instance_fleet: typing.Optional[typing.Union["EmrClusterMasterInstanceFleet", typing.Dict[str, typing.Any]]] = None,
        master_instance_group: typing.Optional[typing.Union["EmrClusterMasterInstanceGroup", typing.Dict[str, typing.Any]]] = None,
        scale_down_behavior: typing.Optional[builtins.str] = None,
        security_configuration: typing.Optional[builtins.str] = None,
        step: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EmrClusterStep", typing.Dict[str, typing.Any]]]]] = None,
        step_concurrency_level: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        termination_protection: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        visible_to_all_users: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster aws_emr_cluster} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#name EmrCluster#name}.
        :param release_label: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#release_label EmrCluster#release_label}.
        :param service_role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#service_role EmrCluster#service_role}.
        :param additional_info: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#additional_info EmrCluster#additional_info}.
        :param applications: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#applications EmrCluster#applications}.
        :param autoscaling_role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#autoscaling_role EmrCluster#autoscaling_role}.
        :param auto_termination_policy: auto_termination_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#auto_termination_policy EmrCluster#auto_termination_policy}
        :param bootstrap_action: bootstrap_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#bootstrap_action EmrCluster#bootstrap_action}
        :param configurations: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#configurations EmrCluster#configurations}.
        :param configurations_json: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#configurations_json EmrCluster#configurations_json}.
        :param core_instance_fleet: core_instance_fleet block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#core_instance_fleet EmrCluster#core_instance_fleet}
        :param core_instance_group: core_instance_group block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#core_instance_group EmrCluster#core_instance_group}
        :param custom_ami_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#custom_ami_id EmrCluster#custom_ami_id}.
        :param ebs_root_volume_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#ebs_root_volume_size EmrCluster#ebs_root_volume_size}.
        :param ec2_attributes: ec2_attributes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#ec2_attributes EmrCluster#ec2_attributes}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#id EmrCluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param keep_job_flow_alive_when_no_steps: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#keep_job_flow_alive_when_no_steps EmrCluster#keep_job_flow_alive_when_no_steps}.
        :param kerberos_attributes: kerberos_attributes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#kerberos_attributes EmrCluster#kerberos_attributes}
        :param list_steps_states: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#list_steps_states EmrCluster#list_steps_states}.
        :param log_encryption_kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#log_encryption_kms_key_id EmrCluster#log_encryption_kms_key_id}.
        :param log_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#log_uri EmrCluster#log_uri}.
        :param master_instance_fleet: master_instance_fleet block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#master_instance_fleet EmrCluster#master_instance_fleet}
        :param master_instance_group: master_instance_group block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#master_instance_group EmrCluster#master_instance_group}
        :param scale_down_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#scale_down_behavior EmrCluster#scale_down_behavior}.
        :param security_configuration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#security_configuration EmrCluster#security_configuration}.
        :param step: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#step EmrCluster#step}.
        :param step_concurrency_level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#step_concurrency_level EmrCluster#step_concurrency_level}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#tags EmrCluster#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#tags_all EmrCluster#tags_all}.
        :param termination_protection: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#termination_protection EmrCluster#termination_protection}.
        :param visible_to_all_users: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#visible_to_all_users EmrCluster#visible_to_all_users}.
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
                name: builtins.str,
                release_label: builtins.str,
                service_role: builtins.str,
                additional_info: typing.Optional[builtins.str] = None,
                applications: typing.Optional[typing.Sequence[builtins.str]] = None,
                autoscaling_role: typing.Optional[builtins.str] = None,
                auto_termination_policy: typing.Optional[typing.Union[EmrClusterAutoTerminationPolicy, typing.Dict[str, typing.Any]]] = None,
                bootstrap_action: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EmrClusterBootstrapAction, typing.Dict[str, typing.Any]]]]] = None,
                configurations: typing.Optional[builtins.str] = None,
                configurations_json: typing.Optional[builtins.str] = None,
                core_instance_fleet: typing.Optional[typing.Union[EmrClusterCoreInstanceFleet, typing.Dict[str, typing.Any]]] = None,
                core_instance_group: typing.Optional[typing.Union[EmrClusterCoreInstanceGroup, typing.Dict[str, typing.Any]]] = None,
                custom_ami_id: typing.Optional[builtins.str] = None,
                ebs_root_volume_size: typing.Optional[jsii.Number] = None,
                ec2_attributes: typing.Optional[typing.Union[EmrClusterEc2Attributes, typing.Dict[str, typing.Any]]] = None,
                id: typing.Optional[builtins.str] = None,
                keep_job_flow_alive_when_no_steps: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                kerberos_attributes: typing.Optional[typing.Union[EmrClusterKerberosAttributes, typing.Dict[str, typing.Any]]] = None,
                list_steps_states: typing.Optional[typing.Sequence[builtins.str]] = None,
                log_encryption_kms_key_id: typing.Optional[builtins.str] = None,
                log_uri: typing.Optional[builtins.str] = None,
                master_instance_fleet: typing.Optional[typing.Union[EmrClusterMasterInstanceFleet, typing.Dict[str, typing.Any]]] = None,
                master_instance_group: typing.Optional[typing.Union[EmrClusterMasterInstanceGroup, typing.Dict[str, typing.Any]]] = None,
                scale_down_behavior: typing.Optional[builtins.str] = None,
                security_configuration: typing.Optional[builtins.str] = None,
                step: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EmrClusterStep, typing.Dict[str, typing.Any]]]]] = None,
                step_concurrency_level: typing.Optional[jsii.Number] = None,
                tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                termination_protection: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                visible_to_all_users: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
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
        config = EmrClusterConfig(
            name=name,
            release_label=release_label,
            service_role=service_role,
            additional_info=additional_info,
            applications=applications,
            autoscaling_role=autoscaling_role,
            auto_termination_policy=auto_termination_policy,
            bootstrap_action=bootstrap_action,
            configurations=configurations,
            configurations_json=configurations_json,
            core_instance_fleet=core_instance_fleet,
            core_instance_group=core_instance_group,
            custom_ami_id=custom_ami_id,
            ebs_root_volume_size=ebs_root_volume_size,
            ec2_attributes=ec2_attributes,
            id=id,
            keep_job_flow_alive_when_no_steps=keep_job_flow_alive_when_no_steps,
            kerberos_attributes=kerberos_attributes,
            list_steps_states=list_steps_states,
            log_encryption_kms_key_id=log_encryption_kms_key_id,
            log_uri=log_uri,
            master_instance_fleet=master_instance_fleet,
            master_instance_group=master_instance_group,
            scale_down_behavior=scale_down_behavior,
            security_configuration=security_configuration,
            step=step,
            step_concurrency_level=step_concurrency_level,
            tags=tags,
            tags_all=tags_all,
            termination_protection=termination_protection,
            visible_to_all_users=visible_to_all_users,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAutoTerminationPolicy")
    def put_auto_termination_policy(
        self,
        *,
        idle_timeout: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param idle_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#idle_timeout EmrCluster#idle_timeout}.
        '''
        value = EmrClusterAutoTerminationPolicy(idle_timeout=idle_timeout)

        return typing.cast(None, jsii.invoke(self, "putAutoTerminationPolicy", [value]))

    @jsii.member(jsii_name="putBootstrapAction")
    def put_bootstrap_action(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EmrClusterBootstrapAction", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EmrClusterBootstrapAction, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putBootstrapAction", [value]))

    @jsii.member(jsii_name="putCoreInstanceFleet")
    def put_core_instance_fleet(
        self,
        *,
        instance_type_configs: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EmrClusterCoreInstanceFleetInstanceTypeConfigs", typing.Dict[str, typing.Any]]]]] = None,
        launch_specifications: typing.Optional[typing.Union["EmrClusterCoreInstanceFleetLaunchSpecifications", typing.Dict[str, typing.Any]]] = None,
        name: typing.Optional[builtins.str] = None,
        target_on_demand_capacity: typing.Optional[jsii.Number] = None,
        target_spot_capacity: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param instance_type_configs: instance_type_configs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#instance_type_configs EmrCluster#instance_type_configs}
        :param launch_specifications: launch_specifications block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#launch_specifications EmrCluster#launch_specifications}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#name EmrCluster#name}.
        :param target_on_demand_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#target_on_demand_capacity EmrCluster#target_on_demand_capacity}.
        :param target_spot_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#target_spot_capacity EmrCluster#target_spot_capacity}.
        '''
        value = EmrClusterCoreInstanceFleet(
            instance_type_configs=instance_type_configs,
            launch_specifications=launch_specifications,
            name=name,
            target_on_demand_capacity=target_on_demand_capacity,
            target_spot_capacity=target_spot_capacity,
        )

        return typing.cast(None, jsii.invoke(self, "putCoreInstanceFleet", [value]))

    @jsii.member(jsii_name="putCoreInstanceGroup")
    def put_core_instance_group(
        self,
        *,
        instance_type: builtins.str,
        autoscaling_policy: typing.Optional[builtins.str] = None,
        bid_price: typing.Optional[builtins.str] = None,
        ebs_config: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EmrClusterCoreInstanceGroupEbsConfig", typing.Dict[str, typing.Any]]]]] = None,
        instance_count: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param instance_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#instance_type EmrCluster#instance_type}.
        :param autoscaling_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#autoscaling_policy EmrCluster#autoscaling_policy}.
        :param bid_price: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#bid_price EmrCluster#bid_price}.
        :param ebs_config: ebs_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#ebs_config EmrCluster#ebs_config}
        :param instance_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#instance_count EmrCluster#instance_count}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#name EmrCluster#name}.
        '''
        value = EmrClusterCoreInstanceGroup(
            instance_type=instance_type,
            autoscaling_policy=autoscaling_policy,
            bid_price=bid_price,
            ebs_config=ebs_config,
            instance_count=instance_count,
            name=name,
        )

        return typing.cast(None, jsii.invoke(self, "putCoreInstanceGroup", [value]))

    @jsii.member(jsii_name="putEc2Attributes")
    def put_ec2_attributes(
        self,
        *,
        instance_profile: builtins.str,
        additional_master_security_groups: typing.Optional[builtins.str] = None,
        additional_slave_security_groups: typing.Optional[builtins.str] = None,
        emr_managed_master_security_group: typing.Optional[builtins.str] = None,
        emr_managed_slave_security_group: typing.Optional[builtins.str] = None,
        key_name: typing.Optional[builtins.str] = None,
        service_access_security_group: typing.Optional[builtins.str] = None,
        subnet_id: typing.Optional[builtins.str] = None,
        subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param instance_profile: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#instance_profile EmrCluster#instance_profile}.
        :param additional_master_security_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#additional_master_security_groups EmrCluster#additional_master_security_groups}.
        :param additional_slave_security_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#additional_slave_security_groups EmrCluster#additional_slave_security_groups}.
        :param emr_managed_master_security_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#emr_managed_master_security_group EmrCluster#emr_managed_master_security_group}.
        :param emr_managed_slave_security_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#emr_managed_slave_security_group EmrCluster#emr_managed_slave_security_group}.
        :param key_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#key_name EmrCluster#key_name}.
        :param service_access_security_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#service_access_security_group EmrCluster#service_access_security_group}.
        :param subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#subnet_id EmrCluster#subnet_id}.
        :param subnet_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#subnet_ids EmrCluster#subnet_ids}.
        '''
        value = EmrClusterEc2Attributes(
            instance_profile=instance_profile,
            additional_master_security_groups=additional_master_security_groups,
            additional_slave_security_groups=additional_slave_security_groups,
            emr_managed_master_security_group=emr_managed_master_security_group,
            emr_managed_slave_security_group=emr_managed_slave_security_group,
            key_name=key_name,
            service_access_security_group=service_access_security_group,
            subnet_id=subnet_id,
            subnet_ids=subnet_ids,
        )

        return typing.cast(None, jsii.invoke(self, "putEc2Attributes", [value]))

    @jsii.member(jsii_name="putKerberosAttributes")
    def put_kerberos_attributes(
        self,
        *,
        kdc_admin_password: builtins.str,
        realm: builtins.str,
        ad_domain_join_password: typing.Optional[builtins.str] = None,
        ad_domain_join_user: typing.Optional[builtins.str] = None,
        cross_realm_trust_principal_password: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param kdc_admin_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#kdc_admin_password EmrCluster#kdc_admin_password}.
        :param realm: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#realm EmrCluster#realm}.
        :param ad_domain_join_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#ad_domain_join_password EmrCluster#ad_domain_join_password}.
        :param ad_domain_join_user: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#ad_domain_join_user EmrCluster#ad_domain_join_user}.
        :param cross_realm_trust_principal_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#cross_realm_trust_principal_password EmrCluster#cross_realm_trust_principal_password}.
        '''
        value = EmrClusterKerberosAttributes(
            kdc_admin_password=kdc_admin_password,
            realm=realm,
            ad_domain_join_password=ad_domain_join_password,
            ad_domain_join_user=ad_domain_join_user,
            cross_realm_trust_principal_password=cross_realm_trust_principal_password,
        )

        return typing.cast(None, jsii.invoke(self, "putKerberosAttributes", [value]))

    @jsii.member(jsii_name="putMasterInstanceFleet")
    def put_master_instance_fleet(
        self,
        *,
        instance_type_configs: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EmrClusterMasterInstanceFleetInstanceTypeConfigs", typing.Dict[str, typing.Any]]]]] = None,
        launch_specifications: typing.Optional[typing.Union["EmrClusterMasterInstanceFleetLaunchSpecifications", typing.Dict[str, typing.Any]]] = None,
        name: typing.Optional[builtins.str] = None,
        target_on_demand_capacity: typing.Optional[jsii.Number] = None,
        target_spot_capacity: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param instance_type_configs: instance_type_configs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#instance_type_configs EmrCluster#instance_type_configs}
        :param launch_specifications: launch_specifications block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#launch_specifications EmrCluster#launch_specifications}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#name EmrCluster#name}.
        :param target_on_demand_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#target_on_demand_capacity EmrCluster#target_on_demand_capacity}.
        :param target_spot_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#target_spot_capacity EmrCluster#target_spot_capacity}.
        '''
        value = EmrClusterMasterInstanceFleet(
            instance_type_configs=instance_type_configs,
            launch_specifications=launch_specifications,
            name=name,
            target_on_demand_capacity=target_on_demand_capacity,
            target_spot_capacity=target_spot_capacity,
        )

        return typing.cast(None, jsii.invoke(self, "putMasterInstanceFleet", [value]))

    @jsii.member(jsii_name="putMasterInstanceGroup")
    def put_master_instance_group(
        self,
        *,
        instance_type: builtins.str,
        bid_price: typing.Optional[builtins.str] = None,
        ebs_config: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EmrClusterMasterInstanceGroupEbsConfig", typing.Dict[str, typing.Any]]]]] = None,
        instance_count: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param instance_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#instance_type EmrCluster#instance_type}.
        :param bid_price: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#bid_price EmrCluster#bid_price}.
        :param ebs_config: ebs_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#ebs_config EmrCluster#ebs_config}
        :param instance_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#instance_count EmrCluster#instance_count}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#name EmrCluster#name}.
        '''
        value = EmrClusterMasterInstanceGroup(
            instance_type=instance_type,
            bid_price=bid_price,
            ebs_config=ebs_config,
            instance_count=instance_count,
            name=name,
        )

        return typing.cast(None, jsii.invoke(self, "putMasterInstanceGroup", [value]))

    @jsii.member(jsii_name="putStep")
    def put_step(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EmrClusterStep", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EmrClusterStep, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putStep", [value]))

    @jsii.member(jsii_name="resetAdditionalInfo")
    def reset_additional_info(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdditionalInfo", []))

    @jsii.member(jsii_name="resetApplications")
    def reset_applications(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApplications", []))

    @jsii.member(jsii_name="resetAutoscalingRole")
    def reset_autoscaling_role(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoscalingRole", []))

    @jsii.member(jsii_name="resetAutoTerminationPolicy")
    def reset_auto_termination_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoTerminationPolicy", []))

    @jsii.member(jsii_name="resetBootstrapAction")
    def reset_bootstrap_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBootstrapAction", []))

    @jsii.member(jsii_name="resetConfigurations")
    def reset_configurations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfigurations", []))

    @jsii.member(jsii_name="resetConfigurationsJson")
    def reset_configurations_json(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfigurationsJson", []))

    @jsii.member(jsii_name="resetCoreInstanceFleet")
    def reset_core_instance_fleet(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCoreInstanceFleet", []))

    @jsii.member(jsii_name="resetCoreInstanceGroup")
    def reset_core_instance_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCoreInstanceGroup", []))

    @jsii.member(jsii_name="resetCustomAmiId")
    def reset_custom_ami_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomAmiId", []))

    @jsii.member(jsii_name="resetEbsRootVolumeSize")
    def reset_ebs_root_volume_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEbsRootVolumeSize", []))

    @jsii.member(jsii_name="resetEc2Attributes")
    def reset_ec2_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEc2Attributes", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetKeepJobFlowAliveWhenNoSteps")
    def reset_keep_job_flow_alive_when_no_steps(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeepJobFlowAliveWhenNoSteps", []))

    @jsii.member(jsii_name="resetKerberosAttributes")
    def reset_kerberos_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKerberosAttributes", []))

    @jsii.member(jsii_name="resetListStepsStates")
    def reset_list_steps_states(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetListStepsStates", []))

    @jsii.member(jsii_name="resetLogEncryptionKmsKeyId")
    def reset_log_encryption_kms_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogEncryptionKmsKeyId", []))

    @jsii.member(jsii_name="resetLogUri")
    def reset_log_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogUri", []))

    @jsii.member(jsii_name="resetMasterInstanceFleet")
    def reset_master_instance_fleet(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMasterInstanceFleet", []))

    @jsii.member(jsii_name="resetMasterInstanceGroup")
    def reset_master_instance_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMasterInstanceGroup", []))

    @jsii.member(jsii_name="resetScaleDownBehavior")
    def reset_scale_down_behavior(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScaleDownBehavior", []))

    @jsii.member(jsii_name="resetSecurityConfiguration")
    def reset_security_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurityConfiguration", []))

    @jsii.member(jsii_name="resetStep")
    def reset_step(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStep", []))

    @jsii.member(jsii_name="resetStepConcurrencyLevel")
    def reset_step_concurrency_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStepConcurrencyLevel", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetTerminationProtection")
    def reset_termination_protection(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTerminationProtection", []))

    @jsii.member(jsii_name="resetVisibleToAllUsers")
    def reset_visible_to_all_users(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVisibleToAllUsers", []))

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
    @jsii.member(jsii_name="autoTerminationPolicy")
    def auto_termination_policy(
        self,
    ) -> "EmrClusterAutoTerminationPolicyOutputReference":
        return typing.cast("EmrClusterAutoTerminationPolicyOutputReference", jsii.get(self, "autoTerminationPolicy"))

    @builtins.property
    @jsii.member(jsii_name="bootstrapAction")
    def bootstrap_action(self) -> "EmrClusterBootstrapActionList":
        return typing.cast("EmrClusterBootstrapActionList", jsii.get(self, "bootstrapAction"))

    @builtins.property
    @jsii.member(jsii_name="clusterState")
    def cluster_state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterState"))

    @builtins.property
    @jsii.member(jsii_name="coreInstanceFleet")
    def core_instance_fleet(self) -> "EmrClusterCoreInstanceFleetOutputReference":
        return typing.cast("EmrClusterCoreInstanceFleetOutputReference", jsii.get(self, "coreInstanceFleet"))

    @builtins.property
    @jsii.member(jsii_name="coreInstanceGroup")
    def core_instance_group(self) -> "EmrClusterCoreInstanceGroupOutputReference":
        return typing.cast("EmrClusterCoreInstanceGroupOutputReference", jsii.get(self, "coreInstanceGroup"))

    @builtins.property
    @jsii.member(jsii_name="ec2Attributes")
    def ec2_attributes(self) -> "EmrClusterEc2AttributesOutputReference":
        return typing.cast("EmrClusterEc2AttributesOutputReference", jsii.get(self, "ec2Attributes"))

    @builtins.property
    @jsii.member(jsii_name="kerberosAttributes")
    def kerberos_attributes(self) -> "EmrClusterKerberosAttributesOutputReference":
        return typing.cast("EmrClusterKerberosAttributesOutputReference", jsii.get(self, "kerberosAttributes"))

    @builtins.property
    @jsii.member(jsii_name="masterInstanceFleet")
    def master_instance_fleet(self) -> "EmrClusterMasterInstanceFleetOutputReference":
        return typing.cast("EmrClusterMasterInstanceFleetOutputReference", jsii.get(self, "masterInstanceFleet"))

    @builtins.property
    @jsii.member(jsii_name="masterInstanceGroup")
    def master_instance_group(self) -> "EmrClusterMasterInstanceGroupOutputReference":
        return typing.cast("EmrClusterMasterInstanceGroupOutputReference", jsii.get(self, "masterInstanceGroup"))

    @builtins.property
    @jsii.member(jsii_name="masterPublicDns")
    def master_public_dns(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "masterPublicDns"))

    @builtins.property
    @jsii.member(jsii_name="step")
    def step(self) -> "EmrClusterStepList":
        return typing.cast("EmrClusterStepList", jsii.get(self, "step"))

    @builtins.property
    @jsii.member(jsii_name="additionalInfoInput")
    def additional_info_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "additionalInfoInput"))

    @builtins.property
    @jsii.member(jsii_name="applicationsInput")
    def applications_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "applicationsInput"))

    @builtins.property
    @jsii.member(jsii_name="autoscalingRoleInput")
    def autoscaling_role_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "autoscalingRoleInput"))

    @builtins.property
    @jsii.member(jsii_name="autoTerminationPolicyInput")
    def auto_termination_policy_input(
        self,
    ) -> typing.Optional["EmrClusterAutoTerminationPolicy"]:
        return typing.cast(typing.Optional["EmrClusterAutoTerminationPolicy"], jsii.get(self, "autoTerminationPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="bootstrapActionInput")
    def bootstrap_action_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EmrClusterBootstrapAction"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EmrClusterBootstrapAction"]]], jsii.get(self, "bootstrapActionInput"))

    @builtins.property
    @jsii.member(jsii_name="configurationsInput")
    def configurations_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "configurationsInput"))

    @builtins.property
    @jsii.member(jsii_name="configurationsJsonInput")
    def configurations_json_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "configurationsJsonInput"))

    @builtins.property
    @jsii.member(jsii_name="coreInstanceFleetInput")
    def core_instance_fleet_input(
        self,
    ) -> typing.Optional["EmrClusterCoreInstanceFleet"]:
        return typing.cast(typing.Optional["EmrClusterCoreInstanceFleet"], jsii.get(self, "coreInstanceFleetInput"))

    @builtins.property
    @jsii.member(jsii_name="coreInstanceGroupInput")
    def core_instance_group_input(
        self,
    ) -> typing.Optional["EmrClusterCoreInstanceGroup"]:
        return typing.cast(typing.Optional["EmrClusterCoreInstanceGroup"], jsii.get(self, "coreInstanceGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="customAmiIdInput")
    def custom_ami_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customAmiIdInput"))

    @builtins.property
    @jsii.member(jsii_name="ebsRootVolumeSizeInput")
    def ebs_root_volume_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ebsRootVolumeSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="ec2AttributesInput")
    def ec2_attributes_input(self) -> typing.Optional["EmrClusterEc2Attributes"]:
        return typing.cast(typing.Optional["EmrClusterEc2Attributes"], jsii.get(self, "ec2AttributesInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="keepJobFlowAliveWhenNoStepsInput")
    def keep_job_flow_alive_when_no_steps_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "keepJobFlowAliveWhenNoStepsInput"))

    @builtins.property
    @jsii.member(jsii_name="kerberosAttributesInput")
    def kerberos_attributes_input(
        self,
    ) -> typing.Optional["EmrClusterKerberosAttributes"]:
        return typing.cast(typing.Optional["EmrClusterKerberosAttributes"], jsii.get(self, "kerberosAttributesInput"))

    @builtins.property
    @jsii.member(jsii_name="listStepsStatesInput")
    def list_steps_states_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "listStepsStatesInput"))

    @builtins.property
    @jsii.member(jsii_name="logEncryptionKmsKeyIdInput")
    def log_encryption_kms_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logEncryptionKmsKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="logUriInput")
    def log_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logUriInput"))

    @builtins.property
    @jsii.member(jsii_name="masterInstanceFleetInput")
    def master_instance_fleet_input(
        self,
    ) -> typing.Optional["EmrClusterMasterInstanceFleet"]:
        return typing.cast(typing.Optional["EmrClusterMasterInstanceFleet"], jsii.get(self, "masterInstanceFleetInput"))

    @builtins.property
    @jsii.member(jsii_name="masterInstanceGroupInput")
    def master_instance_group_input(
        self,
    ) -> typing.Optional["EmrClusterMasterInstanceGroup"]:
        return typing.cast(typing.Optional["EmrClusterMasterInstanceGroup"], jsii.get(self, "masterInstanceGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="releaseLabelInput")
    def release_label_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "releaseLabelInput"))

    @builtins.property
    @jsii.member(jsii_name="scaleDownBehaviorInput")
    def scale_down_behavior_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scaleDownBehaviorInput"))

    @builtins.property
    @jsii.member(jsii_name="securityConfigurationInput")
    def security_configuration_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "securityConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceRoleInput")
    def service_role_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceRoleInput"))

    @builtins.property
    @jsii.member(jsii_name="stepConcurrencyLevelInput")
    def step_concurrency_level_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "stepConcurrencyLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="stepInput")
    def step_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EmrClusterStep"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EmrClusterStep"]]], jsii.get(self, "stepInput"))

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
    @jsii.member(jsii_name="terminationProtectionInput")
    def termination_protection_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "terminationProtectionInput"))

    @builtins.property
    @jsii.member(jsii_name="visibleToAllUsersInput")
    def visible_to_all_users_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "visibleToAllUsersInput"))

    @builtins.property
    @jsii.member(jsii_name="additionalInfo")
    def additional_info(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "additionalInfo"))

    @additional_info.setter
    def additional_info(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "additionalInfo", value)

    @builtins.property
    @jsii.member(jsii_name="applications")
    def applications(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "applications"))

    @applications.setter
    def applications(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applications", value)

    @builtins.property
    @jsii.member(jsii_name="autoscalingRole")
    def autoscaling_role(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "autoscalingRole"))

    @autoscaling_role.setter
    def autoscaling_role(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoscalingRole", value)

    @builtins.property
    @jsii.member(jsii_name="configurations")
    def configurations(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "configurations"))

    @configurations.setter
    def configurations(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configurations", value)

    @builtins.property
    @jsii.member(jsii_name="configurationsJson")
    def configurations_json(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "configurationsJson"))

    @configurations_json.setter
    def configurations_json(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configurationsJson", value)

    @builtins.property
    @jsii.member(jsii_name="customAmiId")
    def custom_ami_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customAmiId"))

    @custom_ami_id.setter
    def custom_ami_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customAmiId", value)

    @builtins.property
    @jsii.member(jsii_name="ebsRootVolumeSize")
    def ebs_root_volume_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ebsRootVolumeSize"))

    @ebs_root_volume_size.setter
    def ebs_root_volume_size(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ebsRootVolumeSize", value)

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
    @jsii.member(jsii_name="keepJobFlowAliveWhenNoSteps")
    def keep_job_flow_alive_when_no_steps(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "keepJobFlowAliveWhenNoSteps"))

    @keep_job_flow_alive_when_no_steps.setter
    def keep_job_flow_alive_when_no_steps(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keepJobFlowAliveWhenNoSteps", value)

    @builtins.property
    @jsii.member(jsii_name="listStepsStates")
    def list_steps_states(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "listStepsStates"))

    @list_steps_states.setter
    def list_steps_states(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "listStepsStates", value)

    @builtins.property
    @jsii.member(jsii_name="logEncryptionKmsKeyId")
    def log_encryption_kms_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logEncryptionKmsKeyId"))

    @log_encryption_kms_key_id.setter
    def log_encryption_kms_key_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logEncryptionKmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="logUri")
    def log_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logUri"))

    @log_uri.setter
    def log_uri(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logUri", value)

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
    @jsii.member(jsii_name="releaseLabel")
    def release_label(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "releaseLabel"))

    @release_label.setter
    def release_label(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "releaseLabel", value)

    @builtins.property
    @jsii.member(jsii_name="scaleDownBehavior")
    def scale_down_behavior(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scaleDownBehavior"))

    @scale_down_behavior.setter
    def scale_down_behavior(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scaleDownBehavior", value)

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
    @jsii.member(jsii_name="stepConcurrencyLevel")
    def step_concurrency_level(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "stepConcurrencyLevel"))

    @step_concurrency_level.setter
    def step_concurrency_level(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stepConcurrencyLevel", value)

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
    @jsii.member(jsii_name="terminationProtection")
    def termination_protection(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "terminationProtection"))

    @termination_protection.setter
    def termination_protection(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terminationProtection", value)

    @builtins.property
    @jsii.member(jsii_name="visibleToAllUsers")
    def visible_to_all_users(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "visibleToAllUsers"))

    @visible_to_all_users.setter
    def visible_to_all_users(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "visibleToAllUsers", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.emrCluster.EmrClusterAutoTerminationPolicy",
    jsii_struct_bases=[],
    name_mapping={"idle_timeout": "idleTimeout"},
)
class EmrClusterAutoTerminationPolicy:
    def __init__(self, *, idle_timeout: typing.Optional[jsii.Number] = None) -> None:
        '''
        :param idle_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#idle_timeout EmrCluster#idle_timeout}.
        '''
        if __debug__:
            def stub(*, idle_timeout: typing.Optional[jsii.Number] = None) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument idle_timeout", value=idle_timeout, expected_type=type_hints["idle_timeout"])
        self._values: typing.Dict[str, typing.Any] = {}
        if idle_timeout is not None:
            self._values["idle_timeout"] = idle_timeout

    @builtins.property
    def idle_timeout(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#idle_timeout EmrCluster#idle_timeout}.'''
        result = self._values.get("idle_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmrClusterAutoTerminationPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EmrClusterAutoTerminationPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.emrCluster.EmrClusterAutoTerminationPolicyOutputReference",
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

    @jsii.member(jsii_name="resetIdleTimeout")
    def reset_idle_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdleTimeout", []))

    @builtins.property
    @jsii.member(jsii_name="idleTimeoutInput")
    def idle_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "idleTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="idleTimeout")
    def idle_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "idleTimeout"))

    @idle_timeout.setter
    def idle_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "idleTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[EmrClusterAutoTerminationPolicy]:
        return typing.cast(typing.Optional[EmrClusterAutoTerminationPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EmrClusterAutoTerminationPolicy],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[EmrClusterAutoTerminationPolicy]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.emrCluster.EmrClusterBootstrapAction",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "path": "path", "args": "args"},
)
class EmrClusterBootstrapAction:
    def __init__(
        self,
        *,
        name: builtins.str,
        path: builtins.str,
        args: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#name EmrCluster#name}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#path EmrCluster#path}.
        :param args: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#args EmrCluster#args}.
        '''
        if __debug__:
            def stub(
                *,
                name: builtins.str,
                path: builtins.str,
                args: typing.Optional[typing.Sequence[builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument args", value=args, expected_type=type_hints["args"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "path": path,
        }
        if args is not None:
            self._values["args"] = args

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#name EmrCluster#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#path EmrCluster#path}.'''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def args(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#args EmrCluster#args}.'''
        result = self._values.get("args")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmrClusterBootstrapAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EmrClusterBootstrapActionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.emrCluster.EmrClusterBootstrapActionList",
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
    def get(self, index: jsii.Number) -> "EmrClusterBootstrapActionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EmrClusterBootstrapActionOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterBootstrapAction]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterBootstrapAction]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterBootstrapAction]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterBootstrapAction]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EmrClusterBootstrapActionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.emrCluster.EmrClusterBootstrapActionOutputReference",
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

    @jsii.member(jsii_name="resetArgs")
    def reset_args(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArgs", []))

    @builtins.property
    @jsii.member(jsii_name="argsInput")
    def args_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "argsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="args")
    def args(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "args"))

    @args.setter
    def args(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "args", value)

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
    ) -> typing.Optional[typing.Union[EmrClusterBootstrapAction, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EmrClusterBootstrapAction, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EmrClusterBootstrapAction, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[EmrClusterBootstrapAction, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.emrCluster.EmrClusterConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "name": "name",
        "release_label": "releaseLabel",
        "service_role": "serviceRole",
        "additional_info": "additionalInfo",
        "applications": "applications",
        "autoscaling_role": "autoscalingRole",
        "auto_termination_policy": "autoTerminationPolicy",
        "bootstrap_action": "bootstrapAction",
        "configurations": "configurations",
        "configurations_json": "configurationsJson",
        "core_instance_fleet": "coreInstanceFleet",
        "core_instance_group": "coreInstanceGroup",
        "custom_ami_id": "customAmiId",
        "ebs_root_volume_size": "ebsRootVolumeSize",
        "ec2_attributes": "ec2Attributes",
        "id": "id",
        "keep_job_flow_alive_when_no_steps": "keepJobFlowAliveWhenNoSteps",
        "kerberos_attributes": "kerberosAttributes",
        "list_steps_states": "listStepsStates",
        "log_encryption_kms_key_id": "logEncryptionKmsKeyId",
        "log_uri": "logUri",
        "master_instance_fleet": "masterInstanceFleet",
        "master_instance_group": "masterInstanceGroup",
        "scale_down_behavior": "scaleDownBehavior",
        "security_configuration": "securityConfiguration",
        "step": "step",
        "step_concurrency_level": "stepConcurrencyLevel",
        "tags": "tags",
        "tags_all": "tagsAll",
        "termination_protection": "terminationProtection",
        "visible_to_all_users": "visibleToAllUsers",
    },
)
class EmrClusterConfig(cdktf.TerraformMetaArguments):
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
        name: builtins.str,
        release_label: builtins.str,
        service_role: builtins.str,
        additional_info: typing.Optional[builtins.str] = None,
        applications: typing.Optional[typing.Sequence[builtins.str]] = None,
        autoscaling_role: typing.Optional[builtins.str] = None,
        auto_termination_policy: typing.Optional[typing.Union[EmrClusterAutoTerminationPolicy, typing.Dict[str, typing.Any]]] = None,
        bootstrap_action: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EmrClusterBootstrapAction, typing.Dict[str, typing.Any]]]]] = None,
        configurations: typing.Optional[builtins.str] = None,
        configurations_json: typing.Optional[builtins.str] = None,
        core_instance_fleet: typing.Optional[typing.Union["EmrClusterCoreInstanceFleet", typing.Dict[str, typing.Any]]] = None,
        core_instance_group: typing.Optional[typing.Union["EmrClusterCoreInstanceGroup", typing.Dict[str, typing.Any]]] = None,
        custom_ami_id: typing.Optional[builtins.str] = None,
        ebs_root_volume_size: typing.Optional[jsii.Number] = None,
        ec2_attributes: typing.Optional[typing.Union["EmrClusterEc2Attributes", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        keep_job_flow_alive_when_no_steps: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        kerberos_attributes: typing.Optional[typing.Union["EmrClusterKerberosAttributes", typing.Dict[str, typing.Any]]] = None,
        list_steps_states: typing.Optional[typing.Sequence[builtins.str]] = None,
        log_encryption_kms_key_id: typing.Optional[builtins.str] = None,
        log_uri: typing.Optional[builtins.str] = None,
        master_instance_fleet: typing.Optional[typing.Union["EmrClusterMasterInstanceFleet", typing.Dict[str, typing.Any]]] = None,
        master_instance_group: typing.Optional[typing.Union["EmrClusterMasterInstanceGroup", typing.Dict[str, typing.Any]]] = None,
        scale_down_behavior: typing.Optional[builtins.str] = None,
        security_configuration: typing.Optional[builtins.str] = None,
        step: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EmrClusterStep", typing.Dict[str, typing.Any]]]]] = None,
        step_concurrency_level: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        termination_protection: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        visible_to_all_users: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#name EmrCluster#name}.
        :param release_label: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#release_label EmrCluster#release_label}.
        :param service_role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#service_role EmrCluster#service_role}.
        :param additional_info: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#additional_info EmrCluster#additional_info}.
        :param applications: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#applications EmrCluster#applications}.
        :param autoscaling_role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#autoscaling_role EmrCluster#autoscaling_role}.
        :param auto_termination_policy: auto_termination_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#auto_termination_policy EmrCluster#auto_termination_policy}
        :param bootstrap_action: bootstrap_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#bootstrap_action EmrCluster#bootstrap_action}
        :param configurations: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#configurations EmrCluster#configurations}.
        :param configurations_json: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#configurations_json EmrCluster#configurations_json}.
        :param core_instance_fleet: core_instance_fleet block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#core_instance_fleet EmrCluster#core_instance_fleet}
        :param core_instance_group: core_instance_group block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#core_instance_group EmrCluster#core_instance_group}
        :param custom_ami_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#custom_ami_id EmrCluster#custom_ami_id}.
        :param ebs_root_volume_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#ebs_root_volume_size EmrCluster#ebs_root_volume_size}.
        :param ec2_attributes: ec2_attributes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#ec2_attributes EmrCluster#ec2_attributes}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#id EmrCluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param keep_job_flow_alive_when_no_steps: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#keep_job_flow_alive_when_no_steps EmrCluster#keep_job_flow_alive_when_no_steps}.
        :param kerberos_attributes: kerberos_attributes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#kerberos_attributes EmrCluster#kerberos_attributes}
        :param list_steps_states: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#list_steps_states EmrCluster#list_steps_states}.
        :param log_encryption_kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#log_encryption_kms_key_id EmrCluster#log_encryption_kms_key_id}.
        :param log_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#log_uri EmrCluster#log_uri}.
        :param master_instance_fleet: master_instance_fleet block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#master_instance_fleet EmrCluster#master_instance_fleet}
        :param master_instance_group: master_instance_group block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#master_instance_group EmrCluster#master_instance_group}
        :param scale_down_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#scale_down_behavior EmrCluster#scale_down_behavior}.
        :param security_configuration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#security_configuration EmrCluster#security_configuration}.
        :param step: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#step EmrCluster#step}.
        :param step_concurrency_level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#step_concurrency_level EmrCluster#step_concurrency_level}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#tags EmrCluster#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#tags_all EmrCluster#tags_all}.
        :param termination_protection: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#termination_protection EmrCluster#termination_protection}.
        :param visible_to_all_users: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#visible_to_all_users EmrCluster#visible_to_all_users}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(auto_termination_policy, dict):
            auto_termination_policy = EmrClusterAutoTerminationPolicy(**auto_termination_policy)
        if isinstance(core_instance_fleet, dict):
            core_instance_fleet = EmrClusterCoreInstanceFleet(**core_instance_fleet)
        if isinstance(core_instance_group, dict):
            core_instance_group = EmrClusterCoreInstanceGroup(**core_instance_group)
        if isinstance(ec2_attributes, dict):
            ec2_attributes = EmrClusterEc2Attributes(**ec2_attributes)
        if isinstance(kerberos_attributes, dict):
            kerberos_attributes = EmrClusterKerberosAttributes(**kerberos_attributes)
        if isinstance(master_instance_fleet, dict):
            master_instance_fleet = EmrClusterMasterInstanceFleet(**master_instance_fleet)
        if isinstance(master_instance_group, dict):
            master_instance_group = EmrClusterMasterInstanceGroup(**master_instance_group)
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
                name: builtins.str,
                release_label: builtins.str,
                service_role: builtins.str,
                additional_info: typing.Optional[builtins.str] = None,
                applications: typing.Optional[typing.Sequence[builtins.str]] = None,
                autoscaling_role: typing.Optional[builtins.str] = None,
                auto_termination_policy: typing.Optional[typing.Union[EmrClusterAutoTerminationPolicy, typing.Dict[str, typing.Any]]] = None,
                bootstrap_action: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EmrClusterBootstrapAction, typing.Dict[str, typing.Any]]]]] = None,
                configurations: typing.Optional[builtins.str] = None,
                configurations_json: typing.Optional[builtins.str] = None,
                core_instance_fleet: typing.Optional[typing.Union[EmrClusterCoreInstanceFleet, typing.Dict[str, typing.Any]]] = None,
                core_instance_group: typing.Optional[typing.Union[EmrClusterCoreInstanceGroup, typing.Dict[str, typing.Any]]] = None,
                custom_ami_id: typing.Optional[builtins.str] = None,
                ebs_root_volume_size: typing.Optional[jsii.Number] = None,
                ec2_attributes: typing.Optional[typing.Union[EmrClusterEc2Attributes, typing.Dict[str, typing.Any]]] = None,
                id: typing.Optional[builtins.str] = None,
                keep_job_flow_alive_when_no_steps: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                kerberos_attributes: typing.Optional[typing.Union[EmrClusterKerberosAttributes, typing.Dict[str, typing.Any]]] = None,
                list_steps_states: typing.Optional[typing.Sequence[builtins.str]] = None,
                log_encryption_kms_key_id: typing.Optional[builtins.str] = None,
                log_uri: typing.Optional[builtins.str] = None,
                master_instance_fleet: typing.Optional[typing.Union[EmrClusterMasterInstanceFleet, typing.Dict[str, typing.Any]]] = None,
                master_instance_group: typing.Optional[typing.Union[EmrClusterMasterInstanceGroup, typing.Dict[str, typing.Any]]] = None,
                scale_down_behavior: typing.Optional[builtins.str] = None,
                security_configuration: typing.Optional[builtins.str] = None,
                step: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EmrClusterStep, typing.Dict[str, typing.Any]]]]] = None,
                step_concurrency_level: typing.Optional[jsii.Number] = None,
                tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                termination_protection: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                visible_to_all_users: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
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
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument release_label", value=release_label, expected_type=type_hints["release_label"])
            check_type(argname="argument service_role", value=service_role, expected_type=type_hints["service_role"])
            check_type(argname="argument additional_info", value=additional_info, expected_type=type_hints["additional_info"])
            check_type(argname="argument applications", value=applications, expected_type=type_hints["applications"])
            check_type(argname="argument autoscaling_role", value=autoscaling_role, expected_type=type_hints["autoscaling_role"])
            check_type(argname="argument auto_termination_policy", value=auto_termination_policy, expected_type=type_hints["auto_termination_policy"])
            check_type(argname="argument bootstrap_action", value=bootstrap_action, expected_type=type_hints["bootstrap_action"])
            check_type(argname="argument configurations", value=configurations, expected_type=type_hints["configurations"])
            check_type(argname="argument configurations_json", value=configurations_json, expected_type=type_hints["configurations_json"])
            check_type(argname="argument core_instance_fleet", value=core_instance_fleet, expected_type=type_hints["core_instance_fleet"])
            check_type(argname="argument core_instance_group", value=core_instance_group, expected_type=type_hints["core_instance_group"])
            check_type(argname="argument custom_ami_id", value=custom_ami_id, expected_type=type_hints["custom_ami_id"])
            check_type(argname="argument ebs_root_volume_size", value=ebs_root_volume_size, expected_type=type_hints["ebs_root_volume_size"])
            check_type(argname="argument ec2_attributes", value=ec2_attributes, expected_type=type_hints["ec2_attributes"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument keep_job_flow_alive_when_no_steps", value=keep_job_flow_alive_when_no_steps, expected_type=type_hints["keep_job_flow_alive_when_no_steps"])
            check_type(argname="argument kerberos_attributes", value=kerberos_attributes, expected_type=type_hints["kerberos_attributes"])
            check_type(argname="argument list_steps_states", value=list_steps_states, expected_type=type_hints["list_steps_states"])
            check_type(argname="argument log_encryption_kms_key_id", value=log_encryption_kms_key_id, expected_type=type_hints["log_encryption_kms_key_id"])
            check_type(argname="argument log_uri", value=log_uri, expected_type=type_hints["log_uri"])
            check_type(argname="argument master_instance_fleet", value=master_instance_fleet, expected_type=type_hints["master_instance_fleet"])
            check_type(argname="argument master_instance_group", value=master_instance_group, expected_type=type_hints["master_instance_group"])
            check_type(argname="argument scale_down_behavior", value=scale_down_behavior, expected_type=type_hints["scale_down_behavior"])
            check_type(argname="argument security_configuration", value=security_configuration, expected_type=type_hints["security_configuration"])
            check_type(argname="argument step", value=step, expected_type=type_hints["step"])
            check_type(argname="argument step_concurrency_level", value=step_concurrency_level, expected_type=type_hints["step_concurrency_level"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument termination_protection", value=termination_protection, expected_type=type_hints["termination_protection"])
            check_type(argname="argument visible_to_all_users", value=visible_to_all_users, expected_type=type_hints["visible_to_all_users"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "release_label": release_label,
            "service_role": service_role,
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
        if additional_info is not None:
            self._values["additional_info"] = additional_info
        if applications is not None:
            self._values["applications"] = applications
        if autoscaling_role is not None:
            self._values["autoscaling_role"] = autoscaling_role
        if auto_termination_policy is not None:
            self._values["auto_termination_policy"] = auto_termination_policy
        if bootstrap_action is not None:
            self._values["bootstrap_action"] = bootstrap_action
        if configurations is not None:
            self._values["configurations"] = configurations
        if configurations_json is not None:
            self._values["configurations_json"] = configurations_json
        if core_instance_fleet is not None:
            self._values["core_instance_fleet"] = core_instance_fleet
        if core_instance_group is not None:
            self._values["core_instance_group"] = core_instance_group
        if custom_ami_id is not None:
            self._values["custom_ami_id"] = custom_ami_id
        if ebs_root_volume_size is not None:
            self._values["ebs_root_volume_size"] = ebs_root_volume_size
        if ec2_attributes is not None:
            self._values["ec2_attributes"] = ec2_attributes
        if id is not None:
            self._values["id"] = id
        if keep_job_flow_alive_when_no_steps is not None:
            self._values["keep_job_flow_alive_when_no_steps"] = keep_job_flow_alive_when_no_steps
        if kerberos_attributes is not None:
            self._values["kerberos_attributes"] = kerberos_attributes
        if list_steps_states is not None:
            self._values["list_steps_states"] = list_steps_states
        if log_encryption_kms_key_id is not None:
            self._values["log_encryption_kms_key_id"] = log_encryption_kms_key_id
        if log_uri is not None:
            self._values["log_uri"] = log_uri
        if master_instance_fleet is not None:
            self._values["master_instance_fleet"] = master_instance_fleet
        if master_instance_group is not None:
            self._values["master_instance_group"] = master_instance_group
        if scale_down_behavior is not None:
            self._values["scale_down_behavior"] = scale_down_behavior
        if security_configuration is not None:
            self._values["security_configuration"] = security_configuration
        if step is not None:
            self._values["step"] = step
        if step_concurrency_level is not None:
            self._values["step_concurrency_level"] = step_concurrency_level
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if termination_protection is not None:
            self._values["termination_protection"] = termination_protection
        if visible_to_all_users is not None:
            self._values["visible_to_all_users"] = visible_to_all_users

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
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#name EmrCluster#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def release_label(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#release_label EmrCluster#release_label}.'''
        result = self._values.get("release_label")
        assert result is not None, "Required property 'release_label' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_role(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#service_role EmrCluster#service_role}.'''
        result = self._values.get("service_role")
        assert result is not None, "Required property 'service_role' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def additional_info(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#additional_info EmrCluster#additional_info}.'''
        result = self._values.get("additional_info")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def applications(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#applications EmrCluster#applications}.'''
        result = self._values.get("applications")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def autoscaling_role(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#autoscaling_role EmrCluster#autoscaling_role}.'''
        result = self._values.get("autoscaling_role")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def auto_termination_policy(
        self,
    ) -> typing.Optional[EmrClusterAutoTerminationPolicy]:
        '''auto_termination_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#auto_termination_policy EmrCluster#auto_termination_policy}
        '''
        result = self._values.get("auto_termination_policy")
        return typing.cast(typing.Optional[EmrClusterAutoTerminationPolicy], result)

    @builtins.property
    def bootstrap_action(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterBootstrapAction]]]:
        '''bootstrap_action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#bootstrap_action EmrCluster#bootstrap_action}
        '''
        result = self._values.get("bootstrap_action")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterBootstrapAction]]], result)

    @builtins.property
    def configurations(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#configurations EmrCluster#configurations}.'''
        result = self._values.get("configurations")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def configurations_json(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#configurations_json EmrCluster#configurations_json}.'''
        result = self._values.get("configurations_json")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def core_instance_fleet(self) -> typing.Optional["EmrClusterCoreInstanceFleet"]:
        '''core_instance_fleet block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#core_instance_fleet EmrCluster#core_instance_fleet}
        '''
        result = self._values.get("core_instance_fleet")
        return typing.cast(typing.Optional["EmrClusterCoreInstanceFleet"], result)

    @builtins.property
    def core_instance_group(self) -> typing.Optional["EmrClusterCoreInstanceGroup"]:
        '''core_instance_group block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#core_instance_group EmrCluster#core_instance_group}
        '''
        result = self._values.get("core_instance_group")
        return typing.cast(typing.Optional["EmrClusterCoreInstanceGroup"], result)

    @builtins.property
    def custom_ami_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#custom_ami_id EmrCluster#custom_ami_id}.'''
        result = self._values.get("custom_ami_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ebs_root_volume_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#ebs_root_volume_size EmrCluster#ebs_root_volume_size}.'''
        result = self._values.get("ebs_root_volume_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ec2_attributes(self) -> typing.Optional["EmrClusterEc2Attributes"]:
        '''ec2_attributes block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#ec2_attributes EmrCluster#ec2_attributes}
        '''
        result = self._values.get("ec2_attributes")
        return typing.cast(typing.Optional["EmrClusterEc2Attributes"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#id EmrCluster#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def keep_job_flow_alive_when_no_steps(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#keep_job_flow_alive_when_no_steps EmrCluster#keep_job_flow_alive_when_no_steps}.'''
        result = self._values.get("keep_job_flow_alive_when_no_steps")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def kerberos_attributes(self) -> typing.Optional["EmrClusterKerberosAttributes"]:
        '''kerberos_attributes block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#kerberos_attributes EmrCluster#kerberos_attributes}
        '''
        result = self._values.get("kerberos_attributes")
        return typing.cast(typing.Optional["EmrClusterKerberosAttributes"], result)

    @builtins.property
    def list_steps_states(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#list_steps_states EmrCluster#list_steps_states}.'''
        result = self._values.get("list_steps_states")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def log_encryption_kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#log_encryption_kms_key_id EmrCluster#log_encryption_kms_key_id}.'''
        result = self._values.get("log_encryption_kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_uri(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#log_uri EmrCluster#log_uri}.'''
        result = self._values.get("log_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def master_instance_fleet(self) -> typing.Optional["EmrClusterMasterInstanceFleet"]:
        '''master_instance_fleet block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#master_instance_fleet EmrCluster#master_instance_fleet}
        '''
        result = self._values.get("master_instance_fleet")
        return typing.cast(typing.Optional["EmrClusterMasterInstanceFleet"], result)

    @builtins.property
    def master_instance_group(self) -> typing.Optional["EmrClusterMasterInstanceGroup"]:
        '''master_instance_group block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#master_instance_group EmrCluster#master_instance_group}
        '''
        result = self._values.get("master_instance_group")
        return typing.cast(typing.Optional["EmrClusterMasterInstanceGroup"], result)

    @builtins.property
    def scale_down_behavior(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#scale_down_behavior EmrCluster#scale_down_behavior}.'''
        result = self._values.get("scale_down_behavior")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def security_configuration(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#security_configuration EmrCluster#security_configuration}.'''
        result = self._values.get("security_configuration")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def step(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EmrClusterStep"]]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#step EmrCluster#step}.'''
        result = self._values.get("step")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EmrClusterStep"]]], result)

    @builtins.property
    def step_concurrency_level(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#step_concurrency_level EmrCluster#step_concurrency_level}.'''
        result = self._values.get("step_concurrency_level")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#tags EmrCluster#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#tags_all EmrCluster#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def termination_protection(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#termination_protection EmrCluster#termination_protection}.'''
        result = self._values.get("termination_protection")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def visible_to_all_users(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#visible_to_all_users EmrCluster#visible_to_all_users}.'''
        result = self._values.get("visible_to_all_users")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmrClusterConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.emrCluster.EmrClusterCoreInstanceFleet",
    jsii_struct_bases=[],
    name_mapping={
        "instance_type_configs": "instanceTypeConfigs",
        "launch_specifications": "launchSpecifications",
        "name": "name",
        "target_on_demand_capacity": "targetOnDemandCapacity",
        "target_spot_capacity": "targetSpotCapacity",
    },
)
class EmrClusterCoreInstanceFleet:
    def __init__(
        self,
        *,
        instance_type_configs: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EmrClusterCoreInstanceFleetInstanceTypeConfigs", typing.Dict[str, typing.Any]]]]] = None,
        launch_specifications: typing.Optional[typing.Union["EmrClusterCoreInstanceFleetLaunchSpecifications", typing.Dict[str, typing.Any]]] = None,
        name: typing.Optional[builtins.str] = None,
        target_on_demand_capacity: typing.Optional[jsii.Number] = None,
        target_spot_capacity: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param instance_type_configs: instance_type_configs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#instance_type_configs EmrCluster#instance_type_configs}
        :param launch_specifications: launch_specifications block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#launch_specifications EmrCluster#launch_specifications}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#name EmrCluster#name}.
        :param target_on_demand_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#target_on_demand_capacity EmrCluster#target_on_demand_capacity}.
        :param target_spot_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#target_spot_capacity EmrCluster#target_spot_capacity}.
        '''
        if isinstance(launch_specifications, dict):
            launch_specifications = EmrClusterCoreInstanceFleetLaunchSpecifications(**launch_specifications)
        if __debug__:
            def stub(
                *,
                instance_type_configs: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EmrClusterCoreInstanceFleetInstanceTypeConfigs, typing.Dict[str, typing.Any]]]]] = None,
                launch_specifications: typing.Optional[typing.Union[EmrClusterCoreInstanceFleetLaunchSpecifications, typing.Dict[str, typing.Any]]] = None,
                name: typing.Optional[builtins.str] = None,
                target_on_demand_capacity: typing.Optional[jsii.Number] = None,
                target_spot_capacity: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument instance_type_configs", value=instance_type_configs, expected_type=type_hints["instance_type_configs"])
            check_type(argname="argument launch_specifications", value=launch_specifications, expected_type=type_hints["launch_specifications"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument target_on_demand_capacity", value=target_on_demand_capacity, expected_type=type_hints["target_on_demand_capacity"])
            check_type(argname="argument target_spot_capacity", value=target_spot_capacity, expected_type=type_hints["target_spot_capacity"])
        self._values: typing.Dict[str, typing.Any] = {}
        if instance_type_configs is not None:
            self._values["instance_type_configs"] = instance_type_configs
        if launch_specifications is not None:
            self._values["launch_specifications"] = launch_specifications
        if name is not None:
            self._values["name"] = name
        if target_on_demand_capacity is not None:
            self._values["target_on_demand_capacity"] = target_on_demand_capacity
        if target_spot_capacity is not None:
            self._values["target_spot_capacity"] = target_spot_capacity

    @builtins.property
    def instance_type_configs(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EmrClusterCoreInstanceFleetInstanceTypeConfigs"]]]:
        '''instance_type_configs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#instance_type_configs EmrCluster#instance_type_configs}
        '''
        result = self._values.get("instance_type_configs")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EmrClusterCoreInstanceFleetInstanceTypeConfigs"]]], result)

    @builtins.property
    def launch_specifications(
        self,
    ) -> typing.Optional["EmrClusterCoreInstanceFleetLaunchSpecifications"]:
        '''launch_specifications block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#launch_specifications EmrCluster#launch_specifications}
        '''
        result = self._values.get("launch_specifications")
        return typing.cast(typing.Optional["EmrClusterCoreInstanceFleetLaunchSpecifications"], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#name EmrCluster#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_on_demand_capacity(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#target_on_demand_capacity EmrCluster#target_on_demand_capacity}.'''
        result = self._values.get("target_on_demand_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def target_spot_capacity(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#target_spot_capacity EmrCluster#target_spot_capacity}.'''
        result = self._values.get("target_spot_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmrClusterCoreInstanceFleet(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.emrCluster.EmrClusterCoreInstanceFleetInstanceTypeConfigs",
    jsii_struct_bases=[],
    name_mapping={
        "instance_type": "instanceType",
        "bid_price": "bidPrice",
        "bid_price_as_percentage_of_on_demand_price": "bidPriceAsPercentageOfOnDemandPrice",
        "configurations": "configurations",
        "ebs_config": "ebsConfig",
        "weighted_capacity": "weightedCapacity",
    },
)
class EmrClusterCoreInstanceFleetInstanceTypeConfigs:
    def __init__(
        self,
        *,
        instance_type: builtins.str,
        bid_price: typing.Optional[builtins.str] = None,
        bid_price_as_percentage_of_on_demand_price: typing.Optional[jsii.Number] = None,
        configurations: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EmrClusterCoreInstanceFleetInstanceTypeConfigsConfigurations", typing.Dict[str, typing.Any]]]]] = None,
        ebs_config: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EmrClusterCoreInstanceFleetInstanceTypeConfigsEbsConfig", typing.Dict[str, typing.Any]]]]] = None,
        weighted_capacity: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param instance_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#instance_type EmrCluster#instance_type}.
        :param bid_price: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#bid_price EmrCluster#bid_price}.
        :param bid_price_as_percentage_of_on_demand_price: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#bid_price_as_percentage_of_on_demand_price EmrCluster#bid_price_as_percentage_of_on_demand_price}.
        :param configurations: configurations block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#configurations EmrCluster#configurations}
        :param ebs_config: ebs_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#ebs_config EmrCluster#ebs_config}
        :param weighted_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#weighted_capacity EmrCluster#weighted_capacity}.
        '''
        if __debug__:
            def stub(
                *,
                instance_type: builtins.str,
                bid_price: typing.Optional[builtins.str] = None,
                bid_price_as_percentage_of_on_demand_price: typing.Optional[jsii.Number] = None,
                configurations: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EmrClusterCoreInstanceFleetInstanceTypeConfigsConfigurations, typing.Dict[str, typing.Any]]]]] = None,
                ebs_config: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EmrClusterCoreInstanceFleetInstanceTypeConfigsEbsConfig, typing.Dict[str, typing.Any]]]]] = None,
                weighted_capacity: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            check_type(argname="argument bid_price", value=bid_price, expected_type=type_hints["bid_price"])
            check_type(argname="argument bid_price_as_percentage_of_on_demand_price", value=bid_price_as_percentage_of_on_demand_price, expected_type=type_hints["bid_price_as_percentage_of_on_demand_price"])
            check_type(argname="argument configurations", value=configurations, expected_type=type_hints["configurations"])
            check_type(argname="argument ebs_config", value=ebs_config, expected_type=type_hints["ebs_config"])
            check_type(argname="argument weighted_capacity", value=weighted_capacity, expected_type=type_hints["weighted_capacity"])
        self._values: typing.Dict[str, typing.Any] = {
            "instance_type": instance_type,
        }
        if bid_price is not None:
            self._values["bid_price"] = bid_price
        if bid_price_as_percentage_of_on_demand_price is not None:
            self._values["bid_price_as_percentage_of_on_demand_price"] = bid_price_as_percentage_of_on_demand_price
        if configurations is not None:
            self._values["configurations"] = configurations
        if ebs_config is not None:
            self._values["ebs_config"] = ebs_config
        if weighted_capacity is not None:
            self._values["weighted_capacity"] = weighted_capacity

    @builtins.property
    def instance_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#instance_type EmrCluster#instance_type}.'''
        result = self._values.get("instance_type")
        assert result is not None, "Required property 'instance_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bid_price(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#bid_price EmrCluster#bid_price}.'''
        result = self._values.get("bid_price")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bid_price_as_percentage_of_on_demand_price(
        self,
    ) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#bid_price_as_percentage_of_on_demand_price EmrCluster#bid_price_as_percentage_of_on_demand_price}.'''
        result = self._values.get("bid_price_as_percentage_of_on_demand_price")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def configurations(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EmrClusterCoreInstanceFleetInstanceTypeConfigsConfigurations"]]]:
        '''configurations block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#configurations EmrCluster#configurations}
        '''
        result = self._values.get("configurations")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EmrClusterCoreInstanceFleetInstanceTypeConfigsConfigurations"]]], result)

    @builtins.property
    def ebs_config(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EmrClusterCoreInstanceFleetInstanceTypeConfigsEbsConfig"]]]:
        '''ebs_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#ebs_config EmrCluster#ebs_config}
        '''
        result = self._values.get("ebs_config")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EmrClusterCoreInstanceFleetInstanceTypeConfigsEbsConfig"]]], result)

    @builtins.property
    def weighted_capacity(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#weighted_capacity EmrCluster#weighted_capacity}.'''
        result = self._values.get("weighted_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmrClusterCoreInstanceFleetInstanceTypeConfigs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.emrCluster.EmrClusterCoreInstanceFleetInstanceTypeConfigsConfigurations",
    jsii_struct_bases=[],
    name_mapping={"classification": "classification", "properties": "properties"},
)
class EmrClusterCoreInstanceFleetInstanceTypeConfigsConfigurations:
    def __init__(
        self,
        *,
        classification: typing.Optional[builtins.str] = None,
        properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param classification: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#classification EmrCluster#classification}.
        :param properties: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#properties EmrCluster#properties}.
        '''
        if __debug__:
            def stub(
                *,
                classification: typing.Optional[builtins.str] = None,
                properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument classification", value=classification, expected_type=type_hints["classification"])
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
        self._values: typing.Dict[str, typing.Any] = {}
        if classification is not None:
            self._values["classification"] = classification
        if properties is not None:
            self._values["properties"] = properties

    @builtins.property
    def classification(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#classification EmrCluster#classification}.'''
        result = self._values.get("classification")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def properties(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#properties EmrCluster#properties}.'''
        result = self._values.get("properties")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmrClusterCoreInstanceFleetInstanceTypeConfigsConfigurations(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EmrClusterCoreInstanceFleetInstanceTypeConfigsConfigurationsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.emrCluster.EmrClusterCoreInstanceFleetInstanceTypeConfigsConfigurationsList",
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
    ) -> "EmrClusterCoreInstanceFleetInstanceTypeConfigsConfigurationsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EmrClusterCoreInstanceFleetInstanceTypeConfigsConfigurationsOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterCoreInstanceFleetInstanceTypeConfigsConfigurations]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterCoreInstanceFleetInstanceTypeConfigsConfigurations]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterCoreInstanceFleetInstanceTypeConfigsConfigurations]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterCoreInstanceFleetInstanceTypeConfigsConfigurations]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EmrClusterCoreInstanceFleetInstanceTypeConfigsConfigurationsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.emrCluster.EmrClusterCoreInstanceFleetInstanceTypeConfigsConfigurationsOutputReference",
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

    @jsii.member(jsii_name="resetClassification")
    def reset_classification(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClassification", []))

    @jsii.member(jsii_name="resetProperties")
    def reset_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProperties", []))

    @builtins.property
    @jsii.member(jsii_name="classificationInput")
    def classification_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "classificationInput"))

    @builtins.property
    @jsii.member(jsii_name="propertiesInput")
    def properties_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "propertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="classification")
    def classification(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "classification"))

    @classification.setter
    def classification(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "classification", value)

    @builtins.property
    @jsii.member(jsii_name="properties")
    def properties(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "properties"))

    @properties.setter
    def properties(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.Mapping[builtins.str, builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "properties", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EmrClusterCoreInstanceFleetInstanceTypeConfigsConfigurations, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EmrClusterCoreInstanceFleetInstanceTypeConfigsConfigurations, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EmrClusterCoreInstanceFleetInstanceTypeConfigsConfigurations, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[EmrClusterCoreInstanceFleetInstanceTypeConfigsConfigurations, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.emrCluster.EmrClusterCoreInstanceFleetInstanceTypeConfigsEbsConfig",
    jsii_struct_bases=[],
    name_mapping={
        "size": "size",
        "type": "type",
        "iops": "iops",
        "volumes_per_instance": "volumesPerInstance",
    },
)
class EmrClusterCoreInstanceFleetInstanceTypeConfigsEbsConfig:
    def __init__(
        self,
        *,
        size: jsii.Number,
        type: builtins.str,
        iops: typing.Optional[jsii.Number] = None,
        volumes_per_instance: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#size EmrCluster#size}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#type EmrCluster#type}.
        :param iops: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#iops EmrCluster#iops}.
        :param volumes_per_instance: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#volumes_per_instance EmrCluster#volumes_per_instance}.
        '''
        if __debug__:
            def stub(
                *,
                size: jsii.Number,
                type: builtins.str,
                iops: typing.Optional[jsii.Number] = None,
                volumes_per_instance: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument size", value=size, expected_type=type_hints["size"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument iops", value=iops, expected_type=type_hints["iops"])
            check_type(argname="argument volumes_per_instance", value=volumes_per_instance, expected_type=type_hints["volumes_per_instance"])
        self._values: typing.Dict[str, typing.Any] = {
            "size": size,
            "type": type,
        }
        if iops is not None:
            self._values["iops"] = iops
        if volumes_per_instance is not None:
            self._values["volumes_per_instance"] = volumes_per_instance

    @builtins.property
    def size(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#size EmrCluster#size}.'''
        result = self._values.get("size")
        assert result is not None, "Required property 'size' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#type EmrCluster#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def iops(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#iops EmrCluster#iops}.'''
        result = self._values.get("iops")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def volumes_per_instance(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#volumes_per_instance EmrCluster#volumes_per_instance}.'''
        result = self._values.get("volumes_per_instance")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmrClusterCoreInstanceFleetInstanceTypeConfigsEbsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EmrClusterCoreInstanceFleetInstanceTypeConfigsEbsConfigList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.emrCluster.EmrClusterCoreInstanceFleetInstanceTypeConfigsEbsConfigList",
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
    ) -> "EmrClusterCoreInstanceFleetInstanceTypeConfigsEbsConfigOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EmrClusterCoreInstanceFleetInstanceTypeConfigsEbsConfigOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterCoreInstanceFleetInstanceTypeConfigsEbsConfig]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterCoreInstanceFleetInstanceTypeConfigsEbsConfig]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterCoreInstanceFleetInstanceTypeConfigsEbsConfig]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterCoreInstanceFleetInstanceTypeConfigsEbsConfig]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EmrClusterCoreInstanceFleetInstanceTypeConfigsEbsConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.emrCluster.EmrClusterCoreInstanceFleetInstanceTypeConfigsEbsConfigOutputReference",
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

    @jsii.member(jsii_name="resetIops")
    def reset_iops(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIops", []))

    @jsii.member(jsii_name="resetVolumesPerInstance")
    def reset_volumes_per_instance(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVolumesPerInstance", []))

    @builtins.property
    @jsii.member(jsii_name="iopsInput")
    def iops_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "iopsInput"))

    @builtins.property
    @jsii.member(jsii_name="sizeInput")
    def size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sizeInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="volumesPerInstanceInput")
    def volumes_per_instance_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "volumesPerInstanceInput"))

    @builtins.property
    @jsii.member(jsii_name="iops")
    def iops(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "iops"))

    @iops.setter
    def iops(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iops", value)

    @builtins.property
    @jsii.member(jsii_name="size")
    def size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "size"))

    @size.setter
    def size(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "size", value)

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
    @jsii.member(jsii_name="volumesPerInstance")
    def volumes_per_instance(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "volumesPerInstance"))

    @volumes_per_instance.setter
    def volumes_per_instance(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumesPerInstance", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EmrClusterCoreInstanceFleetInstanceTypeConfigsEbsConfig, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EmrClusterCoreInstanceFleetInstanceTypeConfigsEbsConfig, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EmrClusterCoreInstanceFleetInstanceTypeConfigsEbsConfig, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[EmrClusterCoreInstanceFleetInstanceTypeConfigsEbsConfig, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EmrClusterCoreInstanceFleetInstanceTypeConfigsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.emrCluster.EmrClusterCoreInstanceFleetInstanceTypeConfigsList",
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
    ) -> "EmrClusterCoreInstanceFleetInstanceTypeConfigsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EmrClusterCoreInstanceFleetInstanceTypeConfigsOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterCoreInstanceFleetInstanceTypeConfigs]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterCoreInstanceFleetInstanceTypeConfigs]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterCoreInstanceFleetInstanceTypeConfigs]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterCoreInstanceFleetInstanceTypeConfigs]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EmrClusterCoreInstanceFleetInstanceTypeConfigsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.emrCluster.EmrClusterCoreInstanceFleetInstanceTypeConfigsOutputReference",
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

    @jsii.member(jsii_name="putConfigurations")
    def put_configurations(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EmrClusterCoreInstanceFleetInstanceTypeConfigsConfigurations, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EmrClusterCoreInstanceFleetInstanceTypeConfigsConfigurations, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putConfigurations", [value]))

    @jsii.member(jsii_name="putEbsConfig")
    def put_ebs_config(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EmrClusterCoreInstanceFleetInstanceTypeConfigsEbsConfig, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EmrClusterCoreInstanceFleetInstanceTypeConfigsEbsConfig, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEbsConfig", [value]))

    @jsii.member(jsii_name="resetBidPrice")
    def reset_bid_price(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBidPrice", []))

    @jsii.member(jsii_name="resetBidPriceAsPercentageOfOnDemandPrice")
    def reset_bid_price_as_percentage_of_on_demand_price(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBidPriceAsPercentageOfOnDemandPrice", []))

    @jsii.member(jsii_name="resetConfigurations")
    def reset_configurations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfigurations", []))

    @jsii.member(jsii_name="resetEbsConfig")
    def reset_ebs_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEbsConfig", []))

    @jsii.member(jsii_name="resetWeightedCapacity")
    def reset_weighted_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWeightedCapacity", []))

    @builtins.property
    @jsii.member(jsii_name="configurations")
    def configurations(
        self,
    ) -> EmrClusterCoreInstanceFleetInstanceTypeConfigsConfigurationsList:
        return typing.cast(EmrClusterCoreInstanceFleetInstanceTypeConfigsConfigurationsList, jsii.get(self, "configurations"))

    @builtins.property
    @jsii.member(jsii_name="ebsConfig")
    def ebs_config(self) -> EmrClusterCoreInstanceFleetInstanceTypeConfigsEbsConfigList:
        return typing.cast(EmrClusterCoreInstanceFleetInstanceTypeConfigsEbsConfigList, jsii.get(self, "ebsConfig"))

    @builtins.property
    @jsii.member(jsii_name="bidPriceAsPercentageOfOnDemandPriceInput")
    def bid_price_as_percentage_of_on_demand_price_input(
        self,
    ) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "bidPriceAsPercentageOfOnDemandPriceInput"))

    @builtins.property
    @jsii.member(jsii_name="bidPriceInput")
    def bid_price_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bidPriceInput"))

    @builtins.property
    @jsii.member(jsii_name="configurationsInput")
    def configurations_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterCoreInstanceFleetInstanceTypeConfigsConfigurations]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterCoreInstanceFleetInstanceTypeConfigsConfigurations]]], jsii.get(self, "configurationsInput"))

    @builtins.property
    @jsii.member(jsii_name="ebsConfigInput")
    def ebs_config_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterCoreInstanceFleetInstanceTypeConfigsEbsConfig]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterCoreInstanceFleetInstanceTypeConfigsEbsConfig]]], jsii.get(self, "ebsConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceTypeInput")
    def instance_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="weightedCapacityInput")
    def weighted_capacity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "weightedCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="bidPrice")
    def bid_price(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bidPrice"))

    @bid_price.setter
    def bid_price(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bidPrice", value)

    @builtins.property
    @jsii.member(jsii_name="bidPriceAsPercentageOfOnDemandPrice")
    def bid_price_as_percentage_of_on_demand_price(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "bidPriceAsPercentageOfOnDemandPrice"))

    @bid_price_as_percentage_of_on_demand_price.setter
    def bid_price_as_percentage_of_on_demand_price(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bidPriceAsPercentageOfOnDemandPrice", value)

    @builtins.property
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceType"))

    @instance_type.setter
    def instance_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceType", value)

    @builtins.property
    @jsii.member(jsii_name="weightedCapacity")
    def weighted_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "weightedCapacity"))

    @weighted_capacity.setter
    def weighted_capacity(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "weightedCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EmrClusterCoreInstanceFleetInstanceTypeConfigs, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EmrClusterCoreInstanceFleetInstanceTypeConfigs, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EmrClusterCoreInstanceFleetInstanceTypeConfigs, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[EmrClusterCoreInstanceFleetInstanceTypeConfigs, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.emrCluster.EmrClusterCoreInstanceFleetLaunchSpecifications",
    jsii_struct_bases=[],
    name_mapping={
        "on_demand_specification": "onDemandSpecification",
        "spot_specification": "spotSpecification",
    },
)
class EmrClusterCoreInstanceFleetLaunchSpecifications:
    def __init__(
        self,
        *,
        on_demand_specification: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EmrClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecification", typing.Dict[str, typing.Any]]]]] = None,
        spot_specification: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EmrClusterCoreInstanceFleetLaunchSpecificationsSpotSpecification", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param on_demand_specification: on_demand_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#on_demand_specification EmrCluster#on_demand_specification}
        :param spot_specification: spot_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#spot_specification EmrCluster#spot_specification}
        '''
        if __debug__:
            def stub(
                *,
                on_demand_specification: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EmrClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecification, typing.Dict[str, typing.Any]]]]] = None,
                spot_specification: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EmrClusterCoreInstanceFleetLaunchSpecificationsSpotSpecification, typing.Dict[str, typing.Any]]]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument on_demand_specification", value=on_demand_specification, expected_type=type_hints["on_demand_specification"])
            check_type(argname="argument spot_specification", value=spot_specification, expected_type=type_hints["spot_specification"])
        self._values: typing.Dict[str, typing.Any] = {}
        if on_demand_specification is not None:
            self._values["on_demand_specification"] = on_demand_specification
        if spot_specification is not None:
            self._values["spot_specification"] = spot_specification

    @builtins.property
    def on_demand_specification(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EmrClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecification"]]]:
        '''on_demand_specification block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#on_demand_specification EmrCluster#on_demand_specification}
        '''
        result = self._values.get("on_demand_specification")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EmrClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecification"]]], result)

    @builtins.property
    def spot_specification(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EmrClusterCoreInstanceFleetLaunchSpecificationsSpotSpecification"]]]:
        '''spot_specification block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#spot_specification EmrCluster#spot_specification}
        '''
        result = self._values.get("spot_specification")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EmrClusterCoreInstanceFleetLaunchSpecificationsSpotSpecification"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmrClusterCoreInstanceFleetLaunchSpecifications(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.emrCluster.EmrClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecification",
    jsii_struct_bases=[],
    name_mapping={"allocation_strategy": "allocationStrategy"},
)
class EmrClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecification:
    def __init__(self, *, allocation_strategy: builtins.str) -> None:
        '''
        :param allocation_strategy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#allocation_strategy EmrCluster#allocation_strategy}.
        '''
        if __debug__:
            def stub(*, allocation_strategy: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument allocation_strategy", value=allocation_strategy, expected_type=type_hints["allocation_strategy"])
        self._values: typing.Dict[str, typing.Any] = {
            "allocation_strategy": allocation_strategy,
        }

    @builtins.property
    def allocation_strategy(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#allocation_strategy EmrCluster#allocation_strategy}.'''
        result = self._values.get("allocation_strategy")
        assert result is not None, "Required property 'allocation_strategy' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmrClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecification(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EmrClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecificationList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.emrCluster.EmrClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecificationList",
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
    ) -> "EmrClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecificationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EmrClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecificationOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecification]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecification]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecification]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecification]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EmrClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecificationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.emrCluster.EmrClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecificationOutputReference",
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
    @jsii.member(jsii_name="allocationStrategyInput")
    def allocation_strategy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "allocationStrategyInput"))

    @builtins.property
    @jsii.member(jsii_name="allocationStrategy")
    def allocation_strategy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "allocationStrategy"))

    @allocation_strategy.setter
    def allocation_strategy(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allocationStrategy", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EmrClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecification, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EmrClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecification, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EmrClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecification, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[EmrClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecification, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EmrClusterCoreInstanceFleetLaunchSpecificationsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.emrCluster.EmrClusterCoreInstanceFleetLaunchSpecificationsOutputReference",
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

    @jsii.member(jsii_name="putOnDemandSpecification")
    def put_on_demand_specification(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EmrClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecification, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EmrClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecification, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putOnDemandSpecification", [value]))

    @jsii.member(jsii_name="putSpotSpecification")
    def put_spot_specification(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EmrClusterCoreInstanceFleetLaunchSpecificationsSpotSpecification", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EmrClusterCoreInstanceFleetLaunchSpecificationsSpotSpecification, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSpotSpecification", [value]))

    @jsii.member(jsii_name="resetOnDemandSpecification")
    def reset_on_demand_specification(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOnDemandSpecification", []))

    @jsii.member(jsii_name="resetSpotSpecification")
    def reset_spot_specification(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSpotSpecification", []))

    @builtins.property
    @jsii.member(jsii_name="onDemandSpecification")
    def on_demand_specification(
        self,
    ) -> EmrClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecificationList:
        return typing.cast(EmrClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecificationList, jsii.get(self, "onDemandSpecification"))

    @builtins.property
    @jsii.member(jsii_name="spotSpecification")
    def spot_specification(
        self,
    ) -> "EmrClusterCoreInstanceFleetLaunchSpecificationsSpotSpecificationList":
        return typing.cast("EmrClusterCoreInstanceFleetLaunchSpecificationsSpotSpecificationList", jsii.get(self, "spotSpecification"))

    @builtins.property
    @jsii.member(jsii_name="onDemandSpecificationInput")
    def on_demand_specification_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecification]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecification]]], jsii.get(self, "onDemandSpecificationInput"))

    @builtins.property
    @jsii.member(jsii_name="spotSpecificationInput")
    def spot_specification_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EmrClusterCoreInstanceFleetLaunchSpecificationsSpotSpecification"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EmrClusterCoreInstanceFleetLaunchSpecificationsSpotSpecification"]]], jsii.get(self, "spotSpecificationInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[EmrClusterCoreInstanceFleetLaunchSpecifications]:
        return typing.cast(typing.Optional[EmrClusterCoreInstanceFleetLaunchSpecifications], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EmrClusterCoreInstanceFleetLaunchSpecifications],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[EmrClusterCoreInstanceFleetLaunchSpecifications],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.emrCluster.EmrClusterCoreInstanceFleetLaunchSpecificationsSpotSpecification",
    jsii_struct_bases=[],
    name_mapping={
        "allocation_strategy": "allocationStrategy",
        "timeout_action": "timeoutAction",
        "timeout_duration_minutes": "timeoutDurationMinutes",
        "block_duration_minutes": "blockDurationMinutes",
    },
)
class EmrClusterCoreInstanceFleetLaunchSpecificationsSpotSpecification:
    def __init__(
        self,
        *,
        allocation_strategy: builtins.str,
        timeout_action: builtins.str,
        timeout_duration_minutes: jsii.Number,
        block_duration_minutes: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param allocation_strategy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#allocation_strategy EmrCluster#allocation_strategy}.
        :param timeout_action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#timeout_action EmrCluster#timeout_action}.
        :param timeout_duration_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#timeout_duration_minutes EmrCluster#timeout_duration_minutes}.
        :param block_duration_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#block_duration_minutes EmrCluster#block_duration_minutes}.
        '''
        if __debug__:
            def stub(
                *,
                allocation_strategy: builtins.str,
                timeout_action: builtins.str,
                timeout_duration_minutes: jsii.Number,
                block_duration_minutes: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument allocation_strategy", value=allocation_strategy, expected_type=type_hints["allocation_strategy"])
            check_type(argname="argument timeout_action", value=timeout_action, expected_type=type_hints["timeout_action"])
            check_type(argname="argument timeout_duration_minutes", value=timeout_duration_minutes, expected_type=type_hints["timeout_duration_minutes"])
            check_type(argname="argument block_duration_minutes", value=block_duration_minutes, expected_type=type_hints["block_duration_minutes"])
        self._values: typing.Dict[str, typing.Any] = {
            "allocation_strategy": allocation_strategy,
            "timeout_action": timeout_action,
            "timeout_duration_minutes": timeout_duration_minutes,
        }
        if block_duration_minutes is not None:
            self._values["block_duration_minutes"] = block_duration_minutes

    @builtins.property
    def allocation_strategy(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#allocation_strategy EmrCluster#allocation_strategy}.'''
        result = self._values.get("allocation_strategy")
        assert result is not None, "Required property 'allocation_strategy' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def timeout_action(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#timeout_action EmrCluster#timeout_action}.'''
        result = self._values.get("timeout_action")
        assert result is not None, "Required property 'timeout_action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def timeout_duration_minutes(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#timeout_duration_minutes EmrCluster#timeout_duration_minutes}.'''
        result = self._values.get("timeout_duration_minutes")
        assert result is not None, "Required property 'timeout_duration_minutes' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def block_duration_minutes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#block_duration_minutes EmrCluster#block_duration_minutes}.'''
        result = self._values.get("block_duration_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmrClusterCoreInstanceFleetLaunchSpecificationsSpotSpecification(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EmrClusterCoreInstanceFleetLaunchSpecificationsSpotSpecificationList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.emrCluster.EmrClusterCoreInstanceFleetLaunchSpecificationsSpotSpecificationList",
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
    ) -> "EmrClusterCoreInstanceFleetLaunchSpecificationsSpotSpecificationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EmrClusterCoreInstanceFleetLaunchSpecificationsSpotSpecificationOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterCoreInstanceFleetLaunchSpecificationsSpotSpecification]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterCoreInstanceFleetLaunchSpecificationsSpotSpecification]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterCoreInstanceFleetLaunchSpecificationsSpotSpecification]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterCoreInstanceFleetLaunchSpecificationsSpotSpecification]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EmrClusterCoreInstanceFleetLaunchSpecificationsSpotSpecificationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.emrCluster.EmrClusterCoreInstanceFleetLaunchSpecificationsSpotSpecificationOutputReference",
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

    @jsii.member(jsii_name="resetBlockDurationMinutes")
    def reset_block_duration_minutes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBlockDurationMinutes", []))

    @builtins.property
    @jsii.member(jsii_name="allocationStrategyInput")
    def allocation_strategy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "allocationStrategyInput"))

    @builtins.property
    @jsii.member(jsii_name="blockDurationMinutesInput")
    def block_duration_minutes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "blockDurationMinutesInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutActionInput")
    def timeout_action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeoutActionInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutDurationMinutesInput")
    def timeout_duration_minutes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timeoutDurationMinutesInput"))

    @builtins.property
    @jsii.member(jsii_name="allocationStrategy")
    def allocation_strategy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "allocationStrategy"))

    @allocation_strategy.setter
    def allocation_strategy(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allocationStrategy", value)

    @builtins.property
    @jsii.member(jsii_name="blockDurationMinutes")
    def block_duration_minutes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "blockDurationMinutes"))

    @block_duration_minutes.setter
    def block_duration_minutes(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "blockDurationMinutes", value)

    @builtins.property
    @jsii.member(jsii_name="timeoutAction")
    def timeout_action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timeoutAction"))

    @timeout_action.setter
    def timeout_action(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeoutAction", value)

    @builtins.property
    @jsii.member(jsii_name="timeoutDurationMinutes")
    def timeout_duration_minutes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "timeoutDurationMinutes"))

    @timeout_duration_minutes.setter
    def timeout_duration_minutes(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeoutDurationMinutes", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EmrClusterCoreInstanceFleetLaunchSpecificationsSpotSpecification, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EmrClusterCoreInstanceFleetLaunchSpecificationsSpotSpecification, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EmrClusterCoreInstanceFleetLaunchSpecificationsSpotSpecification, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[EmrClusterCoreInstanceFleetLaunchSpecificationsSpotSpecification, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EmrClusterCoreInstanceFleetOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.emrCluster.EmrClusterCoreInstanceFleetOutputReference",
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

    @jsii.member(jsii_name="putInstanceTypeConfigs")
    def put_instance_type_configs(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EmrClusterCoreInstanceFleetInstanceTypeConfigs, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EmrClusterCoreInstanceFleetInstanceTypeConfigs, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putInstanceTypeConfigs", [value]))

    @jsii.member(jsii_name="putLaunchSpecifications")
    def put_launch_specifications(
        self,
        *,
        on_demand_specification: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EmrClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecification, typing.Dict[str, typing.Any]]]]] = None,
        spot_specification: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EmrClusterCoreInstanceFleetLaunchSpecificationsSpotSpecification, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param on_demand_specification: on_demand_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#on_demand_specification EmrCluster#on_demand_specification}
        :param spot_specification: spot_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#spot_specification EmrCluster#spot_specification}
        '''
        value = EmrClusterCoreInstanceFleetLaunchSpecifications(
            on_demand_specification=on_demand_specification,
            spot_specification=spot_specification,
        )

        return typing.cast(None, jsii.invoke(self, "putLaunchSpecifications", [value]))

    @jsii.member(jsii_name="resetInstanceTypeConfigs")
    def reset_instance_type_configs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceTypeConfigs", []))

    @jsii.member(jsii_name="resetLaunchSpecifications")
    def reset_launch_specifications(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLaunchSpecifications", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetTargetOnDemandCapacity")
    def reset_target_on_demand_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetOnDemandCapacity", []))

    @jsii.member(jsii_name="resetTargetSpotCapacity")
    def reset_target_spot_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetSpotCapacity", []))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="instanceTypeConfigs")
    def instance_type_configs(
        self,
    ) -> EmrClusterCoreInstanceFleetInstanceTypeConfigsList:
        return typing.cast(EmrClusterCoreInstanceFleetInstanceTypeConfigsList, jsii.get(self, "instanceTypeConfigs"))

    @builtins.property
    @jsii.member(jsii_name="launchSpecifications")
    def launch_specifications(
        self,
    ) -> EmrClusterCoreInstanceFleetLaunchSpecificationsOutputReference:
        return typing.cast(EmrClusterCoreInstanceFleetLaunchSpecificationsOutputReference, jsii.get(self, "launchSpecifications"))

    @builtins.property
    @jsii.member(jsii_name="provisionedOnDemandCapacity")
    def provisioned_on_demand_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "provisionedOnDemandCapacity"))

    @builtins.property
    @jsii.member(jsii_name="provisionedSpotCapacity")
    def provisioned_spot_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "provisionedSpotCapacity"))

    @builtins.property
    @jsii.member(jsii_name="instanceTypeConfigsInput")
    def instance_type_configs_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterCoreInstanceFleetInstanceTypeConfigs]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterCoreInstanceFleetInstanceTypeConfigs]]], jsii.get(self, "instanceTypeConfigsInput"))

    @builtins.property
    @jsii.member(jsii_name="launchSpecificationsInput")
    def launch_specifications_input(
        self,
    ) -> typing.Optional[EmrClusterCoreInstanceFleetLaunchSpecifications]:
        return typing.cast(typing.Optional[EmrClusterCoreInstanceFleetLaunchSpecifications], jsii.get(self, "launchSpecificationsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="targetOnDemandCapacityInput")
    def target_on_demand_capacity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "targetOnDemandCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="targetSpotCapacityInput")
    def target_spot_capacity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "targetSpotCapacityInput"))

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
    @jsii.member(jsii_name="targetOnDemandCapacity")
    def target_on_demand_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "targetOnDemandCapacity"))

    @target_on_demand_capacity.setter
    def target_on_demand_capacity(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetOnDemandCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="targetSpotCapacity")
    def target_spot_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "targetSpotCapacity"))

    @target_spot_capacity.setter
    def target_spot_capacity(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetSpotCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[EmrClusterCoreInstanceFleet]:
        return typing.cast(typing.Optional[EmrClusterCoreInstanceFleet], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EmrClusterCoreInstanceFleet],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[EmrClusterCoreInstanceFleet]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.emrCluster.EmrClusterCoreInstanceGroup",
    jsii_struct_bases=[],
    name_mapping={
        "instance_type": "instanceType",
        "autoscaling_policy": "autoscalingPolicy",
        "bid_price": "bidPrice",
        "ebs_config": "ebsConfig",
        "instance_count": "instanceCount",
        "name": "name",
    },
)
class EmrClusterCoreInstanceGroup:
    def __init__(
        self,
        *,
        instance_type: builtins.str,
        autoscaling_policy: typing.Optional[builtins.str] = None,
        bid_price: typing.Optional[builtins.str] = None,
        ebs_config: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EmrClusterCoreInstanceGroupEbsConfig", typing.Dict[str, typing.Any]]]]] = None,
        instance_count: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param instance_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#instance_type EmrCluster#instance_type}.
        :param autoscaling_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#autoscaling_policy EmrCluster#autoscaling_policy}.
        :param bid_price: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#bid_price EmrCluster#bid_price}.
        :param ebs_config: ebs_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#ebs_config EmrCluster#ebs_config}
        :param instance_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#instance_count EmrCluster#instance_count}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#name EmrCluster#name}.
        '''
        if __debug__:
            def stub(
                *,
                instance_type: builtins.str,
                autoscaling_policy: typing.Optional[builtins.str] = None,
                bid_price: typing.Optional[builtins.str] = None,
                ebs_config: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EmrClusterCoreInstanceGroupEbsConfig, typing.Dict[str, typing.Any]]]]] = None,
                instance_count: typing.Optional[jsii.Number] = None,
                name: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            check_type(argname="argument autoscaling_policy", value=autoscaling_policy, expected_type=type_hints["autoscaling_policy"])
            check_type(argname="argument bid_price", value=bid_price, expected_type=type_hints["bid_price"])
            check_type(argname="argument ebs_config", value=ebs_config, expected_type=type_hints["ebs_config"])
            check_type(argname="argument instance_count", value=instance_count, expected_type=type_hints["instance_count"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "instance_type": instance_type,
        }
        if autoscaling_policy is not None:
            self._values["autoscaling_policy"] = autoscaling_policy
        if bid_price is not None:
            self._values["bid_price"] = bid_price
        if ebs_config is not None:
            self._values["ebs_config"] = ebs_config
        if instance_count is not None:
            self._values["instance_count"] = instance_count
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def instance_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#instance_type EmrCluster#instance_type}.'''
        result = self._values.get("instance_type")
        assert result is not None, "Required property 'instance_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def autoscaling_policy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#autoscaling_policy EmrCluster#autoscaling_policy}.'''
        result = self._values.get("autoscaling_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bid_price(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#bid_price EmrCluster#bid_price}.'''
        result = self._values.get("bid_price")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ebs_config(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EmrClusterCoreInstanceGroupEbsConfig"]]]:
        '''ebs_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#ebs_config EmrCluster#ebs_config}
        '''
        result = self._values.get("ebs_config")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EmrClusterCoreInstanceGroupEbsConfig"]]], result)

    @builtins.property
    def instance_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#instance_count EmrCluster#instance_count}.'''
        result = self._values.get("instance_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#name EmrCluster#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmrClusterCoreInstanceGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.emrCluster.EmrClusterCoreInstanceGroupEbsConfig",
    jsii_struct_bases=[],
    name_mapping={
        "size": "size",
        "type": "type",
        "iops": "iops",
        "throughput": "throughput",
        "volumes_per_instance": "volumesPerInstance",
    },
)
class EmrClusterCoreInstanceGroupEbsConfig:
    def __init__(
        self,
        *,
        size: jsii.Number,
        type: builtins.str,
        iops: typing.Optional[jsii.Number] = None,
        throughput: typing.Optional[jsii.Number] = None,
        volumes_per_instance: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#size EmrCluster#size}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#type EmrCluster#type}.
        :param iops: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#iops EmrCluster#iops}.
        :param throughput: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#throughput EmrCluster#throughput}.
        :param volumes_per_instance: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#volumes_per_instance EmrCluster#volumes_per_instance}.
        '''
        if __debug__:
            def stub(
                *,
                size: jsii.Number,
                type: builtins.str,
                iops: typing.Optional[jsii.Number] = None,
                throughput: typing.Optional[jsii.Number] = None,
                volumes_per_instance: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument size", value=size, expected_type=type_hints["size"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument iops", value=iops, expected_type=type_hints["iops"])
            check_type(argname="argument throughput", value=throughput, expected_type=type_hints["throughput"])
            check_type(argname="argument volumes_per_instance", value=volumes_per_instance, expected_type=type_hints["volumes_per_instance"])
        self._values: typing.Dict[str, typing.Any] = {
            "size": size,
            "type": type,
        }
        if iops is not None:
            self._values["iops"] = iops
        if throughput is not None:
            self._values["throughput"] = throughput
        if volumes_per_instance is not None:
            self._values["volumes_per_instance"] = volumes_per_instance

    @builtins.property
    def size(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#size EmrCluster#size}.'''
        result = self._values.get("size")
        assert result is not None, "Required property 'size' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#type EmrCluster#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def iops(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#iops EmrCluster#iops}.'''
        result = self._values.get("iops")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def throughput(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#throughput EmrCluster#throughput}.'''
        result = self._values.get("throughput")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def volumes_per_instance(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#volumes_per_instance EmrCluster#volumes_per_instance}.'''
        result = self._values.get("volumes_per_instance")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmrClusterCoreInstanceGroupEbsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EmrClusterCoreInstanceGroupEbsConfigList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.emrCluster.EmrClusterCoreInstanceGroupEbsConfigList",
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
    ) -> "EmrClusterCoreInstanceGroupEbsConfigOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EmrClusterCoreInstanceGroupEbsConfigOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterCoreInstanceGroupEbsConfig]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterCoreInstanceGroupEbsConfig]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterCoreInstanceGroupEbsConfig]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterCoreInstanceGroupEbsConfig]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EmrClusterCoreInstanceGroupEbsConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.emrCluster.EmrClusterCoreInstanceGroupEbsConfigOutputReference",
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

    @jsii.member(jsii_name="resetIops")
    def reset_iops(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIops", []))

    @jsii.member(jsii_name="resetThroughput")
    def reset_throughput(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThroughput", []))

    @jsii.member(jsii_name="resetVolumesPerInstance")
    def reset_volumes_per_instance(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVolumesPerInstance", []))

    @builtins.property
    @jsii.member(jsii_name="iopsInput")
    def iops_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "iopsInput"))

    @builtins.property
    @jsii.member(jsii_name="sizeInput")
    def size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sizeInput"))

    @builtins.property
    @jsii.member(jsii_name="throughputInput")
    def throughput_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "throughputInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="volumesPerInstanceInput")
    def volumes_per_instance_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "volumesPerInstanceInput"))

    @builtins.property
    @jsii.member(jsii_name="iops")
    def iops(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "iops"))

    @iops.setter
    def iops(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iops", value)

    @builtins.property
    @jsii.member(jsii_name="size")
    def size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "size"))

    @size.setter
    def size(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "size", value)

    @builtins.property
    @jsii.member(jsii_name="throughput")
    def throughput(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "throughput"))

    @throughput.setter
    def throughput(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "throughput", value)

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
    @jsii.member(jsii_name="volumesPerInstance")
    def volumes_per_instance(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "volumesPerInstance"))

    @volumes_per_instance.setter
    def volumes_per_instance(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumesPerInstance", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EmrClusterCoreInstanceGroupEbsConfig, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EmrClusterCoreInstanceGroupEbsConfig, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EmrClusterCoreInstanceGroupEbsConfig, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[EmrClusterCoreInstanceGroupEbsConfig, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EmrClusterCoreInstanceGroupOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.emrCluster.EmrClusterCoreInstanceGroupOutputReference",
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

    @jsii.member(jsii_name="putEbsConfig")
    def put_ebs_config(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EmrClusterCoreInstanceGroupEbsConfig, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EmrClusterCoreInstanceGroupEbsConfig, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEbsConfig", [value]))

    @jsii.member(jsii_name="resetAutoscalingPolicy")
    def reset_autoscaling_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoscalingPolicy", []))

    @jsii.member(jsii_name="resetBidPrice")
    def reset_bid_price(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBidPrice", []))

    @jsii.member(jsii_name="resetEbsConfig")
    def reset_ebs_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEbsConfig", []))

    @jsii.member(jsii_name="resetInstanceCount")
    def reset_instance_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceCount", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="ebsConfig")
    def ebs_config(self) -> EmrClusterCoreInstanceGroupEbsConfigList:
        return typing.cast(EmrClusterCoreInstanceGroupEbsConfigList, jsii.get(self, "ebsConfig"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="autoscalingPolicyInput")
    def autoscaling_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "autoscalingPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="bidPriceInput")
    def bid_price_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bidPriceInput"))

    @builtins.property
    @jsii.member(jsii_name="ebsConfigInput")
    def ebs_config_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterCoreInstanceGroupEbsConfig]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterCoreInstanceGroupEbsConfig]]], jsii.get(self, "ebsConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceCountInput")
    def instance_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "instanceCountInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceTypeInput")
    def instance_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="autoscalingPolicy")
    def autoscaling_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "autoscalingPolicy"))

    @autoscaling_policy.setter
    def autoscaling_policy(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoscalingPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="bidPrice")
    def bid_price(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bidPrice"))

    @bid_price.setter
    def bid_price(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bidPrice", value)

    @builtins.property
    @jsii.member(jsii_name="instanceCount")
    def instance_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "instanceCount"))

    @instance_count.setter
    def instance_count(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceCount", value)

    @builtins.property
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceType"))

    @instance_type.setter
    def instance_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceType", value)

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
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[EmrClusterCoreInstanceGroup]:
        return typing.cast(typing.Optional[EmrClusterCoreInstanceGroup], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EmrClusterCoreInstanceGroup],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[EmrClusterCoreInstanceGroup]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.emrCluster.EmrClusterEc2Attributes",
    jsii_struct_bases=[],
    name_mapping={
        "instance_profile": "instanceProfile",
        "additional_master_security_groups": "additionalMasterSecurityGroups",
        "additional_slave_security_groups": "additionalSlaveSecurityGroups",
        "emr_managed_master_security_group": "emrManagedMasterSecurityGroup",
        "emr_managed_slave_security_group": "emrManagedSlaveSecurityGroup",
        "key_name": "keyName",
        "service_access_security_group": "serviceAccessSecurityGroup",
        "subnet_id": "subnetId",
        "subnet_ids": "subnetIds",
    },
)
class EmrClusterEc2Attributes:
    def __init__(
        self,
        *,
        instance_profile: builtins.str,
        additional_master_security_groups: typing.Optional[builtins.str] = None,
        additional_slave_security_groups: typing.Optional[builtins.str] = None,
        emr_managed_master_security_group: typing.Optional[builtins.str] = None,
        emr_managed_slave_security_group: typing.Optional[builtins.str] = None,
        key_name: typing.Optional[builtins.str] = None,
        service_access_security_group: typing.Optional[builtins.str] = None,
        subnet_id: typing.Optional[builtins.str] = None,
        subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param instance_profile: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#instance_profile EmrCluster#instance_profile}.
        :param additional_master_security_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#additional_master_security_groups EmrCluster#additional_master_security_groups}.
        :param additional_slave_security_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#additional_slave_security_groups EmrCluster#additional_slave_security_groups}.
        :param emr_managed_master_security_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#emr_managed_master_security_group EmrCluster#emr_managed_master_security_group}.
        :param emr_managed_slave_security_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#emr_managed_slave_security_group EmrCluster#emr_managed_slave_security_group}.
        :param key_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#key_name EmrCluster#key_name}.
        :param service_access_security_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#service_access_security_group EmrCluster#service_access_security_group}.
        :param subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#subnet_id EmrCluster#subnet_id}.
        :param subnet_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#subnet_ids EmrCluster#subnet_ids}.
        '''
        if __debug__:
            def stub(
                *,
                instance_profile: builtins.str,
                additional_master_security_groups: typing.Optional[builtins.str] = None,
                additional_slave_security_groups: typing.Optional[builtins.str] = None,
                emr_managed_master_security_group: typing.Optional[builtins.str] = None,
                emr_managed_slave_security_group: typing.Optional[builtins.str] = None,
                key_name: typing.Optional[builtins.str] = None,
                service_access_security_group: typing.Optional[builtins.str] = None,
                subnet_id: typing.Optional[builtins.str] = None,
                subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument instance_profile", value=instance_profile, expected_type=type_hints["instance_profile"])
            check_type(argname="argument additional_master_security_groups", value=additional_master_security_groups, expected_type=type_hints["additional_master_security_groups"])
            check_type(argname="argument additional_slave_security_groups", value=additional_slave_security_groups, expected_type=type_hints["additional_slave_security_groups"])
            check_type(argname="argument emr_managed_master_security_group", value=emr_managed_master_security_group, expected_type=type_hints["emr_managed_master_security_group"])
            check_type(argname="argument emr_managed_slave_security_group", value=emr_managed_slave_security_group, expected_type=type_hints["emr_managed_slave_security_group"])
            check_type(argname="argument key_name", value=key_name, expected_type=type_hints["key_name"])
            check_type(argname="argument service_access_security_group", value=service_access_security_group, expected_type=type_hints["service_access_security_group"])
            check_type(argname="argument subnet_id", value=subnet_id, expected_type=type_hints["subnet_id"])
            check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
        self._values: typing.Dict[str, typing.Any] = {
            "instance_profile": instance_profile,
        }
        if additional_master_security_groups is not None:
            self._values["additional_master_security_groups"] = additional_master_security_groups
        if additional_slave_security_groups is not None:
            self._values["additional_slave_security_groups"] = additional_slave_security_groups
        if emr_managed_master_security_group is not None:
            self._values["emr_managed_master_security_group"] = emr_managed_master_security_group
        if emr_managed_slave_security_group is not None:
            self._values["emr_managed_slave_security_group"] = emr_managed_slave_security_group
        if key_name is not None:
            self._values["key_name"] = key_name
        if service_access_security_group is not None:
            self._values["service_access_security_group"] = service_access_security_group
        if subnet_id is not None:
            self._values["subnet_id"] = subnet_id
        if subnet_ids is not None:
            self._values["subnet_ids"] = subnet_ids

    @builtins.property
    def instance_profile(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#instance_profile EmrCluster#instance_profile}.'''
        result = self._values.get("instance_profile")
        assert result is not None, "Required property 'instance_profile' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def additional_master_security_groups(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#additional_master_security_groups EmrCluster#additional_master_security_groups}.'''
        result = self._values.get("additional_master_security_groups")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def additional_slave_security_groups(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#additional_slave_security_groups EmrCluster#additional_slave_security_groups}.'''
        result = self._values.get("additional_slave_security_groups")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def emr_managed_master_security_group(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#emr_managed_master_security_group EmrCluster#emr_managed_master_security_group}.'''
        result = self._values.get("emr_managed_master_security_group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def emr_managed_slave_security_group(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#emr_managed_slave_security_group EmrCluster#emr_managed_slave_security_group}.'''
        result = self._values.get("emr_managed_slave_security_group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#key_name EmrCluster#key_name}.'''
        result = self._values.get("key_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_access_security_group(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#service_access_security_group EmrCluster#service_access_security_group}.'''
        result = self._values.get("service_access_security_group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subnet_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#subnet_id EmrCluster#subnet_id}.'''
        result = self._values.get("subnet_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#subnet_ids EmrCluster#subnet_ids}.'''
        result = self._values.get("subnet_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmrClusterEc2Attributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EmrClusterEc2AttributesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.emrCluster.EmrClusterEc2AttributesOutputReference",
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

    @jsii.member(jsii_name="resetAdditionalMasterSecurityGroups")
    def reset_additional_master_security_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdditionalMasterSecurityGroups", []))

    @jsii.member(jsii_name="resetAdditionalSlaveSecurityGroups")
    def reset_additional_slave_security_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdditionalSlaveSecurityGroups", []))

    @jsii.member(jsii_name="resetEmrManagedMasterSecurityGroup")
    def reset_emr_managed_master_security_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmrManagedMasterSecurityGroup", []))

    @jsii.member(jsii_name="resetEmrManagedSlaveSecurityGroup")
    def reset_emr_managed_slave_security_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmrManagedSlaveSecurityGroup", []))

    @jsii.member(jsii_name="resetKeyName")
    def reset_key_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyName", []))

    @jsii.member(jsii_name="resetServiceAccessSecurityGroup")
    def reset_service_access_security_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceAccessSecurityGroup", []))

    @jsii.member(jsii_name="resetSubnetId")
    def reset_subnet_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubnetId", []))

    @jsii.member(jsii_name="resetSubnetIds")
    def reset_subnet_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubnetIds", []))

    @builtins.property
    @jsii.member(jsii_name="additionalMasterSecurityGroupsInput")
    def additional_master_security_groups_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "additionalMasterSecurityGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="additionalSlaveSecurityGroupsInput")
    def additional_slave_security_groups_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "additionalSlaveSecurityGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="emrManagedMasterSecurityGroupInput")
    def emr_managed_master_security_group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emrManagedMasterSecurityGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="emrManagedSlaveSecurityGroupInput")
    def emr_managed_slave_security_group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emrManagedSlaveSecurityGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceProfileInput")
    def instance_profile_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceProfileInput"))

    @builtins.property
    @jsii.member(jsii_name="keyNameInput")
    def key_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyNameInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceAccessSecurityGroupInput")
    def service_access_security_group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceAccessSecurityGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetIdInput")
    def subnet_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetIdsInput")
    def subnet_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "subnetIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="additionalMasterSecurityGroups")
    def additional_master_security_groups(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "additionalMasterSecurityGroups"))

    @additional_master_security_groups.setter
    def additional_master_security_groups(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "additionalMasterSecurityGroups", value)

    @builtins.property
    @jsii.member(jsii_name="additionalSlaveSecurityGroups")
    def additional_slave_security_groups(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "additionalSlaveSecurityGroups"))

    @additional_slave_security_groups.setter
    def additional_slave_security_groups(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "additionalSlaveSecurityGroups", value)

    @builtins.property
    @jsii.member(jsii_name="emrManagedMasterSecurityGroup")
    def emr_managed_master_security_group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "emrManagedMasterSecurityGroup"))

    @emr_managed_master_security_group.setter
    def emr_managed_master_security_group(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emrManagedMasterSecurityGroup", value)

    @builtins.property
    @jsii.member(jsii_name="emrManagedSlaveSecurityGroup")
    def emr_managed_slave_security_group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "emrManagedSlaveSecurityGroup"))

    @emr_managed_slave_security_group.setter
    def emr_managed_slave_security_group(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emrManagedSlaveSecurityGroup", value)

    @builtins.property
    @jsii.member(jsii_name="instanceProfile")
    def instance_profile(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceProfile"))

    @instance_profile.setter
    def instance_profile(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceProfile", value)

    @builtins.property
    @jsii.member(jsii_name="keyName")
    def key_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyName"))

    @key_name.setter
    def key_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyName", value)

    @builtins.property
    @jsii.member(jsii_name="serviceAccessSecurityGroup")
    def service_access_security_group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceAccessSecurityGroup"))

    @service_access_security_group.setter
    def service_access_security_group(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceAccessSecurityGroup", value)

    @builtins.property
    @jsii.member(jsii_name="subnetId")
    def subnet_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subnetId"))

    @subnet_id.setter
    def subnet_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetId", value)

    @builtins.property
    @jsii.member(jsii_name="subnetIds")
    def subnet_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnetIds"))

    @subnet_ids.setter
    def subnet_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetIds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[EmrClusterEc2Attributes]:
        return typing.cast(typing.Optional[EmrClusterEc2Attributes], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[EmrClusterEc2Attributes]) -> None:
        if __debug__:
            def stub(value: typing.Optional[EmrClusterEc2Attributes]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.emrCluster.EmrClusterKerberosAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "kdc_admin_password": "kdcAdminPassword",
        "realm": "realm",
        "ad_domain_join_password": "adDomainJoinPassword",
        "ad_domain_join_user": "adDomainJoinUser",
        "cross_realm_trust_principal_password": "crossRealmTrustPrincipalPassword",
    },
)
class EmrClusterKerberosAttributes:
    def __init__(
        self,
        *,
        kdc_admin_password: builtins.str,
        realm: builtins.str,
        ad_domain_join_password: typing.Optional[builtins.str] = None,
        ad_domain_join_user: typing.Optional[builtins.str] = None,
        cross_realm_trust_principal_password: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param kdc_admin_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#kdc_admin_password EmrCluster#kdc_admin_password}.
        :param realm: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#realm EmrCluster#realm}.
        :param ad_domain_join_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#ad_domain_join_password EmrCluster#ad_domain_join_password}.
        :param ad_domain_join_user: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#ad_domain_join_user EmrCluster#ad_domain_join_user}.
        :param cross_realm_trust_principal_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#cross_realm_trust_principal_password EmrCluster#cross_realm_trust_principal_password}.
        '''
        if __debug__:
            def stub(
                *,
                kdc_admin_password: builtins.str,
                realm: builtins.str,
                ad_domain_join_password: typing.Optional[builtins.str] = None,
                ad_domain_join_user: typing.Optional[builtins.str] = None,
                cross_realm_trust_principal_password: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument kdc_admin_password", value=kdc_admin_password, expected_type=type_hints["kdc_admin_password"])
            check_type(argname="argument realm", value=realm, expected_type=type_hints["realm"])
            check_type(argname="argument ad_domain_join_password", value=ad_domain_join_password, expected_type=type_hints["ad_domain_join_password"])
            check_type(argname="argument ad_domain_join_user", value=ad_domain_join_user, expected_type=type_hints["ad_domain_join_user"])
            check_type(argname="argument cross_realm_trust_principal_password", value=cross_realm_trust_principal_password, expected_type=type_hints["cross_realm_trust_principal_password"])
        self._values: typing.Dict[str, typing.Any] = {
            "kdc_admin_password": kdc_admin_password,
            "realm": realm,
        }
        if ad_domain_join_password is not None:
            self._values["ad_domain_join_password"] = ad_domain_join_password
        if ad_domain_join_user is not None:
            self._values["ad_domain_join_user"] = ad_domain_join_user
        if cross_realm_trust_principal_password is not None:
            self._values["cross_realm_trust_principal_password"] = cross_realm_trust_principal_password

    @builtins.property
    def kdc_admin_password(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#kdc_admin_password EmrCluster#kdc_admin_password}.'''
        result = self._values.get("kdc_admin_password")
        assert result is not None, "Required property 'kdc_admin_password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def realm(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#realm EmrCluster#realm}.'''
        result = self._values.get("realm")
        assert result is not None, "Required property 'realm' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ad_domain_join_password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#ad_domain_join_password EmrCluster#ad_domain_join_password}.'''
        result = self._values.get("ad_domain_join_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ad_domain_join_user(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#ad_domain_join_user EmrCluster#ad_domain_join_user}.'''
        result = self._values.get("ad_domain_join_user")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cross_realm_trust_principal_password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#cross_realm_trust_principal_password EmrCluster#cross_realm_trust_principal_password}.'''
        result = self._values.get("cross_realm_trust_principal_password")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmrClusterKerberosAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EmrClusterKerberosAttributesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.emrCluster.EmrClusterKerberosAttributesOutputReference",
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

    @jsii.member(jsii_name="resetAdDomainJoinPassword")
    def reset_ad_domain_join_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdDomainJoinPassword", []))

    @jsii.member(jsii_name="resetAdDomainJoinUser")
    def reset_ad_domain_join_user(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdDomainJoinUser", []))

    @jsii.member(jsii_name="resetCrossRealmTrustPrincipalPassword")
    def reset_cross_realm_trust_principal_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCrossRealmTrustPrincipalPassword", []))

    @builtins.property
    @jsii.member(jsii_name="adDomainJoinPasswordInput")
    def ad_domain_join_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "adDomainJoinPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="adDomainJoinUserInput")
    def ad_domain_join_user_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "adDomainJoinUserInput"))

    @builtins.property
    @jsii.member(jsii_name="crossRealmTrustPrincipalPasswordInput")
    def cross_realm_trust_principal_password_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "crossRealmTrustPrincipalPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="kdcAdminPasswordInput")
    def kdc_admin_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kdcAdminPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="realmInput")
    def realm_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "realmInput"))

    @builtins.property
    @jsii.member(jsii_name="adDomainJoinPassword")
    def ad_domain_join_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "adDomainJoinPassword"))

    @ad_domain_join_password.setter
    def ad_domain_join_password(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adDomainJoinPassword", value)

    @builtins.property
    @jsii.member(jsii_name="adDomainJoinUser")
    def ad_domain_join_user(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "adDomainJoinUser"))

    @ad_domain_join_user.setter
    def ad_domain_join_user(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adDomainJoinUser", value)

    @builtins.property
    @jsii.member(jsii_name="crossRealmTrustPrincipalPassword")
    def cross_realm_trust_principal_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "crossRealmTrustPrincipalPassword"))

    @cross_realm_trust_principal_password.setter
    def cross_realm_trust_principal_password(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "crossRealmTrustPrincipalPassword", value)

    @builtins.property
    @jsii.member(jsii_name="kdcAdminPassword")
    def kdc_admin_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kdcAdminPassword"))

    @kdc_admin_password.setter
    def kdc_admin_password(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kdcAdminPassword", value)

    @builtins.property
    @jsii.member(jsii_name="realm")
    def realm(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "realm"))

    @realm.setter
    def realm(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "realm", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[EmrClusterKerberosAttributes]:
        return typing.cast(typing.Optional[EmrClusterKerberosAttributes], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EmrClusterKerberosAttributes],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[EmrClusterKerberosAttributes]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.emrCluster.EmrClusterMasterInstanceFleet",
    jsii_struct_bases=[],
    name_mapping={
        "instance_type_configs": "instanceTypeConfigs",
        "launch_specifications": "launchSpecifications",
        "name": "name",
        "target_on_demand_capacity": "targetOnDemandCapacity",
        "target_spot_capacity": "targetSpotCapacity",
    },
)
class EmrClusterMasterInstanceFleet:
    def __init__(
        self,
        *,
        instance_type_configs: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EmrClusterMasterInstanceFleetInstanceTypeConfigs", typing.Dict[str, typing.Any]]]]] = None,
        launch_specifications: typing.Optional[typing.Union["EmrClusterMasterInstanceFleetLaunchSpecifications", typing.Dict[str, typing.Any]]] = None,
        name: typing.Optional[builtins.str] = None,
        target_on_demand_capacity: typing.Optional[jsii.Number] = None,
        target_spot_capacity: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param instance_type_configs: instance_type_configs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#instance_type_configs EmrCluster#instance_type_configs}
        :param launch_specifications: launch_specifications block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#launch_specifications EmrCluster#launch_specifications}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#name EmrCluster#name}.
        :param target_on_demand_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#target_on_demand_capacity EmrCluster#target_on_demand_capacity}.
        :param target_spot_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#target_spot_capacity EmrCluster#target_spot_capacity}.
        '''
        if isinstance(launch_specifications, dict):
            launch_specifications = EmrClusterMasterInstanceFleetLaunchSpecifications(**launch_specifications)
        if __debug__:
            def stub(
                *,
                instance_type_configs: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EmrClusterMasterInstanceFleetInstanceTypeConfigs, typing.Dict[str, typing.Any]]]]] = None,
                launch_specifications: typing.Optional[typing.Union[EmrClusterMasterInstanceFleetLaunchSpecifications, typing.Dict[str, typing.Any]]] = None,
                name: typing.Optional[builtins.str] = None,
                target_on_demand_capacity: typing.Optional[jsii.Number] = None,
                target_spot_capacity: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument instance_type_configs", value=instance_type_configs, expected_type=type_hints["instance_type_configs"])
            check_type(argname="argument launch_specifications", value=launch_specifications, expected_type=type_hints["launch_specifications"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument target_on_demand_capacity", value=target_on_demand_capacity, expected_type=type_hints["target_on_demand_capacity"])
            check_type(argname="argument target_spot_capacity", value=target_spot_capacity, expected_type=type_hints["target_spot_capacity"])
        self._values: typing.Dict[str, typing.Any] = {}
        if instance_type_configs is not None:
            self._values["instance_type_configs"] = instance_type_configs
        if launch_specifications is not None:
            self._values["launch_specifications"] = launch_specifications
        if name is not None:
            self._values["name"] = name
        if target_on_demand_capacity is not None:
            self._values["target_on_demand_capacity"] = target_on_demand_capacity
        if target_spot_capacity is not None:
            self._values["target_spot_capacity"] = target_spot_capacity

    @builtins.property
    def instance_type_configs(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EmrClusterMasterInstanceFleetInstanceTypeConfigs"]]]:
        '''instance_type_configs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#instance_type_configs EmrCluster#instance_type_configs}
        '''
        result = self._values.get("instance_type_configs")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EmrClusterMasterInstanceFleetInstanceTypeConfigs"]]], result)

    @builtins.property
    def launch_specifications(
        self,
    ) -> typing.Optional["EmrClusterMasterInstanceFleetLaunchSpecifications"]:
        '''launch_specifications block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#launch_specifications EmrCluster#launch_specifications}
        '''
        result = self._values.get("launch_specifications")
        return typing.cast(typing.Optional["EmrClusterMasterInstanceFleetLaunchSpecifications"], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#name EmrCluster#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_on_demand_capacity(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#target_on_demand_capacity EmrCluster#target_on_demand_capacity}.'''
        result = self._values.get("target_on_demand_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def target_spot_capacity(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#target_spot_capacity EmrCluster#target_spot_capacity}.'''
        result = self._values.get("target_spot_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmrClusterMasterInstanceFleet(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.emrCluster.EmrClusterMasterInstanceFleetInstanceTypeConfigs",
    jsii_struct_bases=[],
    name_mapping={
        "instance_type": "instanceType",
        "bid_price": "bidPrice",
        "bid_price_as_percentage_of_on_demand_price": "bidPriceAsPercentageOfOnDemandPrice",
        "configurations": "configurations",
        "ebs_config": "ebsConfig",
        "weighted_capacity": "weightedCapacity",
    },
)
class EmrClusterMasterInstanceFleetInstanceTypeConfigs:
    def __init__(
        self,
        *,
        instance_type: builtins.str,
        bid_price: typing.Optional[builtins.str] = None,
        bid_price_as_percentage_of_on_demand_price: typing.Optional[jsii.Number] = None,
        configurations: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EmrClusterMasterInstanceFleetInstanceTypeConfigsConfigurations", typing.Dict[str, typing.Any]]]]] = None,
        ebs_config: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EmrClusterMasterInstanceFleetInstanceTypeConfigsEbsConfig", typing.Dict[str, typing.Any]]]]] = None,
        weighted_capacity: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param instance_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#instance_type EmrCluster#instance_type}.
        :param bid_price: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#bid_price EmrCluster#bid_price}.
        :param bid_price_as_percentage_of_on_demand_price: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#bid_price_as_percentage_of_on_demand_price EmrCluster#bid_price_as_percentage_of_on_demand_price}.
        :param configurations: configurations block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#configurations EmrCluster#configurations}
        :param ebs_config: ebs_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#ebs_config EmrCluster#ebs_config}
        :param weighted_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#weighted_capacity EmrCluster#weighted_capacity}.
        '''
        if __debug__:
            def stub(
                *,
                instance_type: builtins.str,
                bid_price: typing.Optional[builtins.str] = None,
                bid_price_as_percentage_of_on_demand_price: typing.Optional[jsii.Number] = None,
                configurations: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EmrClusterMasterInstanceFleetInstanceTypeConfigsConfigurations, typing.Dict[str, typing.Any]]]]] = None,
                ebs_config: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EmrClusterMasterInstanceFleetInstanceTypeConfigsEbsConfig, typing.Dict[str, typing.Any]]]]] = None,
                weighted_capacity: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            check_type(argname="argument bid_price", value=bid_price, expected_type=type_hints["bid_price"])
            check_type(argname="argument bid_price_as_percentage_of_on_demand_price", value=bid_price_as_percentage_of_on_demand_price, expected_type=type_hints["bid_price_as_percentage_of_on_demand_price"])
            check_type(argname="argument configurations", value=configurations, expected_type=type_hints["configurations"])
            check_type(argname="argument ebs_config", value=ebs_config, expected_type=type_hints["ebs_config"])
            check_type(argname="argument weighted_capacity", value=weighted_capacity, expected_type=type_hints["weighted_capacity"])
        self._values: typing.Dict[str, typing.Any] = {
            "instance_type": instance_type,
        }
        if bid_price is not None:
            self._values["bid_price"] = bid_price
        if bid_price_as_percentage_of_on_demand_price is not None:
            self._values["bid_price_as_percentage_of_on_demand_price"] = bid_price_as_percentage_of_on_demand_price
        if configurations is not None:
            self._values["configurations"] = configurations
        if ebs_config is not None:
            self._values["ebs_config"] = ebs_config
        if weighted_capacity is not None:
            self._values["weighted_capacity"] = weighted_capacity

    @builtins.property
    def instance_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#instance_type EmrCluster#instance_type}.'''
        result = self._values.get("instance_type")
        assert result is not None, "Required property 'instance_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bid_price(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#bid_price EmrCluster#bid_price}.'''
        result = self._values.get("bid_price")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bid_price_as_percentage_of_on_demand_price(
        self,
    ) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#bid_price_as_percentage_of_on_demand_price EmrCluster#bid_price_as_percentage_of_on_demand_price}.'''
        result = self._values.get("bid_price_as_percentage_of_on_demand_price")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def configurations(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EmrClusterMasterInstanceFleetInstanceTypeConfigsConfigurations"]]]:
        '''configurations block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#configurations EmrCluster#configurations}
        '''
        result = self._values.get("configurations")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EmrClusterMasterInstanceFleetInstanceTypeConfigsConfigurations"]]], result)

    @builtins.property
    def ebs_config(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EmrClusterMasterInstanceFleetInstanceTypeConfigsEbsConfig"]]]:
        '''ebs_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#ebs_config EmrCluster#ebs_config}
        '''
        result = self._values.get("ebs_config")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EmrClusterMasterInstanceFleetInstanceTypeConfigsEbsConfig"]]], result)

    @builtins.property
    def weighted_capacity(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#weighted_capacity EmrCluster#weighted_capacity}.'''
        result = self._values.get("weighted_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmrClusterMasterInstanceFleetInstanceTypeConfigs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.emrCluster.EmrClusterMasterInstanceFleetInstanceTypeConfigsConfigurations",
    jsii_struct_bases=[],
    name_mapping={"classification": "classification", "properties": "properties"},
)
class EmrClusterMasterInstanceFleetInstanceTypeConfigsConfigurations:
    def __init__(
        self,
        *,
        classification: typing.Optional[builtins.str] = None,
        properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param classification: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#classification EmrCluster#classification}.
        :param properties: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#properties EmrCluster#properties}.
        '''
        if __debug__:
            def stub(
                *,
                classification: typing.Optional[builtins.str] = None,
                properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument classification", value=classification, expected_type=type_hints["classification"])
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
        self._values: typing.Dict[str, typing.Any] = {}
        if classification is not None:
            self._values["classification"] = classification
        if properties is not None:
            self._values["properties"] = properties

    @builtins.property
    def classification(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#classification EmrCluster#classification}.'''
        result = self._values.get("classification")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def properties(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#properties EmrCluster#properties}.'''
        result = self._values.get("properties")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmrClusterMasterInstanceFleetInstanceTypeConfigsConfigurations(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EmrClusterMasterInstanceFleetInstanceTypeConfigsConfigurationsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.emrCluster.EmrClusterMasterInstanceFleetInstanceTypeConfigsConfigurationsList",
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
    ) -> "EmrClusterMasterInstanceFleetInstanceTypeConfigsConfigurationsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EmrClusterMasterInstanceFleetInstanceTypeConfigsConfigurationsOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterMasterInstanceFleetInstanceTypeConfigsConfigurations]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterMasterInstanceFleetInstanceTypeConfigsConfigurations]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterMasterInstanceFleetInstanceTypeConfigsConfigurations]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterMasterInstanceFleetInstanceTypeConfigsConfigurations]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EmrClusterMasterInstanceFleetInstanceTypeConfigsConfigurationsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.emrCluster.EmrClusterMasterInstanceFleetInstanceTypeConfigsConfigurationsOutputReference",
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

    @jsii.member(jsii_name="resetClassification")
    def reset_classification(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClassification", []))

    @jsii.member(jsii_name="resetProperties")
    def reset_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProperties", []))

    @builtins.property
    @jsii.member(jsii_name="classificationInput")
    def classification_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "classificationInput"))

    @builtins.property
    @jsii.member(jsii_name="propertiesInput")
    def properties_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "propertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="classification")
    def classification(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "classification"))

    @classification.setter
    def classification(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "classification", value)

    @builtins.property
    @jsii.member(jsii_name="properties")
    def properties(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "properties"))

    @properties.setter
    def properties(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.Mapping[builtins.str, builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "properties", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EmrClusterMasterInstanceFleetInstanceTypeConfigsConfigurations, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EmrClusterMasterInstanceFleetInstanceTypeConfigsConfigurations, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EmrClusterMasterInstanceFleetInstanceTypeConfigsConfigurations, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[EmrClusterMasterInstanceFleetInstanceTypeConfigsConfigurations, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.emrCluster.EmrClusterMasterInstanceFleetInstanceTypeConfigsEbsConfig",
    jsii_struct_bases=[],
    name_mapping={
        "size": "size",
        "type": "type",
        "iops": "iops",
        "volumes_per_instance": "volumesPerInstance",
    },
)
class EmrClusterMasterInstanceFleetInstanceTypeConfigsEbsConfig:
    def __init__(
        self,
        *,
        size: jsii.Number,
        type: builtins.str,
        iops: typing.Optional[jsii.Number] = None,
        volumes_per_instance: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#size EmrCluster#size}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#type EmrCluster#type}.
        :param iops: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#iops EmrCluster#iops}.
        :param volumes_per_instance: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#volumes_per_instance EmrCluster#volumes_per_instance}.
        '''
        if __debug__:
            def stub(
                *,
                size: jsii.Number,
                type: builtins.str,
                iops: typing.Optional[jsii.Number] = None,
                volumes_per_instance: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument size", value=size, expected_type=type_hints["size"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument iops", value=iops, expected_type=type_hints["iops"])
            check_type(argname="argument volumes_per_instance", value=volumes_per_instance, expected_type=type_hints["volumes_per_instance"])
        self._values: typing.Dict[str, typing.Any] = {
            "size": size,
            "type": type,
        }
        if iops is not None:
            self._values["iops"] = iops
        if volumes_per_instance is not None:
            self._values["volumes_per_instance"] = volumes_per_instance

    @builtins.property
    def size(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#size EmrCluster#size}.'''
        result = self._values.get("size")
        assert result is not None, "Required property 'size' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#type EmrCluster#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def iops(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#iops EmrCluster#iops}.'''
        result = self._values.get("iops")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def volumes_per_instance(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#volumes_per_instance EmrCluster#volumes_per_instance}.'''
        result = self._values.get("volumes_per_instance")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmrClusterMasterInstanceFleetInstanceTypeConfigsEbsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EmrClusterMasterInstanceFleetInstanceTypeConfigsEbsConfigList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.emrCluster.EmrClusterMasterInstanceFleetInstanceTypeConfigsEbsConfigList",
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
    ) -> "EmrClusterMasterInstanceFleetInstanceTypeConfigsEbsConfigOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EmrClusterMasterInstanceFleetInstanceTypeConfigsEbsConfigOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterMasterInstanceFleetInstanceTypeConfigsEbsConfig]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterMasterInstanceFleetInstanceTypeConfigsEbsConfig]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterMasterInstanceFleetInstanceTypeConfigsEbsConfig]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterMasterInstanceFleetInstanceTypeConfigsEbsConfig]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EmrClusterMasterInstanceFleetInstanceTypeConfigsEbsConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.emrCluster.EmrClusterMasterInstanceFleetInstanceTypeConfigsEbsConfigOutputReference",
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

    @jsii.member(jsii_name="resetIops")
    def reset_iops(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIops", []))

    @jsii.member(jsii_name="resetVolumesPerInstance")
    def reset_volumes_per_instance(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVolumesPerInstance", []))

    @builtins.property
    @jsii.member(jsii_name="iopsInput")
    def iops_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "iopsInput"))

    @builtins.property
    @jsii.member(jsii_name="sizeInput")
    def size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sizeInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="volumesPerInstanceInput")
    def volumes_per_instance_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "volumesPerInstanceInput"))

    @builtins.property
    @jsii.member(jsii_name="iops")
    def iops(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "iops"))

    @iops.setter
    def iops(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iops", value)

    @builtins.property
    @jsii.member(jsii_name="size")
    def size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "size"))

    @size.setter
    def size(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "size", value)

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
    @jsii.member(jsii_name="volumesPerInstance")
    def volumes_per_instance(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "volumesPerInstance"))

    @volumes_per_instance.setter
    def volumes_per_instance(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumesPerInstance", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EmrClusterMasterInstanceFleetInstanceTypeConfigsEbsConfig, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EmrClusterMasterInstanceFleetInstanceTypeConfigsEbsConfig, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EmrClusterMasterInstanceFleetInstanceTypeConfigsEbsConfig, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[EmrClusterMasterInstanceFleetInstanceTypeConfigsEbsConfig, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EmrClusterMasterInstanceFleetInstanceTypeConfigsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.emrCluster.EmrClusterMasterInstanceFleetInstanceTypeConfigsList",
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
    ) -> "EmrClusterMasterInstanceFleetInstanceTypeConfigsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EmrClusterMasterInstanceFleetInstanceTypeConfigsOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterMasterInstanceFleetInstanceTypeConfigs]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterMasterInstanceFleetInstanceTypeConfigs]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterMasterInstanceFleetInstanceTypeConfigs]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterMasterInstanceFleetInstanceTypeConfigs]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EmrClusterMasterInstanceFleetInstanceTypeConfigsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.emrCluster.EmrClusterMasterInstanceFleetInstanceTypeConfigsOutputReference",
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

    @jsii.member(jsii_name="putConfigurations")
    def put_configurations(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EmrClusterMasterInstanceFleetInstanceTypeConfigsConfigurations, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EmrClusterMasterInstanceFleetInstanceTypeConfigsConfigurations, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putConfigurations", [value]))

    @jsii.member(jsii_name="putEbsConfig")
    def put_ebs_config(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EmrClusterMasterInstanceFleetInstanceTypeConfigsEbsConfig, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EmrClusterMasterInstanceFleetInstanceTypeConfigsEbsConfig, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEbsConfig", [value]))

    @jsii.member(jsii_name="resetBidPrice")
    def reset_bid_price(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBidPrice", []))

    @jsii.member(jsii_name="resetBidPriceAsPercentageOfOnDemandPrice")
    def reset_bid_price_as_percentage_of_on_demand_price(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBidPriceAsPercentageOfOnDemandPrice", []))

    @jsii.member(jsii_name="resetConfigurations")
    def reset_configurations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfigurations", []))

    @jsii.member(jsii_name="resetEbsConfig")
    def reset_ebs_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEbsConfig", []))

    @jsii.member(jsii_name="resetWeightedCapacity")
    def reset_weighted_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWeightedCapacity", []))

    @builtins.property
    @jsii.member(jsii_name="configurations")
    def configurations(
        self,
    ) -> EmrClusterMasterInstanceFleetInstanceTypeConfigsConfigurationsList:
        return typing.cast(EmrClusterMasterInstanceFleetInstanceTypeConfigsConfigurationsList, jsii.get(self, "configurations"))

    @builtins.property
    @jsii.member(jsii_name="ebsConfig")
    def ebs_config(
        self,
    ) -> EmrClusterMasterInstanceFleetInstanceTypeConfigsEbsConfigList:
        return typing.cast(EmrClusterMasterInstanceFleetInstanceTypeConfigsEbsConfigList, jsii.get(self, "ebsConfig"))

    @builtins.property
    @jsii.member(jsii_name="bidPriceAsPercentageOfOnDemandPriceInput")
    def bid_price_as_percentage_of_on_demand_price_input(
        self,
    ) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "bidPriceAsPercentageOfOnDemandPriceInput"))

    @builtins.property
    @jsii.member(jsii_name="bidPriceInput")
    def bid_price_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bidPriceInput"))

    @builtins.property
    @jsii.member(jsii_name="configurationsInput")
    def configurations_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterMasterInstanceFleetInstanceTypeConfigsConfigurations]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterMasterInstanceFleetInstanceTypeConfigsConfigurations]]], jsii.get(self, "configurationsInput"))

    @builtins.property
    @jsii.member(jsii_name="ebsConfigInput")
    def ebs_config_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterMasterInstanceFleetInstanceTypeConfigsEbsConfig]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterMasterInstanceFleetInstanceTypeConfigsEbsConfig]]], jsii.get(self, "ebsConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceTypeInput")
    def instance_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="weightedCapacityInput")
    def weighted_capacity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "weightedCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="bidPrice")
    def bid_price(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bidPrice"))

    @bid_price.setter
    def bid_price(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bidPrice", value)

    @builtins.property
    @jsii.member(jsii_name="bidPriceAsPercentageOfOnDemandPrice")
    def bid_price_as_percentage_of_on_demand_price(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "bidPriceAsPercentageOfOnDemandPrice"))

    @bid_price_as_percentage_of_on_demand_price.setter
    def bid_price_as_percentage_of_on_demand_price(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bidPriceAsPercentageOfOnDemandPrice", value)

    @builtins.property
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceType"))

    @instance_type.setter
    def instance_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceType", value)

    @builtins.property
    @jsii.member(jsii_name="weightedCapacity")
    def weighted_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "weightedCapacity"))

    @weighted_capacity.setter
    def weighted_capacity(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "weightedCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EmrClusterMasterInstanceFleetInstanceTypeConfigs, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EmrClusterMasterInstanceFleetInstanceTypeConfigs, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EmrClusterMasterInstanceFleetInstanceTypeConfigs, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[EmrClusterMasterInstanceFleetInstanceTypeConfigs, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.emrCluster.EmrClusterMasterInstanceFleetLaunchSpecifications",
    jsii_struct_bases=[],
    name_mapping={
        "on_demand_specification": "onDemandSpecification",
        "spot_specification": "spotSpecification",
    },
)
class EmrClusterMasterInstanceFleetLaunchSpecifications:
    def __init__(
        self,
        *,
        on_demand_specification: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EmrClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecification", typing.Dict[str, typing.Any]]]]] = None,
        spot_specification: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EmrClusterMasterInstanceFleetLaunchSpecificationsSpotSpecification", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param on_demand_specification: on_demand_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#on_demand_specification EmrCluster#on_demand_specification}
        :param spot_specification: spot_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#spot_specification EmrCluster#spot_specification}
        '''
        if __debug__:
            def stub(
                *,
                on_demand_specification: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EmrClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecification, typing.Dict[str, typing.Any]]]]] = None,
                spot_specification: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EmrClusterMasterInstanceFleetLaunchSpecificationsSpotSpecification, typing.Dict[str, typing.Any]]]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument on_demand_specification", value=on_demand_specification, expected_type=type_hints["on_demand_specification"])
            check_type(argname="argument spot_specification", value=spot_specification, expected_type=type_hints["spot_specification"])
        self._values: typing.Dict[str, typing.Any] = {}
        if on_demand_specification is not None:
            self._values["on_demand_specification"] = on_demand_specification
        if spot_specification is not None:
            self._values["spot_specification"] = spot_specification

    @builtins.property
    def on_demand_specification(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EmrClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecification"]]]:
        '''on_demand_specification block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#on_demand_specification EmrCluster#on_demand_specification}
        '''
        result = self._values.get("on_demand_specification")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EmrClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecification"]]], result)

    @builtins.property
    def spot_specification(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EmrClusterMasterInstanceFleetLaunchSpecificationsSpotSpecification"]]]:
        '''spot_specification block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#spot_specification EmrCluster#spot_specification}
        '''
        result = self._values.get("spot_specification")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EmrClusterMasterInstanceFleetLaunchSpecificationsSpotSpecification"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmrClusterMasterInstanceFleetLaunchSpecifications(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.emrCluster.EmrClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecification",
    jsii_struct_bases=[],
    name_mapping={"allocation_strategy": "allocationStrategy"},
)
class EmrClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecification:
    def __init__(self, *, allocation_strategy: builtins.str) -> None:
        '''
        :param allocation_strategy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#allocation_strategy EmrCluster#allocation_strategy}.
        '''
        if __debug__:
            def stub(*, allocation_strategy: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument allocation_strategy", value=allocation_strategy, expected_type=type_hints["allocation_strategy"])
        self._values: typing.Dict[str, typing.Any] = {
            "allocation_strategy": allocation_strategy,
        }

    @builtins.property
    def allocation_strategy(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#allocation_strategy EmrCluster#allocation_strategy}.'''
        result = self._values.get("allocation_strategy")
        assert result is not None, "Required property 'allocation_strategy' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmrClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecification(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EmrClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecificationList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.emrCluster.EmrClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecificationList",
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
    ) -> "EmrClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecificationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EmrClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecificationOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecification]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecification]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecification]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecification]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EmrClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecificationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.emrCluster.EmrClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecificationOutputReference",
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
    @jsii.member(jsii_name="allocationStrategyInput")
    def allocation_strategy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "allocationStrategyInput"))

    @builtins.property
    @jsii.member(jsii_name="allocationStrategy")
    def allocation_strategy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "allocationStrategy"))

    @allocation_strategy.setter
    def allocation_strategy(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allocationStrategy", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EmrClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecification, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EmrClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecification, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EmrClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecification, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[EmrClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecification, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EmrClusterMasterInstanceFleetLaunchSpecificationsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.emrCluster.EmrClusterMasterInstanceFleetLaunchSpecificationsOutputReference",
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

    @jsii.member(jsii_name="putOnDemandSpecification")
    def put_on_demand_specification(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EmrClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecification, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EmrClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecification, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putOnDemandSpecification", [value]))

    @jsii.member(jsii_name="putSpotSpecification")
    def put_spot_specification(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EmrClusterMasterInstanceFleetLaunchSpecificationsSpotSpecification", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EmrClusterMasterInstanceFleetLaunchSpecificationsSpotSpecification, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSpotSpecification", [value]))

    @jsii.member(jsii_name="resetOnDemandSpecification")
    def reset_on_demand_specification(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOnDemandSpecification", []))

    @jsii.member(jsii_name="resetSpotSpecification")
    def reset_spot_specification(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSpotSpecification", []))

    @builtins.property
    @jsii.member(jsii_name="onDemandSpecification")
    def on_demand_specification(
        self,
    ) -> EmrClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecificationList:
        return typing.cast(EmrClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecificationList, jsii.get(self, "onDemandSpecification"))

    @builtins.property
    @jsii.member(jsii_name="spotSpecification")
    def spot_specification(
        self,
    ) -> "EmrClusterMasterInstanceFleetLaunchSpecificationsSpotSpecificationList":
        return typing.cast("EmrClusterMasterInstanceFleetLaunchSpecificationsSpotSpecificationList", jsii.get(self, "spotSpecification"))

    @builtins.property
    @jsii.member(jsii_name="onDemandSpecificationInput")
    def on_demand_specification_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecification]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecification]]], jsii.get(self, "onDemandSpecificationInput"))

    @builtins.property
    @jsii.member(jsii_name="spotSpecificationInput")
    def spot_specification_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EmrClusterMasterInstanceFleetLaunchSpecificationsSpotSpecification"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EmrClusterMasterInstanceFleetLaunchSpecificationsSpotSpecification"]]], jsii.get(self, "spotSpecificationInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[EmrClusterMasterInstanceFleetLaunchSpecifications]:
        return typing.cast(typing.Optional[EmrClusterMasterInstanceFleetLaunchSpecifications], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EmrClusterMasterInstanceFleetLaunchSpecifications],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[EmrClusterMasterInstanceFleetLaunchSpecifications],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.emrCluster.EmrClusterMasterInstanceFleetLaunchSpecificationsSpotSpecification",
    jsii_struct_bases=[],
    name_mapping={
        "allocation_strategy": "allocationStrategy",
        "timeout_action": "timeoutAction",
        "timeout_duration_minutes": "timeoutDurationMinutes",
        "block_duration_minutes": "blockDurationMinutes",
    },
)
class EmrClusterMasterInstanceFleetLaunchSpecificationsSpotSpecification:
    def __init__(
        self,
        *,
        allocation_strategy: builtins.str,
        timeout_action: builtins.str,
        timeout_duration_minutes: jsii.Number,
        block_duration_minutes: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param allocation_strategy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#allocation_strategy EmrCluster#allocation_strategy}.
        :param timeout_action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#timeout_action EmrCluster#timeout_action}.
        :param timeout_duration_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#timeout_duration_minutes EmrCluster#timeout_duration_minutes}.
        :param block_duration_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#block_duration_minutes EmrCluster#block_duration_minutes}.
        '''
        if __debug__:
            def stub(
                *,
                allocation_strategy: builtins.str,
                timeout_action: builtins.str,
                timeout_duration_minutes: jsii.Number,
                block_duration_minutes: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument allocation_strategy", value=allocation_strategy, expected_type=type_hints["allocation_strategy"])
            check_type(argname="argument timeout_action", value=timeout_action, expected_type=type_hints["timeout_action"])
            check_type(argname="argument timeout_duration_minutes", value=timeout_duration_minutes, expected_type=type_hints["timeout_duration_minutes"])
            check_type(argname="argument block_duration_minutes", value=block_duration_minutes, expected_type=type_hints["block_duration_minutes"])
        self._values: typing.Dict[str, typing.Any] = {
            "allocation_strategy": allocation_strategy,
            "timeout_action": timeout_action,
            "timeout_duration_minutes": timeout_duration_minutes,
        }
        if block_duration_minutes is not None:
            self._values["block_duration_minutes"] = block_duration_minutes

    @builtins.property
    def allocation_strategy(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#allocation_strategy EmrCluster#allocation_strategy}.'''
        result = self._values.get("allocation_strategy")
        assert result is not None, "Required property 'allocation_strategy' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def timeout_action(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#timeout_action EmrCluster#timeout_action}.'''
        result = self._values.get("timeout_action")
        assert result is not None, "Required property 'timeout_action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def timeout_duration_minutes(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#timeout_duration_minutes EmrCluster#timeout_duration_minutes}.'''
        result = self._values.get("timeout_duration_minutes")
        assert result is not None, "Required property 'timeout_duration_minutes' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def block_duration_minutes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#block_duration_minutes EmrCluster#block_duration_minutes}.'''
        result = self._values.get("block_duration_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmrClusterMasterInstanceFleetLaunchSpecificationsSpotSpecification(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EmrClusterMasterInstanceFleetLaunchSpecificationsSpotSpecificationList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.emrCluster.EmrClusterMasterInstanceFleetLaunchSpecificationsSpotSpecificationList",
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
    ) -> "EmrClusterMasterInstanceFleetLaunchSpecificationsSpotSpecificationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EmrClusterMasterInstanceFleetLaunchSpecificationsSpotSpecificationOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterMasterInstanceFleetLaunchSpecificationsSpotSpecification]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterMasterInstanceFleetLaunchSpecificationsSpotSpecification]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterMasterInstanceFleetLaunchSpecificationsSpotSpecification]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterMasterInstanceFleetLaunchSpecificationsSpotSpecification]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EmrClusterMasterInstanceFleetLaunchSpecificationsSpotSpecificationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.emrCluster.EmrClusterMasterInstanceFleetLaunchSpecificationsSpotSpecificationOutputReference",
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

    @jsii.member(jsii_name="resetBlockDurationMinutes")
    def reset_block_duration_minutes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBlockDurationMinutes", []))

    @builtins.property
    @jsii.member(jsii_name="allocationStrategyInput")
    def allocation_strategy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "allocationStrategyInput"))

    @builtins.property
    @jsii.member(jsii_name="blockDurationMinutesInput")
    def block_duration_minutes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "blockDurationMinutesInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutActionInput")
    def timeout_action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeoutActionInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutDurationMinutesInput")
    def timeout_duration_minutes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timeoutDurationMinutesInput"))

    @builtins.property
    @jsii.member(jsii_name="allocationStrategy")
    def allocation_strategy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "allocationStrategy"))

    @allocation_strategy.setter
    def allocation_strategy(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allocationStrategy", value)

    @builtins.property
    @jsii.member(jsii_name="blockDurationMinutes")
    def block_duration_minutes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "blockDurationMinutes"))

    @block_duration_minutes.setter
    def block_duration_minutes(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "blockDurationMinutes", value)

    @builtins.property
    @jsii.member(jsii_name="timeoutAction")
    def timeout_action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timeoutAction"))

    @timeout_action.setter
    def timeout_action(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeoutAction", value)

    @builtins.property
    @jsii.member(jsii_name="timeoutDurationMinutes")
    def timeout_duration_minutes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "timeoutDurationMinutes"))

    @timeout_duration_minutes.setter
    def timeout_duration_minutes(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeoutDurationMinutes", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EmrClusterMasterInstanceFleetLaunchSpecificationsSpotSpecification, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EmrClusterMasterInstanceFleetLaunchSpecificationsSpotSpecification, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EmrClusterMasterInstanceFleetLaunchSpecificationsSpotSpecification, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[EmrClusterMasterInstanceFleetLaunchSpecificationsSpotSpecification, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EmrClusterMasterInstanceFleetOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.emrCluster.EmrClusterMasterInstanceFleetOutputReference",
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

    @jsii.member(jsii_name="putInstanceTypeConfigs")
    def put_instance_type_configs(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EmrClusterMasterInstanceFleetInstanceTypeConfigs, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EmrClusterMasterInstanceFleetInstanceTypeConfigs, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putInstanceTypeConfigs", [value]))

    @jsii.member(jsii_name="putLaunchSpecifications")
    def put_launch_specifications(
        self,
        *,
        on_demand_specification: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EmrClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecification, typing.Dict[str, typing.Any]]]]] = None,
        spot_specification: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EmrClusterMasterInstanceFleetLaunchSpecificationsSpotSpecification, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param on_demand_specification: on_demand_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#on_demand_specification EmrCluster#on_demand_specification}
        :param spot_specification: spot_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#spot_specification EmrCluster#spot_specification}
        '''
        value = EmrClusterMasterInstanceFleetLaunchSpecifications(
            on_demand_specification=on_demand_specification,
            spot_specification=spot_specification,
        )

        return typing.cast(None, jsii.invoke(self, "putLaunchSpecifications", [value]))

    @jsii.member(jsii_name="resetInstanceTypeConfigs")
    def reset_instance_type_configs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceTypeConfigs", []))

    @jsii.member(jsii_name="resetLaunchSpecifications")
    def reset_launch_specifications(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLaunchSpecifications", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetTargetOnDemandCapacity")
    def reset_target_on_demand_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetOnDemandCapacity", []))

    @jsii.member(jsii_name="resetTargetSpotCapacity")
    def reset_target_spot_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetSpotCapacity", []))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="instanceTypeConfigs")
    def instance_type_configs(
        self,
    ) -> EmrClusterMasterInstanceFleetInstanceTypeConfigsList:
        return typing.cast(EmrClusterMasterInstanceFleetInstanceTypeConfigsList, jsii.get(self, "instanceTypeConfigs"))

    @builtins.property
    @jsii.member(jsii_name="launchSpecifications")
    def launch_specifications(
        self,
    ) -> EmrClusterMasterInstanceFleetLaunchSpecificationsOutputReference:
        return typing.cast(EmrClusterMasterInstanceFleetLaunchSpecificationsOutputReference, jsii.get(self, "launchSpecifications"))

    @builtins.property
    @jsii.member(jsii_name="provisionedOnDemandCapacity")
    def provisioned_on_demand_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "provisionedOnDemandCapacity"))

    @builtins.property
    @jsii.member(jsii_name="provisionedSpotCapacity")
    def provisioned_spot_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "provisionedSpotCapacity"))

    @builtins.property
    @jsii.member(jsii_name="instanceTypeConfigsInput")
    def instance_type_configs_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterMasterInstanceFleetInstanceTypeConfigs]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterMasterInstanceFleetInstanceTypeConfigs]]], jsii.get(self, "instanceTypeConfigsInput"))

    @builtins.property
    @jsii.member(jsii_name="launchSpecificationsInput")
    def launch_specifications_input(
        self,
    ) -> typing.Optional[EmrClusterMasterInstanceFleetLaunchSpecifications]:
        return typing.cast(typing.Optional[EmrClusterMasterInstanceFleetLaunchSpecifications], jsii.get(self, "launchSpecificationsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="targetOnDemandCapacityInput")
    def target_on_demand_capacity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "targetOnDemandCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="targetSpotCapacityInput")
    def target_spot_capacity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "targetSpotCapacityInput"))

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
    @jsii.member(jsii_name="targetOnDemandCapacity")
    def target_on_demand_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "targetOnDemandCapacity"))

    @target_on_demand_capacity.setter
    def target_on_demand_capacity(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetOnDemandCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="targetSpotCapacity")
    def target_spot_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "targetSpotCapacity"))

    @target_spot_capacity.setter
    def target_spot_capacity(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetSpotCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[EmrClusterMasterInstanceFleet]:
        return typing.cast(typing.Optional[EmrClusterMasterInstanceFleet], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EmrClusterMasterInstanceFleet],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[EmrClusterMasterInstanceFleet]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.emrCluster.EmrClusterMasterInstanceGroup",
    jsii_struct_bases=[],
    name_mapping={
        "instance_type": "instanceType",
        "bid_price": "bidPrice",
        "ebs_config": "ebsConfig",
        "instance_count": "instanceCount",
        "name": "name",
    },
)
class EmrClusterMasterInstanceGroup:
    def __init__(
        self,
        *,
        instance_type: builtins.str,
        bid_price: typing.Optional[builtins.str] = None,
        ebs_config: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EmrClusterMasterInstanceGroupEbsConfig", typing.Dict[str, typing.Any]]]]] = None,
        instance_count: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param instance_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#instance_type EmrCluster#instance_type}.
        :param bid_price: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#bid_price EmrCluster#bid_price}.
        :param ebs_config: ebs_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#ebs_config EmrCluster#ebs_config}
        :param instance_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#instance_count EmrCluster#instance_count}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#name EmrCluster#name}.
        '''
        if __debug__:
            def stub(
                *,
                instance_type: builtins.str,
                bid_price: typing.Optional[builtins.str] = None,
                ebs_config: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EmrClusterMasterInstanceGroupEbsConfig, typing.Dict[str, typing.Any]]]]] = None,
                instance_count: typing.Optional[jsii.Number] = None,
                name: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            check_type(argname="argument bid_price", value=bid_price, expected_type=type_hints["bid_price"])
            check_type(argname="argument ebs_config", value=ebs_config, expected_type=type_hints["ebs_config"])
            check_type(argname="argument instance_count", value=instance_count, expected_type=type_hints["instance_count"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "instance_type": instance_type,
        }
        if bid_price is not None:
            self._values["bid_price"] = bid_price
        if ebs_config is not None:
            self._values["ebs_config"] = ebs_config
        if instance_count is not None:
            self._values["instance_count"] = instance_count
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def instance_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#instance_type EmrCluster#instance_type}.'''
        result = self._values.get("instance_type")
        assert result is not None, "Required property 'instance_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bid_price(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#bid_price EmrCluster#bid_price}.'''
        result = self._values.get("bid_price")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ebs_config(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EmrClusterMasterInstanceGroupEbsConfig"]]]:
        '''ebs_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#ebs_config EmrCluster#ebs_config}
        '''
        result = self._values.get("ebs_config")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EmrClusterMasterInstanceGroupEbsConfig"]]], result)

    @builtins.property
    def instance_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#instance_count EmrCluster#instance_count}.'''
        result = self._values.get("instance_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#name EmrCluster#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmrClusterMasterInstanceGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.emrCluster.EmrClusterMasterInstanceGroupEbsConfig",
    jsii_struct_bases=[],
    name_mapping={
        "size": "size",
        "type": "type",
        "iops": "iops",
        "throughput": "throughput",
        "volumes_per_instance": "volumesPerInstance",
    },
)
class EmrClusterMasterInstanceGroupEbsConfig:
    def __init__(
        self,
        *,
        size: jsii.Number,
        type: builtins.str,
        iops: typing.Optional[jsii.Number] = None,
        throughput: typing.Optional[jsii.Number] = None,
        volumes_per_instance: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#size EmrCluster#size}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#type EmrCluster#type}.
        :param iops: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#iops EmrCluster#iops}.
        :param throughput: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#throughput EmrCluster#throughput}.
        :param volumes_per_instance: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#volumes_per_instance EmrCluster#volumes_per_instance}.
        '''
        if __debug__:
            def stub(
                *,
                size: jsii.Number,
                type: builtins.str,
                iops: typing.Optional[jsii.Number] = None,
                throughput: typing.Optional[jsii.Number] = None,
                volumes_per_instance: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument size", value=size, expected_type=type_hints["size"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument iops", value=iops, expected_type=type_hints["iops"])
            check_type(argname="argument throughput", value=throughput, expected_type=type_hints["throughput"])
            check_type(argname="argument volumes_per_instance", value=volumes_per_instance, expected_type=type_hints["volumes_per_instance"])
        self._values: typing.Dict[str, typing.Any] = {
            "size": size,
            "type": type,
        }
        if iops is not None:
            self._values["iops"] = iops
        if throughput is not None:
            self._values["throughput"] = throughput
        if volumes_per_instance is not None:
            self._values["volumes_per_instance"] = volumes_per_instance

    @builtins.property
    def size(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#size EmrCluster#size}.'''
        result = self._values.get("size")
        assert result is not None, "Required property 'size' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#type EmrCluster#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def iops(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#iops EmrCluster#iops}.'''
        result = self._values.get("iops")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def throughput(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#throughput EmrCluster#throughput}.'''
        result = self._values.get("throughput")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def volumes_per_instance(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#volumes_per_instance EmrCluster#volumes_per_instance}.'''
        result = self._values.get("volumes_per_instance")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmrClusterMasterInstanceGroupEbsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EmrClusterMasterInstanceGroupEbsConfigList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.emrCluster.EmrClusterMasterInstanceGroupEbsConfigList",
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
    ) -> "EmrClusterMasterInstanceGroupEbsConfigOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EmrClusterMasterInstanceGroupEbsConfigOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterMasterInstanceGroupEbsConfig]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterMasterInstanceGroupEbsConfig]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterMasterInstanceGroupEbsConfig]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterMasterInstanceGroupEbsConfig]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EmrClusterMasterInstanceGroupEbsConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.emrCluster.EmrClusterMasterInstanceGroupEbsConfigOutputReference",
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

    @jsii.member(jsii_name="resetIops")
    def reset_iops(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIops", []))

    @jsii.member(jsii_name="resetThroughput")
    def reset_throughput(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThroughput", []))

    @jsii.member(jsii_name="resetVolumesPerInstance")
    def reset_volumes_per_instance(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVolumesPerInstance", []))

    @builtins.property
    @jsii.member(jsii_name="iopsInput")
    def iops_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "iopsInput"))

    @builtins.property
    @jsii.member(jsii_name="sizeInput")
    def size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sizeInput"))

    @builtins.property
    @jsii.member(jsii_name="throughputInput")
    def throughput_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "throughputInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="volumesPerInstanceInput")
    def volumes_per_instance_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "volumesPerInstanceInput"))

    @builtins.property
    @jsii.member(jsii_name="iops")
    def iops(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "iops"))

    @iops.setter
    def iops(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iops", value)

    @builtins.property
    @jsii.member(jsii_name="size")
    def size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "size"))

    @size.setter
    def size(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "size", value)

    @builtins.property
    @jsii.member(jsii_name="throughput")
    def throughput(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "throughput"))

    @throughput.setter
    def throughput(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "throughput", value)

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
    @jsii.member(jsii_name="volumesPerInstance")
    def volumes_per_instance(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "volumesPerInstance"))

    @volumes_per_instance.setter
    def volumes_per_instance(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumesPerInstance", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EmrClusterMasterInstanceGroupEbsConfig, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EmrClusterMasterInstanceGroupEbsConfig, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EmrClusterMasterInstanceGroupEbsConfig, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[EmrClusterMasterInstanceGroupEbsConfig, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EmrClusterMasterInstanceGroupOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.emrCluster.EmrClusterMasterInstanceGroupOutputReference",
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

    @jsii.member(jsii_name="putEbsConfig")
    def put_ebs_config(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EmrClusterMasterInstanceGroupEbsConfig, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EmrClusterMasterInstanceGroupEbsConfig, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEbsConfig", [value]))

    @jsii.member(jsii_name="resetBidPrice")
    def reset_bid_price(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBidPrice", []))

    @jsii.member(jsii_name="resetEbsConfig")
    def reset_ebs_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEbsConfig", []))

    @jsii.member(jsii_name="resetInstanceCount")
    def reset_instance_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceCount", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="ebsConfig")
    def ebs_config(self) -> EmrClusterMasterInstanceGroupEbsConfigList:
        return typing.cast(EmrClusterMasterInstanceGroupEbsConfigList, jsii.get(self, "ebsConfig"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="bidPriceInput")
    def bid_price_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bidPriceInput"))

    @builtins.property
    @jsii.member(jsii_name="ebsConfigInput")
    def ebs_config_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterMasterInstanceGroupEbsConfig]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterMasterInstanceGroupEbsConfig]]], jsii.get(self, "ebsConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceCountInput")
    def instance_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "instanceCountInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceTypeInput")
    def instance_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="bidPrice")
    def bid_price(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bidPrice"))

    @bid_price.setter
    def bid_price(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bidPrice", value)

    @builtins.property
    @jsii.member(jsii_name="instanceCount")
    def instance_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "instanceCount"))

    @instance_count.setter
    def instance_count(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceCount", value)

    @builtins.property
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceType"))

    @instance_type.setter
    def instance_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceType", value)

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
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[EmrClusterMasterInstanceGroup]:
        return typing.cast(typing.Optional[EmrClusterMasterInstanceGroup], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EmrClusterMasterInstanceGroup],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[EmrClusterMasterInstanceGroup]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.emrCluster.EmrClusterStep",
    jsii_struct_bases=[],
    name_mapping={
        "action_on_failure": "actionOnFailure",
        "hadoop_jar_step": "hadoopJarStep",
        "name": "name",
    },
)
class EmrClusterStep:
    def __init__(
        self,
        *,
        action_on_failure: typing.Optional[builtins.str] = None,
        hadoop_jar_step: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EmrClusterStepHadoopJarStep", typing.Dict[str, typing.Any]]]]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param action_on_failure: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#action_on_failure EmrCluster#action_on_failure}.
        :param hadoop_jar_step: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#hadoop_jar_step EmrCluster#hadoop_jar_step}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#name EmrCluster#name}.
        '''
        if __debug__:
            def stub(
                *,
                action_on_failure: typing.Optional[builtins.str] = None,
                hadoop_jar_step: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EmrClusterStepHadoopJarStep, typing.Dict[str, typing.Any]]]]] = None,
                name: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument action_on_failure", value=action_on_failure, expected_type=type_hints["action_on_failure"])
            check_type(argname="argument hadoop_jar_step", value=hadoop_jar_step, expected_type=type_hints["hadoop_jar_step"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {}
        if action_on_failure is not None:
            self._values["action_on_failure"] = action_on_failure
        if hadoop_jar_step is not None:
            self._values["hadoop_jar_step"] = hadoop_jar_step
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def action_on_failure(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#action_on_failure EmrCluster#action_on_failure}.'''
        result = self._values.get("action_on_failure")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def hadoop_jar_step(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EmrClusterStepHadoopJarStep"]]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#hadoop_jar_step EmrCluster#hadoop_jar_step}.'''
        result = self._values.get("hadoop_jar_step")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EmrClusterStepHadoopJarStep"]]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#name EmrCluster#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmrClusterStep(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.emrCluster.EmrClusterStepHadoopJarStep",
    jsii_struct_bases=[],
    name_mapping={
        "args": "args",
        "jar": "jar",
        "main_class": "mainClass",
        "properties": "properties",
    },
)
class EmrClusterStepHadoopJarStep:
    def __init__(
        self,
        *,
        args: typing.Optional[typing.Sequence[builtins.str]] = None,
        jar: typing.Optional[builtins.str] = None,
        main_class: typing.Optional[builtins.str] = None,
        properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param args: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#args EmrCluster#args}.
        :param jar: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#jar EmrCluster#jar}.
        :param main_class: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#main_class EmrCluster#main_class}.
        :param properties: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#properties EmrCluster#properties}.
        '''
        if __debug__:
            def stub(
                *,
                args: typing.Optional[typing.Sequence[builtins.str]] = None,
                jar: typing.Optional[builtins.str] = None,
                main_class: typing.Optional[builtins.str] = None,
                properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument args", value=args, expected_type=type_hints["args"])
            check_type(argname="argument jar", value=jar, expected_type=type_hints["jar"])
            check_type(argname="argument main_class", value=main_class, expected_type=type_hints["main_class"])
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
        self._values: typing.Dict[str, typing.Any] = {}
        if args is not None:
            self._values["args"] = args
        if jar is not None:
            self._values["jar"] = jar
        if main_class is not None:
            self._values["main_class"] = main_class
        if properties is not None:
            self._values["properties"] = properties

    @builtins.property
    def args(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#args EmrCluster#args}.'''
        result = self._values.get("args")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def jar(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#jar EmrCluster#jar}.'''
        result = self._values.get("jar")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def main_class(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#main_class EmrCluster#main_class}.'''
        result = self._values.get("main_class")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def properties(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/emr_cluster#properties EmrCluster#properties}.'''
        result = self._values.get("properties")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmrClusterStepHadoopJarStep(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EmrClusterStepHadoopJarStepList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.emrCluster.EmrClusterStepHadoopJarStepList",
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
    def get(self, index: jsii.Number) -> "EmrClusterStepHadoopJarStepOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EmrClusterStepHadoopJarStepOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterStepHadoopJarStep]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterStepHadoopJarStep]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterStepHadoopJarStep]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterStepHadoopJarStep]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EmrClusterStepHadoopJarStepOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.emrCluster.EmrClusterStepHadoopJarStepOutputReference",
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

    @jsii.member(jsii_name="resetArgs")
    def reset_args(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArgs", []))

    @jsii.member(jsii_name="resetJar")
    def reset_jar(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJar", []))

    @jsii.member(jsii_name="resetMainClass")
    def reset_main_class(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMainClass", []))

    @jsii.member(jsii_name="resetProperties")
    def reset_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProperties", []))

    @builtins.property
    @jsii.member(jsii_name="argsInput")
    def args_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "argsInput"))

    @builtins.property
    @jsii.member(jsii_name="jarInput")
    def jar_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "jarInput"))

    @builtins.property
    @jsii.member(jsii_name="mainClassInput")
    def main_class_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mainClassInput"))

    @builtins.property
    @jsii.member(jsii_name="propertiesInput")
    def properties_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "propertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="args")
    def args(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "args"))

    @args.setter
    def args(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "args", value)

    @builtins.property
    @jsii.member(jsii_name="jar")
    def jar(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "jar"))

    @jar.setter
    def jar(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jar", value)

    @builtins.property
    @jsii.member(jsii_name="mainClass")
    def main_class(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mainClass"))

    @main_class.setter
    def main_class(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mainClass", value)

    @builtins.property
    @jsii.member(jsii_name="properties")
    def properties(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "properties"))

    @properties.setter
    def properties(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.Mapping[builtins.str, builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "properties", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EmrClusterStepHadoopJarStep, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EmrClusterStepHadoopJarStep, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EmrClusterStepHadoopJarStep, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[EmrClusterStepHadoopJarStep, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EmrClusterStepList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.emrCluster.EmrClusterStepList",
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
    def get(self, index: jsii.Number) -> "EmrClusterStepOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EmrClusterStepOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterStep]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterStep]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterStep]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterStep]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EmrClusterStepOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.emrCluster.EmrClusterStepOutputReference",
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

    @jsii.member(jsii_name="putHadoopJarStep")
    def put_hadoop_jar_step(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EmrClusterStepHadoopJarStep, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EmrClusterStepHadoopJarStep, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putHadoopJarStep", [value]))

    @jsii.member(jsii_name="resetActionOnFailure")
    def reset_action_on_failure(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetActionOnFailure", []))

    @jsii.member(jsii_name="resetHadoopJarStep")
    def reset_hadoop_jar_step(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHadoopJarStep", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="hadoopJarStep")
    def hadoop_jar_step(self) -> EmrClusterStepHadoopJarStepList:
        return typing.cast(EmrClusterStepHadoopJarStepList, jsii.get(self, "hadoopJarStep"))

    @builtins.property
    @jsii.member(jsii_name="actionOnFailureInput")
    def action_on_failure_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionOnFailureInput"))

    @builtins.property
    @jsii.member(jsii_name="hadoopJarStepInput")
    def hadoop_jar_step_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterStepHadoopJarStep]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EmrClusterStepHadoopJarStep]]], jsii.get(self, "hadoopJarStepInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="actionOnFailure")
    def action_on_failure(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "actionOnFailure"))

    @action_on_failure.setter
    def action_on_failure(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "actionOnFailure", value)

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
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EmrClusterStep, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EmrClusterStep, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EmrClusterStep, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[EmrClusterStep, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "EmrCluster",
    "EmrClusterAutoTerminationPolicy",
    "EmrClusterAutoTerminationPolicyOutputReference",
    "EmrClusterBootstrapAction",
    "EmrClusterBootstrapActionList",
    "EmrClusterBootstrapActionOutputReference",
    "EmrClusterConfig",
    "EmrClusterCoreInstanceFleet",
    "EmrClusterCoreInstanceFleetInstanceTypeConfigs",
    "EmrClusterCoreInstanceFleetInstanceTypeConfigsConfigurations",
    "EmrClusterCoreInstanceFleetInstanceTypeConfigsConfigurationsList",
    "EmrClusterCoreInstanceFleetInstanceTypeConfigsConfigurationsOutputReference",
    "EmrClusterCoreInstanceFleetInstanceTypeConfigsEbsConfig",
    "EmrClusterCoreInstanceFleetInstanceTypeConfigsEbsConfigList",
    "EmrClusterCoreInstanceFleetInstanceTypeConfigsEbsConfigOutputReference",
    "EmrClusterCoreInstanceFleetInstanceTypeConfigsList",
    "EmrClusterCoreInstanceFleetInstanceTypeConfigsOutputReference",
    "EmrClusterCoreInstanceFleetLaunchSpecifications",
    "EmrClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecification",
    "EmrClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecificationList",
    "EmrClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecificationOutputReference",
    "EmrClusterCoreInstanceFleetLaunchSpecificationsOutputReference",
    "EmrClusterCoreInstanceFleetLaunchSpecificationsSpotSpecification",
    "EmrClusterCoreInstanceFleetLaunchSpecificationsSpotSpecificationList",
    "EmrClusterCoreInstanceFleetLaunchSpecificationsSpotSpecificationOutputReference",
    "EmrClusterCoreInstanceFleetOutputReference",
    "EmrClusterCoreInstanceGroup",
    "EmrClusterCoreInstanceGroupEbsConfig",
    "EmrClusterCoreInstanceGroupEbsConfigList",
    "EmrClusterCoreInstanceGroupEbsConfigOutputReference",
    "EmrClusterCoreInstanceGroupOutputReference",
    "EmrClusterEc2Attributes",
    "EmrClusterEc2AttributesOutputReference",
    "EmrClusterKerberosAttributes",
    "EmrClusterKerberosAttributesOutputReference",
    "EmrClusterMasterInstanceFleet",
    "EmrClusterMasterInstanceFleetInstanceTypeConfigs",
    "EmrClusterMasterInstanceFleetInstanceTypeConfigsConfigurations",
    "EmrClusterMasterInstanceFleetInstanceTypeConfigsConfigurationsList",
    "EmrClusterMasterInstanceFleetInstanceTypeConfigsConfigurationsOutputReference",
    "EmrClusterMasterInstanceFleetInstanceTypeConfigsEbsConfig",
    "EmrClusterMasterInstanceFleetInstanceTypeConfigsEbsConfigList",
    "EmrClusterMasterInstanceFleetInstanceTypeConfigsEbsConfigOutputReference",
    "EmrClusterMasterInstanceFleetInstanceTypeConfigsList",
    "EmrClusterMasterInstanceFleetInstanceTypeConfigsOutputReference",
    "EmrClusterMasterInstanceFleetLaunchSpecifications",
    "EmrClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecification",
    "EmrClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecificationList",
    "EmrClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecificationOutputReference",
    "EmrClusterMasterInstanceFleetLaunchSpecificationsOutputReference",
    "EmrClusterMasterInstanceFleetLaunchSpecificationsSpotSpecification",
    "EmrClusterMasterInstanceFleetLaunchSpecificationsSpotSpecificationList",
    "EmrClusterMasterInstanceFleetLaunchSpecificationsSpotSpecificationOutputReference",
    "EmrClusterMasterInstanceFleetOutputReference",
    "EmrClusterMasterInstanceGroup",
    "EmrClusterMasterInstanceGroupEbsConfig",
    "EmrClusterMasterInstanceGroupEbsConfigList",
    "EmrClusterMasterInstanceGroupEbsConfigOutputReference",
    "EmrClusterMasterInstanceGroupOutputReference",
    "EmrClusterStep",
    "EmrClusterStepHadoopJarStep",
    "EmrClusterStepHadoopJarStepList",
    "EmrClusterStepHadoopJarStepOutputReference",
    "EmrClusterStepList",
    "EmrClusterStepOutputReference",
]

publication.publish()
