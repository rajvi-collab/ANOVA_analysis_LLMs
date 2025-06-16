from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Sort the candidates list in ascending order
        candidates.sort()
        # Initialize an empty result list to store unique combinations
        result = []
        # Define a helper function for backtracking
        def backtrack(remain, comb, start):
            if remain == 0:
                # If the remaining target is zero, add the current combination to the result
                result.append(list(comb))
                return
            # Iterate over the candidates list starting from the 'start' index
            for i in range(start, len(candidates)):
                # Skip duplicates by checking if this candidate is the same as the previous one
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                # If the current candidate exceeds the remaining target, break the loop
                if candidates[i] > remain:
                    break
                # Add the current candidate to the combination
                comb.append(candidates[i])
                # Recursively call the backtrack function with updated parameters
                backtrack(remain - candidates[i], comb, i + 1)
                # Remove the last added candidate for backtracking
                comb.pop()
        # Call the backtrack function with initial parameters
        backtrack(target, [], 0)
        return result

# Example usage:
solution = Solution()
print(solution.combinationSum2([10,1,2,7,6,1,5], 8))
# Output: [[1,1,6],[1,2,5],[1,7],[2,6]]

print(solution.combinationSum2([2,5,2,1,2], 5))
# Output: [[1,2,2],[5]]