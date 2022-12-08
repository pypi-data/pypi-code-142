# Importing required libraries and function
from networkx.algorithms.community import modularity
from sklearn.metrics.cluster import adjusted_rand_score

# Function to calculate Adjusted Rand Score
# Can only be used when ground truth is known

def ari_score(truth, partition):
    return adjusted_rand_score(truth, partition)

# Function to calculate modularity of partitioning
def modularity_score(G, partition):
    return modularity(G, partition)
