# Importing required libraries and functions
import networkx as nx
import pandas as pd

# Function to create edgelist
def edgelist(file, header):
    # Reading file using Pandas
    if file[-3:] == 'txt':
        df = pd.read_table(file, header = header)
    elif file[-3:] == "csv":
        df = pd.read_csv(file, header = header)
    elif file[-4:] == "xlsx":
        df = pd.read_excel(file, header = header)
    else:
        raise TypeError("File format not supported")
    if len(df.columns) != 2:
        raise ValueError("Edgelist should contain only 2 columns")
    df.columns = ['0', '1']

    return df


# Function to create graph from edgelist
def loadGraph(edgelist, undirected):
    # Creating a NetworkX Graph object
    if undirected:
        G = nx.from_pandas_edgelist(edgelist)
    else:
        G = nx.from_pandas_edgelist(edgelist, source = '0', target = '1', create_using = nx.DiGraph())
    
    return G

# Function to divide a graph into its connected components
def getComponents(G, undirected):
    if undirected:
        connected_components = [G.subgraph(comp) for comp in sorted(nx.connected_components(G), key = len, reverse = True)]
    else:
        connected_components = [G.subgraph(comp) for comp in sorted(nx.strongly_connected_components(G), key = len, reverse = True)]

    return connected_components
