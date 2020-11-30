""""
Input
Row 1: an integer N between 5 and 1000, representing the number of publications
made by the account to be reviewed.
Rows 2 to N+1: a string of characters of the form hh:mm representing the time of a
publication
Output
The string SUSPICIOUS if the account is suspicious, the string OK otherwise.
An account is considered suspicious if more than half of the posts are made at night
(between 20 :00 and 7:59 included). It is guaranteed that no account has as many
publications at night as during the day.

Example
For the input:
5
20:04
20:23
08:00
09:15
13:00
Your program will output OK as 2 publications were made at night on this account.

For the input :
5
20:00
00:29
22:58
15:06
17:50
Your program will output: SUSPICIOUS
"""

def time_is_suspiscious(hour, minute):
    return hour >= 20 and hour <= 23 or \
           hour >= 0 and hour <= 7

def find_fake_account(number_of_connections, time_of_connections):
    number_of_suspiscious_accounts = 0
    for time_of_connection in time_of_connections:
        hour, minute = time_of_connection.split(":")
        if time_is_suspiscious(int(hour), int(minute)):
            number_of_suspiscious_accounts +=1
    return number_of_suspiscious_accounts

if __name__ == "__main__":
    number_of_connections = 5
    time_of_connections_ok = ["20:04", "20:23", "08:00", "09:15", "13:00"]
    time_of_connections_suspiscious = ["20:00", "00:29", "22:58", "15:06", "17:50"]
    
    print("SUSPISCIOUS") \
        if find_fake_account(number_of_connections, time_of_connections_ok) > number_of_connections/2 else print("OK")

    print("SUSPISCIOUS") \
        if find_fake_account(number_of_connections, time_of_connections_suspiscious) > number_of_connections/2 \
        else print("OK")


