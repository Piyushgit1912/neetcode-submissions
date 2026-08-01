class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,a in enumerate(nums):
            for j,b in enumerate(nums):
                if i==j:continue
                elif a+b==target:
                    return [i,j]