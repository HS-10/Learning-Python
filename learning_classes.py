class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(2, 6)
print(p.x)
print(p.y)
#object
class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    #method
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
    #method
    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)

people = ["Harry", "Ron", "Hermione", "Ginny"]

for person in people:
    success = flight.add_passenger(person)
    if success:
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No available seats for {person}")