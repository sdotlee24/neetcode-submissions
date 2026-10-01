class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)
        for i in range(1, len(height)):
            maxLeft[i] = max(height[i-1], maxLeft[i-1])
        
        for j in range(len(height) - 2, -1, -1):
            maxRight[j] = max(height[j+1], maxRight[j+1])
        
        res = 0
        for k in range(len(height)):
            temp = min(maxLeft[k], maxRight[k]) - height[k]
            if temp > 0:
                res += temp
        
        return res