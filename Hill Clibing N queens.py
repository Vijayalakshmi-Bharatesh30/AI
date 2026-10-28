
def cost(state):
    n = len(state)
    conflicts = 0
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1
    return conflicts


def show(state):
    n = len(state)
    for r in range(1, n + 1):
        print(" ".join("Q" if state[c] == r else "." for c in range(n)))


def neighbors(state):
    n = len(state)
    result = []
    for c in range(n):
        for r in range(1, n + 1):
            if r != state[c]:
                new_state = state.copy()
                new_state[c] = r
                result.append((c, r, new_state))
    return result


def hill_climbing(state):
    step = 0

    while cost(state) > 0:
        step += 1
        current_cost = cost(state)

        print("\n========== STEP", step, "==========")
        print("Current state:", state)
        print("Current cost:", current_cost)
        show(state)

        candidates = neighbors(state)
        best_state = None
        best_cost = current_cost

        print("\nAll neighboring states:")

        for col, row, neighbor in candidates:
            neighbor_cost = cost(neighbor)
            print("\nMove queen in column", col + 1, "to row", row)
            print("State:", neighbor)
            show(neighbor)
            print("Cost:", neighbor_cost)

            if neighbor_cost < best_cost:
                best_cost = neighbor_cost
                best_state = neighbor

        if best_state is None:
            print("\nLocal minimum reached.")
            print("Restarting with a new initial configuration.")
            state = [1, 2, 3, 4]
            if cost(state) >= current_cost:
                state = [4, 2, 1, 3]
            if cost(state) >= current_cost:
                state = [2, 4, 1, 3]
            if cost(state) >= current_cost:
                state = [3, 1, 4, 2]
            if cost(state) >= current_cost:
                print("Could not find an improving move.")
                return
        else:
            print("\nSelected best neighbor:", best_state)
            print("New cost:", best_cost)
            state = best_state

    print("\n========== GOAL REACHED ==========")
    print("Final state:", state)
    print("Final cost:", cost(state))
    show(state)


n = int(input("Enter number of queens: "))

if n != 4:
    print("Enter N = 4 for this observation.")
else:
    state = list(map(
        int,
        input("Enter row position of each queen (4 numbers): ").split()
    ))

    if len(state) != 4 or any(x < 1 or x > 4 for x in state):
        print("Invalid input. Enter 4 numbers between 1 and 4.")
    else:
        print("\nINITIAL BOARD")
        print("State:", state)
        print("Cost:", cost(state))
        show(state)
        hill_climbing(state)


