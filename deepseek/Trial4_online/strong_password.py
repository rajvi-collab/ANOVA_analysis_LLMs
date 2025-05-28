class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        missing_types = 3
        if any('a' <= c <= 'z' for c in password):
            missing_types -= 1
        if any('A' <= c <= 'Z' for c in password):
            missing_types -= 1
        if any(c.isdigit() for c in password):
            missing_types -= 1
        
        n = len(password)
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
            return max(missing_types, 6 - n)
        elif n <= 20:
            return max(missing_types, replace)
        else:
            delete = n - 20
            replace -= min(delete, one_seq * 1) // 1
            replace -= min(max(delete - one_seq, 0), two_seq * 2) // 2
            replace -= max(delete - one_seq - 2 * two_seq, 0) // 3
            return delete + max(missing_types, replace)