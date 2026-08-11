class Solution:
    def isValid(self, s: str) -> bool:
        cache = {')':'(', ']':'[', '}':'{'}
        stack = []
        for c in s:
            if c in ['(', '[', '{']:
                stack.append(c)
            elif stack:
                top = stack.pop()
                if cache[c] != top:
                    return False
            else:
                return False
        
        return len(stack) == 0