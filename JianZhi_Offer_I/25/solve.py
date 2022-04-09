# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        current_node = sentinel = ListNode(0)

        while l1 and l2:
            if l1.val < l2.val:
                current_node.next, l1 = l1, l1.next
            else:
                current_node.next, l2 = l2, l2.next
            current_node = current_node.next
        current_node.next = l1 if l1 else l2
        
        return sentinel.next
