###### Task ######
#
# Create an Animal base class with a method make_sound()
# Subclasses: Dog, Cat, Bird with custom implementations of make_sound()
# Instantiate each and call make_sound()
##################

# Base class
class Animal:
    def __init__(self, sound):
        self.sound = sound
    
    def make_sound(self):
        print(self.sound)

# Subclasses
class Dog(Animal):
    def __init__(self):
        super().__init__("Bark")

class Cat(Animal):
    def __init__(self):
        super().__init__("Meow")

class Bird(Animal):
    def __init__(self):
        super().__init__("Chip")

# Instantiate and call methods
dog = Dog()
cat = Cat()
bird = Bird()

dog.make_sound()
cat.make_sound()
bird.make_sound()
