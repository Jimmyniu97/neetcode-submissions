class TimeMap:

    def __init__(self):
        self.cache = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.cache:
            self.cache[key] = []
        self.cache[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        ans = ""
        values = self.cache.get(key, [])
        
        left, right = 0, len(values)-1
        while left <= right:
            mid = (left+right) // 2
            if values[mid][0] > timestamp:
                right = mid - 1
            else:
                left = mid + 1
                ans = self.cache[key][mid][1]
        
        return ans

