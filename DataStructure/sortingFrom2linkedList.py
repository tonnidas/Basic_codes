# Problem: https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    root = ListNode(0, None)
    
    def dfs(self, node1, node2):
        if not node1 and node2:
            self.root.next = node2
            return
        elif node1 and not node2: 
            self.root.next = node1
            return 
        elif not node1 and not node2:
            return 
        else:
            if node1.val == node2.val:
                self.root.next = ListNode(node1.val, None)
                self.root.next.next = ListNode(node2.val, None)
                self.root = self.root.next.next
                self.dfs(node1.next, node2.next)

            if node1.val > node2.val:
                self.root.next = ListNode(node2.val, None)
                self.root = self.root.next 
                self.dfs(node1, node2.next)

            if node1.val < node2.val:
                self.root.next = ListNode(node1.val, None)
                self.root = self.root.next 
                self.dfs(node1.next, node2)
            
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        self.root = ListNode(0, None)
        temp = self.root 
        self.dfs(list1, list2)    
            
        return temp.next