def max_cont_sum_subarray(arr: list[int], k: int) -> int:
    length = len(arr)
    if length < k | length == 0:
        return 0
    max_sum = sum(arr[:k])
    window_sum = max_sum;
    for i in range (k, length):
        window_sum += arr[i] - arr[i-k]
        if window_sum > max_sum:
            max_sum = window_sum

    return max_sum



print(max_cont_sum_subarray([2, 1, 6, 8, 4, 7, 3, 4], 3))