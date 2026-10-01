class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        charMap = {}
        for c in s:
            if c not in charMap:
                charMap[c] = 1
            else:
                charMap[c] += 1
        
        for c in t:
            if c not in charMap or charMap[c] <= 0:
                return False
            else:
                charMap[c] -= 1
        
        for key in charMap.values():
            if key != 0:
                return False

        return True