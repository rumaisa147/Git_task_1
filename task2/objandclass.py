class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")


# Creating objects of the Person class
person1 = Person("Anand", 23)
person2 = Person("Alex", 30)

# Accessing object attributes
print(person1.name)
print(person2.age)

# Calling object methods
person1.greet()
person2.greet()  
