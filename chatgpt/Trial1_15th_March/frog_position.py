from collections import defaultdict
from typing import List
class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        def dfs(node, parent, time, prob):
            if time == 0:
                return prob if node == target else 0
            neighbors = [nei for nei in graph[node] if nei != parent]
            if not neighbors:
                return prob if node == target else 0
            probability = 0
            for nei in neighbors:
                probability += dfs(nei, node, time - 1, prob / len(neighbors))
            return probability
        return dfs(1, -1, t, 1.0)


