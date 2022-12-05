import pickle
import sys
from json import dumps as json_dumps
from json import loads as json_loads
from pathlib import Path
from typing import Any, Dict, Optional

import inquirer as i
import rich
import toml
import typer
from rich.markup import escape

import encord_active.app.conf  # pylint: disable=unused-import
from encord_active.app.app_config import CONFIG_PROPERTIES, AppConfig
from encord_active.app.app_print_utils import get_projects_json
from encord_active.app.common.cli_helpers import choose_local_project, get_local_project
from encord_active.lib.coco.importer import CocoImporter
from encord_active.lib.metrics.fetch_prebuilt_metrics import (
    PREBUILT_PROJECTS,
    fetch_prebuilt_project,
    fetch_prebuilt_project_size,
)
from encord_active.lib.metrics.run_all import run_metrics

APP_NAME = "encord-active"

cli = typer.Typer(
    rich_markup_mode="rich",
    help="""
All commands in this CLI have a --help option, which will guide you on the way.
If you don't find the information you need here, we recommend that you visit
our main documentation: [blue]https://encord-active-docs.web.app[/blue]
""",
    epilog="""
Made by Encord. Contact Encord here: [blue]https://encord.com/contact_us/[/blue] to learn more
about our active learning platform for computer vision.
""",
)
config_cli = typer.Typer(rich_markup_mode="markdown")
import_cli = typer.Typer(rich_markup_mode="markdown")
print_cli = typer.Typer(rich_markup_mode="markdown")
cli.add_typer(config_cli, name="config", help="Configure global settings 🔧")
cli.add_typer(import_cli, name="import", help="Import Projects or Predictions ⬇️")
cli.add_typer(print_cli, name="print")

__PREBUILT_PROJECT_NAMES = list(PREBUILT_PROJECTS.keys())


config = AppConfig(APP_NAME)
state: Dict[str, Any] = {}


@config_cli.command()
def list():
    """
    List Encord Active configuration properties.
    """
    rich.print(toml.dumps(config.contents) or "[bold red]Nothing configured.")


def _check_property(property: str):
    if property not in CONFIG_PROPERTIES:
        rich.print(f"[bold red]`{property}` is not a valid property.")
        rich.print("Valid properties are:")
        rich.print(CONFIG_PROPERTIES)
        exit()


@config_cli.command()
def get(
    property: str = typer.Argument(..., help="Name of the property"),
):
    """
    Print the value of an Encord Active configuration property.
    """
    _check_property(property)
    value = config.contents.get(property)
    rich.print(f"{property} = {value}" or f"[bold red]Property `{property}` not configured.")


@config_cli.command()
def set(
    property: str = typer.Argument(..., help="Name of the property"),
    value: str = typer.Argument(..., help="Value to set"),
):
    """
    Sets an Encord Active configuration property.
    """
    _check_property(property)
    config.contents[property] = value
    config.save()

    rich.print(f"[bold green]Property `{property}` has been set.")


@config_cli.command()
def unset(
    property: str = typer.Argument(..., help="Name of the property"),
):
    """
    Unsets the value of an Encord Active configuration property.
    """
    _check_property(property)
    del config.contents[property]
    config.save()

    rich.print(f"[bold green]Property `{property}` was unset.")


@cli.command()
def download(
    project_name: str = typer.Option(
        None, help=f"Name of the chosen project. Available prebuilt projects: {__PREBUILT_PROJECT_NAMES}."
    ),
):
    """
    Try out Encord Active fast. [bold]Download[/bold] an existing dataset to get started. 📁

    * If --project_name is not given as an argument, available prebuilt projects will be listed
     and the user can select one from the menu.
    """
    project_parent_dir = config.get_or_query_project_path()

    if project_name is not None and project_name not in PREBUILT_PROJECTS:
        rich.print("No such project in prebuilt projects.")
        raise typer.Abort()

    if not project_name:
        rich.print("Loading prebuilt projects ...")
        project_names_with_storage = []
        for project_name in __PREBUILT_PROJECT_NAMES:
            project_size = fetch_prebuilt_project_size(project_name)
            modified_project_name = project_name + (f" ({project_size} mb)" if project_size is not None else "")
            project_names_with_storage.append(modified_project_name)

        questions = [i.List("project_name", message="Choose a project", choices=project_names_with_storage)]
        answers = i.prompt(questions)
        if not answers or "project_name" not in answers:
            rich.print("No project was selected.")
            raise typer.Abort()
        project_name = answers["project_name"].split(" ", maxsplit=1)[0]

    # create project folder
    project_dir = project_parent_dir / project_name
    project_dir.mkdir(exist_ok=True)

    fetch_prebuilt_project(project_name, project_dir)


@import_cli.command(name="predictions")
def import_predictions(
    predictions_path: Path = typer.Argument(
        ...,
        help="Path of the project to which you would like to import the predictions into",
        dir_okay=False,
    ),
):
    """
    [bold]Imports[/bold] a predictions file. The predictions should be in a using the `Prediction` model and stored in a pkl file :brain:
    """

    from encord_active.app.db.predictions import (
        import_predictions as app_import_predictions,
    )

    project_dir = choose_local_project(config)
    if not project_dir:
        raise typer.Abort()

    project = get_local_project(project_dir)

    with open(predictions_path, "rb") as f:
        predictions = pickle.load(f)

    app_import_predictions(project, project_dir, predictions)


@import_cli.command(name="project")
def import_project(
    encord_project_hash: Optional[str] = typer.Option(
        None, "--project_hash", help="Encord project hash of the project you wish to import."
    ),
):
    """
    [bold]Imports[/bold] a project from Encord 📦
    """
    from encord_active.lib.metrics.import_encord_project import main as import_script

    import_script(config, encord_project_hash=encord_project_hash)


@import_cli.command(name="coco")
def import_coco(
    images_dir: Path = typer.Argument(
        ...,
        help="Path to the directory containing the dataset images",
        file_okay=False,
        exists=True,
    ),
    annotations_file: Path = typer.Argument(
        ...,
        help="Path to the file containing the dataset annotations",
        dir_okay=False,
        exists=True,
    ),
):
    """
    [bold]Imports[/bold] a project in the coco data format 🚗
    """
    ssh_key_path = config.get_or_query_ssh_key()
    projects_root = config.get_or_query_project_path()

    coco_importer = CocoImporter(
        images_dir_path=images_dir,
        annotations_file_path=annotations_file,
        ssh_key_path=ssh_key_path,
        destination_dir=projects_root,
    )

    dataset = coco_importer.create_dataset()
    ontology = coco_importer.create_ontology()
    coco_importer.create_project(
        dataset=dataset,
        ontology=ontology,
    )

    run_metrics(data_dir=coco_importer.project_dir)


@print_cli.command(name="encord-projects")
def print_encord_projects(
    query: Optional[str] = typer.Option(None, help="Optional fuzzy title filter; SQL syntax."),
):
    """
    Print the mapping between \`project_hash\`es of your Encord projects and their titles.

    You can query projects by title with the SQL fuzzy syntax. To look for a title including "validation" you would do:

    > encord-active print encord-projects --query "%validation%"

    """
    json_projects = get_projects_json(config, query)
    if state.get("json_output"):
        Path("./encord-projects.json").write_text(json_projects, encoding="utf-8")
    else:
        rich.print(escape(json_projects))


@print_cli.command(name="ontology")
def print_ontology():
    """
    [bold]Prints[/bold] an ontology mapping between the class name to the `featureNodeHash` JSON format.
    """
    project_dir = choose_local_project(config)
    if not project_dir:
        raise typer.Abort()

    project = get_local_project(project_dir)
    objects = project.ontology["objects"]

    ontology = {o["name"].lower(): o["featureNodeHash"] for o in objects}
    json_ontology = json_dumps(ontology, indent=2)

    if state.get("json_output"):
        Path("./ontology.json").write_text(json_ontology, encoding="utf-8")
        rich.print("Stored mapping in [blue]`./ontology.json`")
    else:
        rich.print(escape(json_ontology))


@print_cli.command(name="data-mapping")
def print_data_mapping(limit: int = typer.Option(None, help="Limit the result to the first `limit` data hashes")):
    """
    [bold]Prints[/bold] a mapping between `data_hashes` and their corresponding `filename`
    """
    project_dir = choose_local_project(config)
    if not project_dir:
        raise typer.Abort()

    mapping: Dict[str, str] = {}

    for label in (project_dir / "data").iterdir():
        if not label.is_dir() and not (label / "label_row.json").is_file():
            continue

        label_row = json_loads((label / "label_row.json").read_text())
        mapping = {
            **mapping,
            **{data_hash: value["data_title"] for data_hash, value in label_row["data_units"].items()},
        }
        if limit and len(mapping) > limit:
            break

    if limit and limit < len(mapping):
        mapping = {k: v for i, (k, v) in enumerate(mapping.items()) if i < limit}

    json_mapping = json_dumps(mapping, indent=2)

    if state.get("json_output"):
        Path("./data_mapping.json").write_text(json_mapping, encoding="utf-8")
        rich.print("Stored mapping in [blue]`./data_mapping.json`")
    else:
        rich.print(escape(json_mapping))


@print_cli.command(name="system-info")
def print_system_info():
    """
    [bold]Prints[/bold] the information of the system for the purpose of bug reporting.
    """
    import platform

    import psutil

    def get_size(bytes, suffix="B"):
        """
        Scale bytes to its proper format
        e.g:
            1253656 => '1.20MB'
            1253656678 => '1.17GB'
        """
        factor = 1024
        for unit in ["", "K", "M", "G", "T", "P"]:
            if bytes < factor:
                return f"{bytes:.2f}{unit}{suffix}"
            bytes /= factor

    print("System Information:")
    uname = platform.uname()
    print(f"\tSystem: {uname.system}")
    print(f"\tRelease: {uname.release}")
    print(f"\tMachine: {uname.machine}")
    print(f"\tProcessor: {uname.processor}")
    print(f"\tPython: {sys.version}")
    print("\nCPU Info:")
    print("\tPhysical cores:", psutil.cpu_count(logical=False))
    print("\tTotal cores:", psutil.cpu_count(logical=True))
    print(f"\tTotal CPU Usage: {psutil.cpu_percent()}%")
    print("\nMemory Information:")
    svmem = psutil.virtual_memory()
    print(f"\tTotal: {get_size(svmem.total)}")
    print(f"\tAvailable: {get_size(svmem.available)}")
    print(f"\tUsed: {get_size(svmem.used)}")


@print_cli.callback()
def main(json: bool = False):  # pylint: disable=redefined-outer-name
    """
    [bold]Print[/bold] useful information 🖨️
    """
    state["json_output"] = json


@cli.command()
def visualise(
    project_path: Optional[Path] = typer.Argument(
        None,
        help="Path of the project you would like to visualise",
        file_okay=False,
    ),
):
    """
    Launches the application with the provided project ✨
    """
    from streamlit.web import cli as stcli

    streamlit_page = (Path(__file__).parent / "streamlit_entrypoint.py").expanduser().absolute()

    project_path = project_path or choose_local_project(config)

    if not project_path:
        raise typer.Abort()

    data_dir = project_path.expanduser().absolute().as_posix()
    sys.argv = ["streamlit", "run", streamlit_page.as_posix(), data_dir]
    sys.exit(stcli.main())  # pylint: disable=no-value-for-parameter


if __name__ == "__main__":
    cli(prog_name=APP_NAME)
