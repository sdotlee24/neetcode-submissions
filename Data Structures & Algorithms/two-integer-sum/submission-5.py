class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valMap = {}
        for j in range(len(nums)):
            diff = target - nums[j]
            if diff in valMap:
                return [valMap[diff], j]
            
            valMap[nums[j]] = j