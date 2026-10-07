class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x: x[0])
        newStart, newEnd = intervals[0]
        idx = 1
        res = []
        while idx < len(intervals):
            if intervals[idx][0] <= newEnd:
                newStart = min(newStart, intervals[idx][0])
                newEnd = max(newEnd, intervals[idx][1])
            else:
                res.append([newStart, newEnd])
                newStart = intervals[idx][0]
                newEnd = intervals[idx][1]
            idx += 1
        
        res.append([newStart, newEnd])
        
        return res