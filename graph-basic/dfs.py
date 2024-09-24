graph = {
    'A': ['B','C'],
    'B': ['D'],
    'C': ['E','F'],
    'D': [],
    'E': ['G','H'],
    'F': [],
    'G': [],
    'H': []
}

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(start)
    print(start, end=' ')

    for x in graph[start]:
        if x not in visited:
            dfs(graph, x, visited)

print("DFS starting from vertex A")
dfs(graph, 'A')