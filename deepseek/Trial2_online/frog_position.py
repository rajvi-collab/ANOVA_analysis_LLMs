from typing import List
from collections import deque
class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        # Build the adjacency list
        adj = [[] for _ in range(n + 1)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        visited = [False] * (n + 1)
        q = deque()
        q.append((1, 0, 1.0))  # (current vertex, time, probability)
        visited[1] = True
        while q:
            vertex, time, prob = q.popleft()
            if time > t:
                continue
            # Get unvisited neighbors
            unvisited = []
            for neighbor in adj[vertex]:
                if not visited[neighbor]:
                    unvisited.append(neighbor)
            # Check if current vertex is target
            if vertex == target:
                if time == t or (time < t and not unvisited):
                    return prob
                else:
                    return 0.0
            # Handle movement
            for neighbor in unvisited:
                visited[neighbor] = True
                q.append((neighbor, time + 1, prob / len(unvisited)))
        return 0.0