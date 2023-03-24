import random
import math

def cookie_order(input):
    '''
Purpose: takes cookies names as keys and number of those cookies as values
Parameter(s):input : cookie name and number of cookies
Return Value: Number of boxes needed for cookie name and value
'''

    my_cookie = {}
    for key in input:
        tasty = input[key]
        my_cookie[key] = math.ceil(tasty/30)
    return my_cookie

def follow_words(text):
    '''
Purpose: takes in a string and returns a dictionary
Parameter(s): text: the string of text
Return Value: returns a dictionary
'''

    lis = text.split()
    # print(lis)
    result = {}
    for i in range(len(lis)-1):
        # print(i)
        if lis[i] in result:
            result[lis[i]].append(lis[i+1])
    #         # print(result)
        else:
            result[lis[i]] = [lis[i+1]]
    return result

def auto_complete(follows_dict, current):
    '''
Purpose: Suggests a list of words to potentially follow the current in a
randomly generated sentence
Parameter(s): follows_dict: a dictionary formatted like problem B
current: a randomly generated sentence
Return Value: gives you random generated sentence based off your dictionary
'''

    finish = current.split()
    last = []
    for key in follows_dict:
        if key == current:
            return follows_dict[key]
        else:
            last.append(key)
    return last

def random_sent(fname, max_length):
    '''
Purpose: function reads in a file then creates a random sentence that is based
of the given length
Parameter(s): fname: is the file name
max_length: given length based off if you the random sentence has a .,!,?
Return Value: a randomly generated sentence based of the filename and max length
'''

    f = open(fname)
    writing = f.read()
    following = follow_words(writing)
    take = writing.split()
    current = random.choice(take)
    nlist = [current]
    while len(nlist) < max_length and current[-1] != '!' and current[-1] != '?' and current[-1] != '.':
        auto = auto_complete(following, current)
        current = random.choice(auto)
        nlist.append(current)
    result = ''
    for current in nlist:
        result = result + current + ' '
    f.close()
    result = result.rstrip()
    return result
