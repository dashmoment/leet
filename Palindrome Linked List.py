"""
Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?
"""

class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):

    def isdPalindrome(self, head):
        self.left = head
        return self.isisdPalindrome_eval(head)

    def isisdPalindrome_eval(self,node):

        if node == None: return True

        right = node

        result = self.isisdPalindrome_eval(right.next)
        if right.val == self.left.val:
           
            self.left = self.left.next
            return result and True
        else:
            self.left = self.left.next
            return False
        

context = [1,2,3,3,4,1]

root = ListNode(context[0])
head = root
for i in range(1,len(context)):
    head.next = ListNode(context[i])
    head = head.next


s = Solution()
print(s.isdPalindrome(root))

    
    
