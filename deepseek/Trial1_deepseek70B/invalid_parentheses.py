# Attempt 2nd ====================
# Local Deepseek
# 1. 64 / 129 testcases passed - s = "()())()" Expected = ["(())()","()()()"]

from collections import deque

def min_deletions_to_balance(s):
    def is_balanced(string):
        stack = []
        for char in string:
            if char == '(':
                stack.append(char)
            elif char == ')':
                if not stack:
                    return False
                stack.pop()
        return len(stack) == 0

    queue = deque([(s, 0)])
    visited = set([s])

    while queue:
        current_str, deletions = queue.popleft()

        if is_balanced(current_str):
            # Collect all possible valid strings at this level
            result = []
            for item in list(queue):
                str_item, del_count = item
                if is_balanced(str_item) and del_count == deletions:
                    result.append(str_item)
            return [current_str] + result

        if len(current_str) == 0:
            continue

        for i in range(len(current_str)):
            new_str = current_str[:i] + current_str[i+1:]
            if new_str not in visited and is_balanced(new_str):
                # If this string is valid, collect all such at this level
                result = []
                for item in list(queue):
                    str_item, del_count = item
                    if is_balanced(str_item) and del_count == deletions + 1:
                        result.append(str_item)
                return [new_str] + result
            if new_str not in visited:
                visited.add(new_str)
                queue.append((new_str, deletions + 1))

    # If no balanced string found except empty
    return [""]

# Example usage:
print(min_deletions_to_balance("(()"))  # Output: ['()']