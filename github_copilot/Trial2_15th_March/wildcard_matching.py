class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        # dp[i][j] will be True if s[:i] matches p[:j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        # Empty string matches empty pattern
        dp[0][0] = True
        # Handle patterns with '*' at the start
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # '*' can match any sequence: dp[i][j-1] (empty sequence) or dp[i-1][j] (one or more chars)
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    # Match single character or '?'
                    dp[i][j] = dp[i - 1][j - 1]
        return dp[m][n]



