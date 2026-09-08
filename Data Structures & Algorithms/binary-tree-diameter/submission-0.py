# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = 0
        def getHeight(node):
            nonlocal maxDiameter
            if not node:
                return 0
            leftHeight = getHeight(node.left)
            rightHeight = getHeight(node.right)
            diameter = leftHeight + rightHeight
            if diameter > maxDiameter:
                maxDiameter = diameter
            return 1 + max(leftHeight, rightHeight)
        getHeight(root)
        return maxDiameter