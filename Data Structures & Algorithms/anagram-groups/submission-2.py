class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        memo = defaultdict(list)
        for s in strs:
            memo[''.join(sorted(s))].append(s)
        
        return [x for x in memo.values()]