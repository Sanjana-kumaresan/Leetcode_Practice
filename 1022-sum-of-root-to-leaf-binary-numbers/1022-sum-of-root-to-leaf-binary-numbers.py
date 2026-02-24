class Solution(object):
    def sumRootToLeaf(self, root):
        def magic(root, pathsum):
			if not root:
				return 0
			pathsum += str(root.val)
			if not root.right and not root.left:
				return int(pathsum, 2)
			return magic(root.left, pathsum) + magic(root.right, pathsum)
	return magic(root, '')