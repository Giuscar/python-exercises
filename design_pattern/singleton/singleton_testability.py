import unittest


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).\
                __call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=Singleton):
    def __init__(self):
        self.population = {}
        f = open('capitals.txt', 'r')
        lines = f.readlines()
        for i in range(0, len(lines), 2):
            self.population[lines[i].strip()] = \
            int(lines[i+1].strip())
        f.close()


class SingletonRecordFinder:

    def total_population(self, cities):
        result = 0
        for c in cities:
            result += Database().population[c]
        return result


class ConfigurableRecordFinder:
    def __init__(self, db):
        self.db = db

    def total_population(self, cities):
        result = 0
        for c in cities:
            result += self.db.population[c]
        return result


class DummyDatabase:
    population = {
        'alpha': 1,
        'beta': 2,
        'gamma': 3
    }

    def get_population(self, name):
        return self.population[name]


class SingletonTests(unittest.TestCase):
    def test_is_singleton(self):
        db1 = Database()
        db2 = Database()
        self.assertEqual(db1, db2)

    def test_singleton_total_population(self):
        rf = SingletonRecordFinder()
        names = ['New York', 'Tokyo', 'Shanghai']
        tp = rf.total_population(names)
        self.assertEqual(1750000+3500000+24000000, tp)

    """"The test you have above have the problem to be highly dependent on the data. If the data changes, the test
    won't pass anymore. Therefore what is better to do is creating a new template in order to launch your unittests."""

    ddb = DummyDatabase()

    def test_dependent_total_population(self):
        crf = ConfigurableRecordFinder(self.ddb)
        self.assertEqual(3,
            crf.total_population(['alpha', 'beta']))


if __name__ == '__main__':
    unittest.main()