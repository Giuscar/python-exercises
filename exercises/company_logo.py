""""
A newly opened multinational brand has decided to base their company logo on the three most common characters in the
company name. They are now trying out various combinations of company names and logos based on this condition. Given a
string s, which is the company name in lowercase letters, your task is to find the top three most common characters in
the string.

- Print the three most common characters along with their occurrence count.
- Sort in descending order of occurrence count.
- If the occurrence count is the same, sort the characters in alphabetical order.
For example, according to the conditions described above,

GOOGLE would have it's logo with the letters G,O,E.

Input Format

A single line of input containing the string S.

Constraints
3 <= len(S) <= 10^4

Output Format
Print the three most common characters along with their occurrence count each on a separate line.
Sort output in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.

Sample Input 0
aabbbccde

Sample Output 0
b 3
a 2
c 2
Explanation 0
aabbbccde

Here, b occurs 3 times. It is printed first.
Both a and c occur 2 times. So, a is printed in the second line and c in the third line because a comes before c in the
alphabet.

Note: The string S has at least 3 distinct characters.
"""
from itertools import groupby


def generate_new_company_logo(s):
    res = []
    for k, g in groupby(sorted(s)):
        res.append((k, len(list(g))))
    res.sort(key=lambda f: f[1], reverse=True)

    for i in range(0, 3):
        if i <= len(res):
            print("{} {}".format(res[i][0], res[i][1]))


if __name__ == "__main__":
    generate_new_company_logo("aabbbccde")
    # TODO: implement solution with OrderedCount. See the following documentation:
    # https://docs.python.org/3.4/library/collections.html?highlight=ordereddict#ordereddict-examples-and-recipes)