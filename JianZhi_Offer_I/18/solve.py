# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        original = head

        # When the first item == target
        if head.val == val:
            return head.next

        # Otherwise
        while head.next:
            if head.next.val == val:
                head.next = head.next.next
                return original
            head = head.next
        
        return original
