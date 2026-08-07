class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        total = 0
        ans = 0
        i = 0
        while i < len(cost)-1:
            total += gas[i]-cost[i]
            if total < 0:
                total = 0
                ans = i+1
            i += 1
        return ans