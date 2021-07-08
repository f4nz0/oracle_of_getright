import networkx as nx
from networkx.algorithms.community import girvan_newman, k_clique_communities
from communities.algorithms import louvain_method
import community as community_louvain
import Helpers
import matplotlib.pyplot as plt
import matplotlib.cm as cm

options1 = {'node_color': 'blue',
            'node_size': 50,
            'with_labels': 'True',
            'font_color': 'red',
            'font_weight': 'normal',
            'font_size': 10
            }


# Algorithms
def louvain(G):
    # https://python-louvain.readthedocs.io/en/latest/api.html
    partition = community_louvain.best_partition(G)

    # draw the graph
    pos = nx.spring_layout(G)
    # color the nodes according to their partition
    cmap = cm.get_cmap('viridis', max(partition.values()) + 1)
    nx.draw_networkx_nodes(G, pos, partition.keys(), node_size=40,
                           cmap=cmap, node_color=list(partition.values()))
    nx.draw_networkx_edges(G, pos, alpha=0.5)
    nx.draw_networkx_labels(G, pos)
    plt.show()


def grvn_nwmn(G):
    # Girvan-Newman https://networkx.guide/algorithms/community-detection/girvan-newman/
    communities = girvan_newman(G)
    node_groups = []
    for com in next(communities):
        node_groups.append(list(com))

    print(node_groups)

    color_map = []
    for node in G:
        if node in node_groups[0]:
            color_map.append('blue')
        else:
            color_map.append('green')
    nx.draw(G, node_color=color_map, with_labels=True)
    plt.show()


def find_community(graph, k):
    return list(k_clique_communities(graph, k))


def clique_perc(g):
    # https://www.programmersought.com/article/38355328990/
    layout = [nx.shell_layout,
              nx.circular_layout,
              nx.fruchterman_reingold_layout,
              nx.kamada_kawai_layout,
              nx.spring_layout]
    nodeid = list(g.nodes())
    node_size = [g.degree(i) ** 1.2 * 90 for i in nodeid]
    options2 = {
        'node_size': node_size,
        'linewidths': 0.2,
        'width': 0.4,
        'node_color': node_size,  # the larger the node, the lighter the color
        'font_color': 'b',
        'font_size': 10
    }
    nx.draw(g, pos=nx.circular_layout(g), with_labels=True, **options2)

    for k in range(2, 15):
        rst_com = find_community(g, k)
        print("For k = %d, there are %d Communities" % (k, len(rst_com)))
        print("Community View: %s" % rst_com)
    plt.show()


G, _, _ = Helpers.network_from_json()
GK = nx.karate_club_graph()
A = nx.adjacency_matrix(GK)

# grvn_nwmn(GK)                               #girvan_newman schaffts vermutlich nicht, läuft und läuft und macht Dinge
# coms = list(nx.community.girvan_newman(G))  #girvan_newman schaffts vermutlich nicht, läuft und läuft und macht Dinge
# print(coms)

print("###########################################")
clique_perc(G)  # seems okay
#  louvain(G)
# nx.draw(coms, **options1)
#nx.draw(G, **options1)
#plt.show()
