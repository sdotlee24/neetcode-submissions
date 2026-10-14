class MovingAverage:

    def __init__(self, size: int):
        self.i = 0
        self.k = size
        self.window = [0] * size
        self.p = 0
    def next(self, val: int) -> float:
        self.window[self.p] = val
        self.i += 1
        # edge case (list not full size yet)
        self.p = (self.p+1) % self.k
        if self.i < self.k:
            return sum(self.window) / self.i

        return sum(self.window) / self.k


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
