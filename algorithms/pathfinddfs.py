import random

def dfs(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    stack = [start]
    visited = set()
    parent = {start: None}

    # Directions for moving in the grid (right, down, left, up)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while stack:
        current = stack.pop()

        if current == goal:
            # Reconstruct the path from goal to start
            path = []
            while current:
                path.append(current)
                current = parent[current]
            path.reverse()
            return path

        if current not in visited:
            visited.add(current)

            for direction in directions:
                next_cell = (current[0] + direction[0], current[1] + direction[1])

                first = next_cell[0]
                second = next_cell[1]

                if 0 <= first < rows and 0 <= second < cols and next_cell not in visited:
                    if grid[first][second] == 0:
                        stack.append(next_cell)
                        parent[next_cell] = current

                elif grid[first][second] == 2:
                    num = random.randint(1, 3)
                    guess = input("Guess a number between 1 to 3: ")
                    if num==guess:
                        stack.append(next_cell)
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

path = dfs(grid, (mx, my), (px, py))
print("DFS Path:", path)

print()

grid = [
    [0, 0, 1, 0, 1, 0],
    [1, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 1, 0],
    [1, 0, 0, 1, 1, 0]
]

px, py = 7, 5
mx, my = 0, 3

path = dfs(grid, (mx, my), (px, py))
print("DFS Path:", path)

print()

grid = [
    [0, 0, 2, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 1],
    [0, 1, 1, 0, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 1, 1, 1, 0, 1],
    [0, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 1],
    [0, 1, 1, 0, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 1, 0, 1]
]

px, py = 7, 6
mx, my = 0, 0

path = dfs(grid, (mx, my), (px, py))
print("DFS Path:", path)
