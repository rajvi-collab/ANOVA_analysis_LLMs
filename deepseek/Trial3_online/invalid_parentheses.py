from typing import List
from collections import deque
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(t):
            count = 0
            for c in t:
                if c == '(':
                    count += 1
                elif c == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0
        queue = deque()
        visited = set()
        result = []
        found = False
        queue.append(s)
        visited.add(s)
        while queue:
            current = queue.popleft()
            if is_valid(current):
                result.append(current)
                found = True
            # If a valid string is found at this level, skip generating next level
            if found:
                continue
            for i in range(len(current)):
                if current[i] not in '()':
                    continue
                next_str = current[:i] + current[i+1:]
                if next_str not in visited:
                    visited.add(next_str)
                    queue.append(next_str)
        return result if result else [""]