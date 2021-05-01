""""
**Note**: language to use: Python

For a given chemical formula represented by a string, count the number of atoms of each element contained in the molecule
and return a dict.

For example:

```py
water = 'H2O'
parse_molecule(water)                 # return {'H': 2, 'O': 1}

magnesium_hydroxide = 'Mg(OH)2'
parse_molecule(magnesium_hydroxide)   # return {'Mg': 1, 'O': 2, 'H': 2}

fremy_salt = 'K4[ON(SO3)2]2'
parse_molecule(fremy_salt)             # return {'K': 4, 'O': 14, 'N': 2, 'S': 4}
```

As you can see, some formulas have brackets in them. The index outside the brackets tells you that you have to multiply
count of each atom inside the bracket on this index. For example, in Fe(NO3)2 you have one iron atom, two nitrogen atoms
and six oxygen atoms.
Note that brackets may be round, square or curly and can also be nested. Index after the braces is optional.
Send us your work in an archive, in private gist file(s) or using an other private solution.
Make it ready for production ;)
"""


def create_number(index: int, chemical_formula: str):
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    res = []
    while index < len(chemical_formula) and chemical_formula[index] in numbers:
        res.append(chemical_formula[index])
        index += 1

    return ''.join(res), index



def calculate_chemical_formula(chemical_formula: str) -> {}:
    stack = []
    parenthesis = {']': '[', ')': '(', '}': '{'}
    res = {}
    new_index = -1

    for word in chemical_formula:
        if word.isalpha():
            res[word] = 1

    for index in range(len(chemical_formula)):
        if chemical_formula[index].isdigit() and index > new_index:
            word, new_index = create_number(index, chemical_formula)
            stack.append(word)
        elif chemical_formula[index].isupper() or chemical_formula[index] in parenthesis.values():
            new_index = -1
            if index + 1 < len(chemical_formula) and chemical_formula[index+1].islower():
                stack.append(chemical_formula[index]+chemical_formula[index+1])
            else:
                stack.append(chemical_formula[index])



    return res


if __name__ == "__main__":
    chemical_formula = 'Mg{FO[(AB)2(OH)4]2}5'
    res = calculate_chemical_formula(chemical_formula)

    # for key, value in res.items():
    #     print(key + ': ' + str(value))