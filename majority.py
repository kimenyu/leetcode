class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """   
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[i] == nums[j]:
                    count += 1
            if count > len(nums) /2:
                return nums[i]
nums = [2, 2, 1, 1, 1, 1, 1, 1, 2, 2]
