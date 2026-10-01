class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1

        hash_table = {}
        length = l = 0
        for r in range(len(s)):
            if s[r] not in hash_table:
                hash_table[s[r]] = r
            else:
                length = max(length, r - l)
                new_l = hash_table[s[r]]
                del hash_table[s[l]]
                l += 1
                while l <= new_l:
                    del hash_table[s[l]]
                    l += 1
                hash_table[s[r]] = r
            length = max(length, r - l + 1)
        return length
                

        
