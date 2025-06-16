class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Sort the candidates list to handle duplicates
        candidates.sort()

        # Initialize result list and current combination list
        result = []
        curr_combination = []

        # Define a helper function for backtracking
        def backtrack(start, remaining_target):
            if remaining_target == 0:
                # If target is reached, add the current combination to the result
                result.append(curr_combination[:])
                return

            for i in range(start, len(candidates)):
                # Skip duplicates to avoid duplicate combinations
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # If the current candidate exceeds the remaining target, break the loop
                if candidates[i] > remaining_target:
                    break

                # Add the current candidate to the current combination
                curr_combination.append(candidates[i])

                # Recursively call backtrack with updated parameters
                backtrack(i + 1, remaining_target - candidates[i])

                # Remove the last added candidate from the current combination for backtracking
                curr_combination.pop()

        # Call the helper function to start backtracking
        backtrack(0, target)

        return result