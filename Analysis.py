import Algorithms
import Helpers
import networkx as nx


def female_to_male_bridges(es_graph, labels, weights):
    juliano = Helpers.get_player_id_from_json("Juliano")
    harvey = Helpers.get_player_id_from_json("Missharvey")
    blackie = Helpers.get_player_id_from_json("Blackie")
    sapphire = Helpers.get_player_id_from_json("SapphiRe")
    showliana = Helpers.get_player_id_from_json("Showliana")
    di = Helpers.get_player_id_from_json("Di%5E")
    for edge in Algorithms.find_bridges(es_graph):
        print(labels[edge[0]] + " < - > " + labels[edge[1]])
        if juliano in edge:
            print("JAUSAAAAA")
    for edge in es_graph.edges(juliano):
        print(labels[edge[1]])
    ## Juliano has too many connections to male/female players to appear as a bridge (in terms of edges)
    ## What if we were to remove juliano as a node?

    graph = es_graph.copy()
    print(Algorithms.oracle_algorithm(graph, labels, weights, Helpers.get_player_id_from_json("Missa"),
                                      Helpers.get_player_id_from_json("GeT_RiGhT"), tie_strength=1))
    print("Komponenten: " + str(len(list(nx.algorithms.components.connected_components(graph)))))
    graph.remove_node(juliano)
    print("Komponenten nach Entfernung von juliano: " + str(len(list(nx.algorithms.components.connected_components(graph)))))
    print(Algorithms.oracle_algorithm(graph,labels, weights, Helpers.get_player_id_from_json("Missa"),
                                      Helpers.get_player_id_from_json("GeT_RiGhT"), tie_strength=1))
    graph.remove_node(harvey)
    print(Algorithms.oracle_algorithm(graph, labels, weights, Helpers.get_player_id_from_json("Missa"),
                                      Helpers.get_player_id_from_json("GeT_RiGhT"), tie_strength=1))
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

    graph2 = es_graph.copy()
    # ASP
    graph2.remove_node(juliano)
    # ASP
