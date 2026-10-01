class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjList = defaultdict(list)
        for a, b in sorted(tickets, reverse=True):
            adjList[a].append(b)
        
        res = []

        def traverse(node):
            while adjList[node]:
                traverse(adjList[node].pop())
            res.append(node)
        traverse("JFK")
        res.reverse()
        return res
        