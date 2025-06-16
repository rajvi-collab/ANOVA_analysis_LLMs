# 3 attempts
# 123 / 207 testcases passed
class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        # Build the graph
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Initialize visited and queue for BFS
        visited = set()
        queue = [(1, 1.0)]  # (node, probability)
        visited.add(1)

        while t > 0 and queue:
            next_queue = []
            for node, prob in queue:
                if node == target:
                    # If the target is reached and there are no unvisited neighbors,
                    # the frog will stay at this vertex forever
                    if not any(neighbor not in visited for neighbor in graph[node]):
                        t -= 1
                        continue

                # Add unvisited neighbors to the next queue
                unvisited_neighbors = [neighbor for neighbor in graph[node] if neighbor not in visited]
                if unvisited_neighbors:
                    prob_next = prob / len(unvisited_neighbors)
                    for neighbor in unvisited_neighbors:
                        next_queue.append((neighbor, prob_next))
                        visited.add(neighbor)
                else:
                    # If there are no unvisited neighbors, the frog will stay at this vertex forever
                    t -= 1

            queue = next_queue
            t -= 1

        # Calculate the final probability
        for node, prob in queue:
            if node == target:
                return prob

        # If the target is not reached after t seconds, return 0
        return 0
