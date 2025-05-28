# Single attempt

from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(candidates, target, start, path, res):
            if target < 0:  # If the remaining sum is less than zero, we stop searching this branch.
                return

            elif target == 0:  # If the remaining sum equals to zero, we add it to the result list.
                res.append(path)

                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:  # If current candidate is same as previous one, skip to avoid duplicate
                    continue

                dfs(candidates, target-candidates[i], i+1, path + [candidates[i]], res)  # Recursive call with updated start index and reduced sum.

        candidates.sort()   # Sort the candidate list to easily skip duplicates in DFS search.
        res = []
        dfs(candidates, target, 0, [], res)

        return res
