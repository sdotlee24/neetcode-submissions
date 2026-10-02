class Solution:
    def numDecodings(self, s: str) -> int:
        # 1223 -> 1 2 2 3, 12 23, 12 2 3, 1 2 23, 1 22 3
        # [0, 0, 2, 1] -> [0, 3, 2, 1]
        ways = [0] * (len(s) + 2)
        ways[-1] = 1
        ways[-2] = 1
        for i in range(len(ways) - 3, -1, -1):
            ways[i] = ways[i+1]
            if i < len(s)-1 and int(s[i:i+2]) <= 26:
                ways[i] += ways[i+2]
            if s[i] == "0":
                ways[i] = 0
        
        return ways[0]