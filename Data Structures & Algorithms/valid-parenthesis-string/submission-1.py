class Solution:
    def checkValidString(self, s: str) -> bool:
        left, star = [], []

        for i, c in enumerate(s):
            if c == "(":
                left.append(i)
            if c == "*":
                star.append(i)
            if c == ")":
                if left:
                    left.pop()
                elif star:
                    star.pop()
                else:
                    return False
        
        for _ in range(min(len(left), len(star))):
            l, s = left.pop(), star.pop()
            if l > s:
                return False
        
        return len(left) == 0