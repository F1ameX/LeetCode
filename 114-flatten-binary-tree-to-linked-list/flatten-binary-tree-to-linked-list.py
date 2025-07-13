# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        self.flatten(root.left)
        self.flatten(root.right)
        
        left = root.left
        right = root.right

        if left:
            root.right = left
            root.left = None

            current = root.right
            while current.right:
                current = current.right
            
            current.right = right
        