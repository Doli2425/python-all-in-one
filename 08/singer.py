class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfun(self):
        print(f"name: {self.name}")
        print(f"age: {self.age}")

p1 = Person("John", 25)
p1.myfun()