class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        brackets = {')':'(', '}':'{', ']':'['}
        stack = []
        for char in s:
            if char in brackets.values():
                stack.append(char)
            elif char in brackets.keys():
                if len(stack) == 0:
                    return False
                closing_bracket = stack.pop()
                if closing_bracket != brackets[char]:
                    return False
        if len(stack) != 0:
            return False
        return True
