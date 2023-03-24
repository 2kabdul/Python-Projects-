
import random

class Character:
    '''
        Purpose: an object of this class represents the characters
        Instance variables: self.name: The characters name
        self.color: the characters color, self.alive: To check if the character is Alive
        Self.role: Check if its a good role or evil role
        self.tast_list: A list representing the task that a character must complete
        Methods: __init__(self,name,color,num_tasks): Gives the instance variables
        __repr__(self): To check if the players alive and their Health
        get_identity(self): Gets the identity of the character
    '''
    def __init__(self,name,color,num_tasks):
        possible_tasks = ['Stabilize drill', 'Calibrate distributor',
'Map course', 'Clear out O2 filter', 'Download files',
'Redirect power', 'Empty garbage', 'Repair wiring',
'Fill engines tanks', 'Inspect laboratory', 'Record temperature',
'Sign in with ID', 'Enable manifolds', 'Upload files']

        self.name = name
        self.color = color
        self.alive = True
        self.role =  "Good"
        self.task_list = []
        i = 0
        while i < num_tasks:
            diff_task = random.choice(possible_tasks)
            if diff_task not in self.task_list:
                self.task_list.append(diff_task)
                i += 1
    def __repr__(self):
        if self.alive == True:
            return self.name + ": " + self.color + " - " + "Health Status" + ": " + "Alive"
        else:
            return self.name + ":" + self.color + "-" + "Health Status" + ":" + "Ghost"
    def get_identity(self):
        return "Character"

class Crewperson(Character):
    '''
        Purpose: an object of this class represents the characters
        Instance variables: self.name: The characters name
        self.color: the characters color, self.alive: To check if the character is Alive
        Self.role: Check if its a good role or evil role
        self.tast_list: A list representing the task that a character must complete
        Methods: get_identity: overrideds part A get identity to return crewperson
        complete_task(self): removes first item in the list and completes task
    '''
    def get_identity(self):
        return "Crewperson"
    def complete_task(self):
        if len(self.task_list) > 0:
            print(self.name + " has completed task" + ": " + self.task_list[0] + '.')
            self.task_list.pop(0)
        else:
            return self.name + " has completed task" + ": "

class Pretender(Character):
    '''
        Purpose: an object of this class represents the characters
        Instance variables: derives from the character class
        self.role: saves as evil
        Methods: get_identity: overrideds part A get identity to return Pretender
        eliminate: If it is false then you return the name of the eliminated and the target
    '''

    def __init__(self,name,color,num_tasks):
        Character.__init__(self,name,color,num_tasks)
        self.role = "Evil"
    def get_identity(self):
        return 'Pretender'
    def eliminate(self,target):
        target.alive = False
        print(self.name + " eliminated " + str(target.name) + ".")

class Sheriff(Crewperson):
    '''
        Purpose: sherrif class looks for the elimantaed
        Instance variables: derives it from the character class
        Methods: __init__(self,name,color,num_tasks): derives from the character class
        get_identity(self): ovverideds the get identity to return sherrif
        encounter(self,target): switches the alive if they are pretender to False
    '''
    def __init__(self,name,color,num_tasks):
        Character.__init__(self,name,color,num_tasks)
    def get_identity(self):
        return "Sheriff"
    def encounter(self,target):
        if target.get_identity() == 'Pretender':
            target.alive = False
            print(self.name + " eliminated " + str(target.name) + ".")

class Game:
    '''
        Purpose: checks which characters their are still playing in the game and if a team wins
        Instance variables:
        Methods: encounter(self,target): stores the list of objects that is the player_list
        check_winner(self): To play the game and check who the winner is
    '''

    # def encounter(self,target):
    #     self.player_list = player_list
    # def check_winner(self):
