class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        memo = defaultdict(list)

        for word in strs:
            key = ''.join(sorted(word))
            memo[key].append(word)
        
        for k in memo:
            res.append(memo[k])

        return res
        