candidate1 = [95, 93, 50, 91, 98, 90, 82]
candidate2 = [65, 75, 85, 95, 100, 100, 81]
candidate3 = [100, 100, 95, 85, 75, 65, 80]
candidate4 = [98, 70, 55, 61, 98, 90, 90]
candidate5 = [100, 95, 55, 61, 75, 95, 90]
candidate6 = [95, 90, 98, 88, 93, 95, 94]
candidate7 = [90, 80, 80, 100, 70, 75, 90]
candidate8 = [80, 83, 79, 83, 77, 77, 82]
candidate9 = [90, 100, 100, 98, 100, 99, 55]
candidate10 = [77, 82, 92, 100, 95, 92, 70]

def filter_average(cand):

    if cand[6] >= 85:
        return True
    else:
        return False


def filter_no_fail(cand):

    for x in range(len(cand) - 1):
        if cand[x] < 65:
            return False
    return True


def filter_4_high(cand):

    poss_cand = []

    for x in cand:
        if x >= 85:
            poss_cand.append(x)

    if len(poss_cand) >= 4:
        return True
    return False


def filter_averageCS(cand):

    total = 0
    for x in range(len(cand)-1):
        total += cand[x]

    avg = total / (len(cand) - 1)

    if avg >= 85:
        return True
    return False


applicants = [
    [100,  95,  80,  89,  61,  75,  83], # 0
    [ 95,  99,  92,  89,  94,  86,  88], # 1
    [ 75,  40,  55,  70,  85,  62,  90], # 2
    [ 85,  70,  99, 100,  81,  82,  91], # 3
    [ 86,  90,  88,  89,  91,  91,  90], # 4
    [ 64,  75,  92,  99,  95,  97,  60], # 5
  ]

def filter_all_nf(applicants_list):

    passing = []
    for x in applicants:
        if filter_no_fail(x) == True:
            passing.append(applicants.index(x))
    print(passing)

def aggregated_filter(applicants_list):
    passing = []
    for x in applicants:
        if filter_no_fail(x) == True:
            passing.append(applicants.index(x))
    print(passing)
