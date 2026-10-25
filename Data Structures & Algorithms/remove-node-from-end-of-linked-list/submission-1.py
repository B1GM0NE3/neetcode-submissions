# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
        
        remove = len(nodes) - n
        if remove == 0 and len(nodes) == 1:
            return
        elif remove == 0:
            return nodes[1] 
        else:
            if nodes[remove].next:
                nodes[remove-1].next = nodes[remove+1]
            else:
                nodes[remove-1].next = None
            return nodes[0]