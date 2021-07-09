from liquipediapy import liquipediapy, counterstrike
from CSGOAPI import CSGOAPI
import Helpers
import networkx as nx
import matplotlib.pyplot as plt
import time


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




if __name__ == '__main__':
    api = CSGOAPI('Oracle_of_GeT_RiGhT, University Research Project, https://github.com/f4nz0/oracle_of_getright')

    # Helpers.clear_json()
    # info = api.get_tournament_info("Cs_summit/8")
    # print(info)

    # all_tournament_ids = api.get_all_tournament_ids("B-Tier_Tournaments/2020-2019")
    # time.sleep(40)
    # all_tournaments = api.get_all_tournaments_from_ids(all_tournament_ids, 150, 200)
    # Helpers.write_results_to_json(all_tournaments)

    # api.get_all_real_player_ids(0, 500000)

    esports_graph, labels, weights = Helpers.network_from_json(tier='s')
    # nbs = esports_graph.neighbors(n='1886')

    # subgraph_labels = {'1886': "GeT_RiGhT"}
    # subgraph_nodes = ['1886']
    # for node in nbs:
    #     subgraph_nodes.append(node)
    #     subgraph_labels[node] = labels[node]
    # get_right = esports_graph.subgraph(subgraph_nodes)
    # # print(weights[('70745', '1886')])
    # # print(weights[('1886', '70745')])
    # # nx.draw(get_right, with_labels=True, labels=subgraph_labels)
    # # plt.show()
    #
    # nx.draw(esports_graph, with_labels=True, labels=labels)
    # plt.show()
    print(esports_graph.edges(Helpers.get_player_id_from_json("Juliano")))
    print(oracle_algorithm(esports_graph,labels, weights, Helpers.get_player_id_from_json("KennyS"), Helpers.get_player_id_from_json("GeT_RiGhT"), tie_strength=5))

