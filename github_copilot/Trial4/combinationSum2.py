from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, end, target, path):
            if target == 0:
                result.append(path)
                return
            if target < 0:
                return
            for i in range(start, end):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                backtrack(i + 1, end, target - candidates[i], path + [candidates[i]])
                
        candidates.sort()
        result = []
        backtrack(0, len(candidates), target, [])
        return result