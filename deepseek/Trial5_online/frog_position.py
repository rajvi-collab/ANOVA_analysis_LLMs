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
                node, prob = q.popleft()
                if node == target and time == t:
                    return prob
                
                # Count unvisited neighbors
                unvisited_neighbors = []
                for neighbor in adj[node]:
                    if not visited[neighbor]:
                        unvisited_neighbors.append(neighbor)
                
                if not unvisited_neighbors:
                    # Frog stays here forever
                    if node == target and time <= t:
                        return prob
                    else:
                        # No further moves, but we need to check time
                        continue
                else:
                    next_prob = prob / len(unvisited_neighbors)
                    for neighbor in unvisited_neighbors:
                        visited[neighbor] = True
                        q.append((neighbor, next_prob))
            time += 1
        
        return 0.0