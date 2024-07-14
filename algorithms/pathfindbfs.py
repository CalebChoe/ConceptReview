from collections import deque

def bfs(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    queue = deque([start])
    visited = set()
    visited.add(start)
    parent = {start: None}
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    while queue:
        current = queue.popleft()

        if current == goal:
            # Reconstruct the path from goal to start
            path = []
            while current:
                path.append(current)
                current = parent[current]
            path.reverse()
            return path

        for direction in directions:
            next_cell = (current[0] + direction[0], current[1] + direction[1])

            if 0 <= next_cell[0] < rows and 0 <= next_cell[1] < cols and \
                    next_cell not in visited and grid[next_cell[0]][next_cell[1]] == 0:
                queue.append(next_cell)
                visited.add(next_cell)
                parent[next_cell] = current

    return None  # No path found

grid = [
    [0, 0, 1, 0],
    [1, 0, 1, 0],
    [0, 0, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 0]
]

px, py = 4, 3
mx, my = 0, 0

path = bfs(grid, (mx, my), (px, py))
print("BFS Path:", path)
