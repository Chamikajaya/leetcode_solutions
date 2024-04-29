import heapq
from collections import defaultdict

def networkDelayTime(times, n,  k):  # k - start node
    
    graph = defaultdict(list)
    
    # creating the graph
    for node1, node2, cost in times:
        graph[node1].append((node2, cost))
        
    
    # initializing distances dict  
    distances = {node:float('inf') for node in range(1,n+1)}
    distances[k] = 0
    
    # min heap is needed to get the shortest distance node at each iteration
    min_heap = [(0, k)] # (distance, node)
    
    while min_heap:
        curr_dist, curr_node = heapq.heappop(min_heap)
        
        if curr_dist > distances[curr_node]:
            continue
        
        for neighbor, weight in graph[curr_node]:
            new_dist = weight + curr_dist
            
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(min_heap, (new_dist, neighbor))
        
    return max(distances.values()) if max(distances.values()) < float('inf') else -1
            
            
        
        
        
        

print(networkDelayTime(times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2))