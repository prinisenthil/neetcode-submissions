# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        val = None
        def checkSubtrees(root, p, q):
            nonlocal val
            if not root:
                return
            if (p >= root.val and q <= root.val) or (p <= root.val and q >= root.val):
                val = root
                return
            checkSubtrees(root.left, p, q)
            checkSubtrees(root.right, p, q)
        checkSubtrees(root, p.val, q.val)
        return val
            