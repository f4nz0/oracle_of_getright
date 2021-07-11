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

# communities = sorted(nxcom.greedy_modularity_communities(esports_graph), key=len, reverse=True)
# print(communities)
# vc.visualize_communities(esports_graph, labels, communities)
# Conclusion: in 2015 players were concentrated in national communities
# while in 2020 the communities are more mixed with different nationalities


# Algorithms.grvn_nwmn(esports_graph2, labels2)
# finds less Communities then the greedy_modularity algo in 2015

# Algorithms.louvain(esports_graph, labels)
#
Algorithms.clique_perc(esports_graph, labels)
# keine ahnung.. find_community stellt irgendwas an mit dem Graphen oder so
