""""
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, S.
Both players have to make substrings using the letters of the string S.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string S.

For Example:
String S = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

Your task is to determine the winner of the game and their score.

Input Format

A single line of input containing the string S.
Note: The string S will contain only uppercase letters: [A - Z].

Constraints
0 < len(S) <= 10^6

Output Format
Print one line: the name of the winner and their score separated by a space.
If the game is a draw, print Draw.

Sample Input:
BANANA

Sample Output:
Stuart 12
"""


def get_winner(string):
    vowels = ["A", "E", "I", "O", "U"]
    Kevin = 0
    Stuart = 0

    for i in range(0, len(string)):
        if string[i] in vowels:
            Kevin += len(string) - i
        else:
            Stuart += len(string) - i

    return ("Stuart", Stuart) if Stuart > Kevin else ("Kevin", Kevin)


if __name__ == "__main__":
    winner = get_winner("BANANA")
    print("{0} {1}".format(*winner))
