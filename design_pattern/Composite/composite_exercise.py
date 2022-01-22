"""
Consider the code presented below. We have two classes called SingleValue and ManyValues. SingleValue stores
just one numeric value, but ManyValues can store either numeric values or SingleValue objects. You are asked to give
both SingleValue and ManyValues a property member called sum that returns a sum of all the values that the object
contains. Please ensure that there is only a single method that realizes the property sum, not multiple methods.
"""
from unittest import TestCase
from abc import ABC


class Sum(ABC):
    @property
    def sum(self):
        result = 0
        for c in self:
            for i in c:
                result += i
        return result


class SingleValue:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        print("here")
        yield self.value


class ManyValues(list, Sum):
    pass


if __name__ == '__main__':
    single_value = SingleValue(11)
    other_values = ManyValues()
    other_values.append(22)
    other_values.append(33)
    # make a list of all values
    all_values = ManyValues()
    all_values.append(single_value)
    all_values.append(other_values)
    print(all_values.sum)

"""
class Evaluate(TestCase):
    def test_exercise(self):
        single_value = SingleValue(11)
        other_values = ManyValues()
        other_values.append(22)
        other_values.append(33)
        # make a list of all values
        all_values = ManyValues()
        all_values.append(single_value)
        all_values.append(other_values)
        self.assertEqual(all_values.sum, 66)
"""