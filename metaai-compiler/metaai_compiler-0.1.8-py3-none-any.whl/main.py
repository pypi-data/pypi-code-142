from __future__ import annotations
import sys
import json
import logging
from pathlib import PurePosixPath
from typing import List, Dict, Optional, Union
import argparse
from kubernetes.client.models import V1EnvVar
import warnings

from dataclasses import dataclass, field
from kfp import dsl
from kfp import compiler as kfp_compiler
from kfp.compiler import Compiler
import kfp
from kfp.dsl import UserContainer, ContainerOp, Sidecar
from kfp.dsl._container_op import Container

warnings.filterwarnings("ignore")

logger = logging.getLogger(__name__)


@dataclass
class Constants:
    METAAI_VOLUMES_BASE_PATH: str = "/metaai"

    METAAI_CODE_PATH: str = field(
        default_factory=lambda: str(
            PurePosixPath(Constants.METAAI_VOLUMES_BASE_PATH, "code/")
        )
    )

    STORAGE_DEFAULT_IMAGE: str = (
        "registry.cn-hangzhou.aliyuncs.com/metaai/storage-initializer:v0.8.1"
    )

    STORAGE_DEFAULT_CPU_LIMIT: str = "1"
    STORAGE_DEFAULT_MEMORY_LIMIT: str = "1Gi"

    STORAGE_DEFAULT_CPU_REQUEST: str = "100m"
    STORAGE_DEFAULT_MEMORY_REQUEST: str = "100Mi"

    POD_DEFAULT_CPU_REQUEST: str = "1"

    POD_DEFAULT_MEMORY_REQUEST: str = "1Gi"


class HumanComponent:
    def __init__(
            self,
            id: str,
            name: str,
            image: str,
            envs: Optional[None | List[Dict[str, str]]] = None,
            artifacts_outputs: Optional[List] = None,
            command: Optional[str | List[str]] = None,
            arguments: Optional[str | None | List[str]] = None,
            init_containers: Optional[List[Dict]] | None = None,
            sidecars: Optional[List[Dict]] | None = None,
            # delete in 0.1.8
            # code_path: Optional[Union[None, str]] = None,
            image_pull_policy=None,
            cpu=None,
            memory=None,
            gpu=None,
            **kwargs,
    ):
        self.cons = Constants()
        self.id = id
        self.name = name
        self.command = command
        self.arguments = arguments
        self.image = image
        self.cpu = str(cpu) if cpu else self.cons.POD_DEFAULT_CPU_REQUEST
        self.memory = memory if memory else self.cons.POD_DEFAULT_MEMORY_REQUEST
        self.gpu = gpu
        self.image_pull_policy = image_pull_policy

        if envs:
            self.envs = self.__envs_to_envvars(envs)

        self.artifacts_outputs = artifacts_outputs

        self.init_containers = self.__get_init_containers(init_containers)
        self.sidecars = self.__get_sidecars(sidecars)

        # remove in 0.1.8
        # if code_path:
        #     self.init_containers = self.__get_init_containers(code_path)

    def __make_user_container(self, container_info_lst: List[Dict]) -> List[UserContainer]:

        pass

    # init container
    def __get_init_containers(self, init_container_lst: List[Dict]) -> List[UserContainer]:
        # init containers create
        if not init_container_lst:
            return []
        containers = []
        for infos in init_container_lst:
            containers.append(UserContainer(
                image=infos["images"],
                name=infos["name"],
                command=infos["command"],
                env=self.__envs_to_envvars(infos["envs"])
            ))

        return containers

    def __get_sidecars(self, sidecars: List[Dict]) -> List[UserContainer]:
        # sidecar containers create
        if not sidecars:
            return []
        containers = []
        for infos in sidecars:
            containers.append(Sidecar(
                image=infos["images"],
                name=infos["name"],
                command=infos["command"],
                env=self.__envs_to_envvars(infos["envs"])
            ))

        return containers

    @staticmethod
    def __envs_to_envvars(envs: List[Dict[str, str]]):
        lst = []
        for env_dic in envs:
            for k, v in env_dic.items():
                lst.append(V1EnvVar(name=k, value=v))

        return lst

    @staticmethod
    def __add_human_name_to_op(func, name):
        func._component_human_name = name

        return dsl.component(func)()

    def __set_container_resources(
            self,
            container: Union[dsl.ContainerOp, dsl.UserContainer],
            cpu_req=None,
            memory_req=None,
            cpu_limit=None,
            memory_limit=None,
            is_init=False,
    ) -> Union[UserContainer, Container, ContainerOp]:
        rcpu = cpu_req if cpu_req else self.cpu
        rmem = memory_req if memory_req else self.memory
        lcpu = cpu_limit if cpu_limit else rcpu
        lmemory = memory_limit if memory_limit else rmem

        container.set_cpu_request(rcpu).set_memory_request(rmem).set_cpu_limit(
            lcpu
        ).set_memory_limit(lmemory)

        if self.gpu and not is_init:
            container.set_gpu_limit(self.gpu.get("num"), self.gpu.get("vendor"))

        # add annotations
        if hasattr(container, "add_pod_annotation"):
            container.add_pod_annotation(
                name="pipelines.kubeflow.org/component_uuid", value=self.id
            )
        if hasattr(container, "display_name"):
            container.display_name = self.name

        return container

    def __call__(self, *args, **kwargs):

        op = lambda: dsl.ContainerOp(
            name="main",
            image=self.image,
            command=self.command,
            arguments=self.arguments,
            init_containers=self.init_containers,
            container_kwargs={
                "env": self.envs,
                "working_dir": self.cons.METAAI_CODE_PATH,
                "image_pull_policy": self.image_pull_policy,
            },
            # out put config names and values to set here
            output_artifact_paths=self.artifacts_outputs
        )

        return self.__set_container_resources(
            self.__add_human_name_to_op(op, self.name)
        )

    @classmethod
    def from_dict(cls, d: dict):
        return cls(**d)()


class PipelineCompiler:
    def __init__(
            self,
            name: str,
            description: str,
            components: List,
            volumes: List = None,
            **kwargs,
    ):
        self.name = name
        self.description = description
        self.components = components
        self.pipeline_conf = dsl.PipelineConf()
        if "globalEnv" in kwargs:
            genv_dic: dict = kwargs.pop("globalEnv")
            genv_lst = [{"name": k, "value": v} for k, v in genv_dic.items()]

            setattr(self.pipeline_conf, "template_defaults", {
                "container": {
                    "env": genv_lst
                }
            })

    @classmethod
    def from_json(cls, json_path: str):
        with open(json_path, "r", encoding="UTF-8") as jfp:
            return cls.from_dict(json.load(jfp))

    @classmethod
    def from_dict(cls, d: dict):
        return cls(**d)

    @staticmethod
    def __get_envs_from_params(runtimes, inputs, outputs):
        lst = []

        if runtimes:
            lst.append({"RUN_CONFIG": runtimes})
        if inputs:
            lst.append(inputs)
        if outputs:
            lst.append(outputs)

        return lst

    @staticmethod
    def __parse_python_arguments(arguments_str: str):

        if arguments_str.endswith(".py"):
            return ["python", f"{arguments_str}"]

        return ["python", "-m", f"{arguments_str}"]

    def __parse_component_kvs(self, comp_d: dict):


        return {
            "name": comp_d.get("name", "no name"),
            "id": comp_d.get("id"),
            "image": comp_d.get("image"),
            "image_pull_policy": comp_d.get("imagePullPolicy", "Always"),
            "envs": self.__get_envs_from_params(
                comp_d.get("runtimes"), comp_d.get("outputs"), comp_d.get("inputs")
            ),
            "artifacts_outputs": comp_d.get("outputs"),
            "command": self.__parse_python_arguments(comp_d.get("mainEnter")),
            # "code_path": comp_d.get("codePath"),
            "cpu": comp_d.get("cpu"),
            "memory": comp_d.get("memory"),
            "gpu": comp_d.get("gpu"),
        }

    def __parse_component_dependencies(self, lst):
        # 解析顺序关系
        # {"id": HumanComponent}
        human_component_dic: Dict[str, dsl.ContainerOp] = {}
        # {"id": afters}
        component_afters: Dict[str, list] = {}
        for comp in lst:
            _id = comp["id"]
            if not comp.get("skip", False):
                human_component_dic[_id] = HumanComponent.from_dict(
                    self.__parse_component_kvs(comp)
                )

                component_afters[_id] = comp.get("afterIds", [])

        return human_component_dic, component_afters

    def compile(self, output_path: str):

        func = dsl.pipeline(name=self.name, description=self.description)(self.main())

        # kfp.compiler.Compiler().compile(func, output_path)
        kfp_compiler_cls = kfp.compiler.Compiler()
        wkflow = kfp_compiler_cls._compile(func)

        if hasattr(self.pipeline_conf, "template_defaults"):
            wkflow["spec"]["templateDefaults"] = self.pipeline_conf.template_defaults

        # add archive none:{} to outputs artifacts
        for tpl in wkflow["spec"]["templates"]:
            for artifact in tpl.get("outputs", {}).get("artifacts", []):
                artifact["archive"] = {"none": {}}

        kfp_compiler_cls._write_workflow(wkflow, output_path)
        kfp_compiler.compiler._validate_workflow(wkflow)

    @staticmethod
    def parser_id_to_variable(id_str):
        # id的变量合法性
        # 中划线 空格，改成下划线 且变为小写。
        # 变量开头不能为数字，加一个前缀var
        if not isinstance(id_str, str):
            id_str = str(id_str)
        return "var_" + id_str.strip().replace("-", "_").replace(" ", "_").lower()

    def main(self):
        def func():
            components_dic, dependencies = self.__parse_component_dependencies(
                self.components
            )

            for id_, op in components_dic.items():
                if id_ not in locals():
                    exec(f"{self.parser_id_to_variable(id_)} = op")
            for id_, afters in dependencies.items():
                for aft_id in afters:
                    try:
                        exec(
                            f"{self.parser_id_to_variable(aft_id)}.after({self.parser_id_to_variable(id_)})"
                        )
                    except Exception as e:
                        logger.error("The relationship between components may be incorrect. \n"
                                     "Please analyze your input json\n "
                                     "Possible errors include: \n"
                                     "1: the dependent component has been skipped; \n"
                                     "2: the component ID is incorrect; \n"
                                     "3: the ID of the afterIds of the component does not exist in json.component")

                        sys.exit(1)

        return func


def main():
    parser = argparse.ArgumentParser(prog="kfp component compiler with metaai")
    parser.add_argument(
        "--input", dest="input", type=str, help="metaai components json input abspath"
    )
    parser.add_argument(
        "--output",
        dest="output",
        type=str,
        help="kfp component argo yaml output abspath",
    )
    parser.add_argument(
        "--root_path",
        dest="root_path",
        type=str,
        help="pod runtime volumes mount root path",
    )

    args, _ = parser.parse_known_args()

    if args.root_path:
        Constants.METAAI_VOLUMES_BASE_PATH = args.root_path.strip()

    ins = PipelineCompiler.from_json(args.input.strip())
    ins.compile(args.output.strip())


if __name__ == "__main__":
    main()
