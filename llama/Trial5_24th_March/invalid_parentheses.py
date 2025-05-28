# 4th attempts =====================

from collections import deque
from typing import List

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        # Define the level of invalidity (number of removals needed)
        level = {s}

        while True:
            # Check if any string in the current level is valid
            valid_strings = [string for string in level if self.isValid(string)]

            # If there are valid strings, return them
            if valid_strings:
                return valid_strings

            # Otherwise, generate the next level by removing one parenthesis at a time
            next_level = set()
            for string in level:
                for i in range(len(string)):
                    if string[i] in ('(', ')'):
                        next_level.add(string[:i] + string[i+1:])

            # Move to the next level
            level = next_level

    def isValid(self, s: str) -> bool:
        """Check if a string has balanced parentheses."""
        balance = 0

        for char in s:
            if char == '(':
                balance += 1
            elif char == ')':
                balance -= 1

            # If the balance is negative at any point, return False
            if balance < 0:
                return False

        # Return True if the final balance is zero (i.e., the parentheses are balanced)
        return balance == 0