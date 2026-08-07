"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        count = 0
        ans = 0
        start, end = [], []
        s, e = 0, 0
        for i in intervals:
            start.append(i.start)
            end.append(i.end)
        
        start.sort()
        end.sort()
        
        while s < len(start):
            if start[s] < end[e]:
                count += 1
                s += 1
            else:
                e += 1
                count -= 1
            ans = max(ans, count)
        
        return ans