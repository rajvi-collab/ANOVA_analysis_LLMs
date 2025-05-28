class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        missing_type = 3
        if any('a' <= c <= 'z' for c in password):
            missing_type -= 1
        if any('A' <= c <= 'Z' for c in password):
            missing_type -= 1
        if any(c.isdigit() for c in password):
            missing_type -= 1

        one = two = replacements = 0
        i = 2
        while i < len(password):
            if password[i-2] == password[i-1] == password[i]:
                length = 2
                while i+1 < len(password) and password[i] == password[i+1]:
                    i += 1
                    length += 1
                if length % 3 == 0:
                    one += 1
                elif length % 3 == 1:
                    two += 1
                replacements += length // 3
            i += 1

        if len(password) < 6:
            return max(missing_type, 6 - len(password))
        elif len(password) <= 20:
            return max(missing_type, replacements)
        else:
            delete = len(password) - 20

            # Remove one character from sequences of three repeating characters
            replacements -= min(delete, one)

            # Remove two characters from sequences of four repeating characters
            replacements -= min(max(delete - one, 0), two * 2) // 2

            # Remove three characters from sequences of five or more repeating characters
            replacements -= max(delete - one - 2 * two, 0) // 3

            return delete + max(missing_type, replacements)