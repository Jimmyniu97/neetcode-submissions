class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        left, right = 0, len(heights)-1
        while left < right:
            current_amount = min(heights[left], heights[right]) * (right - left)
            ans = max(ans, current_amount)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        
        return ans