class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        res = []
        # "montonically decreasing queue"
        for i in range(k):
            while len(queue) > 0 and queue[-1] < nums[i]:
                queue.pop()
            queue.append(nums[i])
            
        res.append(queue[0])

        l = 0
        for r in range(k, len(nums)):
            #increment left pointer
            if len(queue) > 0 and queue[0] == nums[l]:
                queue.popleft()
            l += 1

            #right pointer
            while len(queue) > 0 and queue[-1] < nums[r]:
                queue.pop()
            queue.append(nums[r])

            res.append(queue[0])
        
        return res


            