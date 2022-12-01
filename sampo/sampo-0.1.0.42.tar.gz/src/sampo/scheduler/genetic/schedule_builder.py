import math
import random
from operator import attrgetter
from typing import Dict, List, Tuple

import numpy as np
import seaborn as sns
from deap import tools
from matplotlib import pyplot as plt
from pandas import DataFrame

from sampo.schemas.schedule_spec import ScheduleSpec
from sampo.schemas.time_estimator import WorkTimeEstimator
from sampo.scheduler.genetic.converter import convert_schedule_to_chromosome, convert_chromosome_to_schedule
from sampo.scheduler.genetic.operators import init_toolbox, ChromosomeType
from sampo.schemas.contractor import Contractor, WorkerContractorPool
from sampo.schemas.graph import GraphNode, WorkGraph
from sampo.schemas.schedule import ScheduleWorkDict, Schedule
from sampo.utilities.collections import reverse_dictionary


def build_schedule(wg: WorkGraph,
                   contractors: List[Contractor],
                   agents: WorkerContractorPool,
                   population_size: int,
                   generation_number: int,
                   selection_size: int,
                   mutate_order: float,
                   mutate_resources: float,
                   init_schedules: Dict[str, Schedule],
                   rand: random.Random,
                   spec: ScheduleSpec,
                   work_estimator: WorkTimeEstimator = None,
                   show_fitness_graph: bool = False) \
        -> ScheduleWorkDict:
    """
    Genetic algorithm
    Structure of chromosome:
    [[order of job], [numbers of workers types 1 for each job], [numbers of workers types 2], ... ]
    Different mate and mutation for order and for workers
    Generate order of job by prioritization from HEFT and from Topological
    Generate resources from min to max
    Overall initial population is valid
    :param show_fitness_graph:
    :param agents:
    :param work_estimator:
    :param contractors:
    :param wg:
    :param population_size:
    :param generation_number:
    :param selection_size:
    :param mutate_order:
    :param mutate_resources:
    :param rand:
    :param spec: spec for current scheduling
    :param init_schedules:
    :return: scheduler
    """

    if show_fitness_graph:
        fitness_history = list()

    index2node: Dict[int, GraphNode] = {index: node for index, node in enumerate(wg.nodes)}
    work_id2index: Dict[str, int] = {node.id: index for index, node in index2node.items()}
    worker_name2index = {worker_name: index for index, worker_name in enumerate(agents)}
    index2contractor = {ind: contractor.id for ind, contractor in enumerate(contractors)}
    index2contractor_obj = {ind: contractor for ind, contractor in enumerate(contractors)}

    init_chromosomes: Dict[str, ChromosomeType] = \
        {name: convert_schedule_to_chromosome(index2node, work_id2index, worker_name2index,
                                              reverse_dictionary(index2contractor), schedule)
         for name, schedule in init_schedules.items()}

    resources_border = np.zeros((2, len(agents), len(index2node)))
    for work_index, node in index2node.items():
        for req in node.work_unit.worker_reqs:
            worker_index = worker_name2index[req.kind]
            resources_border[0, worker_index, work_index] = req.min_count
            resources_border[1, worker_index, work_index] = \
                min(req.max_count, max(list(map(attrgetter('count'), agents[req.kind].values()))))

    toolbox = init_toolbox(wg, contractors, agents, index2node,
                           work_id2index, worker_name2index, index2contractor,
                           index2contractor_obj, init_chromosomes, mutate_order,
                           mutate_resources, selection_size, rand, spec, work_estimator)
    # save best individuals
    hof = tools.HallOfFame(1, similar=compare_individuals)
    # create population of a given size
    pop = toolbox.population(n=population_size)

    # probability to participate in mutation and crossover for each individual
    cxpb, mutpb = 0.5, 0.5
    mutpb_res, cxpb_res = 0.3, 0.3

    # map to each individual fitness function
    fitness = list(map(toolbox.evaluate, pop))
    for ind, fit in zip(pop, fitness):
        ind.fitness.values = [fit]

    if show_fitness_graph:
        fitness_history.append(sum(fitness) / len(fitness))

    g = 0

    while g < generation_number:
        # print("-- Generation %i --" % g)
        # select individuals of next generation
        offspring = toolbox.select(pop, len(pop))
        # clone selected individuals
        offspring = list(map(toolbox.clone, offspring))

        # operations for ORDER
        # crossover
        # take 2 individuals as input 1 modified individuals
        # take after 1: (1,3,5) and (2,4,6) and get pairs 1,2; 3,4; 5,6
        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if rand.random() < cxpb:
                toolbox.mate(child1[0][0], child2[0][0])
                del child1.fitness.values  # remove previous
                del child2.fitness.values

        # mutation
        # take 1 individuals as input and return 1 individuals as output
        for mutant in offspring:
            if rand.random() < mutpb:
                toolbox.mutate(mutant[0][0])
                del mutant.fitness.values

        # gather all the fitness in one list and print the stats
        # invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        # evaluation for each individual
        # fitness = map(toolbox.evaluate, invalid_ind)
        # for ind, fit in zip(invalid_ind, fitness):
        #     ind.fitness.values = [fit]

        # renewing population
        pop[:] = offspring
        hof.update(pop)

        # operations for RESOURCES
        # mutation
        # select types for mutation
        # numbers of changing types
        number_of_type_for_changing = rand.randint(1, len(worker_name2index) - 1)
        # workers type for changing(+1 means contractor 'resource')
        workers = rand.sample(range(len(worker_name2index) + 1), number_of_type_for_changing)

        # resources mutation
        for worker in workers:
            low = resources_border[0, worker] if worker != len(worker_name2index) else 0
            up = resources_border[1, worker] if worker != len(worker_name2index) else 0
            for mutant in offspring:
                if rand.random() < mutpb_res:
                    toolbox.mutate_resources(mutant[0], low=low, up=up, type_of_worker=worker)
                    del mutant.fitness.values

        # for the crossover, we use those types that did not participate in the mutation(+1 means contractor 'resource')
        workers_for_mate = list(set(list(range(len(worker_name2index) + 1))) - set(workers))
        # crossover
        for ind_worker in range(len(workers_for_mate)):
            # take 2 individuals as input 1 modified individuals
            for child1, child2 in zip(offspring[::2], offspring[1::2]):
                if rand.random() < cxpb_res:
                    toolbox.mate_resources(child1[0][1][workers_for_mate[ind_worker]],
                                           child2[0][1][workers_for_mate[ind_worker]])
                    del child1.fitness.values  # remove prev
                    del child2.fitness.values

        # Gather all the fitness in one list and print the stats
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        # for each individual - evaluation
        fitness = map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitness):
            ind.fitness.values = [fit]

        if show_fitness_graph:
            _ftn = [f for f in fitness if not math.isinf(f)]
            if len(_ftn) > 0:
                fitness_history.append(sum(_ftn) / len(_ftn))

        # renewing population
        pop[:] = offspring
        hof.update(pop)

        # best = hof[0]
        # fits = [ind.fitness.values[0] for ind in pop]
        # evaluation = chromosome_evaluation(best, index2node, resources_border, work_id2index, worker_name2index,
        #                                   parent2inseparable_son, agents)
        # print("fits: ", fits)
        # print(evaluation)
        g += 1

    chromosome = hof[0][0]

    scheduled_works = convert_chromosome_to_schedule(chromosome, agents, index2node,
                                                     worker_name2index,
                                                     index2contractor_obj,
                                                     spec, work_estimator)

    if show_fitness_graph:
        sns.lineplot(
            data=DataFrame.from_records([(g * 4, v) for g, v in enumerate(fitness_history)],
                                        columns=["Поколение", "Функция качества"]),
            x="Поколение",
            y="Функция качества",
            palette='r')
        plt.show()

    return scheduled_works


def compare_individuals(a: Tuple[ChromosomeType], b: Tuple[ChromosomeType]):
    return a[0][0] == b[0][0] and (a[0][1] == b[0][1]).all()
