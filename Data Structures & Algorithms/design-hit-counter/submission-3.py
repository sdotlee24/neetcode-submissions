class HitCounter:

    def __init__(self):
        self.q = deque() # (timestamp, count)
        self.hits = 0
    def hit(self, timestamp: int) -> None:
        if not self.q or self.q[-1][0] < timestamp:
            self.q.append([timestamp, 1])
        else:
            self.q[-1][1] += 1
        self.hits += 1
    def getHits(self, timestamp: int) -> int:
        while self.q and self.q[0][0] <= timestamp-300:
            _, count = self.q.popleft()
            self.hits -= count
        return self.hits


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
