class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_pointer, right_pointer, string = 0, -1, ''
        for i in s.lower():
            if re.match(r'[A-Za-z0-9]', i):
                string += i
            
        while left_pointer < len(string) // 2:
            if string[left_pointer] != string[right_pointer]:
                return False
            left_pointer += 1
            right_pointer -= 1

        return True