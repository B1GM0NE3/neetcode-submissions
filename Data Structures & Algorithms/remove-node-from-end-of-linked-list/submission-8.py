# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr, cnt = head, 1
        while curr:
            curr = curr.next
            if curr:
                cnt += 1

        remove_index = cnt - n
        if remove_index == 0:
            return head.next

        curr = head
        for i in range(cnt - 1):
            if i + 1 == remove_index:
                curr.next = curr.next.next
                return head
            curr = curr.next
            
            
            
        





