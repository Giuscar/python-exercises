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

"""
- Loop from the end of the string
- if str[i] is Number and i-1 > 0 and str[i-1] is letter: 
    dict[str[i-1]] += str[i]
- if str[i] is Number and i-1 > 0 and str[i-1] in ["]", ")"]
    recursive_call until str[i] in ["(", "["]    
"""
import re

atoms = {
    "a": 0,
    "b": 0,
    "c": 0,
    "d": 0,
    "e": 0,
    "f": 0,
    "g": 0,
    "h": 0,
    "i": 0,
    "j": 0,
    "k": 0,
    "l": 0,
    "m": 0,
    "n": 0,
    "o": 0,
    "p": 0,
    "q": 0,
    "r": 0,
    "s": 0,
    "t": 0,
    "u": 0,
    "v": 0,
    "w": 0,
    "x": 0,
    "y": 0,
    "z": 0,
}


def retrieve_number_of_atoms(formula: str, start_index, end_index):
    index = start_index
    print(f"{formula[start_index:end_index]}")
    while index < end_index:
        print(f"Formula index is {formula[index]}")
        if formula[index].isalpha():
            if index + 1 < end_index and formula[index + 1].isdigit():
                atoms[formula[index].lower()] += int(formula[index+1])
                index += 2
            else:
                atoms[formula[index].lower()] += 1
                index += 1
        elif formula[index] == "[":
            index_final = next((i for i in range(index, end_index) if formula[i] == "]"), None)
            if index_final:
                retrieve_number_of_atoms(formula, index+1, index_final)
            index += index_final+1
        elif formula[index] == "(":
            index_final = next((i for i in range(index, end_index) if formula[i] == ")"), None)
            if index_final:
                retrieve_number_of_atoms(formula, index + 1, index_final)
            index += index_final+1

    return atoms

if __name__ == "__main__":
    formula = "K4ONSO3[(O3)(S2)]"
    atoms_result = retrieve_number_of_atoms(formula, 0, len(formula))
    result = ",".join([f"{k.upper()}={v}" for k, v in atoms_result.items() if v >= 1])
    print(f"Number of atoms are {result}")
