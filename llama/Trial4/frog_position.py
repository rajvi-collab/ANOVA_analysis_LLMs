# took 3 attempts, just question no example no constrain
# 207 / 207 testcases passed

from collections import defaultdict
from typing import List

class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * (n + 1)
        probability = [0.0] * (n + 1)
        probability[1] = 1.0
        visited[1] = True

        for _ in range(t):
            new_probability = [0.0] * (n + 1)
            for i in range(1, n + 1):
                if probability[i] > 0:
                    num_neighbors = sum(not visited[j] for j in graph[i])
                    if num_neighbors == 0:  # frog stays on the same vertex
                        new_probability[i] += probability[i]
                    else:
                        for j in graph[i]:
                            if not visited[j]:
                                new_probability[j] += probability[i] / num_neighbors
            probability = new_probability
            for i in range(1, n + 1):
                if probability[i] > 0 and not visited[i]:
                    visited[i] = True

        return probability[target]