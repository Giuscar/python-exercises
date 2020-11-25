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

def print_winner(string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    Kevin = 0
    Stuart = 0
    for i in range(len(string)):
        if string[i] in vowels:
            Kevin += len(string) - i
        else:
            Stuart += len(string) - i
    if Kevin > Stuart:
        print("Kevin {0}".format(str(Kevin)))
    else:
        print("Stuart {0}".format(Stuart))

if __name__ == "__main__":
    print_winner("BANANA")