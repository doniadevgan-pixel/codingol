from abc import ABC, abstractmethod

class Animal(ABC):

    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat

    def display(self):
        print(f"Name: {self.name} | Habitat: {self.habitat}")

    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):

    def __init__(self, name, habitat, breed):
        super().__init__(name, habitat)
        self.breed = breed

    def speak(self):
        print(f"{self.name} ({self.breed}) says: Woof! Woof!")

class Lion(Animal):

    def __init__(self, name, habitat, pride):
        super().__init__(name, habitat)
        self.pride = pride

    def speak(self):
        print(f"{self.name} (Pride: {self.pride}) says: RooarRRRRR!")

dog = Dog("Bruno", "Home", "Labrador")
lion = Lion("Simba", "Savannah", "Pride Rock")

print ("=== Animal Sound Show ===\n")
for animal in [dog, lion]:
    animal.display()
    animal.speak()
    print()
        
    