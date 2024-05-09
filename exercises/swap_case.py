""""
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase
letters and vice versa.

Input Format:
A single line containing a string S.

Constraints:
Print the modified string S.
"""


def swap_the_string(string_to_swap):
    print("".join([c.lower() if c.isupper() else c.upper() for c in string_to_swap]))


if __name__ == "__main__":
    string_to_swap = "I am A sOftware Engineer"
    swap_the_string(string_to_swap)
