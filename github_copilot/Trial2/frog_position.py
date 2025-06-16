from typing import List
class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        from collections import defaultdict, deque
        # Build the graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        # BFS to find the probability
        queue = deque([(1, 1.0, 0)])  # (current_node, probability, time)
        visited = set()
        visited.add(1)
        while queue:
            node, prob, time = queue.popleft()
            if time == t:
                if node == target:
                    return prob
                continue
            unvisited_neighbors = [neighbor for neighbor in graph[node] if neighbor not in visited]
            if not unvisited_neighbors:
                if node == target:
                    return prob
                continue
            next_prob = prob / len(unvisited_neighbors)
            for neighbor in unvisited_neighbors:
                visited.add(neighbor)
                queue.append((neighbor, next_prob, time + 1))
        return 0.0




