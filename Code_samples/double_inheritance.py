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

# a subclass of Student, which inherits from Person and Student
class EconMajor(Student):
    def __init__(self, name, age, major, class_standing, GPA, course_list):
        super().__init__(name, age,major)
        self.class_standing = class_standing
        self.GPA = GPA
        self.course_list = course_list

    def add_classes(self, classlist):
        for c in classlist:
            self.course_list.append(c)
    #    self.course_list.extend(classlist)
        #extend is a variant of append that adds multiple items

    def student_record(self):
        print(f"{self.name},{self.age}, {self.major}, {self.class_standing}, {self.GPA}, {self.course_list}")

#now create an EconMajor
beth = EconMajor("Elizabeth",22, "Economics", "Junior", 3.9, [])
#beth.study()
beth.student_record()
beth.add_classes(["CMSC104", "MATH 131", "PHYS414", "ECON202", "ECON412"])
beth.student_record()

