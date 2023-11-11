# Two Number Sum

![Two Number Sum](https://github.com/aaronespasa/competitive-programming/blob/main/Arrays/001.Two-Number-Sum/001.png)

Solution:

```py
def twoNumberSum(array, targetSum):
    targets = {}

    for num in array:
        if num in targets:
            return [num, targets[num]]

        targets[targetSum - num] = num

    return []
```

The `twoNumberSum` function has a time complexity of O(n) and a space complexity of O(n).

1. **Time Complexity**: The function iterates through each element of the array exactly once. During each iteration, it performs constant time operations: checking if an element exists in the `targets` dictionary and updating the dictionary. Accessing and inserting elements in a dictionary in Python are O(1) operations on average. Therefore, the overall time complexity of this function is O(n), where n is the number of elements in the array.

2. **Space Complexity**: The space complexity is primarily determined by the `targets` dictionary that stores elements from the array. In the worst case, if no two numbers sum up to the `targetSum`, the function will end up storing almost every element from the array in the dictionary (specifically, all elements except the last one). Therefore, the space complexity is O(n), where n is the number of elements in the array.

