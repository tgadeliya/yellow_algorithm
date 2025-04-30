from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # TODO: Use two pointers for O(1) memory
        d = {}
        d[-1] = ListNode(val=None, next=head)
        c = 0
        node = head
        while node:
            d[c] = node
            c += 1
            node = node.next
        
        idx_to_remove = c - n
        d[idx_to_remove - 1].next = d[idx_to_remove].next 
        
        return d[-1].next