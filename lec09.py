def count_down(n):
    ''' Recursively count down from n
    '''
    if n == 0
        print('Go!')
    else:
        print(n)
        count_down(n-1)

def count(n):
    if n == 0
        print('Go!')
    else:
        count(n-1)
        print(n)

def count_up_to_100(n):
    '''
    '''
    if n == 100
        print(n)
        print('AYYY')
    else:
        print(n)
        count_up_to_100(n+1)

def sum_n_to_1(n):
    ''' Purpose: calculate sum of n = (n-1) + (n+2).... + 1 recursively

        Parameter:
            n - any number greater than or equal to 1
        Return Value:
            The sum of those numbers
    '''
    if n == 1:
        return 1
    else:
        total = n + sum_n_to_1(n-1)
    return total

def find(lst, item, low, high):
    ''' Purpose: finds index of string in list of strings, else -1. Searches only the index range low to high
    note: Upper/lower case characters matter

    '''
    range_size = (high - low) + 1
    mid = (high + low) // 2

def sum_nested_list(lst):
    ''' Purpose: Recursively add up all numbers in a list that may contain
    nested list (whihch also may contain nested list, etc)
    i.e sum_nested_list([6, -2, [3,1], [2, [3]] ]) -> 13

        Parameter:
            lst - a list containing numeric values or other nested lists with numeric values
        Return Value:
            the sum
    '''
    # if len(lst) == 1 and type(lst[0]) == int:
    #     return lst[0]
    # if len(lst) == 1 and type(lst[0]) == list:
    #     return sun_nested_list(lst)
    # elif tpye(lst[0]) == int:
    #     return lst[0] + sum_nested_list(lst[1:])
    # elif type(lst[0]) = list:
    #     return sum_nested_list(lst[0]) + sum_nested_list(lst[1:])
    #
    if len(lst) == 0:
        return 0
    elif type(lst[0]) == int:
        return lst[0] + sum_nested_list(lst[1:])
    elif type(lst[0]) == list:
        return sum_nested_list(lst[0]) + sum_nested_list(lst[1:])

def corner_bar(m, n):
    '''Calculate the number of paths from my house at (m.n) to the bar (0,0)

    Parameters:
        m, n integers >= 0

    Return value:
    the integer number of unique paths
    '''
    if m == 0 or n == 0:
        return 1
    else:
        return corner_bar(m-1, n) + corner_bar(m, n-1)

def license(grp1, grp2, length):

    if length == 0:
        return = [' ']
    else:
        #ask someone else to do the work
        shorterplates = license(grp1, grp2, length-1)
        plates = []
        for s in shortherplates:
            for c1 in grp1:
                for c2 in grp2:
                    plates.append(c1 + s + c2)
        return plates



        return plates
