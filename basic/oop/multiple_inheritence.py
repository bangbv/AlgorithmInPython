# Parent class 1
class Mammal:
    def has_fur(self):
        return True

# Parent class 2
class Carnivore:
    def eats_meat(self):
        return True

# Child class that inherits from both Mammal and Carnivore
class Lion(Mammal, Carnivore):
    def roar(self):
        print("Roar!")

# Usage
lion = Lion()
print(lion.has_fur())   # True (from Mammal)
print(lion.eats_meat()) # True (from Carnivore)
lion.roar()             # Roar!

# Method Resolution Order (MRO): In cases of multiple inheritance,
# Python determines the order in which classes are checked for methods
# and attributes using the C3 linearization algorithm
print(Lion.__mro__)