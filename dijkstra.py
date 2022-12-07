"""
Dijkstra's Algorithm
- an algorithm for finding shortest paths between nodes in a graph
"""
class Graph(): 
    #init method of Graph class
    #constructs a graph attribute using construct_graph
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)

    def construct_graph(self, nodes, init_graph):
        graph = {} #graph (to be returned) initially set to an empty dictionary
        for node in nodes:
            graph[node] = {} #initialize values of all keys (nodes) to an empty dictionary
        graph = init_graph #updates graph to be init_graph

        #graph: node, edges. edges: adjacent_node(cities), value (distance to other cities)
        for (node, edges) in graph.items(): #for each key-value pair (node, edges=dict(adj_node, distance)) in graph.items()
            for (adj_node, dist) in edges.items(): #for each key-value pair (adj_node, dist) in edges.items()
                if graph[adj_node].get(node, False) == False: #if there is no pointer from node's adj_node to node
                    graph[adj_node][node] = dist #create an pointer from adj_node to node with value dist 

        return graph

    def get_nodes(self):
        return self.nodes
    
    def get_adj_nodes(self, node):
        connections = [] #to be returned
        #if there is a path from node to adj_node then append adj_node to connections
        for adj_node in self.nodes:
            if self.graph[node].get(adj_node):
                connections.append(adj_node)
        return connections
    
    def dist(self, node1, node2):
        return self.graph[node1][node2]


    #dijkstra implementation
    def dijkstra(graph, start_node):
        #initialization
        unvisited_nodes = list(graph.get_nodes()) #list of unvisited nodes
        shortest_path = {} #gives distance of shortest path to each node
        previous_nodes = {}
        for node in unvisited_nodes:
            shortest_path[node] = float('inf')
        shortest_path[start_node] = 0

        while unvisited_nodes: #"while we haven't visited all the nodes yet" -> algorithm runs until all nodes visited
            #min_node = node with lowest distance
            min_node = None
            for node in unvisited_nodes:
                if min_node == None:
                    min_node = node
                elif shortest_path[node] < shortest_path[min_node]:
                    min_node = node
 
            adj_nodes = graph.get_adj_nodes(min_node)
            for adj_node in adj_nodes:
                #calculates distance to min_node + distance to ad_node from min_node
                potential_path = shortest_path[min_node] + graph.dist(min_node, adj_node) 
                if potential_path < shortest_path[adj_node]: #if potential_path is quicker than any previous path to adj_node
                    #update shortest_path dictionary
                    shortest_path[adj_node] = potential_path
                    #update previous_nodes dictionary
                    previous_nodes[adj_node] = min_node
            #after visiting all the adjacent nodes mark current min_node as visited
            unvisited_nodes.remove(min_node)
        #return our two dictionaries
        return previous_nodes, shortest_path

    def print_result(self, previous_nodes, shortest_path, start, end):
        path = []
        node = end
        while node != start:
            path.append(node)
            node = previous_nodes[node]
        path.append(start)
        print(" -> ".join(reversed(path)))
        print(f"The best path has a distance of {shortest_path[end]}.")

#example
nodes = ["A", "B", "C", "D", "E", "F", "G", "H"]

init_graph = {}
for node in nodes:
    init_graph[node] = {}
#manually initialize init_graph
init_graph["A"]["B"] = 5
init_graph["A"]["D"] = 4
init_graph["B"]["F"] = 1
init_graph["B"]["C"] = 3
init_graph["C"]["G"] = 5
init_graph["C"]["H"] = 4
init_graph["H"]["G"] = 1
init_graph["E"]["F"] = 2
init_graph["E"]["H"] = 2

graph = Graph(nodes, init_graph)
#call dijkstra and print result
previous_nodes, shortest_path = graph.dijkstra("A")
graph.print_result(previous_nodes, shortest_path, "A", "G")