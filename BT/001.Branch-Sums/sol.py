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