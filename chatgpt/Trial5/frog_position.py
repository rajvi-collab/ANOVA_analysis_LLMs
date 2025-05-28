from typing import List
from collections import defaultdict

class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        # Build the graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * (n + 1)

        def dfs(node, time_left, prob):
            visited[node] = True
            if time_left == 0 or (len(graph[node]) == 1 and visited[graph[node][0]]):
                return prob if node == target else 0.0

            unvisited_neighbors = [nei for nei in graph[node] if not visited[nei]]
            if not unvisited_neighbors:
                return prob if node == target else 0.0

            next_prob = prob / len(unvisited_neighbors)
            for nei in unvisited_neighbors:
                res = dfs(nei, time_left - 1, next_prob)
                if res > 0:
                    return res

            return 0.0

        return dfs(1, t, 1.0)
