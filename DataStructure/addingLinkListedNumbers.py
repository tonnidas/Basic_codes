# Problem: https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    r = ListNode(-1, None)
            
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        self.r = ListNode(-1, None)
        sumheadPointer, v, tail = self.r, 0, ListNode(-1, None)
        
        while True:
            if not l1 and not l2 and v==0:
                break
            v1, v2 = 0, 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            else:
                l1 = None
            if l2:
                v2 = l2.val
                l2 = l2.next
            else:
                l2 = None

            t = v1 + v2 + v
            self.r.val = t % 10
            v = t // 10
            tail = self.r
            self.r.next = ListNode(-1, None)
            self.r = self.r.next
            
        tail.next = None
        return sumheadPointer