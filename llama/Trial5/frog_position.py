# 207 / 207 testcases passed 2 attempts
class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        # Build adjacency list for tree
        graph = [[] for _ in range(n + 1)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = [False] * (n + 1)
        visited[1] = True

        # BFS traversal to find the probability
        queue = collections.deque([(1, 1)])
        while t > 0 and queue:
            size = len(queue)
            for _ in range(size):
                node, prob = queue.popleft()
                num_unvisited_neighbors = sum(1 for neighbor in graph[node] if not visited[neighbor])

                # If we have reached the target node
                if node == target:
                    # If there are no unvisited neighbors or we've run out of time, return probability
                    if t == 1 and num_unvisited_neighbors > 0:
                        return 0.0
                    elif num_unvisited_neighbors == 0:
                        return prob

                # Add unvisited neighbors to queue with updated probability
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        queue.append((neighbor, prob / num_unvisited_neighbors))
                        visited[neighbor] = True

            t -= 1

        # If we've run out of time and the target node is still reachable, return probability
        while queue:
            node, prob = queue.popleft()
            if node == target:
                return prob

        # Target node is not reachable or we have run out of time
        return 0.0