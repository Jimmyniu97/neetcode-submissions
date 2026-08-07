class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        unique_nums = set(nums)

        start_list = []
        for num in unique_nums:
            if num-1 not in unique_nums:
                start_list.append(num)

        for num in start_list:
            current_length = 1
            current_num = num
            while current_num + 1 in unique_nums:
                current_num += 1
                current_length += 1
                ans = max(ans, current_length)
            ans = max(ans, current_length)
        
        return ans