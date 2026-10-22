# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curri, currj = list1, list2

        if not curri:
            return currj
        
        if not currj:
            return curri
        
        if curri.val <= currj.val:
            newHead = curri
            prev = list1
            curri = curri.next
        else:
            newHead = currj
            prev = list2
            currj = currj.next

        while curri and currj:
            if curri.val < currj.val:
                prev.next = curri
                curri = curri.next
            else:
                prev.next = currj
                currj = currj.next
            prev = prev.next
            
        while curri:
            prev.next = curri
            curri = curri.next
            prev = prev.next
        
        while currj:
            prev.next = currj
            currj = currj.next
            prev = prev.next

        return newHead




        