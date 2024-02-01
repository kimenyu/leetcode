class Solution:
    """
    Given an array of integers nums and an integer target, 
    return indices of the two numbers such that they add up to target.
    
    """  
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return None

nums = [2, 7, 11, 15]
target = 17
sol = Solution()
mySol = sol.twoSum(nums, target)
print(mySol)
