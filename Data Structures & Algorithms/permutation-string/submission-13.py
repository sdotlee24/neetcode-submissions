class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        charMap = defaultdict(int)
        for s in s1:
            charMap[s] += 1
        l = 0
        building = defaultdict(int)
        for r in range(len(s2)):
            building[s2[r]] += 1
            while building[s2[r]] > charMap[s2[r]]:
                building[s2[l]] -= 1
                l += 1
            
            if r-l+1 == len(s1):
                return True
        return False