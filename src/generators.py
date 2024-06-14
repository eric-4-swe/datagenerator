import random



def generate_numbers(start, end): 
    range_ = range(start, end + 1)
    return random.choice(range_)


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





    