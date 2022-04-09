# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        # Initialize slow pointer and fast pointer
        slow, fast = head, head
        # Advance fast pointer for k steps
        for _ in range(k):
            fast = fast.next

        while fast:
            slow, fast = slow.next, fast.next
        
        return slow
