from collections import deque
class Solution:
    def removeInvalidParentheses(self, s: str):
        def is_valid(string):
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                if count < 0:
                    return False
            return count == 0
        queue = deque([s])
        visited = set([s])
        found = False
        result = []
        while queue:
            level_size = len(queue)
            level_seen = set()
            for _ in range(level_size):
                curr = queue.popleft()
                if is_valid(curr):
                    result.append(curr)
                    found = True
                if found:
                    continue
                for i in range(len(curr)):
                    if curr[i] not in "()":
                        continue
                    new_str = curr[:i] + curr[i+1:]
                    if new_str not in visited:
                        queue.append(new_str)
                        visited.add(new_str)
            if found:
                break
        return result