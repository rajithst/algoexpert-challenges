def firstNonRepeatingCharacter(string):
    mem = {}
    for i in string:
        if i not in mem:
            mem[i] = 1
        else:
            mem[i] += 1
    for i in range(len(string)):
        if mem[string[i]] == 1:
            return i
    return -1
