class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        intervals.sort(key=lambda x: x[0])
        prevEnd = intervals[0][1]

        for i in range(1, len(intervals)):
            current = intervals[i]
            if current[0] < prevEnd:
                count += 1
                prevEnd = min(prevEnd, current[1])
            else:
                prevEnd = current[1]
        
        return count