class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_table = {}
        length = l = 0
        for r in range(len(s)):
            if s[r] in hash_table:
                l = max(l, hash_table[s[r]]+1)
            hash_table[s[r]] = r
            length = max(length, r - l + 1)
        return length

                

        
