# took 2 attempts
# 38 / 54 testcases passed

class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        missing_type = 3
        if any('a' <= c <= 'z' for c in password):
            missing_type -= 1
        if any('A' <= c <= 'Z' for c in password):
            missing_type -= 1
        if any(c.isdigit() for c in password):
            missing_type -= 1

        change = 0
        one = two = p = i = 0
        while i < len(password):
            length = 1
            while i + 1 < len(password) and password[i] == password[i+1]:
                i += 1
                length += 1
            if length >= 3:
                change += length // 3
                if length % 3 == 0:
                    one += 1
                elif length % 3 == 1:
                    two += 1
                else:
                    p += 1
            i += 1

        if len(password) < 6:
            return max(missing_type, 6 - len(password))
        elif len(password) <= 20:
            return max(missing_type, change)
        else:
            delete = len(password) - 20

            change -= min(delete, one)
            change -= min(max(delete - one, 0), two * 2) // 2
            change -= max(delete - one - 2 * two, 0) // 3

            return delete + max(missing_type, change)