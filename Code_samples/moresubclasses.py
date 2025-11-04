class Person:
    """Represents a general person."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        """Print a short introduction."""
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")

# Another subclass
class Teacher(Person):
    """Represents a teacher, which is also a kind of person."""

    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def teach(self):
        """Describe what the teacher teaches."""
        print(f"{self.name} is teaching {self.subject}.")

    def add_course(self, cls):
        self.subject = self.subject + " " + cls
        self.subject.split()  # we do this because we need a list of the classes being taught


susan = Teacher("Susan", 35, "CMSC104")
susan.teach()

susan.add_course("CMSC 201")
susan.teach()
