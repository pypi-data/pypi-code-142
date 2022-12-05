import polars as pl
import pandas as pd
import typer


def percentage_formatter(x):
    return f"{x:.2%}"


def main(
    table_path: str,
):
    df = pl.read_csv(table_path)
    ord = {
        e: i
        for i, e in enumerate(
            [
                "Setting",
                "# Clusters",
                "Node cov.",
                "Edge cov.",
                "High deg. singletons",
                "Cluster Size",
                "MCD",
                "Connectivity",
                "Cut Size",
            ]
        )
    }
    df = df.select(sorted(df.columns, key=lambda c: ord.get(c, 99)))
    print(
        df.to_pandas().to_latex(
            formatters={
                "Node cov.": percentage_formatter,
                "Edge cov.": percentage_formatter,
                "High deg. singletons": percentage_formatter,
            },
            index=False,
        )
    )


def entry_point():
    typer.run(main)


if __name__ == "__main__":
    entry_point()
