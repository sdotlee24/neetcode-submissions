class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        count = defaultdict(int)
        for n in hand:
            count[n] += 1
        nums = [(val, c) for val, c in count.items()]
        heapq.heapify(nums)
        
        numIters = int(len(hand) / groupSize)
        
        for _ in range(numIters):
            prevVal = 0
            toAppend = []
            for i in range(groupSize):
                if not nums:       
                    return False
                val, c = heapq.heappop(nums)
                if i and val-prevVal != 1:
                    return False
                prevVal = val
                if c > 1:
                    toAppend.append((val, c-1))
            for val, c in toAppend:
                heapq.heappush(nums, (val, c))
        
        return True