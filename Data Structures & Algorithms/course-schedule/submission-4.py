class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #if cycle detected, impossible
        tree = defaultdict(list)
        for a, b in prerequisites:
            tree[a].append(b)
        visited = set()

        def traverse(k):
            if k in visited:
                return False
            if tree[k] == []:
                return True
            visited.add(k)
            for i in tree[k]:
                if not traverse(i):
                    return False
            visited.remove(k)
            tree[k] = []

            return True
        
        for i in range(numCourses):
            if not traverse(i):
                return False
        
        return True
