""""
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
You can use each character in text at most once. Return the maximum number of instances that can be formed.


Example 1:
Input: text = "nlaebolko"
Output: 1
Example 2:

Input: text = "loonbalxballpoon"
Output: 2

Example 3:

Input: text = "leetcode"
Output: 0


Constraints:

1 <= text.length <= 10^4
text consists of lower case English letters only.
"""
from itertools import groupby


def max_number_of_balloons(text: str) -> int:
    occurrences = {}
    occ = 0
    string_to_find = "balloon"

    text = sorted(text)
    for k, v in groupby(text):
        occurrences[k] = len(list(v))

    while True:
        for char in string_to_find:
            if occurrences.get(char) and occurrences[char] > 0:
                occurrences[char] -= 1
            else:
                return occ

        occ += 1

    return occ


if __name__ == "__main__":
    print(max_number_of_balloons("loonbalxballpoon"))