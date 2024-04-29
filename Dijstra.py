import heapq
from collections import defaultdict

def dijkstra_algo(graph, source, target ):
    
    # initialize the distances dict with vertex:infinity but source:0
    distances = {vertex:float('inf') for vertex in graph}
    distances[source] = 0
    
    # add the source vertex and distance to the min-heap
    pq = [(0, source)]
    
    # previous dict -> to store the previous node in the shortest path for each node.
    previous = {node:None for node in graph}
    
    # as long as min heap is not empty
    while pq:
        
        # pop the smallest distance node from min-heap 
        # In each iteration, the node with the smallest distance (closest to the starting node) is dequeued from the priority queue 
        curr_distance, curr_node = heapq.heappop(pq)
        
        # checks if the current distance is greater than the stored distance for the current node. If it is, it means that a shorter path has already been found, so the algorithm skips this node and moves to the next iteration using the 'continue' statement
        if distances[curr_node] < curr_distance:
            continue
        
        # if curr_distance is less than the one in distances dict
        # Here  the distances for neighboring nodes are updated.
        
        # For each neighbor of the current node, the algorithm calculates the tentative distance (the sum of the current distance and the weight of the edge connecting the current node and the neighbor).
        
        # If the tentative distance is smaller than the stored distance for the neighbor, it updates the distance in the 'distances' dictionary and adds the neighbor to the priority queue with the updated distance
        for neighbor, cost in graph[curr_node].items():
            new_distance = cost + curr_distance
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                
                # when we find a shorter distance to a neighbor, update the previous dictionary with the current node as the previous node in the shortest path to that neighbor.
                previous[neighbor] = curr_node
                
                
                heapq.heappush(pq, (new_distance, neighbor) ) 
        
    print (distances)
    
    path = []
    node = target
    
    while node is not None:
        path.append(node)
        node = previous[node]
        
    # now we have to reverse the list 
    path.reverse()
    
    if path[0] == source:
        print("Shortest path is : " + " -> ".join(path) )
    else:
        print("No such path exists between the source and the target")
        
        
    



graph = {
    'A': {'B': 2, 'D': 8},
    'B': {'A': 2, 'D': 5, 'E': 6},
    'C': {'E': 9, 'F': 3},
    'D': {'A': 8, 'B': 5, 'E': 3, 'F': 2},
    'E': {'B': 6, 'C': 9, 'D': 3, 'F' :1},
    'F': {'C': 3, 'D': 2, 'E': 1}
}

dijkstra_algo(graph, 'A', 'C')