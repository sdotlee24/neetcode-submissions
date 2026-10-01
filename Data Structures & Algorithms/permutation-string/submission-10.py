class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Map = defaultdict(int)
        for s in s1:
            s1Map[s] += 1
        
        charMap = defaultdict(int)
        l = 0
        for r in range(len(s2)):
            charMap[s2[r]] += 1
            while charMap[s2[r]] > s1Map[s2[r]]:
                charMap[s2[l]] -= 1
                l += 1
            if r-l+1 == len(s1):
                for k, v in s1Map.items():
                    if not charMap[k] == v:
                        break
                return True
        return False