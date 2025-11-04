
# A simple example of classes and inheritance

class Person:
    """Represents a general person."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        """Print a short introduction."""
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")

# create a couple of persons

joe = Person("Joe", 35)
mohammed = Person("Mohammed", 54)

joe.introduce()
mohammed.introduce()
