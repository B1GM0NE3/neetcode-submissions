class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        hashset_list = {}
        index = 0

        for string in strs:
            array = [0] * 26
            for ch in string:
                array[ord(ch) - ord('a')] += 1
            array = tuple(array)
            if array in hashset_list:
                result[hashset_list[array]].append(string)
            else:
                hashset_list[array] = index
                result.append([string])
                index += 1
        return result
            
