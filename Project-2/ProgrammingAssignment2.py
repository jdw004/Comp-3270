from collections import deque

def bfs(start, finish):
    q = deque()
    q.append((start, 0))
    visited = set()

    while q:
        node, length = q.popleft()
        visited.add(node)
        if node == finish:
            return length
        
        #Check neighbors
        if node in adj:
            for new in adj[node]:
                if new not in visited:
                    q.append((new, length + 1))
    return -1

def dfs(start, finish, length, visited):
    visited.add(start)
    if start == finish:
        return length

    for neighbor in adj[start]:
        if neighbor not in visited:
            result = dfs(neighbor, finish, length + 1, visited)
            if result is not None:
                return result
    return None

# Read inputs
inputs = []
with open("/Users/johnwelch/Downloads/Test_Case_Assignment2.txt", "r") as file:
    for line in file:
        node1, node2 = line.strip().split(",")
        inputs.append((node1, node2))

# Set up our graph
# Make a dictionary with key as node and values as connections
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

# Run BFS/DFS
visited = set()
print(dfs("N_0","N_10",0,set()))