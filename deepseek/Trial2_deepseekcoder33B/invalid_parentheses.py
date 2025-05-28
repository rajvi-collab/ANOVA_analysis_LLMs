# Attempt 1st
# Runtime error

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        """
        :type s: str
        :rtype: List[str]
        """
        def is_valid(s):
            cnt = 0
            for ch in s:
                if ch == '(':
                    cnt += 1
                elif ch == ')':
                    cnt -= 1
                    if cnt < 0:
                        return False
            return cnt == 0

        level = {s}
        while True:
            valid = filter(is_valid, level)
            if valid:
                return valid
            level = {st[:i] + st[i+1:] for st in level for i in range(len(st))}

# Attempt 2

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isValid(s: str) -> bool:
            cnt = 0
            for ch in s:
                if ch == '(':
                    cnt += 1
                elif ch == ')':
                    cnt -= 1
                    if cnt < 0:
                        return False
            return cnt == 0

        level = {s}  # start from set to remove duplicate
        while True:
            valid = filter(isValid, level)
            if valid:   # if there is any valid string
                return list(valid)

            # BFS search for next level
            level = {s[:i] + s[i+1:] for s in level for i in range(len(s))}

# Attempt 3
# 1 / 129 testcases passed

from typing import List
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        left = right = 0
        for ch in s:
            if ch == '(':
                left += 1
            elif ch == ')':
                if left != 0:
                    left -= 1
                else:
                    right += 1
        res = set()

        def dfs(depth, idx, left_count, right_count, left_rem, right_rem, cur):
            if depth == len(s):
                if left_rem == 0 and right_rem == 0:
                    res.add(cur)
            else:
                # The character is '(' or ')'
                if s[depth] == '(' and left_count > 0: dfs(depth + 1, idx, left_count - 1, right_count, left_rem, right_rem, cur)
                if s[depth] == ')' and right_count > 0: dfs(depth + 1, idx, left_count, right_count - 1, left_rem, right_rem, cur)

                # The character is not a parenthesis or it's a matching parenthesis.
                if s[depth] != '(' and s[depth] != ')' or idx < len(cur) and s[depth] == cur[-1]:
                    dfs(depth + 1, idx + 1, left_count, right_count, left_rem - (s[depth] == '('), right_rem - (s[depth] == ')'), cur + s[depth])

        dfs(0, 0, left, right, left, right, "")
        return list(res)


# Attempt 4 Succesfull

from typing import List
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(s):
            count = 0
            for ch in s:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1
                    if count < 0: return False
            return count == 0

        level = {s}  # start from original string and then gradually remove one character each time.
        while True:
            valid = list(filter(is_valid, level))
            if valid:  # if we find a valid string at some point, it's the answer.
                return valid
            next_level = set()
            for item in level:
                for i in range(len(item)):
                    if item[i] in '()':  # only remove parentheses
                        next_level.add(item[:i] + item[i+1:])
            level = next_level
        return []