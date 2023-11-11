def twoNumberSum(array, targetSum):
    targets = {}

    for num in array:
        if num in targets:
            return [num, targets[num]]

        targets[targetSum - num] = num

    return []