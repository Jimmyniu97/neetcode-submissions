class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix, suffix = [0] * n, [0] * n

        currMax = -1
        for i in range(n):
            currMax = max(currMax, height[i])
            prefix[i] = currMax
        currMax = -1
        for i in range(n-1, -1, -1):
            currMax = max(currMax, height[i])
            suffix[i] = currMax
        
        ans = 0
        for i in range(n):
            ans += min(prefix[i], suffix[i]) - height[i]
        return ans
