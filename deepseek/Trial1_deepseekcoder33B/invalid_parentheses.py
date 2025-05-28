# Attempt 1st ======================
'''
TypeError: <filter object at 0x7fa11d067fd0> is not valid value for the expected return type list<string>
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    raise TypeError(str(ret) + " is not valid value for the expected return type list<string>");
'''
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        """
        :type s: str
        :rtype: List[str]
        """
        def isValid(s):
            count = 0
            for ch in s:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1
                    if count < 0: return False
            return count == 0

        level = {s} # start from original string
        while True:
            valid = filter(isValid, level)
            if valid:
                return valid
            level = {st[:i] + st[i+1:] for st in level for i in range(len(st))}



# 4 / 129 testcases passed
class Solution:
    def removeInvalidParentheses(self, s):
        def isValid(s):
            cnt = 0
            for i in range(len(s)):
                if s[i] == '(':
                    cnt += 1
                elif s[i] == ')':
                    cnt -= 1
                    if cnt < 0: return False
            return cnt == 0
        level = {s}
        while True:
            valid = filter(isValid, level)
            if valid:
                return list(valid)
            level = {s[:i] + s[i+1:] for s in level for i in range(len(s))}





# 129 / 129 testcases passed
from collections import deque
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(s):
            count = 0
            for c in s:
                if c == '(':
                    count += 1
                elif c == ')':
                    if count == 0:
                        return False
                    count -= 1
            return count == 0

        level = {s}  # level set of BFS, each string in the level is one removal away from the original string
        while True:
            valid = [*filter(is_valid, level)]
            if valid:
                return valid  # If we found valid strings at this level, then they are the answer

            # Otherwise add a layer of strings to 'level' for next BFS iteration
            level = {s[:i] + s[i+1:] for s in level for i in range(len(s)) if s[i] in "()"}
