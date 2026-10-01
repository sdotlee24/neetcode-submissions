class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # [a, b] means must take b to take a, b is prerequisite of a
        # a -> b

        adjList = defaultdict(list)
        for a, b in prerequisites:
            adjList[a].append(b)
        res = []
        state = [0] * numCourses #0: not visited, 1: visited in this call, 2: completely visited
        def traverse(cur):
            if state[cur] == 1:
                return False
            if state[cur] == 2:
                return True
            state[cur] = 1
            for prereq in adjList[cur]:
                if not traverse(prereq):
                    return False
                
            res.append(cur)
            adjList[cur] = []
            state[cur] = 2
            return True
        for i in range(numCourses):
            if not traverse(i):
                return []
            
        
        return res