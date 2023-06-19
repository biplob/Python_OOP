class Vichel:

    def __init__(self, color):
        self.color = color
    def move(self):
        return "The vichels can move on the road"

# class Car:
#     def __int__(self, color, wheel):
#         self.color = color
#         self.wheel = wheel
#
#     def move(self):
#         return  "The car move on road"

class Car(Vichel):
    def __init__(self, color):
        super().__init__(color)
        self.wheels = 4


    def move(self):
        return  "The car move on road"

class Cycle(Vichel):
    def __init__(self, color):
        super().__init__(color)
        self.wheels = 2

    def move(self):
        return  "The cycle move on road"

class Airplan(Vichel):
    def __init__(self,color):
        super().__init__(color)
        self.wheels = 5

    def move(self):
        return "The airplan move on the sky"

# v1 = Vichel('Red')
# print(v1.color)
# print(v1.move())
car1 = Car('Red')
cycle1 = Cycle('Blue')
airplane = Airplan('Green')

# print(car1.color)
# print(cycle1.color)
# print(airplane.color)

# print(f'{car1.color} car: {car1.move()}')
# print(f'{cycle1.color} cycle: {cycle1.move()}')
# print(f'{airplane.color} airplane: {airplane.move()}')

print(car1.wheels)
print(cycle1.wheels)
print(airplane.wheels)