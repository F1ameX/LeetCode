# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.flag = True
    def check(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.check(root.left)
        right = self.check(root.right)
        if abs(left - right) > 1:
            self.flag = False
        return 1 + max(left, right)
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        self.check(root)
        if self.flag:
            return True
        return False
        
        