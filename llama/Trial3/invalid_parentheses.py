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

        # Initialize the queue with the input string and a set to store unique results
        queue = deque([s])
        seen = {s}
        result = []
        found_valid = False

        while queue:
            curr_str = queue.popleft()

            # If the current string is valid, add it to the result list
            if is_valid(curr_str):
                result.append(curr_str)
                found_valid = True

            # If we've already found a set of valid strings, stop exploring further levels
            if found_valid:
                continue

            # Generate all possible strings by removing one parenthesis at a time
            for i in range(len(curr_str)):
                if curr_str[i] == '(' or curr_str[i] == ')':
                    new_str = curr_str[:i] + curr_str[i+1:]

                    # If the new string is not seen before, add it to the queue and mark as seen
                    if new_str not in seen:
                        queue.append(new_str)
                        seen.add(new_str)

        return result