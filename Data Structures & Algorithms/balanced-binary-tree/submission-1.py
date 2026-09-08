# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalanced = True
        def subtreeBalanced(root):
            nonlocal isBalanced
            if not root:
                return 0
            left = subtreeBalanced(root.left)
            right = subtreeBalanced(root.right)
            if abs(left - right) > 1:
                isBalanced = False
            return 1 + max(left, right)
        subtreeBalanced(root)
        return isBalanced