# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = collections.deque()
        queue.append(root)

        depth = 1
        while queue:
            level = collections.deque()
            for _ in range(len(queue)):
                node = queue.popleft()
                # Odd level: left to right
                if depth % 2 != 0:
                    level.append(node.val)
                # Even level: right to left
                else:
                    level.appendleft(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(list(level))
            depth += 1

        return result