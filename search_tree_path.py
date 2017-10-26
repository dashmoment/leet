class treenode:
    def __init__(self, val):
            self.val = val
            self.right = None
            self.left = None

class solution:
    def searchpath(self, root):

        stack = [(root, "")]
        res = []

        while stack:
            node, ls = stack.pop()

            if not node.right and not node.left:
                res.append(ls + "->" + str(node.val))
            if node.right:
                stack.append((node.right, ls + "->"+node.val))
            if node.left:
                stack.append((node.left, ls+"->"+node.val))
        return res

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
    
    def bfs_print_tree(self, root):

        res = []
        queue = [(root, "")]

        while queue:
            node, print_str = queue[0]
            del queue[0]

            if not node.right and not node.left:
                res.append(print_str  + str(node.val))
            if node.right:
                queue.append((node.right, print_str+ str(node.val) + "->"))
            if node.left:
                queue.append((node.left, print_str+ str(node.val)+"->"))

        return res

    def delete(self, head, root, nodeval):

        head = root
        head_father = root
        tag = "None"
        while nodeval != head.val:
            head_father = head
            if nodeval <= root.val and head.left:         
                head = head.left
            elif nodeval > root.val and head.right: 
                head = head.right
            else: 
                print("Node not found")
                return
        
        if head.val > head_father.val and 
            if head.right:
                head_father.right = head.right
                head.right.left = head.left 
            elif head.left:
                head_father.right = head.left 











bt = build_tree_from_lists()
tree = [5,2,3,4,6,1,2]
tree = sorted(tree)

root = bt.build_tree_from_list(tree)
print(bt.bfs_print_tree(root))
