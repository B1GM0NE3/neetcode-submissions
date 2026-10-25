# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        new_head, curr, cnt = head, head, 1
        while curr:
            curr = curr.next
            if curr:
                cnt += 1

        remove = cnt - n
        if remove == 0:
            return head.next
        i = 0
        while True:
            if i == remove - 1:
                head.next = head.next.next
                return new_head
            head = head.next
            i += 1
            
            
            
        





