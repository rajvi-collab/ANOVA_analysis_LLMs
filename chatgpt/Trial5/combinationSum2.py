from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(start: int, path: List[int], remaining: int):
            if remaining == 0:
                res.append(path[:])
                return
            for i in range(start, len(candidates)):
                # Skip duplicates at the same depth
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                # If the candidate exceeds the remaining target, no need to continue
                if candidates[i] > remaining:
                    break
                path.append(candidates[i])
                backtrack(i + 1, path, remaining - candidates[i])  # move to next index
                path.pop()

        backtrack(0, [], target)
        return res
