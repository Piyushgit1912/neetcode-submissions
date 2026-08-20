class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
       right_max=0
       for i in range(len(arr)-1,-1,-1):
        possible_max=arr[i]
        arr[i]=right_max
        right_max=max(right_max,possible_max)
       arr[-1]=-1
       return arr

            