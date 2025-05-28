# Attempt 1st ======================
# 19 / 54 testcases passed

class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        # Helper functions to check character conditions.
        def is_lower(c): return 'a' <= c <= 'z'
        def is_upper(c): return 'A' <= c <= 'Z'
        def is_digit(c): return '0' <= c <= '9'

        # Counters for missing character categories and sequences.
        lowers = sum(is_lower(c) for c in password)
        uppers = sum(is_upper(c) for c in password)
        digits = sum(is_digit(c) for c in password)

        # Count repeating characters sequences.
        repeats, length = 0, len(password)
        i, prev = 0, None
        while i < length:
            j = i + 1
            while j < length and password[j] == password[i]:
                j += 1

            if j - i >= 3:
                repeats += (j-i) // 3
            i = j

        # Check password conditions.
        steps = 0
        if length < 6:
            steps = max(steps, 6 - length)
        elif length > 20:
            steps = min(repeats, length - 20)

        missing_types = 3 - (lowers > 0) - (uppers > 0) - (digits > 0)

        if len(password) <= 20:
            return max(steps, missing_types)
        else:
            lowers = max(0, 6 - repeats - missing_types)
            uppers = max(0, 6 - repeats - missing_types - (lowers > 0))
            digits = max(0, 6 - repeats - missing_types - (lowers > 0) - (uppers > 0))

            return steps + lowers + uppers + digits


# testcase not passes input: password="aaa111" output got: 1, Expected output: 2
# 11 / 54 testcases passed
class Solution:
    def strongPasswordChecker(self, s: str) -> int:
        missing_types = max(3 - len({c for c in set(s)} & {"lowercase", "uppercase", "digit"}), 0)
        total_changes = 0
        one = two = 0
        p = 2
        while p < len(s):
            if s[p] == s[p-1] == s[p-2]:
                length = 2
                while p < len(s) and s[p] == s[p-1]:
                    length += 1
                    p += 1

                total_changes += length // 3
                if length % 3 == 0: one += 1
                elif length % 3 == 1: two += 1

            else:
                p += 1

        if len(s) < 6:
            return max(missing_types, total_changes, (total_changes - min(one, missing_types)) // 2 + one)
        elif len(s) <= 20:
            return max(missing_types, total_changes)
        else:
            delete = len(s) - 20

            total_changes -= min(delete, one)
            total_changes -= min(max(delete - one, 0), two * 2) // 2
            total_changes -= max(delete - one - 2 * two, 0) // 3

            return delete + max(missing_types, total_changes)

# Attempt 3rd === Same solution


