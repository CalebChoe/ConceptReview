
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')

    for neighbor in graph[start] - visited:
        dfs(graph, neighbor, visited)

graph = {'A': {'B', 'C'},
         'B': {'A', 'D', 'E'},
         'C': {'A', 'F', 'G'},
         'D': {'B'},
         'E': {'B'},
         'F': {'C'},
         'G': {'C'}}

print("DFS traversal:")
dfs(graph, 'A')
