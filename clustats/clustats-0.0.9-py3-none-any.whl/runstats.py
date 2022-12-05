from pathlib import Path
from typing import List
from belinda import *
from itertools import tee
import polars as pl
from structlog import get_logger
import typer

CUT_SIZE = "connectivity"


def high_degree_singletons(g, c):
    nodes = g.nodes(c)
    below = nodes.with_column(
        pl.col("labels").arr.lengths().alias("num_assigned")
    ).filter(pl.col("degree") > pl.col("degree").quantile(0.95))
    above = below.filter(pl.col("num_assigned") == 0)
    return len(above) / len(below)


def multi_range(expr, numvalues):
    if numvalues == 3:
        exprs = [
            expr.quantile(0),
            expr.quantile(0.5),
            expr.quantile(1),
        ]
    else:
        exprs = [
            expr.quantile(0),
            expr.quantile(0.25),
            expr.quantile(0.5),
            expr.quantile(0.75),
            expr.quantile(1),
        ]
    return pl.concat_str(
        exprs,
        sep=" - ",
    )


def basic_statistics(g, c, overlap=False, numvalues=3):
    high_deg_singletons = high_degree_singletons(g, c)
    to_compute = [
        pl.col("n").count().alias("# Clusters"),
        g.node_coverage(overlap).alias("Node cov."),
        g.edge_coverage(overlap).alias("Edge cov."),
        pl.lit(high_deg_singletons).alias("High deg. singletons"),
        multi_range(pl.col("n"), numvalues=numvalues).alias("Cluster Size"),
        multi_range(pl.col("mcd"), numvalues=numvalues).alias("MCD"),
    ]
    if CUT_SIZE in c.columns:
        to_compute.append(
            multi_range(pl.col(CUT_SIZE), numvalues=numvalues).alias("Cut Size"),
        )
    return c.select(to_compute)


def load_clustering(g, c):
    if Path(c).suffix == ".json":
        return read_json(g, c, mode=SingletonMode.Ignore)
    else:
        return read_assignment(g, c, mode=SingletonMode.Ignore)


def entry_point():
    typer.run(main)


if __name__ == "__main__":
    entry_point()


def chunker(seq, size):
    return (seq[pos : pos + size] for pos in range(0, len(seq), size))


def main(
    label_pairs: List[str],
    graph: str = typer.Option(..., "--graph", "-g"),
    output: str = typer.Option(..., "--output", "-o"),
    numvalues: int = typer.Option(3, "--numvalues", "-n"),
):
    logger = get_logger()
    g = Graph(graph)
    logger.info("Loaded graph", n=g.n, m=g.m)
    dfs = []
    size_lb = 0
    for l, p in chunker(label_pairs, 2):
        overlap = False
        if ":" in l:
            l = l.split(":")[0]
            overlap = True
        if "." in l:
            l, size_lb = l.split(".")
            size_lb = int(size_lb)
        c = load_clustering(g, p)
        size_lb_bounds = [0]
        if size_lb > 0:
            size_lb_bounds.append(size_lb)
        for s in size_lb_bounds:
            stats = basic_statistics(g, c.filter(pl.col('n') > s), overlap, numvalues)
            stats = stats.with_column(pl.lit(l + (f">= {s}" if s > 0 else "")).alias("Setting"))
            dfs.append(stats)
    df = pl.concat(dfs)
    logger.info("Computed statistics", num_variants=len(df))
    df.write_csv(output)
