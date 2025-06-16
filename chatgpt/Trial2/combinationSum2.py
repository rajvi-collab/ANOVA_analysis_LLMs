from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        def backtrack(start, target, path):
            if target == 0:
                result.append(path[:])
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > target:
                    break
                path.append(candidates[i])
                backtrack(i + 1, target - candidates[i], path)
                path.pop()
        backtrack(0, target, [])
        return result

# Example usage
solution = Solution()
print(solution.combinationSum2([10,1,2,7,6,1,5], 8))
print(solution.combinationSum2([2,5,2,1,2], 5))
