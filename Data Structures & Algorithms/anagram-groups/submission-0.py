from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=defaultdict(list)
         
        for char in strs:
            d[str(sorted(char))].append(char)
            
        
        new_l = []
        
        for i in d:
            new_l.append(d[i])
        
        return new_l

        