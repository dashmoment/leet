"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.

"""

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        hash_set = {}
        best = 0
        for i in nums:
            hash_set[i]=0

        for i in range(len(nums)):
            if nums[i] - 1 not in hash_set:
                y = nums[i] + 1
                while y in hash_set:
                    y = y + 1
                best = max(best, y-nums[i])
        return best
        


s = Solution()
print(s.longestConsecutive([]))
