class Pet:
    def __init__(self, name, health):
        self.name = name
        self.__health = health

    def show_info(self):
        print(f"Pet Name: {self.name}")
        print(f"Health Level: {self.__health}")

    def care_action(self):
        print(f"{self.name} needs general care.")

    def set_health(self, new_health):
        if new_health >= 0 and new_health <= 100:
            self.__health = new_health
            print(f"{self.name}'s health updated to {self.__health}.")
        else:
            print("Health must be between 0 and 100.")

class Dog(Pet):
    def care_action(self):
        print(f"{self.name} needs a walk and some playtime.")

class Fish(Pet):
    def care_action(self):
        print(f"{self.name} needs some quiet time and a clean glass bowl.")

class Cat(Pet):
    def care_action(self):
        print(f"{self.name} needs some streaching and quiet rest.")


# Objects
dog = Dog("Rocket", 70)
fish = Fish("goldi", 50)
cat = Cat("Sophi", 65)

pets = [dog, fish, cat]

print("===== My Pet Care Dashboard =====\n")

for pet in pets:
    pet.show_info()
    pet.care_action()
    print()

print("===== Updating Pet Health =====\n")

dog.set_health(85)
fish.set_health(80)
cat.set_health(78)

print("\n===== Final Pet Care Summary =====\n")

for pet in pets:
    pet.show_info()
    print()



 