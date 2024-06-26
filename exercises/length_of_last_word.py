""""
Given a string s consists of some words separated by spaces, return the length of the last word in the string. If the
last word does not exist, return 0.

A word is a maximal substring consisting of non-space characters only.


Example 1:

Input: s = "Hello World"
Output: 5
Example 2:

Input: s = " "
Output: 0


Constraints:

1 <= s.length <= 104
s consists of only English letters and spaces ' '.
"""


def lengthOfLastWord(self, s: str) -> int:

    # removes the non-char at the beginning and at the end of the string
    s = s.strip()
    words = s.split(" ")

    if len(words[len(words) - 1]) > 0:
        return len(words[len(words) - 1])

    return 0


if __name__ == "__main__":
    s = "Hello World"
    lengthOfLastWord(s)
