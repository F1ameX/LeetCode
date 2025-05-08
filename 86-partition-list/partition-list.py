# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left = ListNode()
        right = ListNode()
        l_current, r_current = left, right

        while head:
            if head.val < x:
                l_current.next = head
                l_current = l_current.next
            else:
                r_current.next = head
                r_current = r_current.next
    
            head = head.next
        
        l_current.next = right.next
        r_current.next = None
        return left.next