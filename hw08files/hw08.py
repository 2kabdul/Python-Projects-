import random

def durdle_match(guess, target):
    '''
    Purpose:
        Determines which letters in the user's guess match the target
    Parameters:
        guess - a 5-letter string representing the user's guess
        target - a 5-letter string representing the target word
    Return Value:
        A 5-letter string, where each letter represents whether or not
        the letter in that position is correct.  'B' means the letter
        is not present in the target, 'Y' means that it's present in
        a different location, 'G' means it's in the correct location.
    '''
    matches = ''
    for i in range(5):
        if guess[i] not in target:
            matches += 'B'
        elif guess[i] == target[i]:
            matches += 'G'
        else:
            matches += 'Y'
    return matches

def durdle_game():
    '''
    Purpose:
        Lets the user play a game where they try to match a target word
    Parameters:
        None
    Return Value:
        The number of guesses it took the user to get the correct word.
    '''
    wrd = get_word_list('words_full.txt')

    print("Welcome to Durdle!")
    guess = ''
    count = 0
    target = random.choice(wrd)
    while guess != target:
        guess = input("Enter a guess:")
        if guess not in wrd:
            print("Invalid guess, try again.")
        else:
            print('              '+durdle_match(guess, target))
            count += 1
    print("Congratulations, you got it in",count,"guesses!")
    return count

def get_word_list(filename):
    '''
    Purpose:
        use a file with a list and return it in a new list in the order they appear
    Parameters:
        filename: the name of the file
    Return Value:
        return a string a list of strings containing the words from the file in
        order they appear
    '''
    f = open(filename)
    words = f.read()
    b = words.split()
    f.close()
    return b


def grade_quiz(filename):
    '''
    Purpose:
        function returns a list of integers that are the students score
    Parameters:
        filename: the name of the file of students
    Return Value:
        return the students score
    '''
    try:
        f = open(filename)
        nlist = [0, 0, 0]
        test = ['42', 'Belgium', 'Towel']
        score = f.read()
        b = score.split("\n")
        for i in range(len(b)-1):
            if b[i] == '':
                nlist[i] = 0
            elif b[i] == test[i]:
                nlist[i] = 2
            elif b[i] != test[i]:
                nlist[i] = 1
    except FileNotFoundError:
        return [0, 0, 0]
    return nlist

import csv

def grade_all(grade_file):
    '''
    Purpose:
        creates a new csv file that has the updated grades
    Parameters:
        grade_file: the orginal csv file which you use to then update
    Return Value:
        return an updated csv file with the updated grades from grade_quiz
    '''
    var = ''
    f = open(grade_file)
    t = open('updated_' + grade_file, 'w')
    updated = f.readlines()
    t.write(updated[0])
    for x in updated[1:]:
        b = x.split(',')
        filename = (b[0].lower() + '_' + b[1].lower() + '.txt')
        tests = grade_quiz(filename)
        var = b[0] + ',' + b[1] + ','
        # print(var)
        for i in range(3):
            b[i+ 2] = str(tests[i])
            var = var + str(tests[i])
            var += ','
        var = var[:-1]
        var += '\n'
        t.write(var)
    f.close()
    t.close()
