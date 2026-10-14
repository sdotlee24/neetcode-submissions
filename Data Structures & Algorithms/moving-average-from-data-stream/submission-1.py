class MovingAverage:
    def __init__(self, size: int):
        self.k = size
        self.window = [0] * size
        self.p = 0
        self.count = 0
        self.total = 0

    def next(self, val: int) -> float:
        self.total += val - self.window[self.p]   # slot holds 0 until filled
        self.window[self.p] = val
        self.p = (self.p + 1) % self.k
        self.count = min(self.count + 1, self.k)
        return self.total / self.count