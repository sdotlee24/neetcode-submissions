class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        memo = defaultdict(list)
        for s in strs:
            memo[''.join(sorted(s))].append(s)
        
        for val in memo.values():
            res.append(val)
        
        return res
