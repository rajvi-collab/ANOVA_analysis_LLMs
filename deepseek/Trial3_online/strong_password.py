class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)
        missing_types = 3
        if any('a' <= c <= 'z' for c in password):
            missing_types -= 1
        if any('A' <= c <= 'Z' for c in password):
            missing_types -= 1
        if any(c.isdigit() for c in password):
            missing_types -= 1
        # Handle repeating sequences
        replace = 0
        one_seq = 0  # sequences of length 3k
        two_seq = 0   # sequences of length 3k+1
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
        if n < 6:
            return max(6 - n, missing_types)
        elif n <= 20:
            return max(replace, missing_types)
        else:
            # When length > 20, deletions are needed
            delete = n - 20
            # Each deletion can help reduce the number of replacements needed
            # For sequences with length % 3 == 0, each deletion reduces replace by 1
            replace -= min(delete, one_seq * 1) // 1
            replace -= max(min(delete - one_seq, two_seq * 2), 0) // 2
            replace -= max(delete - one_seq - 2 * two_seq, 0) // 3
            return delete + max(replace, missing_types)