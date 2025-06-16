from collections import deque
class Solution:
    def removeInvalidParentheses(self, s: str):
        level = {s}
        while True:
            valid = list(filter(self.isValid, level))
            if valid:
                return valid
            level = {s[:i] + s[i+1:] for s in level for i in range(len(s)) if s[i] in ('(', ')')}
    def isValid(self, s: str):
        count = 0
        for c in s:
            if c == '(':
                count += 1
            elif c == ')':
                if count == 0:
                    return False
                count -= 1
        return count == 0


# Example usage:
if __name__ == "__main__":
    solution = Solution()

    print(solution.removeInvalidParentheses("()())()"))
    # Output: ["(())()", "()()()"]

    print(solution.removeInvalidParentheses("(a)())()"))
    # Output: ["(a())()", "(a)()()"]

    print(solution.removeInvalidParentheses(")("))
    # Output: [""]