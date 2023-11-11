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