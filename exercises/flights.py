""""
You are given a list of flight start and end times. Determine the maximum amount of airplanes in the air at the same
time.

Example:
Start: 2, End: 2
Start: 3, End: 7
Start: 8, End: 9
"""


class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def insert(self, element):
        self.queue.append(element)
        sorted(self.queue, key=lambda tup: tup[1])

    def get(self):
        return self.queue[0]

    def pop(self):
        return self.queue.remove(self.queue[0])

    def is_empty(self):
        return True if len(self.queue) == 0 else False

    def get_size(self):
        return len(self.queue)


def calculate_max_flights_on_air(list_of_flights):
    list_of_flights.sort(key=lambda tup: tup[0])
    max_flights = -1
    flights_on_air = PriorityQueue()

    for list_of_flight in list_of_flights:
        if flights_on_air.is_empty():
            flights_on_air.insert(list_of_flight)
        else:
            while not flights_on_air.is_empty() and list_of_flight[0] > flights_on_air.get()[1]:
                flights_on_air.pop()

            flights_on_air.insert(list_of_flight)
        max_flights = max(max_flights, flights_on_air.get_size())

    return max_flights


if __name__ == "__main__":
    print("The max value is {0}".format(
        calculate_max_flights_on_air([(1, 3), (2, 8), (3, 4), (5, 6), (9, 10)]))
    )

    print("The max value is {0}".format(
        calculate_max_flights_on_air([(4, 8), (2, 5), (17, 20), (10, 21), (9, 18)]))
    )
