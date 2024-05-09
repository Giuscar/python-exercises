"""
Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
Example 3:

Input: s = "a"
Output: "a"
Example 4:

Input: s = "ac"
Output: "a"


Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters (lower-case and/or upper-case),
"""


def calculate_max_palindrome(s):
    res = ""
    len_res = 0

    for i in range(len(s)):
        # even number
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l + 1 > len_res:
                res = s[l : r + 1]
                len_res = r - l + 1
            l -= 1
            r += 1

        # odd number
        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l + 1 > len_res:
                res = s[l : r + 1]
                len_res = r - l + 1
            l -= 1
            r += 1

    return res


if __name__ == "__main__":
    print(calculate_max_palindrome("babad"))
