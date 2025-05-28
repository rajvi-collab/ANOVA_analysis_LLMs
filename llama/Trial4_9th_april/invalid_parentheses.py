class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        # Define helper function to check if a string is valid
        def isValid(string):
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    if count == 0:
                        return False
                    count -= 1
            return count == 0

        # Initialize queue with the input string and its level (number of removals)
        queue = [(s, 0)]
        visited = {s}
        result = []
        min_removals = float('inf')

        while queue:
            current_string, level = queue.pop(0)

            # If the current string is valid and has fewer removals than before,
            # update the result list
            if isValid(current_string):
                if level < min_removals:
                    min_removals = level
                    result = [current_string]
                elif level == min_removals:
                    result.append(current_string)

            # If we have already found a valid string with fewer removals, stop exploring
            # this branch of the queue
            if level > min_removals:
                continue

            # Generate all possible strings by removing one parenthesis at a time
            for i in range(len(current_string)):
                if current_string[i] in ('(', ')'):
                    new_string = current_string[:i] + current_string[i+1:]
                    if new_string not in visited:
                        queue.append((new_string, level + 1))
                        visited.add(new_string)

        return result