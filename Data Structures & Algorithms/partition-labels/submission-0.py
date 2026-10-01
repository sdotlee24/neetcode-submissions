class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastOccurenceOf = defaultdict(int)
        for i in range(len(s)):
            lastOccurenceOf[s[i]] = i
        
        res = []
        temp = 0
        lastOccurence = 0
        for i in range(len(s)):
            temp += 1
            lastOccurence = max(lastOccurence, lastOccurenceOf[s[i]])
            if i == lastOccurence:
                res.append(temp)
                temp = 0
        
        return res