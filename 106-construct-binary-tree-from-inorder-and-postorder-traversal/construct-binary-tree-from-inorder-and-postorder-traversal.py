# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        mapping = {}
        
        for i in range(len(inorder)):
            mapping[inorder[i]] = i
        
        postorder = deque(postorder[::-1])

        def build(start : int, end : int) -> Optional[TreeNode]:
            if start > end: return None

            root = TreeNode(postorder.popleft())
            mid = mapping[root.val]
            root.right = build(mid + 1, end)
            root.left = build(start, mid - 1)
            return root
        
        return build(0, len(postorder) - 1)
        