def wordcount(fname):
    try:
        f = open(fname)
        read_file = f.read()
        w = read_file.split()

        z = len(w)
        f.close()
        print(z)
        return z
    except FileNotFoundError:

        print('Bad file name')
        z = -1
        return z
import random

def make_data(fname):
    f = open(fname,'w')

    for i in range(1000):
        f.write(str(i+1)+','+str(random.randint(-1000,1000))+'\n')

    f.close()

def read_data(fname):
    f = open(fname,'r')
    line = f.readline()
    min_num = 0
    max_num = 0
    while line:
        values = line.split(',')
        rand = int(values[1])
        if rand > max_num:
            max_num = rand
        elif rand < min_num:
            min_num = rand
        line = f.readline()
    print(max_num)
    print(min_num)
import statistics

def stocks(fname):
    f = open(fname,'r')
    f.readline()
    line = f.readlines()
    min_num = float('inf')
    max_num = 0
    list = []

    for number in line:
        values = number.split(',')
        rand = float(values[4])
        if rand > max_num:
            max_num = rand
        elif rand < min_num:
            min_num = rand
        list.append(float(values[4]))
    print(max_num)
    print(min_num)
    print(statistics.mean(list))
    print(statistics.median(list))
