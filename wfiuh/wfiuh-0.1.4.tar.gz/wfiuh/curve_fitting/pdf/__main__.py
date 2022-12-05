import concurrent.futures
import glob
import os
import signal
import sys

import pandas as pd
import rich.console
import rich.live
import rich.panel
import rich.pretty
import rich.progress

from ..typed import Model
from . import (
    Beta,
    DoubleTriangular,
    Hoerl,
    InverseGaussian,
    NormalGaussian,
    Polynomial,
    curve_fitting_file,
)


def initializer():
    signal.signal(signal.SIGINT, signal.SIG_IGN)
    sys.stderr = open(file=os.devnull, mode="w")


def main(
    prefix: str = "2-sub-WFIUH_rescaled",
    models: list[Model] = [
        Beta(),
        DoubleTriangular(),
        Hoerl(),
        InverseGaussian(),
        NormalGaussian(),
        Polynomial(),
    ],
) -> int:
    files = glob.glob(pathname=f"{prefix}/*.csv")
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
        rich.panel.Panel(models_progress), rich.panel.Panel(overall_progress)
    )
    with rich.live.Live(progress_group) as live:
        overview_task_id = overall_progress.add_task(description="Overall Progress")
        for model in overall_progress.track(models, task_id=overview_task_id):
            model_task_id = models_progress.add_task(
                description=model.name, total=len(files)
            )
            rets: list[dict] = []
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
                            ),
                            files,
                        )
                    )
                    for future in concurrent.futures.as_completed(futures):
                        try:
                            ret = future.result()
                            if ret:
                                rets.append(ret)
                                models_progress.advance(task_id=model_task_id)
                        except KeyboardInterrupt as e:
                            raise e
                        except Exception as e:
                            live.console.log(
                                model.name,
                                rich.pretty.Pretty(e),
                                style="logging.level.error",
                            )
            except KeyboardInterrupt as e:
                results = pd.DataFrame.from_records(data=rets, index="id")
                results.sort_index(inplace=True)
                results.to_csv(f"{model.name}.csv")
                raise e
            except Exception as e:
                live.console.log(
                    model.name, rich.pretty.Pretty(e), style="logging.level.error"
                )
            else:
                results = pd.DataFrame.from_records(data=rets, index="id")
                results.sort_index(inplace=True)
                results.to_csv(f"{model.name}.csv")
    return 0


if __name__ == "__main__":
    sys.exit(main())
