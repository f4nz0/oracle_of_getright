from liquipediapy import liquipediapy, counterstrike

import Analysis
from CSGOAPI import CSGOAPI
import Helpers
import Algorithms
import networkx as nx
import matplotlib.pyplot as plt
import time



if __name__ == '__main__':
    api = CSGOAPI('Oracle_of_GeT_RiGhT, University Research Project, https://github.com/f4nz0/oracle_of_getright')

    # Usage example for getting a specific set of tournaments:
    # all_tournament_ids = api.get_all_tournament_ids("B-Tier_Tournaments/2020-2019")
    # time.sleep(40)
    # all_tournaments = api.get_all_tournaments_from_ids(all_tournament_ids, 150, 200)
    # Helpers.write_results_to_json(all_tournaments)

    # Usage example for getting the real player IDs from Liquipedia
    # api.get_all_real_player_ids(0, 500000)

    # This will create and show a graph from 2020 with only the highest level of competitions
    esports_graph, labels, weights = Helpers.network_from_json(start_date="2020-01-01", end_date="2020-12-31", tier='s')
    nx.draw(esports_graph, with_labels=True, labels=labels)
    plt.show()

    # This will get the ids for two players, and calculate + draw the path between them
    karrigan = Helpers.get_player_id_from_json("Karrigan")
    get_right = Helpers.get_player_id_from_json("GeT_RiGhT")
    print(Algorithms.oracle_algorithm(esports_graph, labels, weights, karrigan, get_right, tie_strength=1, vis=True))


