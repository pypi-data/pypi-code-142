import inspect
import logging
import os
from importlib import import_module
from typing import Callable, List, Optional, Union

from encord.project_ontology.object_type import ObjectShape

from encord_active.lib.common.metric import AnnotationType, DataType, Metric, MetricType
from encord_active.lib.common.tester import perform_test


def get_metrics(module: Optional[Union[str, list[str]]] = None, filter_func=lambda x: True):
    if module is None:
        module = ["geometric", "heuristic", "semantic"]
    elif isinstance(module, str):
        module = [module]

    return [i for m in module for i in get_module_metrics(m, filter_func)]


def get_module_metrics(module_name: str, filter_func: Callable) -> List:
    if __name__ == "__main__":
        base_module_name = ""
    else:
        base_module_name = __name__[: __name__.rindex(".")] + "."  # Remove "run_all"

    metrics = []
    path = os.path.join(os.path.dirname(__file__), *module_name.split("."))
    for file in os.listdir(path):
        if file.endswith(".py") and not file.startswith("_") and not file.split(".")[0].endswith("_"):
            logging.debug("Importing %s", file)
            clsmembers = inspect.getmembers(
                import_module(f"{base_module_name}{module_name}.{file.split('.')[0]}"), inspect.isclass
            )
            for cls in clsmembers:
                if issubclass(cls[1], Metric) and cls[1] != Metric and filter_func(cls[1]):
                    metrics.append((f"{base_module_name}{module_name}.{file.split('.')[0]}", f"{cls[0]}"))

    return metrics


def run_all_heuristic_metrics():
    run_metrics(filter_func=lambda x: x.METRIC_TYPE == MetricType.HEURISTIC)


def run_all_image_metrics():
    run_metrics(filter_func=lambda x: x.DATA_TYPE == DataType.IMAGE)


def run_all_polygon_metrics():
    run_metrics(filter_func=lambda x: x.ANNOTATION_TYPE in [AnnotationType.OBJECT.POLYGON, AnnotationType.ALL])


def run_all_prediction_metrics(**kwargs):
    # Return all metrics that apply to objects.
    def filter(m: Metric):
        at = m.ANNOTATION_TYPE
        if isinstance(at, list):
            for t in at:
                if isinstance(t, ObjectShape):
                    return True
            return False
        else:
            return isinstance(at, ObjectShape)

    run_metrics(filter_func=filter, **kwargs)


def run_metrics(filter_func: Callable = lambda x: True, **kwargs):
    metrics: List[Metric] = list(
        map(
            lambda mod_cls: import_module(mod_cls[0]).__getattribute__(mod_cls[1])(),
            get_metrics(filter_func=filter_func),
        )
    )
    perform_test(metrics, **kwargs)


if __name__ == "__main__":
    # To run on all samples:
    import os
    from pathlib import Path

    import yaml
    from encord import EncordUserClient

    conf_file = Path(__file__).parents[0] / "conf" / "config.yaml"
    if conf_file.is_file():
        # Fallback to read old config file and store it in new format, directly in the
        # data directory instead of in the code root.
        with conf_file.open("r", encoding="utf-8") as f:
            conf = yaml.safe_load(f)

        data_dir = conf["paths"]["data"]
        private_key_path = conf["paths"]["private_key"]
        project_name = conf["encord"]["project_name"]

        with open(os.path.expanduser(private_key_path), "r", encoding="utf-8") as f:
            private_key = f.read()

        client = EncordUserClient.create_with_ssh_private_key(private_key)
        project_desc = client.get_projects(title_eq=project_name)[0]["project"]
        project = client.get_project(project_hash=project_desc.project_hash)
        project_name = f"{project.project_hash[:8]}_{project.title.replace(' ', '-').lower()}"
        project_root = Path(data_dir).expanduser() / project_name

        project_meta = {
            "project_title": project.title,
            "project_description": project.description,
            "project_hash": project.project_hash,
            "ssh_key_path": os.path.abspath(os.path.expanduser(private_key_path)),
        }
        meta_file_path = project_root / "project_meta.yaml"
        with meta_file_path.open("w", encoding="utf-8") as f:
            f.write(yaml.dump(project_meta))
    else:
        # Just specify a project root by input.
        project_root = Path(input("Choose data root: ")).expanduser().absolute()

    run_metrics(data_dir=project_root)
