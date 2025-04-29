from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(val=None)
        head = res 
        while list1 is not None or list2 is not None:
            if list1 is None:
                res.next = ListNode(list2.val,)
                res = res.next
                list2 = list2.next
            elif list2 is None:
                res.next = ListNode(list1.val)
                res = res.next
                list1 = list1.next
            else:
                if list1.val < list2.val:
                    res.next = ListNode(val=list1.val)
                    res = res.next
                    list1 = list1.next
                else:
                    res.next = ListNode(val=list2.val)
                    res = res.next            
                    list2 = list2.next
        
        return head.next