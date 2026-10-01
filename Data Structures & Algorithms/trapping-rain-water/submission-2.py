class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height)-1
        wallLeft = [0] * len(height)
        wallRight = [0] * len(height)
        for i in range(1, len(height)):
            wallLeft[i] = max(wallLeft[i-1], height[i-1])
        for i in range(len(height)-2, -1, -1):
            wallRight[i] = max(wallRight[i+1], height[i+1])
        
        for i in range(len(height)):
            wallLeft[i] = min(wallLeft[i], wallRight[i])
        
        for i in range(len(height)):
            if wallLeft[i] > height[i]:
                res += wallLeft[i]-height[i]
        
        return res