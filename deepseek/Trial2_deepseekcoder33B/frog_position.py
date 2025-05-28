# Attempt 1
# 107 / 207 testcases passed

from collections import defaultdict, deque
from typing import List

class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        """
        :type n: int
        :type edges: List[List[int]]
        :type t: int
        :type target: int
        :rtype: float
        """
        graph = [[] for _ in range(n+1)]  # adjacency list representation of the tree
        proba = [0.0] * (n+1)             # probability to reach each node starting from node 1
        seen  = [False] * (n+1)           # mark visited nodes

        for u, v in edges:               # construct adjacency list representation of the tree
            graph[u].append(v)
            graph[v].append(u)

        proba[1] = 1.0                   # probability to reach node 1 is 1 as frog starts from node 1

        def dfs(i, t):
            if i != 1 and len(graph[i]) == 1 or t == 0:      # base cases
                return i == target                         # frog reaches the target vertex within time limit

            seen[i] = True                                # mark node as visited
            res = 0.0                                    # probability to reach the target from node i

            for j in graph[i]:                           # iterate over each neighbor of node i
                if not seen[j]:                          # if neighbor is not visited yet
                    s = sum(not seen[k] for k in graph[j])  # count unvisited neighbors of the neighbor vertex j
                    res += dfs(j, t-1) / (len(graph[i]) - int(i != 1)) * (s or 1.0)   # DFS with probability calculation
            return res if i == target else 0.0           # return the result

        return dfs(1, t)



# 202 / 207 testcases passed

class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        graph = [[] for _ in range(n + 1)]
        prob = [0.0] * (n + 1)
        visited = [False] * (n + 1)

        # Build the tree graph
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        queue = collections.deque([(1, 1.0, 0)])    # node, probability, seconds

        while queue:
            node, p, time = queue.popleft()
            visited[node] = True

            if node == target and (time == t or len(graph[node]) == 1):
                prob[target] += p

            elif node != target and time < t:
                unvisited_neighbors = 0   # number of neighbors that are not visited yet
                for nei in graph[node]:
                    if not visited[nei]:
                        unvisited_neighbors += 1

                if unvisited_neighbors > 0:    # there are nodes to visit next
                    for nei in graph[node]:
                        if not visited[nei]:
                            queue.append((nei, p / unvisited_neighbors, time + 1))

                else:   # current node is a leaf node -> stay here
                    prob[node] += p

        return prob[target] if target > 0 else 1.0

# 206 / 207 testcases passed

from collections import defaultdict, deque
from typing import List

class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        if n == 1:
            return 1.0

        graph = [[] for _ in range(n + 1)]
        prob = [0.0] * (n + 1)
        visited = [False] * (n + 1)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        queue = collections.deque([(1, 1.0, 0)])     # node, probability, seconds

        while queue:
            node, p, time = queue.popleft()
            visited[node] = True

            if node == target and (time == t or len(graph[node]) == 1):
                prob[target] += p

            elif node != target and time < t:
                unvisited_neighbors = 0    # number of neighbors that are not visited yet
                for nei in graph[node]:
                    if not visited[nei]:
                        unvisited_neighbors += 1

                if unvisited_neighbors > 0:     # there are nodes to visit next
                    for nei in graph[node]:
                        if not visited[nei]:
                            queue.append((nei, p / unvisited_neighbors, time + 1))

                else:    # current node is a leaf node -> stay here
                    prob[node] += p

        return prob[target] if target > 0 else 1.0