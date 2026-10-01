class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []
        for i in range(len(heights)):
            h = heights[i]
            prev = i
            while len(stack) > 0 and stack[-1][0] > h:
                prevHeight, prevIdx = stack.pop()
                res = max(res, prevHeight * (i-prevIdx))
                prev = prevIdx
            stack.append([h, prev])
        
        for h, i in stack:
            res = max(res, h * (len(heights) -i))
        
        return res