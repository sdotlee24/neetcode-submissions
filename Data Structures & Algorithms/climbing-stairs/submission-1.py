class Solution:
    def climbStairs(self, n: int) -> int:
        distinct = [0] * (n+1)
        if n == 1:
            return 1

        if n == 2:
            return 2
        distinct[1] = 1
        distinct[2] = 2
        for i in range(3,n+1):
            distinct[i] = distinct[i-1] + distinct[i-2]
        
        return distinct[n]