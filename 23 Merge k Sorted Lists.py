#Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        head = None
        root = None

        while True:

        	tmp = []


        	for i in range(len(lists)):

        		if lists[i] is not None:

        			if tmp == []:

        				tmp = [lists[i], i]
        				
        				
        			else:
        				if lists[i].val <= tmp[0].val:
        					tmp = [lists[i], i]
        					
        					
        	if tmp != []:
        		if head == None: 
        			head = tmp[0]
        			root = head
        			
        		else: 
        			head.next = tmp[0]
        			head = head.next

        		try:
        			lists[tmp[1]] = lists[tmp[1]].next
        			
        		except:
        			return root
        	else:
        		return root

  
root = ListNode(0)
root.next = ListNode(2)
root.next.next = ListNode(5)

lists = [root]

s = Solution()
res = s.mergeKLists(lists)

tmp = res
while tmp != None:
	print(tmp.val)
	tmp = tmp.next
