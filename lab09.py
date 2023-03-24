def word_freq(fname):
    fp = open(fname)
    fp2 = fp.readlines()
    counts = {}
    for line in fp2:
        words = line.split()
        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1

    fp.close()
    return counts



morse_dictionary={'A': '.-', 'B': '-...', 'C': '-.-.',
'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--',
'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--',
'X': '-..-', 'Y': '-.--', 'Z': '--..', ' ': '/'}



def morse_code(message):
    morsemessage = ''
    upper = message.upper()

    for val in upper:
        if val in morse_dictionary:
            morsemessage = morsemessage + ' ' + morse_dictionary[val]
    print(morsemessage)



costs = {'Philadelphia':{'Chicago':227, 'Dallas':289},
         'Chicago':{'Philadelphia':227, 'Dallas':105, 'Las Vegas':56},
         'Dallas':{'Philadelphia':289, 'Houston':173, 'Chicago':105,
                   'Las Vegas':44, 'San Diego':303},
         'Houston':{'Dallas':173},
         'Las Vegas':{'Chicago':56, 'Dallas':44, 'San Diego':74,
                      'Los Angeles':44, 'San Francisco':56},
         'Los Angeles':{'Las Vegas':44, 'San Diego':157,
                        'San Francisco':111},
         'San Diego':{'Las Vegas':44, 'Los Angeles':157, 'Dallas':303},
         'San Francisco':{'Las Vegas':56, 'Los Angeles':111}}



total = costs['Chicago']['Las Vegas'] + costs['Las Vegas']['Dallas']


print(total)



def cheapest(costs, origin, destination):
    list = []
    for flights in costs[origin]:
        if flights == destination:
            direct_flight = costs[origin][destination]
            list.append(direct_flight)


        for j in costs[flights]:
            if j == destination:
                var = costs[origin][flights] + costs[flights][j]
                list.append(var)
        if list == []:
            return float('inf')
        else:
            return min(list)

    return min(list)
