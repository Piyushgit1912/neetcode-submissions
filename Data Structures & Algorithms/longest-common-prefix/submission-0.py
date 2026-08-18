class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs: return ""
        current=strs[0]
        for i in strs[1:]:
           while not i.startswith(current):
            current=current[:-1]
            if not current:
                return ""
        return current
            
            