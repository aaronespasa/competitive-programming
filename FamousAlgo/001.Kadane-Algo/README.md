# Kadane's Algorithm

![Kadane's Algorithm](https://github.com/aaronespasa/competitive-programming/blob/main/FamousAlgo/001.Kadane-Algo/001.png)

Solution:

```py
def kadanesAlgorithm(array):
    maxSum, curr = array[0], array[0]

    for num in array[1:]:
        curr = max(curr + num, num)
        maxSum = max(curr, maxSum)
    
    return maxSum
```

The `kadanesAlgorithm` function is an implementation of Kadane's Algorithm, which is used to find the maximum sum of a contiguous subarray within a one-dimensional array of numbers. Here's an analysis of its time and space complexities:

1. **Time Complexity**:
   - The function iterates through the input array once, starting from the second element.
   - In each iteration, it performs a constant number of operations: calculating the maximum of the current sum and the current number, and then updating the maximum sum if needed.
   - Since the number of operations for each element in the array is constant, and the array is traversed once, the time complexity is O(n), where n is the length of the input array.

2. **Space Complexity**:
   - The function uses a fixed amount of extra space. 
   - It maintains two variables, `maxSum` and `curr`, for keeping track of the maximum sum of any subarray found so far and the maximum sum of the subarray ending at the current position, respectively.
   - As the amount of extra space used does not scale with the size of the input array, the space complexity is O(1), indicating constant space usage.