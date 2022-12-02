import os
import typing

import httpx
import typer

from neosctl import util
from neosctl.auth import ensure_login
from neosctl.util import process_response


app = typer.Typer()
secret_app = typer.Typer()
app.add_typer(secret_app, name="secret", help="Manage secrets for a spark job.")


def spark_url(name: str, gateway_api_url: str) -> str:
    return "{}/spark/{}".format(gateway_api_url.rstrip("/"), name)


def secret_url(name: str, gateway_api_url: str) -> str:
    return "{}/secret/{}".format(gateway_api_url.rstrip("/"), name)


@app.command()
def add_job(
    ctx: typer.Context,
    product_name: str = typer.Argument(os.getenv("NEOSCTL_PRODUCT", ...), help="Data Product name"),
    job_filepath: str = typer.Option(..., "--job-filepath", "-f"),
):
    """Assign a spark job.

    Assign and configure a spark job for a data product. This will result in a
    one off run of the spark job.
    """
    @ensure_login
    def _request(ctx: typer.Context, f: typing.IO) -> httpx.Response:
        return util.post(
            ctx,
            spark_url(product_name, ctx.obj.gateway_api_url),
            files={"spark_file": f},
        )

    fp = util.get_file_location(job_filepath)

    with fp.open("rb") as f:
        r = _request(ctx, f)

    process_response(r)


@app.command()
def job_status(
    ctx: typer.Context,
    product_name: str = typer.Argument(os.getenv("NEOSCTL_PRODUCT", ...), help="Data Product name"),
):
    """Get current status of a spark job.
    """
    @ensure_login
    def _request(ctx: typer.Context) -> httpx.Response:
        return util.get(
            ctx,
            "{spark_url}".format(spark_url=spark_url(product_name, ctx.obj.gateway_api_url)),
        )
    r = _request(ctx)

    process_response(r)


def render_logs(payload: typing.Dict):
    return "\n".join(payload["logs"])


@app.command()
def job_logs(
    ctx: typer.Context,
    product_name: str = typer.Argument(os.getenv("NEOSCTL_PRODUCT", ...), help="Data Product name"),
):
    """Get logs for a spark job.
    """
    @ensure_login
    def _request(ctx: typer.Context) -> httpx.Response:
        return util.get(
            ctx,
            "{spark_url}/log".format(spark_url=spark_url(product_name, ctx.obj.gateway_api_url)),
        )
    r = _request(ctx)

    process_response(r, render_logs)


@app.command()
def update_job(
    ctx: typer.Context,
    product_name: str = typer.Argument(os.getenv("NEOSCTL_PRODUCT", ...), help="Data Product name"),
    job_filepath: str = typer.Option(None, "--job-filepath", "-f"),
):
    """Update an assigned spark job.

    Update the assigned spark job file and/or the spark job configuration values.
    """
    @ensure_login
    def _request(
        ctx: typer.Context,
        f: typing.Optional[typing.IO],
    ) -> httpx.Response:
        files = {"spark_file": f} if f else {}

        return util.put(
            ctx,
            spark_url(product_name, ctx.obj.gateway_api_url),
            files=files,
        )

    if job_filepath:
        fp = util.get_file_location(job_filepath)

        with fp.open("rb") as f:
            r = _request(ctx, f)
    else:
        r = _request(ctx, None)

    process_response(r)


@app.command()
def remove_job(
    ctx: typer.Context,
    product_name: str = typer.Argument(os.getenv("NEOSCTL_PRODUCT", ...), help="Data Product name"),
):
    """Remove assigned spark job.
    """
    @ensure_login
    def _request(ctx: typer.Context) -> httpx.Response:
        return util.delete(
            ctx,
            spark_url(product_name, ctx.obj.gateway_api_url),
        )

    r = _request(ctx)
    process_response(r)


@app.command()
def trigger_job(
    ctx: typer.Context,
    product_name: str = typer.Argument(os.getenv("NEOSCTL_PRODUCT", ...), help="Data Product name"),
):
    """Trigger assigned spark job.

    Trigger an additional run of a spark job.
    """
    @ensure_login
    def _request(ctx: typer.Context) -> httpx.Response:
        return util.post(
            ctx,
            "{spark_url}/trigger".format(spark_url=spark_url(product_name, ctx.obj.gateway_api_url)),
        )

    r = _request(ctx)
    process_response(r)


@app.command()
def csv_job(
    ctx: typer.Context,
    product_name: str = typer.Argument(os.getenv("NEOSCTL_PRODUCT", ...), help="Data Product name"),
    delimiter: str = typer.Option(",", "--delimiter", "-d", help="csv delimiter"),
    quotechar: typing.Optional[str] = typer.Option(None, "--quote-char", "-q", help="csv quote char"),
    job_filepath: str = typer.Option(..., "--job-filepath", "-f"),
):
    """Ingest a csv file into a data product.

    Upload a csv file for processing into a data product.
    """
    @ensure_login
    def _request(ctx: typer.Context, f: typing.IO) -> httpx.Response:
        params = {
            "delimiter": delimiter,
        }

        if quotechar is not None:
            params["quotechar"] = quotechar

        return util.post(
            ctx,
            "{spark_url}/csv".format(spark_url=spark_url(product_name, ctx.obj.gateway_api_url)),
            params=params,
            files={"csv_file": f},
        )

    fp = util.get_file_location(job_filepath)

    with fp.open("rb") as f:
        r = _request(ctx, f)

    process_response(r)


@app.command()
def schedule_job(
    ctx: typer.Context,
    product_name: str = typer.Argument(os.getenv("NEOSCTL_PRODUCT", ...), help="Data Product name"),
    schedule: str = typer.Option(..., "--schedule", "-s", help='Schedule in crontab format (e.g. "* * * * *")'),
):
    """Schedule an assigned spark job.

    Schedule a spark job once it is configured correctly to run periodically.
    """
    @ensure_login
    def _request(ctx: typer.Context) -> httpx.Response:
        return util.post(
            ctx,
            "{spark_url}/scheduled".format(spark_url=spark_url(product_name, ctx.obj.gateway_api_url)),
            json={
                "cron_expression": schedule,
            },
        )

    r = _request(ctx)
    process_response(r)


@secret_app.command()
def add(
    ctx: typer.Context,
    product_name: str = typer.Argument(os.getenv("NEOSCTL_PRODUCT", ...), help="Data Product name"),
    secrets: typing.List[str] = typer.Option(..., "--secret", "-s", help="Secret in the form key:value"),
):
    """Add a set of secrets for a spark job.
    """
    @ensure_login
    def _request(ctx: typer.Context, payload: typing.Dict) -> httpx.Response:
        return util.post(
            ctx,
            secret_url(product_name, ctx.obj.gateway_api_url),
            json=payload,
        )
    payload = {"data": {}}
    for s in secrets:
        name, value = s.split(":")
        payload["data"][name] = value

    r = _request(ctx, payload)

    process_response(r)


@secret_app.command()
def update(
    ctx: typer.Context,
    product_name: str = typer.Argument(os.getenv("NEOSCTL_PRODUCT", ...), help="Data Product name"),
    secrets: typing.List[str] = typer.Option(..., "--secret", "-s", help="Secret in the form key:value"),
):
    """Update existing secrets.

    This will overwrite existing keys, and add new keys, any keys that already
    exist but aren't provided will remain.
    """
    @ensure_login
    def _request(ctx: typer.Context, payload: typing.Dict) -> httpx.Response:
        return util.patch(
            ctx,
            secret_url(product_name, ctx.obj.gateway_api_url),
            json=payload,
        )
    payload = {"data": {}}
    for s in secrets:
        name, value = s.split(":")
        payload["data"][name] = value

    r = _request(ctx, payload)

    process_response(r)


@secret_app.command()
def remove(
    ctx: typer.Context,
    product_name: str = typer.Argument(os.getenv("NEOSCTL_PRODUCT", ...), help="Data Product name"),
):
    """Remove secret.
    """
    @ensure_login
    def _request(ctx: typer.Context) -> httpx.Response:
        return util.delete(
            ctx,
            secret_url(product_name, ctx.obj.gateway_api_url),
        )

    r = _request(ctx)

    process_response(r)


@secret_app.command()
def remove_key(
    ctx: typer.Context,
    product_name: str = typer.Argument(os.getenv("NEOSCTL_PRODUCT", ...), help="Data Product name"),
    keys: typing.List[str] = typer.Option(..., "--key", "-k", help="Key name you wish to remove from secret"),
):
    """Remove a set of keys from a secret.
    """
    @ensure_login
    def _request(ctx: typer.Context) -> httpx.Response:
        return util.delete(
            ctx,
            "{secret_url}/key".format(secret_url=secret_url(product_name, ctx.obj.gateway_api_url)),
            json={"keys": keys},
        )

    r = _request(ctx)

    process_response(r)


@secret_app.command()
def get(
    ctx: typer.Context,
    product_name: str = typer.Argument(os.getenv("NEOSCTL_PRODUCT", ...), help="Data Product name"),
):
    """Get existing secret keys.
    """
    @ensure_login
    def _request(ctx: typer.Context) -> httpx.Response:
        return util.get(
            ctx,
            secret_url(product_name, ctx.obj.gateway_api_url),
        )

    r = _request(ctx)

    process_response(r)
