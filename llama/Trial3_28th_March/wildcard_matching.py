class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

        # Initialize the base case where both strings are empty
        dp[0][0] = True

        # Handle '*' in the pattern when the input string is empty
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]

        # Fill up the dynamic programming table
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                else:
                    dp[i][j] = (p[j - 1] == s[i - 1] or p[j - 1] == '?') and dp[i - 1][j - 1]

        return dp[len(s)][len(p)]