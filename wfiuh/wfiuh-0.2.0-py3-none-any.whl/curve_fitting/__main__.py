import concurrent.futures
import glob
import itertools
import os
import signal
import sys

import click
import pandas as pd
import rich.console
import rich.live
import rich.panel
import rich.pretty
import rich.progress

from . import curve_fitting_file
from .models import (
    Beta,
    DoubleTriangular,
    Gamma,
    Hoerl,
    InverseGaussian,
    Model,
    NormalGaussian,
    Polynomial,
    Rational,
    ShiftedLogPearson3,
)


def initializer():
    signal.signal(signal.SIGINT, signal.SIG_IGN)
    sys.stderr = open(file=os.devnull, mode="w")


def save_results(results: list[dict], filepath: str) -> None:
    if not results:
        return
    df = pd.DataFrame.from_records(data=results, index="id")
    df.sort_index(inplace=True)
    os.makedirs(name=os.path.dirname(filepath), exist_ok=True)
    df.to_csv(filepath)


@click.command(name="curve-fitting")
@click.option(
    "--input-dir", show_default=True, type=click.Path(), default="2-sub-WFIUH_rescaled"
)
@click.option(
    "--output-dir", show_default=True, type=click.Path(), default="results/params/cdf"
)
@click.option(
    "--func",
    show_default=True,
    type=click.Choice(choices=["cdf", "pdf"]),
    default="cdf",
)
@click.option("--verbose", is_flag=True, default=False)
def main(
    input_dir: str = "2-sub-WFIUH_rescaled",
    output_dir: str = "results/params/cdf",
    models: list[Model] = [
        NormalGaussian(),
        InverseGaussian(),
        Polynomial(),
        Rational(),
        ShiftedLogPearson3(),
        Gamma(),
        Hoerl(),
        Beta(),
        DoubleTriangular(),
    ],
    func: str = "cdf",
    verbose: bool = False,
) -> int:
    files = glob.glob(pathname=f"{input_dir}/*.csv")
    overall_progress = rich.progress.Progress(
        rich.progress.TextColumn(
            text_format="{task.description}", style="logging.level.info"
        ),
        rich.progress.BarColumn(),
        rich.progress.TaskProgressColumn(),
        rich.progress.MofNCompleteColumn(),
        rich.progress.TimeElapsedColumn(),
    )
    models_progress = rich.progress.Progress(
        rich.progress.TextColumn(
            text_format="{task.description}", style="logging.level.info"
        ),
        rich.progress.BarColumn(),
        rich.progress.TaskProgressColumn(),
        rich.progress.MofNCompleteColumn(),
        rich.progress.TimeElapsedColumn(),
        rich.progress.TimeRemainingColumn(),
    )
    progress_group = rich.console.Group(
        rich.panel.Panel(models_progress, expand=False),
        rich.panel.Panel(overall_progress, expand=False),
    )
    with rich.live.Live(progress_group) as live:
        overview_task_id = overall_progress.add_task(description="Overall Progress")
        for model in overall_progress.track(models, task_id=overview_task_id):
            model_task_id = models_progress.add_task(
                description=f"{model.name} {func}", total=len(files)
            )
            results: list[dict] = []
            try:
                with concurrent.futures.ProcessPoolExecutor(
                    initializer=initializer
                ) as pool:
                    futures: list[concurrent.futures.Future] = list(
                        map(
                            lambda filepath: pool.submit(
                                curve_fitting_file,
                                model=model,
                                filepath=filepath,
                                func=func,
                            ),
                            files,
                        )
                    )
                    for future in concurrent.futures.as_completed(futures):
                        try:
                            result = future.result()
                            if result:
                                results.append(result)
                                models_progress.advance(task_id=model_task_id)
                        except KeyboardInterrupt as e:
                            raise e
                        except Exception as e:
                            if verbose:
                                live.console.log(
                                    model.name,
                                    func,
                                    rich.pretty.Pretty(e),
                                    style="logging.level.error",
                                )
            except KeyboardInterrupt as e:
                save_results(results, os.path.join(output_dir, f"{model.name}.csv"))
                raise e
            except Exception as e:
                live.console.print_exception()
            else:
                save_results(results, os.path.join(output_dir, f"{model.name}.csv"))
            finally:
                models_progress.stop_task(model_task_id)
    return 0


if __name__ == "__main__":
    sys.exit(main())
