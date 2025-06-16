class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        # Build adjacency list for graph
        graph = [[] for _ in range(n + 1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Initialize probabilities and visited set
        probabilities = [0.0] * (n + 1)
        probabilities[1] = 1.0
        visited = {1}

        # Perform DFS to calculate probabilities at each time step
        def dfs(node: int, prob: float, time: int) -> None:
            if time == t or len(graph[node]) == 0:
                return

            unvisited_neighbors = [neighbor for neighbor in graph[node] if neighbor not in visited]
            if not unvisited_neighbors:
                probabilities[node] = prob
                return

            probability_to_neighbor = prob / len(unvisited_neighbors)
            for neighbor in unvisited_neighbors:
                visited.add(neighbor)
                dfs(neighbor, probability_to_neighbor, time + 1)

        dfs(1, 1.0, 0)

        # If the target node is not reachable within t steps, return 0
        if probabilities[target] == 0 and len(graph[target]) > 0:
            return 0

        return probabilities[target]