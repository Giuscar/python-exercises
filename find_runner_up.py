""""
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
You are given n scores. Store them in a list and find the score of the runner-up.
Input Format
The first line contains n. The second line contains an array A[] of n integers each separated by a space.

Constraints
1 <= n <= 10
-100 <= A[i] <= 100

Output Format
Print the runner-up score.

Sample Input 0
5
2 3 6 6 5
Sample Output 0
5
Explanation 0
Given list is [2, 3, 6, 6, 5]. The maximum score is 6, second maximum is 5. Hence, we print  as the runner-up score.
"""""


def print_maximum_value(n, string):
    list_size = int(n)
    array_values = list(map(int, string.split(' ')))
    max_list = max(array_values)

    while max_list == max(array_values):
        array_values.remove(max(array_values))

    print(max(array_values))


if __name__ == "__main__":
    print_maximum_value("1", "2 3 6 6 5")
