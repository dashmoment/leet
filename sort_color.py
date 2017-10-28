class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        color_dict = {0:[],1:[],2:[]}
        
        for i in range(len(nums)):
            color_dict[nums[i]].append(nums[i])
        
        for i in range(len(nums)):
            if i < len(color_dict[0]):
                nums[i] = 0
            elif i >= len(color_dict[0]) and i < len(color_dict[0]) + len(color_dict[1]):
                nums[i] = 1
            elif i>= len(color_dict[0]) + len(color_dict[1]):
                nums[i] = 2

        
nums = [0,1,0,0,2,1,1,1,2]
s = Solution()
s.sortColors(nums)
print(nums)
