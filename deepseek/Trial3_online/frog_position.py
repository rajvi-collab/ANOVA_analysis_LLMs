from collections import deque
from typing import List
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
            level_size = len(q)
            for _ in range(level_size):
                current_vertex, prob = q.popleft()
                if time == t and current_vertex == target:
                    return prob
                unvisited_children = []
                for neighbor in adj[current_vertex]:
                    if not visited[neighbor]:
                        unvisited_children.append(neighbor)
                if not unvisited_children:
                    # Frog stays here forever
                    if current_vertex == target and time <= t:
                        return prob
                    else:
                        # No further processing for this node
                        continue
                if time < t:
                    next_prob = prob / len(unvisited_children)
                    for child in unvisited_children:
                        visited[child] = True
                        q.append((child, next_prob))
            time += 1
        return 0.0