# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head
        dummy = second = ListNode(-1, head)
        i = 0
        while first:
            if i >= n:
                second = second.next
            first = first.next
            i += 1
        
        second.next = second.next.next
        return dummy.next
