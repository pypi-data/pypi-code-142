"""
Reading data from RAW Limax files.

Anonymization.
"""

from pathlib import Path
from typing import Any, Dict, List, Optional

import pandas as pd

from limax import log
from limax.console import console
from limax.model import LX, LXData, LXMetaData
from limax.plot import plot_lx_matplotlib


logger = log.get_logger(__file__)


def read_limax_dir(input_dir: Path, output_dir: Path) -> None:
    """Read limax data from folder."""
    # process all files
    for limax_csv in input_dir.glob("**/*.csv"):
        limax_csv_rel = limax_csv.relative_to(input_dir)
        output_path: Path = Path(output_dir / limax_csv_rel)
        read_limax_file(limax_csv=limax_csv, output_dir=output_path.parent)


def read_limax_file(
    limax_csv: Path, output_dir: Optional[Path] = None, line_offset: int = 13
) -> LX:
    """Read limax data."""
    if output_dir:
        output_dir.mkdir(parents=True, exist_ok=True)
        output_path = output_dir / f"{limax_csv.stem}.json"
        fig_path = output_dir / f"{limax_csv.stem}.png"
        console.log(f"Processing '{limax_csv}' -> '{output_path}'")

    with open(limax_csv, "r") as f:
        lines: List[str] = f.readlines()
        # remove empty lines
        lines = [line.strip() for line in lines]
        lines = [line for line in lines if len(line) > 0]
        # strip header lines
        time, dob, error = [], [], []

        # parse metadata
        # 0  # mID 102
        # 1  # 'doc' (, )
        # 2  # Dr. Max Mustermann
        # 3  # 01.01.2010 08:30
        # 4  # utouARg
        # 5  # 160 cm
        # 6  # 70 kg
        # 7  # 43,295187
        # 8  # 44,395187
        # 9  # 630,0
        # 10  # Nahrungskarenz: über 3 Std., Raucher: Nein, Sauerstoff: Nein, Beatmung: Nein, Medikation: Ja
        md_lines = [line[2:] for line in lines[:line_offset]]
        tokens: List[str] = md_lines[10].split(",")
        metadata_dict: Dict[str, Any] = {
            "mid": md_lines[0].split()[1],
            # "name": md_lines[2],  # drop patient information
            "datetime": md_lines[3],
            "height": float(md_lines[5].split()[0]),
            "weight": float(md_lines[6].split()[0]),
            "food_abstinence": tokens[0].split(":")[1].strip(),
            "smoking": tokens[1].split(":")[1].strip(),
            "oxygen": tokens[2].split(":")[1].strip(),
            "ventilation": tokens[3].split(":")[1].strip(),
            "medication": tokens[4].split(":")[1].strip(),
        }
        for key in ["smoking", "oxygen", "ventilation", "medication"]:
            if metadata_dict[key].lower() == "ja":
                metadata_dict[key] = True
            elif metadata_dict[key].lower() == "nein":
                metadata_dict[key] = False
            else:
                logger.error(
                    f"Invalid value in metadata: '{key}: {metadata_dict[key]}'"
                )
                metadata_dict[key] = True

        lx_metadata: LXMetaData = LXMetaData(**metadata_dict)

        # parse data
        for line in lines[line_offset:]:
            tokens = [t.strip() for t in line.split("\t")]
            time.append(int(tokens[0]))
            dob.append(float(tokens[1]))
            error.append(str(tokens[2]))

    d: Dict[str, Any] = {
        "time": time,
        "dob": dob,
        "error": error,
    }
    df = pd.DataFrame(data=d)
    df = df[["time", "dob", "error"]]

    # sort by time (some strange artefacts in some files)
    df.sort_values(by=["time"], inplace=True)
    lx_data = LXData(
        time=list(df.time.values), dob=list(df.dob.values), error=list(df.error.values)
    )
    lx = LX(metadata=lx_metadata, data=lx_data)

    # serialization to JSON
    if output_dir:
        with open(output_path, "w") as f_json:
            f_json.write(lx.json(indent=2))
        plot_lx_matplotlib(lx, fig_path=fig_path)

    return lx


if __name__ == "__main__":
    from limax import EXAMPLE_LIMAX_PATH, PROCESSED_DIR

    lx = read_limax_file(limax_csv=EXAMPLE_LIMAX_PATH, output_dir=PROCESSED_DIR)
    console.print(lx)
    console.print(lx.json())
    console.print(lx.data.to_df())

    # read_limax_dir(input_dir=RAW_DIR, output_dir=PROCESSED_DIR)
