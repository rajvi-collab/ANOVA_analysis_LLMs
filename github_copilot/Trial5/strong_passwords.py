# took 3 attempts =============
# 50 / 54 testcases passed

class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)
        has_lower = any(c.islower() for c in password)
        has_upper = any(c.isupper() for c in password)
        has_digit = any(c.isdigit() for c in password)

        # Count consecutive repeating characters
        repeat_groups = []
        i = 2
        while i < n:
            if password[i] == password[i - 1] == password[i - 2]:
                length = 2
                while i < n and password[i] == password[i - 1]:
                    length += 1
                    i += 1
                repeat_groups.append(length)
            else:
                i += 1

        steps_to_add = int(not has_lower) + int(not has_upper) + int(not has_digit)

        if n < 6:
            # If the password is too short, we need to both add characters and meet the other requirements
            return max(6 - n, steps_to_add)
        elif n > 20:
            # If the password is too long, we need to delete characters
            excess_length = n - 20
            repeat_groups.sort(key=lambda x: x % 3)

            # Reduce the length by breaking repeating groups
            for i in range(len(repeat_groups)):
                if excess_length <= 0:
                    break
                if repeat_groups[i] >= 3:
                    to_remove = min(repeat_groups[i] - 2, excess_length)
                    repeat_groups[i] -= to_remove
                    excess_length -= to_remove

            # Any leftover excess length will directly reduce groups
            repeat_groups = [max(0, group - excess_length) for group in repeat_groups]
            excess_length = max(0, excess_length - sum(repeat_groups))

            return (n - 20) + max(steps_to_add, sum(group // 3 for group in repeat_groups))
        else:
            # If the password length is within bounds, just fix the repeating characters
            return max(steps_to_add, sum(group // 3 for group in repeat_groups))