import evomatic as evo

evolver = evo.Evolver(
    **{
        "population_size": 50,
        "targets": {"maximise": ["density"], "minimise": ["mass"]},
        "min_iterations": 50,
    }
)

history = evolver.evolve()
print(history["alloys"])

evolver.output_results()
