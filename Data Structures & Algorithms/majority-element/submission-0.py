class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dictt={}
        avg=len(nums)/2
        for num in nums:
            dictt[num]= dictt.get(num,0)+1
            if dictt[num]>= avg:
                return num