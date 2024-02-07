def isValidSubsequence(array, sequence):
    idx = 0
    for num in array:
        if num == sequence[idx]:
            idx += 1
        if idx == len(sequence):
            return True

    return False