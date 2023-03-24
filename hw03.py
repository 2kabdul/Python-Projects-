def sound(weight):
    '''
    Purpose: Represent a dogs bark by the weight of the scale
    Parameter(s): the weight of the dog
    Return Value: The sound of the dogs bark
    '''
    if weight < 13:
        weight = "Yip"
    elif weight >= 13 and weight <= 30:
        weight = "Ruff"
    elif weight >= 31 and weight <= 70:
        weight = "Bark"
    else:
        weight = "Boof"
    return weight
def sound2(weight, is_cat):
    '''
    Purpose: Represent a cats meow if true statement
    Parameter(s): the weight and if it is a cat
    Return Value: The sound of the dogs bark and if true then meow
    '''

    if is_cat == True:
        is_cat = "Meow"
    elif is_cat == False:
        is_cat = sound(weight)
    return is_cat 

def selection(text, optionA, optionB, optionC):
    '''
    Purpose: Give you options a,b,c for text
    Parameter(s):
    Text: the text that comes with optionA, optionB, optionC
    optionA,B,C: option use string value for possible options
    Return Value: gives you the choice you picked from the options
    '''
    print(text)
    print("A.", optionA)
    print("B.", optionB)
    print("C.", optionC)

    choice = input("Choose A, B, or C: ")

    if choice == "A" or choice == "B" or choice == "C":
        return choice
    else:
        print("Invalid option, defaulting to A")
        return "A"

def adventure():
    '''
    Purpose: use a sequence of choices leading to different endings
    Parameter(s): use selection to give choices A, B, C
    Return Value: gives you the choice you picked from the options
    '''
    choice = selection("I woke up with a headeache", "Take tyenol", "Go to sleep", "Go to the doctor")
    if choice == "A":
        choice = selection("You start feeling weird", "you are super","goes away", "you pass")
        if choice == "B":
            return False
        if choice == "C":
                return True
        if choice == "A":
            choice = selection("Super soldier sereum in your blood", "Become superman", "Become Hulk", "Become Xmen",)
            if choice == "A":
                return True
            if choice == "B":
                return False
            if choice == "C":
                return False
    elif choice == "B":
        choice = selection("You never wake", "dream", "wake", "fly")
        if choice == "A":
            return True
        if choice == "C":
            return True
        if choice == "B":
            choice = selection("Super soldier sereum in your blood", "Become superman", "Become Hulk", "Become Xmen",)
            if choice == "A":
                return True
            if choice == "B":
                return False
            if choice == "C":
                return False
    elif choice == "C":
        return False
