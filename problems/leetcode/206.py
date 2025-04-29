from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        return f"Node(val={self.val})"

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:        
        # def rec(node: Optional[ListNode]):
        #     if node.next is None:
        #         return node

        #     res = rec(node.next) 
        #     nn = ListNode(node.val)
        #     res.next = nn
        #     return res

        # return rec(head)

        node = ListNode(val = head.val, next=None)
        while head.next is not None:
            node = ListNode(val = head.next.val, next=node)
            head = head.next
        return node

if __name__ == "__main__":
    sol = Solution()
    cases = [
        ([1,2,3], [3,2,1])
    ]
    for c, c_true in cases:
        cn = [ListNode(n) for n in c]
        for i in range(1, len(c)):
            cn[i-1].next = cn[i]

        cn_true = [ListNode(n) for n in c[::-1]]
        for i in range(1, len(c)):
            cn_true[i-1].next = cn_true[i]

        res = sol.reverseList(cn[0]) # Run solution func
        assert res == cn_true[0], f"{res} and {c_true}"
    print("Microtests passed!")