class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        cache = {')':'(', ']':'[', '}':'{'}

        for character in s:
            if character in {'(', '[', '{'}:
                stack.append(character)
            else:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if cache[character] != top:
                    return False
        
        return len(stack) == 0