class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        ans = [intervals[0]]
        for i in range(1, len(intervals)):
            last = ans[-1]
            current = intervals[i]
            if current[0] <= last[1]:
                ans.pop()
                ans.append([last[0], max(current[1], last[1])])
            else:
                ans.append(current)

        return ans            