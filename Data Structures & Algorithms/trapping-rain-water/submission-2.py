class Solution:
    def trap(self, height: List[int]) -> int:
        prefix, suffix = [0]*len(height), [0]*len(height)
        ans = 0
        leftMax = 0
        for i in range(1, len(height)):
            leftMax = max(leftMax, height[i-1])
            prefix[i] = leftMax
        rightMax = 0
        for j in range(len(height)-2, -1, -1):
            rightMax = max(rightMax, height[j+1])
            suffix[j] = rightMax
        
        for i in range(len(height)):
            if min(prefix[i], suffix[i]) > height[i]:
                ans += min(prefix[i], suffix[i]) - height[i]
        
        return ans