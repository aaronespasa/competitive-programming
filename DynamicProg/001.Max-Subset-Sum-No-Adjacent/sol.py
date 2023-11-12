def maxSubsetSumNoAdjacent(array):
    if len(array) < 2: # return 0 if emtpy, array[0] if len = 1
        return sum(array)
    
    prev, curr = array[0], max(array[0], array[1])

    for num in array[2:]: # max(cumVals[i - 2] + array[i], cumVals[i-1])
        prev, curr = curr, max(prev + num, curr)
    
    return curr