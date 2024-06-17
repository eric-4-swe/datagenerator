# About objects , have behavior and state

# Define a class

class Box:
    pass 


# creating Instance of our class
redbox = Box()  # instace 1
blackbox = Box()  # instace 2

# Define instance attributes

redbox.color = "red"
blackbox.color = "black"



 # Initialization of attributes for all instances of a class
 
class Box:
    def __init__(self, color_, length_, breath_):
        self.color = color_
        self.length = length_
        self.breath = breath_
        
# creating Instance of our class
redbox = Box("red", 56, 60)  # instace 1
blackbox = Box("black", 60, 60) # instace 2


print(redbox.color)

#Define instance methods


class Box:
    def __init__(self, color_, length_, breath_):
        self.color = color_
        self.length = length_
        self.breath = breath_
        
    def desc(self):
        formated_ = f"<Box color:{self.color} length:{self.length} breath:{self.breath} />"
        print(formated_)
        
    
# creating Instance of our class
redbox = Box("red", 56, 60)  # instace 1
blackbox = Box("black", 60, 60) # instace 2


# Calling The Instance Method

redbox.desc()
blackbox.desc()


#Define class attributes that will be same for all instances created

class Box:
    counter = 0
    
    def __init__(self, color_, length_, breath_):
        self.color = color_
        self.length = length_
        self.breath = breath_
        Box.counter = Box.counter + 1
        
    def desc(self):
        formated_ = f"<Box color:{self.color} length:{self.length} breath:{self.breath} />"
        print(formated_)



# creating Instance of our class
redbox = Box("red", 56, 70)  # instace 1
blackbox = Box("black", 60, 60) # instace 2

print(redbox.breath)
print(blackbox.breath)

print(redbox.counter)
print(blackbox.counter)


#Define class method

class Box:
    counter = 0
    
    def __init__(self, color_, length_, breath_):
        self.color = color_
        self.length = length_
        self.breath = breath_
        Box.counter = Box.counter + 1
        
    def desc(self):
    
        formated_ = f"<Box color:{self.color} length:{self.length} breath:{self.breath} />"
        print(formated_)
        
    @classmethod    
    def create_box(cls):
        return Box("White", 100, 100)




# creating Instance of our class
redbox = Box("red", 56, 70)  # instace 1
blackbox = Box("black", 60, 60) # instace 2


# Calling The Instance Method

redbox.desc()
blackbox.desc()


# I- Attr 

print(redbox.breath)
print(blackbox.breath)

# Class Attr
print(redbox.counter)
print(blackbox.counter)


# Class Methods

whitebox = Box.create_box()
whitebox.desc()

import random

# Define static method

class generators:
    h = 5
    @staticmethod
    def generate_numbers(start, end): 
        range_ = range(start, end + 1)
        return random.choice(range_)

    @staticmethod
    def generate_names():
        names_ = [
    "Emma", "Olivia", "Ava", "Sophia", "Isabella", "Charlotte", "Mia", "Amelia", "Evelyn", "Harper",
    "Aiden", "Noah", "Liam", "William", "James", "Oliver", "Benjamin", "Elijah", "Lucas", "Mason",
    "Avery", "Sofia", "Evelyn", "Chloe", "Abigail", "Luna", "Mila", "Ella", "Scarlett", "Eleanor",
    "Jackson", "Logan", "David", "Ethan", "Alexander", "Anthony", "Matthew", "Daniel", "Joseph", "Gabriel",
    "Charlotte", "Aurora", "Amelia", "Isla", "Olivia", "Ava", "Sophia", "Isabella", "Mia", "Evelyn",
    "Elijah", "Muhammad", "Aiden", "Jacob", "Mason", "William", "Lucas", "Ethan", "Alexander", "Benjamin",
    "Harper", "Nora", "Riley", "Zoey", "Emilia", "Sienna", "Avery", "Evelyn", "Scarlett", "Eleanor",
    "Liam", "Jackson", "Mason",  "Noah", "Alexander", "Aiden", "Daniel", "Elijah", "William",
    "Mia", "Amelia", "Isabella", "Charlotte", "Evelyn", "Olivia", "Sophia", "Avery", "Isla", "Riley",
    "Noah", "Liam", "William", "Mason", "James", "Benjamin", "Aiden", "Elijah", "Lucas", "Jackson",
]
        return random.choice(names_)




name_ = generators.generate_names()
som_num = generators.generate_numbers(10000, 600000)

print(name_, som_num)



#Single inheritance


class Shape:
    counter = 0
    
    def __init__(self, color_, length_, height_):
        self.color = color_
        self.length = length_
        self.height =  height_
        Box.counter = Box.counter + 1
        
    def desc(self):
    
        formated_ = f"<Shape color:{self.color} length:{self.length} height:{self.height} />"
        print(formated_)
        
    @classmethod    
    def create_box(cls):
        return Box("White", 100, 100)
    
    
    

class Square(Shape):
    pass


Square1 = Square("red", 10, 10)

Square1.desc()