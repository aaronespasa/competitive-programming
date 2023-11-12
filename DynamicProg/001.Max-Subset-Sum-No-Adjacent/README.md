# Max Subset Sum No Adjacent

![Max Subset Sum No Adjacent](https://github.com/aaronespasa/competitive-programming/blob/main/DynamicProg/001.Max-Subset-Sum-No-Adjacent/001.png)

Solution:

```py
def maxSubsetSumNoAdjacent(array):
    if len(array) < 2: # return 0 if emtpy, array[0] if len = 1
        return sum(array)
    
    prev, curr = array[0], max(array[0], array[1])

    for num in array[2:]: # max(cumVals[i - 2] + array[i], cumVals[i-1])
        prev, curr = curr, max(prev + num, curr)
    
    return curr
```

The `maxSubsetSumNoAdjacent` function calculates the maximum sum of non-adjacent elements in an array. Here's an analysis of its time and space complexities:

1. **Time Complexity**:
   - The function iterates through the input array once, starting from the third element (index 2).
   - Within each iteration, it performs a constant number of operations (calculations and comparisons).
   - Since the number of operations per element is constant and independent of the size of the input, the time complexity is O(n), where n is the length of the input array.

2. **Space Complexity**:
   - The function uses a fixed amount of extra space, irrespective of the input size. 
   - It only maintains two variables, `prev` and `curr`, for storing the maximum sums up to the current and previous positions in the array.
   - Since the amount of extra space used does not scale with the size of the input array, the space complexity is O(1), indicating constant space usage.
