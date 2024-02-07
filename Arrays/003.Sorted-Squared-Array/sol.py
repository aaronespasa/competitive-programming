def sortedSquaredArray(array):
    # we know that they are storted
    # the ones that values that can have the greatest value
    # once they are squared are the first and the last one
    sequence = [0 for _ in range(len(array))]
    seq_idx = len(sequence) - 1
    ini_idx = 0
    end_idx = len(array) - 1
    
    while ini_idx <= end_idx:
        ini_val = abs(array[ini_idx])
        end_val = abs(array[end_idx])

        if ini_val >= end_val:
            sequence[seq_idx] = ini_val ** 2
            ini_idx += 1
        elif ini_val < end_val:
            sequence[seq_idx] = end_val ** 2
            end_idx -= 1
        seq_idx -= 1

    return sequence