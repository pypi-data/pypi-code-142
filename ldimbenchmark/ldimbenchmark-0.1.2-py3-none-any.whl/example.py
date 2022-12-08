from typing import Dict, Any

import numpy as np

from timeeval import (
    TimeEval,
    DatasetManager,
    Algorithm,
    TrainingType,
    InputDimensionality,
)
from timeeval.adapters import FunctionAdapter
from timeeval.constants import HPI_CLUSTER
from timeeval.params import FixedParameters


# Load presupplied dataset
dataset = DatasetLoader(path="./loaded-datasets").load(DATASETS.BATTLEDIM)

# Custom Dataset
# Datases are lazy evaluated, so they are not loaded until they are needed
dataset = Dataset(
    path="data",  # Path to the dataset (or where to download it))
)

loadedDataset = dataset.load()  # => LoadedDataset


# DatasetDerivator is a helper class to create derivated datasets from an existing one
datasets = DatasetDerivator(dataset=dataset, outPath="./derivations").derive(
    "noise", [0.1, 0.2, 0.3]
)


DatasetAnalyzer(outFolder="./analysis-results").analyze(datasets)


local_methods = [YourCustomLDIMMethod()]

configuration = {"hyperparameters": {}}


benchmark = (
    LDIMBenchmark(configuration, datasets)
    .add_local_methods(methods)
    .add_docker_methods(methods)
)

# execute benchmark
benchmark.run(
    # parallel=True,
    # resultsDir="./benchmark-results",
)

# execute complexity analysis
benchmark.run_complexity_analysis()
# > datasets are ignored... (as well as hyperparameters)


benchmark.evaluate(
    # evaluationDir="./evaluation-results",
)  # Returns printable evaluation results

# or

LDIMBenchmark.evaluate(
    # resultsDir="./benchmark-results", => Optional
    # evaluationDir="./evaluation-results",
)


# Load dataset metadata
dm = DatasetManager(
    HPI_CLUSTER.akita_dataset_paths[HPI_CLUSTER.BENCHMARK], create_if_missing=False
)

# Define algorithm
def my_algorithm(data: np.ndarray, args: Dict[str, Any]) -> np.ndarray:
    score_value = args.get("score_value", 0)
    return np.full_like(data, fill_value=score_value)


# Select datasets and algorithms
datasets = dm.select(collection="NAB")
datasets = datasets[-1:]
# Add algorithms to evaluate...
algorithms = [
    Algorithm(
        name="MyAlgorithm",
        main=FunctionAdapter(my_algorithm),
        data_as_file=False,
        training_type=TrainingType.UNSUPERVISED,
        input_dimensionality=InputDimensionality.UNIVARIATE,
        param_config=FixedParameters({"score_value": 1.0}),
    )
]
timeeval = TimeEval(dm, datasets, algorithms)

# execute evaluation
timeeval.run_benchmark()


# retrieve results
print(timeeval.get_results())
