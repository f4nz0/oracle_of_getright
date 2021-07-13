import Algorithms
import Helpers
import networkx as nx
import networkx.algorithms.community as nxcom
import matplotlib.pyplot as plt
import VisualizeCommunities as vc

# Testgraph
g_karate = nx.karate_club_graph() # comment out labels=labels in visualize_communities()

# Hypothesis:
# in the early years of cs players were more clustered in national communities
# check Communities in 2015
esports_graph, labels, weights = Helpers.network_from_json(start_date="2015-01-01", end_date="2015-12-31", tier='s')
#  and 2020
esports_graph2, labels2, weights2 = Helpers.network_from_json(start_date="2020-01-01", end_date="2020-12-31", tier='s')
# then from 2015 to 2020
esports_graph3, labels3, weights3 = Helpers.network_from_json(start_date="2015-01-01", end_date="2020-12-31", tier='s')
# alles
esports_graph_b, labels_b, weights_b = Helpers.network_from_json(start_date="2015-01-01", end_date="2020-12-31", tier='b')

communities = sorted(nxcom.greedy_modularity_communities(esports_graph_b), key=len, reverse=True)
# print(communities)
vc.visualize_communities(esports_graph_b, labels_b, communities)
# Conclusion: in 2015 players were concentrated in national communities
# while in 2020 the communities are more mixed with different nationalities

# Algorithms.grvn_nwmn(esports_graph2, labels2)
# finds less Communities then the greedy_modularity algo in 2015

# Algorithms.louvain(esports_graph_b, labels_b)
#
# Algorithms.clique_perc(esports_graph, labels)
# keine ahnung.. find_community stellt irgendwas an mit dem Graphen oder so

# Algorithms.find_largest_clique(esports_graph3, labels3)
# Algorithms.small_world(esports_graph2)
# 2015
# after ~ 45 mins of calc: sigma = 8.168844 is > 1 = small world
# also after very long time (1h): omega = -0.388746 is near 0 = small world