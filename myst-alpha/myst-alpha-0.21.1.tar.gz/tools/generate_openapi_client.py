import os
import pathlib
import re
import shutil
from typing import Dict

import typer
from openapi_python_client import Config, MetaType, create_new_client

TOOLS_ROOT = pathlib.Path(__file__).parent.absolute()
PROJECT_ROOT = TOOLS_ROOT.parent.absolute()
HANDWRITTEN_MODELS_DIR = PROJECT_ROOT / "myst" / "models"
_KNOWN_HANDWRITTEN_MODELS = ("time_dataset",)
OPENAPI_URL = "https://api.dev.myst.ai/v1alpha2/openapi.json"
SENTINEL_DELETION_MARKER = "# DELETE ME!!"

# Note: The `openapi_python_client` library uses Open API tags to determine the sub-packages to create in the generated
#   endpoints module. It removes the `.` delimiter in tags but we want to create nested packages based on this
#   delimiter. This maps sanitized tags to their original tags so that this script can use the original tags to create
#   the appropriate nested packages. Note that new tags added to the Myst Platform Open API spec must be *manually*
#   added to this mapping.
PACKAGE_NAME_MAP: Dict[str, str] = {
    "aliases": "aliases",
    "connectors": "connectors",
    "organizations": "organizations",
    "projects": "projects",
    "projects_backtests": "projects.backtests",
    "projects_backtests_jobs": "projects.backtests.jobs",
    "projects_backtests_results": "projects.backtests.results",
    "projects_deployments": "projects.deployments",
    "projects_edges": "projects.edges",
    "projects_hpos": "projects.hpos",
    "projects_hpos_jobs": "projects.hpos.jobs",
    "projects_hpos_results": "projects.hpos.results",
    "projects_models": "projects.models",
    "projects_models_fit_jobs": "projects.models.fit_jobs",
    "projects_models_fit_policies": "projects.models.fit_policies",
    "projects_models_fit_results": "projects.models.fit_results",
    "projects_models_inputs": "projects.models.inputs",
    "projects_models_run_results": "projects.models.run_results",
    "projects_nodes": "projects.nodes",
    "projects_nodes_jobs": "projects.nodes.jobs",
    "projects_nodes_policies": "projects.nodes.policies",
    "projects_nodes_results": "projects.nodes.results",
    "projects_operations": "projects.operations",
    "projects_operations_inputs": "projects.operations.inputs",
    "projects_sources": "projects.sources",
    "projects_time_series": "projects.time_series",
    "projects_time_series_layers": "projects.time_series.layers",
    "projects_time_series_run_jobs": "projects.time_series.run_jobs",
    "projects_time_series_run_policies": "projects.time_series.run_policies",
    "projects_time_series_run_results": "projects.time_series.run_results",
    "users": "users",
}


def _move_directory(old_path: pathlib.Path, new_path: pathlib.Path) -> None:
    """Moves a directory, recursively creating any nested directories in new path."""
    # Create new.
    new_path.mkdir(parents=True, exist_ok=True)

    # Copy files from old to new.
    for f_ in old_path.glob("*"):
        shutil.copy(f_, new_path)

    # Remove old.
    shutil.rmtree(old_path)


def _remove_all_files_marked_for_deletion(base_path: pathlib.Path) -> None:
    for root, _, files in os.walk(base_path):
        for file in files:
            if file.endswith(".py"):
                full_path = pathlib.Path(root) / file
                with open(full_path) as f:
                    contents = f.read().strip()

                if contents == SENTINEL_DELETION_MARKER:
                    typer.echo(f"Deleting {file}")
                    full_path.unlink()


def _fix_imports(base_path: pathlib.Path, relative_models_package_name: str, absolute_models_package_name: str) -> None:
    relative_import_pattern = rf"from \.+{relative_models_package_name}"
    absolute_import_pattern = f"from {absolute_models_package_name}"

    typer.echo("Making all model imports absolute")
    typer.echo("Redirecting some imports to known handwritten models")

    for root, _, files in os.walk(base_path):
        for file in files:
            if file.endswith(".py"):
                full_path = pathlib.Path(root) / file
                with open(full_path) as f:
                    file_contents = f.read()

                file_contents = re.sub(
                    pattern=relative_import_pattern, repl=absolute_import_pattern, string=file_contents
                )

                # These auto-generated models have handwritten overrides.
                for model_name in _KNOWN_HANDWRITTEN_MODELS:
                    file_contents = file_contents.replace(
                        f"{absolute_import_pattern}.{model_name} import ", f"from myst.models.{model_name} import "
                    )

                with open(full_path, "w") as f:
                    f.write(file_contents)


def _rename_packages(base_path: pathlib.Path) -> None:
    for path in base_path.iterdir():
        if not path.is_dir():
            continue

        old_dirname = path.name
        new_dirname = PACKAGE_NAME_MAP.get(old_dirname)

        # Same name, so skip!
        if new_dirname == old_dirname:
            continue

        if new_dirname is None:
            raise KeyError(
                f"Package name: `{old_dirname}` does not have a corresponding entry in package name map. If "
                f"this is a new collection of endpoints, their tag must be added to the map so that the client "
                f"generator can rename their package appropriately."
            )

        namespaced_dirname: str = new_dirname.replace(".", "/")

        typer.echo(f"Moving {old_dirname} -> {namespaced_dirname}")

        old_package_path = base_path / old_dirname
        new_package_path = base_path / namespaced_dirname

        _move_directory(old_package_path, new_package_path)


app = typer.Typer()


@app.command()
def main(openapi_url: str = OPENAPI_URL) -> None:
    """Generates the OpenAPI client library."""
    lib_path = PROJECT_ROOT / "myst"
    project_name = "openapi"
    api_dirname = "api"
    models_dirname = "models"

    # Create a (clean) place for the project to go.
    gen_client_container_path = lib_path / project_name
    typer.echo(f"Removing {gen_client_container_path}")
    shutil.rmtree(gen_client_container_path.absolute(), ignore_errors=True)

    # Generate a project config under our custom name.
    config = Config()
    config.project_name_override = project_name

    # Custom Jinja2 templates live here.
    custom_template_dir = TOOLS_ROOT / "client-gen-templates"

    # Generate the openapi client in the correct directory.
    os.chdir(lib_path.absolute())
    typer.echo(f"Creating new client in {gen_client_container_path} based on OpenAPI schema at {openapi_url}")
    create_new_client(
        url=openapi_url, path=None, meta=MetaType.NONE, config=config, custom_template_path=custom_template_dir
    )

    typer.echo(f'Removing all files with sentinel deletion marker "{SENTINEL_DELETION_MARKER}"')
    _remove_all_files_marked_for_deletion(gen_client_container_path)

    typer.echo(f"Fixing imports")

    _fix_imports(
        gen_client_container_path,
        relative_models_package_name=models_dirname,
        absolute_models_package_name=f"{lib_path.name}.{project_name}.{models_dirname}",
    )

    typer.echo(f"Renaming default {api_dirname} package names")

    _rename_packages(gen_client_container_path / api_dirname)

    typer.echo("All done.")


if __name__ == "__main__":
    app()
