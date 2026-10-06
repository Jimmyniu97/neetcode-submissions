class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        idx = 0
        while idx < len(intervals) and intervals[idx][1] < newInterval[0]:
            idx += 1
        
        if idx == len(intervals):
            intervals.append(newInterval)
            return intervals
        
        if intervals[idx][0] > newInterval[1]:
            intervals.insert(idx, newInterval)
            return intervals
        
        newStart = min(intervals[idx][0], newInterval[0])
        newEnd = max(intervals[idx][1], newInterval[1])
        prev = idx
        while idx < len(intervals) and intervals[idx][0] <= newEnd:
            newStart = min(intervals[idx][0], newStart)
            newEnd = max(intervals[idx][1], newEnd)
            idx += 1
        intervals[prev:idx] = [[newStart, newEnd]]
        
        return intervals