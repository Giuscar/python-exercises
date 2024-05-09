""""
Given 2 strings, write a method to decide if one is a permutation of the other.
"""


def calculate_permutation(s1, s2):
    checker = {}

    if len(s1) != len(s2):
        return False

    for val in s1:
        idx_value = ord(val) - ord("a")
        if checker.get(idx_value):
            checker[idx_value] = checker.get(idx_value) + 1
        else:
            checker[idx_value] = 1

    for val in s2:
        idx_value = ord(val) - ord("a")
        if checker.get(idx_value) and checker[idx_value] > 0:
            checker[idx_value] = checker.get(idx_value) - 1
        else:
            return False

    return True


if __name__ == "__main__":
    s1 = "cicoriandoli"
    s2 = "cicoriandoli"
    print("Yes") if calculate_permutation(s1, s2) == True else print("No")
