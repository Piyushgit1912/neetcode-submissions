class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        avg=len(nums)/3
        dictt={}
        result=[]
        for num in nums:
            dictt[num]= dictt.get(num,0)+1
        for num, count in dictt.items():
            if count>avg:
              result.append(num)
        return result
