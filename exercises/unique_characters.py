""""
Implement an algorithm to determine if a string has all unique characters (i.e., no duplicata).
What if you cannot use additional data structure?
We provide three implementations - you can pick whatever you want in the main.

Note: empty strings return True.
"""

def has_unique_char_v1(s : str) -> bool:
    """ Use sets and remove duplicata. If the size of the set is 1, return True. """
    return True if len(set(s)) == len(s) else False

def has_unique_char_v2(s : str) -> bool:
    """ Don't rely on any other data structure """
    for char in s:
        if s.count(char) > 1:
            return False
    return True
    
def has_unique_char_v3(s : str) -> bool:
    """ Yet another method with string frequency"""
    from collections import Counter
    return True if len(set(Counter(s).values())) in range(0, 2) else False

if __name__ == "__main__":
    s1 = "abcdef"
    s2 = "abcdea"
    print("Does ", s1, "have unique chars? ", str(has_unique_char_v1(s1)))
    print("Does ", s2, "have unique chars? ", str(has_unique_char_v1(s2)))
