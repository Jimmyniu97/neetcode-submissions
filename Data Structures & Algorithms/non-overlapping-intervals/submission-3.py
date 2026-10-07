class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        prevEnd = intervals[0][1]
        i = 1
        ans = 0
        while i < len(intervals):
            if intervals[i][0] >= prevEnd:
                prevEnd = intervals[i][1]
            else:
                prevEnd = min(prevEnd, intervals[i][1])
                ans += 1
            i += 1
        
        return ans