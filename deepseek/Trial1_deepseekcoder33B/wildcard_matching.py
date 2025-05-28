# Attempt 1st ======================
# 1811 / 1811 testcases passed
# 1 time Ran - without constarined

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

        # An empty pattern can only match with an empty string.
        dp[0][0] = True

        # Only '*' can match with an empty string.
        for i in range(1, len(p) + 1):
            if p[i - 1] != '*':
                break
            else:
                dp[0][i] = True

        # Build the DP table.
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]

        # The answer is in the bottom-right corner of the DP table.
        return dp[-1][-1]