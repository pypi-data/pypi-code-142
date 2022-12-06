import math
from pathlib import Path

import pandas as pd
import pytest

from pycirclize.parser import Matrix


@pytest.fixture
def csv_matrix_file(testdata_dir: Path) -> Path:
    """CSV matrix file fixture"""
    return testdata_dir / "matrix" / "matrix.csv"


@pytest.fixture
def tsv_matrix_file(testdata_dir: Path) -> Path:
    """TSV matrix file fixture"""
    return testdata_dir / "matrix" / "matrix.tsv"


def test_load_dataframe_matrix():
    """Test load panda dataframe matrix"""
    # Pandas matrix dataframe
    matrix_data = [
        [4, 14, 13, 17, 5, 2],
        [7, 1, 6, 8, 12, 15],
        [9, 10, 3, 16, 11, 18],
    ]
    row_names = ["S1", "S2", "S3"]
    col_names = ["E1", "E2", "E3", "E4", "E5", "E6"]
    matrix_df = pd.DataFrame(matrix_data, index=row_names, columns=col_names)

    # Load pandas matrix dataframe
    matrix = Matrix(matrix_df)

    # Test row & column names
    assert matrix.all_names == row_names + col_names
    assert matrix.row_names == row_names
    assert matrix.col_names == col_names

    # Only test successfully call function
    matrix.to_sectors()
    matrix.to_links()


def test_load_tsv_matrix(tsv_matrix_file: Path):
    """Test load tsv matrix"""
    # Load tsv format matrix file
    matrix = Matrix(tsv_matrix_file)

    # Test row & column names
    row_names = ["S1", "S2", "S3"]
    col_names = ["E1", "E2", "E3", "E4", "E5", "E6"]
    assert matrix.all_names == row_names + col_names
    assert matrix.row_names == row_names
    assert matrix.col_names == col_names

    # Only test successfully call function
    matrix.to_sectors()
    matrix.to_links()


def test_load_csv_matrix(csv_matrix_file: Path):
    """Test load csv matrix"""
    # Load csv format matrix file
    matrix = Matrix(csv_matrix_file, delimiter=",")

    # Test row & column names
    row_names = ["S1", "S2", "S3"]
    col_names = ["E1", "E2", "E3", "E4", "E5", "E6"]
    assert matrix.all_names == row_names + col_names
    assert matrix.row_names == row_names
    assert matrix.col_names == col_names

    # Only test successfully call function
    matrix.to_sectors()
    matrix.to_links()
