class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #adj List
        adjList = defaultdict(list)
        for course, prereq in prerequisites:
            adjList[prereq].append(course)

        visited = set()
        
        def traverse(course):
            if course in visited:
                return False
            if not adjList[course]:
                return True
            visited.add(course)
            for c in adjList[course]:
                if not traverse(c):
                    return False
            visited.remove(course)
            adjList[course] = []
            return True
            
        for k in list(adjList.keys()):
            if adjList[k] and not traverse(k):
                return False
        return True
        