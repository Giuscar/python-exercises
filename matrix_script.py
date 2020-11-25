""""
Input
7 3
Tsi
h%x
i #
sM
$a
#t%
ir!

Output
This is Matrix#  %!
"""
import re

def format_and_print_string(input, list_inputs):
    n, m = map(int, input.split(' '))
    a, b = [], ""

    for z in zip(*list_inputs):
        b += "".join(z)

    print(re.sub(r"(?<=\w)([^\w]+)(?=\w)", " ", b))


if __name__ == "__main__":
    format_and_print_string("7 3", ["Tsi", "h%x", "i #", "sM ", "$a ", "#t%", "ir!"])
