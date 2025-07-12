# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        self.dfs(root, targetSum, 0, result, [])
        return result
    
    def dfs(self, root: Optional[TreeNode], targetSum: int, current: int, result: List[List[int]], path: List[int]) -> None:
        if not root:
            return
        current += root.val
        path.append(root.val)
        if not root.left and not root.right and current == targetSum:
            result.append(list(path))

        self.dfs(root.left, targetSum, current, result, path)
        self.dfs(root.right, targetSum, current, result, path)
        path.pop()        