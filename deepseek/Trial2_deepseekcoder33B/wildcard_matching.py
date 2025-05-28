# Single attempt

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        len_s = len(s)
        len_p = len(p)

        # DP table
        dp = [[False] * (len_p + 1) for _ in range(len_s + 1)]

        # Empty string matches empty pattern
        dp[0][0] = True

        # Only '*' can match an empty string
        for i in range(1, len_p + 1):
            if p[i - 1] == '*':
                dp[0][i] = dp[0][i - 1]

        for i in range(1, len_s + 1):
            for j in range(1, len_p + 1):
                if p[j - 1] == '*':
                    # '*' matches any sequence of characters or empty sequence
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    # '?' matches any single character or exact match with s's character
                    dp[i][j] = dp[i - 1][j - 1]

        return dp[-1][-1]