# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getKth(self, node: ListNode, k: int):
        while node and k > 0:
            node = node.next
            k -= 1
        return node
        
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            curr = groupPrev.next
            prev = kth.next
            while curr != groupNext:
                nextNode = curr.next
                curr.next = prev
                prev = curr
                curr = nextNode
            
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        
        return dummy.next
