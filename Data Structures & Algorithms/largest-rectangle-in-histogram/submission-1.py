class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        size = len(heights)
        for i in range(len(heights)):
            tempIdx = i
            while len(stack) > 0 and stack[-1][0] > heights[i]:
                val, idx = stack.pop()
                res = max(res, val * (i-idx))
                tempIdx = idx
            
            stack.append([heights[i], tempIdx])
        
        for h, idx in stack:
            res = max(res, h * (size-idx))

        return res
