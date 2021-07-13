import Algorithms
import Helpers
import networkx as nx
import networkx.algorithms.community as nxcom
import matplotlib.pyplot as plt
import VisualizeCommunities as vc

def hypothesis_female_to_male_bridges():
    es_graph, labels, weights = Helpers.network_from_json(tier='b')

    juliano = Helpers.get_player_id_from_json("Juliano")
    harvey = Helpers.get_player_id_from_json("Missharvey")
    blackie = Helpers.get_player_id_from_json("Blackie")
    sapphire = Helpers.get_player_id_from_json("SapphiRe")
    showliana = Helpers.get_player_id_from_json("Showliana")
    di = Helpers.get_player_id_from_json("Di%5E")
    Algorithms.find_bridges(es_graph, labels, vis=True)

    # Juliano has too many connections to male/female players to appear as a bridge (in terms of edges)
    # What if we were to remove juliano as a node?

    graph = es_graph.copy()
    print(Algorithms.oracle_algorithm(graph, labels, weights, Helpers.get_player_id_from_json("Missa"),
                                      Helpers.get_player_id_from_json("GeT_RiGhT"), tie_strength=1))
    print("Components: " + str(len(list(nx.algorithms.components.connected_components(graph)))))
    graph.remove_node(juliano)
    print("Components after removing juliano: " + str(len(list(nx.algorithms.components.connected_components(graph)))))

    # The number of components doesn't increase as there is still a connection between male and female players

    print(Algorithms.oracle_algorithm(graph,labels, weights, Helpers.get_player_id_from_json("Missa"),
                                      Helpers.get_player_id_from_json("GeT_RiGhT"), tie_strength=1))
    # This connection is a player called 'MissHarvey'. We deleted her from the network.
    graph.remove_node(harvey)
    print(Algorithms.oracle_algorithm(graph, labels, weights, Helpers.get_player_id_from_json("Missa"),
                                      Helpers.get_player_id_from_json("GeT_RiGhT"), tie_strength=1))
    # Now a player called 'blackie' provides the connection.
    graph.remove_node(blackie)
    print(Algorithms.oracle_algorithm(graph, labels, weights, Helpers.get_player_id_from_json("Missa"),
                                      Helpers.get_player_id_from_json("GeT_RiGhT"), tie_strength=1))
    graph.remove_node(sapphire)
    print(Algorithms.oracle_algorithm(graph, labels, weights, Helpers.get_player_id_from_json("Missa"),
                                      Helpers.get_player_id_from_json("GeT_RiGhT"), tie_strength=1))
    graph.remove_node(showliana)
    print(Algorithms.oracle_algorithm(graph, labels, weights, Helpers.get_player_id_from_json("Missa"),
                                      Helpers.get_player_id_from_json("GeT_RiGhT"), tie_strength=1))
    graph.remove_node(di)
    print(Algorithms.oracle_algorithm(graph, labels, weights, Helpers.get_player_id_from_json("Missa"),
                                      Helpers.get_player_id_from_json("GeT_RiGhT"), tie_strength=1))

    # Even after removing multiple players, there is still a path between female and male players.

    # There are more than half a dozen female players connecting to various male players
    # So is juliano not that important for the connectedness of the network?
    # One last check: What does the Average Shortest Path (ASP) look like with our without juliano?


    graph2 = es_graph.copy()
    # print(Algorithms2.average_shortest_path(graph2))  # Result: 4.524040829526511
    graph2.remove_node(juliano)
    # print(Algorithms2.average_shortest_path(graph2))  # Result: 4.590959028867526
    graph3 = es_graph.copy()
    graph3.remove_node(Helpers.get_player_id_from_json("GeT_RiGhT"))
    # print(Algorithms2.average_shortest_path(graph3))  # Result: 4.534702141238089

    # Conclusion: Removing juliano from the network has a much larger effect on the ASP than even GeT_RiGhT,
    # since she provides a direct and comparatively short link to highly connected nodes. Other female players
    # might connect to the male scene, but they do so over longer paths.
    # Final proof: Shortest Path from Missa to GeT_RiGhT with or without juliano

    print(str(len(Algorithms.oracle_algorithm(es_graph, labels, weights, Helpers.get_player_id_from_json("Missa"),
                                      Helpers.get_player_id_from_json("GeT_RiGhT"), tie_strength=1))))  # Result: 4
    print(str(len(Algorithms.oracle_algorithm(graph2, labels, weights, Helpers.get_player_id_from_json("Missa"),
                                      Helpers.get_player_id_from_json("GeT_RiGhT"), tie_strength=1))))  # Result: 7

    # The path length between Missa and GeT_RiGhT jumps up by 3 after removing juliano!


def hypothesis_asp_decrease():
    graph_2014, labels_2014, weights_2014 = Helpers.network_from_json(end_date="2014-12-31", tier='b')
    graph_2020, labels_2020, weights_2020 = Helpers.network_from_json(end_date="2020-12-31", tier='b')
    asp_2014 = Algorithms.average_shortest_path(graph_2014)
    print("ASP in 2014: " + str(asp_2014))
    asp_2020 = Algorithms.average_shortest_path(graph_2020)
    print("ASP in 2020: " + str(asp_2020))
    print("Difference in %: " + str((1 - asp_2020 / asp_2014) * 100))

    graph_2014, labels_2014, weights_2014 = Helpers.network_from_json(end_date="2014-12-31", tier='s')
    graph_2020, labels_2020, weights_2020 = Helpers.network_from_json(end_date="2020-12-31", tier='s')
    asp_2014 = Algorithms.average_shortest_path(graph_2014)
    print("ASP in 2014 (S-Tier): " + str(asp_2014))
    asp_2020 = Algorithms.average_shortest_path(graph_2020)
    print("ASP in 2020 (S-Tier): " + str(asp_2020))
    print("Difference in % (S-Tier): " + str((1 - asp_2020 / asp_2014) * 100))


def betweenness():
    esports_graph_2015, labels_2015, weights_2015 = Helpers.network_from_json(start_date="2015-01-01", end_date="2015-12-31", tier='b')
    Algorithms.betweenness_centrality(esports_graph_2015, labels_2015, weights_2015, tie_strength=1, vis=True)


def hypothesis_community():
    # Testgraph
    g_karate = nx.karate_club_graph()  # comment out labels=labels in visualize_communities()

    # in the early years of cs players were more clustered in national communities
    # check Communities in 2015
    esports_graph, labels, weights = Helpers.network_from_json(start_date="2015-01-01", end_date="2015-12-31", tier='s')
    #  and 2020
    esports_graph2, labels2, weights2 = Helpers.network_from_json(start_date="2020-01-01", end_date="2020-12-31",
                                                                  tier='s')
    # then from 2015 to 2020
    esports_graph3, labels3, weights3 = Helpers.network_from_json(start_date="2015-01-01", end_date="2020-12-31",
                                                                  tier='s')
    # alles
    esports_graph_b, labels_b, weights_b = Helpers.network_from_json(start_date="2015-01-01", end_date="2020-12-31",
                                                                     tier='b')

    # communities = sorted(nxcom.greedy_modularity_communities(esports_graph_b), key=len, reverse=True)
    # print(communities)
    # vc.visualize_communities(esports_graph_b, labels_b, communities)
    # Conclusion: in 2015 players were concentrated in national communities
    # while in 2020 the communities are more mixed with different nationalities

    # Algorithms.grvn_nwmn(esports_graph2, labels2)
    # finds less Communities then the greedy_modularity algo in 2015

    # Algorithms.louvain(esports_graph_b, labels_b)
    #
    Algorithms.clique_perc(esports_graph2, labels)
    # Visualization doesn't work, only print()

    # Algorithms.find_largest_clique(esports_graph_b, labels_b)
    # Algorithms.small_world(esports_graph2)
    # 2015
    # after ~ 45 mins of calc: sigma = 8.168844 is > 1 = small world
    # also after very long time (1h): omega = -0.388746 is near 0 = small world