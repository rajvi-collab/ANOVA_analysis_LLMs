class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)
        missing_types = 3
        has_lower = has_upper = has_digit = False
        
        for char in password:
            if char.islower() and not has_lower:
                missing_types -= 1
                has_lower = True
            elif char.isupper() and not has_upper:
                missing_types -= 1
                has_upper = True
            elif char.isdigit() and not has_digit:
                missing_types -= 1
                has_digit = True
        
        # Calculate the number of replacements needed for sequences of 3 or more repeating characters
        replace = 0
        one_seq = 0  # sequences that can be fixed by one replacement (length % 3 == 0)
        two_seq = 0  # sequences that can be fixed by two replacements (length % 3 == 1)
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
            return max(missing_types, replace)
        else:
            # When length > 20, deletions are needed
            delete = n - 20
            
            # Each deletion can help reduce the number of replacements needed
            replace -= min(delete, one_seq * 1) // 1
            replace -= min(max(delete - one_seq, 0), two_seq * 2) // 2
            replace -= max(delete - one_seq - two_seq * 2, 0) // 3
            
            return delete + max(missing_types, replace)