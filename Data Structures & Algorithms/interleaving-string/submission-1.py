class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        memo = {}

        def traverse(i, j, k):
            if k == len(s3):
                return True
            if (i,j,k) in memo:
                return memo[(i,j,k)]
            works = False
            if i < len(s1) and s1[i] == s3[k]:
                works = works or traverse(i+1, j, k+1)
            if not works and j < len(s2) and s2[j] == s3[k]:
                works = works or traverse(i, j+1, k+1)
            memo[(i,j,k)] = works
            return works
        return traverse(0,0,0)