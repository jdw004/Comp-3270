from collections import deque
import time

# DFS Iterative
def dfs(start, end):
    if end not in adj:
        print(f"Not possible")
        return -1
    
    visited = set()
    stack = [start]
    visited.add(start)
    
    while stack:
        node = stack.pop()
        
        if node == end:
            return len(visited)
        
        if node in adj:
            for neighbor in reversed(adj[node]):
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
    
    return len(visited)

# BFS Iterative
def bfs(start, end):
    if end not in adj:
        print(f"Not posible")
        return -1
    
    q = deque([start])
    visited = set([start])
    
    while q:
        node = q.popleft()
        if node == end:
            return len(visited)
        
        # Check neighbors
        if node in adj:  
            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)
    
    return len(visited)

# Read input from file
inputs = []
with open("/Users/johnwelch/Downloads/Test_Case_Assignment2.txt", "r") as file:
    for line in file:
        node1, node2 = line.strip().split(",")
        inputs.append((node1, node2))

# Build the graph as a dictionary with each node and its connections
adj = {}
for x, y in inputs:
    if x in adj:
        adj[x].append(y)
    else:
        adj[x] = [y]
    if y in adj:
        adj[y].append(x)
    else:
        adj[y] = [x]


#Testing 
# DFS
startTime = time.perf_counter_ns()
visited_nodes_dfs = dfs("N_0", "N_24")
endTime = time.perf_counter_ns()
dfsTime = endTime - startTime
dfsTimeMs = round((dfsTime / 1_000_000),4)

# BFS
startTimeTwo = time.perf_counter_ns()
visited_nodes_bfs = bfs("N_0", "N_24")
endTimeTwo = time.perf_counter_ns()
bfsTime = endTimeTwo - startTimeTwo
bfsTimeMs = round((bfsTime / 1_000_000),4)

print("Nodes Visited (BFS):", visited_nodes_bfs)
print("BFS Runtime (milliseconds):", bfsTimeMs)
print("Nodes Visited (DFS):", visited_nodes_dfs)
print("DFS Runtime (milliseconds):", dfsTimeMs)
