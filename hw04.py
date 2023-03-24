def glorious(val):
    '''
    Purpose: Check if its not divisible by any number from 10 to 50
    Parameter(s): if val is divisible by the range(10,50)f
    Return Value: return false if value is divisble else return true
    '''
    for i in range(10,50):
        if val % i == 0:
            return False
    return True

def count_glorious(low,high):
    '''
    Purpose: takes in two positive integer and returns low and high inclusive
    Parameter(s): to get the range fromn low and high
    Return Value: returns if number glorious if between low and high inclusive
    '''
    if low > high:
        return 0
    count = 0
    for i in range(low,high + 1):
        if glorious(i):
            count += 1
    return count

def durdle_match(guess, target):
    '''
    Purpose: Guess a five letter word in succesive guesses
    Parameter(s): guess the word and return the target in B,Y,G
    Return Value: return a 5 string letter consisting of the letter B,G,Y
    '''
    for i in range(5):
        if guess[i] == target[i]:
            result += "G"
        elif guess[i] in target:
            result += "Y"
        else:
            result += "B"
    return result
#
def durdle_game(target):
    '''
    Purpose: takes in an argument that is a single string and return and let
    user guess the word
    Parameter(s): the guess and the target recall durdle_match to get the right
    match
    Return Value: The user guesses correctly the game ends an you return the
    number of tries
    '''
    guess = 0
    i = 0
    while guess != target:
        guess = input('Enter a guess:')
        print(durdle_match(guess, target))
        i += 1
    print('Congratulations, you got it in', i , 'guesses!')
    return i
