    from typing import List
    class Solution:
        def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
            graph = [[] for _ in range(n + 1)]
            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)
            def dfs(node: int, parent: int, time: int, probability: float):
                if node == target and (time == t or len(graph[node]) == 0):
                    return probability
                total_probability = 0.0
                for neighbor in graph[node]:
                    if neighbor != parent:
                        total_probability += dfs(neighbor, node, time + 1, probability / len([x for x in graph[node] if x != parent]))
                return total_probability
            result = dfs(1, -1, 0, 1.0)
            return result


# Example usage:
if __name__ == "__main__":
    solution = Solution()

    print(solution.frogPosition(n=7, edges=[[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t=2, target=4))
    # Output: 0.16666666666666666

    print(solution.frogPosition(n=7, edges=[[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t=1, target=7))
    # Output: 0.3333333333333333