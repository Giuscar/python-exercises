""""
Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data
structure?
"""


def has_unique_char(s):
    return True if len(set(s)) < len(s) else False


if __name__ == "__main__":
    s = "aaaaaaaaa"
    print(has_unique_char(s))