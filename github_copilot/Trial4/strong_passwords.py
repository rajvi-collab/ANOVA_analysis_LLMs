# Took 2 attemps
# 54 / 54 testcases passed

class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)

        has_lower = any(c.islower() for c in password)
        has_upper = any(c.isupper() for c in password)
        has_digit = any(c.isdigit() for c in password)
        
        categories = has_lower + has_upper + has_digit
        
        if n < 6:
            return max(6 - n, 3 - categories)
        elif n <= 20:
            replace = 0
            i = 2
            while i < n:
                if password[i] == password[i - 1] == password[i - 2]:
                    replace += 1
                    i += 3
                else:
                    i += 1
            return max(replace, 3 - categories)
        else:
            replace = 0
            remove = n - 20
            one_mod = two_mod = 0
            i = 2
            while i < n:
                if password[i] == password[i - 1] == password[i - 2]:
                    length = 2
                    while i < n and password[i] == password[i - 1]:
                        length += 1
                        i += 1
                    replace += length // 3
                    if length % 3 == 0:
                        one_mod += 1
                    elif length % 3 == 1:
                        two_mod += 1
                else:
                    i += 1

            if remove <= one_mod:
                replace -= remove
            elif remove - one_mod <= 2 * two_mod:
                replace -= (remove - one_mod) // 2 + one_mod
            else:
                replace -= (remove - one_mod - 2 * two_mod) // 3 + one_mod + two_mod

            return remove + max(replace, 3 - categories)

# Test case
password = "bbaaaaaaaaaaaaaaacccccc"
solution = Solution()
output = solution.strongPasswordChecker(password)
print(f"Output: {output}")  # Expected: 8