"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        lo = 0
        ho = len(nums) - 1

        while lo <= ho:
        	mid = (ho + lo)//2

        	if target == nums[lo]: return lo
        	elif target == nums[ho]: return ho
        	elif target == nums[mid]: return mid
        	
        	if mid > 0 and mid < len(nums) - 1:
	        	if abs(target - nums[mid+1]) > abs(target - nums[mid-1]):
	        		ho = mid-1
	        	elif abs(target - nums[mid+1]) < abs(target - nums[mid-1]):
	        		lo = mid+1
	    
	        	else: break
	        		
	        else: break
        return -1

s = Solution()
print(s.search([1],1))