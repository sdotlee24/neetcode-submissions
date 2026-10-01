class Solution:
    def maxArea(self, heights: List[int]) -> int:
        top = 0
        i, j = 0, len(heights) - 1
        while i < j:
            curHeight = min(heights[i], heights[j])
            top = max(top, curHeight *  (j-i))
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
            
        return top