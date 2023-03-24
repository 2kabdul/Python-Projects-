def closest(vals):
    '''
    Purpose:
    Parameter(s):
    Return Value:
    '''
    close = float('inf')
    for a in range(len(vals)):
        for b in range(len(vals)):
            if a != b:
                diff = abs(vals[a]- vals[b])
                if diff < close:
                    close = diff
    return close

def change_key(notes, up):
    '''
    Purpose:
    Parameter(s):
    Return Value:
    '''
    new_list = []
    scale = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    for i in notes:
        key = (scale.index(i) + up) % 12
        new_list.append(scale[key])
    return new_list

def avoid_sz(names_list):
    '''
    Purpose:
    Parameter(s):
    Return Value:
    '''
    contain_sz = []
    not_sz = []
    new_list = []

    for i in range(len(names_list)):
        if 's' in names_list[i] or 'S' in names_list[i] or 'z' in names_list[i] or 'Z' in names_list[i]:
            contain_sz.append(names_list[i])
        else:
            not_sz.append(names_list)
    if len(not_sz) != len(not_sz):
        print("Impossible: Too many s/z names")
        return []
