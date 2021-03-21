""""
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two
characters may map to the same character, but a character may map to itself.


Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true


Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
"""


def is_isomorphic(s: str, t: str) -> bool:
    map_letters = {}
    len_s = len(s)
    len_t = len(t)

    if len_s != len_t:
        return False

    for i in range(0, len_s):
        if s[i] in map_letters and t[i] != map_letters[s[i]]:
            return False

        if s[i] not in map_letters and t[i] in map_letters.values():
            return False

        map_letters[s[i]] = t[i]

    return t == ''.join([map_letters.get(s[v]) for v in range(0, len_s) \
                         if map_letters.get(s[v]) is not None])


if __name__ == "__main__":
    s = "paper"
    t = "title"
    print(is_isomorphic(s, t))