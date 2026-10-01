class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2

        res = [False] * (target + 1)
        res[0] = True

        for i in nums:
            for w in range(target, i - 1, -1):
                if res[w - i]:
                    res[w] = True

        return res[target]