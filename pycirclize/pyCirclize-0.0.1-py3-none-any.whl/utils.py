from __future__ import annotations

import csv
import math
import os
from dataclasses import dataclass
from io import StringIO, TextIOWrapper
from pathlib import Path
from typing import Any
from urllib.request import urlretrieve

import numpy as np
from Bio import Entrez
from matplotlib.cm import get_cmap
from matplotlib.colors import Colormap, to_hex

from pycirclize import config


def load_prokaryote_example_file(
    filename: str,
    cache_dir: str | Path | None = None,
    overwrite_cache: bool = False,
) -> Path:
    """Load pycirclize example Genbank or GFF file

    Load example file from https://github.com/moshi4/pycirclize-data/
    and cache file in local directory (Default: `~/.cache/pycirclize/`).

    List of example Genbank or GFF filename
    - `enterobacteria_phage.gbk`
    - `enterobacteria_phage.gff`
    - `escherichia_coli.gbk.gz`
    - `escherichia_coli.gff.gz`

    Parameters
    ----------
    filename : str
        Genbank or GFF filename (e.g. `enterobacteria_phage.gff`)
    cache_dir : str | Path | None, optional
        Output cache directory (Default: `~/.cache/pycirclize/`)
    overwrite_cache : bool, optional
        If True, overwrite cached file

    Returns
    -------
    file_path : Path
        Genbank or GFF file
    """
    # Check specified filename exists or not
    if filename not in config.PROKARYOTE_FILES:
        err_msg = f"filename='{filename}' not found."
        raise ValueError(err_msg)

    # Cache local directory
    if cache_dir is None:
        package_name = __name__.split(".")[0]
        cache_base_dir = Path.home() / ".cache" / package_name
        cache_dir = cache_base_dir / "prokaryote"
        os.makedirs(cache_dir, exist_ok=True)
    else:
        cache_dir = Path(cache_dir)

    # Download file
    file_url = config.GITHUB_DATA_URL + f"prokaryote/{filename}"
    file_path = cache_dir / filename
    if overwrite_cache or not file_path.exists():
        urlretrieve(file_url, file_path)

    return file_path


def load_eukaryote_example_dataset(
    name: str = "hg38",
    cache_dir: str | Path | None = None,
    overwrite_cache: bool = False,
) -> tuple[Path, Path, list[ChrLink]]:
    """Load pycirclize eukaryote example dataset

    Load example file from https://github.com/moshi4/pycirclize-data/
    and cache file in local directory (Default: `~/.cache/pycirclize/`).

    List of dataset contents (download from UCSC)
    1. Chromosome BED file (e.g. `chr1 0 248956422`)
    2. Cytoband file (e.g. `chr1 0 2300000 p36.33 gneg`)
    3. Chromosome link list (e.g. `chr1 1000 4321 chr3 8000 5600`)

    Parameters
    ----------
    name : str, optional
        Dataset name (`hg38` or `mm10`)
    cache_dir : str | Path | None, optional
        Output cache directory (Default: `~/.cache/pycirclize/`)
    overwrite_cache : bool
        If True, overwrite cached dataset

    Returns
    -------
    chr_bed_file, cytoband_file, chr_link_list : tuple[Path, Path, list[ChrLink]]
        BED file, Cytoband file, Chromosome link list
    """
    # Check specified name dataset exists or not
    if name not in config.EUKARYOTE_DATASET:
        raise ValueError(f"'{name}' dataset not found.")

    # Dataset cache local directory
    if cache_dir is None:
        package_name = __name__.split(".")[0]
        cache_base_dir = Path.home() / ".cache" / package_name
        cache_dir = cache_base_dir / "eukaryote" / name
        os.makedirs(cache_dir, exist_ok=True)
    else:
        cache_dir = Path(cache_dir)

    # Download & cache dataset
    eukaryote_files: list[Path] = []
    chr_link_list: list[ChrLink] = []
    for filename in config.EUKARYOTE_DATASET[name]:
        file_url = config.GITHUB_DATA_URL + f"eukaryote/{name}/{filename}"
        file_path = cache_dir / filename
        if overwrite_cache or not file_path.exists():
            urlretrieve(file_url, file_path)
        if str(file_path).endswith("link.tsv"):
            chr_link_list = ChrLink.load(file_path)
        else:
            eukaryote_files.append(file_path)

    return *eukaryote_files, chr_link_list


def fetch_genbank_by_accid(
    accid: str,
    gbk_outfile: str | Path | None = None,
    email: str | None = None,
) -> TextIOWrapper:
    """Fetch genbank text by 'Accession ID'

    Parameters
    ----------
    accid : str
        Accession ID
    gbk_outfile : str | Path | None, optional
        If file path is set, write fetch data to file
    email : str | None, optional
        Email address to notify download limitation (Required for bulk download)

    Returns
    -------
    TextIOWrapper
        Genbank data

    Examples
    --------
    >>> gbk_fetch_data = fetch_genbank_by_accid("JX128258.1")
    >>> gbk = Genbank(gbk_fetch_data)
    """
    Entrez.email = "" if email is None else email
    gbk_fetch_data: TextIOWrapper = Entrez.efetch(
        db="nucleotide",
        id=accid,
        rettype="gbwithparts",
        retmode="text",
    )
    if gbk_outfile is not None:
        gbk_text = gbk_fetch_data.read()
        with open(gbk_outfile, "w") as f:
            f.write(gbk_text)
        gbk_fetch_data = StringIO(gbk_text)

    return gbk_fetch_data


def get_label_params_by_rad(
    rad: float,
    orientation: str,
    outer: bool = True,
    only_rotation: bool = False,
):
    """Get proper label parameters by radian position

    Parameters
    ----------
    rad : float
        Radian coordinate
    orientation : str
        Label orientation (`horizontal` or `vertical`)
    outer : bool, optional
        If True, show on `outer` style. Else, show on `inner` style.
    only_rotation : bool, optional
        If True, Only return rotation parameter

    Returns
    -------
    dict_param : dict[str, Any]
        `va`, `ha`, `rotation`, `rotation_mode` dict
    """
    # Get position degree & location info
    deg = math.degrees(rad)
    is_lower_loc = True if -270 <= deg < -90 or 90 <= deg < 270 else False
    is_right_loc = True if -360 <= deg < -180 or 0 <= deg < 180 else False
    # Get parameters
    if orientation == "horizontal":
        rotation = 180 - deg if is_lower_loc else -deg
        ha = "center"
        if outer:
            va = "top" if is_lower_loc else "bottom"
        else:
            va = "bottom" if is_lower_loc else "top"
    elif orientation == "vertical":
        rotation = 90 - deg if is_right_loc else 270 - deg
        va = "center_baseline"
        if outer:
            ha = "left" if is_right_loc else "right"
        else:
            ha = "right" if is_right_loc else "left"
    else:
        err_msg = f"orientation='{orientation}' is invalid "
        err_msg += "('horizontal' or 'vertical')"
        raise ValueError(err_msg)

    if only_rotation:
        return dict(rotation=rotation)
    else:
        return dict(va=va, ha=ha, rotation=rotation, rotation_mode="anchor")


def set_axis_default_kwargs(**kwargs) -> dict[str, Any]:
    """Set axis default keyword arguments

    Set simple black axis params (`fc="none", ec="black", lw=0.5`) as default.

    Returns
    -------
    kwargs : dict[str, Any]
        Keyword arguments
    """
    if "fc" not in kwargs and "facecolor" not in kwargs:
        kwargs.update({"fc": "none"})
    if "ec" not in kwargs and "edgecolor" not in kwargs:
        kwargs.update({"ec": "black"})
    if "lw" not in kwargs and "linewidth" not in kwargs:
        kwargs.update({"lw": 0.5})
    return kwargs


class ColorCycler:
    """Color Cycler Class"""

    counter = 0
    cmap: Colormap = get_cmap("tab10")

    def __new__(cls, n: int | None = None) -> str:
        """Get hexcolor cyclically from cmap by counter or user specified number

        `ColorCycler()` works same as `ColorCycler.get_color()`

        Parameters
        ----------
        n : int | None, optional
            Number for color cycle. If None, counter class variable is used.

        Returns
        -------
        hexcolor : str
            Cyclic hexcolor string
        """
        return cls.get_color(n)

    @classmethod
    def reset_cycle(cls) -> None:
        """Reset cycle counter"""
        cls.counter = 0

    @classmethod
    def set_cmap(cls, name: str) -> None:
        """Set colormap (Default: `tab10`)"""
        cls.cmap = get_cmap(name)
        cls.counter = 0

    @classmethod
    def get_color(cls, n: int | None = None) -> str:
        """Get hexcolor cyclically from cmap by counter or user specified number

        Parameters
        ----------
        n : int | None, optional
            Number for color cycle. If None, counter class variable is used.

        Returns
        -------
        hexcolor : str
            Cyclic hexcolor string
        """
        if n is None:
            n = cls.counter
            cls.counter += 1
        return to_hex(cls.cmap(n % cls.cmap.N), keep_alpha=True)

    @classmethod
    def get_color_list(cls, n: int | None = None) -> list[str]:
        """Get hexcolor list of colormap

        Parameters
        ----------
        n : int | None, optional
            If n is None, all(=cmap.N) hexcolors are extracted from colormap.
            If n is specified, hexcolors are extracted from n equally divided colormap.

        Returns
        -------
        hexcolor_list : list[str]
            Hexcolor list
        """
        if n is None:
            cmap_idx_list = list(range(0, cls.cmap.N))
        elif n > 0:
            cmap_idx_list = [int(i) for i in np.linspace(0, cls.cmap.N, n)]
        else:
            raise ValueError(f"n={n} is invalid number (Must be 'n > 0').")

        return [to_hex(cls.cmap(i), keep_alpha=True) for i in cmap_idx_list]


@dataclass
class ChrLink:
    """Chromosome Link DataClass"""

    query_chr: str
    query_start: int
    query_end: int
    ref_chr: str
    ref_start: int
    ref_end: int

    @staticmethod
    def load(chr_link_file: str | Path) -> list[ChrLink]:
        """Load chromosome link file

        Parameters
        ----------
        chr_link_file : str | Path
            Chromosome link file

        Returns
        -------
        chr_link_list : list[ChrLink]
            Chromosome link list
        """
        chr_link_list = []
        with open(chr_link_file) as f:
            reader = csv.reader(f, delimiter="\t")
            for row in reader:
                qchr, qstart, qend = row[0], int(row[1]), int(row[2])
                rchr, rstart, rend = row[3], int(row[4]), int(row[5])
                chr_link_list.append(ChrLink(qchr, qstart, qend, rchr, rstart, rend))
        return chr_link_list
