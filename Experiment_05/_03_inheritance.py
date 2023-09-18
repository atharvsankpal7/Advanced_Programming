class Animal:
    isalive = True

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Lion(Animal):

    def run(self):
        print(f"{self.name} is running")


class Hawk(Animal):
    def fly(self):
        print(f"{self.name} is flying")


ryan = Lion("ryan")
ryan.run()
ryan.sleep()

homelander = Hawk("john")
homelander.fly()


# Multilevel inheritance
class A:
    alive = True

    def eat(self):
        print("A")


class B(A):
    def eat(self):
        print("B")


class C(B):
    pass


c = C()

c.eat()

# Multiple Inheritance
class A:

    def function(self):
        print("A")


class B:

    def function(self):
        print("B")


class C(A, B):
    pass


c = C()

c.function()

# Method Chaining
class Car:
    def turn_on(self):
        print("car turned on")
        return self

    def drive(self):
        print("Drive")

    def brake(self):
        print("Brake")

    def turn_off(self):
        print("car turned off")


car = Car()

car.turn_on().drive()

