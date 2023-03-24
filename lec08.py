def alpha_char_count(message):
  '''
  Purpose:
  alphabetical characters in a given message
  Parameters:
      message - a string
  Return Value:
      a dictionary containng counts of each character that appears
  '''
  letter_count = {}

  for i in message:
      #solution 1 (a bit slow but really slow when we dont have the dictionary check)
      if i not in letter_count and i.isalpha():
          letter_count[i] = message.count(i)
      #solution 2 ( a little slower! oops!)
    if i in letter_count:
      letter_count[i] = letter_count[i] + 1
    else:
      letter_count[i] = 1
    #solution 3
    if i.isalpha():
    letter_count[i] = letter_count.get(i, 0) + 1
      return letter_count

def alpha_char_wordlist(amessage):
     '''
     Purpose:
     create a dictionary of lists of all words that start with the same letter
     Parameters:
         message - a string
     Return Value:
         a dictionary containng letters as keys and lists of words as values

     '''
     letter_words = {}
     wordlist = message.split()
     for word in wordlist
        if word[0] in letter_words:
            lst = letter_words[word[0]]
            lst.append(word)
        else:
            letter_words[word[0]] = [word]

     return letter_words

def combine(d1, d2):
     '''
     Purpose:
     combine two dictionaries into one. If there is a situation where d1 and d2
     have the same key, add their values together in output dictionary
     Parameters:
         d1, d2- two dictionaries containing numeric values
     Return Value:
        a dictionary that is the combination of d1 and d2. It should have all
        k-v pairs from both d1 and d2

     '''
     out = {}
     for key in d1:
         if key in d2:
             out[key] = d1[key] + d2[key]
         else:
             out[key] = d1[key]
     for key in d2:
         if key not in out:
             out[key] = d2[key]
     return out

def pretty_print_dictionary_by_value(d):
     '''
     Purpose: print out the key-value pairs in the given dictionary,one per line,
      sorted by keys in ascending order
     Parameters:
         d - a dictionary with sortable keys
     Return Value:
        none

     '''
     keylist = list(d.keys())
     keylist.sort()
     for i in keylist:
         print(i, d[i])

def pretty_print_dictionary_by_value(d):
    valuelist = list(d.keys())
    valuelist.reverse()
    keylist = list(d.keys())
    


def main():
 #        f = open('')
 #        amessage = f.read()
        amessage = 'how many characters do we have?'
        result = alpha_char_count(amessage)
        print(result)
