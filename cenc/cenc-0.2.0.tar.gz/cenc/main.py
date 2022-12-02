import json
import os
import sys
import time
import requests
import typer


app = typer.Typer()
CENC_ENDPOINT = os.environ.get("CENC_ENDPOINT", "https://ffmpeg-kopg2w5bka-ez.a.run.app/ffmpeg")

def create_task(command: str):
    response = requests.post(CENC_ENDPOINT, json={"command": command})
    if response.status_code == 200:
        task_id = response.json()["id"]
        typer.secho(f"Started task {task_id}", fg=typer.colors.GREEN)
        return task_id
    else:
        typer.secho(f"Error: {response.text}", fg=typer.colors.RED, err=True)
        raise typer.Exit(1)


def track_progress(task_id):
    typer.secho(
        f"Logs for task {task_id} will appear in a minute",
        fg=typer.colors.GREEN,
    )
    prev_log_length = 0
    while True:
        time.sleep(2)
        # Get the status of the task
        response = requests.get(f"{CENC_ENDPOINT}/{task_id}")
        if response.status_code != 200:
            continue
        data = response.json()
        if data is None:
            continue

        # Print the log
        if "logs" in data and len(data["logs"]) > prev_log_length:
            typer.echo(data["logs"][prev_log_length:], nl=False)
            prev_log_length = len(data["logs"])

        # Check if the task is done
        returncode = data.get("returncode")
        if returncode is not None:
            del data["logs"]
            typer.secho(
                json.dumps(data, indent=2, sort_keys=True),
                fg=typer.colors.GREEN,
            )
            raise typer.Exit(returncode)

@app.command(
    help='Print logs for the task id.'
)
def logs(task_id: str):
    track_progress(task_id)

@app.command(
    help="Run ffmpeg with the given arguments on the cloud",
)
def run(command: str):
    typer.secho("Your task is starting...", fg=typer.colors.GREEN)
    task_id = create_task(command)
    track_progress(task_id)
