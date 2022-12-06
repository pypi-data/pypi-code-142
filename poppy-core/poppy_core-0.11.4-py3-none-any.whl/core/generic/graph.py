#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import collections

__all__ = ["Graph"]


class Graph(object):
    """
    A class to manage the graph that is storing the topology of the graph.
    """
    def __init__(self):
        """
        Init the structure containing nodes and their relation.
        """
        self.graph = collections.defaultdict(set)

    def add_node(self, node, child):
        """
        Add a node to the graph, with a given child.
        """
        self.graph[node].add(child)

    def find_all_paths(self, start, end, path=None):
        """
        Find all existing paths between to nodes.
        """
        if path is None:
            path = []
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graph:
            return []
        paths = []
        for node in self.graph[start]:
            if node not in path:
                newpaths = self.find_all_paths(node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

    def find_linking_nodes(self, start, end):
        """
        To find all nodes between two nodes. This is the concatenation of all
        paths between the two nodes in argument.
        """
        # get all paths
        paths = self.find_all_paths(start, end)

        # loop over paths to get the set of unique nodes
        nodes = set()
        for path in paths:
            for node in path:
                nodes.add(node)

        return nodes

    def __contains__(self, task):
        return task in self.graph


# vim: set tw=79 :
