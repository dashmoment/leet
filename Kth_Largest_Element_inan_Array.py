class Solution:
    def bubble_sort(self, nums, k):

        for i in range(k):
            for j in range(len(nums)-i-1):
                if nums[j] > nums[j+1]:
                    nums[j+1], nums[j] = nums[j], nums[j+1]

        return nums[-k]

    def quicksort(self, nums, k=5,sorted_array = []):

        left = []
        right = []
        if len(nums) < 2: return nums
        pivot = nums[0]
        for i in range(1,len(nums)):

            if nums[i] < pivot: left.append(nums[i])
            elif nums[i] >= pivot: right.append(nums[i])

        return self.quicksort(left) + [pivot] + self.quicksort(right)

s = Solution()
print(s.quicksort([6,5,11,7,9,2], 5))
