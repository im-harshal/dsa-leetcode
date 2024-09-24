from collections import deque

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

def bfs(graph, start) :
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')

        for x in graph[vertex]:
            if x not in visited:
                visited.add(x)
                queue.append(x)

print("BFS starting from vertex A :")
bfs(graph, 'A')