# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        """BFS"""

        if not root:
            return 0

        queue = collections.deque()
        queue.append(root)
        count = 0

        while queue:
            level = collections.deque()
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            queue = level
            count += 1

        return count
        
