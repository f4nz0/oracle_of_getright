import networkx as nx
import Helpers


def average_shortest_path(graph):
    largest_cc = graph.subgraph(max(nx.connected_components(graph), key=len))
    return nx.average_shortest_path_length(largest_cc)


def find_bridges(graph):
    return nx.bridges(graph)