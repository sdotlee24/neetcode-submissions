class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskMap = defaultdict(int)
        for task in tasks:
            taskMap[task] += 1
        prioQ = [(-count, t) for t, count in taskMap.items()]

        heapq.heapify(prioQ)
        taskQ = deque()

        cycle = 0
        while prioQ or taskQ:
            if prioQ:
                count, task = heapq.heappop(prioQ)
                count += 1
                if count < 0:
                    taskQ.append([count, task, cycle + n])
            
            if taskQ and taskQ[0][2] == cycle:
                c, t, _ = taskQ.popleft()
                heapq.heappush(prioQ, (c, t))

            cycle += 1
        

        return cycle