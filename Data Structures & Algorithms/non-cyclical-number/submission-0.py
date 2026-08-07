class Solution:
    def helper(self, n):
        ans = 0
        while n >= 1:
            ans += (n%10)**2
            n //= 10
        return ans
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            seen.add(n)
            newN = self.helper(n)
            if newN == 1:
                return True
            elif newN in seen:
                return False
            else:
                n = newN