import datetime
from oci_recommendation.utils import *
import oci.core
from dateutil.relativedelta import relativedelta


# provides the recommendations for deleting the idle instances
def del_idle_instance_recommendation(self, compartments=None) -> list:
    res = []
    if compartments is None:
        compartments = list_compartments(self)

    for compId in compartments:
        response_cpu = get_cpu_datapoints(self, compId, 'oci_computeagent')
        # response_mem = get_memory_datapoints(self, compId, namespace)
        # print(response_mem)

        for item in response_cpu:
            if len(item['datapoints']) < 7:
                continue

            recommend_flag = True
            for dp in item['datapoints']:
                if dp.value > 3:
                    recommend_flag = False
                    break

            if recommend_flag:
                res = insert_to_res(
                    res, item['id'], compId, "Compute Instance",
                    "Delete Idle Compute Instance",
                    str('cpu datapoints:' + item['datapoints']),
                    r_msgs['del_instance']
                )

    return res


# provide recommendation for purging the unattached boot volumes
def purge_unattached_boot_volume(self, compartments=None) -> list:
    res = []
    core_client = oci.core.ComputeClient(self.config)

    if compartments is None:
        compartments = list_compartments(self)

    for compId in compartments:
        boot_volumes = list_boot_volumes(self, compId)
        # print(boot_volumes)

        for boot_vol in boot_volumes:
            list_boot_volume_attachments_response = core_client.list_boot_volume_attachments(
                availability_domain=boot_vol['availability_domain'],
                compartment_id=compId,
                # limit=584,
                # page="EXAMPLE-page-Value",
                # instance_id="ocid1.test.oc1..<unique_ID>EXAMPLE-instanceId-Value",
                boot_volume_id=boot_vol['id']
            )

            # Get the data from response
            # print(list_boot_volume_attachments_response.data)

            if len(list_boot_volume_attachments_response.data) <= 0:
                res = insert_to_res(
                    res, boot_vol['id'], compId, "Boot Volume",
                    "Purge Unattached boot volume",
                    description=r_msgs['purge boot vol']
                )
    return res


# purge unattached volume
def purge_unattached_volume(self, compartments=None) -> list:
    res = []
    core_client = oci.core.ComputeClient(self.config)

    if compartments is None:
        compartments = list_compartments(self)

    for compId in compartments:
        volumes = list_volumes(self, compId)
        # print(volumes)

        for boot_vol in volumes:
            list_volume_attachments_response = core_client.list_volume_attachments(
                # availability_domain=boot_vol['availability_domain'],
                compartment_id=compId,
                # limit=584,
                # page="EXAMPLE-page-Value",
                # instance_id="ocid1.test.oc1..<unique_ID>EXAMPLE-instanceId-Value",
                boot_volume_id=boot_vol['id']
            )

            # Get the data from response
            # print(list_volume_attachments_response.data)

            if len(list_volume_attachments_response.data) <= 0:
                res = insert_to_res(
                    res, boot_vol['id'], compId, "Volume",
                    "Purge Unattached volume",
                    description=r_msgs['purge vol']
                )
    return res


# generates recommendation for enabling monitoring on compute instances
def enable_monitoring_for_instances(self, compartments=None) -> list:
    res = []
    core_client = oci.core.ComputeClient(self.config)

    if compartments is None:
        compartments = list_compartments(self)

    for compId in compartments:
        instance_lst = list_instances(self, compId)
        # print(instance_lst)

        for instance in instance_lst:
            get_instance_response = core_client.get_instance(
                instance_id=instance['id']
            )
            flag = get_instance_response.data.agent_config.is_monitoring_disabled

            if not flag:
                res = insert_to_res(
                    res, instance['id'], compId, "Compute Instance",
                    "Enable Monitoring",
                    description=r_msgs['enable monitoring']
                )
    return res


# generates recommendation for enable object lifecycle management on buckets
def enable_olm(self, compartments=None) -> list:
    res = []

    if compartments is None:
        compartments = list_compartments(self)

    start_time = datetime.datetime.now()
    start_time = start_time - relativedelta(days=1)
    start_time = start_time.replace(hour=0, minute=0, second=0, microsecond=0)

    end_time = datetime.datetime.now()
    end_time = end_time.replace(hour=0, minute=0, second=0, microsecond=0)

    monitoring_client = oci.monitoring.MonitoringClient(self.config)

    for compId in compartments:
        summarize_metrics_data_response = monitoring_client.summarize_metrics_data(
            compartment_id=compId,
            summarize_metrics_data_details=oci.monitoring.models.SummarizeMetricsDataDetails(
                namespace='oci_objectstorage',
                query="(EnabledOLM[24h].avg())",
                start_time=start_time,
                end_time=end_time
            ),
            compartment_id_in_subtree=False
        )
        for item in summarize_metrics_data_response.data:
            try:
                dp = item.aggregated_datapoints[1].value
            except:
                try:
                    dp = item.aggregated_datapoints[0].value
                except:
                    continue
            if dp == 0:
                res = insert_to_res(
                    res, item.dimensions['resourceID'], compId, "Bucket",
                    "Enable Object Lifecycle Management",
                    description=r_msgs['enable olm']
                )
    return res


# generates recommendation for enable performance auto-tuning for boot volumes
def enable_performance_auto_tuning_for_boot_vol(self, compartments=None) -> list:
    res = []
    if compartments is None:
        compartments = list_compartments(self)

    for compId in compartments:
        boot_volumes = list_boot_volumes(self, compId)
        # print(boot_volumes)

        for boot_vol in boot_volumes:
            if not boot_vol['is_auto_tune_enabled']:
                res = insert_to_res(
                    res, boot_vol['id'], compId, "Boot Volume",
                    "Enable performance auto-tuning",
                    description=r_msgs['enable tuning']
                )
    return res


# generates recommendation for enable performance auto-tuning for block volumes
def enable_performance_auto_tuning_for_block_vol(self, compartments=None) -> list:
    res = []

    if compartments is None:
        compartments = list_compartments(self)

    for compId in compartments:
        block_volumes = list_volumes(self, compId)
        # print(boot_volumes)


        for block_vol in block_volumes:
            if not block_vol['is_auto_tune_enabled']:
                res = insert_to_res(
                    res, block_vol['id'], compId, "Block Volume",
                    "Enable performance auto-tuning",
                    description=r_msgs['enable tuning'].replace('boot','block')
                )
    return res


# aggregates all the recommendations
def get_recommendations(self) -> list:
    res = []
    compartments = list_compartments(self)
    res.extend(purge_unattached_boot_volume(self, compartments))
    res.extend(del_idle_instance_recommendation(self, compartments))
    res.extend(purge_unattached_volume(self, compartments))
    res.extend(enable_monitoring_for_instances(self, compartments))
    res.extend(enable_olm(self, compartments))
    res.extend(enable_performance_auto_tuning_for_block_vol(self, compartments))
    res.extend(enable_performance_auto_tuning_for_boot_vol(self, compartments))

    return res
# end of the code
