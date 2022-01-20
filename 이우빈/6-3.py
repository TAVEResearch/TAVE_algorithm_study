from typing import List

def reorderLogfiles(logs: List[str]) -> List[str]:
    letters, digits = [], []

    for log in logs:
        # Identifiers don't affect the order.
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    # If the letters are the same, do it in the order of identifiers.
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))

    return letters + digits # A letter log precedes a digit log.

# The first part of the log is the identifier.
logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]

print(reorderLogfiles(logs))