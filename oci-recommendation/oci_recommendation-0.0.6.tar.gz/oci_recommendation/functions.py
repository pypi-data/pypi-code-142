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
                    str('cpu datapoints:' + str(item['datapoints'])),
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


# Generates recommendation to improve fault tolerance
def improve_fault_tolerance(self, compartments=None) -> list:
    res = []
    if compartments is None:
        compartments = list_compartments(self)

    for compId in compartments:
        instance_list = list_instances(self, compId)

        if len(instance_list) > 1:
            flag = True
            temp = instance_list[0]['fault_domain']
            for instance in instance_list:
                if instance['fault_domain'] != temp:
                    flag = False
                    break
            if flag:
                res = insert_to_res(
                    res, None, compId, None,
                    "Improve fault tolerance",
                    description=r_msgs['improve_fault']
                )
    return res


def cost_recommendations(self) -> list:
    res = []
    usage_client = oci.usage_api.UsageapiClient(self.config)

    time_usage_started = datetime.datetime.now()
    if int(time_usage_started.strftime('%d')) == 1:
        time_usage_started = time_usage_started - relativedelta(months=1)
        time_usage_started = time_usage_started.replace(day=1, hour=0, minute=0, second=0, microsecond=0)

    else:
        time_usage_started = time_usage_started.replace(day=1, hour=0, minute=0, second=0, microsecond=0)

    time_usage_ended = datetime.datetime.now()
    time_usage_ended = time_usage_ended.replace(hour=0, minute=0, second=0, microsecond=0)

    requestSummarizedUsagesDetails = oci.usage_api.models.RequestSummarizedUsagesDetails(
        tenant_id=self.tenant_id,
        granularity='DAILY',
        query_type='COST',
        group_by=['service', 'skuName', 'region', 'resourceId'],
        time_usage_started=time_usage_started.strftime('%Y-%m-%dT%H:%M:%SZ'),
        time_usage_ended=time_usage_ended.strftime('%Y-%m-%dT%H:%M:%SZ')
    )

    # usageClient.request_summarized_usages
    request_summarized_usages = usage_client.request_summarized_usages(
        requestSummarizedUsagesDetails,
        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
    )

    total_computed_amount = 0
    object_storage_cost = 0
    compute_cost = 0

    for item in request_summarized_usages.data.items:
        try:
            total_computed_amount = total_computed_amount + item.computed_amount
            if item.service == 'Object Storage':
                object_storage_cost = object_storage_cost+item.computed_amount
            elif item.service == 'Compute':
                compute_cost = compute_cost + item.computed_amount

        except TypeError:
            pass

    if total_computed_amount*20/100 < object_storage_cost:
        res = insert_to_res(
            res, None, None, 'Object Storage', 'Review and use life cycle management for storage objects',
            None, description='Storage cost is more than 20% of the overall cost, review and use life cycle management for storage objects'
        )

    if total_computed_amount*50/100 < compute_cost:
        res = insert_to_res(
            res, None, None, 'Compute', 'Review compute instances and right size those',
            None, description=
                'Compute cost is more than 50% of the overall cost, review compute instances and right size those and consider discount options like reserved instances, saving plans etc.'
        )

    if total_computed_amount*75/100 < compute_cost:
        res = insert_to_res(
            res, None, None, 'Compute', 'Shutdown under utilized virtual machines during offline hours',
            None, description=
                'compute cost is more than 75% of the overall cost, Shutdown under utilized virtual machines during offline hours'
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
    res.extend(improve_fault_tolerance(self, compartments))
    res.extend(cost_recommendations(self))

    return res

# end of the code
