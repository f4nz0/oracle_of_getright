import networkx as nx
from matplotlib import pyplot as plt
# taken from https://orbifold.net/default/community-detection-using-networkx/


def set_node_community(G, communities):
    '''Add community to node attributes'''
    for c, v_c in enumerate(communities):
        for v in v_c:
            # Add 1 to save 0 for external edges
            G.nodes[v]['community'] = c + 1


def set_edge_community(G):
    '''Find internal edges and add their community to their attributes'''
    for v, w, in G.edges:
        if G.nodes[v]['community'] == G.nodes[w]['community']:
            # Internal edge, mark with community
            G.edges[v, w]['community'] = G.nodes[v]['community']
        else:
            # External edge, mark as 0
            G.edges[v, w]['community'] = 0


def get_color(i, r_off=1, g_off=1, b_off=1):
    '''Assign a color to a vertex.'''
    r0, g0, b0 = 0, 0, 0
    n = 16
    low, high = 0.1, 0.9
    span = high - low
    r = low + span * (((i + r_off) * 3) % n) / (n - 1)
    g = low + span * (((i + g_off) * 5) % n) / (n - 1)
    b = low + span * (((i + b_off) * 7) % n) / (n - 1)
    return r, g, b


def visualize_communities(graph, labels, communities):

    print(f"The Graph has {len(communities)} communities.")

    set_node_community(graph, communities)
    set_edge_community(graph)

    node_color = [get_color(graph.nodes[v]['community']) for v in graph.nodes]

    # Set community color for edges between members of the same
    # community (internal) and intra-community edges (external)
    external = [(v, w) for v, w in graph.edges if graph.edges[v, w]['community'] == 0]
    internal = [(v, w) for v, w in graph.edges if graph.edges[v, w]['community'] > 0]
    internal_color = ['black' for e in internal]

    graph_pos0 = nx.spring_layout(graph)
    graph_pos1 = nx.circular_layout(graph)
    graph_pos2 = nx.fruchterman_reingold_layout(graph)
    graph_pos3 = nx.kamada_kawai_layout(graph)

    plt.rcParams.update({'figure.figsize': (30, 20)})
    # Draw external edges
    nx.draw_networkx(
        graph,
        pos=graph_pos0,
        node_size=0,
        labels=labels,
        edgelist=external,
        edge_color="silver")
    # Draw nodes and internal edges
    nx.draw_networkx(
        graph,
        pos=graph_pos0,
        node_color=node_color,
        labels=labels,
        edgelist=internal,
        edge_color=internal_color)

    plt.show()
