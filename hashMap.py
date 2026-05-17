def two_sum_indexs(arr:list[int], targetNum:int) -> list[int]:
    result = [0, 1]
    length = len(arr)
    required = targetNum - arr[result[0]];
    index = 1;
    while result[1] < length - 1:
        if(arr[index] == required):
            result[1] = index
            return result

    return result