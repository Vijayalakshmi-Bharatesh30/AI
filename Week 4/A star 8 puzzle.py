
import heapq

GOAL = (1, 2, 3,
        8, 0, 4,
        7, 6, 5)


def heuristic(state):
    distance = 0

    for i, tile in enumerate(state):
        if tile != 0:
            goal_index = GOAL.index(tile)
            row, col = divmod(i, 3)
            goal_row, goal_col = divmod(goal_index, 3)
            distance += abs(row - goal_row) + abs(col - goal_col)

    return distance


def get_neighbors(state):
    neighbors = []
    blank = state.index(0)
    row, col = divmod(blank, 3)

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:
        nr, nc = row + dr, col + dc

        if 0 <= nr < 3 and 0 <= nc < 3:
            new_blank = nr * 3 + nc
            board = list(state)
            board[blank], board[new_blank] = board[new_blank], board[blank]
            neighbors.append(tuple(board))

    return neighbors


def is_solvable(state):
    start_tiles = [x for x in state if x != 0]
    goal_tiles = [x for x in GOAL if x != 0]
    goal_order = {tile: index for index, tile in enumerate(goal_tiles)}
    sequence = [goal_order[tile] for tile in start_tiles]

    inversions = sum(
        sequence[i] > sequence[j]
        for i in range(len(sequence))
        for j in range(i + 1, len(sequence))
    )

    return inversions % 2 == 0


def a_star(start):
    open_set = [(heuristic(start), 0, start)]
    came_from = {}
    g_score = {start: 0}

    while open_set:
        f, g, current = heapq.heappop(open_set)

        if g != g_score.get(current):
            continue

        if current == GOAL:
            path = [current]

            while current in came_from:
                current = came_from[current]
                path.append(current)

            path.reverse()

            for step, state in enumerate(path):
                g_n = step
                h_n = heuristic(state)
                f_n = g_n + h_n

                print(f"Step {step}:")
                print_board(state)
                print(f"g(n) = {g_n}")
                print(f"h(n) = {h_n}")
                print(f"f(n) = {f_n}")
                print()

            return path

        for neighbor in get_neighbors(current):
            tentative_g = g + 1

            if tentative_g < g_score.get(neighbor, float("inf")):
                g_score[neighbor] = tentative_g
                came_from[neighbor] = current
                f_score = tentative_g + heuristic(neighbor)
                heapq.heappush(open_set, (f_score, tentative_g, neighbor))

    return None


def print_board(state):
    for i in range(0, 9, 3):
        print(" ".join(
            "_" if tile == 0 else str(tile)
            for tile in state[i:i + 3]
        ))
    print()


print("Enter the initial 8-puzzle state row by row.")
print("Use 0 for the blank space.")

try:
    values = []

    for i in range(3):
        row = list(map(int, input(f"Enter row {i + 1}: ").split()))

        if len(row) != 3:
            raise ValueError("Each row must contain exactly 3 numbers.")

        values.extend(row)

    start = tuple(values)

    if sorted(start) != list(range(9)):
        raise ValueError("Enter each number from 0 to 8 exactly once.")

    print("\nInitial state:")
    print_board(start)

    print("Goal state:")
    print_board(GOAL)

    if not is_solvable(start):
        print("This puzzle cannot reach the specified goal state.")
    else:
        solution = a_star(start)

        if solution:
            print("Solution found!")
            print("Minimum number of moves:", len(solution) - 1)
        else:
            print("No solution found.")

except ValueError as error:
    print("Invalid input:", error)



   