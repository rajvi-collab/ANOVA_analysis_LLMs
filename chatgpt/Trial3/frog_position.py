# all testcases passed
from typing import List
from collections import defaultdict, deque

class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        # Build the graph using adjacency list
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # BFS queue: (current_node, time, probability)
        queue = deque()
        queue.append((1, 0, 1.0))  # start from node 1 at time 0 with probability 1
        visited = set()
        
        while queue:
            node, time, prob = queue.popleft()
            visited.add(node)

            # If time exceeds t, stop processing further
            if time > t:
                continue

            # Count unvisited neighbors
            unvisited_neighbors = [nei for nei in graph[node] if nei not in visited]
            num_choices = len(unvisited_neighbors)

            # If it's the target
            if node == target:
                # If we reach target exactly at time t or can't move further
                if time == t or num_choices == 0:
                    return prob
                else:
                    return 0.0  # Still can move but we shouldn't

            # Spread probability to unvisited neighbors
            for neighbor in unvisited_neighbors:
                queue.append((neighbor, time + 1, prob / num_choices))

        return 0.0  # If we never reached the target
