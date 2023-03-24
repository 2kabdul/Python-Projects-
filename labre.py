def mystery_loop(lst):
    for i in range(len(lst)):
        lst[i] = lst[i] - 5
    return lst
def sum_list(vals):
    if vals == []:
        return []
    elif len(vals) == 1:
        return vals[0]
    else:
        return vals[0] + sum_list(vals[1:])
def reverse_string(st):
    if st == '':
        return ''
    else:
        return st[-1] + reverse_string(st[:-1])
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def double_reverse(str_list):
    if str_list == []:
        return []
    else:
        return [reverse_string(str_list[-1])] + double_reverse(str_list[:-1])

def deep_square(lst):
    if (lst) == []:
        return []
    # if len(lst) == 1 and type(lst[0]) == int:
    #     return [lst[0] * lst[0]]
    # elif len(lst) == 1 and type(lst[0]) == list:
    #     return [deep_square(lst[0])]
    elif type(lst[0]) == int:
        return [lst[0] * lst[0]] + deep_square(lst[1:])
    else:
        return [deep_square(lst[0])] + deep_square(lst[1:])
