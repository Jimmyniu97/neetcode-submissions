# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        l1 = head
        l2_head = slow.next
        slow.next = None
        prev = None
        while l2_head:
            nextNode = l2_head.next
            l2_head.next = prev
            prev = l2_head
            l2_head = nextNode

        l2 = prev
        while l1 and l2:
            l1Next = l1.next
            l2Next = l2.next
            l1.next = l2
            if l1Next:
                l2.next = l1Next
            l1 = l1Next
            l2 = l2Next


        