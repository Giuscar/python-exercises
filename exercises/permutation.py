""""
@Def: Given 2 strings, write a method to decide if one is a permutation of the other.

@Note: the 2 strings are considered anagram if they have the same characters,
in the same number, but the number of whitespaces/tabs and friends DOES NOT MATTER.

@Example: "dormitory" and "dirty room" are considered anagrams in this exercise.

@Sol: we propose one solution more classical, which calculates the permutations, and
another one less pedagogical but faster.
"""

import sys

def preproc_input(input_str : str) -> str:
    """Do some preprocessing - example checks on input, strip, all lowercase and so on"""
    if not isinstance(input_str, str):
        err_str = "The input ", input_str, " is not a Python string. Aborting."
        sys.exit(err_str)
    input_str = "".join(input_str.lower().split())
    if len(input_str) == 0:
        sys.exit("At least one input is an empty string - forbidden. Aborting.")
    else:
        return input_str


def calculate_permutation(s1 : str, s2 : str) -> bool:
    """ Return True whether s1 is a permutation of s2 """
    checker = {}

    if len(s1) != len(s2):
        return False

    for val in s1:
        idx_value = ord(val) - ord('a')
        if checker.get(idx_value):
            checker[idx_value] = checker.get(idx_value) + 1
        else:
            checker[idx_value] = 1

    for val in s2:
        idx_value = ord(val) - ord('a')
        if checker.get(idx_value) and checker[idx_value] > 0:
            checker[idx_value] = checker.get(idx_value) - 1
        else:
            return False
    return True


def check_anagram_fast(s1 : str, s2 : str) -> bool:
    """ Alternative to `calculate_permutation` method. Return True whether s1 is an anagram of s2"""
    return sorted(s1) == sorted(s2)


if __name__ == "__main__":
    s1 = "Tom Marvolo Riddle"
    s2 = "I am Lord Voldemort"
    s1 = preproc_input(s1)
    s2 = preproc_input(s2)
    print("They are anagrams (classical method)") if calculate_permutation(s1, s2) == True else print("They are NOT anagrams (classical method)")
    print("They are anagrams (shortcut method)") if check_anagram_fast(s1, s2) == True else print("They are NOT anagrams (shortcut method)")
