# Copyright (c) 2022, Ora Lassila & So Many Aircraft
# All rights reserved.
#
# See LICENSE for licensing information
#
# This module implements some useful stuff when programming with RDFLib.

from rdfhelpers.rdfhelpers import expandQName, URI, getvalue, setvalue
from rdfhelpers.rdfhelpers import isContainerItemPredicate, makeContainerItemPredicate, diff
from rdfhelpers.cbd import cbd, reverse_cbd
from rdfhelpers.rdfhelpers import getContainerStatements, getContainerItems, setContainerItems
from rdfhelpers.rdfhelpers import SPARQLRepository, FocusedGraph, CBDGraph
from rdfhelpers.templated import graphFrom, identity, mapDict
from rdfhelpers.templated import Templated, Composable
from rdfhelpers.constructor import Constructor
from rdfhelpers.labels import LabelCache, SKOSLabelCache, BNodeTracker, BNodeMarker
from rdfhelpers.gsp import GraphStoreClient
from rdfhelpers.tinyrml import RR, Mapper

__all__ = [
    'expandQName', 'URI', 'getvalue', 'setvalue',
    'isContainerItemPredicate', 'makeContainerItemPredicate', 'diff',
    'cbd', "reverse_cbd",
    'getContainerStatements', 'getContainerItems', 'setContainerItems',
    'SPARQLRepository', 'FocusedGraph', 'CBDGraph',
    'graphFrom', 'identity', 'mapDict',
    'Templated', 'Composable',
    'Constructor',
    'LabelCache', 'SKOSLabelCache', 'BNodeTracker', 'BNodeMarker',
    'GraphStoreClient',
    'RR', 'Mapper'
]
