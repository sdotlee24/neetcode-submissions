class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for i in nums:
            count[i] += 1
        
        bucket = [[] for _ in range(len(nums) + 1)]
        res = []

        for n in count.keys():
            bucket[count[n]].append(n)

        for frequency in range(len(bucket) - 1, 0, -1):
            for num in bucket[frequency]:
                res.append(num)

                if len(res) == k:
                    return res