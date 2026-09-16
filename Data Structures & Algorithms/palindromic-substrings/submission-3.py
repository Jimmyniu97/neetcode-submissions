class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        def helper(left, right):
            nonlocal res
            while left >= 0 and right < len(s) and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
        
        for i in range(len(s)):
            left, right = i, i
            helper(left, right)

            left, right = i, i+1
            helper(left, right)
        
        return res