# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        deq = deque([root])
        
        while deq:
            result.append([elem.val for elem in list(deq)])
            for _ in range(len(deq)):
                pop = deq.popleft()
                if pop.left:
                    deq.append(pop.left)
                if pop.right:
                    deq.append(pop.right)
        return result[::-1]
        
        