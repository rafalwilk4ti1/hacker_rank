from collections import Counter


def checkMagazine(magazine, note):
    answer = not(Counter(note) - Counter(magazine))
    if answer == True:
        print('Yes')
    else:
        print('No')