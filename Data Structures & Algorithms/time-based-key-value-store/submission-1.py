from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.cache = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.cache[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        valList = self.cache[key]
        left, right = 0, len(valList)-1
        res = ""
        while left <= right:
            mid = (left+right) // 2
            if valList[mid][0] > timestamp:
                right = mid-1
            else:
                res = valList[mid][1]
                left = mid+1
        
        return res
