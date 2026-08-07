class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        valid = []
        for i in range(len(triplets)):
            count = 0
            for j in range(len(target)):
                if triplets[i][j] <= target[j]:
                    count += 1
            if count == len(target):
                valid.append(i)
        
        res = [False] * len(target)
        for i in valid:
            for j in range(len(target)):
                if triplets[i][j] == target[j]:
                    res[j] = True
        
        return sum(res) == len(target)
                
        
        
