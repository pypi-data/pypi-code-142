import datetime
import oci.core
from dateutil.relativedelta import relativedelta

# contains the description messages for recommendations
r_msgs = {
    'del_instance': "CPU Utilization of instance is less than 3% from last 7 days",
    'purge boot vol': "The Boot Volume is unattached, can be purged",
    'purge vol': "The volume is unattached, can be purged",
    'enable monitoring': "Monitoring is not enabled in Instance, should be enabled ",
    'enable olm': 'The Enable object lifecycle management recommendation indicates that no lifecycle policy rules exist for a Object Storage bucket in your tenancy. Object versioning increases your storage costs because the resource includes multiple versions of the same object. Consider using Object Lifecycle Management to help manage object versions automatically.',
    'enable tuning': 'The Enable performance auto-tuning for boot volumes recommendation indicates that a boot volume is using suboptimal performance settings. Implementing this recommendation improves performance of the volume. The auto-tune feature automatically shifts performance between lower cost, balanced, and higher performance as necessary to optimize utilization of each volume. With the auto-tune feature enabled, you do not need to continually manage volume resources.',
    'improve_fault': 'The Improve fault tolerance recommendation indicates that all virtual machine (VM) instances in the indicated compartment are clustered in a single fault domain. Implementing this recommendation improves availability of your VMs across fault domains. Manually move instances to spread them across multiple fault domains',
}


# inserts the data into the provided list
def insert_to_res(res: list, Id: str, comp_id: str, r_type: str, recommendation: str, datapoints=None, description=None) -> list:
    res.append(
        {
            'Resource Id': Id,
            'Compartment Id': comp_id,
            'Resource Type': r_type,
            'Recommendation': recommendation,
            'Description': description,
            'Datapoints': datapoints
        }
    )
    return res


# returns the list of instances
def list_instances(self, compartment_id: str) -> list:
    instance_lst = []
    core_client = oci.core.ComputeClient(self.config)

    list_instances_response = core_client.list_instances(
        compartment_id=compartment_id,
        sort_by="TIMECREATED"
    )

    for item in list_instances_response.data:
        temp = {
            'id': item.id,
            'tags': item.defined_tags,
            'display_name': item.display_name,
            'region': item.region,
            'time_created': item.time_created,
            'fault_domain': item.fault_domain
        }
        instance_lst.append(temp)

    return instance_lst


# returns the list of boot volumes
def list_boot_volumes(self, compartment_id: str) -> list:
    core_client = oci.core.BlockstorageClient(self.config)
    boot_volumes = []

    list_boot_volumes_response = core_client.list_boot_volumes(
        compartment_id=compartment_id
    )
    for item in list_boot_volumes_response.data:
        temp = {
            'id': item.id,
            'tags': item.defined_tags,
            'display_name': item.display_name,
            'time_created': item.time_created,
            'availability_domain': item.availability_domain,
            'is_auto_tune_enabled': item.is_auto_tune_enabled
        }
        boot_volumes.append(temp)
    return boot_volumes


def list_volumes(self, compartment_id: str) -> list:
    core_client = oci.core.BlockstorageClient(self.config)
    volumes = []

    list_volumes_response = core_client.list_volumes(
        compartment_id=compartment_id
    )
    for item in list_volumes_response.data:
        temp = {
            'id': item.id,
            'tags': item.defined_tags,
            'display_name': item.display_name,
            'time_created': item.time_created,
            'availability_domain': item.availability_domain,
            'is_auto_tune_enabled': item.is_auto_tune_enabled
        }
        volumes.append(temp)
    return volumes


# return the memory utilization datapoints of instances
def get_memory_datapoints(self, compartment_id: str, namespace: str) -> list:
    datapoints = []
    start_time = datetime.datetime.now()
    start_time = start_time - relativedelta(days=7)
    start_time = start_time.replace(hour=0, minute=0, second=0, microsecond=0)

    end_time = datetime.datetime.now()
    end_time = end_time.replace(hour=0, minute=0, second=0, microsecond=0)

    MonitoringClient = oci.monitoring.MonitoringClient(self.config)

    summarize_metrics_data_response = MonitoringClient.summarize_metrics_data(
        compartment_id=compartment_id,
        summarize_metrics_data_details=oci.monitoring.models.SummarizeMetricsDataDetails(
            namespace=namespace,
            query="(MemoryUtilization[24h].avg())",
            start_time=start_time,
            end_time=end_time
        ),
        compartment_id_in_subtree=False
    )

    for st in summarize_metrics_data_response.data:
        temp = {
            'id': st.dimensions['resourceId'],
            'datapoints': st.aggregated_datapoints,
            'region': st.dimensions['region']
        }
        datapoints.append(temp)
    return datapoints


# returns cpu utilization datapoints of instances
def get_cpu_datapoints(self, compartment_id: str, namespace: str) -> list:
    datapoints = []
    start_time = datetime.datetime.now()
    start_time = start_time - relativedelta(days=7)
    start_time = start_time.replace(hour=0, minute=0, second=0, microsecond=0)

    end_time = datetime.datetime.now()
    end_time = end_time.replace(hour=0, minute=0, second=0, microsecond=0)

    MonitoringClient = oci.monitoring.MonitoringClient(self.config)

    summarize_metrics_data_response = MonitoringClient.summarize_metrics_data(
        compartment_id=compartment_id,
        summarize_metrics_data_details=oci.monitoring.models.SummarizeMetricsDataDetails(
            namespace=namespace,
            query="(CpuUtilization[24h].avg())",
            start_time=start_time,
            end_time=end_time
        ),
        compartment_id_in_subtree=False
    )

    for st in summarize_metrics_data_response.data:
        temp = {
            'id': st.dimensions['resourceId'],
            'datapoints': st.aggregated_datapoints,
            'region': st.dimensions['region']
        }
        datapoints.append(temp)
    return datapoints


# returns the list of compartments
def list_compartments(self) -> list:
    identity_client = oci.identity.IdentityClient(self.config)
    compartment_lst = []

    list_compartments_response = identity_client.list_compartments(
        compartment_id=self.tenant_id
    )
    for compartment in list_compartments_response.data:
        compartment_lst.append(compartment.id)

    return compartment_lst