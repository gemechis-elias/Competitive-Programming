# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        ans = []
        queue = deque([root])

        while queue:
            _sum = 0
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                _sum += node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            ans.append(_sum / size)

        return ans