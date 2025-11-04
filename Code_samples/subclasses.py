#first import the class definition

class Person:
    """Represents a general person."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        """Print a short introduction."""
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")


# Subclass (inherits from Person)
class Student(Person):
    """Represents a student, which is a kind of person."""

    def __init__(self, name, age, major):
        # Call the constructor of the parent class
        super().__init__(name, age)
        self.major = major

    def study(self):
        """Describe what the student is studying."""
        print(f"{self.name} is studying {self.major}.")


# create a couple of persons

joe = Person("Joe", 35)
mohammed = Person("Mohammed", 54)

mike = Student("Mike", 19, "physics")
erica = Student("Erica", 21, "Economics")

mohammed.introduce()
erica.introduce()
erica.study()

