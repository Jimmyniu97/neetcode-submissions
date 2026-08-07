# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def merge(self, l1, l2):
        dummyHead = ListNode(0,None)
        current = dummyHead
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        current.next = l1 if l1 else l2
        return dummyHead.next
    
    def mergeRange(self, lists, left, right):
        if left > right:
            return None
        if left == right:
            return lists[left]
        
        mid = (left+right) // 2
        leftPart = self.mergeRange(lists, left, mid)
        rightPart = self.mergeRange(lists, mid+1, right)
        return self.merge(leftPart, rightPart)

          
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        return self.mergeRange(lists, 0, len(lists)-1)
