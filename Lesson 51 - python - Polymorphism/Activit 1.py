class Cricket:

    def __init__(self, player, score):
        self.__player = player
        self.__score = score

    def info(self):
        print(f"cricket - player: {self.__player}, Score: {self.__score}")

    def play(self):
        print(f"{self.__player} Hits a six!")

    def get_score(self):
        return self.__score

    def set_score(self, new_score):
        if new_score >= 0:
            self.__score= new_score
            print(f"Score updated to {self.__score}")
        else:
            print("Score can not be negative.")

class Soccer:

    def __init__(self, player, score):
            self.__player = player
            self.__score = score
    
    def info(self):
            print(f"Soceer - player: {self.__player}, Score: {self.__score}")
    
    def play(self):
            print(f"{self.__player} Scores a goal!")
    
    def get_score(self):
            return self.__score
    
    def set_score(self, new_score):
            if new_score >= 0:
                self.__score= new_score
                print(f"Score updated to {self.__score}")
            else:
                print("Score can not be negative.")

# create objects
cricket = Cricket("Rohit", 85)
soccer =Soccer("Arjun", 2)

# Polymorphism : Same method but diffent Behiviour
print("=== Sports Scoreboard ===\n")
for sport in (cricket, soccer):
     sport.info()
     sport.play()
     print()

# Encapulation: Direct change does not work
print("--- Direct change attempt ---")
cricket.__score = 999
print(f"get_score() still shows: {cricket.get_score()}")

# Setter: the only safe way to update
print("\n--- Updating scores ---")
cricket.set_score(100)
soccer.set_score(3)

# What is encapsulation?
# Encapsulation is the concept of bundling data (attributes) and methods (functions) that operate on that data within a single unit (class), and restricting direct access to some of the object's components.

# What is polymorphism?
# Polymorphism is the ability of different classes to be treated as instances of the same class through a common interface. It allows methods to do different things based on the object it is acting upon, even if they share the same method name.

# 



        













    