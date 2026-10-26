"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hash_table = defaultdict(lambda: Node(0))
        hash_table[None] = None

        curr = head
        while curr:
            hash_table[curr].val = curr.val
            hash_table[curr].next = hash_table[curr.next]
            hash_table[curr].random = hash_table[curr.random]
            curr = curr.next
        return hash_table[head]