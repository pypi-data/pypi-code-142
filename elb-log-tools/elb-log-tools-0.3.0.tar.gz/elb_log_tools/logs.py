#!/usr/bin/env python3
"""
Stream ELB logs for a given date range to stdout.

Does not currently support Gzipped logs.
"""
# Copyright 2022 Pymetrics, Inc.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import argparse
import os
import sys
from datetime import date, datetime, timedelta
from typing import Generator

import boto3

DATETIME_FMT = "%Y-%m-%d"
DEFAULT_REGION = "us-east-1"
DEFAULT_INPUT_ENCODING = "cp437"  # after much trial and error this seems to work best
DEFAULT_OUTPUT_ENCODING = "utf_8"
DEFAULT_BUCKET_ENV_VAR = "ELB_LOG_BUCKET"


def date_str(s: str) -> date:
    try:
        return datetime.strptime(s, DATETIME_FMT).date()
    except ValueError:
        raise argparse.ArgumentTypeError(f"Not a valid date string: {s}")


def get_account_id():
    """
    Returns the AWS account ID for the current user.
    """
    return boto3.client("sts").get_caller_identity().get("Account")


def get_path(account_id: str, region: str, d: date):
    return f"AWSLogs/{account_id}/elasticloadbalancing/{region}/{d.year}/{d.month:02}/{d.day:02}"


def emit_dates(start_date: date, num_days: int) -> Generator[date, None, None]:
    for i in range(num_days):
        yield start_date
        start_date += timedelta(days=1)


def list_log_file_keys(
    client, bucket, prefix="", token=None
) -> Generator[str, None, None]:
    """
    List all logs for the given date, optionally filtered by the given prefix.
    """
    kwargs = {"Bucket": bucket, "Prefix": prefix}
    if token:
        kwargs["ContinuationToken"] = token
    resp = client.list_objects_v2(**kwargs)
    for log in resp.get("Contents", []):
        yield log["Key"]
    token = resp.get("ContinuationToken", None)
    if token:
        yield from list_log_file_keys(client, bucket=bucket, prefix=prefix, token=token)


def read_log_key(client, bucket: str, key: str) -> Generator[bytes, None, None]:
    """
    Yields lines from the given log key.
    """
    resp = client.get_object(Bucket=bucket, Key=key)
    yield from resp["Body"].iter_lines()


def emit_lines(
    start_date, num_days, bucket, region=DEFAULT_REGION
) -> Generator[bytes, None, None]:
    client = boto3.client("s3")
    account_id = get_account_id()
    for d in emit_dates(start_date, num_days):
        prefix = get_path(account_id, region, d)
        for log in list_log_file_keys(client, bucket=bucket, prefix=prefix):
            yield from read_log_key(client, bucket, log)


def elb_logs(opts):

    for line in emit_lines(
        start_date=opts.start_date,
        num_days=opts.num_days,
        bucket=opts.bucket,
        region=opts.region,
    ):
        try:
            decoded = line.decode(opts.input_encoding)
            sys.stdout.buffer.write(decoded.encode(opts.output_encoding))
            sys.stdout.write("\n")
            sys.stdout.flush()
        except UnicodeDecodeError:
            sys.stderr.write("Error decoding line: ")
            sys.stderr.buffer.write(line)
            sys.stderr.write("\n")


def detect_encoding(opts):
    from collections import Counter

    try_encodings = (
        "cp037",
        "cp437",
        "cp1252",
        "utf_32",
        "utf_32_be",
        "utf_32_le",
        "utf_16",
        "utf_16_be",
        "utf_16_le",
        "utf_7",
        "utf_8",
        "utf_8_sig",
    )
    success_counts = Counter()
    fail_counts = Counter()

    for i, line in enumerate(
        emit_lines(
            start_date=opts.start_date,
            num_days=opts.num_days,
            bucket=opts.bucket,
            region=opts.region,
        )
    ):
        try:
            decoded = line.decode("utf8")
        except UnicodeDecodeError:
            sys.stdout.write("\nUnicodeDecodeError: ")
            sys.stdout.buffer.write(line)
            sys.stdout.write("\n")
            for enc in try_encodings:
                try:
                    decoded = line.decode(enc)
                    print(f"Decoded to {enc}: {decoded}")
                    success_counts.update([enc])
                except Exception:
                    fail_counts.update([enc])
                print(f"Success counts: {success_counts}")
                print(f"Fail counts: {fail_counts}")

    print(f"Most success: {success_counts.most_common(n=3)}")
    print(f"Most failed: {fail_counts.most_common(n=3)}")


def env_arg(key):
    value = os.environ.get(key, None)
    if value:
        return {"default": value}
    else:
        return {"required": True}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-s",
        "--start-date",
        help="Start from this time. Format YYYY-MM-DD. Defaults to the current date.",
        type=date_str,
        default=date.today(),
    )
    parser.add_argument(
        "-n", "--num-days", help="Number of days to emit.", type=int, default=1
    )
    parser.add_argument(
        "-b", "--bucket", help="Log bucket name", **env_arg(DEFAULT_BUCKET_ENV_VAR)
    )
    parser.add_argument("-r", "--region", default=DEFAULT_REGION)
    parser.add_argument(
        "--input-encoding",
        help="Decode incoming log entries using this encoding",
        default=DEFAULT_INPUT_ENCODING,
    )
    parser.add_argument(
        "--output-encoding",
        help="Encode output using this encoding",
        default=DEFAULT_OUTPUT_ENCODING,
    )
    parser.add_argument(
        "--detect-encoding",
        help="Attempt to detect the character encoding "
        "of the input stream. Does not emit lines in this mode.",
        default=False,
        action="store_true",
    )

    args = parser.parse_args()

    try:
        if args.detect_encoding:
            detect_encoding(args)
        else:
            elb_logs(args)
    except BrokenPipeError:
        # Happens when piped into e.g. head. Close stderr
        # to avoid an "Exception ignored..." message
        sys.stderr.close()
        sys.exit(0)


if __name__ == "__main__":
    main()
