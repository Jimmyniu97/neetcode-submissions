class Solution:
    def bs(self, nums, target, l, r):
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        return -1

    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left < right:
            mid = (left+right) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        
        if target <= nums[-1]:
            l ,r = left, len(nums)-1
            return self.bs(nums, target, l, r)
        else:
            l, r = 0, left-1
            return self.bs(nums, target, l, r)
