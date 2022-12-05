import typer
import leidenalg as la
from igraph import Graph
from enum import Enum
from structlog import get_logger

class Quality(str, Enum):
    cpm = "cpm"
    modularity = "mod"

def main(
    input: str = typer.Option(..., "--input", "-i"),
    quality: Quality = typer.Option(Quality.cpm, "--quality", "-q"),
    resolution: float = typer.Option(1.0, "--gamma", "-r"),
    output: str = typer.Option(..., "--output", "-o"),
):
    """Run Leiden algorithm on an input edgelist file."""
    logger = get_logger()
    g = Graph.Load(input, format='edgelist', directed=False)
    logger.info("loaded graph", n=g.vcount(), m=g.ecount())
    if resolution != 1.0 and quality == Quality.modularity:
        logger.warn("resolution parameter is ignored for modularity")
    if quality == Quality.cpm:
        partition = la.find_partition(
            g, la.CPMVertexPartition, resolution_parameter=resolution
        )
    else:
        partition = la.find_partition(
            g, la.ModularityVertexPartition
        )
    
    logger.info("clustering finished, writing to file")
    with open(output, "w+") as fh:
        for n, cid in enumerate(partition.membership):
            fh.write(f"{n}\t{cid}\n")
    logger.info("wrote output", output=output, n_clusters=cid+1)

def entry_point():
    typer.run(main)

if __name__ == '__main__':
    entry_point()