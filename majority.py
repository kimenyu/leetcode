class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate = None
        count = 0
        
        # Step 1: Find the potential candidate for majority element
        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            elif num == candidate:
                count += 1
            else:
                count -= 1
        
        # Step 2: Validate if the candidate is the majority element
        count = 0
        for num in nums:
            if num == candidate:
                count += 1
        if count > len(nums) / 2:
            return candidate
        else:
            return None  # If no majority element found, return None
