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
    "H": 0,
    "He": 0,
    "Li": 0,
    "Be": 0,
    "B": 0,
    "C": 0,
    "N": 0,
    "O": 0,
    "F": 0,
    "Ne": 0,
    "Na": 0,
    "Mg": 0,
    "Al": 0,
    "Si": 0,
    "P": 0,
    "S": 0,
    "Cl": 0,
    "Ar": 0,
    "K": 0,
    "Ca": 0,
    "Sc": 0,
    "Ti": 0,
    "V": 0,
    "Cr": 0,
    "Mn": 0,
    "Fe": 0,
    "Co": 0,
    "Ni": 0,
    "Cu": 0,
    "Zn": 0,
    "Ga": 0,
    "Ge": 0,
    "As": 0,
    "Se": 0,
    "Br": 0,
    "Kr": 0,
    "Rb": 0,
    "Sr": 0,
    "Y": 0,
    "Zr": 0,
    "Nb": 0,
    "Mo": 0,
    "Tc": 0,
    "Ru": 0,
    "Rh": 0,
    "Pd": 0,
    "Ag": 0,
    "Cd": 0,
    "In": 0,
    "Sn": 0,
    "Sb": 0,
    "Te": 0,
    "I": 0,
    "Xe": 0,
    "Cs": 0,
    "Ba": 0,
    "La": 0,
    "Ce": 0,
    "Pr": 0,
    "Nd": 0,
    "Pm": 0,
    "Sm": 0,
    "Eu": 0,
    "Gd": 0,
    "Tb": 0,
    "Dy": 0,
    "Ho": 0,
    "Er": 0,
    "Tm": 0,
    "Yb": 0,
    "Lu": 0,
    "Hf": 0,
    "Ta": 0,
    "W": 0,
    "Re": 0,
    "Os": 0,
    "Ir": 0,
    "Pt": 0,
    "Au": 0,
    "Hg": 0,
    "Tl": 0,
    "Pb": 0,
    "Bi": 0,
    "Po": 0,
    "At": 0,
    "Rn": 0,
    "Fr": 0,
    "Ra": 0,
    "Ac": 0,
    "Th": 0,
    "Pa": 0,
    "U": 0,
    "Np": 0,
    "Pu": 0,
    "Am": 0,
    "Cm": 0,
    "Bk": 0,
    "Cf": 0,
    "Es": 0,
    "Fm": 0,
    "Md": 0,
    "No": 0,
    "Lr": 0,
    "Rf": 0,
    "Db": 0,
    "Sg": 0,
    "Bh": 0,
    "Hs": 0,
    "Mt": 0,
    "Ds": 0,
    "Rg": 0,
    "Cn": 0,
    "Nh": 0,
    "Fl": 0,
    "Mc": 0,
    "Lv": 0,
    "Ts": 0,
    "Og": 0,
}

brackets = {"[": "]", "(": ")"}


def retrieve_number_of_atoms(formula: str, start_index, end_index, input_constant=1):
    index = start_index
    while index < end_index:
        if formula[index].isalpha():
            if index + 1 < end_index and formula[index + 1].isdigit():
                atoms[formula[index]] += int(formula[index + 1]) * input_constant
                index += 2
            elif index + 1 < end_index and formula[index + 1].isalpha() and formula[index + 1].islower():
                if index + 2 < end_index and formula[index + 2].isdigit():
                    atoms[formula[index : index + 2]] += int(formula[index + 2]) * input_constant
                    index += 3
                else:
                    atoms[formula[index:index+2]] += input_constant
                    index += 2
            else:
                atoms[formula[index]] += 1 * input_constant
                index += 1
        elif formula[index] in ["[", "("]:
            index_final = next((i for i in range(index, end_index) if formula[i] == brackets[formula[index]]), None)
            constant = 1
            if index_final:
                if index_final + 1 < end_index and formula[index_final + 1].isdigit():
                    constant = int(formula[index_final + 1])
                retrieve_number_of_atoms(formula, index + 1, index_final, constant * input_constant)
                index = index_final + 1 if constant == 1 else index_final + 2

    return atoms


if __name__ == "__main__":
    formula = "K4ONSO3[(O3K2)2S2]2"
    # formula = "Mg(OH)2"
    atoms_result = retrieve_number_of_atoms(formula, 0, len(formula))
    result = ",".join([f"{k.upper()}={v}" for k, v in atoms_result.items() if v >= 1])
    print(f"Number of atoms are {result}")
