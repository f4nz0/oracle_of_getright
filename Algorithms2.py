import networkx as nx
import Helpers
from operator import itemgetter
import matplotlib.pyplot as plt


def average_shortest_path(graph):
    largest_cc = graph.subgraph(max(nx.connected_components(graph), key=len))
    return nx.average_shortest_path_length(largest_cc)


def find_bridges(graph, labels, print_results=True, vis=False):
    bridges = nx.bridges(graph)
    bridgeslist = []
    for edge in bridges:
        bridgeslist.append(edge)

    if print_results:
        for edge in bridgeslist:
            print(labels[edge[0]] + " < - > " + labels[edge[1]])

    if vis:
        edge_colors = []
        edge_widths = []
        bridges = nx.bridges(graph)
        for edge in graph.edges:
            if edge in bridgeslist:
                edge_colors.append('red')
                edge_widths.append(4)
            else:
                edge_colors.append('black')
                edge_widths.append(1)
        nx.draw(graph, edge_color=edge_colors, width=edge_widths, with_labels=True, labels=labels)
        plt.show()

    return bridges


# Finds nodes who connect two otherwise disparate parts of the network
def betweenness_centrality(es_graph, labels, weights, tie_strength=1, print_results=True, vis=False):
    es_graph = es_graph.copy()
    for edge in weights:
        if len(weights[edge]) < tie_strength:
            if es_graph.has_edge(*edge):
                es_graph.remove_edge(*edge)

    betweenness_dict = nx.betweenness_centrality(es_graph)  # Run betweenness centrality

    # Assign each to an attribute in your network
    nx.set_node_attributes(es_graph, betweenness_dict, 'betweenness')

    sorted_betweenness = sorted(betweenness_dict.items(), key=itemgetter(1), reverse=True)
    if print_results:
        print("Top 20 players by betweenness centrality:")
        for b in sorted_betweenness[:20]:
            print(labels[b[0]] + " - " + str(b[1]))

    if vis:
        color_map = {}
        for node in es_graph.nodes:
            for btwnode in sorted_betweenness[:20]:
                if node == btwnode[0] :
                    color_map[node] = 'blue'
                    break
                else:
                    color_map[node] = 'red'
        values = [color_map.get(node, 0.25) for node in es_graph.nodes()]
        nx.draw(es_graph, node_color=values, edge_color='grey', with_labels=True, labels=labels)
        plt.show()

    return sorted_betweenness


def get_hubs(es_graph, labels, weights, tie_strength=1, print_results=True, vis=False):
    es_graph = es_graph.copy()
    for edge in weights:
        if len(weights[edge]) < tie_strength:
            if es_graph.has_edge(*edge):
                es_graph.remove_edge(*edge)

    degree_dict = dict(es_graph.degree(es_graph.nodes()))
    nx.set_node_attributes(es_graph, degree_dict, 'degree')

    if print_results:
        sorted_degree = sorted(degree_dict.items(), key=itemgetter(1), reverse=True)
        print("Top 20 players by degree (hubs): ")
        for d in sorted_degree[:20]:
            print(labels[d[0]] + " - " + str(d[1]))

    if vis:
        color_map = {}
        for node in es_graph.nodes:
            for srtnode in sorted_degree[:20]:
                if node == srtnode[0]:
                    color_map[node] = 'blue'
                    break
                else:
                    color_map[node] = 'red'
        values = [color_map.get(node, 0.25) for node in es_graph.nodes()]
        nx.draw(es_graph, node_color=values, edge_color='grey', with_labels=True, labels=labels)
        plt.show()


def print_metadata(graph):
    print("The player network contains " + str(len(graph.nodes)) + " players and " + str(len(graph.edges)) + " links between them.")
    largest_cc = graph.subgraph(max(nx.connected_components(graph), key=len))
    print("The largest component contains " + str(len(largest_cc.nodes)) + " (" + str(round(len(largest_cc.nodes) / len(graph.nodes) * 100, 2)) + "%) of the players.")
    print("The average shortest path for the largest component is " + str(round(average_shortest_path(graph), 2)))
    print("The average degree is: " + str(round(graph.number_of_edges() / len(graph.nodes), 2)))
    print("The average degree within the largest component is: " + str(round(largest_cc.number_of_edges() / len(largest_cc.nodes), 2)))
