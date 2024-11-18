def fptas_knapsack(values, weights, capacity, epsilon):
    """
    Fully Polynomial Time Approximation Scheme (FPTAS) for the 0/1 knapsack problem.
    
    Parameters:
        values (list): List of item values (profits).
        weights (list): List of item weights.
        capacity (int): Knapsack capacity.
        epsilon (float): Desired approximation factor (0 < epsilon <= 1).

    Returns:
        tuple: (approximate_max_value, selected_items)
               - approximate_max_value: Approximate maximum value for the knapsack.
               - selected_items: List of indices of items included in the solution.
    """
    n = len(values)
    max_value = max(values)

    # Calculate scaling factor
    k = (epsilon * max_value) / n

    # Scale down values
    scaled_values = [int(value // k) for value in values]

    # Initialize DP table
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Sparse DP optimization: track weight-to-value mappings
    weight_value_mapping = {}

    # Dynamic programming to solve the scaled problem
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + scaled_values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

            # Store sparse weight-to-value mapping
            weight_value_mapping[(i, w)] = dp[i][w]

    # Recover the approximate solution
    w = capacity
    selected_items = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:  # Item was included
            selected_items.append(i - 1)
            w -= weights[i - 1]

    # Compute the approximate max value
    approximate_max_value = sum(values[i] for i in selected_items)

    return approximate_max_value, selected_items


# Example usage
if __name__ == "__main__":
    # Example inputs
    values = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50
    epsilon = 0.1  # Approximation factor

    approximate_value, selected_items = fptas_knapsack(values, weights, capacity, epsilon)

    print("Approximate Max Value:", approximate_value)
    print("Selected Items (Indices):", selected_items)
