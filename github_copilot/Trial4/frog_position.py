# 207 / 207 testcases passed

from typing import List, Dict
from collections import defaultdict, deque

class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        # Create adjacency list for the tree
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # BFS to find probability
        queue = deque([(1, 1.0)])  # (current vertex, probability)
        visited = set()
        visited.add(1)
        time = 0
        
        while queue and time <= t:
            for _ in range(len(queue)):
                current, prob = queue.popleft()
                
                if current == target:
                    # If we reached the target vertex
                    if time == t or len(graph[current]) == (1 if current != 1 else 0):
                        return prob
                    else:
                        return 0.0
                
                unvisited_neighbors = [neighbor for neighbor in graph[current] if neighbor not in visited]
                num_unvisited = len(unvisited_neighbors)
                
                for neighbor in unvisited_neighbors:
                    visited.add(neighbor)
                    queue.append((neighbor, prob / num_unvisited))
            
            time += 1
        
        return 0.0