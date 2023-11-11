# BST Closest Value

![BST Closest Value](https://github.com/aaronespasa/competitive-programming/blob/main/BST/001.Closest-Value/001.png)

Solution:

```py
def findClosestValueInBst(tree, target):
	return findClosestValueInBstHelper(tree, target, tree.value)
		
def findClosestValueInBstHelper(tree, target, closest):
	if tree is None:
		# if some branch is None, this will return the closest number
		return closest
	
	if abs(target - closest) > abs(target - tree.value):
		# if the distance between the target and the actual tree value is
		# smaller than the previous distances, modify closest
		closest = tree.value
	
	if tree.value > target:
		return findClosestValueInBstHelper(tree.left, target, closest)
	elif tree.value < target:
		return findClosestValueInBstHelper(tree.right, target, closest)
	else: # tree.value == target
		return closest
	
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
```

The `findClosestValueInBst` function is designed to find the closest value to a given target in a Binary Search Tree (BST). Here's an analysis of its time and space complexities:

1. **Time Complexity**:
   - In the best-case scenario, particularly when the BST is balanced, the time complexity is O(log n), where n is the number of nodes in the tree. This is because, in a balanced BST, the function makes a decision at each level of the tree's height, which is about log n.
   - In the worst-case scenario, especially when the BST is unbalanced and resembles a linked list (i.e., every node has only one child), the time complexity becomes O(n). This happens when the function has to visit each node in the tree.

2. **Space Complexity**:
   - The space complexity is influenced by the recursive calls that the function makes, which are stored in the call stack.
   - In a balanced BST, the space complexity is O(log n), corresponding to the height of the tree, since the recursive calls go as deep as the tree's height.
   - In the worst-case scenario with an unbalanced tree, the space complexity could reach O(n) if the tree's shape is like a straight line, where the height is equal to n.
