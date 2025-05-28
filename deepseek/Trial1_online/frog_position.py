class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        visited = set()
        queue = deque()
        queue.append((1, 1.0, 0))  # (current_node, probability, time)
        visited.add(1)
        while queue:
            current_node, prob, time = queue.popleft()
            if time == t:
                if current_node == target:
                    return prob
                else:
                    continue
            unvisited_neighbors = [neighbor for neighbor in tree[current_node] if neighbor not in visited]
            if not unvisited_neighbors:
                queue.append((current_node, prob, time + 1))
            else:
                for neighbor in unvisited_neighbors:
                    visited.add(neighbor)
                    queue.append((neighbor, prob / len(unvisited_neighbors), time + 1))
        return 0.0
