class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)
        # Check for missing character types
        has_lower = any(c.islower() for c in password)
        has_upper = any(c.isupper() for c in password)
        has_digit = any(c.isdigit() for c in password)
        missing_types = 3 - (has_lower + has_upper + has_digit)
        # Identify repeating characters
        replace = 0
        one_seq = two_seq = 0
        i = 2
        while i < n:
            if password[i] == password[i-1] == password[i-2]:
                length = 2
                while i < n and password[i] == password[i-1]:
                    length += 1
                    i += 1
                replace += length // 3
                if length % 3 == 0:
                    one_seq += 1
                elif length % 3 == 1:
                    two_seq += 1
            else:
                i += 1
        # If password is too short
        if n < 6:
            return max(6 - n, missing_types)
        # If password is within the valid range
        elif n <= 20:
            return max(missing_types, replace)
        # If password is too long
        else:
            delete_count = n - 20
            # First, fix sequences using deletions
            replace -= min(delete_count, one_seq)
            delete_count -= min(delete_count, one_seq)
            replace -= min(delete_count, two_seq * 2) // 2
            delete_count -= min(delete_count, two_seq * 2)
            replace -= delete_count // 3
            return (n - 20) + max(missing_types, replace)
