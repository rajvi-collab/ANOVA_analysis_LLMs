from collections import defaultdict, deque
from typing import List
class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        if n == 1:
            return 1.0
        # Build the graph using adjacency list
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        # Perform BFS
        queue = deque([(1, 1.0)])  # (current_node, current_probability)
        visited = set([1])
        while queue and t >= 0:
            size = len(queue)
            for _ in range(size):
                node, prob = queue.popleft()
                # If the target is reached and no time left, return the probability
                if node == target and (t == 0 or len([x for x in graph[node] if x not in visited]) == 0):
                    return prob
                # Explore neighbors
                neighbors = [x for x in graph[node] if x not in visited]
                for neighbor in neighbors:
                    visited.add(neighbor)
                    queue.append((neighbor, prob / len(neighbors)))
            t -= 1
        return 0.0
