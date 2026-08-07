class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = [0]
        for i in range(1,n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                last = stack.pop()
                res[last] = i-last
            stack.append(i)
        
        return res