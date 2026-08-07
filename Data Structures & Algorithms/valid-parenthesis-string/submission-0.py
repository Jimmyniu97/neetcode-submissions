class Solution:
    def checkValidString(self, s: str) -> bool:
        paren = []
        star = []

        for i in range(len(s)):
            if s[i] == "(":
                paren.append(i)
            elif s[i] == "*":
                star.append(i)
            elif s[i] == ")":
                if paren:
                    paren.pop()
                elif star:
                    star.pop()
                else:
                    return False
        
        while paren and star:
            if paren.pop() > star.pop():
                return False
        
        return len(paren) == 0