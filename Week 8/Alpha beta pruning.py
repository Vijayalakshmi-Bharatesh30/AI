def alphabeta(depth, node, maximizing, values, alpha, beta, max_depth):
    if depth == max_depth:
        return values[node]

    if maximizing:
        best = float('-inf')
        for i in range(2):
            val = alphabeta(depth + 1, node * 2 + i, False, values, alpha, beta, max_depth)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = float('inf')
        for i in range(2):
            val = alphabeta(depth + 1, node * 2 + i, True, values, alpha, beta, max_depth)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

values = list(map(int, input("Enter leaf node values: ").split()))
n = len(values)

if n == 0 or n & (n - 1):
    print("Enter a power-of-2 number of leaf values")
else:
    max_depth = n.bit_length() - 1
    result = alphabeta(0, 0, True, values, float('-inf'), float('inf'), max_depth)
    print("Optimal value:", result)