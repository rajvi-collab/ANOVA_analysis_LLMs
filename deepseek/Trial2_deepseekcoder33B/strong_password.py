# 10 / 54 testcases passed

import re
from collections import Counter

class Solution:
    def strongPasswordChecker(self, s: str) -> int:
        n = len(s)

        lower_case = 1 if re.search('[a-z]', s) else 0
        upper_case = 1 if re.search('[A-Z]', s) else 0
        digit = 1 if re.search('\d', s) else 0

        repeating_characters = [len(m.group()) for m in re.finditer(r'(\w)\1*', s)]

        missing_type = 3 - (lower_case + upper_case + digit)

        if n < 6:
            return max(missing_type, 6-n)
        else:
            deleting = sum([i//3 for i in repeating_characters])

            while deleting > 0 and n > 20:
                deleting -= 1
                n -= 1

            changing = 0
            replacing_chars = [c for c in s if (s.count(c) % 3 == 0) and (s.count(c) >= 6)]

            while len(set(replacing_chars)) > 0:
                if deleting > changing:
                    n -= 1
                    replacing_char = max([s.count(c) for c in set(replacing_chars)])
                    repeating_characters[repeating_characters.index(replacing_char)] -= min(deleting-changing, 3 if (replacing_char % 3 ==0) else 2)
                else:
                    replacing_char = max([s.count(c) for c in set(replacing_chars)])
                    repeating_characters[repeating_characters.index(replacing_char)] -= min((3 if (replacing_char % 3 == 0) else 2),changing)
                replacing_chars = [c for c in s if (s.count(c) % 3 == 0) and (s.count(c) >= 6)]

            return deleting + max(sum([i//3 for i in repeating_characters]), missing_type, n - 20)




# 11 / 54 testcases passed

import re
from collections import Counter

class Solution:
    def strongPasswordChecker(self, s: str) -> int:
        # count the number of each type of character
        missing_types = [not re.search('[a-z]', s), not re.search('[A-Z]', s), not re.search('\d', s)]

        n = len(s)
        if n < 6:
            return max(3 - sum(missing_types), 6 - n)

        # calculate the number of repeating characters that need to be replaced or deleted
        repeats, one_char_repeats, two_char_repeats = 0, 0, 0
        i = j = 0

        while j < n:
            if s[i] == s[j]:
                j += 1
            else:
                if j - i > 2:
                    repeats += (j-i) // 3
                    if (j-i) % 3 == 0:
                        one_char_repeats += 1
                    elif (j-i) % 3 == 1:
                        two_char_repeats += 1
                i = j

        if j - i > 2:
            repeats += (j-i) // 3
            if (j-i) % 3 == 0:
                one_char_repeats += 1
            elif (j-i) % 3 == 1:
                two_char_repeats += 1

        # decide on the best course of action: replace, delete or insert
        if n > 20:
            deletes = n - 20
            changes = max(deletes, one_char_repeats) + two_char_repeats * 2

            # handle edge case when we can only delete
            changes = max(changes, repeats) if changes == deletes else changes
        else:
            changes = max(sum(missing_types), repeats)

        return n - 20 + max(changes, sum(missing_types))



# 20 / 54 testcases passed

class Solution:
    def strongPasswordChecker(self, s: str) -> int:
        missing_types = [not any('a' <= c <= 'z' for c in s), not any('A' <= c <= 'Z' for c in s), not any(c.isdigit() for c in s)]

        n = len(s)
        if n < 6:
            return max(3 - sum(missing_types), 6 - n)

        repeats, one_char_repeats, two_char_repeats = 0, 0, 0
        i = 0
        while i < n:
            length = 1
            while i + length < n and s[i + length] == s[i]:
                length += 1

            repeats += (length // 3)
            if length % 3 == 2:
                two_char_repeats += 1
            elif length % 3 == 1:
                one_char_repeats += 1

            i += length

        if n <= 20:
            return max(sum(missing_types), repeats)

        deletes = n - 20

        # If we have enough deletions to remove one repeat, do that
        if one_char_repeats <= deletes:
            return max(deletes, sum(missing_types)) + two_char_repeats * 2

        # Else, delete from the repeats and try to replace some of them later.
        changes = deletes + two_char_repeats
        one_char_repeats -= min(deletes, one_char_repeats)

        # If we have enough deletions to remove a repeat but not 3 repeats at once,
        # do that and replace some of them later.
        changes += (one_char_repeats // 2) * 2 + one_char_repeats % 2

        return max(changes, sum(missing_types))


# Same answers after this