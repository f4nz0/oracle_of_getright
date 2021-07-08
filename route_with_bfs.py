import Helpers as hp

visited_nodes, front_queue = [], []


#  Search route between two nodes with BFS
def route_between_two_nodes_with_bfs(graph, player_labels, start_n, end_n):
    start_node, end_node = name_to_rid_resolution(start_n, end_n)
    print(start_node)
    print(end_node)
    if start_node is None or int(start_node) < 0:
        return "Player " + start_n + " not found"
    if end_node is None or int(end_node) < 0:
        return "Player " + end_n + " not found"

    front_queue.append(start_node)
    visited_nodes.append(start_node)

    while front_queue:
        node = front_queue.pop(0)
        if node == end_node:
            return "Found route between " + player_labels[start_node] + " and " + player_labels[node]

        for next_node in graph[node]:
            if next_node not in visited_nodes:
                visited_nodes.append(next_node)
                front_queue.append(next_node)

    return "No route found between node " + player_labels[start_node] + " and " + player_labels[node]


def name_to_rid_resolution(start, end):
    id_from_name_start = hp.get_player_id_from_json(start)
    id_from_name_end = hp.get_player_id_from_json(end)
    return id_from_name_start, id_from_name_end


if __name__ == '__main__':

    G, pl, ew = hp.network_from_json()

    print("--Search route between two nodes with BFS--")
    print(route_between_two_nodes_with_bfs(G, pl, 'Get_RiGhT', 'friberg'))
    print("--visited nodes--")
    visited_names = []
    for i in visited_nodes:
        visited_names.append(pl[i])

    print(visited_names)
