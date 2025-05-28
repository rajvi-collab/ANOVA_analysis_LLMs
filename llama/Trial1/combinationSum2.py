from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        def backtrack(remain, comb, start):
            if remain == 0:
                result.append(list(comb))
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > remain:
                    break
                comb.append(candidates[i])
                backtrack(remain - candidates[i], comb, i + 1)
                comb.pop()
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