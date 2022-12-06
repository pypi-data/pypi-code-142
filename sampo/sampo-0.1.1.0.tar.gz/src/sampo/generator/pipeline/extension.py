from random import Random

from sampo.generator import get_graph
from sampo.schemas.graph import WorkGraph, GraphNode


def generate_work_graph(activities_count: int, edges_count: int, uniq_activities: int, uniq_resources: int,
                        rand: Random) -> WorkGraph:
    wg = get_graph(top_border=activities_count)
    return wg


def add_edges(edges_count: int, wg: WorkGraph, rand: Random) -> WorkGraph:
    current_edges = sum([len(node.parents) for node in wg.nodes], 0)
    matrix = {}
    return wg


def add_resources(uniq_activities: int, wg: WorkGraph, rand: Random) -> WorkGraph:
    current_edges = sum([len(node.parents) for node in wg.nodes], 0)
    matrix = {}
    return wg


def _change_name(node: GraphNode, name_to_suffixes: dict[str, list[str]], rand: Random):
    name = node.work_unit.name
    options = name_to_suffixes[name]
    print(options)
    node.work_unit.name = name + options[rand.randint(0, len(options))]


def add_names(uniq_resources: int, wg: WorkGraph, rand: Random) -> WorkGraph:
    start_finish_names = {wg.start.work_unit.name, wg.finish.work_unit.name}
    current_uniq_names = list(set(node.work_unit.name for node in wg.nodes) - start_finish_names)
    if uniq_resources <= len(current_uniq_names):
        return wg

    rand.shuffle(current_uniq_names)
    names_plus_one = set(current_uniq_names[:uniq_resources % len(current_uniq_names)])
    suffixes = ['_' + str(i + 1) for i in range(uniq_resources // len(current_uniq_names))]
    name_to_suffixes = {name: (suffixes + ['_0'] if name in names_plus_one else []) for name in current_uniq_names}
    c = [_change_name(node, name_to_suffixes, rand) for node in wg.nodes if node.work_unit.name not in start_finish_names]

    return wg