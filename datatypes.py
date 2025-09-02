from classes.my_classes import Car

my_car = Car("Toyota", "Camry", 2020, 15000, "Good", "Blue")

my_car.start()
my_car.accelerate(30)
my_car.accelerate(20)
my_car.stop()

from classes.my_person import Person

my_person = Person("John", "Doe", 30, 180.5, "New York")
my_person.introduce()
my_person.relocate("Los Angeles")
my_person.introduce()