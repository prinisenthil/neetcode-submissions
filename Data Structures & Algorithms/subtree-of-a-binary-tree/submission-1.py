# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # 1. declare global tracking var
        # 2. traverse main tree until node matches subroot
        # 3. once subroot is found in tree, declare tracker as true 
        # 4. traverse left and right of tree and subtree and change tracker to false 
        # if nodes don't match
        # return tracker outside of helper func
        def checkSubtree(root, subRoot):
            if not root and not subRoot:
                return True
            if not root or not subRoot or root.val != subRoot.val:
                return False
            return checkSubtree(root.left, subRoot.left) and checkSubtree(root.right, subRoot.right)
        
        if not root:
            return False
        
        if checkSubtree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)





            
