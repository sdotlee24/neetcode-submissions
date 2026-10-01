class Solution:
    def numDecodings(self, s: str) -> int:
        nums = [0] * (len(s)+1)
        nums[-1] = 1
        for i in range(len(s)-1, -1, -1):
            if s[i] == "0":
                nums[i] = 0
            else:
                nums[i] = nums[i+1]

            if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456"):
                nums[i] += nums[i+2]
        
        return nums[0]