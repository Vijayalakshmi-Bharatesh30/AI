

GOAL = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]
MOVES = [
    (-1, 0, "Up"),
    (1, 0, "Down"),
    (0, -1, "Left"),
    (0, 1, "Right")
]
def print_grid(grid):
    for row in grid:
        print(" ".join("_" if x == 0 else str(x) for x in row))
    print()

def find_blank(grid):
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 0:
                return i, j

def is_goal(grid):
    return grid == GOAL

def dfs_backtracking(grid, visited, path):

   
    if is_goal(grid):
        return True

    x, y = find_blank(grid)

    for dx, dy, move in MOVES:

        nx = x + dx
        ny = y + dy

        
        if 0 <= nx < 3 and 0 <= ny < 3:

            
            grid[x][y], grid[nx][ny] = \
                grid[nx][ny], grid[x][y]

            state = tuple(tuple(row) for row in grid)

            
            if state not in visited:

                visited.add(state)
                path.append(move)

                print("Move:", move)
                print_grid(grid)

                
                if dfs_backtracking(grid, visited, path):
                    return True

               
                path.pop()

                grid[x][y], grid[nx][ny] = \
                    grid[nx][ny], grid[x][y]

                print("Backtracking...")
                print_grid(grid)

            else:
                
                grid[x][y], grid[nx][ny] = \
                    grid[nx][ny], grid[x][y]

    return False
start = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

print("INITIAL STATE:")
print_grid(start)

start_state = tuple(tuple(row) for row in start)

visited = {start_state}
path = []

if dfs_backtracking(start, visited, path):

    print("GOAL FOUND!")
    print()
    print("Moves:")
    print(" -> ".join(path))

    print()
    print("FINAL GOAL STATE:")
    print_grid(start)

else:

    print("No solution found.")
