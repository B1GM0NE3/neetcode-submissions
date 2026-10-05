class Solution:
    def isValid(self, s: str) -> bool:
        dictionary = {')': '(', ']': '[', '}': '{'}
        stack = []
        for i in range(len(s)):
            if stack and s[i] in dictionary:
                if dictionary[s[i]] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
        if stack:
            return False
        else:
            return True
                
