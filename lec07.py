def first_clause(sentence):
    if ',' in sentence:
        return sentence[0: sentence.find(',')]
    else:
        return sentence

def second_clause(sentence):
    first_comma = sentence.find(',')
    second_comma = sentence.find(',', first_comma+1)
    if sentence.count(',') >= 2:
        return sentence[first_comma+1:second_comma]
    elif sentence.count(',') == 1:
        return sentence[first_comma+1:]
    else:
        return ''

def last_word(sentence):
    last_space = sentence.rfind(' ')
        return sentence[last_space+1:]

def remove_vowels(message):
     for vowel in 'aeiouAeiou':
        message = message.replace(vowel, '')

def count_uppercase_words(text):
    count = 0
    worldlist = text.split()
    for word in wordlist:
        if word[0].isupper() == True:
            count += 1
    return count

def censor(text):
    worldlist = text.split()
    for word in worldlist:
        if len(word) == 4:
            worldlist[worldlist.index(word)] = '****'
    newtext = ' '.join(worldlist)
