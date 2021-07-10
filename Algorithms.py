import networkx as nx
from networkx.algorithms.community import girvan_newman, k_clique_communities
from communities.algorithms import louvain_method
import community as community_louvain
import random
import Helpers
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import VisualizeCommunities as vc
import networkx.algorithms.community as nxcom
import time


# Algorithms
def print_oracle(path, labels, weights, show=True):
    for i in range(0, len(path)):
        id = path[i]
        print(labels[id])
        if i + 1 < len(path) and show:
            print(weights[id, path[i + 1]])


def oracle_algorithm(graph, labels, weights, startplayer, endplayer, show_tournaments=True, show_teams=False, tie_strength=1):
    visited = []
    unvisited = [[startplayer]]

    if startplayer == endplayer:
        print("Same Node")
        return

    while unvisited:
        path = unvisited.pop(0)
        node = path[-1]
        if node not in visited:
            neighbors = graph[node]
            for neighbor in neighbors:
                tournaments = weights[(node, neighbor)]
                if len(tournaments) >= tie_strength:
                    new_path = list(path)
                    new_path.append(neighbor)
                    unvisited.append(new_path)
                    if neighbor == endplayer:
                        print_oracle(new_path, labels, weights, show_tournaments)
                        return new_path
            visited.append(node)


def louvain(G, labels):
    # https://python-louvain.readthedocs.io/en/latest/api.html
    partition = community_louvain.best_partition(G)

    # draw the graph
    pos = nx.spring_layout(G)
    # color the nodes according to their partition
    cmap = cm.get_cmap('viridis', max(partition.values()) + 1)
    nx.draw_networkx_nodes(G, pos, partition.keys(), node_size=40,
                           cmap=cmap, node_color=list(partition.values()))
    nx.draw_networkx_edges(G, pos, alpha=0.5)
    nx.draw_networkx_labels(G, pos, labels=labels)
    plt.show()


def grvn_nwmn(graph, labels):
    # Girvan-Newman https://networkx.guide/algorithms/community-detection/girvan-newman/
    communities = sorted(list(girvan_newman(graph)), key=len, reverse=True)

    # node_groups = []
    # for com in next(communities):
    #     node_groups.append(list(com))
    #
    # print(node_groups)
    #
    # color_map = []
    # for node in graph:
    #     if node in node_groups[0]:
    #         color_map.append('blue')
    #     else:
    #         color_map.append('green')
    # print(color_map)
    # nx.draw(graph, node_color=color_map, with_labels=True, labels=labels)
    # plt.show()
    vc.visualize_communities(graph, labels, communities)


def find_community(graph, k):
    return list(k_clique_communities(graph, k))


def clique_perc(graph, labels):
    # https://www.programmersought.com/article/38355328990/
    # layout = [nx.shell_layout,
    #           nx.circular_layout,
    #           nx.fruchterman_reingold_layout,
    #           nx.kamada_kawai_layout,
    #           nx.spring_layout]
    # nodeid = list(graph.nodes())
    # node_size = [graph.degree(i) ** 1.2 * 90 for i in nodeid]
    # options2 = {
    #     'node_size': node_size,
    #     'linewidths': 0.2,
    #     'width': 0.4,
    #     # 'node_color': node_size,  # the larger the node, the lighter the color
    #     'font_color': 'b',
    #     'font_size': 10,
    #     # 'labels': labels
    # }
    # nx.draw(g, pos=nx.spring_layout(g), with_labels=True, **options2)

    # for k in range(2, 10):
    #     rst_com = find_community(graph, k)
    #     print("For k = %d, there are %d Communities" % (k, len(rst_com)))
    #     print("Community View: %s" % rst_com)
    # time.sleep(10)
    communities = sorted(nxcom.greedy_modularity_communities(graph), key=len, reverse=True)
    k_com = sorted(find_community(graph, 3), key=len, reverse=True)
    print(k_com)
    print(communities)
    vc.visualize_communities(graph, labels, k_com)



