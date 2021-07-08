import Helpers as hp

#BreadthFirstSearch
def my_bfs(visited_nodes, graph, start_node):
    front_queue.append(start_node)
    visited_nodes.append(start_node)

    while front_queue:
        node = front_queue.pop(0)
        print("Next Node in front_queue: " + node)


        for next_node in graph[node]:
            if next_node not in visited_nodes:
                visited_nodes.append(next_node)
                front_queue.append(next_node)
    return visited_nodes


#Search route between two nodes with BFS
def route_between_two_nodes_with_bfs(visited_nodes, graph, start_node, end_node):
    front_queue.append(start_node)    #GeT_RiGhT
    visited_nodes.append(start_node)  #GeT_RiGhT

    while front_queue:
        node = front_queue.pop(0)      #--GeT_RiGhT
        if node == end_node:           #GeT_RiGhT == Karrigan?
            return "Found route between " + start_node + " and " + node

        for next_node in graph[node]:   #next adj node of GeT_RiGhT
            if next_node not in visited_nodes:  #not visited yet?
                visited_nodes.append(next_node)     #insert in both lists
                front_queue.append(next_node)

    return "No route found between node " + start_node + " and " + end_node


if __name__ == '__main__':
    # BFS Algorithm and search route between two nodes
    G = hp.network_from_json()
    visited_nodes, front_queue = [], []
    print("--Search route between two nodes with BFS--")
    print(route_between_two_nodes_with_bfs(visited_nodes, G, 'GeT_RiGhT', 'Karrigan'))
    print("Visited: ", visited_nodes)