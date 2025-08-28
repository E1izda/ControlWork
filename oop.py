# Задание первое

class Persоn:
    def __init__(self):
        self.__age = 0

    def set_age(self, age):
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным.")
        self.__age = age

    def get_age(self):
        return self.__age

p = Persоn()
p.set_age(25)
print(p.get_age())
p.set_age(-5)


# задание второе

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I am an animal"

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

dog = Dog("Buddy")
cat = Cat("Kitty")

print(dog.name, dog.speak())
print(cat.name, cat.speak())


# задание третье

class Vehicle:
    def move(self):
        return "Vehicle is moving"

class Car(Vehicle):
    def move(self):
        return "Car is driving"

class Bicycle(Vehicle):
    def move(self):
        return "Bicycle is pedaling"

def move(vehicle):
    return vehicle.move()

car = Car()
bike = Bicycle()

print(move(car))
print(move(bike))

# задание четвертое

import math

class Shape:
    def area(self):
        print("Пожалуйста, сделай этот метод в своём классе")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

rect = Rectangle(10, 5)
circle = Circle(7)

print(rect.area())
print(round(circle.area()))
