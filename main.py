# 1-m
class Car:
    def __init__(self, brand, year, speed, fuel):
        self.brand = brand
        self.year = year
        self._speed = speed
        self.__fuel = fuel

    def accelerate(self, x):
        self._speed += x

    def refuel(self, x):
        self.__fuel += x

    def show_info(self):
        print(f"Brand: {self.brand}")
        print(f"year: {self.year}")
        print(f"speed: {self._speed}")
        print(f"fuel: {self.__fuel}")


car1 = Car("BMW", 2020, 100, 50)
car1.accelerate(20)
car1.refuel(10)
car1.show_info()


# 2-m
class Student:
    def __init__(self, name, age, grade, password):
        self.name = name
        self.age = age
        self._grade = grade
        self.__password = password

    def study(self, h):
        self._grade += h

    def check_password(self):
        print(f"Password: {self.__password}")

    def info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade: {self._grade}")
        print(f"Password: {self.__password}")

s1 = Student("Ali", 23, 40, 1234)
s1.info()

