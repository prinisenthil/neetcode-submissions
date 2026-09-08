# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        isSame = True
        def isSameSubtree(p, q):
            nonlocal isSame
            # traverse through left and right
            if (not p and q) or (not q and p):
                isSame = False
                return
            if not p and not q:
                return
            # left subtree traversal
            isSameSubtree(p.left, q.left)
            # right subtree traversal
            isSameSubtree(p.right, q.right)
            # check if nodes match
            if p.val != q.val:
                isSame = False
        isSameSubtree(p, q)
        return isSame