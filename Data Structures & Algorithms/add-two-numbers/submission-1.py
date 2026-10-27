# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        new_dummy = dummy = ListNode(0)
        tmp = 0
        while l1 and l2:
            summ = l1.val + l2.val + tmp
            tmp = 1 if summ > 9 else 0
            dummy.val = summ % 10
            if l1.next or l2.next:
                dummy.next = ListNode(0) 
                dummy = dummy.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            summ = l1.val + tmp
            tmp = 1 if summ > 9 else 0
            dummy.val = summ % 10
            if l1.next:
                dummy.next = ListNode(0)
                dummy = dummy.next
            l1 = l1.next
        
        while l2:
            summ = l2.val + tmp
            tmp = 1 if summ > 9 else 0
            dummy.val = summ % 10
            if l2.next:
                dummy.next = ListNode(0)
                dummy = dummy.next
            l2 = l2.next
        
        if tmp > 0:
            dummy.next = ListNode(tmp)
            dummy = dummy.next
        
        dummy.next = None

        return new_dummy
            
            
