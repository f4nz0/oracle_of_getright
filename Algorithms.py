import networkx as nx
import community as community_louvain
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import VisualizeCommunities as vc
import networkx.algorithms.community as nxcom
import time


# Algorithms
def print_oracle(graph, path, labels, weights, show=True, vis=False):
    edgelist = []
    for i in range(0, len(path)):
        id = path[i]
        print(labels[id])
        if i + 1 < len(path) and show:
            print(weights[id, path[i + 1]])
            if vis:
                edgelist.append((id, path[i + 1]))

    if vis:
        edge_colors = []
        edge_widths = []
        for edge in graph.edges:
            if edge in edgelist:
                edge_colors.append('red')
                edge_widths.append(7)
            else:
                edge_colors.append('grey')
                edge_widths.append(1)
        nx.draw(graph, edge_color=edge_colors, width=edge_widths, with_labels=True, labels=labels)
        plt.show()


def oracle_algorithm(graph, labels, weights, startplayer, endplayer, show_tournaments=True, vis=False, tie_strength=1):
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
                        print_oracle(graph, new_path, labels, weights, show_tournaments, vis)
                        return new_path
            visited.append(node)


def louvain(G, labels):
    # https://python-louvain.readthedocs.io/en/latest/api.html
    partition = community_louvain.best_partition(G)
    print(partition.values())
    partition_list = list(partition.values())
    tmp2 = []
    for value in partition_list:
        if value not in tmp2:
            tmp2.append(value)
    print('Partitions: %d ' % len(tmp2))
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
    temp = nxcom.girvan_newman(graph)
    communities = next(temp)
    vc.visualize_communities(graph, labels, communities)


def find_community(graph, k):
    return list(nxcom.k_clique_communities(graph, k))


def clique_perc(graph, labels):
    # https://www.programmersought.com/article/38355328990/
    largest_cc = graph.subgraph(max(nx.connected_components(graph), key=len))

    for k in range(2, 14):
        rst_com = find_community(largest_cc, k)
        print("For k = %d, there are %d Communities generated" % (k, len(rst_com)))
        # print("Community View: %s" % rst_com)
    # time.sleep(5)
    #
    # communities = sorted(nxcom.greedy_modularity_communities(graph), key=len, reverse=True)
    # k_com = sorted(find_community(graph, 3), key=len, reverse=True)
    # vc.visualize_communities(graph, labels, k_com)


def find_largest_clique(graph, labels):

    graph_pos = nx.spring_layout(graph)
    plt.rcParams.update(plt.rcParamsDefault)
    plt.rcParams.update({'figure.figsize': (15, 10)})
    cliques = list(nx.find_cliques(graph))
    max_clique = max(cliques, key=len)
    node_color = [(0.5, 0.5, 0.5) for v in graph.nodes()]
    for i, v in enumerate(graph.nodes()):
        if v in max_clique:
            node_color[i] = (0.5, 0.5, 0.9)
    nx.draw_networkx(graph, node_color=node_color, pos=graph_pos, labels=labels)
    plt.show()


def small_world(graph):
    largest_cc = graph.subgraph(max(nx.connected_components(graph), key=len))
    small_world_coeff_si = nx.algorithms.sigma(largest_cc)
    small_world_coeff_om = nx.algorithms.omega(largest_cc)
    print('sigma: %f ' % small_world_coeff_si)
    print('omega: %f ' % small_world_coeff_om)
    if small_world_coeff_si > 1:
        print('this graph is classified as small-world')
    else:
        print('no small-world')

    if -0.5 < small_world_coeff_om < 0.5:
        print('this graph features small-world characteristics')
    else:
        print('no small-world')

    nx.draw_networkx(largest_cc)
    plt.show()


