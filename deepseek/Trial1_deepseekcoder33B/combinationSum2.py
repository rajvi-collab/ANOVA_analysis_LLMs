# Attempt 1st ======================
# 176 / 176 testcases passed
# 1 time Ran - without constarined

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidates, begin, size, path, res, remain):
            if remain == 0:
                res.append(path[:])
                return

            for index in range(begin, size):
                # We can not use the same number again, so we need to skip duplicates.
                if index > begin and candidates[index] == candidates[index - 1]:
                    continue

                pick = candidates[index]

                # If a candidate is too large, we cannot choose it.
                if remain < pick:
                    return

                path.append(pick)
                dfs(candidates, index + 1, size, path, res, remain - pick)
                path.pop()

        size = len(candidates)
        if size == 0:
            return []

        candidates.sort()
        path = []
        res = []
        dfs(candidates, 0, size, path, res, target)
        return res