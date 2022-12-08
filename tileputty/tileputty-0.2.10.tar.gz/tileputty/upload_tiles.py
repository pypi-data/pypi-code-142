import logging
import multiprocessing
import os
import sys
from logging import Logger
from typing import Iterator

import boto3
from botocore.config import Config
from parallelpipe import Stage
from typer import Argument, Option, run

LOGGER: Logger = logging.getLogger("tileputty")
CORES: int = int(os.environ.get("CORES", multiprocessing.cpu_count()))

# File headers for different formats
MVT_META = {
    "ContentType": "application/x-protobuf",
    "ContentEncoding": "gzip",
    "CacheControl": "max-age=31536000",  # 1 yr
}
PNG_META = {"ContentType": "image/png", "CacheControl": "max-age=31536000"}  # 1 yr
JPG_META = {"ContentType": "image/jpeg", "CacheControl": "max-age=31536000"}  # 1 yr
JSON_META = {"ContentType": "application/json"}

ARGS = {
    ".pbf": MVT_META,
    ".mvt": MVT_META,
    ".png": PNG_META,
    ".jpg": JPG_META,
    ".json": JSON_META,
}


def main(
    tile_cache: str = Argument(..., help="Path to local tile cache"),
    dataset: str = Option(..., help="Dataset Name"),
    version: str = Option(..., help="Dataset Version ID"),
    bucket: str = Option("gfw-tiles", help="AWS Bucket"),
    implementation: str = Option(..., help="Tile Cache Implementation"),
    cores: int = Option(..., help="Number or processes to use to upload tiles"),
) -> None:
    """Upload a local tile cache to S3."""

    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(
        logging.Formatter(
            fmt="%(asctime)s %(levelname)-4s %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
        )
    )
    LOGGER.addHandler(handler)

    upload_tiles(
        tile_cache=tile_cache,
        bucket=bucket,
        dataset=dataset,
        version=version,
        implementation=implementation,
        cores=cores,
    )


def upload_tiles(
    tile_cache: str,
    dataset: str,
    version: str,
    bucket: str = "gfw-tiles",
    implementation: str = "default",
    cores: int = CORES,
) -> None:
    """Upload a local tile cache to S3."""

    LOGGER.info(
        f"Upload tile cache to {dataset}/{version}/{implementation} using {cores} processes"
    )

    # pipe files
    pipe = get_tiles(tile_cache) | Stage(
        copy_tiles, tile_cache, bucket, dataset, version, implementation
    ).setup(workers=cores)

    # collect results
    for output in pipe.results():
        LOGGER.debug(output)


def get_tiles(tile_cache: str) -> Iterator[str]:
    """Collect all files in tile cache."""
    for root, dirs, files in os.walk(tile_cache):
        for f in files:
            yield os.path.join(root, f).replace("\\", "/")


def copy_tiles(
    files, tile_cache, bucket, dataset, version, implementation
) -> Iterator[str]:
    """Upload files to S3 and update file header."""

    config = Config(retries={"max_attempts": 10, "mode": "standard"})
    endpoint_url = os.environ.get("ENDPOINT_URL", None)
    s3 = boto3.client("s3", config=config, endpoint_url=endpoint_url)

    for f in files:

        file_name = os.path.basename(f)
        prefix = os.path.dirname(f).replace(tile_cache + "/", "")
        basename, extension = os.path.splitext(file_name)

        try:
            args = ARGS[extension]
        except KeyError:
            args = {}

        s3_path = f"{dataset}/{version}/{implementation}/{prefix}/{file_name}"
        s3.upload_file(f, bucket, s3_path, ExtraArgs=args)
        yield s3_path


def cli():
    run(main)
