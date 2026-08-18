class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Ek default dictionary banayenge jisme list by default hogi
        anagram_map = defaultdict(list)
        
        for s in strs:
            # String ke characters ko sort karke tuple bana lenge (kyunki dict ki key mutable nahi ho sakti)
            sorted_s = "".join(sorted(s))
            
            # Use sorted key ke under original string ko push kar do
            anagram_map[sorted_s].append(s)
            
        # Dictionary ki saari values (sublists) ko return kar do
        return list(anagram_map.values())