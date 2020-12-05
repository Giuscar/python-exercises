""""
You are asked to ensure that the first and last names of people begin with a capital letter in their passports.
For example, alison heck should be capitalised correctly as Alison Heck.

alison heck ==> Alison Heck

Given a full name, your task is to capitalize the name appropriately.

Input Format
A single line of input containing the full name, S.

Constraints
- 0 < len(S) < 1000
- The string consists of alphanumeric characters and spaces.
Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.

Output Format
Print the capitalized string, S.

Sample Input
chris alan

Sample Output
Chris Alan
"""

def solve(s):
    a_string = s.split(' ')
    return ' '.join((word.capitalize() for word in a_string))

if __name__ == "__main__":
    print(solve("chris alan"))