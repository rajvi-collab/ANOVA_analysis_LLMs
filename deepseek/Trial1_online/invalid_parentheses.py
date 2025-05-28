from typing import List
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(s: str) -> bool:
            count = 0
            for char in s:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0
        def backtrack(index: int, left_removed: int, right_removed: int, path: str) -> None:
            if index == len(s):
                if left_removed == 0 and right_removed == 0 and is_valid(path):
                    valid_expressions.add(path)
                return
            current_char = s[index]
            if current_char == '(' and left_removed > 0:
                backtrack(index + 1, left_removed - 1, right_removed, path)
            elif current_char == ')' and right_removed > 0:
                backtrack(index + 1, left_removed, right_removed - 1, path)
            backtrack(index + 1, left_removed, right_removed, path + current_char)
        left_removed = 0
        right_removed = 0
        for char in s:
            if char == '(':
                left_removed += 1
            elif char == ')':
                if left_removed == 0:
                    right_removed += 1
                else:
                    left_removed -= 1
        valid_expressions = set()
        backtrack(0, left_removed, right_removed, "")
        return list(valid_expressions)

# Example usage:
solution = Solution()
print(solution.removeInvalidParentheses("()())()"))  # Output: ["(())()","()()()"]
print(solution.removeInvalidParentheses("(a)())()")) # Output: ["(a())()","(a)()()"]
print(solution.removeInvalidParentheses(")("))        # Output: [""]
