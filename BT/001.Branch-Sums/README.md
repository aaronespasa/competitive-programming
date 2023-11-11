# Binary Trees Branch Sums

![Binary Trees Branch Sums](https://github.com/aaronespasa/competitive-programming/blob/main/BT/001.Branch-Sums/001.png)

Solution:

```py
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    result = []
    fillBranchSums(root, 0, result)
    return result

def fillBranchSums(node, curr_sum, result):
    if node is None:
        return

    curr_sum += node.value

    # check if it's a leaf
    if node.left is None and node.right is None:
        result.append(curr_sum)
        return
    
    fillBranchSums(node.left, curr_sum, result)
    fillBranchSums(node.right, curr_sum, result)
```

The `branchSums` function calculates the sum of values from the root to each leaf in a binary tree. Here's an analysis of its time and space complexities:

1. **Time Complexity**:
   - The function traverses each node in the binary tree exactly once.
   - The number of operations for each node is constant, as the function performs a fixed set of operations (addition, comparison, and method calls).
   - Therefore, the time complexity is O(n), where n is the number of nodes in the tree. This is because each node is visited once.

2. **Space Complexity**:
   - The space complexity is influenced by two factors: the space needed for the result list and the space used by the call stack due to recursion.
   - The result list will contain as many elements as there are leaf nodes in the tree. In the worst case, a binary tree can have up to n/2 leaves (consider a complete binary tree), so the space needed for the result list is O(n).
   - The space used by the call stack in recursion depends on the height of the tree. In the best case (a balanced tree), the height is log(n), leading to a space complexity of O(log(n)). In the worst case (a skewed tree), the height is n, leading to a space complexity of O(n).
   - Combining these factors, the overall space complexity is O(n) because the size of the result list (which is dependent on the number of leaf nodes) becomes the dominating factor in the space complexity.
