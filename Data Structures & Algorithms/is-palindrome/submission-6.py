class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_pointer, right_pointer, string = 0, -1, ''
        for i in s.lower():
            if i.isalnum():
                string += i
        return string[::-1] == string