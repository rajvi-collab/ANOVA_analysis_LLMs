from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Sort the candidates array in ascending order
        candidates.sort()

        # Initialize an empty list to store the result
        result = []

        # Define a helper function for backtracking
        def backtrack(remain, comb, start):
            if remain == 0:
                # If the remaining target is zero, add the current combination to the result
                result.append(list(comb))
                return

            for i in range(start, len(candidates)):
                # Skip duplicates to avoid duplicate combinations
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Check if adding the current candidate exceeds the target
                if candidates[i] > remain:
                    break

                # Add the current candidate to the combination and update the remaining target
                comb.append(candidates[i])
                backtrack(remain - candidates[i], comb, i + 1)

                # Remove the last added candidate for backtracking
                comb.pop()

        # Start the backtracking process with an empty combination and a starting index of zero
        backtrack(target, [], 0)
        return result


# Example usage:
if __name__ == "__main__":
    solution = Solution()

    candidates = [10,1,2,7,6,1,5]
    target = 8

    result = solution.combinationSum2(candidates, target)
    print(result)
    # Output:
    # [
    #   [1,1,6],
    #   [1,2,5],
    #   [1,7],
    #   [2,6]
    # ]

    candidates = [2,5,2,1,2]
    target = 5

    result = solution.combinationSum2(candidates, target)
    print(result)
    # Output:
    # [
    #   [1,2,2],
    #   [5]
    # ]