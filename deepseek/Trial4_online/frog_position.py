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
        q.append((1, 1.0))  # (current vertex, probability)
        visited[1] = True
        time = 0
        
        while q and time <= t:
            for _ in range(len(q)):
                vertex, prob = q.popleft()
                next_vertices = []
                for neighbor in adj[vertex]:
                    if not visited[neighbor]:
                        next_vertices.append(neighbor)
                
                if time == t and vertex == target:
                    return prob
                
                if not next_vertices:
                    # Frog stays here
                    q.append((vertex, prob))
                else:
                    for neighbor in next_vertices:
                        visited[neighbor] = True
                        q.append((neighbor, prob / len(next_vertices)))
            time += 1
        
        return 0.0