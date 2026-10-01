class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        tree = defaultdict(list)
        for course, prereq in prerequisites:
            tree[course].append(prereq)
        
        res = []
        state = [0] * numCourses # 0: not visited, 1: visited in this path, 2: completely visited
        def traverse(course):
            if state[course] == 1:
                return False
            if state[course] == 2:
                return True
            state[course] = 1
            for c in tree[course]:
                if not traverse(c):
                    return False
            state[course] = 2
            res.append(course)
            tree[course] = []
            return True
        
        for course in range(numCourses):
            if not traverse(course):
                return []
        return res
            