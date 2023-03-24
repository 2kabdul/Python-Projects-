import math

str = 'mississippi'
str.count('s')

str = str.replace('iss', 'ox')

def foo(istring):
    p = '0123456789'
    os = ''
    for ch in istring:
        if ch not in p:
            os += ch
    return os

def foo2(istring):
    p = '0123456789'
    os = ''
    for ch in range(len(istring)):
        if istring[ch] not in p:
            os += istring[ch]
    return os

def repeat_first(string):
    first_letter = string[0]

    if first_letter in string[1:]:
        return True
    else:
        return False

def repeat_word():

    repeated_words = []

    i = 0
    while i != 1:
        x = input('Enter a word: ')
        if x == '':
            i += 1
        elif repeat_first(x):
            repeated_words.append(x)
    return repeated_words

def is_palindrome(string):

    new_string = ''
    string = string.lower()
    string = string.split()
    for char in string:
        if char.isalpha():
            new_string += char
    s = new_string
    s2 = new_string[::-1]
    if s == s2:
        return True
    else:
        return False

def look_vowel(shown):

    vowel = 'aeiou'
    min = float('inf')
    for char in shown:
        if char in vowel:
            j = shown.find(char)
            if j < min:
                min = j
    return min

def igpay(word):

    vowels = 'aeiou'

    if look_vowel(word) == 0:
        word = word + 'way'
    else:
        s = look_vowel(word)
        c = word[:s]
        word = word[s:] + c + 'ay'

    return word
