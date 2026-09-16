class Solution:
    def longestPalindrome(self, s: str) -> str:
        resLen = 0
        res = 0
        def helper(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                nonlocal resLen, res
                if right-left+1 > resLen:
                    resLen = right-left+1
                    res = left
                left -= 1
                right += 1
        for i in range(len(s)):
            #odd
            left, right = i, i
            helper(left, right)
            #even
            left, right = i, i+1
            helper(left, right)
        
        return s[res:res+resLen]
