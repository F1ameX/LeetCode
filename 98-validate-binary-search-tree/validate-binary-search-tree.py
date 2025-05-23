class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_valid(node: Optional[TreeNode], minimum: int, maximum: int) -> bool:
            if not node:
                return True
            
            if not (node.val > minimum and node.val < maximum):
                return False
            
            return is_valid(node.left, minimum, node.val) and is_valid(node.right, node.val, maximum)
        
        return is_valid(root, float("-inf"), float("inf"))