from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()  # Sort to handle duplicates easily
        self.backtrack(candidates, target, 0, [], res)
        return res
    def backtrack(self, candidates, target, start, path, res):
        if target == 0:
            res.append(list(path))
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:  # Skip duplicates
                continue
            if candidates[i] > target:  # No need to continue if the number exceeds target
                break
            path.append(candidates[i])
            self.backtrack(candidates, target - candidates[i], i + 1, path, res)
            path.pop()  # Backtrack

