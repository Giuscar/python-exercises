"""
The goal of composite design pattern is to treat individual and aggregate objects uniformly.

What you need to do with composite:
- Objects can use other objects via inheritance/composition.
- Some composed and singular objects need similar/identical behaviors.
- Composite design pattern lets us treat both types of objects uniformily.
- Python supports iteration with __iter__ the Iterable ABC.
- A single object can make itself iterable by yielding self from __iter__.
"""


class GraphicObject:
    def __init__(self, color=None):
        self.color = color
        self.children = []
        self._name = 'Group'

    @property
    def name(self):
        return self._name

    def _print(self, items, depth):
        items.append('*' * depth)
        if self.color:
            items.append(self.color)
        items.append(f'{self.name}\n')
        for child in self.children:
            child._print(items, depth + 1)

    def __str__(self):
        items = []
        self._print(items, 0)
        return ''.join(items)


class Circle(GraphicObject):
    @property
    def name(self):
        return 'Circle'


class Square(GraphicObject):
    @property
    def name(self):
        return 'Square'


if __name__ == '__main__':
    drawing = GraphicObject()
    drawing._name = 'My Drawing'
    drawing.children.append(Square('Red'))
    drawing.children.append(Circle('Yellow'))

    group = GraphicObject()
    group.children.append(Circle('Blue'))
    group.children.append(Square('Blue'))

    drawing.children.append(group)

    print(drawing)
