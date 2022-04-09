# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        result = []
        p = head
        while p:
            result.append(p.val)
            p = p.next
        
        return result[::-1]
