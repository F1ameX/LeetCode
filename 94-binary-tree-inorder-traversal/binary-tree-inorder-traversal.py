class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        
        def traversal(root: Optional[TreeNode]) -> None:
            if not root:
                return
            traversal(root.left)
            result.append(root.val)
            traversal(root.right)
        
        traversal(root)
        return result
