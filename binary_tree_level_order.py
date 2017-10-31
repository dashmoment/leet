class treenode:
    def __init__(self, val):
            self.val = val
            self.right = None
            self.left = None


class build_tree_from_lists:
    def add_node(self,root, node_val):

        if node_val <= root.val :
            if not root.left: root.left = treenode(node_val)
            else: self.add_node(root.left, node_val)
        elif node_val > root.val :
            if not root.right: root.right = treenode(node_val)
            else: self.add_node(root.right, node_val)
    
    def build_tree_from_list(self , lists):
        
        assert len(lists) > 0, "Lists shall contain more than one elements"
        root = treenode(lists[0])
        for i in range(1,len(lists)):
            self.add_node(root, lists[i])

        return root
    def dfs_print_tree(self, root):

        res = []
        stack = [(root, "")]

        while stack:
            node, print_str = stack.pop()

            if not node.right and not node.left:
                res.append(print_str  + str(node.val))
            if node.right:
                stack.append((node.right, print_str+ str(node.val) + "->"))
            if node.left:
                stack.append((node.left, print_str+ str(node.val)+"->"))

        return res

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        path = []
        queue = [root]

        while queue:
            node = queue[0]
            del queue[0]

        if not node.left and node.right:
            path.append(node.val)
            path.append(None)
            path.append(None)
            
        if node.left:
            queue.append[node.left]
        if node.right:
            queue.append[node.right]
            node.append(node.val)

            
tree = build_tree_from_lists()
t = tree.build_tree_from_list([3,2,5,4,6, null, null])

s = Solution()
print(s.levelOrder(t))

            
                

            





        
