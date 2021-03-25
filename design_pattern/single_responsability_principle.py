""""
The Single Responsability Principle (SRP) or separation of concerns (SOC). The concept is pretty simple: if you have
a class, that class should have its primary responsability whatever it's meant to be doing and it should not take on
other responsabilities.

Anti patterns are the representation of bad code.
"""


class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return '\n'.join(self.entries)

    """
    It's a bad idea to implement this part in the same class. It's better to create a separate class.
    def save(self, filename):
        file = open(filename, 'w')
        file.write(str(self))
        file.close()
    
    def load(self, filename):
        pass
    
    def low_from_web(self, uri):
        pass

    """


class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()


if __name__ == "__main__":
    j = Journal()
    j.add_entry('I cried today')
    j.add_entry('I had a bug')
    print(f'Journal entries:\n{j}')

    file = r'C:\Users\gcare\python-exercises\journal.txt'
    PersistenceManager.save_to_file(j, file)
    with open(file) as fh:
        print(fh.read())
