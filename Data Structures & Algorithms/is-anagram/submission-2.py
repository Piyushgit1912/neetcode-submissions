class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # # if sorted(s)==sorted(t):
        # if len(s)!=len(t):
        #     return False
        # if s in t and t in s:
        #     return True
        # else : return False
        return Counter(s)==Counter(t)