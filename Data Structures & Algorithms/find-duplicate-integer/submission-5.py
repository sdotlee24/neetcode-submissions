class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 1, 4, 3, 2, 3
        slow = fast = 0

        while slow < len(nums):
            slow = nums[slow]
            fast = nums[nums[fast]]

            if nums[slow] == nums[fast]:
                break
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
        