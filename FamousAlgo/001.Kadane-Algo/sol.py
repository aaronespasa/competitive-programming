def kadanesAlgorithm(array):
    maxSum, curr = array[0], array[0]

    for num in array[1:]:
        curr = max(curr + num, num)
        maxSum = max(curr, maxSum)
    
    return maxSum