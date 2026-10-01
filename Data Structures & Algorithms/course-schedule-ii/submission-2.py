class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        pr = defaultdict(list)

        for a,b in prerequisites:
            pr[a].append(b)
        
        visit, cycle = set(), set()
        def traverse(k):
            if k in cycle:
                return False
            if k in visit:
                return True
            cycle.add(k)
            for b in pr[k]:
                if not traverse(b):
                    return False
            
            cycle.remove(k)
            visit.add(k)
            res.append(k)
            return True
        for c in range(numCourses):
            if not traverse(c):
                return []

        return res 
            