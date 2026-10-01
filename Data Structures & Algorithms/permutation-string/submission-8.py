class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        def createCharMap(text):
            charMap = {}
            for s in text:
                charMap[s] = charMap.get(s, 0) + 1
            return charMap
        charMap = createCharMap(s1)
            
        l, r = 0, len(s1)
        while r <= len(s2):
            compareMap = createCharMap(s2[l:r])
            present = True
            for key in charMap:
                if key not in compareMap or compareMap[key] != charMap[key]:
                    present = False
            if present:
                return True
            
            l += 1
            r += 1
        return False
            
                