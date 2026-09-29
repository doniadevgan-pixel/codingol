class Technology(ABC):
    pass

    def __init__(self, name, category):
        self.name = name
        self.category = category

    def display_info(self):
            print(f"Technology Name: {self.name}")
            print(f"Category: {self.category}")

    @abstractmethod
    def play_sound(self):
        pass

    class Phone(technology):

        def __init__(self, name, category, display):
                super().__init__(name, category)
                self.strings = strings

        def display_apps(self):
                print(f"{self.name} has {self.display} display shows and looks like entertaning!")

# Child class 2
class laptop(Instrument):

    def __init__(self, name, category, laptop type):
        super().__init__(name, category)
        self.laptop_type = laptop_type

    def plays_apps(self):
        print(f"{self.name} is a {self.laptop_type} and sounds like: enaging or boring!")


# Creating objects
Technology_1 = ("Phone", "small Technology", 6)
Technology_2 = Laptop(" big Technology")


# Displaying output
print("===== technology display Show =====
")

technology_1.display_info()
technology_1.play_sound()

print()
technology_2.display_info()
technology_2.play_sound()