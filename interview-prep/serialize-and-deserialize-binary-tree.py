# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        queue = deque([root])
        temp = []
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                
                if node:
                    temp.append(node.val)
                else:
                    temp.append(node)

                if node:
                    queue.append(node.left)
                    queue.append(node.right)

        return ','.join([str(x) for x in temp])

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        values = data.split(",")
        if values[0] == 'None':
            return None
            
        root = TreeNode(int(values[0]))
        queue = deque([root])

        i = 1
        while queue:
            node = queue.popleft()
            if values[i] != 'None':
                left = TreeNode(int(values[i]))
                node.left = left
                queue.append(left)
            i += 1

            if values[i] != 'None':
                right = TreeNode(int(values[i]))
                node.right = right
                queue.append(right)
            i += 1

        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))