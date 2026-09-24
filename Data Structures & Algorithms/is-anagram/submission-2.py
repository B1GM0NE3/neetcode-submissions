class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        abt = [0] * 26
        for i in range(len(s)):
            abt[ord(s[i]) - ord('a')] += 1
            abt[ord(t[i]) - ord('a')] -= 1

        for val in abt:
            if val != 0:
                return False
        return True