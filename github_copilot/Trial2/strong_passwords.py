class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)
        has_lower = any(c.islower() for c in password)
        has_upper = any(c.isupper() for c in password)
        has_digit = any(c.isdigit() for c in password)
        categories = sum([has_lower, has_upper, has_digit])
        if n < 6:
            return max(6 - n, 3 - categories)
        change = 0
        one = two = three = 0
        i = 2
        while i < n:
            if password[i] == password[i - 1] == password[i - 2]:
                length = 2
                while i < n and password[i] == password[i - 1]:
                    length += 1
                    i += 1
                change += length // 3
                if length % 3 == 0:
                    one += 1
                elif length % 3 == 1:
                    two += 1
                else:
                    three += 1
            else:
                i += 1
        if n <= 20:
            return max(change, 3 - categories)
        delete = n - 20
        change -= min(delete, one)
        change -= min(max(delete - one, 0), two * 2) // 2
        change -= max(delete - one - 2 * two, 0) // 3
        return delete + max(change, 3 - categories)

