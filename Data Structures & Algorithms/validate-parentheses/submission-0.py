class Solution:
    def isValid(self, s: str) -> bool:
        dictionary = {')': '(', ']': '[', '}': '{'}
        stack = []
        for i in range(len(s)):
            if stack:
                if s[i] in dictionary:
                    if dictionary[s[i]] == stack[-1]:
                        stack.pop()
                    else:
                        return False
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])
            if i == len(s) - 1 and not stack:
                return True
        return False
                    
                
