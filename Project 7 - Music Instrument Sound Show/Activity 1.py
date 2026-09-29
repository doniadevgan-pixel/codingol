class Technology(ABC):
    pass

    def __init__(self, name, category):
    self.name = name
    self.category = category

    @abstractmethod
    def play_sound(self):
        pass

    super().__init__(name, category)

instrument_1 = Guitar("Acoustic Guitar", "String Instrument", 6)
instrument_1.display_info()
instrument_1.play_sound()