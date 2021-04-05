""""
You have a list of words and a pattern, and you want to know which words in words matches the pattern.
A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the
pattern with p(x), we get the desired word.
(Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and
no two letters map to the same letter.)
Return a list of the words in words that match the given pattern.
You may return the answer in any order.

Example 1:

Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]
Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}.
"ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation,
since a and b map to the same letter.


Note:

1 <= words.length <= 50
1 <= pattern.length = words[i].length <= 20
"""

""""
Solution to be improved:
def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
    output = []
    for word in words:
        mappings = {}
        if len(word) == len(pattern):
            idx = 0
            current_word = word
            tmp_s = list()
            for letter in word:
                if mappings.get(letter) and pattern[idx] == mappings[letter]:
                    idx += 1
                    tmp_s.append(letter)
                else:
                    mappings[letter] = pattern[idx]
                    idx += 1
                    
            if ''.join(tmp_s) == current_word:
                print('here')
                output.append(current_word)
            del tmp_s
            del current_word
    return output
"""
from typing import List, Iterator


def find_and_replace_pattern(words: List[str], pattern: str) -> Iterator[str]:
    def match(word):
        mappings = {}
        for x, y in zip(pattern, word):
            if mappings.setdefault(x, y) != y:
                return False
        return len(set(mappings.values())) == len(mappings.values())

    return filter(match, words)


if __name__ == "__main__":
    print('\n'.join(find_and_replace_pattern(["abc", "deq", "mee", "aqq", "dkd", "ccc"], "abb")))
