class CountSquares:

    def __init__(self):
        self.cache = dict()

    def add(self, point: List[int]) -> None:
        if tuple(point) in self.cache:
            self.cache[tuple(point)] += 1
        else:
            self.cache[tuple(point)] = 1

    def count(self, point: List[int]) -> int:
        diagonal = []
        ans = 0
        for p in self.cache:
            if abs(p[0] - point[0]) == abs(p[1] - point[1]) and p[0] != point[0]:
                for _ in range(self.cache[p]):
                    diagonal.append(p)
        
        for p in diagonal:
            point1 = (p[0], point[1])
            point2 = (point[0], p[1])
            if point1 in self.cache and point2 in self.cache:
                ans += self.cache[point1] * self.cache[point2]
        
        return ans