class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(string: str) -> bool:
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
        seen = {s}
        result = []
        found_valid = False
        while queue:
            curr_str = queue.popleft()
            if is_valid(curr_str):
                result.append(curr_str)
                found_valid = True
            if found_valid:
                continue
            for i in range(len(curr_str)):
                if curr_str[i] == '(' or curr_str[i] == ')':
                    new_str = curr_str[:i] + curr_str[i+1:]
                    if new_str not in seen:
                        queue.append(new_str)
                        seen.add(new_str)
        return result