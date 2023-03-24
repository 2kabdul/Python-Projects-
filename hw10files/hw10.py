def collatz(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return collatz(n//2) + 1
    else:
        return collatz(3 * n + 1) + 1
def is_target(lines):
    no_decoy = "ACME"
    if len(lines) == 0:
        return True 
    elif "A" in lines[0] or "C" in lines[0] or "M" in lines[0] or "E" in lines[0]:
        # print('True')
        if len(lines) == 1:
            return True
        return is_target(lines[1:]) 
    else:
        return False 
