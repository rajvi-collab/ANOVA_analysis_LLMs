class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)
        has_lower = has_upper = has_digit = False
        replace = 0
        one_mod = two_mod = 0  # For counting repeating sequences
        i = 0
        while i < n:
            if password[i].islower():
                has_lower = True
            if password[i].isupper():
                has_upper = True
            if password[i].isdigit():
                has_digit = True
            length = 1
            while i + 1 < n and password[i] == password[i + 1]:
                length += 1
                i += 1
            if length >= 3:
                replace += length // 3
                if length % 3 == 0:
                    one_mod += 1
                elif length % 3 == 1:
                    two_mod += 1
            i += 1
        missing_types = 3 - (has_lower + has_upper + has_digit)
        if n < 6:
            return max(6 - n, missing_types)
        elif n <= 20:
            return max(replace, missing_types)
        else:
            delete_count = n - 20
            replace -= min(delete_count, one_mod) // 1
            replace -= min(max(delete_count - one_mod, 0), two_mod * 2) // 2
            replace -= max(delete_count - one_mod - 2 * two_mod, 0) // 3
            return delete_count + max(replace, missing_types)

# Attempt 1st ==============================
# 54 / 54 testcases passed
# 3 Attempt -  added wrong testcase, remove constrain

# Example usage
sol = Solution()
print(sol.strongPasswordChecker("a"))  # Output: 5
print(sol.strongPasswordChecker("aA1"))  # Output: 3
print(sol.strongPasswordChecker("1337C0d3"))  # Output: 0
print(sol.strongPasswordChecker("bbaaaaaaaaaaaaaaacccccc"))  # Output: 8


