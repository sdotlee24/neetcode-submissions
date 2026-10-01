class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tick = 0
        queue = deque()
        counter = Counter(tasks)
        heap = [-val for val in counter.values()]
        heapq.heapify(heap)
        
        while heap or queue:
            if heap:
                task = heapq.heappop(heap)
                task += 1
                if task < 0:
                    queue.append((task, tick+n))
            if queue and queue[0][1] <= tick:
                task, _ = queue.popleft()
                heapq.heappush(heap, task)
            
            tick += 1
        

        return tick