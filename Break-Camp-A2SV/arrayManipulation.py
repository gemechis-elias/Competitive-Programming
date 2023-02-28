def arrayManipulation(n, queries):
    # Initialize array with zeros
    arr = [0] * n

    # Perform operations
    for query in queries:
        a, b, k = query
        arr[a-1] += k
        if b < n:
            arr[b] -= k

    # Find maximum value
    max_value = 0
    running_sum = 0
    for i in range(n):
        running_sum += arr[i]
        max_value = max(max_value, running_sum)

    return max_value
