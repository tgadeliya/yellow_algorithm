


class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float("inf")

    def push(self, val: int) -> None:
        self.stack.append((val, self.min))
        self.min = min(val, self.min)

    def pop(self) -> None:
        _, prev_min = self.stack.pop()
        self.min = prev_min

    def top(self) -> int:
        return self.stack[-1][0]
        
    def getMin(self) -> int:
        return self.min