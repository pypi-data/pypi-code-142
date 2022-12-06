from pathlib import Path

import pytest

from pycirclize import Circos
from pycirclize.utils import load_eukaryote_example_dataset


def test_circos_init(tmp_path: Path):
    """Test circos initialization"""
    circos = Circos({"A": 10, "B": 20, "C": 15})
    assert [s.name for s in circos.sectors] == ["A", "B", "C"]


@pytest.mark.parametrize(
    "start, end",
    [
        (-10, 360),  # End - Start > 360
        (0, -90),  # Start > End
        (-400, -200),  # Start < -360
        (200, 400),  # End > 360
    ],
)
def test_circos_init_range_error(start: float, end: float):
    """Test circos initialization range error"""
    with pytest.raises(ValueError):
        Circos({s: 10 for s in "ABC"}, start=start, end=end)


def test_get_sector():
    """Test `get_sector()`"""
    sectors = {"A": 10, "B": 20, "C": 15}
    circos = Circos(sectors)
    # Case1: Successfully get sector
    for sector_name in sectors.keys():
        circos.get_sector(sector_name)
    # Case2: Failed to get sector
    with pytest.raises(ValueError):
        circos.get_sector("error")


def test_cytoband_plot(tmp_path: Path):
    """Test hg38 cytoband plot"""
    # Add tracks for cytoband plot
    chr_bed_file, cytoband_file, _ = load_eukaryote_example_dataset("hg38")
    circos = Circos.initialize_from_bed(chr_bed_file, space=2)
    circos.add_cytoband_tracks((95, 100), cytoband_file)

    # Plot and check fig file exists
    result_fig_file = tmp_path / "test.png"
    circos.savefig(result_fig_file)
    assert result_fig_file.exists()
