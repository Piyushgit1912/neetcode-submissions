class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        
        # Phase 1: Place each positive integer x at index x - 1
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap nums[i] to its correct position
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
        
        # Phase 2: Find the first index where the number doesn't match the index + 1
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
                
        # If all 1 to n are present, the answer is n + 1
        return n + 1
