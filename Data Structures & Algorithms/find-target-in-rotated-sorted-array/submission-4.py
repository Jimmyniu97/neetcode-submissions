class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left+right) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid+1

        pivot = left
        l, r = 0, len(nums)-1
        if nums[pivot] <= target and nums[r] >= target:
            l = pivot
        else:
            r = pivot-1

        while l <= r:
            mid = (l+r) // 2
            if nums[mid] < target:
                l = mid+1
            elif nums[mid] > target:
                r = mid-1
            else:
                return mid        
        return -1