class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = [[] for _ in range(n)]

        for s, d, w in edges:
            adj[s].append([d, w])

        minHeap = [[0, src]]  ## cost, dest
        shortest = {}   ## node: cost

        while minHeap:
            c, n1 = heapq.heappop(minHeap)
            if n1 in shortest:
                continue
            
            shortest[n1] = c

            for n2, c2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(minHeap, [c + c2, n2])

        for i in range(n):
            if i not in shortest:
                shortest[i] = -1

        return shortest 