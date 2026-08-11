class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = math.inf

    def push(self, val: int) -> None:
        self.mini = min(self.mini, val)
        self.stack.append((val, self.mini))

    def pop(self) -> None:
        self.stack.pop()
        self.mini = self.stack[-1][1] if self.stack else math.inf

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.mini
        
