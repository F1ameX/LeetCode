# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getNode(self, current, k):
        while current and k > 0:
            current = current.next
            k -= 1
        return current

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        checker = dummy

        while True:
            node = self.getNode(checker, k)
            if not node:
                break
            
            nodeNext = node.next
            previous, current = node.next, checker.next

            while current != nodeNext:
                temp = current.next
                current.next = previous
                previous = current
                current = temp
            
            temp = checker.next
            checker.next = node
            checker = temp
        
        return dummy.next