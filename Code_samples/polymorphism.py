
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Duck:
    def speak(self):
        return "Quack!"


# Function that uses polymorphism
def animal_sound(animal):
    print(animal.speak())


# Create objects
dog = Dog()
cat = Cat()
duck = Duck()

# Same function, different behaviors
animal_sound(dog)   # Woof!
animal_sound(cat)   # Meow!
animal_sound(duck)  # Quack!