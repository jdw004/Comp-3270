from collections import deque

# DFS
def dfs(start, end, visited):
    visited.add(start)
    if start == end:
        return len(visited)
    
    #Visit neighbors
    if start in adj: 
        for neighbor in adj[start]:
            if neighbor not in visited:
                result = dfs(neighbor, end, visited)
                if result:
                    return result
    return len(visited)

# BFS Iterative
def bfs(start, end):
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


#Testing here
visited_nodes = dfs("N_0", "N_10", set())
print("Nodes Visited (DFS):", visited_nodes)
visited_nodes = bfs("N_0", "N_10")
print("Nodes Visited (BFS):", visited_nodes)
