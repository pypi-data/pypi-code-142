# Copyright (c) 2022, Ora Lassila & So Many Aircraft
# All rights reserved.
#
# See LICENSE for licensing information
#
# This module implements some useful functionality for querying with RDFLib.
#
import logging
import rdflib
import rdflib.plugins.sparql.processor
from rdflib import Literal, URIRef
import string
import numbers
from rdfhelpers.tinyrml import Mapper

def identity(x):
    return x

# Make a new dictionary with values mapped using a callable
def mapDict(dictionary, mapper=identity):
    d = dict()
    for key, value in dictionary.items():
        d[key] = mapper(value)
    return d

# TEMPLATED QUERIES
#
# This mechanism can be used in lieu of RDFLib's "initBindings=" parameter for SPARQL queries,
# with the added benefit that replacements are not limited to SPARQL terms.
class Templated:

    @classmethod
    def query(cls, graph, template, **kwargs):
        q = cls.convert(template, kwargs) if kwargs else template
        logging.debug(q)
        return graph.query(q)

    @classmethod
    def update(cls, graph, template, **kwargs):
        q = cls.convert(template, kwargs) if kwargs else template
        logging.debug(q)
        graph.update(q)

    @classmethod
    def convert(cls, template, kwargs):
        return string.Template(template).substitute(**mapDict(kwargs, mapper=cls.forSPARQL))

    @classmethod
    def forSPARQL(cls, thing):
        if isinstance(thing, URIRef) or isinstance(thing, Literal):
            return thing.n3()
        elif isinstance(thing, str):
            return thing  # if thing[0] == '?' else cls.forSPARQL(Literal(thing))
        elif isinstance(thing, bool):
            return "true" if thing else "false"
        elif isinstance(thing, numbers.Number):
            return thing
        elif thing is None:
            return ""
        else:
            raise ValueError("Cannot make a SPARQL compatible value: %s", thing)

class TemplatedQueryMixin:  # abstract, can be mixed with Graph or Store

    def query(self, querystring, **kwargs):
        return Templated.query(super(), querystring, **kwargs)

    def update(self, querystring, **kwargs):
        Templated.update(super(), querystring, **kwargs)

class TemplateWrapper:
    def __init__(self, graph):
        self._graph = graph

    def query(self, querystring, **kwargs):
        return Templated.query(self._graph, querystring, **kwargs)

    def update(self, querystring, **kwargs):
        Templated.update(self._graph, querystring, **kwargs)


# Make a new Graph instance from triples (an iterable)
def graphFrom(triples, add_to=None, graph_class=rdflib.Graph, **kwargs):
    if add_to is None:
        add_to = graph_class(**kwargs)
    for triple in triples:
        add_to.add(triple)
    return add_to if len(add_to) > 0 else None

class Composable:
    def __init__(self, graph=None):
        if isinstance(graph, Composable):
            self._graph = graph._graph
        else:
            self._graph = graph or rdflib.Graph()

    @property
    def result(self):
        return self._graph

    def __len__(self):
        return len(self._graph)

    def __add__(self, other):
        if isinstance(other, Composable):
            other = other._graph
        elif not isinstance(other, rdflib.Graph):
            raise ValueError("Cannot be added to a graph: {}".format(other))
        return self.__class__(self._graph + other)

    def add(self, *triples):
        for triple in triples:
            self._graph.add(triple)
        return self

    def bind(self, prefix, namespace):
        self._graph.bind(prefix, namespace)
        return self

    def parse(self, *args, **kwargs):
        self._graph.parse(*args, **kwargs)
        return self

    def serialize(self, *args, **kwargs):
        self._graph.serialize(*args, **kwargs)

    def construct(self, template, **kwargs):
        # TODO: How do we confirm that `template` is a `CONSTRUCT` query?
        return self.__class__(graphFrom(Templated.query(self._graph, template, **kwargs)))

    def query(self, template, **kwargs):
        return Templated.query(self._graph, template, **kwargs)

    def update(self, template, **kwargs):
        Templated.update(self._graph, template, **kwargs)
        return self

    def mapData(self, m, rows, **kwargs):
        mapper = m if isinstance(m, Mapper) else Mapper(m, **kwargs)
        mapper.process(rows, result_graph=self.result)
        return self

    def injectResult(self, target, context, function, **kwargs):
        logging.warning("Adding data to graph {}".format(context))
        return function(target, self.result, context, **kwargs)
