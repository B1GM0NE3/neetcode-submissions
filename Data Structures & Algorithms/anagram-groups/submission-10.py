class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for string in strs:
            array = [0] * 26
            for ch in string:
                array[ord(ch) - ord('a')] += 1
            res[tuple(array)].append(string)
        return list(res.values())
            
