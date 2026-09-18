class parrot:
# class attribute
 species = "bird"

# instance attribute
 def __init__(self, name, age):
     self.name = name
     self.age = age

# instantiate the parrot object
blu = parrot("Blu", 10)
woo = parrot("Woo", 15)

# access the class attributes
print("Blu is a {}".format(blu.species))
print("Woo is also a {}".format(woo.species))

# access the instance attributes
print("{} is {} years old".format(blu.name, blu.age))
print("{} is {} years old".format(woo.name, woo.age))

# object- an object is an instance of a class. It is created from the class and has its own unique attributes and methods.

# class- a class is a blueprint for creating objects. It defines the attributes and methods that the objects created from the class will have.

# attributes- attributes are the characteristics or properties of an object. They can be instance attributes (unique to each object) or class attributes (shared among all instances of the class).

# behaviors- behaviors are the actions or methods that an object can perform. They define how the object behaves and interacts with other objects.

# self parameter- the self parameter is a reference to the current instance of the class. It is used to access the attributes and methods of the object within the class definition.

# init satnds for "initialize". It is a special method in Python classes that is automatically called when a new object is created. It is used to initialize the attributes of the object with specific values.

# constructor- a constructor is a special method in a class that is used to create and initialize objects. In Python, the constructor is defined using the __init__ method.

# Whithout constructor it 

# enumerate- enumerate is a built-in function in Python that adds a counter to an iterable and returns it as an enumerate object. It can be used to loop through a list or other iterable and get both the index and the value of each item.