""""
Objective
After a long search we managed to find Dolan's Twitter account: @DolanGrump! You
decide to take an interest in its millions of followers: given the number of retweets on
each article shared, you greatly suspect that many of these followers are actually
bots...
You decide to do a first scan to identify potential bots: you notice that most bots have
an account name that only ends with numbers, unlike real people's accounts.
Write an algorithm to determine suspicious accounts. An account is suspicious if it
ends with 5 digits.
Data
Input
Row 1: an integer N between 1 and 1000, representing the number of accounts to be
checked
Rows 2 to No.1: A string of characters (composed only of numbers and letters and
between 6 and 15 characters in length) representing the name of an account to be
examined.
Output
An integer representing the number of suspicious accounts in the input.

Example
For input:
7
h25io
gn0mi12345
RealDon4321
yaNNd3v
cup0ft3444455
bienvenueCorbier
BClukschoco

Your program must return:
2
Indeed, the accounts cup0ft3444455 and gn0mi12345 are suspect, not the others.
"""

def calculate_fake_accounts(number_of_accounts, accounts):
    fake_account = 0
    for account in accounts:
        account = account[::-1]
        if account[0:5].isnumeric():
            fake_account += 1

    return fake_account

if __name__ == "__main__":
    number_of_accounts = 7
    accounts = ["h25io", "gn0mi12345", "RealDon4321", "yaNNd3v", "cup0ft3444455", "bienvenueCorbier", "BClukschoco"]
    print("The number of fake accounts is {0}".format(calculate_fake_accounts(number_of_accounts, accounts)))