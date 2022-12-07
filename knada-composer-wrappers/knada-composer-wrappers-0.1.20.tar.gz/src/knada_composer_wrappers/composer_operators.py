import os
from collections import Callable
from pathlib import Path

from enum import Enum
from datetime import timedelta
from airflow.contrib.operators import kubernetes_pod_operator
from kubernetes.client.models import V1Volume, V1VolumeMount, V1ResourceRequirements
from knada_composer_wrappers.init_containers import create_read_bucket_init_container


class DBTCommand(Enum):
    DEBUG = "debug"
    TEST = "test"
    RUN = "run"


def create_dbt_pod_operator(
    task_id: str,
    bucket_dbt_path: str,
    dbt_cmd: DBTCommand = DBTCommand.DEBUG,
    delete_on_completed: bool = True,
    retries: int = 1,
    retry_delay: timedelta = timedelta(seconds=5),
    namespace: str = "default",
    startup_timeout_seconds: int=360
):
    return kubernetes_pod_operator.KubernetesPodOperator(
        init_containers=[create_read_bucket_init_container(bucket_dbt_path)],
        task_id=task_id,
        name=task_id,
        cmds=["dbt", dbt_cmd.value],
        arguments=["--profiles-dir", "/data", "--project-dir", "/data"],
        env_vars={"REQUESTS_CA_BUNDLE": "/etc/ssl/certs/ca-certificates.crt"},
        namespace=namespace,
        volume_mounts=[
            V1VolumeMount(
                name="data", mount_path="data", sub_path=None, read_only=False
            )
        ],
        startup_timeout_seconds=startup_timeout_seconds,
        volumes=[V1Volume(name="data")],
        image=os.getenv("KNADA_DBT_IMAGE", "navikt/knada-dbt:4"),
        retries=retries,
        retry_delay=retry_delay,
        is_delete_operator_pod=delete_on_completed,
        container_resources=V1ResourceRequirements(
            requests={"memory": "512Mi"},
            limits={"memory": "512Mi"}
        )
    )


def create_python_pod_operator(
    task_id: str,
    python_cmd: str,
    bucket_path: str = None,
    extra_envs: dict = None,
    delete_on_completed: bool = True,
    retries: int = 1,
    retry_delay: timedelta = timedelta(seconds=5),
    namespace: str = "default",
    startup_timeout_seconds: int=360
):

    envs = {"REQUESTS_CA_BUNDLE": "/etc/ssl/certs/ca-certificates.crt"}

    if extra_envs:
        envs = dict(envs, **extra_envs)

    return kubernetes_pod_operator.KubernetesPodOperator(
        init_containers=[create_read_bucket_init_container(bucket_path)] if bucket_path else None,
        task_id=task_id,
        name=task_id,
        cmds=["python", "-c"],
        arguments=[python_cmd],
        env_vars=envs,
        namespace=namespace,
        volume_mounts=[
            V1VolumeMount(
                name="data", mount_path="data", sub_path=None, read_only=False
            )
        ],
        volumes=[V1Volume(name="data")],
        image=os.getenv("KNADA_PYTHON_IMAGE", "navikt/dataprodukt-poc:v6"),
        retries=retries,
        retry_delay=retry_delay,
        startup_timeout_seconds=startup_timeout_seconds,
        is_delete_operator_pod=delete_on_completed,
        container_resources=V1ResourceRequirements(
            requests={"memory": "512Mi"},
            limits={"memory": "512Mi"}
        )
    )


def create_nb_pod_operator(
    task_id: str,
    bucket_path: str = None,
    nb_path: str = None,
    extra_envs: dict = None,
    delete_on_completed: bool = True,
    retries: int = 1,
    retry_delay: timedelta = timedelta(seconds=5),
    namespace: str = "default",
    log_output: bool = False,
    startup_timeout_seconds: int=360,
    nls_lang: str = "NORWEGIAN_NORWAY.AL32UTF8"
):

    env_vars = {
        "LOG_ENABLED": "true" if log_output else "false",
        "NOTEBOOK_PATH": f"/workspace/{Path(nb_path).parent}",
        "NOTEBOOK_NAME": Path(nb_path).name,
        "REQUESTS_CA_BUNDLE": "/etc/ssl/certs/ca-certificates.crt",
        "NLS_LANG": nls_lang
    }

    if extra_envs:
        env_vars = dict(env_vars, **extra_envs)

    return kubernetes_pod_operator.KubernetesPodOperator(
        init_containers=[create_read_bucket_init_container(bucket_path)] if bucket_path else None,
        task_id=task_id,
        name=task_id,
        env_vars=env_vars,
        namespace=namespace,
        volume_mounts=[
            V1VolumeMount(
                name="data", mount_path="/workspace", sub_path=None, read_only=False
            )
        ],
        volumes=[V1Volume(name="data")],
        image=os.getenv("KNADA_NOTEBOOK_OP_IMAGE", "navikt/knada-airflow-nb:2021-09-02-6e78659"),
        retries=retries,
        retry_delay=retry_delay,
        startup_timeout_seconds=startup_timeout_seconds,
        is_delete_operator_pod=delete_on_completed,
        container_resources=V1ResourceRequirements(
            requests={"memory": "512Mi"},
            limits={"memory": "512Mi"}
        )
    )
