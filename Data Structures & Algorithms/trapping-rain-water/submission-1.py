class Solution:
    def trap(self, height: List[int]) -> int:
        # min(max left, max right) - current = # water cubes in that column
        res = 0
        fromLeft = [0] * len(height)
        fromRight = [0] * len(height)
        for i in range(1, len(height)):
            fromLeft[i] = max(fromLeft[i-1], height[i-1])
        for i in range(len(height) - 2, -1, -1):
            fromRight[i] = max(fromRight[i+1], height[i+1])
        
        for i in range(len(height)):
            bar = min(fromLeft[i], fromRight[i])
            if bar > height[i]:
                res += bar - height[i]
        return res