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


def increase_number(res: {}, number: int, element: str) -> {}:
    if res.get(element):
        res[element] += int(number)
    else:
        res[element] = int(number)

    return res


def calculate_chemical_formula(chemical_formula: str) -> {}:

    element = ""
    res = {}
    new_index = -1
    parenthesis = {']': '[', ')': '(', '}': '{'}

    for idx in range(len(chemical_formula)):
        if chemical_formula[idx].isupper():
            if element != "":
                increase_number(res, 1, element)
            element = chemical_formula[idx]
            if idx + 1 >= len(chemical_formula):
                increase_number(res, 1, element)
        elif chemical_formula[idx].islower():
            element += chemical_formula[idx]
            if idx + 1 >= len(chemical_formula):
                increase_number(res, 1, element)
        elif chemical_formula[idx].isdigit() and idx > new_index:
            number, new_index = create_number(idx, chemical_formula)
            increase_number(res, int(number), element)
            element = ""
        elif chemical_formula[idx] in parenthesis.keys() or chemical_formula[idx] in parenthesis.values():
            continue

    return res


def retrieve_value(parenthesis_beg: str, index: int, chemical_formula: str) -> int:
    parenthesis = {'[': ']', '(': ')', '{': '}'}
    final_index = -1

    for idx in range(index, len(chemical_formula)):
        if idx > final_index:
            if chemical_formula[idx] == parenthesis[parenthesis_beg]:
                final_index = idx
                break
                # if idx + 1 < len(chemical_formula) and chemical_formula[idx+1].isdigit():
                #     _, final_index = create_number(idx+1, chemical_formula)
                #     break
                # else:
                #     final_index = idx
                #     break

    return final_index


def update_res(res: {}, tmp_res: {}) -> {}:

    for key, value in tmp_res.items():
        if res.get(key):
            res[key] += value
        else:
            res[key] = value
    return res


if __name__ == "__main__":
    chemical_formula = '(Mg2H3)2'
    parenthesis = {']': '[', ')': '(', '}': '{'}

    # res = calculate_chemical_formula(chemical_formula)

    element = ""
    new_index = -1
    final_idx = -1
    res = {}
    tmp_res = {}
    for idx in range(len(chemical_formula)):
        if idx > final_idx:
            if chemical_formula[idx] in parenthesis.values():
                final_idx = retrieve_value(chemical_formula[idx], idx, chemical_formula)
                tmp_res = calculate_chemical_formula(chemical_formula[idx:final_idx])
            elif chemical_formula[idx].isdigit():
                for key, value in tmp_res.items():
                    tmp_res[key] *= int(chemical_formula[idx])
                update_res(res, tmp_res)

    for key, value in res.items():
        print(key + ': ' + str(value))