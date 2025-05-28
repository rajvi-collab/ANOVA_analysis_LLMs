class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)
        has_lower = has_upper = has_digit = False
        for c in password:
            if c.islower():
                has_lower = True
            elif c.isupper():
                has_upper = True
            elif c.isdigit():
                has_digit = True

        missing_types = int(not has_lower) + int(not has_upper) + int(not has_digit)

        # Count replacements needed for 3+ repeating characters
        i = 2
        repeat = []
        while i < n:
            if password[i] == password[i - 1] == password[i - 2]:
                length = 2
                while i < n and password[i] == password[i - 1]:
                    length += 1
                    i += 1
                repeat.append(length)
            else:
                i += 1

        total_replace = sum(r // 3 for r in repeat)

        if n < 6:
            return max(missing_types, 6 - n)
        elif n <= 20:
            return max(missing_types, total_replace)
        else:
            # Too long, must delete some characters
            delete = n - 20
            left_delete = delete

            # Reduce replace count by using deletions on repeating characters
            for i in range(len(repeat)):
                if left_delete <= 0:
                    break
                r = repeat[i]
                if r >= 3:
                    reduce = min(left_delete, r - 2)
                    repeat[i] -= reduce
                    left_delete -= reduce

            # After deletions, recalculate total replacements needed
            total_replace = sum(r // 3 for r in repeat)
            return delete + max(missing_types, total_replace)
