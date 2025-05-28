class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        missing_type = 3
        if any('a' <= c <= 'z' for c in password):
            missing_type -= 1
        if any('A' <= c <= 'Z' for c in password):
            missing_type -= 1
        if any(c.isdigit() for c in password):
            missing_type -= 1
        one = two = p = i = 0
        while i < len(password):
            count = 1
            while i + 1 < len(password) and password[i] == password[i+1]:
                i += 1
                count += 1
            if count >= 3:
                one += count // 3
                two += (count - 1) // 3 if count % 3 == 1 else 0
                p += (count - 2) // 3 if count % 3 == 2 else 0
            i += 1
        if len(password) < 6:
            return max(missing_type, 6 - len(password))
        elif len(password) <= 20:
            return max(missing_type, one)
        else:
            delete = len(password) - 20
            one -= min(delete, one)
            two -= min(max(delete - one, 0), two * 2) // 2
            three = max(delete - one - 2 * two, 0)
            return delete + max(missing_type, one + two + three)



# Attempt 1st =======
# 34 / 54 testcases passed