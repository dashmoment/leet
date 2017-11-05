# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        stack_p = []
        stack_q = []
        
        head = root
        
        def find_path(head, taget, stack):
            if taget == None: return [head]
            while head is not None:
                if taget < head.val: 
                    stack.append(head)
                    head = head.left
                elif taget > head.val:
                    stack.append(head)
                    head = head.right
                elif taget == head.val:
                    stack.append(head)
                    break
                    
            return stack
        
        
        stack_p = find_path(root, p, stack_p)
       
        stack_q = find_path(root, q, stack_q)
        
        for i in range(len(stack_p)):
            for j in range(len(stack_q)):
                
                if stack_p[-i-1].val == stack_q[-j-1].val:
                    return stack_q[-j-1]
        


root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)


s = Solution()
print(s.lowestCommonAncestor(root, None,3).val)
