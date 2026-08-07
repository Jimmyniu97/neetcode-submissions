class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        sorted_speed = [x for _,x in sorted(zip(position, speed), reverse=True)]
        sorted_position = sorted(position, reverse=True)
        stack = []
        for i in range(n):
            time = (target-sorted_position[i]) / sorted_speed[i]
            if not stack or stack[-1] < time:
                stack.append(time)
        
        return len(stack)
