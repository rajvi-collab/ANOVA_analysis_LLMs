# 129 / 129 testcases passed

from typing import List

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
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

        level = {s}
        while True:
            valid = list(filter(is_valid, level))
            if valid:
                return valid
            next_level = set()
            for item in level:
                for i in range(len(item)):
                    if item[i] in ('(', ')'):
                        next_level.add(item[:i] + item[i + 1:])
            level = next_level