class MinStack:

    def __init__(self):
        self.stack = []
        self.minTracker = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minTracker) == 0 or self.minTracker[-1] >= val:
            self.minTracker.append(val)
        
    def pop(self) -> None:
        v = self.stack.pop()
        if len(self.minTracker) != 0 and self.minTracker[-1] == v:
            self.minTracker.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minTracker[-1]
