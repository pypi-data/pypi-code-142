# Importing required libraries and functions
import networkx as nx
import numpy as np

# Function to initialize the centroids
# using PageRank algorithm
def getCentroids(G, clusters):
    page_ranks = nx.pagerank(G)
    sorted_pages = [node[0] for node in sorted(page_ranks.items(), key = lambda node:node[1], reverse = True)]

    return sorted_pages[:clusters]

# Function to calculate the shortest distance between two nodes
def dist_btw_nodes(G, node, centroids):
    distances = np.array([])
    for i in centroids:
        distances = np.append(distances, nx.shortest_path_length(G, source = i, target = node))
    
    return distances


# KGraph - The clustering algorithm class
class KGraph:
    def __init__(self, n_clusters, max_iters):
        self.clusters = n_clusters
        self.max_iter = max_iters
    
    def fit(self, G):
        self.centroids = getCentroids(G, self.clusters)
        iter = 0
        prev_centroids = None
        while np.not_equal(self.centroids, prev_centroids).any() and iter < self.max_iter:
            clusters_list = [[] for _ in range(self.clusters)]
            for node in G:
                dists = dist_btw_nodes(G.to_undirected(), node, self.centroids)
                centroid_idx = np.argmin(dists)
                clusters_list[centroid_idx].append(node)
            iter += 1
        
        self.partition = clusters_list
