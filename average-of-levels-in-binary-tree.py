# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        res = []
        queue = deque([root])
        while queue:
            total, count = 0, 0
            temp = deque([])
            while queue:
                node = queue.popleft()
                total += node.val
                count += 1
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            queue = temp
            res.append(total / count)
        return res