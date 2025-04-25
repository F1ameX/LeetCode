# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        last = head
        size = 1

        while last.next:
            last = last.next
            size += 1

        k = k % size
        if k == 0:
            return head

        current = head
        for i in range(size - k - 1):
            current = current.next
        result = current.next
        current.next = None
        last.next = head

        return result