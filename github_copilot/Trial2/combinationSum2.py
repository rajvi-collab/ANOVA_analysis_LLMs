from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        results = []
        def backtrack(remaining, comb, start):
            if remaining == 0:
                results.append(list(comb))
                return
            elif remaining < 0:
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                comb.append(candidates[i])
                backtrack(remaining - candidates[i], comb, i + 1)
                comb.pop()
        backtrack(target, [], 0)
        return results


