class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #n = 4, [1, 4, 2, 2, 3] => 1 -> 4 -> 3 -> 2 <-> 2
        fast, slow = 0, 0
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow