# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        taki, mitsuha = headA, headB
        
        # 君の名は
        while taki != mitsuha:
            taki = taki.next if taki else headB
            mitsuha = mitsuha.next if mitsuha else headA
        
        return mitsuha
