class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(set(s)) != len(set(t)) or len(s) != len(t):
            return False
        
        for i in set(s):
            if s.count(i) == t.count(i):
                continue 
            else: return False
        return True