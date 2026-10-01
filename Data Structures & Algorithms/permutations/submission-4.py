class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def traverse(i, temp, seen):
            if i == len(nums):
                res.append(temp.copy())
                return
            for n in nums:
                if n not in seen:
                    seen.add(n)
                    temp.append(n)
                    traverse(i+1, temp, seen)
                    seen.remove(n)
                    temp.pop()
        
        traverse(0, [], set())
        return res