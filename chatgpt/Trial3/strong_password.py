# all testcases passed
class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)

        # Flags to track missing character types
        has_lower = has_upper = has_digit = False
        for c in password:
            if c.islower():
                has_lower = True
            elif c.isupper():
                has_upper = True
            elif c.isdigit():
                has_digit = True

        missing_types = 3 - (has_lower + has_upper + has_digit)

        # Count sequences with three or more repeated characters
        replace = 0
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

        if n < 6:
            return max(missing_types, 6 - n)

        elif n <= 20:
            return max(missing_types, replace)

        else:
            delete = n - 20
            # Prioritize deleting in sequences that reduce replace count
            # Remove one character from sequences where len % 3 == 0
            reduce = min(delete, one_mod)
            replace -= reduce
            delete -= reduce

            # Remove two characters from sequences where len % 3 == 1
            reduce = min(delete // 2, two_mod)
            replace -= reduce
            delete -= reduce * 2

            # Remove three characters from the rest
            reduce = delete // 3
            replace -= reduce
            # Final answer is deletions + remaining replacements (if any) + missing types
            return (n - 20) + max(missing_types, replace)
