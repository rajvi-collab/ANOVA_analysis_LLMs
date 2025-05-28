from typing import List
from collections import defaultdict, deque
class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        if n == 1:
            return 1.0
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = [False] * (n + 1)
        queue = deque([(1, 1.0)])  # (current_vertex, probability)
        visited[1] = True
        time = 0
        while queue and time < t:
            for _ in range(len(queue)):
                current, prob = queue.popleft()
                unvisited_neighbors = [neighbor for neighbor in graph[current] if not visited[neighbor]]
                if not unvisited_neighbors:
                    queue.append((current, prob))
                else:
                    for neighbor in unvisited_neighbors:
                        visited[neighbor] = True
                        queue.append((neighbor, prob / len(unvisited_neighbors)))
            time += 1
        while queue:
            current, prob = queue.popleft()
            if current == target:
                return prob
        return 0.0