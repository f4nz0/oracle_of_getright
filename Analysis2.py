import Algorithms
import Helpers
import networkx as nx
import networkx.algorithms.community as nxcom
import matplotlib.pyplot as plt
import VisualizeCommunities as vc

# Hypothesis:
# in the early years of cs players were more clustered in national communities
# check Communities in 2015 and 2020
esports_graph, labels, weights = Helpers.network_from_json(start_date="2015-01-01", end_date="2015-12-31", tier='s')
# nx.draw(esports_graph, with_labels=True, labels=labels)
# plt.show()
# Algorithms.grvn_nwmn(esports_graph, labels)
# maybe not the best algo for this analysis
# needs only the giant component, not the already disconnected ones
g_karate = nx.karate_club_graph()
# Algorithms.clique_perc(g_karate, labels)
vc.visualizeCom(esports_graph, labels)
