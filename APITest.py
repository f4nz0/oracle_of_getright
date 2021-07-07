from liquipediapy import liquipediapy, counterstrike
from CSGOAPI import CSGOAPI
import Helpers
import networkx as nx
import matplotlib.pyplot as plt
import time


if __name__ == '__main__':
    api = CSGOAPI('Oracle_of_GeT_RiGhT, University Research Project, https://github.com/f4nz0/oracle_of_getright')

    # Helpers.clear_json()
    # info = api.get_tournament_info("Cs_summit/8")
    # print(info)

    # all_tournament_ids = api.get_all_tournament_ids("A-Tier_Tournaments/2015-2013")
    # time.sleep(35)
    # all_tournaments = api.get_all_tournaments_from_ids(all_tournament_ids, 0, 56)
    # Helpers.write_results_to_json(all_tournaments)

    # api.get_all_real_player_ids(500, 40000)

    esports_graph, labels, weights = Helpers.network_from_json()
    nbs = esports_graph.neighbors(n='1886')

    subgraph_labels = {'1886': "GeT_RiGhT"}
    subgraph_nodes = ['1886']
    for node in nbs:
        subgraph_nodes.append(node)
        subgraph_labels[node] = labels[node]

    get_right = esports_graph.subgraph(subgraph_nodes)
    print(weights[('70745', '1886')])
    print(weights[('1886', '70745')])
    # nx.draw(get_right, with_labels=True, labels=subgraph_labels)
    # plt.show()

    nx.draw(esports_graph, with_labels=True, labels=labels)
    plt.show()

