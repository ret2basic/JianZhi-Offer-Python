# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # Linked List => List
        array = []
        current_node = head
        while current_node:
            array.append(current_node.val)
            current_node = current_node.next

        return array == array[::-1]

        # # Two Pointers
        # left_pointer = 0
        # right_pointer = len(array) - 1

        # while left_pointer < right_pointer:
        #     if array[left_pointer] != array[right_pointer]:
        #         return False
        #     left_pointer += 1
        #     right_pointer -= 1

        # return True